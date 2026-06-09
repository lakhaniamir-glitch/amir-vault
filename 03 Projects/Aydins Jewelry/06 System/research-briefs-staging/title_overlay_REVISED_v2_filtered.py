"""Title overlay v2: revised playbook + skip non-tungsten-ring listings.

Skip rules:
  1. Section == "Fingerprint Dog Tags"
  2. Section == "Fingerprint Rings"  (keep original fingerprint branding)
  3. Category contains "Necklaces"
  4. Title contains "Dog Tag"

Outputs:
  - title-only-REVISED-FILTERED-TEST10.csv  (10 verified ring listings)
  - title-only-REVISED-FILTERED-FULL.csv    (502 rows, ~478 get updated, ~24 untouched)
"""
import csv
from pathlib import Path

FRESH = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
REVISED = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\etsy\2026-06-04-revision\listings-revised.csv")
OUT_TEST = Path(r"C:\Users\amirl\Downloads\title-only-REVISED-FILTERED-TEST10.csv")
OUT_FULL = Path(r"C:\Users\amirl\Downloads\title-only-REVISED-FILTERED-FULL.csv")

PREV_DONE = {
    "542735340", "522912537", "528037261", "1205810812", "1219759609",
    "575451015", "538386672", "817764707", "650116038", "526238869",
}

# Load eRank-researched titles
revised_titles = {}
with open(REVISED, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        lid = (r.get("Listing ID") or "").strip()
        title = (r.get("Title") or "").strip()
        if lid and title:
            revised_titles[lid] = title

with open(FRESH, encoding="utf-8-sig") as f:
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
        current = {
            "lid": lid,
            "section": (r.get("Section") or "").strip(),
            "category": (r.get("Category") or "").strip(),
            "current_title": (r.get("Title") or "").strip(),
            "rows": [i],
        }
    elif current is not None:
        current["rows"].append(i)
if current is not None:
    blocks.append(current)

def is_skipped(block):
    if block["section"] == "Fingerprint Dog Tags":
        return "section=FingerprintDogTags"
    if block["section"] == "Fingerprint Rings":
        return "section=FingerprintRings"
    if "Necklaces" in block["category"]:
        return "category=Necklaces"
    if "Dog Tag" in block["current_title"]:
        return "title contains DogTag"
    return None

# Tally
will_update, skipped = [], []
for b in blocks:
    if b["lid"] not in revised_titles:
        skipped.append((b, "not in revised playbook"))
    elif (reason := is_skipped(b)):
        skipped.append((b, reason))
    else:
        will_update.append(b)

print(f"Total listings in fresh export: {len(blocks)}")
print(f"  Will get title update: {len(will_update)}")
print(f"  Skipped: {len(skipped)}")
print()
print("=== Skipped breakdown ===")
from collections import Counter
reasons = Counter(s[1] for s in skipped)
for r, n in reasons.most_common():
    print(f"  {n:3d}  {r}")
print()
print("=== Listings being skipped (titles preserved as-is) ===")
for b, reason in skipped[:20]:
    print(f"  LID {b['lid']:<12}  [{reason}]  {b['current_title'][:80]!r}")
print()

def emit_block(block, out_rows, apply_title):
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(rows[row_i])
        if idx_pos == 0 and apply_title:
            r["Title"] = revised_titles[block["lid"]]
        out_rows.append(r)

# TEST10 — pick 10 verified ring listings not yet imported
test_blocks = [b for b in will_update if b["lid"] not in PREV_DONE][:10]
test_rows = []
for block in test_blocks:
    emit_block(block, test_rows, apply_title=True)

with open(OUT_TEST, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(test_rows)

# FULL — every listing from fresh export, title applied only where allowed
full_rows = []
for block in blocks:
    apply = (block["lid"] in revised_titles) and (is_skipped(block) is None)
    emit_block(block, full_rows, apply_title=apply)

with open(OUT_FULL, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(full_rows)

print(f"\nTEST: {OUT_TEST.name}  ({len(test_blocks)} listings, {len(test_rows)} rows)")
print(f"FULL: {OUT_FULL.name}  ({len(blocks)} listings, {len(full_rows)} rows)")
print(f"  Titles changed in FULL: {len(will_update)}")
print(f"  Titles preserved in FULL: {len(skipped)}")
print()
print("=== TEST10 side-by-side ===")
for block in test_blocks:
    first = rows[block["rows"][0]]
    print(f"LID {block['lid']}  [{block['section']!r}]")
    print(f"  OLD: {(first.get('Title','') or '')[:120]!r}")
    print(f"  NEW: {revised_titles[block['lid']][:120]!r}")
    print()
