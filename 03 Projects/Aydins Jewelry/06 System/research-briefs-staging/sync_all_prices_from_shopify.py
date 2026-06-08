"""Match ALL listings to Shopify and sync prices accordingly.
For each listing block:
  - Look up Shopify variant prices for codename (with alias support + width match)
  - Set master Price = MIN price across that codename's variants on Shopify
  - For each variant row: if Shopify variant price != master, set Var Price; else blank"""
import csv, json, re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
SHOPIFY = Path("/home/openclaw/.openclaw/agents/beta/shopify/products.jsonl")
OVERRIDES = Path("/tmp/manual_codename_overrides.json")

def extract_codename(sku):
    if not sku: return ""
    s = sku.strip().upper()
    color_finish = r"-(BLACK|SILVER|GOLD|WHITE|ROSE|POLISHED|BRUSHED|MATTE|SATIN|YELLOW)$"
    while True:
        prev = s
        s = re.sub(r"-CFP\d+$", "", s)
        s = re.sub(r"-VARIATION$", "", s)
        s = re.sub(color_finish, "", s)
        s = re.sub(r"-\d+(?:\.\d+)?$", "", s)
        if s == prev: break
    return s

def norm_width(s):
    m = re.match(r"^(\d+(?:\.\d+)?)\s*mm?$", s.lower().strip()) or re.match(r"^(\d+(?:\.\d+)?)$", s.strip())
    if not m: return None
    v = m.group(1)
    return v.rstrip("0").rstrip(".") if "." in v else v

def norm_size(s):
    s = s.strip()
    m = re.match(r"^(\d+)\s+1/2$", s)
    if m: return f"{int(m.group(1))}.5"
    m = re.match(r"^(\d+)\s+1/4$", s)
    if m: return f"{int(m.group(1))}.25"
    m = re.match(r"^(\d+)\s+3/4$", s)
    if m: return f"{int(m.group(1))}.75"
    m = re.match(r"^(\d+(?:\.\d+)?)$", s)
    return m.group(1) if m else None

# Build Shopify codename -> {(width, size): price}
print("Building Shopify price index (with width+size granularity)...")
shopify_prices = defaultdict(dict)  # {codename: {(width, size): price}}
shopify_min_price = {}              # {codename: min_price_float}

with open(SHOPIFY) as f:
    for line in f:
        try: p = json.loads(line)
        except: continue
        for v in p.get("variants", []):
            sku = v.get("sku", "")
            cn = extract_codename(sku)
            if not cn: continue
            o1 = (v.get("option1") or "").strip()
            o2 = (v.get("option2") or "").strip()
            w = norm_width(o1)
            s = norm_size(o2)
            if w is None:
                w = norm_width(o2)
                s = norm_size(o1)
            if w is None: w = "8"
            price = v.get("price")
            try: pf = float(price) if price else 0
            except: pf = 0
            if pf <= 0: continue
            shopify_prices[cn][(w, s)] = pf
            cur = shopify_min_price.get(cn)
            if cur is None or pf < cur:
                shopify_min_price[cn] = pf

print(f"  indexed {len(shopify_prices)} codenames")

# Load overrides
overrides = json.loads(OVERRIDES.read_text())
codename_aliases = {}
for cn, data in overrides.items():
    if cn.startswith("_"): continue
    if isinstance(data, dict) and "shopify_alias" in data:
        codename_aliases[cn.upper()] = [a.upper() for a in data["shopify_alias"]]

def lookup_price(codename, width=None, size=None):
    """Find price. Try exact (width, size) match. Then any matching width. Then min."""
    candidates = [codename.upper()] + codename_aliases.get(codename.upper(), [])
    for c in candidates:
        if c not in shopify_prices: continue
        prices = shopify_prices[c]
        if width and size:
            if (width, size) in prices: return prices[(width, size)]
        if width:
            width_matches = [p for (w, s), p in prices.items() if w == width]
            if width_matches: return min(width_matches)
        return shopify_min_price[c]
    return None

def lookup_min(codename):
    candidates = [codename.upper()] + codename_aliases.get(codename.upper(), [])
    for c in candidates:
        if c in shopify_min_price: return shopify_min_price[c]
    return None

# Process both CSVs
for fname in ["listings-corrected.csv", "new-shopify-listings.csv"]:
    path = ROOT / fname
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)
    has_lid = any((r.get("Listing ID") or "").strip() for r in rows[:200])

    # Pass 1: group by listing block
    listing_blocks = []
    current = None
    for i, r in enumerate(rows):
        is_first = bool((r.get("Listing ID") or "").strip()) if has_lid else bool((r.get("Title") or "").strip())
        if is_first:
            if current is not None: listing_blocks.append(current)
            current = [i]
        elif current is not None:
            current.append(i)
    if current is not None: listing_blocks.append(current)

    master_price_updates = 0
    var_price_updates = 0
    not_found = []
    not_found_count = 0

    for block in listing_blocks:
        first_idx = block[0]
        first_row = rows[first_idx]
        sku = (first_row.get("Var SKU") or first_row.get("SKU") or "").strip()
        codename = extract_codename(sku)
        if not codename: continue
        min_price = lookup_min(codename)
        if min_price is None:
            not_found_count += 1
            if len(not_found) < 8:
                lid = (first_row.get("Listing ID") or "").strip()
                not_found.append((lid, codename, sku))
            continue

        # Update master Price to min Shopify price
        new_master = f"{min_price:.2f}"
        old_master = (first_row.get("Price") or "").strip()
        if old_master != new_master:
            first_row["Price"] = new_master
            master_price_updates += 1

        # Per-variant pricing: set Var Price if differs from master
        for ridx in block:
            r = rows[ridx]
            v1 = (r.get("V1 Option") or "").strip()
            v2 = (r.get("V2 Option") or "").strip()
            # Determine which is width vs size
            v1_label = (r.get("Variation 1") or "").strip().lower()
            v2_label = (r.get("Variation 2") or "").strip().lower()
            width = None; size = None
            if v1_label == "width": width = norm_width(v1)
            elif v1_label in ("ring size", "size"): size = norm_size(v1)
            if v2_label == "width": width = norm_width(v2) or width
            elif v2_label in ("ring size", "size"): size = norm_size(v2) or size

            variant_price = lookup_price(codename, width, size)
            if variant_price is None: variant_price = min_price
            if abs(variant_price - min_price) < 0.005:
                # same as master, blank Var Price
                if (r.get("Var Price") or "").strip():
                    r["Var Price"] = ""
                    var_price_updates += 1
            else:
                new_var = f"{variant_price:.2f}"
                if (r.get("Var Price") or "").strip() != new_var:
                    r["Var Price"] = new_var
                    var_price_updates += 1

    # Atomic write
    tmp = path.with_suffix(".csv.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)

    print(f"\n=== {fname} ===")
    print(f"  listings: {len(listing_blocks)}")
    print(f"  master price updates: {master_price_updates}")
    print(f"  variant price updates: {var_price_updates}")
    print(f"  codenames not found in Shopify: {not_found_count}")
    for lid, cn, sku in not_found:
        print(f"    L:{lid:12} cn={cn:20} sku={sku!r}")
