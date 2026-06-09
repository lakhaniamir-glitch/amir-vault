"""Cross-reference v2: codename match + Shopify-title-name fallback match.
Also: index Shopify by product title to allow name-based lookup.
"""
import csv, json, re, sys
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

ETSY = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
OUT  = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref.json")

def codename(vs: str) -> str:
    return vs.strip().split("-")[0].upper() if vs else ""

def normalize_name(s: str) -> str:
    """Extract product name like 'GUARDIAN' or 'HARVEST' from 'GUARDIAN | Gold Ring...'."""
    s = s.strip()
    # Take everything before first | or ,
    m = re.match(r"^([A-Z][A-Z0-9 \-]+?)\s*[|,]", s)
    if m:
        return m.group(1).strip().upper()
    return ""

# Index Shopify: codename + title-name
shop_by_codename = {}
shop_by_name = {}

with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = codename(sku)
        title = (r.get("title") or "").strip()
        # Title-extracted name (e.g., "AZAI | Tungsten Ring..." -> "AZAI", "GUARDIAN | Gold Ring..." -> "GUARDIAN")
        name = normalize_name(title)

        info_keys = ["handle", "title", "description", "tags", "product_type", "option_color"]
        info = {k: (r.get(k) or "").strip() for k in info_keys}
        info["first_sku"] = sku

        # Variant width/size
        vt = (r.get("variant_title") or "").strip()
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        width = m.group(1) if m else ""
        size = m.group(2) if m else ""

        if cn:
            existing = shop_by_codename.setdefault(cn, {**info, "widths": set(), "sizes": set()})
            if width: existing["widths"].add(width)
            if size: existing["sizes"].add(size)
        if name:
            existing = shop_by_name.setdefault(name, {**info, "widths": set(), "sizes": set()})
            if width: existing["widths"].add(width)
            if size: existing["sizes"].add(size)

def finalize(d):
    d["widths"] = sorted(d["widths"], key=lambda x: float(x))
    d["sizes"] = sorted(d["sizes"], key=lambda x: float(x))
    return d

shop_by_codename = {k: finalize(v) for k, v in shop_by_codename.items()}
shop_by_name = {k: finalize(v) for k, v in shop_by_name.items()}

print(f"Shopify by codename: {len(shop_by_codename)}")
print(f"Shopify by title-name: {len(shop_by_name)}")

# Read Etsy export, group into listings
with open(ETSY, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

listings = []
current = None
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None:
            listings.append(current)
        current = {"lid": lid, "rows": [r], "section": (r.get("Section") or "").strip(), "title": (r.get("Title") or "").strip()}
    elif current is not None:
        current["rows"].append(r)
if current is not None:
    listings.append(current)

xref = {}
unmatched = []

for L in listings:
    cn = ""
    for r in L["rows"]:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            cn = codename(vs)
            if cn: break

    # Match strategy 1: codename
    shop = shop_by_codename.get(cn) if cn else None
    match_via = "codename" if shop else None

    # Strategy 2: name extracted from Etsy title prefix (e.g., "GUARDIAN | Gold..." -> "GUARDIAN")
    if not shop:
        etsy_name = normalize_name(L["title"])
        if etsy_name and etsy_name in shop_by_name:
            shop = shop_by_name[etsy_name]
            match_via = f"name:{etsy_name}"
            cn = etsy_name  # use the name as the matched codename

    # Strategy 3: codename appears anywhere in Etsy title (e.g., "...Tungsten Ring Hayden, Personalized" -> HAYDEN)
    if not shop:
        for candidate, info in shop_by_codename.items():
            if len(candidate) >= 4 and not candidate.startswith(("JDTR", "AYTR", "TR")):
                # Look for the codename word in Etsy title (case-insensitive whole word)
                if re.search(rf"\b{re.escape(candidate)}\b", L["title"], re.IGNORECASE):
                    shop = info
                    match_via = f"title-contains:{candidate}"
                    cn = candidate
                    break

    if shop:
        xref[L["lid"]] = {
            "codename": cn,
            "match_via": match_via,
            "etsy_section": L["section"],
            "etsy_title": L["title"],
            "shop_handle": shop["handle"],
            "shop_title": shop["title"],
            "shop_description": shop["description"],
            "shop_tags": shop["tags"],
            "shop_product_type": shop["product_type"],
            "shop_option_color": shop["option_color"],
            "shop_widths": shop["widths"],
            "shop_sizes": shop["sizes"],
            "shop_first_sku": shop["first_sku"],
        }
    else:
        unmatched.append((L["lid"], cn, L["section"], L["title"][:70]))

OUT.write_text(json.dumps(xref, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"\nMatched: {len(xref)}/{len(listings)}")
print(f"Unmatched: {len(unmatched)}")
print()
from collections import Counter
match_strategies = Counter(d["match_via"].split(":")[0] for d in xref.values())
print("Match strategies:")
for s, n in match_strategies.most_common():
    print(f"  {n:3d}  {s}")
print()
print("=== Sample unmatched (first 25) ===")
for lid, cn, section, title in unmatched[:25]:
    print(f"  LID {lid:<12}  cn={cn!r:<14}  section={section!r:<28}  {title!r}")
print(f"\nWrote: {OUT}")
