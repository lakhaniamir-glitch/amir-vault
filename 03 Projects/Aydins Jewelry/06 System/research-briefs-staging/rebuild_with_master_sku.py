"""Rebuild Vela update CSV with master SKU populated on the first row of each listing block.
Theory: Vela's matcher uses master SKU as a fallback when Listing ID column is ignored.
Codename (e.g., MAUI, JDTR865) is unique per product = safe to use as master SKU.

Inputs:
  - C:\\Users\\amirl\\Downloads\\listings-corrected-FINAL.csv  (435-listing playbook)

Outputs:
  - C:\\Users\\amirl\\Downloads\\listings-update-mastersku-FULL.csv  (435 listings)
  - C:\\Users\\amirl\\Downloads\\listings-update-mastersku-TEST10.csv  (first 10 listings)

Import test10 first. If 10/10 match in Existing tab, run the full file.
"""
import csv, re
from pathlib import Path

SRC = Path(r"C:\Users\amirl\Downloads\listings-corrected-FINAL.csv")
OUT_FULL = Path(r"C:\Users\amirl\Downloads\listings-update-mastersku-FULL.csv")
OUT_TEST = Path(r"C:\Users\amirl\Downloads\listings-update-mastersku-TEST10.csv")

# Apply the SKU pollution strip same way build_playbook_json.py does, so titles stay clean
def strip_pollution(title: str) -> str:
    out = re.sub(
        r"(Tungsten Ring|Titanium Ring|Damascus Ring|Damascus Steel Ring|Tungsten Band|Titanium Band|Wedding Ring|Wedding Band)\s+([A-Z][a-zA-Z]*\d*)(\s*,)",
        r"\1\3",
        title,
    )
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out

def codename_from_var_sku(vs: str) -> str:
    """Extract codename from Var SKU like 'MAUI-4-2.5' -> 'MAUI', 'JDTR865-8-7' -> 'JDTR865', 'JDTR738' -> 'JDTR738'."""
    if not vs:
        return ""
    return vs.strip().split("-")[0].upper()

with open(SRC, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

print(f"Source rows: {len(rows)}")
print(f"Columns: {len(fieldnames)}")

# Group into listing blocks
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

print(f"Listings: {len(blocks)}")

# Process: on first row of each block, populate master SKU = codename derived from Var SKU
# Also strip SKU pollution from titles (same playbook hygiene)
out_rows = []
master_sku_set = 0
title_strips = 0

for block in blocks:
    block_rows = [dict(rows[i]) for i in block["rows"]]
    first = block_rows[0]

    # Find a codename from any Var SKU in the block (prefer first non-blank)
    codename = ""
    for r in block_rows:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            codename = codename_from_var_sku(vs)
            if codename:
                break

    # Populate master SKU on first row if blank and we have a codename
    cur_master = (first.get("SKU") or "").strip()
    if not cur_master and codename:
        first["SKU"] = codename
        master_sku_set += 1

    # Strip SKU pollution from title (first row only — variants don't have title)
    title = (first.get("Title") or "").strip()
    clean_title = strip_pollution(title)
    if title != clean_title:
        first["Title"] = clean_title
        title_strips += 1

    out_rows.extend(block_rows)

# Write full
with open(OUT_FULL, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(out_rows)

# Write test10
test_blocks = blocks[:10]
test_rows = []
for block in test_blocks:
    block_rows = [dict(rows[i]) for i in block["rows"]]
    first = block_rows[0]
    codename = ""
    for r in block_rows:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            codename = codename_from_var_sku(vs)
            if codename:
                break
    if codename:
        first["SKU"] = codename
    first["Title"] = strip_pollution((first.get("Title") or "").strip())
    test_rows.extend(block_rows)

with open(OUT_TEST, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(test_rows)

print()
print(f"FULL: {OUT_FULL.name}  ({len(blocks)} listings, {len(out_rows)} rows)")
print(f"TEST: {OUT_TEST.name}  ({len(test_blocks)} listings, {len(test_rows)} rows)")
print(f"Master SKUs populated: {master_sku_set}")
print(f"Titles SKU-stripped:   {title_strips}")
print()

# Show the test10 listing IDs + master SKU values for verification
print("=== TEST10 listings (Listing ID -> Master SKU -> Title prefix) ===")
for block, b in zip(test_blocks, test_blocks):
    first = dict(rows[block["rows"][0]])
    codename = ""
    for i in block["rows"]:
        vs = (rows[i].get("Var SKU") or "").strip()
        if vs:
            codename = codename_from_var_sku(vs)
            if codename:
                break
    title = strip_pollution((first.get("Title") or "").strip())
    print(f"  LID={block['lid']:<12} SKU={codename:<14} Title={title[:80]!r}")
