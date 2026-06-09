"""Kitchen-sink matcher: every strategy I can think of, ranked by confidence.

Strategies in order:
  1. Codename exact          (already in v1)
  2. Title-extracted name    (re-added: "GUARDIAN | ..." -> GUARDIAN)
  3. Title-contains codename (already in v1, e.g. "...Ring Hayden..." -> HAYDEN)
  4. JDTR digit-drop          (JDTR1144 -> JDTR144 if exists)
  5. Distinctive-word overlap (3+ shared distinctive words, clear winner)
  6. Shopify HANDLE word match (handle = "guardian-gold-ring" includes "GUARDIAN")
  7. Shopify TITLE proper-noun search (Shop title contains the named product name found in Etsy title)
"""
import csv, json, re, sys
from collections import defaultdict, Counter
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

ETSY = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
OUT  = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v3.json")
DIAG = Path(r"C:\Users\amirl\Downloads\matcher-v3-diagnostic.json")

DISTINCTIVE = {
    "materials":   ["tungsten", "ceramic", "damascus", "titanium", "cobalt", "wood"],
    "colors":      ["black", "silver", "rose gold", "yellow gold", "gold", "blue", "green",
                    "red", "purple", "orange", "white", "gunmetal", "pink", "camo"],
    "inlays":      ["opal", "abalone", "meteorite", "diamond", "antler", "fingerprint",
                    "carbon fiber", "lava rock", "dinosaur bone", "mother of pearl",
                    "mop", "rosewood", "olive wood", "koa", "box elder", "burl wood",
                    "burl", "zebra wood", "ironwood", "iron wood", "ebony", "bocote",
                    "goldstone", "malachite", "turquoise", "shell"],
    "finishes":   ["polished", "brushed", "beveled", "domed", "hammered", "pipe cut",
                   "grooved", "groove", "faceted", "matte", "stepped edge", "knurled",
                   "satin", "flat"],
}
ALL_DISTINCTIVE = {w for vs in DISTINCTIVE.values() for w in vs}

def codename(vs: str) -> str:
    return vs.strip().split("-")[0].upper() if vs else ""

def normalize(s: str) -> str:
    return re.sub(r"[^\w\s]", " ", (s or "").lower())

def extract_distinctive_words(text: str) -> set[str]:
    blob = " " + normalize(text) + " "
    return {w.lower() for w in ALL_DISTINCTIVE if " " + w.lower() + " " in blob}

def extract_name(title: str) -> str:
    """Pull product name from title prefix like 'GUARDIAN | Gold Ring...' -> 'GUARDIAN'."""
    t = title.strip()
    m = re.match(r"^([A-Z][A-Z0-9 \-]{2,})\s*[|,]", t)
    return m.group(1).strip().upper() if m else ""

# Load Shopify
print("Loading Shopify...")
shop = defaultdict(lambda: {"title": "", "description": "", "tags": "",
                             "handle": "", "first_sku": "", "widths": set(), "sizes": set(),
                             "option_color": ""})
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = codename(sku)
        if not cn: continue
        d = shop[cn]
        if not d["title"]:
            d["title"] = (r.get("title") or "").strip()
            d["description"] = (r.get("description") or "").strip()
            d["tags"] = (r.get("tags") or "").strip()
            d["handle"] = (r.get("handle") or "").strip()
            d["first_sku"] = sku
            d["option_color"] = (r.get("option_color") or "").strip()
        vt = (r.get("variant_title") or "").strip()
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m:
            d["widths"].add(m.group(1))
            d["sizes"].add(m.group(2))
print(f"Shopify codenames: {len(shop)}")

# Build indices
shop_by_name = {}  # NAME (from shop title prefix) -> codename
shop_by_handle_tokens = defaultdict(set)  # handle word -> codenames
shop_distinctive = {}
word_to_codenames = defaultdict(set)
all_handles = {}  # handle -> codename
for cn, d in shop.items():
    # Name from shop title (e.g., "GUARDIAN | Gold Ring..." -> "GUARDIAN")
    name = extract_name(d["title"])
    if name and name not in shop_by_name:
        shop_by_name[name] = cn

    # Handle tokens (e.g., "guardian-gold-ring-white-brushed" -> ["guardian", "gold", "ring", "white", "brushed"])
    for tok in re.split(r"[-_]", d["handle"].lower()):
        if len(tok) >= 4:
            shop_by_handle_tokens[tok].add(cn)
    all_handles[d["handle"].lower()] = cn

    # Distinctive words
    text = f"{d['title']} {d['tags']} {d['description']}"
    shop_distinctive[cn] = extract_distinctive_words(text)
    for w in shop_distinctive[cn]:
        word_to_codenames[w].add(cn)

print(f"Indexed: by name={len(shop_by_name)}, by handle tokens={len(shop_by_handle_tokens)}")

# Load Etsy
with open(ETSY, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
listings = []
current = None
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None: listings.append(current)
        current = {"lid": lid, "rows": [r],
                   "section": (r.get("Section") or "").strip(),
                   "title": (r.get("Title") or "").strip(),
                   "description": (r.get("Description") or "").strip()}
    elif current is not None:
        current["rows"].append(r)
if current is not None: listings.append(current)
print(f"Etsy listings: {len(listings)}")

# Match
def attempt_match(L):
    cn = ""
    for r in L["rows"]:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            cn = codename(vs)
            if cn: break

    etsy_text = f"{L['title']} {L['section']} {L['description'][:500]}"
    etsy_words = extract_distinctive_words(etsy_text)
    etsy_name = extract_name(L["title"])

    # 1: Exact codename
    if cn and cn in shop:
        return ("codename_exact", cn)

    # 2: Etsy title name -> Shopify name (e.g. "GUARDIAN | ..." both)
    if etsy_name and etsy_name in shop_by_name:
        return (f"name:{etsy_name}", shop_by_name[etsy_name])

    # 3: Title contains a Shopify proper-noun codename (e.g. "...Ring Hayden...")
    title_words = set(re.findall(r"[A-Za-z]+", L["title"]))
    for shop_cn in shop:
        if not re.match(r"^(JDTR|AYTR|TR\d|LST)", shop_cn) and len(shop_cn) >= 4:
            # Whole-word case-insensitive match of the codename in the title
            if shop_cn.lower() in {w.lower() for w in title_words}:
                return (f"title_contains:{shop_cn}", shop_cn)

    # 4: JDTR/AYTR digit-drop (JDTR1144 -> JDTR144)
    if cn and re.match(r"^(JDTR|AYTR|TR)\d+$", cn):
        base, num = re.match(r"^([A-Z]+)(\d+)$", cn).groups()
        if len(num) >= 4:
            candidate = base + num[1:]
            if candidate in shop:
                return (f"jdtr_drop_lead:{candidate}", candidate)

    # 5: Distinctive-word overlap
    if etsy_words:
        scores = Counter()
        for w in etsy_words:
            for shop_cn in word_to_codenames.get(w, []):
                scores[shop_cn] += 1
        if scores:
            top, top_score = scores.most_common(1)[0]
            second_score = scores.most_common(2)[1][1] if len(scores) > 1 else 0
            if top_score >= 3 and (top_score - second_score) >= 2:
                return (f"distinctive:{top_score}of{len(etsy_words)}", top)
            if top_score >= 4 and (top_score - second_score) >= 1:
                return (f"distinctive:{top_score}of{len(etsy_words)}", top)

    # 6: Handle-token overlap (Etsy title words vs handle words)
    etsy_title_tokens = {t.lower() for t in re.findall(r"[A-Za-z]{4,}", L["title"])}
    handle_scores = Counter()
    for tok in etsy_title_tokens:
        if tok in shop_by_handle_tokens:
            for shop_cn in shop_by_handle_tokens[tok]:
                handle_scores[shop_cn] += 1
    if handle_scores:
        top, top_score = handle_scores.most_common(1)[0]
        second_score = handle_scores.most_common(2)[1][1] if len(handle_scores) > 1 else 0
        if top_score >= 4 and (top_score - second_score) >= 2:
            return (f"handle_overlap:{top_score}", top)

    return None

xref = {}
unmatched_log = []
strategy_counts = Counter()

for L in listings:
    m = attempt_match(L)
    if m:
        via, shop_cn = m
        strategy_counts[via.split(":")[0]] += 1
        d = shop[shop_cn]
        xref[L["lid"]] = {
            "codename": shop_cn,
            "match_via": via,
            "etsy_section": L["section"],
            "etsy_title": L["title"],
            "shop_handle": d["handle"],
            "shop_title": d["title"],
            "shop_description": d["description"],
            "shop_tags": d["tags"],
            "shop_product_type": "",
            "shop_option_color": d["option_color"],
            "shop_widths": sorted(d["widths"], key=lambda x: float(x)),
            "shop_sizes": sorted(d["sizes"], key=lambda x: float(x)),
            "shop_first_sku": d["first_sku"],
        }
    else:
        cn_local = ""
        for r in L["rows"]:
            vs = (r.get("Var SKU") or "").strip()
            if vs:
                cn_local = codename(vs)
                if cn_local: break
        unmatched_log.append({
            "lid": L["lid"], "codename": cn_local, "section": L["section"],
            "title": L["title"][:120],
        })

OUT.write_text(json.dumps(xref, ensure_ascii=False, indent=2), encoding="utf-8")
DIAG.write_text(json.dumps({"unmatched": unmatched_log}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"\n=== TOTAL: {len(xref)}/502 ({len(xref)/502*100:.0f}%) ===")
print("Strategy counts:")
for s, n in strategy_counts.most_common():
    print(f"  {n:3d}  {s}")
print(f"Still unmatched: {len(unmatched_log)}")
print()
print("=== Still unmatched samples (first 20) ===")
for u in unmatched_log[:20]:
    print(f"  LID {u['lid']:<12}  cn={u['codename']!r:<14}  sec={u['section']!r:<25}  {u['title']!r}")
