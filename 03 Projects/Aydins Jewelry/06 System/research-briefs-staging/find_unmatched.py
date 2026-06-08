"""Identify Etsy listings without a Shopify codename match + attempt to find them by alt strategies."""
import csv, json, re
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
SRC = ROOT / "listings-corrected.csv.pre-sku-fix-2026-06-08"  # clean source
INDEX = Path("/tmp/shopify_codename_width_size_index.json")
SHOPIFY_JSONL = Path("/home/openclaw/.openclaw/agents/beta/shopify/products.jsonl")

idx = json.loads(INDEX.read_text())

def extract_codename(sku):
    s = (sku or "").strip().upper()
    while True:
        new = re.sub(r"-\d+(?:\.\d+)?$", "", s)
        if new == s: break
        s = new
    return s

with open(SRC, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

unmatched = []
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if not lid: continue
    sku = (r.get("Var SKU") or r.get("SKU") or "").strip()
    cn = extract_codename(sku)
    title = (r.get("Title") or "")[:90]
    section = (r.get("Section") or "")[:30]
    if not cn or cn not in idx:
        unmatched.append({"lid": lid, "cn": cn, "raw_sku": sku, "title": title, "section": section})

print(f"unmatched listings: {len(unmatched)}\n")
print("=== Full list ===")
for u in unmatched:
    line = f'L:{u["lid"]} cn={u["cn"]!r:14} sku={u["raw_sku"]!r:18} section={u["section"]:30} title={u["title"]}'
    print(line)

# Try alt-lookup: extract first word from title and search Shopify products by handle/title
print("\n\n=== Attempting fuzzy match for each unmatched ===")
# Load Shopify products fully (handle, title, variant SKUs)
shopify_products = []
with open(SHOPIFY_JSONL) as f:
    for line in f:
        try:
            p = json.loads(line)
        except: continue
        skus = [extract_codename(v.get("sku","")) for v in p.get("variants",[])]
        shopify_products.append({
            "id": p.get("id"),
            "handle": p.get("handle",""),
            "title": p.get("title",""),
            "skus": [s for s in skus if s],
        })

# Build handle index
handle_to_product = {p["handle"]: p for p in shopify_products}
title_words_to_product = {}
for p in shopify_products:
    words = re.findall(r"[A-Z][A-Z0-9]+", p["title"])  # find CAPS words
    for w in words:
        if len(w) >= 3:
            title_words_to_product.setdefault(w, []).append(p)

fuzzy_matches = []
no_match = []
for u in unmatched:
    title = u["title"]
    cn = u["cn"]
    sku = u["raw_sku"]
    # Try: codename as handle prefix
    matches = []
    # 1) Look at title for ALL-CAPS brand word
    caps_words = re.findall(r"\b[A-Z][A-Z0-9]{2,}\b", title)
    for w in caps_words:
        if w in title_words_to_product:
            matches.extend(title_words_to_product[w])
    # 2) Look at codename in handles
    if cn:
        for h, p in handle_to_product.items():
            if cn.lower() in h:
                matches.append(p)
    # 3) Look at exact codename in any SKU
    for p in shopify_products:
        if cn and any(cn == s for s in p["skus"]):
            matches.append(p)
    # Dedupe
    seen_ids = set()
    matches = [m for m in matches if not (m["id"] in seen_ids or seen_ids.add(m["id"]))]
    if matches:
        fuzzy_matches.append((u, matches[:2]))
    else:
        no_match.append(u)

print(f"\nfuzzy-matched: {len(fuzzy_matches)} / {len(unmatched)}")
print(f"still no match: {len(no_match)}")
print("\n=== Fuzzy match samples (first 12) ===")
for u, matches in fuzzy_matches[:12]:
    print(f'\nETSY: L:{u["lid"]} cn={u["cn"]!r:14} title="{u["title"]}"')
    for m in matches[:2]:
        skus_short = m["skus"][:3]
        print(f'  -> SHOPIFY: handle={m["handle"]!r}  title="{m["title"][:60]}"  skus={skus_short}')

print("\n=== Still no match (first 10) ===")
for u in no_match[:10]:
    print(f'  L:{u["lid"]} cn={u["cn"]!r:14} title="{u["title"]}"')
