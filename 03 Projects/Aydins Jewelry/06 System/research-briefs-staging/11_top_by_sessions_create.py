"""Use sessions-by-product (handles are authoritative) + Shopify inventory to identify
the top 100 ACTIVE ring products on Shopify. Build a Vela create-CSV for the ones
not already on Etsy.

Pipeline:
  1. Read sessions-by-product-90d.csv (has actual current product URL paths)
  2. Extract handle from each URL path
  3. Look up Shopify product data by handle
  4. Filter: must be Ring product_type AND have inventory in at least one variant
  5. Rank by sessions desc
  6. Take top 100, skip ones already on Etsy
  7. Build Vela create-CSV with authoritative Shopify data per handle
"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

SESS = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sessions-by-product-90d.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
KEEP_CSV = Path(r"C:\Users\amirl\Downloads\etsy-keep-list.csv")
TEMPLATE = Path(r"C:\Users\amirl\Downloads\etsy-import-template.csv")

OUT_RANK = Path(r"C:\Users\amirl\Downloads\top100-by-sessions-verified.csv")
OUT_NEW  = Path(r"C:\Users\amirl\Downloads\vela-new-100-from-sessions.csv")
OUT_REPORT = Path(r"C:\Users\amirl\Downloads\new-listings-preview.md")

def num(x):
    try: return int((x or '0').replace(',',''))
    except: return 0

def handle_from_path(path):
    m = re.match(r"^/products/([^/?#]+)", path or "")
    return m.group(1) if m else ""

# 1. Read sessions, aggregate by handle (max sessions across rows for the same handle)
print("Loading sessions...")
handle_sessions = defaultdict(lambda: {"sessions":0, "cart_adds":0, "checkout":0})
with open(SESS, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        if (r.get("Landing page type") or "").lower() != "product": continue
        h = handle_from_path(r.get("Landing page path"))
        if not h: continue
        s = num(r.get("Sessions"))
        c = num(r.get("Sessions with cart additions"))
        ck = num(r.get("Sessions that reached checkout"))
        # Use max for sessions (some products have multiple variants of the path)
        if s > handle_sessions[h]["sessions"]:
            handle_sessions[h] = {"sessions": s, "cart_adds": c, "checkout": ck}
print(f"Unique handles with sessions: {len(handle_sessions)}")

# 2. Load Shopify, aggregate by handle (product-level)
print("Loading Shopify...")
shop_by_handle = {}  # handle -> dict with product + ALL variants' inventory/widths/sizes
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        h = (r.get("handle") or "").strip()
        if not h: continue
        sku = (r.get("sku") or "").strip()
        d = shop_by_handle.setdefault(h, {
            "title": (r.get("title") or "").strip(),
            "description": (r.get("description") or "").strip(),
            "tags": (r.get("tags") or "").strip(),
            "product_type": (r.get("product_type") or "").strip(),
            "vendor": (r.get("vendor") or "").strip(),
            "handle": h,
            "url": (r.get("absolute_product_url") or "").strip(),
            "first_featured_image": (r.get("featured_image_url") or "").strip(),
            "first_sku": sku,
            "first_price": (r.get("price") or "").strip(),
            "first_option_color": (r.get("option_color") or "").strip(),
            "widths_set": set(),
            "sizes_set": set(),
            "total_inventory": 0,
            "variant_skus": [],
            "additional_images": [],
        })
        d["variant_skus"].append(sku)
        try:
            d["total_inventory"] += int(num(r.get("inventory_quantity")))
        except: pass
        vt = (r.get("variant_title") or "").strip()
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m:
            d["widths_set"].add(m.group(1))
            d["sizes_set"].add(m.group(2))
        # Capture additional image URLs from the first variant
        if not d["additional_images"]:
            for i in range(1, 6):
                u = (r.get(f"additional_image_url_{i}") or "").strip()
                if u: d["additional_images"].append(u)
print(f"Shopify handles: {len(shop_by_handle)}")

# 3. Match sessions to Shopify, filter to Rings with inventory
ranked = []
for h, sdata in handle_sessions.items():
    shop_d = shop_by_handle.get(h)
    if not shop_d:
        continue
    if shop_d["product_type"].lower() not in {"rings", "ring"}:
        continue
    if shop_d["total_inventory"] <= 0:
        continue
    ranked.append({
        "handle": h,
        "sessions": sdata["sessions"],
        "cart_adds": sdata["cart_adds"],
        "checkout": sdata["checkout"],
        "title": shop_d["title"],
        "first_sku": shop_d["first_sku"],
        "first_price": shop_d["first_price"],
        "first_featured": shop_d["first_featured_image"],
        "total_inventory": shop_d["total_inventory"],
        "widths_list": sorted(shop_d["widths_set"], key=lambda x: float(x)),
        "sizes_list": sorted(shop_d["sizes_set"], key=lambda x: float(x)),
        "description": shop_d["description"],
        "tags": shop_d["tags"],
        "url": shop_d["url"],
        "additional_images": shop_d["additional_images"],
    })

ranked.sort(key=lambda x: -x["sessions"])
print(f"Active ring products with sessions: {len(ranked)}")
print(f"Top 5:")
for r in ranked[:5]:
    print(f"  sess={r['sessions']:>5}  inv={r['total_inventory']:>3}  ${r['first_price']:<7}  {r['title'][:80]!r}")

# 4. Exclude codenames already on Etsy (the 24 keepers)
keep_codenames = set()
with open(KEEP_CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        keep_codenames.add(r["codename"])

def codename(sku): return (sku or "").split("-")[0].upper()

ranked_not_on_etsy = []
for r in ranked:
    cn = codename(r["first_sku"])
    if cn in keep_codenames: continue
    r["codename"] = cn
    ranked_not_on_etsy.append(r)
print(f"\nNot already on Etsy: {len(ranked_not_on_etsy)}")

# 5. Take top 100 (or all if fewer)
target_n = min(100, len(ranked_not_on_etsy))
top_n = ranked_not_on_etsy[:target_n]
print(f"Taking top {target_n} by sessions")

# Write ranking file for user reference
with open(OUT_RANK, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["rank", "sessions", "cart_adds", "checkout", "codename",
                                        "first_sku", "first_price", "total_inventory", "title", "url", "handle"])
    w.writeheader()
    for i, r in enumerate(top_n, 1):
        w.writerow({
            "rank": i, "sessions": r["sessions"], "cart_adds": r["cart_adds"], "checkout": r["checkout"],
            "codename": r["codename"], "first_sku": r["first_sku"], "first_price": r["first_price"],
            "total_inventory": r["total_inventory"], "title": r["title"], "url": r["url"], "handle": r["handle"],
        })
print(f"\nWrote rank file: {OUT_RANK}")

# 6. Build Vela create-CSV in template format
with open(TEMPLATE, encoding="utf-8-sig") as f:
    template_fieldnames = list(csv.DictReader(f).fieldnames)

# Generators (conservative, same as 24-keeper script)
MATERIALS_PRI = ["Ceramic", "Damascus Steel", "Damascus", "Titanium", "Cobalt", "14k", "Gold", "Tungsten"]
COLORS_PRI = ["Rose Gold", "Yellow Gold", "Gunmetal", "Black", "Silver", "Gold",
              "Blue", "Green", "Red", "Purple", "Orange", "White", "Pink"]
FEATURES = [
    ("Opal Inlay", r"\bopal\b"),
    ("Meteorite", r"\bmeteorite\b"),
    ("Koa Wood", r"\bkoa\b"),
    ("Box Elder Wood", r"\bbox elder\b"),
    ("Olive Wood", r"\bolive wood\b"),
    ("Whiskey Barrel", r"\bwhiskey barrel\b"),
    ("Wood Inlay", r"\bwood\b"),
    ("Carbon Fiber", r"\bcarbon fiber\b"),
    ("Antler", r"\bantler\b"),
    ("Dinosaur Bone", r"\bdinosaur\b"),
    ("Mother of Pearl", r"\bmother of pearl\b|\bmop\b"),
    ("Abalone", r"\babalone\b"),
    ("Diamond", r"\bdiamond\b"),
    ("Sapphire", r"\bsapphire\b"),
    ("Fidget Spinner", r"\bspinner\b"),
    ("Fingerprint", r"\bfingerprint\b"),
    ("Hammered", r"\bhammered\b"),
    ("Brushed Finish", r"\bbrushed\b"),
    ("Beveled", r"\bbeveled\b"),
    ("Domed", r"\bdomed\b"),
    ("Pipe Cut", r"\bpipe cut\b"),
    ("Grooved", r"\bgroove[ds]?\b"),
    ("Faceted", r"\bfaceted\b"),
    ("Stepped Edge", r"\bstepped edge\b|\bstep edge\b"),
    ("Lava Rock", r"\blava rock\b"),
]
def extract_material(title, desc):
    t = (title or "").lower()
    if "14k" in t or "14 k" in t: return "14k Gold"
    if "10k" in t: return "10k Gold"
    if "ceramic" in t: return "Ceramic"
    if "damascus" in t: return "Damascus Steel"
    if "titanium" in t: return "Titanium"
    if "tungsten" in t: return "Tungsten"
    d = (desc or "")[:300].lower()
    if "14k" in d: return "14k Gold"
    if "10k" in d: return "10k Gold"
    if "ceramic" in d: return "Ceramic"
    if "damascus" in d: return "Damascus Steel"
    if "titanium" in d: return "Titanium"
    if "tungsten" in d: return "Tungsten"
    return "Tungsten"

def material_short(material):
    return {"Damascus Steel": "Damascus", "14k Gold": "Gold", "10k Gold": "Gold"}.get(material, material)

def extract_color(title, tags, option_color):
    # Strongest signal: title prefix
    t = " " + (title or "").lower() + " "
    for c in COLORS_PRI:
        if " " + c.lower() + " " in t: return c
    # Tags
    tg = (tags or "").lower()
    for c in COLORS_PRI:
        if re.search(rf",\s*{re.escape(c.lower())}\s*,", "," + tg + ","): return c
    # option_color
    if option_color: return option_color.strip().title()
    return "Black"

def extract_feature(title, desc):
    t = (title or "").lower()
    for canonical, pat in FEATURES:
        if re.search(pat, t): return canonical
    d = (desc or "")[:300].lower()
    for canonical, pat in FEATURES:
        if re.search(pat, d): return canonical
    return ""

def format_widths(widths_list):
    if not widths_list: return ("8mm", ["8"])
    if len(widths_list) == 1: return (f"{widths_list[0]}mm", widths_list)
    return (f"{widths_list[0]}-{widths_list[-1]}mm", widths_list)

def build_title(material, widths_display, color, feature):
    mshort = material_short(material)
    fpart = f" {feature}" if feature else ""
    title = (f"{material} Wedding Band for Men, {widths_display} {color} Mens {mshort} Ring"
             f"{fpart}, Personalized Engraved Ring, Comfort Fit")
    if len(title) > 140:
        title = f"{material} Wedding Band for Men, {widths_display} {color} Mens {mshort} Ring{fpart}, Comfort Fit"
    if len(title) > 140:
        title = title[:140].rstrip(", ")
    return title

def clean_desc(s):
    if not s: return ""
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("—", ". ").replace("–", "-")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def build_description(material, shop_description):
    hook = (f"{material} wedding band for men, engraved and shipped from our Irving, "
            f"Texas workshop. Free engraving, free 2-day FedEx, lifetime sizing. Comfort fit.")
    body = clean_desc(shop_description)
    return f"{hook}\n\n{body}" if body else hook

def build_tags(material, color, feature):
    mshort = material_short(material).lower()
    color_l = color.lower()
    BASE = {
        "Tungsten":       ["tungsten ring","mens wedding band","mens wedding ring","mens tungsten ring",
                           "mens tungsten band","personalized ring","engraved ring","tungsten band",
                           "mens ring","wedding band men","comfort fit ring"],
        "Ceramic":        ["ceramic ring","mens wedding band","mens wedding ring","mens ceramic ring",
                           "ceramic wedding band","personalized ring","engraved ring","ceramic band",
                           "mens ring","wedding band men","comfort fit ring"],
        "Damascus Steel": ["damascus ring","mens wedding band","mens wedding ring","damascus steel ring",
                           "damascus band","personalized ring","engraved ring","mens ring",
                           "wedding band men","comfort fit ring","anniversary gift"],
        "Titanium":       ["titanium ring","mens wedding band","mens wedding ring","mens titanium ring",
                           "titanium wedding band","personalized ring","engraved ring","titanium band",
                           "mens ring","wedding band men","comfort fit ring"],
        "14k Gold":       ["gold ring","mens wedding band","mens wedding ring","14k gold ring",
                           "yellow gold ring","personalized ring","engraved ring","gold band",
                           "mens ring","wedding band men","comfort fit ring","anniversary gift"],
        "10k Gold":       ["gold ring","mens wedding band","mens wedding ring","10k gold ring",
                           "yellow gold ring","personalized ring","engraved ring","gold band",
                           "mens ring","wedding band men","comfort fit ring","anniversary gift"],
    }
    base = BASE.get(material, BASE["Tungsten"])
    extra = []
    color_tag = f"{color_l} {mshort} ring"
    if len(color_tag) <= 20: extra.append(color_tag)
    elif len(f"{color_l} ring") <= 20: extra.append(f"{color_l} ring")
    if feature:
        ft = f"{feature.lower()} ring"
        if len(ft) <= 20: extra.append(ft)
    tags = base + extra
    tags = [t for t in tags if len(t) <= 20]
    seen, dedup = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t); dedup.append(t)
    return ",".join(dedup[:13])

new_out_rows = []
preview = []
SECTION_MAP = {
    "Black": "Black Wedding Bands",
    "Silver": "Tungsten Rings",
    "Rose Gold": "Rose Gold Wedding Bands",
    "Yellow Gold": "Gold Wedding Bands",
    "Gold": "Gold Wedding Bands",
    "Blue": "Blue Wedding Bands",
    "Green": "Green Wedding Bands",
    "Red": "Red Wedding Bands",
    "Purple": "Purple Wedding Bands",
    "Orange": "Orange Wedding Bands",
    "Gunmetal": "Tungsten Rings",
    "White": "Tungsten Rings",
    "Pink": "Tungsten Rings",
}

for r in top_n:
    material = extract_material(r["title"], r["description"])
    color    = extract_color(r["title"], r["tags"], "")
    feature  = extract_feature(r["title"], r["description"])
    widths_display, widths_list = format_widths(r["widths_list"])
    sizes_list = r["sizes_list"] if r["sizes_list"] else ["7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12"]
    new_title = build_title(material, widths_display, color, feature)
    new_desc  = build_description(material, r["description"])
    new_tags  = build_tags(material, color, feature)
    price     = r["first_price"] or "169.00"
    section = SECTION_MAP.get(color, "Tungsten Rings")
    if feature in ("Wood Inlay", "Koa Wood", "Box Elder Wood", "Olive Wood", "Whiskey Barrel"):
        section = "Wood Inlay Wedding Bands"
    cn = r["codename"]

    # Master row
    master = {fn: "" for fn in template_fieldnames}
    master.update({
        "Title": new_title,
        "Description": new_desc,
        "Category": "Jewelry > Rings > Wedding & Engagement > Wedding Bands",
        "Who made it?": "I did",
        "What is it?": "A finished product",
        "When was it made?": "Made To Order",
        "Renewal options": "Automatic",
        "Product type": "Physical",
        "Tags": new_tags,
        "Materials": f"{material},Comfort Fit",
        "Section": section,
        "Price": price,
        "Quantity": "10",
        "SKU": cn,
        "Variation 1": "Width" if len(widths_list) > 1 else "Ring size",
        "V1 Option": widths_list[0] if len(widths_list) > 1 else sizes_list[0],
        "Variation 2": "Ring size" if len(widths_list) > 1 else "",
        "V2 Option": sizes_list[0] if len(widths_list) > 1 else "",
        "Var Price": price,
        "Var Quantity": "10",
        "Var SKU": f"{cn}-{widths_list[0]}-{sizes_list[0]}" if len(widths_list) > 1 else f"{cn}-{sizes_list[0]}",
        "Var Visibility": "TRUE",
        "Shipping profile": "All Shipping",
        "Weight": "0.5",
        "Length": "1",
        "Width": "1",
        "Height": "0.5",
        "Return policy": "30 days",
        "Photo 1": r["first_featured"],
    })
    # Additional photos (Photo 2-6)
    for idx, img_url in enumerate(r["additional_images"][:5], start=2):
        master[f"Photo {idx}"] = img_url
    new_out_rows.append(master)

    # Variant rows
    if len(widths_list) > 1:
        for wi, wv in enumerate(widths_list):
            for si, sv in enumerate(sizes_list):
                if wi == 0 and si == 0: continue
                vrow = {fn: "" for fn in template_fieldnames}
                vrow.update({
                    "V1 Option": wv, "V2 Option": sv,
                    "Var Price": price, "Var Quantity": "10",
                    "Var SKU": f"{cn}-{wv}-{sv}", "Var Visibility": "TRUE",
                })
                new_out_rows.append(vrow)
    else:
        for si, sv in enumerate(sizes_list):
            if si == 0: continue
            vrow = {fn: "" for fn in template_fieldnames}
            vrow.update({
                "V1 Option": sv,
                "Var Price": price, "Var Quantity": "10",
                "Var SKU": f"{cn}-{sv}", "Var Visibility": "TRUE",
            })
            new_out_rows.append(vrow)

    preview.append({
        "rank": preview.__len__() + 1, "codename": cn, "sessions": r["sessions"],
        "price": price, "title": new_title, "shop_title": r["title"],
        "material": material, "color": color, "feature": feature, "widths": widths_display,
        "url": r["url"], "photo1": r["first_featured"],
    })

with open(OUT_NEW, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=template_fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(new_out_rows)
print(f"\nWrote: {OUT_NEW}  ({target_n} listings, {len(new_out_rows)} variant rows)")

# Preview MD
lines = [
    "# New Listings Preview (Top 100 by Shopify Sessions)",
    "",
    f"All entries pulled from CURRENT Shopify products with active inventory.",
    f"Verify each title against the Shopify URL before publishing.",
    "",
    "| Rank | Codename | Sessions | Price | New Etsy Title | Shopify Product | Verify URL |",
    "|---|---|---|---|---|---|---|",
]
for p in preview:
    lines.append(f"| {p['rank']} | {p['codename']} | {p['sessions']} | ${p['price']} | {p['title'][:60]} | {p['shop_title'][:50]} | {p['url']} |")
OUT_REPORT.write_text("\n".join(lines), encoding="utf-8")
print(f"Preview: {OUT_REPORT}")

print("\n=== TOP 10 PREVIEW ===")
for p in preview[:10]:
    print(f"\nRank {p['rank']} — {p['codename']}  (sessions={p['sessions']}, ${p['price']})")
    print(f"  Shopify: {p['shop_title'][:80]!r}")
    print(f"  New Etsy: {p['title'][:100]!r}")
    print(f"  Material/Color/Feature: {p['material']!r}/{p['color']!r}/{p['feature']!r}")
    print(f"  URL: {p['url']}")
