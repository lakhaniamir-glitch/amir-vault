"""Show prices for a few key listings to sanity-check the Shopify lookup worked."""
import csv, re
from pathlib import Path
from collections import Counter

CSV = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv")
ORIGINAL = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv.pre-sku-fix-2026-06-08")

# Find ORIGINAL empty-price listings
with open(ORIGINAL, encoding="utf-8") as f:
    orig_rows = list(csv.DictReader(f))

empty_lids = set()
for r in orig_rows:
    lid = (r.get("Listing ID") or "").strip()
    if not lid: continue
    price = (r.get("Price") or "").strip()
    try: pval = float(price) if price else 0
    except: pval = 0
    if pval <= 0:
        empty_lids.add(lid)

# Now show the FIXED prices for those listings
with open(CSV, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("Sample of 12 fixed prices (was empty, now from Shopify):")
shown = 0
prices_seen = []
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid in empty_lids and shown < 12:
        sku = r.get("Var SKU","")
        title = r.get("Title","")[:55]
        price = r.get("Price","")
        prices_seen.append(price)
        print(f"  L:{lid:12} sku:{sku:25} ${price:8} {title}")
        shown += 1

# Also dump price distribution among the 124
all_fixed = []
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid in empty_lids:
        all_fixed.append(r.get("Price",""))
print(f"\nPrice distribution among the 124 fixed listings:")
dist = Counter(all_fixed)
for price, n in sorted(dist.items(), key=lambda x: -x[1]):
    print(f"  ${price:8}  {n}x")
