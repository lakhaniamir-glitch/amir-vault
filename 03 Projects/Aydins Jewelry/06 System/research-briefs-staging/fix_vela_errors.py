"""Fix Vela errors:
1. Populate Var Quantity = 10 on every variant row (Aydins convention: 10 per size).
2. Populate Price ($169 default) on listings where Price was empty.
Atomic write."""
import csv, re
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")

DEFAULT_VAR_QTY = "10"
DEFAULT_PRICE = "169.00"

def width_based_price(sku):
    """Derive a price hint from SKU pattern {CODENAME}-{WIDTH}-{SIZE}."""
    m = re.match(r"^[A-Z][A-Z0-9]*-(\d+(?:\.\d+)?)-", sku.strip())
    if not m: return DEFAULT_PRICE
    width = float(m.group(1))
    if width <= 2: return "89.00"
    if width <= 4: return "109.00"
    if width <= 6: return "149.00"
    if width <= 7: return "159.00"
    if width <= 8: return "169.00"
    if width <= 10: return "189.00"
    return "199.00"

for fname in ["listings-corrected.csv", "new-shopify-listings.csv"]:
    path = ROOT / fname
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)
    print(f"\n=== {fname} ({len(rows)} rows) ===")

    # Detect first-row mode (UPDATE vs CREATE)
    has_lid = any((r.get("Listing ID") or "").strip() for r in rows[:200])

    # Pass 1: track first-row of each block + propagate Price
    current_block_first = None
    current_codename_price = DEFAULT_PRICE
    price_fixes = 0
    qty_fills = 0

    for r in rows:
        is_first = bool((r.get("Listing ID") or "").strip()) if has_lid else bool((r.get("Title") or "").strip())
        if is_first:
            current_block_first = r
            # Fix empty Price on this first row
            price = (r.get("Price") or "").strip()
            try:
                pval = float(price) if price else 0
            except: pval = 0
            if pval <= 0:
                sku = (r.get("Var SKU") or r.get("SKU") or "").strip()
                new_price = width_based_price(sku)
                r["Price"] = new_price
                current_codename_price = new_price
                price_fixes += 1
            else:
                current_codename_price = price

            # Fix empty master Quantity (helpful for Vela)
            qty = (r.get("Quantity") or "").strip()
            try: qval = float(qty) if qty else 0
            except: qval = 0
            if qval <= 0:
                r["Quantity"] = "10"

        # Set Var Quantity on EVERY row (Aydins convention)
        vqty = (r.get("Var Quantity") or "").strip()
        if not vqty:
            r["Var Quantity"] = DEFAULT_VAR_QTY
            qty_fills += 1

        # Ensure Var Visibility = "On" if blank
        vvis = (r.get("Var Visibility") or "").strip()
        if not vvis and (r.get("V1 Option") or r.get("V2 Option")):
            r["Var Visibility"] = "On"

    # Atomic write
    tmp = path.with_suffix(".csv.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)

    print(f"  price_fixes (filled missing Price): {price_fixes}")
    print(f"  qty_fills (populated Var Quantity=10): {qty_fills}")
    print(f"  total rows: {len(rows)}")
    print(f"  wrote to {path}")
