"""Validate: for every listing that got an updated title, compare it side-by-side with the
ACTUAL Shopify product. Flag mismatches in material/color/feature so we can fix the generator.

Inputs:
  - NEW: AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv (Vela's export AFTER my title push, has new titles applied)
  - Shopify aydinsjewelry.myshopify.com (2).csv (1915 codenames, source of truth)
  - matcher v4 xref (LID -> Shopify codename)

Output: validation-report.json with each listing's:
  - new_etsy_title
  - shopify_title
  - shopify_description_first_line
  - mismatch flags (color, material, feature)
"""
import csv, json, re, sys
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

NEW   = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv")
SHOP  = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
XREF  = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v4.json")
OUT   = Path(r"C:\Users\amirl\Downloads\validation-report.json")
OUT_MD = Path(r"C:\Users\amirl\Downloads\validation-report.md")

with open(XREF, encoding="utf-8") as f:
    xref = json.load(f)
print(f"Xref entries: {len(xref)}")

# Load Shopify by primary codename (FIRST variant only)
shop = {}
def primary(sku):
    return (sku or "").strip().split("-")[0].upper()
def all_in_sku(sku):
    if not sku: return set()
    out = set()
    for tok in re.split(r"[-_/.]", sku.strip().upper()):
        if tok and not tok.isdigit() and not re.match(r"^\d+(\.\d+)?$", tok) and len(tok) >= 3:
            out.add(tok)
    return out

print("Loading Shopify...")
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        if not sku: continue
        cn = primary(sku)
        if cn in shop: continue
        shop[cn] = {
            "title": (r.get("title") or "").strip(),
            "description": (r.get("description") or "").strip(),
            "tags": (r.get("tags") or "").strip(),
            "handle": (r.get("handle") or "").strip(),
            "first_sku": sku,
            "option_color": (r.get("option_color") or "").strip(),
        }
print(f"Shopify primary codenames: {len(shop)}")

# Read NEW export
with open(NEW, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# Group into listings
listings = []
current = None
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: listings.append(current)
        current = {"lid": lid, "rows": [r],
                   "section": (r.get("Section") or "").strip(),
                   "title": (r.get("Title") or "").strip(),
                   "description": (r.get("Description") or "").strip(),
                   "tags": (r.get("Tags") or "").strip()}
    elif current is not None:
        current["rows"].append(r)
if current is not None: listings.append(current)
print(f"Listings in NEW export: {len(listings)}")

# Detect which got updated titles (matches eRank format start: "X Wedding Band for Men, Nmm")
ERANK_FORMAT_RE = re.compile(r"^(\w+(?:\s\w+)?) Wedding Band for Men, \d", re.IGNORECASE)

# Detect color/material/feature in titles
COLORS = ["Rose Gold", "Yellow Gold", "Black", "Silver", "Gold", "Blue", "Green",
          "Red", "Purple", "Orange", "White", "Gunmetal", "Pink"]
MATERIALS = ["Tungsten", "Ceramic", "Damascus Steel", "Damascus", "Titanium", "Cobalt"]

def find_in(text, vocab):
    blob = " " + text.lower() + " "
    out = []
    for v in vocab:
        if " " + v.lower() + " " in blob:
            out.append(v)
    return out

# Validate each
validations = []
for L in listings:
    new_title = L["title"]
    lid = L["lid"]
    var_skus = [(r.get("Var SKU") or "").strip() for r in L["rows"]]
    var_skus = [v for v in var_skus if v]
    etsy_codenames = set()
    for vs in var_skus:
        etsy_codenames |= all_in_sku(vs)
    primary_etsy_cn = primary(var_skus[0]) if var_skus else ""

    # Did this get a new eRank-format title?
    m = ERANK_FORMAT_RE.match(new_title)
    has_new_format = bool(m)
    if not has_new_format:
        continue  # We didn't touch this one — skip validation

    # What does our xref say the Shopify match is?
    xref_entry = xref.get(lid)
    shop_cn = xref_entry["codename"] if xref_entry else ""
    shop_d = shop.get(shop_cn)
    if not shop_d:
        validations.append({
            "lid": lid, "new_title": new_title[:120],
            "issue": "NO_SHOPIFY_MATCH_IN_XREF",
            "etsy_codename": primary_etsy_cn,
            "shop_codename_per_xref": shop_cn,
        })
        continue

    # Get the title material/color from new title
    title_material = (find_in(new_title, MATERIALS) or [""])[0]
    title_color = (find_in(new_title, COLORS) or [""])[0]
    # Get the actual Shopify material/color
    shop_blob = f"{shop_d['title']} {shop_d['description'][:300]}"
    shop_material = (find_in(shop_blob, MATERIALS) or [""])[0]
    shop_colors = find_in(shop_blob, COLORS)
    # Match check
    color_match = title_color in shop_colors if title_color else False
    # Allow Tungsten=='Tungsten' and 'Tungsten Carbide' to count as same
    material_match = (title_material.lower() in shop_material.lower()
                      or shop_material.lower() in title_material.lower())

    issues = []
    if title_color and not color_match:
        issues.append(f"COLOR_MISMATCH: title says {title_color!r}, shop says {shop_colors!r}")
    if title_material and shop_material and not material_match:
        issues.append(f"MATERIAL_MISMATCH: title says {title_material!r}, shop says {shop_material!r}")

    validations.append({
        "lid": lid,
        "etsy_codename": primary_etsy_cn,
        "shop_codename_per_xref": shop_cn,
        "new_etsy_title": new_title,
        "shop_title": shop_d["title"],
        "shop_first_sku": shop_d["first_sku"],
        "shop_handle": shop_d["handle"],
        "shop_first_desc_line": shop_d["description"].split("\n")[0][:200],
        "title_material": title_material,
        "title_color": title_color,
        "shop_material": shop_material,
        "shop_colors": shop_colors,
        "issues": issues,
    })

# Save
OUT.write_text(json.dumps(validations, ensure_ascii=False, indent=2), encoding="utf-8")

# Tally
total_updated = sum(1 for v in validations if "NO_SHOPIFY_MATCH_IN_XREF" not in v.get("issue", ""))
with_issues = [v for v in validations if v.get("issues")]
color_issues = [v for v in with_issues if any("COLOR_MISMATCH" in i for i in v["issues"])]
mat_issues = [v for v in with_issues if any("MATERIAL_MISMATCH" in i for i in v["issues"])]
no_xref = [v for v in validations if v.get("issue") == "NO_SHOPIFY_MATCH_IN_XREF"]

print(f"\n=== VALIDATION ===")
print(f"Listings with new eRank-format title: {len(validations)}")
print(f"  Validated against Shopify: {total_updated}")
print(f"  No Shopify match in xref: {len(no_xref)}")
print(f"  COLOR mismatches: {len(color_issues)}")
print(f"  MATERIAL mismatches: {len(mat_issues)}")
print()
print("=== Sample COLOR mismatches (first 15) ===")
for v in color_issues[:15]:
    print(f"  LID {v['lid']:<12}  etsy_cn={v['etsy_codename']!r}  shop_cn={v['shop_codename_per_xref']!r}")
    print(f"    New title: {v['new_etsy_title'][:120]!r}")
    print(f"    Shop title: {v['shop_title'][:100]!r}")
    print(f"    Shop desc 1st line: {v['shop_first_desc_line']!r}")
    print(f"    Issues: {v['issues']}")
    print()

# Write a focused MD report for the user
md_lines = [
    "# Title Validation Report",
    "",
    f"- Listings with new eRank-format title: **{len(validations)}**",
    f"- Color mismatches: **{len(color_issues)}**",
    f"- Material mismatches: **{len(mat_issues)}**",
    "",
    "## Color mismatches (title says one color, Shopify product is another)",
    "",
    "| LID | Etsy SKU | Shop SKU | Title color | Shopify colors | New title | Shopify product |",
    "|---|---|---|---|---|---|---|",
]
for v in color_issues:
    md_lines.append(f"| {v['lid']} | {v['etsy_codename']} | {v['shop_first_sku']} | {v['title_color']} | {', '.join(v['shop_colors'][:4])} | {v['new_etsy_title'][:80]} | {v['shop_title'][:60]} |")
md_lines += ["", "## Material mismatches", "",
             "| LID | Etsy SKU | Shop SKU | Title material | Shopify material | New title | Shopify product |",
             "|---|---|---|---|---|---|---|"]
for v in mat_issues:
    md_lines.append(f"| {v['lid']} | {v['etsy_codename']} | {v['shop_first_sku']} | {v['title_material']} | {v['shop_material']} | {v['new_etsy_title'][:80]} | {v['shop_title'][:60]} |")
OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")
print(f"\nWrote: {OUT}")
print(f"Wrote: {OUT_MD}")
