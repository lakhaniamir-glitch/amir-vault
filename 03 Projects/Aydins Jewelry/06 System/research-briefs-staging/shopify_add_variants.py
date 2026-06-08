"""Add missing variants to Shopify products via Admin API GraphQL.
- JDTR698 (RHYTHM): add 6mm width with sizes 5-13 (incl half) = 17 variants
- JDTR079 (RANGER): add 4mm width with sizes 5-12 (incl half) = 15 variants
"""
import json, time
import urllib.request
import urllib.parse
from pathlib import Path

CONFIG = json.load(open("/home/openclaw/.openclaw/agents/beta/shopify/config.json"))
STORE = "aydinsjewelry.myshopify.com"
TOKEN = CONFIG["stores"][STORE]["accessToken"]
ENDPOINT = f"https://{STORE}/admin/api/2024-10/graphql.json"

def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def get_product_by_handle(handle):
    """Fetch product GID + existing variant template via REST (simpler)."""
    url = f"https://{STORE}/admin/api/2024-10/products.json?handle={handle}"
    req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": TOKEN})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())
    products = data.get("products", [])
    return products[0] if products else None

def add_variants_rest(product_id, new_variants_data):
    """Use REST API to add variants (simpler than GraphQL bulk)."""
    results = []
    for v in new_variants_data:
        url = f"https://{STORE}/admin/api/2024-10/products/{product_id}/variants.json"
        body = json.dumps({"variant": v}).encode()
        req = urllib.request.Request(
            url, data=body, method="POST",
            headers={"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN}
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                resp = json.loads(r.read())
                results.append({"status": "ok", "sku": v.get("sku"), "variant_id": resp.get("variant", {}).get("id")})
                print(f"  CREATED variant SKU={v.get('sku'):20s} -> {resp.get('variant', {}).get('id')}")
        except urllib.error.HTTPError as e:
            err = e.read().decode()[:300]
            results.append({"status": "fail", "sku": v.get("sku"), "error": err})
            print(f"  FAIL variant SKU={v.get('sku'):20s}: {err}")
        time.sleep(0.5)  # be kind to API
    return results

def build_variants(codename_prefix, width_mm, sizes, base_price, color, inventory_qty=10):
    """Build list of variant payloads for REST API."""
    variants = []
    for size in sizes:
        variants.append({
            "option1": f"{width_mm}mm",  # lowercase to match existing
            "option2": size,
            "option3": color,
            "price": str(base_price),
            "sku": f"{codename_prefix}-{width_mm}-{size}",
            "inventory_management": "shopify",
            "inventory_quantity": inventory_qty,
        })
    return variants

# === Job 1: JDTR698 (RHYTHM) — add 6mm width ===
print("=" * 60)
print("JOB 1: Add 6mm variants to RHYTHM (JDTR698)")
print("=" * 60)
rhythm = get_product_by_handle("black-high-polished-beveled-edge-with-hawaiian-koa-wood-inlay-8mm-tungsten-carbide-wedding-ring")
if not rhythm:
    print("  RHYTHM product not found")
else:
    print(f"  Product ID: {rhythm['id']}")
    print(f"  Title: {rhythm.get('title')}")
    # Determine price from existing 8mm variants
    existing_prices = [v["price"] for v in rhythm.get("variants", []) if v.get("price")]
    base_price = min(existing_prices) if existing_prices else "169.00"
    print(f"  Base price: ${base_price}")
    sizes_6mm = ["5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13"]
    new_vars = build_variants("JDTR698", "6", sizes_6mm, base_price, "Black")
    print(f"  Adding {len(new_vars)} new 6mm variants...")
    results = add_variants_rest(rhythm["id"], new_vars)
    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"  Done: {ok}/{len(new_vars)} created")

# === Job 2: JDTR079 (RANGER) — add 4mm width ===
print()
print("=" * 60)
print("JOB 2: Add 4mm variants to RANGER (JDTR079)")
print("=" * 60)
ranger = get_product_by_handle("ranger-domed-couple-matching-tungsten-ring-with-shiny-polished-diamond-shaped-faceted-center-6mm-8mm")
if not ranger:
    print("  RANGER product not found")
else:
    print(f"  Product ID: {ranger['id']}")
    print(f"  Title: {ranger.get('title')}")
    existing_prices = [v["price"] for v in ranger.get("variants", []) if v.get("price")]
    base_price = min(existing_prices) if existing_prices else "169.00"
    print(f"  Base price: ${base_price}")
    sizes_4mm = ["5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12"]
    new_vars = build_variants("JDTR079", "4", sizes_4mm, base_price, "Silver")
    print(f"  Adding {len(new_vars)} new 4mm variants...")
    results = add_variants_rest(ranger["id"], new_vars)
    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"  Done: {ok}/{len(new_vars)} created")
