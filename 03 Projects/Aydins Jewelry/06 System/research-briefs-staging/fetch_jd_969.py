"""Fetch Jewelry Depot product page for 969-tr-8mm to extract details for Shopify listing creation."""
import urllib.request, re, json

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
URL = "https://jewelrydepotusa.com/product/969-tr-8mm/"

req = urllib.request.Request(URL, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        html = r.read().decode("utf-8", errors="replace")
except Exception as e:
    print(f"FETCH FAILED: {e}")
    raise

print(f"page size: {len(html):,} bytes")

# Title
m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""
print(f"\n=== TITLE ===\n{title}")

# Try og:title meta
m = re.search(r'<meta\s+property=["\']og:title["\']\s+content=["\']([^"\']+)["\']', html)
print(f"og:title: {m.group(1) if m else 'none'}")

# Description
m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', html)
print(f"\n=== META DESCRIPTION ===\n{m.group(1)[:400] if m else 'none'}")

# Look for product price
m = re.search(r'\$(\d+(?:\.\d+)?)', html)
print(f"\nfirst dollar amount: ${m.group(1) if m else 'none'}")

# Look for images
img_urls = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
product_imgs = [u for u in img_urls if 'wp-content/uploads' in u and u.endswith(('.jpg','.jpeg','.png','.webp'))]
print(f"\n=== PRODUCT IMAGES ({len(product_imgs)}) ===")
for u in product_imgs[:10]: print(f"  {u}")

# Look for sizes / variants
sizes_pattern = re.findall(r'(?:size|Size)[^<]{0,40}["\']?\s*[:>=]\s*["\']?([\d.\s/\-]+(?:through|to)[\d.\s/\-]+)', html)
print(f"\n=== SIZE PATTERNS ===")
for s in sizes_pattern[:5]: print(f"  {s}")

# Look for select options
sel = re.search(r'<select[^>]*name=["\']attribute_pa_size["\'][^>]*>(.*?)</select>', html, re.S)
if sel:
    sizes = re.findall(r'<option[^>]*value=["\']([^"\']*)["\'][^>]*>([^<]+)</option>', sel.group(1))
    print(f"\n=== SIZES (from select) ===")
    for v, t in sizes: print(f"  value={v!r} text={t!r}")
else:
    print("\nNo size select found")

# Look for widths
sel_w = re.search(r'<select[^>]*name=["\']attribute_pa_width["\'][^>]*>(.*?)</select>', html, re.S)
if sel_w:
    widths = re.findall(r'<option[^>]*value=["\']([^"\']*)["\'][^>]*>([^<]+)</option>', sel_w.group(1))
    print(f"\n=== WIDTHS ===")
    for v, t in widths: print(f"  value={v!r} text={t!r}")

# Save HTML for inspection
open("/tmp/jd_969.html","w").write(html)
print(f"\nFull HTML saved to /tmp/jd_969.html")
