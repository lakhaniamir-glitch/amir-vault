import csv

ORIGINAL = "/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv.pre-sku-fix-2026-06-08"
CURRENT = "/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv"

def get_lids(path):
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return set((r.get("Listing ID") or "").strip() for r in rows if (r.get("Listing ID") or "").strip())

orig_lids = get_lids(ORIGINAL)
curr_lids = get_lids(CURRENT)

print(f"Original CSV (Amir's Vela export) unique Listing IDs: {len(orig_lids)}")
print(f"Current CSV (my output) unique Listing IDs: {len(curr_lids)}")

in_both = orig_lids & curr_lids
only_orig = orig_lids - curr_lids
only_curr = curr_lids - orig_lids

print(f"\nIn BOTH (matching): {len(in_both)}")
print(f"In ORIGINAL only (these are the 51 I scrapped + any I lost): {len(only_orig)}")
print(f"In CURRENT only (these are IDs I CREATED/INVENTED - BUG!): {len(only_curr)}")

if only_curr:
    print(f"\n!!! BUG: {len(only_curr)} Listing IDs in my CSV that aren't in the original. Samples:")
    for lid in list(only_curr)[:15]:
        print(f"  {lid}")

# Cross-check: ID lengths
print(f"\nID format distribution in current CSV:")
from collections import Counter
lens = Counter(len(lid) for lid in curr_lids)
for L, n in sorted(lens.items()): print(f"  {L} digits: {n} IDs")
