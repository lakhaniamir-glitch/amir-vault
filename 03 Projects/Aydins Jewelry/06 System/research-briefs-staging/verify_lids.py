import csv
with open("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

lids_populated = [r for r in rows if (r.get("Listing ID") or "").strip()]
unique_ids = set((r.get("Listing ID") or "").strip() for r in lids_populated)

print(f"total rows: {len(rows)}")
print(f"rows with Listing ID populated: {len(lids_populated)}")
print(f"unique Listing IDs: {len(unique_ids)}")
print(f"\nsample first 5 Listing IDs:")
for r in lids_populated[:5]:
    lid = r.get("Listing ID")
    title = r.get("Title", "")[:60]
    print(f"  {lid} title={title}")

# Now examine: do these IDs match Etsy URL pattern (10 digits)?
import re
valid_format = [lid for lid in unique_ids if re.match(r"^\d{8,13}$", lid)]
print(f"\nIDs matching Etsy 8-13 digit format: {len(valid_format)} / {len(unique_ids)}")
invalid = [lid for lid in unique_ids if not re.match(r"^\d{8,13}$", lid)]
if invalid:
    print(f"Invalid format IDs (first 10): {invalid[:10]}")
