"""Parse the saved jd_969.html for product details."""
import re, json

html = open("/tmp/jd_969.html").read()
print(f"page size: {len(html):,} bytes")

# Title
m = re.search(r"<title>([^<]+)</title>", html)
print(f"\nPage title: {m.group(1).strip() if m else 'none'}")

# H1
m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""
print(f"H1: {title}")

# Description (long)
m = re.search(r'<div[^>]*itemprop=["\']description["\'][^>]*>(.*?)</div>', html, re.S)
if m:
    desc = re.sub(r"<[^>]+>", "", m.group(1)).strip()[:500]
    print(f"\nDescription: {desc}")
else:
    # Try woocommerce-product-details__short-description
    m = re.search(r'product-details__short-description[^>]*>(.*?)</div>', html, re.S)
    if m:
        desc = re.sub(r"<[^>]+>", "", m.group(1)).strip()[:500]
        print(f"\nShort desc: {desc}")

# Look for size select
sel = re.search(r'<select[^>]*name=["\']attribute_pa_size["\'][^>]*>(.*?)</select>', html, re.S)
sizes = []
if sel:
    raw = re.findall(r'<option[^>]*value=["\']([^"\']+)["\'][^>]*>([^<]+)</option>', sel.group(1))
    sizes = [(v, t.strip()) for v, t in raw if v]
print(f"\n=== SIZES FOUND ({len(sizes)}) ===")
for v, t in sizes:
    print(f"  value={v!r} display={t!r}")

# Look for variant data JSON (WooCommerce typically embeds this)
vd = re.search(r'data-product_variations=["\']([^"\']+)["\']', html)
if vd:
    raw = vd.group(1).replace("&quot;", '"').replace("&amp;", "&")
    try:
        data = json.loads(raw)
        print(f"\n=== VARIATIONS ({len(data)}) ===")
        for v in data[:5]:
            attrs = v.get("attributes", {})
            print(f"  attrs={attrs} sku={v.get('sku')} price={v.get('display_price')} avail={v.get('is_in_stock')}")
    except Exception as e:
        print(f"failed to parse data-product_variations: {e}")
else:
    print("\nno data-product_variations attribute")

# Look for images
imgs = re.findall(r'<img[^>]+(?:src|data-src)=["\']([^"\']+)["\']', html)
product_imgs = [u for u in imgs if 'jewelrydepotusa.com/wp-content/uploads' in u and re.search(r'\.(jpg|jpeg|png|webp)(\?|$)', u.lower())]
print(f"\n=== PRODUCT IMAGES ({len(product_imgs)}) ===")
for u in list(dict.fromkeys(product_imgs))[:10]:
    print(f"  {u}")

# Look for SKU
m = re.search(r'class=["\']sku["\'][^>]*>([^<]+)</', html)
if m: print(f"\nSKU on page: {m.group(1)}")

# Price
m = re.search(r'<bdi>[^\d]*([\d.,]+)', html)
print(f"\nFirst price: {m.group(1) if m else 'none'}")
