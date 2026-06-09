"""Correct title overlay: use listings-revised.csv (the actual eRank playbook) as title source.

Inputs:
  - FRESH:    C:\\Users\\amirl\\Downloads\\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv  (current Etsy state)
  - PLAYBOOK: 03 Projects\\Aydins Jewelry\\etsy\\2026-06-04-revision\\listings-revised.csv  (the eRank-researched titles)

Outputs:
  - C:\\Users\\amirl\\Downloads\\title-only-REVISED-TEST10.csv  (first 10 for testing)
  - C:\\Users\\amirl\\Downloads\\title-only-REVISED-FULL.csv    (all 501)
"""
import csv
from pathlib import Path

FRESH = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
REVISED = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\etsy\2026-06-04-revision\listings-revised.csv")
OUT_TEST = Path(r"C:\Users\amirl\Downloads\title-only-REVISED-TEST10.csv")
OUT_FULL = Path(r"C:\Users\amirl\Downloads\title-only-REVISED-FULL.csv")

# Build playbook lookup: lid -> eRank title (NO stripping; use as-is)
revised_titles = {}
with open(REVISED, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        lid = (r.get("Listing ID") or "").strip()
        title = (r.get("Title") or "").strip()
        if lid and title:
            revised_titles[lid] = title

print(f"Revised playbook titles: {len(revised_titles)}")

# Read fresh export
with open(FRESH, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

print(f"Fresh export rows: {len(rows)}")
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

print(f"Fresh listings: {len(blocks)}")
overlap = sum(1 for b in blocks if b["lid"] in revised_titles)
print(f"  Will get title update: {overlap}")
print(f"  Will be left untouched (not in revised playbook): {len(blocks) - overlap}")

def emit_block(block, out_rows, apply_title):
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(rows[row_i])
        if idx_pos == 0 and apply_title and block["lid"] in revised_titles:
            r["Title"] = revised_titles[block["lid"]]
        out_rows.append(r)

# TEST10 — first 10 listings in the fresh export that overlap with revised playbook,
# excluding the 10 from earlier mastersku TEST10 to avoid conflict
PREV_DONE = {
    "542735340", "522912537", "528037261", "1205810812", "1219759609",
    "575451015", "538386672", "817764707", "650116038", "526238869",
}
test_blocks = [b for b in blocks if b["lid"] in revised_titles and b["lid"] not in PREV_DONE][:10]

test_rows = []
for block in test_blocks:
    emit_block(block, test_rows, apply_title=True)

with open(OUT_TEST, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(test_rows)

# FULL — all 502 listings from fresh export, eRank title applied where playbook has one
full_rows = []
for block in blocks:
    emit_block(block, full_rows, apply_title=True)

with open(OUT_FULL, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(full_rows)

print()
print(f"TEST: {OUT_TEST.name}  ({len(test_blocks)} listings, {len(test_rows)} rows)")
print(f"FULL: {OUT_FULL.name}  ({len(blocks)} listings, {len(full_rows)} rows)")
print()
print("=== TEST10: side-by-side (CURRENT vs eRank NEW) ===")
for block in test_blocks:
    first = rows[block["rows"][0]]
    old = (first.get("Title") or "").strip()
    new = revised_titles[block["lid"]]
    print(f"LID {block['lid']}")
    print(f"  OLD (Etsy now):  {old[:120]!r}")
    print(f"  NEW (eRank):     {new[:120]!r}")
    print()
