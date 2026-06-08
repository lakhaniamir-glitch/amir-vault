"""Fetch Shopify product data for the 11 listings Amir wants to keep.
For each handle, get variants (SKU, option1=width, option2=size).
Build override JSON entries for each."""
import json, re
from pathlib import Path
import urllib.request

CONFIG = json.load(open("/home/openclaw/.openclaw/agents/beta/shopify/config.json"))
STORE = "aydinsjewelry.myshopify.com"
TOKEN = CONFIG["stores"][STORE]["accessToken"]

# Handle => label (codename to add to override)
KEEPS = {
    "JDTR061": {
        "handle": "fingerprint-jewelry-his-and-her-fingerprint-couples-ring-promise-ring-plus-engraved-ring-personalized-ring-anniversary-ring-tungsten-3",
        "etsy_listing_id": "817764707",
        "notes": "Fingerprint ring per Amir 2026-06-08"
    },
    "AYTR009": {
        "handle": "fingerprint-ring-actual-fingerprint-double-heart-promise-ring-engraved-ring-anniversary-ring-engagement-ring-tungsten-wedding-band",
        "notes": "Fingerprint heart ring per Amir 2026-06-08 - Shopify may need SKU/size fix"
    },
    "AYSSTAGP": {
        "handle_search_keywords": ["fingerprint-dog-tag"],
        "etsy_listing_id": "509712178",
        "notes": "Fingerprint dog tag per Amir 2026-06-08"
    },
    "HALIFAX": {
        "handle": "tungsten-wood-ring-redwood-inlay-tungsten-wedding-band-polished-finish-4mm-6mm-7mm-8mm-10mm-12mm-tungsten-wedding-ring",
        "etsy_listing_id": "4512054893",
        "notes": "Universal-J Redwood inlay; widths visible in handle: 4,6,7,8,10,12mm",
        "needs_shopify_update": True
    },
    "TR210": {
        "handle": "aydins-gold-brushed-flat-tungsten-ring-wedding-band-with-beveled-edge-8mm-tungsten-carbide-wedding-ring",
        "etsy_listing_id": "4512054099",
        "notes": "Gold brushed flat - match Shopify widths/sizes"
    },
    "JDTR172": {
        "handle": "ranger-domed-couple-matching-tungsten-ring-with-shiny-polished-diamond-shaped-faceted-center-6mm-8mm",
        "etsy_listing_id": "4512043912",
        "notes": "RANGER ring - Shopify has 6mm+8mm; needs 4mm added with sizes 5-12 half-sizes (per Amir)",
        "needs_shopify_update": True,
        "missing_widths": {"4": ["5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12"]}
    },
    "KONA": {
        "handle": "tungsten-wood-ring-koa-wood-tungsten-wedding-band-polished-finish-4mm-6mm-8mm-10mm-12mm-tungsten-wedding-ring",
        "etsy_listing_id": "4512020444",
        "notes": "Koa wood - widths in handle: 4,6,8,10,12mm; needs Universal-J data",
        "needs_shopify_update": True
    },
    "VIPER": {
        "handle": "viper-tungsten-carbide-mens-engagement-ring-with-gold-rope-8mm",
        "etsy_listing_id": "4512018501",
        "notes": "Viper gold rope 8mm only"
    },
    "JDTR969": {
        "handle": None,
        "etsy_listing_id": "4512019324",
        "notes": "NOT on Shopify; data from jewelrydepotusa.com/product/969-tr-8mm/",
        "needs_shopify_add": True,
        "default_width": "8"
    },
    "JDTR809": {
        "handle": "black-high-polished-beveled-edge-with-hawaiian-koa-wood-inlay-8mm-tungsten-carbide-wedding-ring",
        "etsy_listing_id": "4512008688",
        "notes": "Hawaiian Koa - Shopify missing 6mm width (per Amir)",
        "needs_shopify_update": True
    },
    "KODIAK": {
        "handle": "tungsten-wood-ring-rosewood-inlay-tungsten-wedding-band-polished-finish-4mm-6mm-7mm-8mm-10mm-12mm-tungsten-wedding-ring",
        "etsy_listing_id": "4512008686",
        "notes": "Rosewood inlay - widths visible: 4,6,7,8,10,12mm; needs Universal-J data",
        "needs_shopify_update": True
    },
}

def fetch_shopify_by_handle(handle):
    """Fetch Shopify product by handle via Admin API."""
    url = f"https://{STORE}/admin/api/2024-10/products.json?handle={handle}"
    req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": TOKEN})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read())
            products = data.get("products", [])
            return products[0] if products else None
    except Exception as e:
        return {"error": str(e)}

def extract_widths_sizes(product):
    """From a Shopify product, extract {width: [sizes]} from variants."""
    if not product or "error" in product:
        return None, []
    widths = {}
    all_skus = []
    for v in product.get("variants", []):
        sku = v.get("sku", "")
        all_skus.append(sku)
        # Determine which option is width vs size
        o1 = (v.get("option1") or "").strip().lower()
        o2 = (v.get("option2") or "").strip().lower()
        # width pattern
        w = None
        s = None
        for opt in [o1, o2]:
            m = re.match(r"^(\d+(?:\.\d+)?)\s*mm?$", opt)
            if m:
                w = m.group(1).rstrip("0").rstrip(".") if "." in m.group(1) else m.group(1)
                continue
            m = re.match(r"^(\d+)\s+1/2$", opt)
            if m:
                s = f"{int(m.group(1))}.5"
                continue
            m = re.match(r"^(\d+(?:\.\d+)?)$", opt)
            if m:
                s = m.group(1)
        if w is None and s is None:
            continue
        if w is None: w = "8"  # default per Amir rule
        if s is None: continue
        widths.setdefault(w, set()).add(s)
    return {w: sorted(s, key=lambda x: float(x)) for w, s in widths.items()}, all_skus[:5]

results = {}
for codename, info in KEEPS.items():
    handle = info.get("handle")
    if handle is None:
        results[codename] = {"status": "no_handle", "info": info}
        continue
    print(f"\n=== {codename} ===")
    print(f"  handle: {handle}")
    product = fetch_shopify_by_handle(handle)
    if not product or "error" in product:
        results[codename] = {"status": "fetch_failed", "error": (product.get("error") if product else "not found"), "info": info}
        print(f"  FETCH FAILED: {results[codename].get('error')}")
        continue
    title = product.get("title", "")
    widths, sample_skus = extract_widths_sizes(product)
    print(f"  title: {title}")
    print(f"  shopify widths: {sorted(widths.keys()) if widths else 'none'}")
    print(f"  sample SKUs: {sample_skus}")
    results[codename] = {
        "status": "ok",
        "shopify_product_id": product.get("id"),
        "shopify_title": title,
        "shopify_widths": widths,
        "sample_skus": sample_skus,
        "info": info
    }

# Write results
out = Path("/tmp/shopify_keep_fetch_results.json")
out.write_text(json.dumps(results, indent=2))
print(f"\nWrote: {out}")
