import csv
from collections import defaultdict
with open("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-corrected.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Check JDTR124, fingerprint codenames
checks = ["JDTR124", "JDTR061", "JDTR100", "JDTR332", "JDTR791", "JDTR792", "AYTR005", "AYTR006"]
by_cn = defaultdict(lambda: {"widths": set(), "sizes": set(), "title": "", "lid": "", "count": 0})
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    sku = (r.get("Var SKU") or "").strip()
    cn = sku.split("-")[0] if sku else ""
    if not cn: continue
    if lid:
        by_cn[cn]["lid"] = lid
        by_cn[cn]["title"] = r.get("Title","")[:80]
    w = r.get("V2 Option","")
    s = r.get("V1 Option","")
    if w: by_cn[cn]["widths"].add(w)
    if s: by_cn[cn]["sizes"].add(s)
    by_cn[cn]["count"] += 1

for cn in checks:
    d = by_cn.get(cn)
    if d and d["count"]:
        widths = sorted(d["widths"])
        sizes = len(d["sizes"])
        count = d["count"]
        lid = d["lid"]
        title = d["title"]
        print(f"{cn} (L:{lid}): widths={widths} sizes={sizes} variants={count}")
        print(f"  title: {title}")
    else:
        print(f"{cn}: NOT IN CSV (still dropped)")
