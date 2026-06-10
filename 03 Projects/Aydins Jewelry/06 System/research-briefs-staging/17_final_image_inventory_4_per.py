"""Precise image inventory for the final 150-listing catalog.
Standard: 4 images per Etsy listing (hero + image-2 + image-3 + image-4).

For each of the 150 listings:
  - HAVE: complete 4-image set in etsy-exports/2026-06-04/images/{handle}/
  - NEED: missing one or more of the 4 images
"""
import csv, json, os, sys, re
from pathlib import Path
from collections import defaultdict

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

IMG_DIR = Path(r"C:\Users\amirl\Documents\Amirs Command Center\brands\aydins\etsy-exports\2026-06-04\images")
KEEP = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
TIER = Path(r"C:\Users\amirl\Downloads\top100-final-tiered.csv")

OUT_CSV = Path(r"C:\Users\amirl\Downloads\image-inventory-150-4per.csv")
OUT_MD  = Path(r"C:\Users\amirl\Downloads\image-inventory-150-4per.md")

REQUIRED_FILES = ["hero.jpg", "image-2.jpg", "image-3.jpg", "image-4.jpg"]

def primary(sku):
    return (sku or "").split("-")[0].upper() if sku else ""

# Build Shopify codename → handle map
codename_to_handle = {}
handle_to_codename = {}
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = primary(sku)
        h = (r.get("handle") or "").strip()
        if cn and h and cn not in codename_to_handle:
            codename_to_handle[cn] = h
        if h and cn and h not in handle_to_codename:
            handle_to_codename[h] = cn
print(f"Shopify codename ↔ handle mappings: {len(codename_to_handle)}")

# Build handle → tier from top100-final-tiered.csv (more accurate than just codename)
tier_handle_lookup = {}
with open(TIER, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        h = r["handle"]
        if h:
            tier_handle_lookup[h] = {"tier": r["tier"], "codename": r["codename"]}

# Inventory existing 4-image sets
have_4_set = {}     # handle -> file count
partial_set = {}    # handle -> dict of which files present
for d in IMG_DIR.iterdir():
    if not d.is_dir() or d.name.startswith("_"): continue
    files_present = {req: (d / req).exists() for req in REQUIRED_FILES}
    n_present = sum(files_present.values())
    if n_present == 4:
        have_4_set[d.name] = 4
    elif n_present > 0:
        partial_set[d.name] = {"count": n_present, "files": files_present}

print(f"\nHandles with COMPLETE 4-image set: {len(have_4_set)}")
print(f"Handles with PARTIAL image set: {len(partial_set)}")
if partial_set:
    print("Partial samples:")
    for h, info in list(partial_set.items())[:3]:
        missing = [req for req, present in info['files'].items() if not present]
        print(f"  {h}  has {info['count']}/4  missing: {missing}")

# Load final 150 catalog
listings_150 = []
with open(KEEP, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        listings_150.append(r)
print(f"\nFinal 150 catalog loaded: {len(listings_150)}")

# Per-listing: HAVE / NEED
have_count = 0
need_count = 0
out_rows = []
for L in listings_150:
    cn = L["codename"]
    # Get handle from codename
    h = codename_to_handle.get(cn, "")
    if not h:
        h = "NO_HANDLE_MAPPING"

    if h in have_4_set:
        img_status = "HAVE_4"
        images_to_generate = 0
        have_count += 1
    elif h in partial_set:
        present = partial_set[h]["count"]
        img_status = f"HAVE_{present}_NEED_{4-present}"
        images_to_generate = 4 - present
        need_count += 1
    else:
        img_status = "NEED_4"
        images_to_generate = 4
        need_count += 1

    out_rows.append({
        "status": L["status"],
        "lid": L["lid"],
        "codename": cn,
        "shop_handle": h,
        "etsy_title": L["etsy_title"][:80],
        "section": L["section"],
        "image_status": img_status,
        "images_to_generate": images_to_generate,
        "etsy_revenue_2026": L.get("etsy_revenue_2026", 0),
    })

# Write CSV
with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
    w.writeheader()
    w.writerows(out_rows)

# Compute total images to generate
total_to_gen = sum(r["images_to_generate"] for r in out_rows)

# MD report
lines = [
    "# Image Inventory — Final 150 Etsy Catalog (4 Images per Listing)",
    "",
    f"_Standard: hero.jpg + image-2.jpg + image-3.jpg + image-4.jpg per product._",
    "",
    "## Summary",
    f"- Existing 4-image sets at `brands/aydins/etsy-exports/2026-06-04/images/`: **{len(have_4_set)}**",
    f"- Listings in final 150 catalog with complete 4-image set: **{have_count}**",
    f"- Listings needing image generation: **{need_count}**",
    f"- **Total new images to generate: {total_to_gen}**",
    "",
    "## Breakdown by listing group",
    "",
]

by_status = defaultdict(lambda: {"have_4": 0, "partial": 0, "need_4": 0, "to_gen": 0})
for r in out_rows:
    s = r["status"]
    if r["image_status"] == "HAVE_4":
        by_status[s]["have_4"] += 1
    elif r["image_status"] == "NEED_4":
        by_status[s]["need_4"] += 1
    else:
        by_status[s]["partial"] += 1
    by_status[s]["to_gen"] += r["images_to_generate"]

lines += ["| Listing group | Total | Have 4 | Partial | Need 4 | Images to generate |",
          "|---|---|---|---|---|---|"]
for s, d in by_status.items():
    total = d["have_4"] + d["partial"] + d["need_4"]
    lines.append(f"| {s} | {total} | {d['have_4']} | {d['partial']} | {d['need_4']} | {d['to_gen']} |")

lines += [
    "",
    "## Listings with COMPLETE 4-image set (ready to use)",
    "",
    "| Codename | LID | Title | Handle |",
    "|---|---|---|---|",
]
for r in out_rows:
    if r["image_status"] == "HAVE_4":
        lines.append(f"| {r['codename']} | {r['lid']} | {r['etsy_title'][:50]} | {r['shop_handle']} |")

lines += [
    "",
    f"## Listings NEEDING image generation ({need_count})",
    "",
    "| Status | Codename | LID | Image Status | New images | Title |",
    "|---|---|---|---|---|---|",
]
for r in out_rows:
    if "HAVE_4" not in r["image_status"]:
        lines.append(f"| {r['status']} | {r['codename']} | {r['lid']} | {r['image_status']} | {r['images_to_generate']} | {r['etsy_title'][:45]} |")

OUT_MD.write_text("\n".join(lines), encoding="utf-8")

print()
print("=== FINAL ANSWER ===")
print(f"Final catalog: 150 listings")
print(f"Listings with complete 4-image set: {have_count}")
print(f"Listings needing image generation: {need_count}")
print(f"Total new images to generate: {total_to_gen}")
print()
print(f"Wrote: {OUT_CSV}")
print(f"Wrote: {OUT_MD}")
