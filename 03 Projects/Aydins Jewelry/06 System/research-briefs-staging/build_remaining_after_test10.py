"""Build the remaining 425-listing CSV (FULL minus the TEST10 that already matched).
Also splits into safety batches in case Vela chokes on 11K-row file.
"""
import csv, re
from pathlib import Path

SRC = Path(r"C:\Users\amirl\Downloads\listings-corrected-FINAL.csv")
OUT_REMAINING = Path(r"C:\Users\amirl\Downloads\listings-update-mastersku-REMAINING-425.csv")
OUT_BATCH_DIR = Path(r"C:\Users\amirl\Downloads\mastersku-batches")
OUT_BATCH_DIR.mkdir(exist_ok=True)
BATCH_SIZE = 100  # safety batches if needed (5 batches of ~85)

# The 10 already imported via TEST10
TEST10_LIDS = {
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

def codename_from_var_sku(vs: str) -> str:
    return vs.strip().split("-")[0].upper() if vs else ""

with open(SRC, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

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

# Filter out TEST10
remaining_blocks = [b for b in blocks if b["lid"] not in TEST10_LIDS]
print(f"Total listings: {len(blocks)}")
print(f"TEST10 excluded: {len(blocks) - len(remaining_blocks)}")
print(f"Remaining to import: {len(remaining_blocks)}")

def process_block(block, sku_set_counter):
    block_rows = [dict(rows[i]) for i in block["rows"]]
    first = block_rows[0]
    codename = ""
    for r in block_rows:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            codename = codename_from_var_sku(vs)
            if codename:
                break
    if codename and not (first.get("SKU") or "").strip():
        first["SKU"] = codename
        sku_set_counter[0] += 1
    first["Title"] = strip_pollution((first.get("Title") or "").strip())
    return block_rows

# Write REMAINING-425 as one file
counter = [0]
all_remaining_rows = []
for block in remaining_blocks:
    all_remaining_rows.extend(process_block(block, counter))

with open(OUT_REMAINING, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(all_remaining_rows)

print(f"\nWrote: {OUT_REMAINING.name}")
print(f"  Listings: {len(remaining_blocks)}, rows: {len(all_remaining_rows)}, master SKUs set: {counter[0]}")

# Also write 100-per-batch safety files
n_batches = (len(remaining_blocks) + BATCH_SIZE - 1) // BATCH_SIZE
counter = [0]
for bi in range(n_batches):
    batch = remaining_blocks[bi * BATCH_SIZE : (bi + 1) * BATCH_SIZE]
    batch_rows = []
    for block in batch:
        batch_rows.extend(process_block(block, counter))
    out = OUT_BATCH_DIR / f"mastersku-batch-{bi+1:02d}-of-{n_batches:02d}.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        w.writeheader()
        w.writerows(batch_rows)
    print(f"  Safety batch {bi+1:02d}: {out.name} ({len(batch)} listings, {len(batch_rows)} rows)")
