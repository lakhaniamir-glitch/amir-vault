"""Build a comprehensive Vela update CSV: includes ALL playbook updates AND the SKU format fix.
Base: Vela's original export (preserves column structure + Listing IDs)
Overlays from playbook: Title, Description, Tags, Price
Additional: Var SKU format fix (MAUI -> MAUI-4-2.5 per variant), Var Quantity=10 per Aydins convention.
Special: JDTR969 gets new AI Photo URLs."""
import csv, re
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
ORIGINAL = ROOT / "listings-corrected.csv.pre-sku-fix-2026-06-08"
PLAYBOOK = ROOT / "listings-corrected.csv"
OUT_FULL = ROOT / "listings-update-comprehensive.csv"
OUT_TEST10 = ROOT / "test10-comprehensive.csv"

EDITABLE_COLS = {"Title", "Tags", "Description", "Price"}
PHOTO_COLS = [f"Photo {i+1}" for i in range(10)]
JDTR969_LID = "4512019324"

# Helpers for SKU format fix
def extract_codename(sku):
    if not sku: return ""
    s = sku.strip().upper()
    color_finish = r"-(BLACK|SILVER|GOLD|WHITE|ROSE|POLISHED|BRUSHED|MATTE|SATIN|YELLOW)$"
    while True:
        prev = s
        s = re.sub(r"-CFP\d+$", "", s)
        s = re.sub(r"-VARIATION$", "", s)
        s = re.sub(color_finish, "", s)
        s = re.sub(r"-\d+(?:\.\d+)?$", "", s)
        if s == prev: break
    return s

def norm_width(s):
    if not s: return None
    m = re.match(r"^(\d+(?:\.\d+)?)\s*mm?$", s.lower().strip()) or re.match(r"^(\d+(?:\.\d+)?)$", s.strip())
    if not m: return None
    v = m.group(1)
    return v.rstrip("0").rstrip(".") if "." in v else v

def norm_size(s):
    if not s: return None
    s = s.strip()
    m = re.match(r"^(\d+)\s+1/2$", s)
    if m: return f"{int(m.group(1))}.5"
    m = re.match(r"^(\d+)\s+1/4$", s)
    if m: return f"{int(m.group(1))}.25"
    m = re.match(r"^(\d+)\s+3/4$", s)
    if m: return f"{int(m.group(1))}.75"
    m = re.match(r"^(\d+(?:\.\d+)?)$", s)
    return m.group(1) if m else None

# Build playbook lookup
playbook_lookup = {}
with open(PLAYBOOK, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        lid = (r.get("Listing ID") or "").strip()
        if not lid: continue
        d = {c: r.get(c, "") for c in EDITABLE_COLS}
        if lid == JDTR969_LID:
            for c in PHOTO_COLS: d[c] = r.get(c, "")
        playbook_lookup[lid] = d

# Read original Vela export
with open(ORIGINAL, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Group by listing block
listings_blocks = []
current = None
for i, r in enumerate(rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: listings_blocks.append(current)
        current = {"lid": lid, "rows": [i]}
    elif current is not None:
        current["rows"].append(i)
if current is not None: listings_blocks.append(current)

# Filter to playbook-kept listings
kept_blocks = [L for L in listings_blocks if L["lid"] in playbook_lookup]

# Process each listing block
def process_block(block, base_rows, current_v1_label="", current_v2_label="", current_codename=""):
    overlay = playbook_lookup[block["lid"]]
    out = []
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(base_rows[row_i])

        # Track variation labels (only set on first row of each block typically)
        v1l = (r.get("Variation 1") or current_v1_label).strip()
        v2l = (r.get("Variation 2") or current_v2_label).strip()
        if v1l: current_v1_label = v1l
        if v2l: current_v2_label = v2l

        # Track codename (only set on first row's Var SKU)
        if idx_pos == 0:
            current_codename = extract_codename(r.get("Var SKU") or r.get("SKU") or "")

        if idx_pos == 0:
            # First row: overlay editable columns
            for c, v in overlay.items():
                if c in fieldnames and v:
                    r[c] = v
            # Master Quantity default
            mq = (r.get("Quantity") or "").strip()
            try: mq_val = float(mq) if mq else 0
            except: mq_val = 0
            if mq_val <= 0:
                r["Quantity"] = "10"

        # All rows: Var Quantity = 10
        if not (r.get("Var Quantity") or "").strip():
            r["Var Quantity"] = "10"

        # All rows: rewrite Var SKU to CODENAME-W-S format
        v1 = (r.get("V1 Option") or "").strip()
        v2 = (r.get("V2 Option") or "").strip()
        width_v = None; size_v = None
        if current_v1_label.lower() == "width":
            width_v = norm_width(v1)
        elif current_v1_label.lower() in ("ring size", "size"):
            size_v = norm_size(v1)
        if current_v2_label.lower() == "width":
            width_v = norm_width(v2) or width_v
        elif current_v2_label.lower() in ("ring size", "size"):
            size_v = norm_size(v2) or size_v
        # Per Amir's 8mm default rule
        if width_v is None and size_v is not None:
            width_v = "8"

        if current_codename:
            parts = [current_codename]
            if width_v is not None: parts.append(width_v)
            if size_v is not None: parts.append(size_v)
            r["Var SKU"] = "-".join(parts)

        out.append(r)
    return out

# Build full CSV
out_rows_full = []
for block in kept_blocks:
    out_rows_full.extend(process_block(block, rows))

with open(OUT_FULL, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(out_rows_full)
print(f"FULL: {OUT_FULL.name}: {len(kept_blocks)} listings, {len(out_rows_full)} rows")

# Build test 10 CSV (first 10 from same processed set)
selected_lids = [L["lid"] for L in kept_blocks[:10]]
test_blocks = [L for L in kept_blocks if L["lid"] in selected_lids]
out_rows_test = []
for block in test_blocks:
    out_rows_test.extend(process_block(block, rows))

with open(OUT_TEST10, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(out_rows_test)
print(f"TEST10: {OUT_TEST10.name}: {len(test_blocks)} listings, {len(out_rows_test)} rows")

# Verify SKU format on a sample
print("\n=== SAMPLE: MAUI first 5 variants AFTER SKU fix ===")
maui_block = next((L for L in kept_blocks if L["lid"] == "542735340"), None)
if maui_block:
    maui_rows = [r for r in out_rows_full if r.get("Listing ID") == "542735340" or (out_rows_full.index(r) >= out_rows_full.index([r2 for r2 in out_rows_full if r2.get("Listing ID") == "542735340"][0]) and out_rows_full.index(r) < out_rows_full.index([r2 for r2 in out_rows_full if r2.get("Listing ID") == "542735340"][0]) + len(maui_block["rows"]))]
    # Simpler: just collect 5 MAUI rows
    count = 0
    for r in out_rows_full:
        sku = r.get("Var SKU","")
        if sku.startswith("MAUI"):
            print(f"  V1={r.get('V1 Option')!r:8} V2={r.get('V2 Option')!r:8} Var SKU={sku!r}")
            count += 1
            if count >= 5: break
