"""Minimal-touch update: take a fresh Vela export, change ONLY the Title field for the 435
playbook listings. Everything else stays exactly as Vela exported it.

Inputs:
  - C:\\Users\\amirl\\Downloads\\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv  (fresh export)
  - C:\\Users\\amirl\\Downloads\\listings-corrected-FINAL.csv  (playbook for new titles)

Outputs:
  - C:\\Users\\amirl\\Downloads\\title-only-TEST10.csv  (first 10 listings test)
  - C:\\Users\\amirl\\Downloads\\title-only-FULL.csv  (all 502 listings — only playbook ones get title change)
"""
import csv, re
from pathlib import Path

FRESH = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
PLAYBOOK = Path(r"C:\Users\amirl\Downloads\listings-corrected-FINAL.csv")
OUT_TEST = Path(r"C:\Users\amirl\Downloads\title-only-TEST10.csv")
OUT_FULL = Path(r"C:\Users\amirl\Downloads\title-only-FULL.csv")

def strip_pollution(title: str) -> str:
    out = re.sub(
        r"(Tungsten Ring|Titanium Ring|Damascus Ring|Damascus Steel Ring|Tungsten Band|Titanium Band|Wedding Ring|Wedding Band)\s+([A-Z][a-zA-Z]*\d*)(\s*,)",
        r"\1\3",
        title,
    )
    return re.sub(r"\s{2,}", " ", out).strip()

# Build playbook lookup: Listing ID -> new title
playbook_titles = {}
with open(PLAYBOOK, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        lid = (r.get("Listing ID") or "").strip()
        title = (r.get("Title") or "").strip()
        if lid and title:
            playbook_titles[lid] = strip_pollution(title)

print(f"Playbook listings: {len(playbook_titles)}")

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

print(f"Fresh export listings: {len(blocks)}")

# Count overlap with playbook
in_playbook = [b for b in blocks if b["lid"] in playbook_titles]
not_in_playbook = [b for b in blocks if b["lid"] not in playbook_titles]
print(f"  In playbook (will get title update): {len(in_playbook)}")
print(f"  Not in playbook (untouched): {len(not_in_playbook)}")

# Pick TEST10 — first 10 in-playbook listings (skipping those already imported)
ALREADY_DONE = {
    "542735340", "522912537", "528037261", "1205810812", "1219759609",
    "575451015", "538386672", "817764707", "650116038", "526238869",
}
test10_candidates = [b for b in in_playbook if b["lid"] not in ALREADY_DONE][:10]
test10_lids = set(b["lid"] for b in test10_candidates)

def emit_listing(block, out_rows, change_title=True):
    """Emit all rows of a listing block, optionally updating ONLY the Title on first row."""
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(rows[row_i])  # exact copy preserving every column
        if idx_pos == 0 and change_title and block["lid"] in playbook_titles:
            r["Title"] = playbook_titles[block["lid"]]
        out_rows.append(r)

# Build TEST10 — only 10 listings, others omitted
test_rows = []
for block in test10_candidates:
    emit_listing(block, test_rows, change_title=True)

with open(OUT_TEST, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(test_rows)

# Build FULL — every listing from fresh export, title updated only for playbook listings
full_rows = []
for block in blocks:
    emit_listing(block, full_rows, change_title=True)

with open(OUT_FULL, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(full_rows)

print()
print(f"TEST: {OUT_TEST.name}  ({len(test10_candidates)} listings, {len(test_rows)} rows)")
print(f"FULL: {OUT_FULL.name}  ({len(blocks)} listings, {len(full_rows)} rows)")
print()
print("=== TEST10 listings (LID -> OLD title -> NEW title) ===")
for block in test10_candidates:
    first = rows[block["rows"][0]]
    old = (first.get("Title") or "").strip()
    new = playbook_titles[block["lid"]]
    print(f"  LID={block['lid']}")
    print(f"    OLD: {old[:90]!r}")
    print(f"    NEW: {new[:90]!r}")
