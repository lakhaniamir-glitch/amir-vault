"""Rebuild ALL 4 batches with SKUs that exactly match Shopify.

Key fix: instead of cartesian-product variant generation, iterate ACTUAL Shopify variants
per product so widths/sizes/Var SKUs/prices match Shopify exactly.

For Batch 1 (UPDATE):
  - Keep Listing ID column populated (preserves existing Etsy listing match)
  - Replace ALL variant rows with Shopify's actual variant grid
  - Master SKU = codename, Var SKU = Shopify's exact SKU

For Batches 2-4 (CREATE):
  - Same logic, template format (no Listing ID)
"""
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

KEEP    = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED-v3.csv")
SHOP    = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
ETSY    = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv")
TEMPL   = Path(r"C:\Users\amirl\Downloads\etsy-import-template.csv")
SALES   = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sales-by-product-90d.csv")

OUT_BATCH1 = Path(r"C:\Users\amirl\Downloads\vela-batch-1-keepers-update.csv")
OUT_BATCH2 = Path(r"C:\Users\amirl\Downloads\vela-batch-2-tier-a-create.csv")
OUT_BATCH3 = Path(r"C:\Users\amirl\Downloads\vela-batch-3-tier-b-first.csv")
OUT_BATCH4 = Path(r"C:\Users\amirl\Downloads\vela-batch-4-tier-b-orphans.csv")

# --- Generators (same as before) ---
COLORS_PRI = ["Rose Gold", "Yellow Gold", "Gunmetal", "Black", "Silver", "Gold",
              "Blue", "Green", "Red", "Purple", "Orange", "White", "Pink"]

def primary(sku): return (sku or "").split("-")[0].upper() if sku else ""

def extract_material(shop_title, shop_desc):
    t = (shop_title or "").lower()
    if "14k" in t: return "14k Gold"
    if "10k" in t: return "10k Gold"
    if "ceramic" in t: return "Ceramic"
    if "damascus" in t: return "Damascus Steel"
    if "titanium" in t: return "Titanium"
    if "tungsten" in t: return "Tungsten"
    d = (shop_desc or "")[:300].lower()
    if "14k" in d: return "14k Gold"
    if "ceramic" in d: return "Ceramic"
    if "damascus" in d: return "Damascus Steel"
    if "titanium" in d: return "Titanium"
    return "Tungsten"

def material_short(m): return {"Damascus Steel": "Damascus", "14k Gold": "Gold", "10k Gold": "Gold"}.get(m, m)

def extract_color(shop_title, shop_desc, shop_tags):
    d_first = (shop_desc or "")[:200].lower()
    for c in COLORS_PRI:
        if " " + c.lower() + " " in " " + d_first + " " or d_first.startswith(c.lower()): return c
    t = (shop_title or "").lower()
    for c in COLORS_PRI:
        if " " + c.lower() + " " in " " + t + " " or t.startswith(c.lower()): return c
    return "Black"

FEATURES = [
    ("Opal Inlay", r"\bopal\b"), ("Meteorite", r"\bmeteorite\b"),
    ("Koa Wood", r"\bkoa\b"), ("Box Elder Wood", r"\bbox elder\b"),
    ("Olive Wood", r"\bolive wood\b"), ("Iron Wood", r"\biron[- ]?wood\b"),
    ("Snake Wood", r"\bsnake wood\b"), ("Wood Inlay", r"\bwood\b"),
    ("Carbon Fiber", r"\bcarbon fiber\b"), ("Antler", r"\bantler\b"),
    ("Dinosaur Bone", r"\bdinosaur\b"), ("Abalone", r"\babalone\b"),
    ("Diamond", r"\bdiamond\b"), ("Sapphire", r"\bsapphire\b"),
    ("Fidget Spinner", r"\bspinner\b"), ("Fingerprint", r"\bfingerprint\b"),
    ("Hammered", r"\bhammered\b"), ("Brushed Finish", r"\bbrushed\b"),
    ("Beveled", r"\bbeveled\b"), ("Domed", r"\bdomed\b"),
    ("Pipe Cut", r"\bpipe cut\b"), ("Grooved", r"\bgroove[ds]?\b"),
    ("Faceted", r"\bfaceted\b"), ("Stepped Edge", r"\bstepped edge\b"),
    ("Lava Rock", r"\blava rock\b"),
]
def extract_feature(shop_title, shop_desc):
    t = (shop_title or "").lower()
    for canonical, pat in FEATURES:
        if re.search(pat, t): return canonical
    d = (shop_desc or "")[:400].lower()
    for canonical, pat in FEATURES:
        if re.search(pat, d): return canonical
    return ""

def format_widths_display(width_list):
    if not width_list: return "8mm"
    if len(width_list) == 1: return f"{width_list[0]}mm"
    return f"{width_list[0]}-{width_list[-1]}mm"

def build_title(material, widths_display, color, feature):
    mshort = material_short(material)
    fpart = f" {feature}" if feature else ""
    t = f"{material} Wedding Band for Men, {widths_display} {color} Mens {mshort} Ring{fpart}, Personalized Engraved Ring, Comfort Fit"
    if len(t) > 140:
        t = f"{material} Wedding Band for Men, {widths_display} {color} Mens {mshort} Ring{fpart}, Comfort Fit"
    return t[:140].rstrip(", ")

def clean_text(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    s = s.replace("—", ". ").replace("–", "-")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def build_description(material, shop_desc):
    hook = (f"{material} wedding band for men, engraved and shipped from our Irving, "
            f"Texas workshop. Free engraving, free 2-day FedEx, lifetime sizing. Comfort fit.")
    body = clean_text(shop_desc or "")
    return f"{hook}\n\n{body}" if body else hook

def build_tags(material, color, feature):
    mshort = material_short(material).lower()
    BASE = {
        "Tungsten": ["tungsten ring","mens wedding band","mens wedding ring","mens tungsten ring",
                     "mens tungsten band","personalized ring","engraved ring","tungsten band",
                     "mens ring","wedding band men","comfort fit ring"],
        "Ceramic": ["ceramic ring","mens wedding band","mens wedding ring","mens ceramic ring",
                    "ceramic wedding band","personalized ring","engraved ring","ceramic band",
                    "mens ring","wedding band men","comfort fit ring"],
        "Damascus Steel": ["damascus ring","mens wedding band","mens wedding ring","damascus steel ring",
                           "damascus band","personalized ring","engraved ring","mens ring",
                           "wedding band men","comfort fit ring","anniversary gift"],
        "Titanium": ["titanium ring","mens wedding band","mens wedding ring","mens titanium ring",
                     "titanium wedding band","personalized ring","engraved ring","titanium band",
                     "mens ring","wedding band men","comfort fit ring"],
        "14k Gold": ["gold ring","mens wedding band","mens wedding ring","14k gold ring",
                     "yellow gold ring","personalized ring","engraved ring","gold band",
                     "mens ring","wedding band men","comfort fit ring","anniversary gift"],
    }
    base = BASE.get(material, BASE["Tungsten"])
    extra = []
    color_l = color.lower()
    color_tag = f"{color_l} {mshort} ring"
    if len(color_tag) <= 20: extra.append(color_tag)
    elif len(f"{color_l} ring") <= 20: extra.append(f"{color_l} ring")
    if feature:
        ft = f"{feature.lower()} ring"
        if len(ft) <= 20: extra.append(ft)
    tags = base + extra
    seen, dedup = set(), []
    for t in tags:
        if t not in seen and len(t) <= 20:
            seen.add(t); dedup.append(t)
    return ",".join(dedup[:13])

def is_non_ring(title, section):
    t = (title or "").lower()
    s = (section or "").lower()
    for kw in ["dog tag", "fingerprint jewelry", "signet ring", "necklace", "pendant"]:
        if kw in t or kw in s: return True
    return False

SECTION_MAP = {
    "Black": "Black Wedding Bands", "Silver": "Tungsten Rings",
    "Rose Gold": "Rose Gold Wedding Bands", "Yellow Gold": "Gold Wedding Bands",
    "Gold": "Gold Wedding Bands", "Blue": "Blue Wedding Bands",
    "Green": "Green Wedding Bands", "Red": "Red Wedding Bands",
    "Purple": "Purple Wedding Bands", "Orange": "Orange Wedding Bands",
    "Gunmetal": "Tungsten Rings", "White": "Tungsten Rings",
}

# --- Load Shopify with FULL variant data per codename ---
print("Loading Shopify with full variant grid...")
shop_master = {}
shop_variants_grid = defaultdict(list)  # codename -> list of variant dicts in their original order

with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = primary(sku)
        if not cn: continue
        if cn not in shop_master:
            shop_master[cn] = {
                "title": (r.get("title") or "").strip(),
                "description": (r.get("description") or "").strip(),
                "tags": (r.get("tags") or "").strip(),
                "handle": (r.get("handle") or "").strip(),
                "first_sku": sku,
                "first_price": (r.get("price") or "").strip(),
                "featured_image": (r.get("featured_image_url") or "").strip(),
                "additional_images": [],
                "url": (r.get("absolute_product_url") or "").strip(),
            }
            for i in range(1, 6):
                u = (r.get(f"additional_image_url_{i}") or "").strip()
                if u: shop_master[cn]["additional_images"].append(u)
        try: inv = int(r.get("inventory_quantity") or 0)
        except: inv = 0
        shop_variants_grid[cn].append({
            "sku": sku,
            "variant_title": (r.get("variant_title") or "").strip(),
            "price": (r.get("price") or "").strip(),
            "inv": inv,
            "option_color": (r.get("option_color") or "").strip(),
        })

print(f"Loaded Shopify: {len(shop_master)} codenames, {sum(len(v) for v in shop_variants_grid.values())} variants")

def parse_variant_options(variant_title, sku=""):
    """Parse variant_title like '8mm / 7' or '8mm / 7.5' or '8' or '7' into (width, size).
    Falls back to parsing the SKU if variant_title doesn't yield them."""
    vt = variant_title.strip()
    # 'Nmm / S' pattern
    m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
    if m: return m.group(1), m.group(2)
    # 'N / S' pattern (no mm marker)
    m = re.match(r"^(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)$", vt)
    if m: return m.group(1), m.group(2)
    # Just 'Nmm' (single width, no size)
    m = re.match(r"^(\d+(?:\.\d+)?)\s*mm$", vt)
    if m: return m.group(1), ""
    # Just 'S' (just size)
    m = re.match(r"^(\d+(?:\.\d+)?)$", vt)
    if m: return "", m.group(1)
    # SKU fallback: CODENAME-WIDTH-SIZE pattern (e.g., NYMERIA-4-4.5, JDTR776-8-7)
    if sku:
        parts = sku.split("-")
        # Try (codename, width, size) — last two parts are numeric
        if len(parts) >= 3:
            try:
                width = parts[-2]
                size = parts[-1]
                float(width); float(size)  # validate they're numeric
                return width, size
            except ValueError:
                pass
        # Try (codename, size) — last one is numeric
        if len(parts) == 2:
            try:
                float(parts[-1])
                return "", parts[-1]
            except ValueError:
                pass
    return "", ""

def get_widths_sizes(codename):
    """Return sorted lists of unique widths and sizes for a codename."""
    widths, sizes = set(), set()
    for v in shop_variants_grid.get(codename, []):
        w, s = parse_variant_options(v["variant_title"], v["sku"])
        if w: widths.add(w)
        if s: sizes.add(s)
    return sorted(widths, key=float), sorted(sizes, key=float)

# --- Manual overrides (color/feature where formula misses) ---
OVERRIDES = {
    "JDTR131": {"color": "Silver", "feature": "Gold Groove"},
    "JDTR661": {"color": "Black", "feature": "Silver Groove"},
    "JDTR880": {"color": "Black", "feature": "Rose Gold Groove"},
    "AYTR435": {"color": "Black", "feature": "Blue Groove"},
    "AYTR591": {"color": "Black", "feature": "Green Groove"},
    "AYTR563": {"color": "Black", "feature": "Gold Groove"},
    "AYTR588": {"color": "Black", "feature": "Green Groove"},
    "AYTR330": {"color": "Silver", "feature": "Brushed Finish"},
    "AYTR259": {"color": "Black", "feature": "Hammered"},
    "ZEUS": {"color": "Silver", "feature": "Rose Gold Groove"},
    "REVOLVE": {"color": "Black", "feature": "Fidget Spinner"},
    "AYTR031": {"color": "Black", "feature": "Orange Groove"},
    "DOMINUS": {"color": "Silver", "feature": "Domed"},
    "AYTR412": {"color": "Blue", "feature": "Brushed Finish"},
    "AYTR052": {"color": "Black", "feature": "Snake Wood"},
    "AYTR080": {"color": "Silver", "feature": "Iron Wood"},
    "JDTR115": {"color": "Black", "feature": "Silver Stripe"},
    "AYTR030": {"color": "Black", "feature": "Green Groove"},
    "AYTR001": {"color": "Black", "feature": "Red Inlay"},
    "AYTR005": {"color": "Black", "feature": "Red Inside"},
    "JDTR226": {"color": "Silver", "feature": "Celtic Design"},
}

USER_DISCONTINUED = {"ADC023", "KNIGHT"}

# --- Load remaining data ---
with open(ETSY, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    etsy_fieldnames = list(reader.fieldnames)
    etsy_rows = list(reader)
etsy_blocks = {}
current = None
for i, r in enumerate(etsy_rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current: etsy_blocks[current["lid"]] = current
        current = {"lid": lid, "rows": [i]}
    elif current: current["rows"].append(i)
if current: etsy_blocks[current["lid"]] = current

with open(TEMPL, encoding="utf-8-sig") as f:
    template_fieldnames = list(csv.DictReader(f).fieldnames)

keep_rows = []
with open(KEEP, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        keep_rows.append(r)

# Partition into batches
batch1 = [r for r in keep_rows if r["status"] == "EXISTING_KEEP" and r["lid"]]
batch2_pool = [r for r in keep_rows if r["status"] == "NEW_TIER_A_HAS_IMAGE"
               and r["codename"] not in USER_DISCONTINUED
               and r["codename"] and r["codename"] not in {"?",""}]
tier_b = [r for r in keep_rows if r["status"] == "NEW_TIER_B_NEED_IMAGE"]
half = len(tier_b) // 2
batch3 = tier_b[:half]
batch4 = tier_b[half:] + [r for r in keep_rows
                           if r["status"] == "NEW_HAS_IMAGES_FETCH_DATA"
                           and r["codename"] in shop_master]

print(f"\nBatches: B1={len(batch1)}, B2={len(batch2_pool)}, B3={len(batch3)}, B4={len(batch4)}")

# --- Builder using REAL Shopify variants ---
def build_listing_with_shopify_variants(codename, lid=None):
    shop_d = shop_master.get(codename)
    if not shop_d:
        # Orphan fallback — should be filtered already
        return None
    variants = shop_variants_grid.get(codename, [])
    if not variants:
        return None

    material = extract_material(shop_d["title"], shop_d["description"])
    color = extract_color(shop_d["title"], shop_d["description"], shop_d.get("tags", ""))
    feature = extract_feature(shop_d["title"], shop_d["description"])
    if codename in OVERRIDES:
        color = OVERRIDES[codename].get("color", color)
        feature = OVERRIDES[codename].get("feature", feature)

    widths, sizes = get_widths_sizes(codename)
    width_display = format_widths_display(widths)
    new_title = build_title(material, width_display, color, feature)
    new_desc = build_description(material, shop_d["description"])
    new_tags = build_tags(material, color, feature)
    section = SECTION_MAP.get(color, "Tungsten Rings")
    if feature.lower() in {"wood inlay","koa wood","box elder wood","olive wood",
                             "snake wood","iron wood","whiskey barrel"}:
        section = "Wood Inlay Wedding Bands"

    # Is non-ring? Keep original title AND original variant structure in update mode
    is_nonring = False
    if lid and lid in etsy_blocks:
        original = etsy_rows[etsy_blocks[lid]["rows"][0]]
        is_nonring = is_non_ring(original.get("Title",""), original.get("Section",""))

    # For non-ring UPDATE: preserve original variant grid (don't overwrite with ring SKUs)
    if is_nonring and lid and lid in etsy_blocks:
        return [dict(etsy_rows[ri]) for ri in etsy_blocks[lid]["rows"]], etsy_fieldnames

    rows = []

    # Build first row (master) based on UPDATE vs CREATE
    if lid:
        # UPDATE mode: use Etsy fieldnames
        # Pull the original master row to preserve all unchanged columns
        original_first = dict(etsy_rows[etsy_blocks[lid]["rows"][0]])
        master = dict(original_first)
        master["Listing ID"] = lid
        if not is_nonring:
            master["Title"] = new_title
            master["Description"] = new_desc
            master["Tags"] = new_tags
            master["Section"] = section
        master["SKU"] = codename
        # Set up variation labels
        if widths and sizes:
            master["Variation 1"] = "Width"
            master["Variation 2"] = "Ring size"
            master["V1 Option"] = widths[0]
            master["V2 Option"] = sizes[0]
        elif sizes:
            master["Variation 1"] = "Ring size"
            master["Variation 2"] = ""
            master["V1 Option"] = sizes[0]
            master["V2 Option"] = ""
        # Use first Shopify variant as master variant info
        first_v = variants[0]
        master["Var Price"] = first_v["price"]
        master["Var Quantity"] = "10"
        master["Var SKU"] = first_v["sku"]
        master["Var Visibility"] = "TRUE"
        master["Price"] = shop_d["first_price"]
        master["Quantity"] = "10"
        rows.append(master)
        fieldnames = etsy_fieldnames
    else:
        # CREATE mode: template fieldnames
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
            "Price": shop_d["first_price"] or "149.00",
            "Quantity": "10",
            "SKU": codename,
            "Shipping profile": "All Shipping",
            "Weight": "0.5", "Length": "1", "Width": "1", "Height": "0.5",
            "Return policy": "30 days",
            "Photo 1": shop_d["featured_image"],
        })
        for idx, img in enumerate(shop_d["additional_images"][:5], start=2):
            master[f"Photo {idx}"] = img
        first_v = variants[0]
        if widths and sizes:
            master["Variation 1"] = "Width"
            master["Variation 2"] = "Ring size"
            master["V1 Option"] = widths[0]
            master["V2 Option"] = sizes[0]
        elif sizes:
            master["Variation 1"] = "Ring size"
            master["V1 Option"] = sizes[0]
        master["Var Price"] = first_v["price"]
        master["Var Quantity"] = "10"
        master["Var SKU"] = first_v["sku"]
        master["Var Visibility"] = "TRUE"
        rows.append(master)
        fieldnames = template_fieldnames

    # Add ALL remaining Shopify variants as variant rows (skip first, already in master)
    for v in variants[1:]:
        w, s = parse_variant_options(v["variant_title"], v["sku"])
        vrow = {fn: "" for fn in fieldnames}
        if widths and sizes:
            vrow["V1 Option"] = w or widths[0]
            vrow["V2 Option"] = s or sizes[0]
        elif sizes:
            vrow["V1 Option"] = s
        vrow["Var Price"] = v["price"]
        vrow["Var Quantity"] = "10"
        vrow["Var SKU"] = v["sku"]  # EXACT Shopify SKU
        vrow["Var Visibility"] = "TRUE"
        rows.append(vrow)

    return rows, fieldnames

def write_batch(path, all_rows, fieldnames):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        w.writeheader()
        for rs in all_rows:
            w.writerows(rs)

# Build each batch
print("\nBuilding...")
b1_all, b1_fn = [], etsy_fieldnames
for k in batch1:
    result = build_listing_with_shopify_variants(k["codename"], k["lid"])
    if result:
        rows, _ = result
        b1_all.append(rows)
    else:
        # Codename not in Shopify (38 revenue listings might be in this bucket)
        # Fall back to preserving the existing Etsy listing as-is
        block = etsy_blocks.get(k["lid"])
        if block:
            preserved = [dict(etsy_rows[ri]) for ri in block["rows"]]
            b1_all.append(preserved)
write_batch(OUT_BATCH1, b1_all, b1_fn)
print(f"  B1: {len(b1_all)} listings, {sum(len(r) for r in b1_all)} rows")

for batch, out_path, name in [(batch2_pool, OUT_BATCH2, "B2"),
                                (batch3, OUT_BATCH3, "B3"),
                                (batch4, OUT_BATCH4, "B4")]:
    b_all = []
    for k in batch:
        result = build_listing_with_shopify_variants(k["codename"])
        if result:
            rows, _ = result
            b_all.append(rows)
    write_batch(out_path, b_all, template_fieldnames)
    print(f"  {name}: {len(b_all)} listings, {sum(len(r) for r in b_all)} rows")

print("\nDone. All batches now use exact Shopify variant SKUs.")
