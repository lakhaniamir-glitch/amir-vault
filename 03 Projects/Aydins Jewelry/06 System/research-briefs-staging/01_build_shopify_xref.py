"""Step 1: Build Etsy LID -> Shopify product cross-reference.
Match via Var SKU codename (extracted from Etsy Var SKU like 'GALACTIC-8-5' -> 'GALACTIC').

Inputs:
  - C:\\Users\\amirl\\Downloads\\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv (fresh Etsy export)
  - C:\\Users\\amirl\\Downloads\\aydinsjewelry.myshopify.com.csv (Shopify products)

Output:
  - C:\\Users\\amirl\\Downloads\\etsy-to-shopify-xref.json
"""
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path

ETSY = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
OUT  = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref.json")

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

# Helper: extract codename from Var SKU like "GALACTIC-8-5" -> "GALACTIC"
def codename(vs: str) -> str:
    return vs.strip().split("-")[0].upper() if vs else ""

# Step 1: Build Shopify codename -> aggregated product info
# Each Shopify product has multiple variant rows (one per size). We want the FIRST/canonical row's data.
shop_by_codename = {}  # codename -> {sku_pattern, handle, title, description, tags, product_type, option_color, widths:set, sizes:set}

with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = codename(sku)
        if not cn:
            continue
        existing = shop_by_codename.setdefault(cn, {
            "first_sku": sku,
            "handle": (r.get("handle") or "").strip(),
            "title": (r.get("title") or "").strip(),
            "description": (r.get("description") or "").strip(),
            "tags": (r.get("tags") or "").strip(),
            "product_type": (r.get("product_type") or "").strip(),
            "option_color": (r.get("option_color") or "").strip(),
            "widths": set(),
            "sizes": set(),
        })
        # Track all widths/sizes from variant titles
        vt = (r.get("variant_title") or "").strip()
        # "8mm / 5" -> width=8mm, size=5
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m:
            existing["widths"].add(m.group(1))
            existing["sizes"].add(m.group(2))
        # If option_color was empty initially but populated in later row, capture it
        oc = (r.get("option_color") or "").strip()
        if oc and not existing["option_color"]:
            existing["option_color"] = oc

# Normalize sets -> sorted lists
for cn, d in shop_by_codename.items():
    d["widths"] = sorted(d["widths"], key=lambda x: float(x))
    d["sizes"] = sorted(d["sizes"], key=lambda x: float(x))

print(f"Shopify codenames indexed: {len(shop_by_codename)}")

# Step 2: Build Etsy LID -> codename (from Var SKU)
with open(ETSY, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# Group into listings
listings = []
current = None
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None:
            listings.append(current)
        current = {"lid": lid, "rows": [r], "section": (r.get("Section") or "").strip()}
    elif current is not None:
        current["rows"].append(r)
if current is not None:
    listings.append(current)

print(f"Etsy listings: {len(listings)}")

# For each Etsy listing, find first non-blank Var SKU -> codename
matched = []
unmatched = []
for L in listings:
    cn = ""
    for r in L["rows"]:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            cn = codename(vs)
            if cn:
                break
    if cn and cn in shop_by_codename:
        matched.append((L["lid"], cn, L["section"]))
    else:
        unmatched.append((L["lid"], cn, L["section"], (L["rows"][0].get("Title") or "")[:60]))

print(f"\nMatched (Etsy LID -> Shopify codename): {len(matched)}")
print(f"Unmatched: {len(unmatched)}")
print()
print("=== Unmatched sample (first 20) ===")
for lid, cn, section, title in unmatched[:20]:
    print(f"  LID {lid:<12}  codename={cn!r:<15}  section={section!r:<25}  {title!r}")

# Build the xref output
xref = {}
for lid, cn, section in matched:
    s = shop_by_codename[cn]
    xref[lid] = {
        "codename": cn,
        "etsy_section": section,
        "shop_handle": s["handle"],
        "shop_title": s["title"],
        "shop_description": s["description"],
        "shop_tags": s["tags"],
        "shop_product_type": s["product_type"],
        "shop_option_color": s["option_color"],
        "shop_widths": s["widths"],
        "shop_sizes": s["sizes"],
        "shop_first_sku": s["first_sku"],
    }

OUT.write_text(json.dumps(xref, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nWrote: {OUT}")
print(f"  Cross-references: {len(xref)}")

# Spot-check GALACTIC
print("\n=== GALACTIC spot-check ===")
for lid, data in xref.items():
    if data["codename"] == "GALACTIC":
        print(f"  Etsy LID: {lid}")
        print(f"  Etsy section: {data['etsy_section']!r}")
        print(f"  Shop title: {data['shop_title']!r}")
        print(f"  Shop description[:200]: {data['shop_description'][:200]!r}")
        print(f"  Shop tags[:200]: {data['shop_tags'][:200]!r}")
        print(f"  Shop widths: {data['shop_widths']}")
        print(f"  Shop option_color: {data['shop_option_color']!r}")
        break
