"""Pull side-by-side Etsy ↔ Shopify data for named-codename unmatched listings.
Lets Amir manually verify whether the products are physically the same."""
import csv, json, re
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
SRC = ROOT / "listings-corrected.csv.pre-sku-fix-2026-06-08"  # clean original
SHOPIFY_JSONL = Path("/home/openclaw/.openclaw/agents/beta/shopify/products.jsonl")
OUT = Path("/tmp/side-by-side-compare.md")

def extract_codename(sku):
    s = (sku or "").strip().upper()
    while True:
        new = re.sub(r"-\d+(?:\.\d+)?$", "", s)
        if new == s: break
        s = new
    return s

def detect_vendor(sku):
    s = (sku or "").upper().strip()
    if s.startswith("JDTR"): return "Jewelry Depot"
    if s.startswith("AYTR") or s.startswith("AYSS") or s.startswith("AY"): return "Aydins Jewelry"
    if s.startswith("TR"): return "Legacy TR"
    if s and not s[0].isdigit(): return "Universal J (named codename)"
    return "Unknown"

# Load Shopify by indexing handle + title CAPS-word
shopify_products = []
with open(SHOPIFY_JSONL) as f:
    for line in f:
        try: p = json.loads(line)
        except: continue
        skus = [v.get("sku","") for v in p.get("variants", [])]
        shopify_products.append({
            "id": p.get("id"),
            "handle": p.get("handle",""),
            "title": p.get("title",""),
            "skus": skus,
            "vendor_implied": detect_vendor(skus[0] if skus else ""),
            "images": [i.get("src","") for i in p.get("images",[])],
            "variants_sample": [(v.get("option1",""), v.get("option2",""), v.get("sku","")) for v in p.get("variants",[])[:5]],
        })

# Index by title-CAPS-word for fuzzy lookup
title_word_to_products = {}
for p in shopify_products:
    words = re.findall(r"\b[A-Z][A-Z0-9]{2,}\b", p["title"])
    for w in words:
        title_word_to_products.setdefault(w, []).append(p)

# Load Etsy unmatched listings
with open(SRC, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Build index of Shopify codenames for filtering
shopify_sku_codenames = set()
for p in shopify_products:
    for s in p["skus"]:
        cn = extract_codename(s)
        if cn: shopify_sku_codenames.add(cn)

# Find unmatched (no exact SKU codename match)
unmatched_named = []
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if not lid: continue
    sku = (r.get("Var SKU") or r.get("SKU") or "").strip()
    cn = extract_codename(sku)
    if not cn or cn not in shopify_sku_codenames:
        # Check if this is a named codename (potential Universal J)
        is_named = cn and not cn[0].isdigit() and not cn.startswith(("JDTR","AYTR","AYSS","AY","TR"))
        unmatched_named.append({
            "lid": lid, "cn": cn, "raw_sku": sku, "is_named": is_named,
            "etsy_title": r.get("Title",""), "etsy_section": r.get("Section",""),
            "etsy_materials": r.get("Materials",""), "etsy_v1": r.get("Variation 1",""),
            "etsy_v1_opt": r.get("V1 Option",""), "etsy_v2": r.get("Variation 2",""),
            "etsy_v2_opt": r.get("V2 Option",""), "etsy_photo1": r.get("Photo 1",""),
        })

# Output markdown
lines = []
lines.append("# Side-by-side: Etsy unmatched listings vs Shopify candidates")
lines.append(f"\nTotal unmatched: {len(unmatched_named)}")
lines.append(f"Named codenames (potential Universal J): {sum(1 for u in unmatched_named if u['is_named'])}")
lines.append(f"\nLegend: each section shows the Etsy listing and any Shopify candidates that share its CAPS title word or codename in handle.\n")
lines.append("---\n")

# Process named first
for u in [x for x in unmatched_named if x["is_named"]][:25]:
    cn = u["cn"]
    lines.append(f"## ETSY listing {u['lid']} — codename: `{cn}`\n")
    lines.append(f"- **Etsy Title:** {u['etsy_title']}")
    lines.append(f"- **Section:** {u['etsy_section']}")
    lines.append(f"- **Materials:** {u['etsy_materials']}")
    lines.append(f"- **Variation 1 / V1 Option:** `{u['etsy_v1']}` / `{u['etsy_v1_opt']}`")
    lines.append(f"- **Variation 2 / V2 Option:** `{u['etsy_v2']}` / `{u['etsy_v2_opt']}`")
    if u['etsy_photo1']:
        lines.append(f"- **Etsy Photo 1:** {u['etsy_photo1']}")

    # Find Shopify candidates by codename in title or handle
    candidates = []
    for w in re.findall(r"\b[A-Z][A-Z0-9]{2,}\b", u['etsy_title']):
        candidates.extend(title_word_to_products.get(w, []))
    candidates.extend([p for p in shopify_products if cn.lower() in p["handle"].lower()])

    seen_ids = set()
    candidates = [c for c in candidates if not (c["id"] in seen_ids or seen_ids.add(c["id"]))]

    if candidates:
        lines.append(f"\n### Shopify candidates ({len(candidates)}):\n")
        for c in candidates[:3]:
            lines.append(f"- **{c['title']}**")
            lines.append(f"  - Handle: `{c['handle']}`")
            lines.append(f"  - SKU prefix: `{extract_codename(c['skus'][0]) if c['skus'] else 'none'}` → vendor: **{c['vendor_implied']}**")
            lines.append(f"  - Sample variants (width,size,sku): {c['variants_sample'][:3]}")
            if c['images']:
                lines.append(f"  - Shopify Image 1: {c['images'][0]}")
            lines.append("")
    else:
        lines.append(f"\n### No Shopify match found by title or handle search\n")
    lines.append("---\n")

OUT.write_text("\n".join(lines))
print(f"Wrote: {OUT}")
print(f"Total named-codename unmatched: {sum(1 for u in unmatched_named if u['is_named'])}")
