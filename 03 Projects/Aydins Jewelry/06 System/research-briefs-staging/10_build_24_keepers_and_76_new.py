"""Build two Vela CSVs:

  A. 24-keeper UPDATE CSV — applies clean title/desc/tags to the 24 top-100 Etsy listings.
     Uses fresh Etsy export structure (so Vela matches via existing Listing IDs).
     Only the 24 keepers have their Title/Description/Tags overwritten.
     The other 478 are excluded from this file.

  B. 76-new CREATE CSV — for the 76 top-100 Shopify products not yet on Etsy.
     Uses Vela's etsy-import-template column structure (no Listing ID column).
     Fully populated from Shopify data so Vela can create new Etsy listings.

Conservative matcher fixes for the 24 keepers:
  - Color extracted from Shopify TAGS first (explicit Color tags), then title; never defaults blindly to Silver.
  - Material from Shopify title first, then description (already correct in v4).
  - Feature from Shopify title first, then description body.

Outputs:
  - vela-update-24-keepers.csv
  - vela-new-76-create.csv
  - 24-keepers-preview.md  (human review before push)
"""
import csv, json, re, sys
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

ETSY        = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv")
KEEP_CSV    = Path(r"C:\Users\amirl\Downloads\etsy-keep-list.csv")
TOP100_CSV  = Path(r"C:\Users\amirl\Downloads\top100-shopify-ranked.csv")
SHOP        = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
TEMPLATE    = Path(r"C:\Users\amirl\Downloads\etsy-import-template.csv")

OUT_KEEP_VELA = Path(r"C:\Users\amirl\Downloads\vela-update-24-keepers.csv")
OUT_NEW_VELA  = Path(r"C:\Users\amirl\Downloads\vela-new-76-create.csv")
OUT_REVIEW    = Path(r"C:\Users\amirl\Downloads\24-keepers-preview.md")

# ---------- Load Shopify full data (per codename) ----------
print("Loading Shopify...")
def primary(sku): return (sku or "").strip().split("-")[0].upper()

shop = {}
shop_first_url_by_cn = {}
shop_variant_skus_by_cn = {}
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = primary(sku)
        if not cn: continue
        if cn not in shop:
            shop[cn] = {
                "title": (r.get("title") or "").strip(),
                "description": (r.get("description") or "").strip(),
                "tags": (r.get("tags") or "").strip(),
                "handle": (r.get("handle") or "").strip(),
                "first_sku": sku,
                "first_price": (r.get("price") or "").strip(),
                "first_featured": (r.get("featured_image_url") or "").strip(),
                "first_seo_desc": (r.get("seo_description") or "").strip(),
                "option_color": (r.get("option_color") or "").strip(),
                "widths_set": set(), "sizes_set": set(),
            }
        # collect every variant SKU + width/size
        shop_variant_skus_by_cn.setdefault(cn, []).append(sku)
        vt = (r.get("variant_title") or "").strip()
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m:
            shop[cn]["widths_set"].add(m.group(1))
            shop[cn]["sizes_set"].add(m.group(2))
print(f"Shopify codenames: {len(shop)}")

# ---------- Load 24 keepers ----------
keepers = []
with open(KEEP_CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        keepers.append(r)
print(f"24 keepers loaded: {len(keepers)}")

# ---------- Load Top 100 ----------
top100 = []
with open(TOP100_CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        top100.append(r)
print(f"Top 100 loaded: {len(top100)}")

# ---------- Generators (conservative) ----------
MATERIAL_PRIORITY = ["Ceramic", "Damascus Steel", "Damascus", "Titanium", "Cobalt", "Tungsten"]
COLOR_PRIORITY = ["Rose Gold", "Yellow Gold", "Gunmetal", "Black", "Silver", "Gold",
                  "Blue", "Green", "Red", "Purple", "Orange", "White", "Pink"]

def extract_material(shop_title: str, shop_description: str) -> str:
    """Pick from Shopify title first (most reliable), then description first 300 chars."""
    t = (shop_title or "").lower()
    d = (shop_description or "")[:300].lower()
    for m in MATERIAL_PRIORITY:
        if m.lower() in t: return "Tungsten" if m == "Tungsten" else ("Damascus Steel" if m == "Damascus" else m)
    for m in MATERIAL_PRIORITY:
        if m.lower() in d: return "Tungsten" if m == "Tungsten" else ("Damascus Steel" if m == "Damascus" else m)
    return "Tungsten"

def material_short(material: str) -> str:
    return {"Damascus Steel": "Damascus"}.get(material, material)

def extract_color_conservative(shop_title: str, shop_tags: str, shop_section_tags: str) -> str:
    """
    Conservative color extraction:
      1. From Shopify title prefix (e.g., 'REVOLVE | Black Tungsten Ring' -> Black)
      2. From Shopify tags (explicit color tags)
      3. From section/category tags
      4. Default 'Black' (Aydins's dominant color)
    """
    t = " " + (shop_title or "").lower() + " "
    # Search title first
    for c in COLOR_PRIORITY:
        if " " + c.lower() + " " in t:
            return c
    # Search tags
    tags = (shop_tags or "").lower()
    for c in COLOR_PRIORITY:
        # Look for tag like "Black,", "Black Mens", " Blue,"
        if re.search(rf",\s*{re.escape(c.lower())}\s*[,/]", "," + tags + ","):
            return c
        if re.search(rf"\b{re.escape(c.lower())}\s+mens\s+wedding", tags):
            return c
    # Section
    s = " " + (shop_section_tags or "").lower() + " "
    for c in COLOR_PRIORITY:
        if " " + c.lower() + " " in s:
            return c
    return "Black"  # Aydins's dominant color, better default than Silver

# Feature extraction — prioritize features mentioned in Shopify TITLE
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
    ("Fidget Spinner", r"\bfidget spinner\b|\bspinner\b"),
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
    ("Sapphire", r"\bsapphire\b"),
]
def extract_feature(shop_title: str, shop_description: str) -> str:
    t = (shop_title or "").lower()
    for canonical, pat in FEATURES:
        if re.search(pat, t): return canonical
    d = (shop_description or "")[:300].lower()
    for canonical, pat in FEATURES:
        if re.search(pat, d): return canonical
    return ""

def format_widths(widths_set: set) -> tuple:
    """Return (display_width_for_title, all_widths_list_sorted)."""
    widths = sorted(widths_set, key=lambda x: float(x))
    if not widths: return ("8mm", ["8"])
    if len(widths) == 1: return (f"{widths[0]}mm", widths)
    return (f"{widths[0]}-{widths[-1]}mm", widths)

def build_title(material: str, widths_display: str, color: str, feature: str) -> str:
    mshort = material_short(material)
    fpart = f" {feature}" if feature else ""
    title = (f"{material} Wedding Band for Men, {widths_display} {color} Mens {mshort} Ring"
             f"{fpart}, Personalized Engraved Ring, Comfort Fit")
    if len(title) > 140:
        title = f"{material} Wedding Band for Men, {widths_display} {color} Mens {mshort} Ring{fpart}, Comfort Fit"
    if len(title) > 140:
        title = title[:140].rstrip(", ")
    return title

def clean_desc(s: str) -> str:
    if not s: return ""
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("—", ". ").replace("–", "-")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def build_description(material: str, shop_description: str) -> str:
    hook = (f"{material} wedding band for men, engraved and shipped from our Irving, "
            f"Texas workshop. Free engraving, free 2-day FedEx, lifetime sizing. Comfort fit.")
    body = clean_desc(shop_description)
    return f"{hook}\n\n{body}" if body else hook

def build_tags(material: str, color: str, feature: str) -> str:
    mshort = material_short(material).lower()
    color_l = color.lower()
    base = {
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
    }.get(material, ["tungsten ring","mens wedding band","mens wedding ring","mens tungsten ring",
                     "mens tungsten band","personalized ring","engraved ring","tungsten band",
                     "mens ring","wedding band men","comfort fit ring"])
    extra = []
    color_tag = f"{color_l} {mshort} ring"
    if len(color_tag) <= 20: extra.append(color_tag)
    elif len(f"{color_l} ring") <= 20: extra.append(f"{color_l} ring")
    if feature:
        ft = f"{feature.lower()} ring"
        if len(ft) <= 20: extra.append(ft)
    tags = base + extra
    tags = [t for t in tags if len(t) <= 20]
    seen, deduped = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t); deduped.append(t)
    return ",".join(deduped[:13])

# ---------- A. Build 24-keeper update CSV ----------
with open(ETSY, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    etsy_fieldnames = list(reader.fieldnames)
    etsy_rows = list(reader)

# Index Etsy rows by listing block
etsy_blocks = {}
current = None
for i, r in enumerate(etsy_rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: etsy_blocks[current["lid"]] = current
        current = {"lid": lid, "rows": [i]}
    elif current is not None:
        current["rows"].append(i)
if current is not None: etsy_blocks[current["lid"]] = current

keep_out_rows = []
preview_rows = []
for k in keepers:
    lid = k["lid"]
    cn = k["codename"]
    shop_d = shop.get(cn)
    if not shop_d:
        print(f"WARNING: codename {cn} not in shop data for LID {lid}")
        continue
    if lid not in etsy_blocks:
        print(f"WARNING: LID {lid} not in fresh Etsy export")
        continue

    material = extract_material(shop_d["title"], shop_d["description"])
    color    = extract_color_conservative(shop_d["title"], shop_d["tags"], shop_d.get("option_color",""))
    feature  = extract_feature(shop_d["title"], shop_d["description"])
    widths_display, widths_list = format_widths(shop_d["widths_set"])
    new_title = build_title(material, widths_display, color, feature)
    new_desc  = build_description(material, shop_d["description"])
    new_tags  = build_tags(material, color, feature)

    block = etsy_blocks[lid]
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(etsy_rows[row_i])
        if idx_pos == 0:
            r["Title"] = new_title
            r["Description"] = new_desc
            r["Tags"] = new_tags
        keep_out_rows.append(r)

    preview_rows.append({
        "rank": k.get("rank",""), "lid": lid, "codename": cn,
        "shop_title": shop_d["title"],
        "material": material, "color": color, "feature": feature, "widths": widths_display,
        "new_title": new_title,
        "new_tags": new_tags,
        "new_desc_preview": new_desc[:160],
    })

with open(OUT_KEEP_VELA, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=etsy_fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(keep_out_rows)
print(f"\n[A] Wrote: {OUT_KEEP_VELA}  ({len(keepers)} keepers, {len(keep_out_rows)} rows)")

# ---------- B. Build 76-new CSV in Vela's import-template format ----------
# Read template to get column structure
with open(TEMPLATE, encoding="utf-8-sig") as f:
    template_fieldnames = list(csv.DictReader(f).fieldnames)

# Codenames in keepers already on Etsy
keep_codenames = {k["codename"] for k in keepers}
missing_top100 = [t for t in top100 if t["codename"] not in keep_codenames]
print(f"\n[B] Missing top-100 (to create new): {len(missing_top100)}")

new_out_rows = []
for t in missing_top100:
    cn = t["codename"]
    shop_d = shop.get(cn)
    if not shop_d:
        print(f"  WARN: top-100 codename {cn} has no Shopify data; skipping")
        continue

    material = extract_material(shop_d["title"], shop_d["description"])
    color    = extract_color_conservative(shop_d["title"], shop_d["tags"], shop_d.get("option_color",""))
    feature  = extract_feature(shop_d["title"], shop_d["description"])
    widths_display, widths_list = format_widths(shop_d["widths_set"])
    new_title = build_title(material, widths_display, color, feature)
    new_desc  = build_description(material, shop_d["description"])
    new_tags  = build_tags(material, color, feature)
    price     = shop_d["first_price"] or "169.00"
    photo1    = shop_d["first_featured"]

    # Section based on material+color
    section_map = {
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
    }
    section = section_map.get(color, "Tungsten Rings")
    # Wood inlay override
    if feature in ("Wood Inlay", "Koa Wood", "Box Elder Wood", "Olive Wood", "Whiskey Barrel"):
        section = "Wood Inlay Wedding Bands"

    # Build variant rows per width × size
    sorted_sizes = sorted(shop_d["sizes_set"], key=lambda x: float(x)) if shop_d["sizes_set"] else ["7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12"]
    sorted_widths = widths_list

    # Master row (first row of listing block)
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
        "Production partners": "",
        "Section": section,
        "Price": price,
        "Quantity": "10",
        "SKU": cn,
        "Variation 1": "Width" if len(sorted_widths) > 1 else "Ring size",
        "V1 Option": sorted_widths[0] if len(sorted_widths) > 1 else sorted_sizes[0],
        "Variation 2": "Ring size" if len(sorted_widths) > 1 else "",
        "V2 Option": sorted_sizes[0] if len(sorted_widths) > 1 else "",
        "Var Price": price,
        "Var Quantity": "10",
        "Var SKU": f"{cn}-{sorted_widths[0]}-{sorted_sizes[0]}" if len(sorted_widths) > 1 else f"{cn}-{sorted_sizes[0]}",
        "Var Visibility": "TRUE",
        "Var Photo": "",
        "Shipping profile": "All Shipping",
        "Weight": "0.5",
        "Length": "1",
        "Width": "1",
        "Height": "0.5",
        "Return policy": "30 days",
        "Photo 1": photo1,
    })
    new_out_rows.append(master)

    # Additional variant rows (Var Price/Quantity/SKU per combo)
    if len(sorted_widths) > 1:
        for wi, w_val in enumerate(sorted_widths):
            for si, s_val in enumerate(sorted_sizes):
                if wi == 0 and si == 0: continue  # already covered by master
                vrow = {fn: "" for fn in template_fieldnames}
                vrow.update({
                    "V1 Option": w_val,
                    "V2 Option": s_val,
                    "Var Price": price,
                    "Var Quantity": "10",
                    "Var SKU": f"{cn}-{w_val}-{s_val}",
                    "Var Visibility": "TRUE",
                })
                new_out_rows.append(vrow)
    else:
        for si, s_val in enumerate(sorted_sizes):
            if si == 0: continue
            vrow = {fn: "" for fn in template_fieldnames}
            vrow.update({
                "V1 Option": s_val,
                "Var Price": price,
                "Var Quantity": "10",
                "Var SKU": f"{cn}-{s_val}",
                "Var Visibility": "TRUE",
            })
            new_out_rows.append(vrow)

with open(OUT_NEW_VELA, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=template_fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(new_out_rows)
print(f"[B] Wrote: {OUT_NEW_VELA}  ({len(missing_top100)} new listings, {len(new_out_rows)} variant rows)")

# ---------- Preview MD for the 24 keepers ----------
lines = ["# 24 Keepers — Title / Description / Tags Preview", "",
         "Verify each row matches the actual product on Shopify before pushing.", ""]
for p in preview_rows:
    lines += [
        f"## Rank {p['rank']} — LID {p['lid']} (codename `{p['codename']}`)",
        f"**Shopify product:** {p['shop_title']}",
        f"**Extracted:** material={p['material']!r}, color={p['color']!r}, feature={p['feature']!r}, widths={p['widths']!r}",
        f"**NEW Etsy title:** `{p['new_title']}`",
        f"**NEW tags:** {p['new_tags']}",
        f"**NEW desc start:** {p['new_desc_preview']!r}",
        "",
    ]
OUT_REVIEW.write_text("\n".join(lines), encoding="utf-8")
print(f"[Review] Wrote: {OUT_REVIEW}")

print("\nDone.")
