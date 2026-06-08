import json
d = json.load(open("/tmp/shopify_keep_fetch_results.json"))
for cn, r in d.items():
    if r.get("status") != "ok": continue
    widths = r.get("shopify_widths", {})
    if not widths: continue
    print(f"\n{cn}: {r['shopify_title']}")
    for w, sizes in sorted(widths.items(), key=lambda x: float(x[0])):
        print(f"  {w}mm: {len(sizes)} sizes -> {sizes}")
