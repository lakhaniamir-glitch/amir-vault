"""Cross-check: did my CSV preserve every Listing ID exactly from the original Vela export?
Also check for Excel-corruption artifacts (scientific notation, leading zeros stripped, etc.)."""
import csv, re

ORIGINAL = "/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv.pre-sku-fix-2026-06-08"
CURRENT = "/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv"

def first_rows_lids(path):
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows = list(reader)
    lids = []
    for r in rows:
        v = (r.get("Listing ID") or "").strip()
        if v: lids.append(v)
    return header, lids

orig_header, orig_lids = first_rows_lids(ORIGINAL)
curr_header, curr_lids = first_rows_lids(CURRENT)

print(f"=== HEADER CHECK ===")
print(f"Original header has 'Listing ID' at position: {orig_header.index('Listing ID') if 'Listing ID' in orig_header else 'MISSING'}")
print(f"Current header has 'Listing ID' at position: {curr_header.index('Listing ID') if 'Listing ID' in curr_header else 'MISSING'}")
print(f"Headers match exactly: {orig_header == curr_header}")
if orig_header != curr_header:
    extra_in_orig = set(orig_header) - set(curr_header)
    extra_in_curr = set(curr_header) - set(orig_header)
    if extra_in_orig: print(f"  Cols in original not in current: {extra_in_orig}")
    if extra_in_curr: print(f"  Cols in current not in original: {extra_in_curr}")

print(f"\n=== LISTING ID CHECK ===")
orig_set = set(orig_lids)
curr_set = set(curr_lids)
print(f"Original unique Listing IDs: {len(orig_set)}")
print(f"Current unique Listing IDs:  {len(curr_set)}")

invented = curr_set - orig_set
print(f"\nIDs in current that AREN'T in original (invented/changed): {len(invented)}")
for i in list(invented)[:10]: print(f"  {i}")

dropped = orig_set - curr_set
print(f"\nIDs in original that are MISSING from current (intentionally scrapped): {len(dropped)}")

# Check for Excel-corruption artifacts
print(f"\n=== EXCEL CORRUPTION CHECK ===")
sci_notation = [i for i in curr_lids if "E+" in i.upper() or "E-" in i.upper()]
print(f"IDs in scientific notation: {len(sci_notation)}")
if sci_notation: print(f"  samples: {sci_notation[:5]}")

floats = [i for i in curr_lids if "." in i]
print(f"IDs containing decimal point: {len(floats)}")
if floats: print(f"  samples: {floats[:5]}")

commas = [i for i in curr_lids if "," in i]
print(f"IDs containing commas: {len(commas)}")
if commas: print(f"  samples: {commas[:5]}")

# Raw byte check on first listing-id occurrence
with open(CURRENT, "rb") as f:
    raw = f.read(500)
print(f"\nFirst 200 bytes of CSV:")
print(repr(raw[:200]))
