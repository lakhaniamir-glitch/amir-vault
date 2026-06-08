"""Create JDTR969 product on Shopify with full variants + image upload.
Source: jewelrydepotusa.com/product/969-tr-8mm/
Visual analysis: Black tungsten ring with blue meteorite/textured inlay + silver arrow design, 8mm domed."""
import json, base64, time
import urllib.request

CONFIG = json.load(open("/home/openclaw/.openclaw/agents/beta/shopify/config.json"))
STORE = "aydinsjewelry.myshopify.com"
TOKEN = CONFIG["stores"][STORE]["accessToken"]

# === Product details ===
SKU_PREFIX = "JDTR969"
TITLE = "JDTR969 | Black Tungsten Ring, Blue Meteorite Arrow Inlay, 8mm"
HANDLE_SLUG = "jdtr969-black-tungsten-ring-blue-meteorite-arrow-inlay-8mm"
PRICE = "169.00"
INVENTORY_PER_SIZE = 10
WIDTH = "8mm"
COLOR = "Black"
SIZES_8MM = ["7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","14","15"]

BODY_HTML = """<p>Black tungsten ring with a striking blue meteorite-textured inlay running the length of the band, accented by an inlaid silver arrow that gives this piece its signature look. Domed profile with brushed beveled edges for a polished modern feel.</p>

<h3>Key Features</h3>
<ul>
<li>Black tungsten carbide base</li>
<li>Blue meteorite-style textured inlay</li>
<li>Silver arrow inlay design</li>
<li>Domed profile, brushed beveled edges</li>
<li>8mm width</li>
<li>Comfort fit</li>
<li>Scratch resistant</li>
</ul>

<p>Engrave the inside, make it his.</p>"""

# Build product payload (REST Admin API format)
product_payload = {
    "product": {
        "title": TITLE,
        "body_html": BODY_HTML,
        "vendor": "",
        "product_type": "Rings",
        "tags": "8mm, Tungsten, Black, Tungsten Carbide, Mens Wedding Band, Comfort Fit, Meteorite, Unique Inlays, Wedding Band",
        "status": "active",
        "handle": HANDLE_SLUG,
        "options": [
            {"name": "Width", "values": [WIDTH]},
            {"name": "Size", "values": SIZES_8MM},
            {"name": "Color", "values": [COLOR]},
        ],
        "variants": [
            {
                "option1": WIDTH,
                "option2": size,
                "option3": COLOR,
                "price": PRICE,
                "sku": f"{SKU_PREFIX}-8-{size}",
                "inventory_management": "shopify",
                "inventory_quantity": INVENTORY_PER_SIZE,
            }
            for size in SIZES_8MM
        ],
    }
}

# Create product via REST
url = f"https://{STORE}/admin/api/2024-10/products.json"
req = urllib.request.Request(
    url,
    data=json.dumps(product_payload).encode(),
    method="POST",
    headers={"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN},
)
print("Creating Shopify product...")
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        resp = json.loads(r.read())
        product = resp["product"]
        print(f"  PRODUCT CREATED: id={product['id']} handle={product['handle']}")
        print(f"  variants created: {len(product.get('variants', []))}")
        for v in product.get("variants", [])[:3]:
            print(f"    sample: SKU={v.get('sku')} price=${v.get('price')} qty={v.get('inventory_quantity')}")
except urllib.error.HTTPError as e:
    err = e.read().decode()[:500]
    print(f"  CREATE FAILED: {err}")
    raise

# Upload image
print("\nUploading image...")
img_bytes = open("/tmp/jd_0969.jpg", "rb").read()
img_b64 = base64.b64encode(img_bytes).decode()
image_payload = {
    "image": {
        "attachment": img_b64,
        "filename": "jdtr969-black-tungsten-blue-meteorite-arrow.jpg",
        "alt": "JDTR969 Black tungsten ring with blue meteorite inlay and silver arrow design 8mm",
    }
}
img_url = f"https://{STORE}/admin/api/2024-10/products/{product['id']}/images.json"
req = urllib.request.Request(
    img_url,
    data=json.dumps(image_payload).encode(),
    method="POST",
    headers={"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN},
)
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        resp = json.loads(r.read())
        img = resp["image"]
        print(f"  IMAGE UPLOADED: id={img['id']} src={img['src']}")
except urllib.error.HTTPError as e:
    err = e.read().decode()[:500]
    print(f"  IMAGE UPLOAD FAILED: {err}")

print(f"\nProduct admin URL: https://admin.shopify.com/store/aydinsjewelry/products/{product['id']}")
print(f"Public URL: https://shopaydins.com/products/{product['handle']}")
