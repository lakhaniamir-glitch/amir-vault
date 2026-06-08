"""Diagnose: which listings have missing Price or zero stock?"""
import csv
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")

for fname in ["listings-corrected.csv", "new-shopify-listings.csv"]:
    path = ROOT / fname
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    has_lid = any((r.get("Listing ID") or "").strip() for r in rows[:200])
    print(f"\n========================================")
    print(f"=== {fname} ({len(rows)} rows) ===")
    print(f"========================================")
    # Track per-listing
    listings = []  # (first_row_idx, [row_indices])
    current = None
    for i, r in enumerate(rows):
        first_check = (r.get("Listing ID") or "").strip() if has_lid else (r.get("Title") or "").strip()
        if first_check:
            if current is not None: listings.append(current)
            current = (i, [i])
        elif current is not None:
            current[1].append(i)
    if current is not None: listings.append(current)
    print(f"detected listing blocks: {len(listings)}")

    # Check each listing
    bad_price = []
    bad_qty = []
    bad_var_visibility = []
    for first_idx, block in listings:
        first_row = rows[first_idx]
        price = (first_row.get("Price") or "").strip()
        qty = (first_row.get("Quantity") or "").strip()
        sku = (first_row.get("Var SKU") or first_row.get("SKU") or "").strip()
        lid = (first_row.get("Listing ID") or "").strip()
        title = (first_row.get("Title") or "")[:50]

        # Price check
        try:
            p = float(price) if price else 0
            if p == 0: bad_price.append((lid, sku, title))
        except: bad_price.append((lid, sku, title))

        # Quantity / stock check
        # Sum of all variants in this block - if all empty/zero, listing has no stock
        block_has_stock = False
        block_visibility_on = False
        for ridx in block:
            r = rows[ridx]
            vqty = (r.get("Var Quantity") or "").strip()
            vvis = (r.get("Var Visibility") or "").strip().lower()
            if vvis == "on": block_visibility_on = True
            try:
                vq = float(vqty) if vqty else 0
                if vq > 0: block_has_stock = True
            except: pass
        # If master qty > 0 that's the fallback
        try:
            if float(qty) > 0: block_has_stock = True
        except: pass

        if not block_has_stock:
            bad_qty.append((lid, sku, title, qty, "block_no_stock"))
        if block_visibility_on and not block_has_stock:
            bad_var_visibility.append((lid, sku, title))

    print(f"\nListings with missing/zero Price: {len(bad_price)}")
    for b in bad_price[:5]:
        print(f"  L:{b[0]:12} sku:{b[1]:25} title:{b[2]}")

    print(f"\nListings with no in-stock variant: {len(bad_qty)}")
    for b in bad_qty[:5]:
        print(f"  L:{b[0]:12} sku:{b[1]:25} qty:{b[3]!r:8} title:{b[2]}")

    # Detail: look at the Var Quantity column distribution
    var_qty_dist = Counter()
    var_vis_dist = Counter()
    master_qty_dist = Counter()
    for r in rows:
        vq = (r.get("Var Quantity") or "").strip()
        var_qty_dist[vq] += 1
        vv = (r.get("Var Visibility") or "").strip()
        var_vis_dist[vv] += 1
        mq = (r.get("Quantity") or "").strip()
        if mq: master_qty_dist[mq] += 1
    print(f"\nVar Quantity distribution (top): {dict(var_qty_dist.most_common(5))}")
    print(f"Var Visibility distribution: {dict(var_vis_dist.most_common(5))}")
    print(f"Master Quantity distribution (top, only non-empty): {dict(master_qty_dist.most_common(5))}")
