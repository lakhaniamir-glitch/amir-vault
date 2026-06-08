"""Final pass: drop any listings from listings-corrected.csv that don't have a Shopify match.
1. Improved codename extractor strips -CFP{N}, -VARIATION suffixes
2. Strict exact-codename matching (vendor-safe, no fuzzy)
3. Drop unmatched listing blocks entirely"""
import csv, json, re, shutil
from pathlib import Path
from collections import OrderedDict, Counter

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
SRC = ROOT / "listings-corrected.csv"
DROPPED_REPORT = ROOT / "scrapped-listings-2026-06-08.md"
INDEX = Path("/tmp/shopify_codename_width_size_index.json")

idx = json.loads(INDEX.read_text())
print(f"Shopify index codenames: {len(idx)}")

def extract_codename(sku):
    """Strip -CFP{N}, -VARIATION, -{digits}, -{decimal} suffixes.
    BUG-FIX 2026-06-08: iterate ALL strip patterns together so SKUs like
    'JDTR061-CFP1-4-5' reduce to 'JDTR061' (strip -5, -4, then -CFP1)."""
    if not sku: return ""
    s = sku.strip().upper()
    while True:
        prev = s
        s = re.sub(r"-CFP\d+$", "", s)
        s = re.sub(r"-VARIATION$", "", s)
        s = re.sub(r"-\d+(?:\.\d+)?$", "", s)
        if s == prev: break
    return s

# === Manual overrides ===
# Format: { etsy_codename: { "widths": { width_mm: [size_decimal,...] } } }
# Used when Shopify's own data is incomplete or when one Etsy listing maps to multiple Shopify SKU codes.
MANUAL_OVERRIDES_PATH = Path("/tmp/manual_codename_overrides.json")
manual_overrides = {}
if MANUAL_OVERRIDES_PATH.exists():
    try:
        raw = json.loads(MANUAL_OVERRIDES_PATH.read_text())
        for k, v in raw.items():
            if k.startswith("_"): continue
            if isinstance(v, dict) and "widths" in v:
                manual_overrides[k.upper()] = v["widths"]
        print(f"loaded manual overrides: {len(manual_overrides)} codenames")
    except Exception as e:
        print(f"manual overrides load failed: {e}")

def display_size(s):
    s = s.strip()
    if s.endswith(".5"): return f"{s.split('.')[0]} 1/2"
    if s.endswith(".25"): return f"{s.split('.')[0]} 1/4"
    if s.endswith(".75"): return f"{s.split('.')[0]} 3/4"
    return s

# Read source CSV
with open(SRC, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Group rows by listing block
listings = []
current = None
for i, r in enumerate(rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: listings.append(current)
        current = (i, [i])
    elif current is not None:
        current[1].append(i)
if current is not None: listings.append(current)

print(f"detected listing blocks: {len(listings)}")

# Metadata field copy list
metadata_fields = [
    "Listing ID", "Title", "Description", "Category", "Who made it?",
    "What is it?", "When was it made?", "Renewal options", "Product type",
    "Tags", "Materials", "Production partners", "Section", "Price",
    "Quantity", "SKU", "Shipping profile", "Weight", "Length", "Width",
    "Height", "Return policy", "Video 1",
    "Photo 1", "Photo 2", "Photo 3", "Photo 4", "Photo 5",
    "Photo 6", "Photo 7", "Photo 8", "Photo 9", "Photo 10"
]

new_rows = []
kept = 0
dropped = []
total_kept_variants = 0

for first_idx, block_indices in listings:
    first_row = rows[first_idx]
    var_sku = (first_row.get("Var SKU") or first_row.get("SKU") or "").strip()
    codename = extract_codename(var_sku)
    lid = first_row.get("Listing ID","").strip()
    title = first_row.get("Title","")[:80]

    # Resolve widths: manual override wins over Shopify index
    if codename in manual_overrides:
        shopify_widths = manual_overrides[codename]
    elif codename and codename in idx:
        shopify_widths = idx[codename]
    else:
        dropped.append({"lid": lid, "codename": codename, "raw_sku": var_sku, "title": title})
        continue
    valid_widths = sorted(shopify_widths.keys(), key=lambda x: float(x) if x.replace(".","").isdigit() else 99)
    all_sizes = set()
    for w in valid_widths:
        for s in shopify_widths[w]:
            if s != "ANY": all_sizes.add(s)
    all_sizes_sorted = sorted(all_sizes, key=lambda x: float(x) if x.replace(".","").isdigit() else 99)

    if not all_sizes_sorted:
        dropped.append({"lid": lid, "codename": codename, "raw_sku": var_sku, "title": title, "reason": "no_valid_sizes_in_shopify"})
        continue

    # Build metadata snapshot + adjust title width to Shopify-validated default (8mm preferred)
    metadata = {f: first_row.get(f, "") for f in metadata_fields}
    title_width = "8" if "8" in valid_widths else valid_widths[0]
    metadata["Title"] = re.sub(r",\s*\d+(?:\.\d+)?mm\s+", f", {title_width}mm ", metadata.get("Title",""), count=1)

    is_first = True
    for size_dec in all_sizes_sorted:
        for w in valid_widths:
            if size_dec not in shopify_widths[w]: continue
            row = OrderedDict({c: "" for c in fieldnames})
            if is_first:
                for f, v in metadata.items(): row[f] = v
                is_first = False
            row["Variation 1"] = "Ring size"
            row["V1 Option"] = display_size(size_dec)
            row["Variation 2"] = "Width"
            row["V2 Option"] = f"{w}mm"
            row["Var SKU"] = f"{codename}-{w}-{size_dec}"
            row["Var Visibility"] = "On"
            new_rows.append(row)
            total_kept_variants += 1

    kept += 1

# Atomic write
tmp = Path("/tmp/listings-corrected-final.csv")
with open(tmp, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(new_rows)
tmp.replace(SRC)

# Write dropped report
report_lines = [
    f"# Scrapped Etsy Listings — {len(dropped)} dropped, {kept} kept",
    "",
    f"**Date:** 2026-06-08",
    f"**Reason:** Listings without a Shopify codename match were removed from `listings-corrected.csv` per Amir's instruction.",
    "",
    f"## Summary",
    f"- Total listing blocks scanned: {len(listings)}",
    f"- Kept (Shopify-matched, variants pruned to Shopify reality): **{kept}**",
    f"- Dropped (no Shopify match): **{len(dropped)}**",
    f"- Total variant rows in final CSV: {total_kept_variants}",
    "",
    f"## Dropped listings",
    "| Listing ID | Codename | Raw SKU | Title (truncated) |",
    "|---|---|---|---|",
]
for d in dropped:
    report_lines.append(f"| {d.get('lid','')} | `{d.get('codename','')}` | `{d.get('raw_sku','')}` | {d.get('title','')} |")
DROPPED_REPORT.write_text("\n".join(report_lines))

print(f"\nkept listings: {kept}")
print(f"dropped listings: {len(dropped)}")
print(f"final variant row count: {total_kept_variants}")
print(f"dropped report: {DROPPED_REPORT}")
