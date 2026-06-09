"""Build the FULL 435-listing CSV using the minimal-edit approach.
Base: Vela's original export (preserves Var SKU 'MAUI' format, original col order, all unchanged fields).
Overlays from playbook: Title, Description, Tags, Price.
Plus: ensure Var Quantity = 10 on every variant row (Vela 'at least one combination in stock' fix).
Plus: ensure master Quantity > 0.
Special: JDTR969 (Listing 4512019324) also gets Photo 1-5 overlaid (AI lifestyles)."""
import csv
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
ORIGINAL = ROOT / "listings-corrected.csv.pre-sku-fix-2026-06-08"  # Vela's original export
PLAYBOOK = ROOT / "listings-corrected.csv"                         # My modified version
OUT = ROOT / "listings-update-final.csv"

EDITABLE_COLS = {"Title", "Tags", "Description", "Price"}
PHOTO_COLS = [f"Photo {i+1}" for i in range(10)]
JDTR969_LID = "4512019324"

# Build playbook lookup: lid -> {col: value}
playbook_lookup = {}
with open(PLAYBOOK, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        lid = (r.get("Listing ID") or "").strip()
        if not lid: continue
        d = {c: r.get(c, "") for c in EDITABLE_COLS}
        if lid == JDTR969_LID:
            for c in PHOTO_COLS: d[c] = r.get(c, "")
        playbook_lookup[lid] = d

print(f"Playbook listings: {len(playbook_lookup)}")

# Read Vela's original export
with open(ORIGINAL, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)
print(f"Original Vela rows: {len(rows)}")

# Group by listing block
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

# Filter to ONLY the 435 listings in playbook
kept_blocks = [L for L in listings if L["lid"] in playbook_lookup]
print(f"Kept (in playbook): {len(kept_blocks)}")

# Apply overlays + Var Quantity + Quantity defaults
out_rows = []
var_qty_fills = 0
master_qty_fills = 0
for block in kept_blocks:
    lid = block["lid"]
    overlay = playbook_lookup[lid]
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(rows[row_i])

        if idx_pos == 0:
            # First row: overlay editable columns from playbook
            for c, v in overlay.items():
                if c in fieldnames and v:
                    r[c] = v
            # Ensure master Quantity is populated (>= 1)
            mq = (r.get("Quantity") or "").strip()
            try: mq_val = float(mq) if mq else 0
            except: mq_val = 0
            if mq_val <= 0:
                r["Quantity"] = "10"
                master_qty_fills += 1

        # All rows: ensure Var Quantity = 10 (Vela "in stock" requirement)
        vq = (r.get("Var Quantity") or "").strip()
        if not vq:
            r["Var Quantity"] = "10"
            var_qty_fills += 1

        out_rows.append(r)

# Write
with open(OUT, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(out_rows)

print(f"\nWrote: {OUT.name}")
print(f"  listings: {len(kept_blocks)}")
print(f"  total rows: {len(out_rows)}")
print(f"  master Quantity fills: {master_qty_fills}")
print(f"  Var Quantity fills: {var_qty_fills}")
print(f"  columns preserved: {len(fieldnames)} (matches Vela's export schema)")
