"""Build a TEST CSV: 10 listings using the original Vela export as base,
with only Title / Tags / Description / Price columns overlaid from my playbook CSV.
All other columns (Var SKU, Var Quantity, Photos, etc.) preserved EXACTLY from Vela's original export."""
import csv
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
ORIGINAL = ROOT / "listings-corrected.csv.pre-sku-fix-2026-06-08"   # Vela's original export
PLAYBOOK = ROOT / "listings-corrected.csv"                          # My modified version
OUT = ROOT / "test10-minimal-edit.csv"

# Columns I want to overlay (only these get touched from playbook version)
EDITABLE_COLS = {"Title", "Tags", "Description", "Price"}

# Build playbook lookup by Listing ID -> {col: value} for editable cols
playbook_lookup = {}
with open(PLAYBOOK, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        lid = (r.get("Listing ID") or "").strip()
        if not lid: continue
        playbook_lookup[lid] = {c: r.get(c, "") for c in EDITABLE_COLS}

print(f"Playbook listings indexed: {len(playbook_lookup)}")

# Read original Vela export. Group by listing block. Pick 10 listings that ALSO exist in playbook.
with open(ORIGINAL, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)
print(f"Original Vela CSV cols ({len(fieldnames)}): {fieldnames[:5]}...")

# Walk listing blocks
listings = []
current = None
for i, r in enumerate(rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: listings.append(current)
        current = {"lid": lid, "rows": [i]}
    elif current is not None:
        current["rows"].append(i)
if current is not None: listings.append(current)
print(f"Original listing blocks: {len(listings)}")

# Pick first 10 listings that have a playbook entry
selected_lids = []
for L in listings:
    if L["lid"] in playbook_lookup:
        selected_lids.append(L["lid"])
        if len(selected_lids) >= 10:
            break
print(f"Selected for test: {selected_lids}")

# Filter rows to only these listings' blocks. Apply playbook overlay on the first row of each block.
selected_blocks = [L for L in listings if L["lid"] in selected_lids]
out_rows = []
for block in selected_blocks:
    lid = block["lid"]
    overlay = playbook_lookup[lid]
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(rows[row_i])  # copy
        if idx_pos == 0:
            # Apply ONLY editable column changes to the first row
            for c in EDITABLE_COLS:
                if c in fieldnames and c in overlay and overlay[c]:
                    r[c] = overlay[c]
        out_rows.append(r)

with open(OUT, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(out_rows)

print(f"\nWrote {OUT.name} with {len(out_rows)} variant rows across {len(selected_blocks)} listings.")
print(f"Editable columns overlaid from playbook: {sorted(EDITABLE_COLS)}")
print(f"All other columns preserved exactly from Vela's original export.")

# Show before/after for the first listing
print("\n=== BEFORE/AFTER for first listing in test ===")
first_lid = selected_lids[0]
orig_row = next(r for r in rows if (r.get("Listing ID") or "").strip() == first_lid)
new_row = out_rows[0]
for col in ("Listing ID", "Title", "Price", "Tags", "Var SKU"):
    if col == "Var SKU":
        # Show that VAR SKU was preserved (key matching field)
        print(f"  {col}:")
        print(f"    BEFORE (Vela export): {orig_row.get(col)!r}")
        print(f"    AFTER  (test CSV):    {new_row.get(col)!r}  (preserved)")
    else:
        print(f"  {col}:")
        print(f"    BEFORE (Vela export): {orig_row.get(col, '')[:90]!r}")
        print(f"    AFTER  (test CSV):    {new_row.get(col, '')[:90]!r}")
