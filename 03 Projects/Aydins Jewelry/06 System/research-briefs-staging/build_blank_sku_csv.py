"""User's plan: rebuild CSV with new Title/Desc/Tags/Price but leave SKU columns BLANK entirely.
Theory: when SKU is blank, Vela's matcher falls back to Listing ID for identification.

Outputs:
  - C:\\Users\\amirl\\Downloads\\listings-update-blanksku-TEST10.csv  (10 listings test)
  - C:\\Users\\amirl\\Downloads\\listings-update-blanksku-FULL-MINUS-TEST10.csv  (the other 425)
"""
import csv, re
from pathlib import Path

SRC = Path(r"C:\Users\amirl\Downloads\listings-corrected-FINAL.csv")
OUT_TEST = Path(r"C:\Users\amirl\Downloads\listings-update-blanksku-TEST10.csv")
OUT_FULL = Path(r"C:\Users\amirl\Downloads\listings-update-blanksku-FULL-MINUS-TEST10.csv")

# Use DIFFERENT 10 from the master-SKU TEST10 (those are already imported).
# Pick 10 listings that haven't been touched yet.
TEST10_PREV_LIDS = {
    "542735340", "522912537", "528037261", "1205810812", "1219759609",
    "575451015", "538386672", "817764707", "650116038", "526238869",
}

def strip_pollution(title: str) -> str:
    out = re.sub(
        r"(Tungsten Ring|Titanium Ring|Damascus Ring|Damascus Steel Ring|Tungsten Band|Titanium Band|Wedding Ring|Wedding Band)\s+([A-Z][a-zA-Z]*\d*)(\s*,)",
        r"\1\3",
        title,
    )
    return re.sub(r"\s{2,}", " ", out).strip()

with open(SRC, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Group into blocks
blocks = []
current = None
for i, r in enumerate(rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None:
            blocks.append(current)
        current = {"lid": lid, "rows": [i]}
    elif current is not None:
        current["rows"].append(i)
if current is not None:
    blocks.append(current)

# Exclude prev TEST10 from the remaining set
remaining = [b for b in blocks if b["lid"] not in TEST10_PREV_LIDS]
new_test10 = remaining[:10]
full_minus = remaining[10:]
print(f"Total listings: {len(blocks)}")
print(f"Prev TEST10 (already imported): {len(blocks) - len(remaining)}")
print(f"New TEST10 (blank-sku test): {len(new_test10)}")
print(f"Remaining FULL after new TEST10: {len(full_minus)}")

def process_block_blank_sku(block):
    out_rows = []
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(rows[row_i])
        if idx_pos == 0:
            # Clean title only
            r["Title"] = strip_pollution((r.get("Title") or "").strip())
        # CRITICAL: blank out BOTH SKU columns on every row
        r["SKU"] = ""
        r["Var SKU"] = ""
        out_rows.append(r)
    return out_rows

# Write new TEST10
test_rows = []
for block in new_test10:
    test_rows.extend(process_block_blank_sku(block))

with open(OUT_TEST, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(test_rows)

# Write FULL-MINUS-TEST10 (415 listings)
full_rows = []
for block in full_minus:
    full_rows.extend(process_block_blank_sku(block))

with open(OUT_FULL, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(full_rows)

print()
print(f"TEST: {OUT_TEST.name}  ({len(new_test10)} listings, {len(test_rows)} rows)")
print(f"FULL: {OUT_FULL.name}  ({len(full_minus)} listings, {len(full_rows)} rows)")
print()
print("=== NEW TEST10 listings ===")
for block in new_test10:
    first = rows[block["rows"][0]]
    title = strip_pollution((first.get("Title") or "").strip())
    print(f"  LID={block['lid']:<12}  Title={title[:80]!r}")
