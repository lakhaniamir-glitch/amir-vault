"""User-supplied Etsy listing performance data (year-to-date 2026), extracted from screenshots.
46 listings with non-zero revenue. Cross-match to current Etsy export by title to find Listing IDs.

Output:
  - etsy-revenue-2026-ytd.csv  (46 listings with revenue + matched LIDs)
  - etsy-revenue-keep-list.csv (final expanded keep list)
"""
import csv, re, json
from pathlib import Path

ETSY = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv")
OUT_REV  = Path(r"C:\Users\amirl\Downloads\etsy-revenue-2026-ytd.csv")
OUT_KEEP = Path(r"C:\Users\amirl\Downloads\etsy-revenue-keep-list.csv")

# Year-to-date Etsy revenue data from Amir's Etsy Shop Stats screenshots (2026-06-10).
# Format: (title_prefix, views, favorites, orders, revenue)
ETSY_REVENUE_2026 = [
    ("Personalized Fingerprint Dog Tag w/ Two Name", 339, 15, 31, 1363.57),
    ("Tungsten Wedding Band for Men, 8mm Silver Mens Tungsten Ring Domed", 698, 70, 11, 1324.21),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Brushed Finish", 60, 6, 3, 495.04),
    ("Men's Tungsten Carbide Wedding Band, Black Tungsten Carbide Ring, Gold Tungsten Carbide Ring, Available in 8mm", 26, 1, 1, 399.20),
    ("Tungsten Wedding Band Silver, Yellow Gold Double Braid", 387, 26, 3, 394.83),
    ("Black Tungsten Ring | Men's Wedding Band | Purple Tungsten", 107, 11, 3, 358.64),
    ("Tungsten Wedding Band for Men, 8mm Silver Mens Tungsten Ring Brushed Finish", 121, 5, 2, 351.26),
    ("Tungsten Wedding Band for Men, 8mm Rose Gold Mens Tungsten Ring Brushed Finish", 170, 8, 2, 329.98),
    ("CLEMATIS | Tungsten Ring Purple Inside", 33, 2, 2, 304.64),
    ("Black & Gray Lava Rock Stone Inlay, Ceramic Wedding Band", 198, 11, 1, 292.00),
    ("Men's Tungsten Carbide Wedding Band, Black Tungsten Carbide Ring, Silver Tungsten Carbide Ring, Carbon Fiber Wedding Band", 33, 2, 2, 275.88),
    ("Black Ceramic Ring - Purple Goldstone Inlay - Ceramic Wedding Band", 40, 4, 1, 261.00),
    ("Tungsten Wedding Band for Men, 8mm Silver Mens Tungsten Ring Fingerprint", 29, 1, 2, 251.54),
    ("Tungsten Wedding Band for Men, 8mm Rose Gold Mens Tungsten Ring Diamond", 58, 5, 2, 248.29),
    ("Ceramic Wedding Band for Men, 6-10mm Black Mens Ceramic Ring Beveled", 15, 3, 1, 228.00),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Fingerprint", 20, 3, 2, 220.70),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Hammered", 18, 1, 1, 190.40),
    ("Damascus Steel Wedding Band for Men, 8mm Gunmetal Mens Damascus Ring", 8, 0, 1, 190.40),
    ("Damascus Steel Wedding Band for Men, 8mm Silver Mens Damascus Ring, Personalized Engraved Ring, Comfort Fit", 27, 1, 1, 190.40),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Brushed Finish [a]", 20, 1, 1, 190.40),
    ("Men's Gold Wedding Band, Black Gold Ring, Silver Gold Ring, Personalized Engraved Ring, Comfort Fit, Free Engraving", 360, 5, 4, 177.35),
    ("Blue Tungsten Wedding Band, 18k Rose Gold Tungsten Ring, Men & Women", 108, 4, 1, 175.56),
    ("Blue Tungsten Ring, Mens Wedding Band Black, Tungsten Carbide", 10, 0, 1, 169.62),
    ("Tungsten Wedding Band for Men, 6-10mm Yellow Gold Mens Tungsten Ring Diamond", 18, 1, 1, 169.00),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Brushed Finish [b]", 13, 0, 1, 167.64),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Brushed Finish [c]", 30, 3, 1, 152.32),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Wood Inlay", 20, 2, 1, 149.82),
    ("Tungsten Wedding Band for Men, 8mm Silver Mens Tungsten Ring Fingerprint [b]", 137, 12, 1, 143.74),
    ("Tungsten Wedding Band for Men, 8mm Gold Mens Tungsten Ring Domed", 49, 2, 1, 137.94),
    ("Tungsten Wedding Band for Men, 8mm Silver Mens Tungsten Ring Fingerprint [c]", 63, 3, 1, 137.51),
    ("Tungsten Wedding Band for Men, 8mm Rose Gold Mens Tungsten Ring Brushed Finish [b]", 3, 0, 1, 126.77),
    ("8mm Black Tungsten Ring with Purple Opal Inlay | Men's Wedding Band, Comfort Fit", 61, 2, 1, 126.75),
    ("Tungsten Wedding Band for Men, 8mm Rose Gold Mens Tungsten Ring Pipe Cut", 52, 2, 1, 119.86),
    ("Tungsten Wedding Band for Men, 8mm Silver Mens Tungsten Ring Wood Inlay", 8, 0, 1, 119.86),
    ("Damascus Steel Wedding Band for Men, 8mm Silver Mens Damascus Ring Box Elder Wood", 76, 9, 1, 119.86),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Hammered [b]", 11, 1, 1, 119.20),
    ("Titanium Wedding Band for Men, 8mm Silver Mens Titanium Ring Hammered", 26, 2, 1, 119.00),
    ("Tungsten Ring Silver, Double Groove Rope", 102, 9, 1, 117.21),
    ("Tungsten Ring Green Wedding Band Silver Tungsten Brushed Acid Green", 107, 10, 1, 109.56),
    ("Tungsten Wedding Band for Men, 8mm Black Mens Tungsten Ring Brushed Finish [d]", 39, 3, 1, 109.56),
    ("Tungsten Wedding Band for Men, 8mm Silver Mens Tungsten Ring Olive Wood", 9, 2, 1, 89.89),
    ("Men's Gold Wedding Band, Black Gold Ring, Silver Gold Ring, Fingerprint Ring", 67, 5, 2, 84.01),
    ("Mens Wedding Band Red, Silver Tungsten Ring, Wedding Ring 8mm, Engagement Ring", 37, 4, 1, 82.76),
    ("Green Tungsten Wedding Band, Black Tungsten Ring, Men & Women, Tungsten Carbide Ring, Anniversary Ring", 91, 11, 1, 82.17),
    ("Personalized Fingerprint Dog Tag Necklace | Custom Memorial Keepsake", 14, 0, 1, 47.67),
    ("Laser Engraved Signet Ring Silver with Initial or Custom Logo", 110, 6, 1, 37.34),
]

print(f"Etsy revenue-generating listings (year-to-date): {len(ETSY_REVENUE_2026)}")
total = sum(r[4] for r in ETSY_REVENUE_2026)
print(f"Total 2026 YTD revenue: ${total:,.2f}")
print()

# Read current Etsy export
with open(ETSY, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
listings = {}
current = None
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        current = {"lid": lid, "rows": [r], "title": (r.get("Title") or "").strip(),
                   "section": (r.get("Section") or "").strip()}
        listings[lid] = current
    elif current is not None:
        current["rows"].append(r)

# Build title -> lid index (best match by prefix)
def normalize(s):
    s = re.sub(r"[^\w\s]", " ", (s or "").lower())
    return re.sub(r"\s+", " ", s).strip()

# Build lookup of normalized title -> [lids with that title]
title_to_lids = {}
for lid, L in listings.items():
    nt = normalize(L["title"])
    title_to_lids.setdefault(nt, []).append(lid)

# Match each revenue listing
matched = []
unmatched = []
for entry in ETSY_REVENUE_2026:
    title_search, views, favorites, orders, revenue = entry
    # Remove bracketed disambiguators for matching
    clean_title = re.sub(r"\s*\[\w+\]\s*$", "", title_search)
    nt = normalize(clean_title)

    # Find best match
    best_lid = None
    best_score = 0
    for L_lid, L in listings.items():
        L_nt = normalize(L["title"])
        # Find longest common prefix
        common = 0
        for c1, c2 in zip(nt, L_nt):
            if c1 == c2:
                common += 1
            else:
                break
        # Require min 30 char prefix match
        if common >= 30 and common > best_score:
            best_score = common
            best_lid = L_lid

    if best_lid:
        matched.append({
            "lid": best_lid,
            "title_in_etsy": listings[best_lid]["title"][:120],
            "title_searched": clean_title[:120],
            "section": listings[best_lid]["section"],
            "views": views,
            "favorites": favorites,
            "orders": orders,
            "revenue": revenue,
            "match_strength": best_score,
        })
    else:
        unmatched.append({
            "title_searched": clean_title,
            "views": views,
            "favorites": favorites,
            "orders": orders,
            "revenue": revenue,
        })

# Some revenue entries may match the same LID (multiple instances of the same generic title).
# Aggregate revenue per LID (some LIDs will have multiple revenue rows if the title prefix is generic).
from collections import defaultdict
lid_revenue = defaultdict(lambda: {"revenue": 0, "orders": 0, "views": 0, "favorites": 0, "match_count": 0})
for m in matched:
    L = lid_revenue[m["lid"]]
    L["revenue"] += m["revenue"]
    L["orders"] += m["orders"]
    L["views"] += m["views"]
    L["favorites"] += m["favorites"]
    L["match_count"] += 1

# Write revenue file
with open(OUT_REV, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["lid", "title_searched", "title_in_etsy", "section",
                                       "views", "favorites", "orders", "revenue", "match_strength"])
    w.writeheader()
    for m in matched:
        w.writerow(m)

# Final keep list = LIDs with revenue
keep_rows = []
for lid, agg in sorted(lid_revenue.items(), key=lambda x: -x[1]["revenue"]):
    keep_rows.append({
        "lid": lid,
        "etsy_title": listings[lid]["title"][:120],
        "section": listings[lid]["section"],
        "total_revenue_2026": agg["revenue"],
        "total_orders": agg["orders"],
        "total_views": agg["views"],
        "total_favorites": agg["favorites"],
        "revenue_rows_aggregated": agg["match_count"],
    })

with open(OUT_KEEP, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["lid", "etsy_title", "section", "total_revenue_2026",
                                       "total_orders", "total_views", "total_favorites",
                                       "revenue_rows_aggregated"])
    w.writeheader()
    w.writerows(keep_rows)

print(f"Matched: {len(matched)} of {len(ETSY_REVENUE_2026)}")
print(f"Unique LIDs with revenue: {len(lid_revenue)}")
print(f"Unmatched (need manual review): {len(unmatched)}")
print()
print(f"Wrote: {OUT_REV}")
print(f"Wrote: {OUT_KEEP}")
print()

print("=== UNMATCHED (need manual title fix or LID lookup) ===")
for u in unmatched:
    print(f"  ${u['revenue']:>8.2f}  orders={u['orders']:<3} views={u['views']:<4}  {u['title_searched'][:100]!r}")
print()

print("=== TOP 15 LIDs BY REVENUE (year-to-date 2026) ===")
for i, k in enumerate(keep_rows[:15], 1):
    print(f"  {i:2d}. LID {k['lid']:<12}  ${k['total_revenue_2026']:>8.2f}  orders={k['total_orders']:<3}  {k['etsy_title'][:60]!r}")
