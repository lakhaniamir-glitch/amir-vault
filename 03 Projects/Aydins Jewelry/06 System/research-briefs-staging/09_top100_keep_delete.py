"""Identify the top 100 Shopify products by 90-day revenue, cross-reference to Etsy listings,
and produce KEEP list (top 100 active on Etsy) + DELETE list (everything else on Etsy).

Inputs:
  - sales-by-product-90d.csv  (Shopify sales by Product Title)
  - Shopify aydinsjewelry.myshopify.com (2).csv  (to map Product Title -> Codename)
  - AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv  (current Etsy state)
  - etsy-to-shopify-xref-v4.json  (Etsy LID -> Shopify codename)

Outputs:
  - top100-shopify-ranked.csv      (the 100 winners, with sales/revenue/codename)
  - etsy-keep-list.csv             (Etsy LIDs to keep, with Shopify codename + title)
  - etsy-delete-list.csv           (Etsy LIDs to delete, with reason)
  - keep-delete-summary.md         (human-readable report)
"""
import csv, json, re, sys
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

SALES = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sales-by-product-90d.csv")
SHOP  = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
ETSY  = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv")
XREF  = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v4.json")

OUT_TOP100  = Path(r"C:\Users\amirl\Downloads\top100-shopify-ranked.csv")
OUT_KEEP    = Path(r"C:\Users\amirl\Downloads\etsy-keep-list.csv")
OUT_DELETE  = Path(r"C:\Users\amirl\Downloads\etsy-delete-list.csv")
OUT_REPORT  = Path(r"C:\Users\amirl\Downloads\keep-delete-summary.md")

def primary(sku):
    return (sku or "").strip().split("-")[0].upper()

def num(x):
    if not x: return 0.0
    s = str(x).replace(",", "").replace("$", "").strip()
    try: return float(s)
    except: return 0.0

# 1. Read sales data, filter to actual Rings (skip Shipping Protection etc), sort by revenue
print("Loading sales data...")
sales = []
with open(SALES, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        ptype = (r.get("Product type") or "").strip()
        title = (r.get("Product title") or "").strip()
        if not title: continue
        # Filter to ring products (skip Shipping Protection, gift cards, etc.)
        if ptype.lower() not in {"rings", "ring"}: continue
        sales.append({
            "title": title,
            "vendor": (r.get("Product vendor") or "").strip(),
            "type": ptype,
            "net_items": int(num(r.get("Net items sold"))),
            "gross_sales": num(r.get("Gross sales")),
            "net_sales": num(r.get("Net sales")),
            "total_sales": num(r.get("Total sales")),
        })
sales.sort(key=lambda x: -x["net_sales"])
print(f"Ring products with sales: {len(sales)}")
print(f"Top 5 by net_sales:")
for s in sales[:5]:
    print(f"  ${s['net_sales']:>8.0f}  qty={s['net_items']:3d}  {s['title'][:80]!r}")

# 2. Build Shopify Product Title -> codename map (canonical codename per product)
print("\nBuilding Shopify Title -> codename map...")
shop_title_to_cn = {}
shop_first_word_to_cn = {}  # First all-caps word in title -> codename
shop_handle_to_cn = {}
shop_by_codename = {}

def extract_first_word(title: str) -> str:
    """Extract leading product name like 'KNIGHT | ...' -> 'KNIGHT'."""
    t = (title or "").strip()
    m = re.match(r"^([A-Z][A-Z0-9 \-]{2,})\s*[|,]", t)
    if m:
        return m.group(1).strip().upper()
    m = re.match(r"^([A-Za-z]{3,})\b", t)
    return m.group(1).upper() if m else ""

with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = primary(sku)
        title = (r.get("title") or "").strip()
        handle = (r.get("handle") or "").strip()
        if cn and title and title not in shop_title_to_cn:
            shop_title_to_cn[title] = cn
        fw = extract_first_word(title)
        if fw and fw not in shop_first_word_to_cn:
            shop_first_word_to_cn[fw] = cn
        if handle and handle not in shop_handle_to_cn:
            shop_handle_to_cn[handle] = cn
        if cn not in shop_by_codename:
            shop_by_codename[cn] = {
                "title": title, "handle": handle, "first_sku": sku,
            }
print(f"Shopify titles indexed: {len(shop_title_to_cn)}, first-words: {len(shop_first_word_to_cn)}")

# 3. Get top 100 ring products with mapped codenames
top100 = []
skipped_no_codename = []
for s in sales:
    cn = None
    # Strategy A: exact title match
    cn = shop_title_to_cn.get(s["title"])
    # Strategy B: first-word match (e.g., 'KNIGHT | ...' -> 'KNIGHT' -> codename)
    if not cn:
        fw = extract_first_word(s["title"])
        if fw and fw in shop_first_word_to_cn:
            cn = shop_first_word_to_cn[fw]
    # Strategy C: search Shopify titles for substring match (title starts with sales title prefix)
    if not cn:
        sales_prefix = s["title"].split("|")[0].strip().lower()
        if len(sales_prefix) >= 4:
            for shop_title, shop_cn in shop_title_to_cn.items():
                if shop_title.lower().startswith(sales_prefix) or sales_prefix in shop_title.lower():
                    cn = shop_cn
                    break
    if cn:
        s["codename"] = cn
        s["handle"] = shop_by_codename.get(cn, {}).get("handle", "")
        top100.append(s)
        if len(top100) == 100: break
    else:
        skipped_no_codename.append(s["title"])

print(f"\nTop 100 found: {len(top100)}")
if skipped_no_codename:
    print(f"Sales rows skipped (no codename mapping): {len(skipped_no_codename)}")
    print(f"  Samples: {skipped_no_codename[:5]}")

# Write top100 file
with open(OUT_TOP100, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["rank", "codename", "shop_title", "net_items", "net_sales", "gross_sales", "handle"])
    w.writeheader()
    for i, s in enumerate(top100, 1):
        w.writerow({
            "rank": i, "codename": s["codename"], "shop_title": s["title"],
            "net_items": s["net_items"], "net_sales": s["net_sales"],
            "gross_sales": s["gross_sales"], "handle": s["handle"],
        })

# Codenames of the top 100
top100_codenames = {s["codename"] for s in top100}

# 4. Read Etsy + xref to identify which are top100 vs not
with open(XREF, encoding="utf-8") as f:
    xref = json.load(f)

with open(ETSY, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
listings = []
current = None
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: listings.append(current)
        current = {"lid": lid, "rows": [r],
                   "section": (r.get("Section") or "").strip(),
                   "title": (r.get("Title") or "").strip(),
                   "section": (r.get("Section") or "").strip()}
    elif current is not None:
        current["rows"].append(r)
if current is not None: listings.append(current)

# Load scrapped/discontinued list
scrapped = set()
SCRAP_TXT = Path(r"C:\Users\amirl\Documents\Amirs Command Center\brands\aydins\etsy-exports\2026-06-04\listings-to-deactivate-in-vela.txt")
with open(SCRAP_TXT, encoding="utf-8") as f:
    for line in f:
        s = line.strip()
        if s.isdigit(): scrapped.add(s)

keep_rows = []
delete_rows = []

for L in listings:
    lid = L["lid"]
    xref_entry = xref.get(lid)
    matched_codename = xref_entry["codename"] if xref_entry else ""
    in_top100 = matched_codename in top100_codenames if matched_codename else False
    is_discontinued = lid in scrapped

    if is_discontinued:
        delete_rows.append({"lid": lid, "reason": "discontinued", "codename": matched_codename,
                             "etsy_title": L["title"][:120], "section": L["section"]})
    elif in_top100:
        # Find rank
        rank = next((i+1 for i, s in enumerate(top100) if s["codename"] == matched_codename), 0)
        sales_data = next((s for s in top100 if s["codename"] == matched_codename), {})
        keep_rows.append({
            "lid": lid, "rank": rank, "codename": matched_codename,
            "shop_title": sales_data.get("title", ""),
            "etsy_title": L["title"][:120],
            "section": L["section"],
            "net_items": sales_data.get("net_items", 0),
            "net_sales": sales_data.get("net_sales", 0),
        })
    else:
        if matched_codename:
            delete_rows.append({"lid": lid, "reason": "not_top100",
                                 "codename": matched_codename,
                                 "etsy_title": L["title"][:120], "section": L["section"]})
        else:
            delete_rows.append({"lid": lid, "reason": "no_shopify_match",
                                 "codename": "",
                                 "etsy_title": L["title"][:120], "section": L["section"]})

keep_rows.sort(key=lambda x: x["rank"])

# Some top100 codenames may map to MULTIPLE Etsy listings (duplicates); count unique products
unique_keep_codenames = set(r["codename"] for r in keep_rows)
unique_top100_on_etsy = unique_keep_codenames & top100_codenames
top100_not_on_etsy = top100_codenames - unique_keep_codenames

# Write keep + delete
with open(OUT_KEEP, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["lid", "rank", "codename", "shop_title", "etsy_title", "section", "net_items", "net_sales"])
    w.writeheader()
    w.writerows(keep_rows)

with open(OUT_DELETE, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["lid", "reason", "codename", "etsy_title", "section"])
    w.writeheader()
    w.writerows(delete_rows)

# Tally by reason
from collections import Counter
delete_reasons = Counter(r["reason"] for r in delete_rows)

# MD report
lines = [
    "# Etsy Keep + Delete Plan",
    f"_Based on Shopify 90-day sales (top 100 ring products by net revenue)._",
    "",
    "## Summary",
    f"- Top 100 Shopify ring products identified: **{len(top100)}**",
    f"- Top 100 codenames also currently on Etsy: **{len(unique_top100_on_etsy)}**",
    f"- Top 100 codenames NOT on Etsy (potential gap): **{len(top100_not_on_etsy)}**",
    "",
    "## Etsy listing breakdown",
    f"- Total Etsy listings: **{len(listings)}**",
    f"- Etsy listings to KEEP (match a top-100 Shopify codename): **{len(keep_rows)}**",
    f"- Etsy listings to DELETE: **{len(delete_rows)}**",
    "",
    "### Delete breakdown",
]
for reason, n in delete_reasons.most_common():
    lines.append(f"- {reason}: {n}")
lines += [
    "",
    "## Top 100 Shopify ring products (revenue ranked)",
    "",
    "| Rank | Codename | Title | Qty | Net $ |",
    "|---|---|---|---|---|",
]
for i, s in enumerate(top100[:100], 1):
    lines.append(f"| {i} | {s['codename']} | {s['title'][:60]} | {s['net_items']} | ${s['net_sales']:.0f} |")
lines += [
    "",
    "## Keep list — Etsy LIDs (sorted by Shopify revenue rank)",
    "",
    "| Rank | LID | Codename | Shop title | Etsy title |",
    "|---|---|---|---|---|",
]
for r in keep_rows:
    lines.append(f"| {r['rank']} | {r['lid']} | {r['codename']} | {r['shop_title'][:60]} | {r['etsy_title'][:60]} |")
OUT_REPORT.write_text("\n".join(lines), encoding="utf-8")

print()
print("=" * 80)
print("RESULTS")
print("=" * 80)
print(f"Top 100 Shopify ring products: {len(top100)}")
print(f"  - Codenames also on Etsy: {len(unique_top100_on_etsy)}")
print(f"  - Codenames NOT on Etsy yet: {len(top100_not_on_etsy)}")
print()
print(f"Etsy listings: {len(listings)}")
print(f"  KEEP (top-100 match): {len(keep_rows)}")
print(f"  DELETE: {len(delete_rows)}")
for reason, n in delete_reasons.most_common():
    print(f"    - {reason}: {n}")
print()
print(f"Files written:")
print(f"  {OUT_TOP100}")
print(f"  {OUT_KEEP}")
print(f"  {OUT_DELETE}")
print(f"  {OUT_REPORT}")
print()
print("=== First 10 KEEP listings (by rank) ===")
for r in keep_rows[:10]:
    print(f"  rank={r['rank']:3d}  LID={r['lid']:<12}  {r['codename']:<14}  ${r['net_sales']:>6.0f}  {r['shop_title'][:60]!r}")
print()
print("=== Top 100 codenames NOT yet on Etsy (potential new listings) ===")
for cn in sorted(top100_not_on_etsy):
    sales_data = next((s for s in top100 if s["codename"] == cn), None)
    if sales_data:
        print(f"  {cn:<14}  ${sales_data['net_sales']:>6.0f}  {sales_data['title'][:70]!r}")
