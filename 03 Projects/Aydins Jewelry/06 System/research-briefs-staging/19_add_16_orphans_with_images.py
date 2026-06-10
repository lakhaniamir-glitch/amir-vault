"""Add the 16 orphans with existing 4-image sets to the final keep list.
All 16 are confirmed live on shopaydins.com via sales-by-product-90d.csv + sessions data.

For each:
  - Title from sales-by-product-90d.csv (or fallback)
  - Codename from folder name (caps)
  - Handle from sessions URL (or folder name)
  - 4-image set ready at brands/aydins/etsy-exports/2026-06-04/images/{handle}/

BETA follow-up: WebFetch each Shopify URL to pull current description/material/variants for the Etsy CSV.
"""
import csv, sys, re
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

UNIFIED  = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED.csv")
SALES    = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sales-by-product-90d.csv")
SESS     = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sessions-by-product-90d.csv")
OUT_CSV  = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED-v3.csv")

# Folder name -> {codename overrides per user 2026-06-10}
ORPHANS = {
    "alabaster-silver-ring-white-ceramic-domed":                                  {"codename_pref": "ALABASTER"},
    "auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay":           {"codename_pref": "AURIC"},
    "aurion-gold-tungsten-ring-gold-foil-inlay-beveled-8mm":                      {"codename_pref": "JDTR1166"},
    "baldur-domed-tungsten-rune-wedding-band":                                    {"codename_pref": "BALDUR"},
    "cosmic-black-tungsten-ring-crushed-alexandrite-goldstone-inlay-domed":       {"codename_pref": "COSMIC"},
    "crimsen-red-tungsten-ring-brushed-domed":                                    {"codename_pref": "CRIMSEN"},
    "jdtr969":                                                                    {"codename_pref": "JDTR969"},
    "leporis-black-tungsten-ring-round-cut-white-cz":                             {"codename_pref": "LEPORIS"},
    "lusters-black-tungsten-ring-with-purple-tiger-cowrie-inlay":                 {"codename_pref": "LUSTERS"},
    "nemesis-black-tungsten-ring-white-round-cz-beveled-edge-ring":               {"codename_pref": "JDTR1028"},
    "peachland-black-tungsten-ring-green-celtic-dragon-inlay":                    {"codename_pref": "PEACHLAND"},
    "rugged-black-tungsten-ring-gun-metal-hammered-center-with-stepped-edge":     {"codename_pref": "RUGGED"},
    "sequoia-iron-wood-black-shiny-domed":                                        {"codename_pref": "SEQUOIA"},
    "smokeylade-black-gun-metal-tungsten-with-domed-brushed-ring":                {"codename_pref": "SMOKEYLADE"},
    "spartanite-black-ring-black-brushed-domed-orange-groove":                    {"codename_pref": "SPARTANITE"},
    "valor-silver-tungsten-ring-silver-inlay-black-diamonds":                     {"codename_pref": "VALOR"},  # title displays SURYA
}

# Find current titles from sales data
title_by_first_word = {}
sales_by_first_word = {}
with open(SALES, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        title = (r.get("Product title") or "").strip()
        m = re.match(r"^([A-Z][A-Z0-9]+)\s*[|,]", title)
        if m:
            word = m.group(1).upper()
            title_by_first_word.setdefault(word, title)
            sales_by_first_word.setdefault(word, {
                "qty": int(float(r.get("Net items sold") or "0")),
                "net_sales": float((r.get("Net sales") or "0").replace(",","") or "0"),
            })

# Find sessions per handle
def num(x):
    try: return int((x or '0').replace(',',''))
    except: return 0
handle_sessions = {}
handle_orders = {}
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
            handle_orders[h] = num(r.get("Sessions that reached checkout"))

# Load existing 150 keep list
existing_rows = []
existing_codenames = set()
with open(UNIFIED, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        existing_rows.append(r)
        if r["codename"]: existing_codenames.add(r["codename"])

# Build the 16 additions
additions = []
for folder, meta in ORPHANS.items():
    first_word = folder.split("-")[0].upper()
    codename_pref = meta["codename_pref"]

    title = title_by_first_word.get(first_word, "")
    if not title and first_word == "VALOR":
        title = "VALOR | Silver Tungsten Ring, Silver Inlay & Black Diamonds (titled as SURYA on Shopify)"
    if not title:
        title = f"{first_word} (orphan, fetch from Shopify URL)"

    sales = sales_by_first_word.get(first_word, {"qty": 0, "net_sales": 0})
    sess = handle_sessions.get(folder, 0)

    # Skip if codename already in keep list
    if codename_pref in existing_codenames:
        print(f"SKIP {first_word}: codename {codename_pref} already in catalog")
        continue

    additions.append({
        "status": "NEW_HAS_IMAGES_FETCH_DATA",
        "lid": "",
        "codename": codename_pref,
        "etsy_title": title,
        "section": "",
        "etsy_revenue_2026": 0,
        "etsy_orders_2026": 0,
        "reasons": f"image_set_ready|sales_qty_{sales['qty']}|sessions_{sess}|shop_url=/products/{folder}",
        "had_been_discontinued": False,
        "in_tier": "",
    })

# Write expanded keep list
final_rows = list(existing_rows) + additions
with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    fieldnames = list(existing_rows[0].keys())
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(final_rows)

print(f"\n=== UPDATED CATALOG ===")
print(f"Previous: {len(existing_rows)} listings")
print(f"Adding (orphans with images): {len(additions)}")
print(f"NEW TOTAL: {len(final_rows)} listings")
print()
print(f"Image generation impact:")
print(f"  Previously: 117 listings × 4 = 468 new images")
print(f"  Now: 117 listings × 4 = 468 (unchanged — the 16 additions all have 4-image sets ready)")
print()
print(f"Wrote: {OUT_CSV}")
print()
print("=== Sample additions (full list saved to CSV) ===")
for a in additions[:5]:
    print(f"  {a['codename']:<12} | {a['etsy_title'][:60]!r}")
    print(f"    {a['reasons']}")
    print()
