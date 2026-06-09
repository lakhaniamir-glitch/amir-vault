"""Split listings-update-comprehensive.csv into 5 batches of ~87 listings each.
Each batch is a complete, valid Vela CSV that can be imported separately."""
import csv
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
SRC = ROOT / "listings-update-comprehensive.csv"
BATCH_SIZE = 87  # listings per batch (5 batches total for 435 listings)

with open(SRC, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Group by listing block
blocks = []
current = None
for i, r in enumerate(rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: blocks.append(current)
        current = {"lid": lid, "rows": [i]}
    elif current is not None:
        current["rows"].append(i)
if current is not None: blocks.append(current)

print(f"Source: {len(blocks)} listings, {len(rows)} variant rows")

# Split into 5 batches
batches = [blocks[i:i+BATCH_SIZE] for i in range(0, len(blocks), BATCH_SIZE)]
print(f"Splitting into {len(batches)} batches of ~{BATCH_SIZE} listings each\n")

for bi, batch in enumerate(batches, 1):
    out = ROOT / f"listings-update-batch-{bi}-of-{len(batches)}.csv"
    batch_rows = []
    for blk in batch:
        for ri in blk["rows"]:
            batch_rows.append(rows[ri])
    with open(out, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(batch_rows)
    print(f"  Batch {bi}: {out.name}")
    print(f"    listings: {len(batch)}, rows: {len(batch_rows)}")
    print(f"    Listing IDs range: {batch[0]['lid']} ... {batch[-1]['lid']}")
