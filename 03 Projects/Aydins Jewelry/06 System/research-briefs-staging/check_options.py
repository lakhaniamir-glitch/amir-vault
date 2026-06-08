import json, urllib.request
cfg = json.load(open("/home/openclaw/.openclaw/agents/beta/shopify/config.json"))
token = cfg["stores"]["aydinsjewelry.myshopify.com"]["accessToken"]
for handle in [
    "black-high-polished-beveled-edge-with-hawaiian-koa-wood-inlay-8mm-tungsten-carbide-wedding-ring",
    "ranger-domed-couple-matching-tungsten-ring-with-shiny-polished-diamond-shaped-faceted-center-6mm-8mm",
]:
    url = f"https://aydinsjewelry.myshopify.com/admin/api/2024-10/products.json?handle={handle}"
    req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": token})
    p = json.loads(urllib.request.urlopen(req).read())["products"][0]
    print(f"\n=== {p['title']} ===")
    for o in p.get("options",[]):
        print(f"  option {o.get('position')} ({o.get('name')}): {o.get('values')}")
    v = p["variants"][0]
    print(f"  first variant: option1={v.get('option1')} option2={v.get('option2')} option3={v.get('option3')}")
