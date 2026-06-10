"""Build the FINAL unified Etsy keep list combining all revenue/traffic signals.

Sources:
  1. etsy-revenue-keep-list.csv      → 38 LIDs with confirmed 2026 YTD Etsy revenue
  2. etsy-keep-list.csv              → 24 LIDs in top 100 Shopify revenue (the original keepers)
  3. top100-final-tiered.csv         → Tier A (50 codenames with existing AI image) + Tier B (50 by sessions)
  4. listings-to-deactivate-in-vela.txt → 51 discontinued LIDs (FLAG if any overlap with revenue)

Output:
  - final-etsy-keep-list-UNIFIED.csv  (single source of truth)
  - final-etsy-catalog-summary.md     (readable report)
"""
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

REV  = Path(r"C:\Users\amirl\Downloads\etsy-revenue-keep-list.csv")
KEEP = Path(r"C:\Users\amirl\Downloads\etsy-keep-list.csv")
TIER = Path(r"C:\Users\amirl\Downloads\top100-final-tiered.csv")
SCRAP_TXT = Path(r"C:\Users\amirl\Documents\Amirs Command Center\brands\aydins\etsy-exports\2026-06-04\listings-to-deactivate-in-vela.txt")
ETSY = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv")
XREF = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v4.json")

OUT_CSV = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED.csv")
OUT_MD  = Path(r"C:\Users\amirl\Downloads\final-etsy-catalog-summary.md")

# Load all sources
revenue_lids = {}  # lid -> {revenue, orders, etsy_title, section}
for r in csv.DictReader(open(REV, encoding="utf-8-sig")):
    revenue_lids[r["lid"]] = {
        "revenue": float(r["total_revenue_2026"]),
        "orders": int(r["total_orders"]),
        "views": int(r["total_views"]),
        "favorites": int(r["total_favorites"]),
        "etsy_title": r["etsy_title"],
        "section": r["section"],
    }
print(f"Revenue LIDs (2026 YTD): {len(revenue_lids)}")

keeper_lids = {}  # lid -> codename
for r in csv.DictReader(open(KEEP, encoding="utf-8-sig")):
    keeper_lids[r["lid"]] = r["codename"]
print(f"Original keeper LIDs (top 100 Shopify revenue): {len(keeper_lids)}")

scrapped = set()
with open(SCRAP_TXT, encoding="utf-8") as f:
    for line in f:
        s = line.strip()
        if s.isdigit(): scrapped.add(s)
print(f"Discontinued/scrapped LIDs (from earlier list): {len(scrapped)}")

xref = {}
with open(XREF, encoding="utf-8") as f:
    xref = json.load(f)
print(f"Etsy LID → Shopify codename xref: {len(xref)}")

# Tier data
tier_codenames = {"A": set(), "B": set()}
for r in csv.DictReader(open(TIER, encoding="utf-8-sig")):
    tier_codenames[r["tier"]].add(r["codename"])
print(f"Tier A codenames: {len(tier_codenames['A'])}")
print(f"Tier B codenames: {len(tier_codenames['B'])}")

# Load full Etsy export for titles + sections
listings = {}
current = None
for r in csv.DictReader(open(ETSY, encoding="utf-8-sig")):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        current = {"lid": lid, "title": r.get("Title","").strip(), "section": r.get("Section","").strip()}
        listings[lid] = current

# Cross-reference revenue LIDs with discontinued
revenue_but_discontinued = set(revenue_lids) & scrapped
print(f"\n!! Revenue LIDs marked as discontinued (DO NOT delete): {len(revenue_but_discontinued)}")
for lid in revenue_but_discontinued:
    rev = revenue_lids[lid]['revenue']
    print(f"  LID {lid}  ${rev:.0f}  {revenue_lids[lid]['etsy_title'][:60]!r}")

# Build unified keep set
keep_set = {}  # lid -> reasons + data

# Add revenue LIDs (highest priority)
for lid, data in revenue_lids.items():
    keep_set[lid] = {
        "lid": lid,
        "etsy_title": data["etsy_title"],
        "section": data["section"],
        "etsy_revenue_2026": data["revenue"],
        "etsy_orders_2026": data["orders"],
        "etsy_views_2026": data["views"],
        "shopify_codename": xref.get(lid, {}).get("codename", ""),
        "reasons": ["etsy_revenue_2026"],
        "had_been_discontinued": lid in scrapped,
    }

# Add the 24 keeper LIDs (from Shopify revenue rank)
for lid, cn in keeper_lids.items():
    if lid in keep_set:
        keep_set[lid]["reasons"].append("shopify_top100_revenue")
        keep_set[lid]["shopify_codename"] = cn
    else:
        title = listings.get(lid, {}).get("title", "")[:120]
        section = listings.get(lid, {}).get("section", "")
        keep_set[lid] = {
            "lid": lid,
            "etsy_title": title,
            "section": section,
            "etsy_revenue_2026": 0,
            "etsy_orders_2026": 0,
            "etsy_views_2026": 0,
            "shopify_codename": cn,
            "reasons": ["shopify_top100_revenue"],
            "had_been_discontinued": lid in scrapped,
        }

# Annotate tier membership
for lid, k in keep_set.items():
    cn = k["shopify_codename"]
    if cn in tier_codenames["A"]: k["in_tier"] = "A"
    elif cn in tier_codenames["B"]: k["in_tier"] = "B"
    else: k["in_tier"] = ""

# Build all 117+ listings (kept + new Shopify products to be added)
# For new listings (Tier A + Tier B codenames not yet on Etsy), they don't have LIDs yet
tier_a_not_on_etsy = []
tier_b_not_on_etsy = []
existing_codenames = {k["shopify_codename"] for k in keep_set.values() if k["shopify_codename"]}
for r in csv.DictReader(open(TIER, encoding="utf-8-sig")):
    if r["codename"] in existing_codenames: continue
    entry = {
        "codename": r["codename"],
        "shop_title": r["title"],
        "handle": r["handle"],
        "first_price": r["first_price"],
        "sessions": r["sessions"],
        "url": r["url"],
        "image_path": r["image_path"],
    }
    if r["tier"] == "A":
        tier_a_not_on_etsy.append(entry)
    elif r["tier"] == "B":
        tier_b_not_on_etsy.append(entry)

# Tally final catalog
n_keep = len(keep_set)
n_new_a = len(tier_a_not_on_etsy)
n_new_b = len(tier_b_not_on_etsy)
n_total = n_keep + n_new_a + n_new_b

# Need image generation = listings in keep_set without an existing Tier-A image + all of Tier B not on Etsy
keep_codenames_with_image = {k["shopify_codename"] for k in keep_set.values()
                              if k["shopify_codename"] in tier_codenames["A"]}
keepers_need_image = [k for k in keep_set.values()
                      if not (k["shopify_codename"] and k["shopify_codename"] in tier_codenames["A"])]
n_images_needed = len(keepers_need_image) + len(tier_b_not_on_etsy)

print(f"\n=== FINAL CATALOG ===")
print(f"Existing Etsy listings to KEEP: {n_keep}")
print(f"  - With confirmed Etsy revenue: {sum(1 for k in keep_set.values() if k['etsy_revenue_2026'] > 0)}")
print(f"  - Shopify top 100 revenue: {sum(1 for k in keep_set.values() if 'shopify_top100_revenue' in k['reasons'])}")
print(f"  - Both: {sum(1 for k in keep_set.values() if len(k['reasons']) > 1)}")
print(f"Tier A new listings (have images): {n_new_a}")
print(f"Tier B new listings (need images): {n_new_b}")
print(f"TOTAL FINAL CATALOG: {n_total} listings")
print(f"Image generation needed: {n_images_needed}")

# Write CSV
all_rows = []
for lid, k in sorted(keep_set.items(), key=lambda x: -x[1]["etsy_revenue_2026"]):
    all_rows.append({
        "status": "EXISTING_KEEP",
        "lid": lid,
        "codename": k["shopify_codename"],
        "etsy_title": k["etsy_title"],
        "section": k["section"],
        "etsy_revenue_2026": k["etsy_revenue_2026"],
        "etsy_orders_2026": k["etsy_orders_2026"],
        "reasons": "|".join(k["reasons"]),
        "had_been_discontinued": k["had_been_discontinued"],
        "in_tier": k["in_tier"],
    })
for e in tier_a_not_on_etsy:
    all_rows.append({
        "status": "NEW_TIER_A_HAS_IMAGE",
        "lid": "",
        "codename": e["codename"],
        "etsy_title": e["shop_title"],
        "section": "",
        "etsy_revenue_2026": 0,
        "etsy_orders_2026": 0,
        "reasons": "tier_A_proven_shopify",
        "had_been_discontinued": False,
        "in_tier": "A",
    })
for e in tier_b_not_on_etsy:
    all_rows.append({
        "status": "NEW_TIER_B_NEED_IMAGE",
        "lid": "",
        "codename": e["codename"],
        "etsy_title": e["shop_title"],
        "section": "",
        "etsy_revenue_2026": 0,
        "etsy_orders_2026": 0,
        "reasons": "tier_B_sessions_top",
        "had_been_discontinued": False,
        "in_tier": "B",
    })

with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
    w.writeheader()
    w.writerows(all_rows)

# MD report
lines = [
    f"# Final Etsy Catalog — Unified Keep List",
    f"",
    f"Generated {Path(__file__).name} on {Path(OUT_CSV).stat().st_mtime if OUT_CSV.exists() else ''}",
    f"",
    f"## Catalog total: **{n_total} listings**",
    f"",
    f"| Group | Count | Notes |",
    f"|---|---|---|",
    f"| Existing Etsy keepers (revenue + Shopify top 100) | {n_keep} | Update title/desc/tags + ~20 images |",
    f"| Tier A new (already have AI images) | {n_new_a} | Create new Etsy listings, 0 images needed |",
    f"| Tier B new (need image generation) | {n_new_b} | Create new Etsy listings + generate images |",
    f"| **TOTAL** | **{n_total}** | **{n_images_needed} new images needed** |",
    f"",
    f"## ⚠️ Revenue-generating listings previously marked for deactivation",
    f"",
    f"_These would have been deleted under the earlier 'scrapped' plan but they ARE generating Etsy revenue. KEEP THEM._",
    f"",
    f"| LID | Revenue 2026 | Orders | Title |",
    f"|---|---|---|---|",
]
for lid in sorted(revenue_but_discontinued):
    rd = revenue_lids[lid]
    lines.append(f"| {lid} | ${rd['revenue']:.0f} | {rd['orders']} | {rd['etsy_title'][:60]} |")

lines += [
    f"",
    f"## All existing Etsy listings to keep ({n_keep})",
    f"",
    f"Sorted by 2026 YTD Etsy revenue.",
    f"",
    f"| Rank | LID | $YTD | Orders | Codename | Title | Reasons |",
    f"|---|---|---|---|---|---|---|",
]
for i, k in enumerate(sorted(keep_set.values(), key=lambda x: -x["etsy_revenue_2026"]), 1):
    lines.append(f"| {i} | {k['lid']} | ${k['etsy_revenue_2026']:.0f} | {k['etsy_orders_2026']} | {k['shopify_codename']} | {k['etsy_title'][:50]} | {', '.join(k['reasons'])} |")

OUT_MD.write_text("\n".join(lines), encoding="utf-8")

print(f"\nWrote: {OUT_CSV}")
print(f"Wrote: {OUT_MD}")
