"""Two operations:
1. Wire the 4 AI image URLs into JDTR969 row of listings-corrected.csv (Photo 1-4)
2. Upload the 4 AI images to the Shopify JDTR969 product page"""
import csv, json, base64, time
from pathlib import Path
import urllib.request

ROOT = Path("/home/openclaw/.openclaw")
SHOPIFY_CFG = ROOT / "agents/beta/shopify/config.json"
URL_MAP = ROOT / "vault/brands/aydins/etsy-exports/jdtr969-image-cdn-urls.json"
CSV_PATH = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv")
IMG_DIR = Path("/home/openclaw/.openclaw/vault/brands/aydins/etsy-exports/2026-06-04/images/jdtr969")

cfg = json.load(open(SHOPIFY_CFG))
STORE = "aydinsjewelry.myshopify.com"
TOKEN = cfg["stores"][STORE]["accessToken"]
SHOPIFY_PRODUCT_ID = 9394649694445  # JDTR969 product id from create script

urls = json.loads(URL_MAP.read_text())
print(f"loaded URL map: {urls}")

# === Step 1: Update CSV ===
with open(CSV_PATH, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

updated = False
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid == "4512019324":  # JDTR969 listing
        # Replace Photo 1-4 with AI URLs, push existing Photo 1 to Photo 5
        old_photos = [r.get(f"Photo {i+1}", "") for i in range(10)]
        # Keep the SHOPIFY JD product photo (already in Photo 1 of original or get it from Shopify CDN)
        jd_shopify_url = "https://cdn.shopify.com/s/files/1/1857/8135/files/jdtr969-black-tungsten-blue-meteorite-arrow.jpg?v=1780957443"
        new_photos = [
            urls.get("hero.jpg", ""),
            urls.get("image-2.jpg", ""),
            urls.get("image-3.jpg", ""),
            urls.get("image-4.jpg", ""),
            jd_shopify_url,  # JD product photo as Photo 5
        ]
        # Pad to 10 with original existing photos (in case they had more)
        for i in range(10):
            r[f"Photo {i+1}"] = new_photos[i] if i < len(new_photos) else (old_photos[i] if i < len(old_photos) else "")
        updated = True
        print(f"Updated row Listing ID {lid}")
        for i in range(10):
            v = r.get(f"Photo {i+1}", "")
            if v: print(f"  Photo {i+1}: {v[:80]}")
        break

if not updated:
    print("ERROR: JDTR969 listing not found in CSV")
else:
    tmp = Path("/tmp/listings-corrected.csv.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(CSV_PATH)
    print(f"CSV updated atomic at {CSV_PATH}")

# === Step 2: Upload 4 images to the Shopify JDTR969 product ===
print("\n=== Step 2: Add 4 images to Shopify product ===")

def upload_image_to_product(product_id, file_path, alt):
    """Upload an image to a Shopify product via REST."""
    img_bytes = file_path.read_bytes()
    img_b64 = base64.b64encode(img_bytes).decode()
    payload = {
        "image": {
            "attachment": img_b64,
            "filename": file_path.name,
            "alt": alt,
        }
    }
    url = f"https://{STORE}/admin/api/2024-10/products/{product_id}/images.json"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 method="POST",
                                 headers={"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            resp = json.loads(r.read())
            return resp["image"]
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:300]
        raise RuntimeError(f"upload failed: {err}")

alt_texts = {
    "hero.jpg": "JDTR969 Black Tungsten Ring Blue Meteorite Arrow Inlay - Cinematic Hero Shot",
    "image-2.jpg": "JDTR969 on Man's Ring Finger - Yacht Deck Lifestyle",
    "image-3.jpg": "JDTR969 Macro Detail of Blue Meteorite Inlay and Silver Arrow",
    "image-4.jpg": "JDTR969 on Ring Finger - Archery Quiver Outdoor Lifestyle",
}

# Upload in display order
order = ["hero.jpg", "image-2.jpg", "image-3.jpg", "image-4.jpg"]
for fname in order:
    fp = IMG_DIR / fname
    if not fp.exists():
        print(f"  SKIP {fname} - not found")
        continue
    try:
        img = upload_image_to_product(SHOPIFY_PRODUCT_ID, fp, alt_texts.get(fname, ""))
        print(f"  UPLOADED {fname} -> id={img['id']} position={img.get('position')}")
    except Exception as e:
        print(f"  FAILED {fname}: {e}")
    time.sleep(1)

print("\nDONE. Shopify product now has lifestyle images.")
print(f"View at: https://admin.shopify.com/store/aydinsjewelry/products/{SHOPIFY_PRODUCT_ID}")
