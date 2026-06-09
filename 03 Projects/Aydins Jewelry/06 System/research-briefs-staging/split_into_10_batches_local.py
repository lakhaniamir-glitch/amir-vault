"""Local splitter: takes listings-update-comprehensive.csv and produces 44 batches of 10 listings.

USAGE:
  1. Pull listings-update-comprehensive.csv from VPS to C:\\Users\\amirl\\Downloads\\
     (or update SRC path below to wherever you have it)
  2. Run:  python split_into_10_batches_local.py
  3. Batch files land in C:\\Users\\amirl\\Downloads\\vela-batches\\
     named: listings-update-10batch-01-of-44.csv ... -44-of-44.csv

WHY 10 PER BATCH:
  test10-comprehensive (10 listings) matched 10/10 in Vela. Proven safe size.
  25-listing batches were unreliable (worked once, failed once at 3/25).

PER-BATCH IMPORT PROTOCOL IN VELA:
  1. Close Vela window completely (not minimize, fully close)
  2. Reopen Vela -> sync with Etsy
  3. Import next batch CSV
  4. Verify 10/10 land in Existing tab. If <10, STOP and report which IDs failed.
  5. Select all 10 -> Merge -> Publish
  6. Repeat for next batch
"""
import csv
from pathlib import Path

SRC = Path(r"C:\Users\amirl\Downloads\listings-update-comprehensive.csv")
OUT_DIR = Path(r"C:\Users\amirl\Downloads\vela-batches")
BATCH_SIZE = 10

if not SRC.exists():
    print(f"ERROR: source CSV not found at {SRC}")
    print("Pull listings-update-comprehensive.csv from the VPS to that path, then re-run.")
    raise SystemExit(1)

OUT_DIR.mkdir(parents=True, exist_ok=True)

with open(SRC, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Group by listing block (first row of each block has a Listing ID; variant rows do not)
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

print(f"Source: {len(blocks)} listings, {len(rows)} variant rows")

batches = [blocks[i:i + BATCH_SIZE] for i in range(0, len(blocks), BATCH_SIZE)]
total = len(batches)
print(f"Splitting into {total} batches of {BATCH_SIZE} listings each\n")

# Optional: write a per-batch listing-ID manifest for quick verification in Vela
manifest_lines = ["batch,listing_ids,rows"]

for bi, batch in enumerate(batches, 1):
    out = OUT_DIR / f"listings-update-10batch-{bi:02d}-of-{total:02d}.csv"
    batch_rows = []
    for blk in batch:
        for ri in blk["rows"]:
            batch_rows.append(rows[ri])

    with open(out, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_MINIMAL,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(batch_rows)

    ids = "|".join(blk["lid"] for blk in batch)
    manifest_lines.append(f"{bi:02d},{ids},{len(batch_rows)}")
    print(f"  Batch {bi:02d}: {out.name}  ({len(batch)} listings, {len(batch_rows)} rows)")

manifest_path = OUT_DIR / "batch-manifest.csv"
manifest_path.write_text("\n".join(manifest_lines), encoding="utf-8")
print(f"\nManifest: {manifest_path}")
print(f"\nDONE. {total} batch files ready in {OUT_DIR}")
