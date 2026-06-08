"""Replace the made-up width-based prices with actual Shopify prices.
For each of the 124 listings that originally had empty Price:
  1. Find codename from Var SKU
  2. Look up matching Shopify product
  3. Use the actual Shopify variant price"""
import csv, json, re
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
CSV = ROOT / "listings-corrected.csv"
ORIGINAL = ROOT / "listings-corrected.csv.pre-sku-fix-2026-06-08"
SHOPIFY = Path("/home/openclaw/.openclaw/agents/beta/shopify/products.jsonl")
OVERRIDES = Path("/tmp/manual_codename_overrides.json")

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

# Build Shopify codename -> {width: price} lookup
print("Building Shopify price index...")
codename_prices = {}  # {codename: {width: price}}
codename_min_price = {}  # {codename: min_price}

with open(SHOPIFY) as f:
    for line in f:
        try:
            p = json.loads(line)
        except: continue
        for v in p.get("variants", []):
            sku = v.get("sku", "")
            cn = extract_codename(sku)
            if not cn: continue
            o1 = (v.get("option1") or "").strip().lower()
            m = re.match(r"^(\d+(?:\.\d+)?)\s*mm?$", o1)
            width = m.group(1).rstrip("0").rstrip(".") if m and "." in m.group(1) else (m.group(1) if m else None)
            price = v.get("price")
            if not price: continue
            try: pf = float(price)
            except: continue
            if pf <= 0: continue
            if width is None: width = "8"  # default
            codename_prices.setdefault(cn, {})[width] = price
            cur_min = codename_min_price.get(cn)
            if cur_min is None or pf < float(cur_min):
                codename_min_price[cn] = price

print(f"  indexed {len(codename_prices)} codenames")

# Load overrides to map alias codenames
overrides = json.loads(OVERRIDES.read_text())
codename_aliases = {}  # {etsy_codename: [shopify_aliases]}
for cn, data in overrides.items():
    if cn.startswith("_"): continue
    if isinstance(data, dict) and "shopify_alias" in data:
        codename_aliases[cn.upper()] = [a.upper() for a in data["shopify_alias"]]

def lookup_price(codename, width=None):
    """Look up best Shopify price for codename (and optional width)."""
    candidates = [codename.upper()] + codename_aliases.get(codename.upper(), [])
    for c in candidates:
        if c in codename_prices:
            widths = codename_prices[c]
            if width and width in widths:
                return widths[width]
            return codename_min_price[c]
    return None

# Read original CSV to find listings that had empty Price
print("\nFinding listings that originally had empty Price...")
with open(ORIGINAL, encoding="utf-8") as f:
    orig_rows = list(csv.DictReader(f))

orig_empty_price_lids = set()
for r in orig_rows:
    lid = (r.get("Listing ID") or "").strip()
    if not lid: continue
    price = (r.get("Price") or "").strip()
    try: pval = float(price) if price else 0
    except: pval = 0
    if pval <= 0:
        orig_empty_price_lids.add(lid)
print(f"  {len(orig_empty_price_lids)} listings had empty Price originally")

# Read current CSV, fix prices for those listings
with open(CSV, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

fixed_count = 0
not_found_count = 0
not_found_samples = []

for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if not lid or lid not in orig_empty_price_lids:
        continue
    sku = (r.get("Var SKU") or r.get("SKU") or "").strip()
    cn = extract_codename(sku)
    # Get the V2 Option (width) from this row
    v2 = (r.get("V2 Option") or "").strip()
    m = re.match(r"^(\d+(?:\.\d+)?)\s*mm?$", v2.lower())
    width = m.group(1).rstrip("0").rstrip(".") if m and "." in m.group(1) else (m.group(1) if m else None)
    shopify_price = lookup_price(cn, width)
    if shopify_price:
        r["Price"] = str(shopify_price)
        fixed_count += 1
    else:
        not_found_count += 1
        if len(not_found_samples) < 8:
            not_found_samples.append((lid, cn, sku, r.get("Title","")[:60]))

# Atomic write
tmp = Path("/tmp/listings-corrected-pricefix.csv")
with open(tmp, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
tmp.replace(CSV)

print(f"\nfixed prices from Shopify: {fixed_count}")
print(f"Shopify price not found: {not_found_count}")
if not_found_samples:
    print("\nListings where Shopify price wasn't found (kept the placeholder):")
    for lid, cn, sku, title in not_found_samples:
        print(f"  L:{lid:12} cn={cn:20} sku={sku!r:20} title={title!r}")
