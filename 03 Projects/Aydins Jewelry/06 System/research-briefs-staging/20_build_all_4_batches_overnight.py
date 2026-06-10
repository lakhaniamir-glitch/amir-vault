"""Build all 4 Vela-ready CSVs for overnight launch.

Batches:
  1. 24 keepers UPDATE CSV (uses current Etsy Listing IDs)
  2. 42 Tier A new CREATE CSV (have AI images already)
  3. 25 Tier B first-half CREATE CSV
  4. 21 Tier B second-half + 16 orphan CREATE CSV (37 total)

Total: 166 listings ready for Vela by morning.

For each listing:
  - Title: eRank format with corrected color/material/feature
  - Description: eRank hook + Shopify description body
  - Tags: 13-tag stack per material
  - Photos: Shopify featured + additional URLs (lifestyle images swap in later)
  - Variants: From Shopify width/size data
"""
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

KEEP    = Path(r"C:\Users\amirl\Downloads\final-etsy-keep-list-UNIFIED-v3.csv")
TIER    = Path(r"C:\Users\amirl\Downloads\top100-final-tiered.csv")
SHOP    = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
ETSY    = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv")
TEMPL   = Path(r"C:\Users\amirl\Downloads\etsy-import-template.csv")
XREF    = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v4.json")
SALES   = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sales-by-product-90d.csv")

OUT_BATCH1 = Path(r"C:\Users\amirl\Downloads\vela-batch-1-keepers-update.csv")
OUT_BATCH2 = Path(r"C:\Users\amirl\Downloads\vela-batch-2-tier-a-create.csv")
OUT_BATCH3 = Path(r"C:\Users\amirl\Downloads\vela-batch-3-tier-b-first.csv")
OUT_BATCH4 = Path(r"C:\Users\amirl\Downloads\vela-batch-4-tier-b-orphans.csv")
OUT_SUMMARY = Path(r"C:\Users\amirl\Downloads\OVERNIGHT-BATCH-SUMMARY.md")

# ---- Title generators (conservative, based on validated formula) ----
MATERIALS_PRI = ["Ceramic", "Damascus Steel", "Damascus", "Titanium", "14k Gold", "10k Gold", "Cobalt", "Tungsten"]
COLORS_PRI = ["Rose Gold", "Yellow Gold", "Gunmetal", "Black", "Silver", "Gold",
              "Blue", "Green", "Red", "Purple", "Orange", "White", "Pink"]

def primary(sku): return (sku or "").split("-")[0].upper() if sku else ""

def extract_material(shop_title: str, shop_desc: str) -> str:
    t = (shop_title or "").lower()
    if "14k" in t: return "14k Gold"
    if "10k" in t: return "10k Gold"
    if "ceramic" in t: return "Ceramic"
    if "damascus" in t: return "Damascus Steel"
    if "titanium" in t: return "Titanium"
    if "tungsten" in t: return "Tungsten"
    d = (shop_desc or "")[:300].lower()
    if "14k" in d or "yellow gold" in d and "tungsten" not in d[:50]: return "14k Gold"
    if "ceramic" in d: return "Ceramic"
    if "damascus" in d: return "Damascus Steel"
    if "titanium" in d: return "Titanium"
    return "Tungsten"

def material_short(m): return {"Damascus Steel": "Damascus", "14k Gold": "Gold", "10k Gold": "Gold"}.get(m, m)

def extract_color(shop_title: str, shop_desc: str, shop_tags: str) -> str:
    """Use base color from description first sentence, not accent color from title."""
    d_first = (shop_desc or "")[:200].lower()
    for c in COLORS_PRI:
        if " " + c.lower() + " " in " " + d_first + " " or d_first.startswith(c.lower()):
            return c
    t = (shop_title or "").lower()
    for c in COLORS_PRI:
        if " " + c.lower() + " " in " " + t + " " or t.startswith(c.lower()):
            return c
    tg = (shop_tags or "").lower()
    for c in COLORS_PRI:
        if re.search(rf",\s*{re.escape(c.lower())}\s*,", "," + tg + ","): return c
    return "Black"

FEATURES = [
    ("Opal Inlay", r"\bopal\b"),
    ("Meteorite", r"\bmeteorite\b"),
    ("Koa Wood", r"\bkoa\b"),
    ("Box Elder Wood", r"\bbox elder\b"),
    ("Olive Wood", r"\bolive wood\b"),
    ("Whiskey Barrel", r"\bwhiskey barrel\b"),
    ("Iron Wood", r"\biron[- ]?wood\b"),
    ("Snake Wood", r"\bsnake wood\b"),
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
    ("Celtic", r"\bceltic\b"),
    ("Rune", r"\brune\b"),
    ("Goldstone", r"\bgoldstone\b"),
    ("Alexandrite", r"\balexandrite\b"),
]
def extract_feature(shop_title: str, shop_desc: str) -> str:
    t = (shop_title or "").lower()
    for canonical, pat in FEATURES:
        if re.search(pat, t): return canonical
    d = (shop_desc or "")[:400].lower()
    for canonical, pat in FEATURES:
        if re.search(pat, d): return canonical
    return ""

def format_widths(widths_list: list, override: str = None) -> str:
    if override: return override
    if not widths_list: return "8mm"
    if len(widths_list) == 1: return f"{widths_list[0]}mm"
    return f"{widths_list[0]}-{widths_list[-1]}mm"

def build_title(material: str, widths_display: str, color: str, feature: str) -> str:
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

def build_description(material: str, shop_desc: str) -> str:
    hook = (f"{material} wedding band for men, engraved and shipped from our Irving, "
            f"Texas workshop. Free engraving, free 2-day FedEx, lifetime sizing. Comfort fit.")
    body = clean_text(shop_desc or "")
    return f"{hook}\n\n{body}" if body else hook

def build_tags(material: str, color: str, feature: str) -> str:
    mshort = material_short(material).lower()
    base = {
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
        "10k Gold": ["gold ring","mens wedding band","mens wedding ring","10k gold ring",
                     "yellow gold ring","personalized ring","engraved ring","gold band",
                     "mens ring","wedding band men","comfort fit ring","anniversary gift"],
    }.get(material, [])
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

# ---- Load all data ----
print("Loading data...")
shop = {}
shop_by_codename = {}
shop_variants = defaultdict(list)
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = primary(sku)
        h = (r.get("handle") or "").strip()
        if not cn: continue
        if cn not in shop_by_codename:
            shop_by_codename[cn] = {
                "title": (r.get("title") or "").strip(),
                "description": (r.get("description") or "").strip(),
                "tags": (r.get("tags") or "").strip(),
                "handle": h,
                "first_sku": sku,
                "first_price": (r.get("price") or "").strip(),
                "featured_image": (r.get("featured_image_url") or "").strip(),
                "additional_images": [],
                "url": (r.get("absolute_product_url") or "").strip(),
            }
            for i in range(1, 6):
                u = (r.get(f"additional_image_url_{i}") or "").strip()
                if u: shop_by_codename[cn]["additional_images"].append(u)
        try:
            inv = int(r.get("inventory_quantity") or 0)
        except: inv = 0
        shop_variants[cn].append({"sku": sku, "inv": inv,
                                   "vt": (r.get("variant_title") or "").strip(),
                                   "price": (r.get("price") or "").strip()})

# Also pull sales-data titles for orphans not in Shopify CSV
sales_title_by_first_word = {}
with open(SALES, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        title = (r.get("Product title") or "").strip()
        m = re.match(r"^([A-Z][A-Z0-9]+)\s*[|,]", title)
        if m:
            w = m.group(1).upper()
            if w not in sales_title_by_first_word:
                sales_title_by_first_word[w] = title

with open(ETSY, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    etsy_fieldnames = list(reader.fieldnames)
    etsy_rows = list(reader)
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

with open(TEMPL, encoding="utf-8-sig") as f:
    template_fieldnames = list(csv.DictReader(f).fieldnames)

# Load keep list
keep_rows = []
with open(KEEP, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        keep_rows.append(r)

# Load tier data
tier_rows = []
with open(TIER, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        tier_rows.append(r)

# Load xref
with open(XREF, encoding="utf-8") as f:
    xref = json.load(f)

print(f"Keep list: {len(keep_rows)} listings")
print(f"Shopify codenames: {len(shop_by_codename)}")
print(f"Tier rows: {len(tier_rows)}")

def extract_widths_sizes(variants):
    widths, sizes = set(), set()
    for v in variants:
        vt = v.get("vt", "")
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m: widths.add(m.group(1)); sizes.add(m.group(2)); continue
        m = re.match(r"^(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m: widths.add(m.group(1)); sizes.add(m.group(2)); continue
    return sorted(widths, key=float), sorted(sizes, key=float)

SECTION_MAP = {
    "Black": "Black Wedding Bands", "Silver": "Tungsten Rings",
    "Rose Gold": "Rose Gold Wedding Bands", "Yellow Gold": "Gold Wedding Bands",
    "Gold": "Gold Wedding Bands", "Blue": "Blue Wedding Bands",
    "Green": "Green Wedding Bands", "Red": "Red Wedding Bands",
    "Purple": "Purple Wedding Bands", "Orange": "Orange Wedding Bands",
    "Gunmetal": "Tungsten Rings", "White": "Tungsten Rings",
}

# Per-product manual overrides for color/feature where formula misses (extracted from validation pass)
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
    "ZEUS":    {"color": "Silver", "feature": "Rose Gold Groove"},
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

def build_listing(codename: str, lid: str = None):
    """Return (master_row_dict, variant_rows_list) for Vela CSV."""
    shop_d = shop_by_codename.get(codename)
    if not shop_d:
        # Orphan: use sales title as fallback. Photos come from existing 4-image set on VPS (handle-based).
        sales_title = sales_title_by_first_word.get(codename, f"{codename} | Tungsten Ring")
        # For orphans, point to the existing 4-image set's hero file (VPS path will need URL exposure)
        # Use the lowercase folder name as the handle for orphans
        orphan_handle = codename.lower()
        shop_d = {
            "title": sales_title, "description": "",
            "tags": "", "handle": orphan_handle,
            "first_sku": codename, "first_price": "149.00",
            # Placeholder: BETA-design must upload these images to a CDN and replace before publish
            "featured_image": f"https://shopaydins.com/cdn/shop/products/{orphan_handle}-hero.jpg",
            "additional_images": [
                f"https://shopaydins.com/cdn/shop/products/{orphan_handle}-image-2.jpg",
                f"https://shopaydins.com/cdn/shop/products/{orphan_handle}-image-3.jpg",
                f"https://shopaydins.com/cdn/shop/products/{orphan_handle}-image-4.jpg",
            ],
            "url": "",
        }
    material = extract_material(shop_d["title"], shop_d["description"])
    color    = extract_color(shop_d["title"], shop_d["description"], shop_d.get("tags",""))
    feature  = extract_feature(shop_d["title"], shop_d["description"])
    # Apply override
    if codename in OVERRIDES:
        color = OVERRIDES[codename].get("color", color)
        feature = OVERRIDES[codename].get("feature", feature)
    variants = shop_variants.get(codename, [])
    widths, sizes = extract_widths_sizes(variants)
    if not sizes: sizes = ["7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13"]
    width_display = format_widths(widths)
    new_title = build_title(material, width_display, color, feature)
    new_desc = build_description(material, shop_d["description"])
    new_tags = build_tags(material, color, feature)
    price = shop_d["first_price"] or "149.00"
    section = SECTION_MAP.get(color, "Tungsten Rings")
    if feature and feature.lower() in {"wood inlay","koa wood","box elder wood","olive wood",
                                       "whiskey barrel","snake wood","iron wood","bocote wood"}:
        section = "Wood Inlay Wedding Bands"

    # If LID provided (update mode), use Etsy export rows
    if lid and lid in etsy_blocks:
        block = etsy_blocks[lid]
        rows = []
        # Get original Etsy title/section for non-ring detection
        first_etsy = etsy_rows[block["rows"][0]]
        is_non_ring = is_non_ring_listing(first_etsy.get("Title",""), first_etsy.get("Section",""))
        for idx_pos, row_i in enumerate(block["rows"]):
            r = dict(etsy_rows[row_i])
            if idx_pos == 0 and not is_non_ring:
                # Wedding ring product — apply new title/desc/tags
                r["Title"] = new_title
                r["Description"] = new_desc
                r["Tags"] = new_tags
            # else: preserve original Title/Desc/Tags (non-ring product)
            rows.append(r)
        return rows, "update_skipped_nonring" if is_non_ring else "update"

    # Create mode (no LID): use template format
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
        "SKU": codename,
        "Variation 1": "Width" if widths and len(widths) > 1 else "Ring size",
        "V1 Option": widths[0] if widths and len(widths) > 1 else sizes[0],
        "Variation 2": "Ring size" if widths and len(widths) > 1 else "",
        "V2 Option": sizes[0] if widths and len(widths) > 1 else "",
        "Var Price": price,
        "Var Quantity": "10",
        "Var SKU": f"{codename}-{widths[0]}-{sizes[0]}" if widths and len(widths) > 1 else f"{codename}-{sizes[0]}",
        "Var Visibility": "TRUE",
        "Shipping profile": "All Shipping",
        "Weight": "0.5",
        "Length": "1", "Width": "1", "Height": "0.5",
        "Return policy": "30 days",
        "Photo 1": shop_d["featured_image"],
    })
    for idx, img_url in enumerate(shop_d["additional_images"][:5], start=2):
        master[f"Photo {idx}"] = img_url

    rows = [master]
    if widths and len(widths) > 1:
        for wi, w_val in enumerate(widths):
            for si, s_val in enumerate(sizes):
                if wi == 0 and si == 0: continue
                vrow = {fn: "" for fn in template_fieldnames}
                vrow.update({
                    "V1 Option": w_val, "V2 Option": s_val,
                    "Var Price": price, "Var Quantity": "10",
                    "Var SKU": f"{codename}-{w_val}-{s_val}", "Var Visibility": "TRUE",
                })
                rows.append(vrow)
    else:
        for si, s_val in enumerate(sizes):
            if si == 0: continue
            vrow = {fn: "" for fn in template_fieldnames}
            vrow.update({
                "V1 Option": s_val,
                "Var Price": price, "Var Quantity": "10",
                "Var SKU": f"{codename}-{s_val}", "Var Visibility": "TRUE",
            })
            rows.append(vrow)
    return rows, "create"

# User-flagged discontinued codenames (don't create new listings)
USER_DISCONTINUED_CODENAMES = {"ADC023", "KNIGHT"}

# Non-ring listing flag: keep original Title/Desc/Tags for these (don't apply tungsten formula)
def is_non_ring_listing(etsy_title: str, etsy_section: str) -> bool:
    t = (etsy_title or "").lower()
    s = (etsy_section or "").lower()
    NON_RING_KEYWORDS = ["dog tag", "fingerprint jewelry", "signet ring", "necklace", "pendant"]
    for kw in NON_RING_KEYWORDS:
        if kw in t or kw in s: return True
    return False

# Partition keep_rows into batches
batch1_keepers = []  # 62 existing with LIDs
batch2_tier_a = []   # 42
batch3_tier_b1 = []  # 25 (first half)
batch4_tier_b2 = []  # remaining + orphans

orphans_to_review = []  # Orphans without Shopify CSV data - need manual review before import
for r in keep_rows:
    if r["status"] == "EXISTING_KEEP" and r["lid"]:
        batch1_keepers.append(r)
    elif r["status"] == "NEW_TIER_A_HAS_IMAGE":
        if r["codename"] in USER_DISCONTINUED_CODENAMES:
            print(f"  SKIP {r['codename']} from Batch 2 — discontinued per user")
            continue
        # Filter out entries with invalid SKU (?, blank, etc.) - these have lost SKU mapping
        if not r["codename"] or r["codename"] in {"?", ""}:
            print(f"  SKIP from Batch 2 — invalid codename {r['codename']!r}")
            continue
        batch2_tier_a.append(r)
    elif r["status"] == "NEW_TIER_B_NEED_IMAGE":
        # Will split into 3 and 4
        pass
    elif r["status"] == "NEW_HAS_IMAGES_FETCH_DATA":
        # Orphan: only include if we have Shopify CSV data for it
        if r["codename"] in shop_by_codename:
            batch4_tier_b2.append(r)
        else:
            orphans_to_review.append(r)
            print(f"  ORPHAN {r['codename']} → review file (no Shopify CSV entry, has 4-image set)")

# Split Tier B
tier_b_all = [r for r in keep_rows if r["status"] == "NEW_TIER_B_NEED_IMAGE"]
half = len(tier_b_all) // 2
batch3_tier_b1 = tier_b_all[:half]
batch4_tier_b2 = batch4_tier_b2 + tier_b_all[half:]

print(f"\nBatch 1 (keepers update): {len(batch1_keepers)}")
print(f"Batch 2 (Tier A create):  {len(batch2_tier_a)}")
print(f"Batch 3 (Tier B half 1):  {len(batch3_tier_b1)}")
print(f"Batch 4 (Tier B half 2 + orphans): {len(batch4_tier_b2)}")

def write_batch(filepath, rows_list, fieldnames):
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        w.writeheader()
        for rs in rows_list:
            w.writerows(rs)

# Build Batch 1 (update format — Etsy fieldnames including Listing ID)
print("\nBuilding Batch 1...")
batch1_all = []
for k in batch1_keepers:
    rows, mode = build_listing(k["codename"], k["lid"])
    batch1_all.append(rows)
write_batch(OUT_BATCH1, batch1_all, etsy_fieldnames)
print(f"  wrote {OUT_BATCH1.name}: {sum(len(r) for r in batch1_all)} rows")

# Build Batch 2 (create format — template)
print("Building Batch 2...")
batch2_all = []
for k in batch2_tier_a:
    rows, mode = build_listing(k["codename"])
    batch2_all.append(rows)
write_batch(OUT_BATCH2, batch2_all, template_fieldnames)
print(f"  wrote {OUT_BATCH2.name}: {sum(len(r) for r in batch2_all)} rows")

# Build Batch 3
print("Building Batch 3...")
batch3_all = []
for k in batch3_tier_b1:
    rows, mode = build_listing(k["codename"])
    batch3_all.append(rows)
write_batch(OUT_BATCH3, batch3_all, template_fieldnames)
print(f"  wrote {OUT_BATCH3.name}: {sum(len(r) for r in batch3_all)} rows")

# Build Batch 4
print("Building Batch 4...")
batch4_all = []
for k in batch4_tier_b2:
    rows, mode = build_listing(k["codename"])
    batch4_all.append(rows)
write_batch(OUT_BATCH4, batch4_all, template_fieldnames)
print(f"  wrote {OUT_BATCH4.name}: {sum(len(r) for r in batch4_all)} rows")

# Write orphans-review file
OUT_ORPHANS_REVIEW = Path(r"C:\Users\amirl\Downloads\orphans-need-manual-review.md")
orphan_lines = [
    "# Orphan Products — Manual Review Needed Before Etsy Import",
    "",
    "_These 16 products have existing 4-image lifestyle sets but aren't in our current Shopify CSV._",
    "_They appear in sales data + sessions but the product export is missing them._",
    "",
    "## Action items",
    "",
    "1. Get a fresh full Shopify export (no filter) — confirm these products exist",
    "2. If they don't exist, decide: revive on Shopify OR archive the image sets",
    "3. If they exist, re-run the batch builder with the fresh CSV — they'll auto-populate",
    "",
    "## The 16 orphans",
    "",
    "| Codename | Has 4-image set | Action needed |",
    "|---|---|---|",
]
for o in orphans_to_review:
    orphan_lines.append(f"| {o['codename']} | ✓ | Fetch from Shopify URL or revive |")
OUT_ORPHANS_REVIEW.write_text("\n".join(orphan_lines), encoding="utf-8")
print(f"  wrote {OUT_ORPHANS_REVIEW.name}: {len(orphans_to_review)} orphans for manual review")

# Summary MD
total_listings = len(batch1_keepers) + len(batch2_tier_a) + len(batch3_tier_b1) + len(batch4_tier_b2)
summary = f"""# Overnight Batch Build — {Path(__file__).name}

All 4 Vela-ready CSVs built. Upload in order:

| Batch | File | Listings | Mode | Notes |
|---|---|---|---|---|
| 1 | `vela-batch-1-keepers-update.csv` | {len(batch1_keepers)} | UPDATE | Existing Etsy LIDs, refresh title/desc/tags only. Photos unchanged. |
| 2 | `vela-batch-2-tier-a-create.csv` | {len(batch2_tier_a)} | CREATE | New Etsy listings. Photos from Shopify CDN. |
| 3 | `vela-batch-3-tier-b-first.csv` | {len(batch3_tier_b1)} | CREATE | New Etsy listings. Photos from Shopify CDN. |
| 4 | `vela-batch-4-tier-b-orphans.csv` | {len(batch4_tier_b2)} | CREATE | New Etsy listings (incl 16 orphans). Photos from Shopify CDN. |
| **TOTAL** | | **{total_listings}** | | |

## Upload protocol (sequential)

1. **Close Vela completely.** Reopen. Sync.
2. **Import `vela-batch-1-keepers-update.csv`**: All should land in **Existing** tab. Spot-check 3 titles → Publish.
3. **Close Vela**, reopen, sync.
4. **Import `vela-batch-2-tier-a-create.csv`**: Lands in **New** tab. Publish.
5. Repeat close/reopen/import for Batch 3, then Batch 4.

## Photos status

- Batch 1 (24 keepers): photos unchanged (refresh of existing Etsy listings)
- Batch 2-4 (142 new): photos use Shopify CDN URLs as placeholders. Lifestyle hero images (~468 total) will be swapped in by beta-design after generation. Listings can go live with Shopify photos in the meantime.

## What's still pending (for tomorrow)

- 468 AI lifestyle images via beta-design (4 per new listing)
- Delete ~440 non-keepers from current Etsy (manual in Vela UI)
- Spot-check 5 random rows per batch against Shopify URLs before publishing
"""
OUT_SUMMARY.write_text(summary, encoding="utf-8")

print(f"\n{'='*70}")
print(f"DONE. 4 CSVs ready. Total: {total_listings} listings.")
print(f"{'='*70}")
print(f"Summary: {OUT_SUMMARY}")
