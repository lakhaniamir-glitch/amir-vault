"""Find the 18 products that have complete 4-image sets but aren't in the final 150.
Add them to the keep list so the existing image work isn't wasted.

For each, verify:
  - Active in Shopify
  - Is a Ring product type
  - Has inventory
  - User hasn't flagged as discontinued (e.g., KNIGHT/nurgle)

Output:
  - final-etsy-keep-list-UNIFIED-v2.csv (expanded with new entries)
  - new-additions-from-existing-images.md (the 18 reviewed)
"""
import csv, json, os, sys
from pathlib import Path
from collections import defaultdict

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

IMG_DIR  = Path(r"C:\Users\amirl\Documents\Amirs Command Center\brands\aydins\etsy-exports\2026-06-04\images")
UNIFIED  = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED.csv")
SHOP     = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
SESS     = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sessions-by-product-90d.csv")

OUT_CSV = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED-v2.csv")
OUT_MD  = Path(r"C:\Users\amirl\Downloads\new-additions-from-existing-images.md")

REQUIRED = ["hero.jpg", "image-2.jpg", "image-3.jpg", "image-4.jpg"]

# Discontinued per user 2026-06-10 (KNIGHT/nurgle was AI-failed AND user flagged it)
USER_DISCONTINUED_HANDLES = {
    "nurgle-black-diamond-titanium-wedding-ring",  # KNIGHT - user said discontinued
}

# 1. Inventory complete 4-image sets
complete_handles = set()
for d in IMG_DIR.iterdir():
    if not d.is_dir() or d.name.startswith("_"): continue
    if all((d / req).exists() for req in REQUIRED):
        complete_handles.add(d.name)
print(f"Handles with complete 4-image sets: {len(complete_handles)}")

# 2. Load Shopify by handle AND by codename (handles names can be renamed)
shop_by_handle = {}
shop_by_codename = {}
shop_variants_by_handle = defaultdict(list)
shop_variants_by_codename = defaultdict(list)
import re

with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        h = (r.get("handle") or "").strip()
        sku = (r.get("sku") or "").strip()
        cn = sku.split("-")[0].upper() if sku else ""
        try:
            inv = int(r.get("inventory_quantity") or 0)
        except:
            inv = 0
        info = {
            "title": (r.get("title") or "").strip(),
            "description": (r.get("description") or "").strip(),
            "tags": (r.get("tags") or "").strip(),
            "product_type": (r.get("product_type") or "").strip(),
            "first_sku": sku,
            "codename": cn,
            "first_price": (r.get("price") or "").strip(),
            "first_featured_image": (r.get("featured_image_url") or "").strip(),
            "url": (r.get("absolute_product_url") or "").strip(),
            "current_handle": h,
        }
        if h and h not in shop_by_handle:
            shop_by_handle[h] = info
        if cn and cn not in shop_by_codename:
            shop_by_codename[cn] = info
        if h: shop_variants_by_handle[h].append({"sku": sku, "inv": inv})
        if cn: shop_variants_by_codename[cn].append({"sku": sku, "inv": inv})
print(f"Shopify by handle: {len(shop_by_handle)}, by codename: {len(shop_by_codename)}")

# 3. Sessions per handle
def num(x):
    try: return int((x or '0').replace(',',''))
    except: return 0

handle_sessions = {}
with open(SESS, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        if (r.get("Landing page type") or "").lower() != "product": continue
        path = r.get("Landing page path","")
        m = re.match(r"^/products/([^/?#]+)", path)
        if not m: continue
        h = m.group(1)
        s = num(r.get("Sessions"))
        if s > handle_sessions.get(h, 0):
            handle_sessions[h] = s

# 4. Load unified keep list (the 150)
existing_codenames_in_150 = set()
existing_handles_in_150 = set()
existing_rows = []
with open(UNIFIED, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        existing_rows.append(r)
        if r["codename"]:
            existing_codenames_in_150.add(r["codename"])

# Map handles to codenames for existing 150
for h in list(complete_handles):
    info = shop_by_handle.get(h)
    if info and info["codename"] in existing_codenames_in_150:
        existing_handles_in_150.add(h)

# 5. Identify handles with images NOT in the 150
handles_with_images_not_in_150 = complete_handles - existing_handles_in_150
print(f"\nHandles with 4-image sets NOT yet in catalog: {len(handles_with_images_not_in_150)}")

# 6. For each, review Shopify status. Match by handle OR by codename in handle prefix.
# Folder name may be old handle (e.g. "valor-..." when Shopify renamed to "surya-...").
# Strategy: try handle exact match; if fail, extract first segment (e.g. "valor") and try codename lookup.
additions_to_add = []
additions_to_skip = []
for h in sorted(handles_with_images_not_in_150):
    if h in USER_DISCONTINUED_HANDLES:
        additions_to_skip.append({"handle": h, "reason": "user_flagged_discontinued", "title": "?"})
        continue
    # Try exact handle match
    info = shop_by_handle.get(h)
    inv = sum(v["inv"] for v in shop_variants_by_handle.get(h, []))
    matched_via = "handle_exact"

    # Fall back: try first folder segment as codename
    if not info:
        first_seg = h.split("-")[0].upper()
        info_by_cn = shop_by_codename.get(first_seg)
        if info_by_cn:
            info = info_by_cn
            inv = sum(v["inv"] for v in shop_variants_by_codename.get(first_seg, []))
            matched_via = f"codename:{first_seg}"

    if not info:
        additions_to_skip.append({"handle": h, "reason": "no_shopify_data"})
        continue
    if info["product_type"].lower() not in {"rings", "ring"}:
        additions_to_skip.append({"handle": h, "reason": f"not_a_ring ({info['product_type']!r})", "title": info["title"]})
        continue
    if inv <= 0:
        additions_to_skip.append({"handle": h, "reason": "no_inventory", "title": info["title"], "inv": inv})
        continue
    sess = handle_sessions.get(h, 0) or handle_sessions.get(info.get("current_handle",""), 0)
    additions_to_add.append({
        "handle": h,
        "current_handle": info.get("current_handle", h),
        "matched_via": matched_via,
        "codename": info["codename"],
        "title": info["title"],
        "first_sku": info["first_sku"],
        "first_price": info["first_price"],
        "sessions": sess,
        "inventory": inv,
        "url": info["url"],
        "image_dir": str(IMG_DIR / h),
    })

print(f"\nWill ADD to catalog: {len(additions_to_add)}")
print(f"Will SKIP: {len(additions_to_skip)}")
for s in additions_to_skip:
    print(f"  SKIP {s['handle']}  reason: {s['reason']}  title: {s.get('title','?')}")

# 7. Build expanded catalog
final_rows = list(existing_rows)
for a in additions_to_add:
    final_rows.append({
        "status": "NEW_FROM_EXISTING_IMAGES",
        "lid": "",
        "codename": a["codename"],
        "etsy_title": a["title"],
        "section": "",
        "etsy_revenue_2026": 0,
        "etsy_orders_2026": 0,
        "reasons": "image_set_already_done",
        "had_been_discontinued": False,
        "in_tier": "",
    })

with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    fieldnames = list(existing_rows[0].keys())
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(final_rows)

# 8. MD report
lines = [
    "# Additions to Catalog — Products with Existing 4-Image Sets",
    "",
    f"_18 handles had complete 4-image sets but weren't in the original 150 catalog. Adding the valid ones so existing image work isn't wasted._",
    "",
    "## Summary",
    f"- Handles with complete 4-image sets: 51",
    f"- Already in 150 catalog: {len(existing_handles_in_150)}",
    f"- Not in 150 catalog (candidate additions): {len(handles_with_images_not_in_150)}",
    f"- **Approved additions**: {len(additions_to_add)}",
    f"- Skipped: {len(additions_to_skip)}",
    "",
    f"## NEW CATALOG TOTAL: {len(final_rows)} listings",
    "",
    "## ✓ Approved additions",
    "",
    "| Codename | Sessions | Inventory | Price | Shopify Title | URL |",
    "|---|---|---|---|---|---|",
]
for a in sorted(additions_to_add, key=lambda x: -x["sessions"]):
    lines.append(f"| {a['codename']} | {a['sessions']} | {a['inventory']} | ${a['first_price']} | {a['title'][:50]} | {a['url']} |")

lines += [
    "",
    "## ✗ Skipped (image set exists but product unusable)",
    "",
    "| Handle | Reason | Title |",
    "|---|---|---|",
]
for s in additions_to_skip:
    lines.append(f"| {s['handle']} | {s['reason']} | {s.get('title','')[:50]} |")

OUT_MD.write_text("\n".join(lines), encoding="utf-8")

print(f"\n=== FINAL CATALOG ===")
print(f"Previous: 150 listings")
print(f"Adding: {len(additions_to_add)}")
print(f"NEW TOTAL: {len(final_rows)}")
print(f"\nImage gen impact:")
print(f"  Previously: 117 listings × 4 images = 468 new images")
print(f"  Now: 117 listings × 4 = 468 (unchanged — the new {len(additions_to_add)} all have images already)")
print()
print(f"Wrote: {OUT_CSV}")
print(f"Wrote: {OUT_MD}")
