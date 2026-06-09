"""Matcher v4: case-insensitive name match + compound SKU support + Shopify-title-first-word lookup.

Bugs fixed from v3:
  - extract_name was ALL-CAPS only. Etsy uses "GUARDIAN" but Shopify uses "Guardian" -> miss.
  - Codenames like FPR-JDTR061 were indexed only as 'FPR'. Now indexed as both 'FPR' AND 'JDTR061'.
  - Added Shopify-title-first-word lookup ("Guardian Black Brushed..." -> indexed as 'GUARDIAN').
"""
import csv, json, re, sys
from collections import defaultdict, Counter
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

ETSY = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
OUT  = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v4.json")
DIAG = Path(r"C:\Users\amirl\Downloads\matcher-v4-diagnostic.json")

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

def primary_codename(vs: str) -> str:
    return vs.strip().split("-")[0].upper() if vs else ""

def all_codenames_in_sku(vs: str) -> set[str]:
    """For SKU 'FPR-JDTR061-8-5' return {'FPR', 'JDTR061'}; for 'GALACTIC-8-5' return {'GALACTIC'}.
    Treats any uppercase alphanumeric token of length >= 3 as a possible codename."""
    if not vs: return set()
    out = set()
    for tok in re.split(r"[-_/.]", vs.strip().upper()):
        if not tok: continue
        # Skip pure-numeric tokens (those are sizes/widths)
        if tok.isdigit(): continue
        # Skip floats like 7.5
        if re.match(r"^\d+(\.\d+)?$", tok): continue
        if len(tok) >= 3:
            out.add(tok)
    return out

def normalize(s: str) -> str:
    return re.sub(r"[^\w\s]", " ", (s or "").lower())

def extract_distinctive_words(text: str) -> set[str]:
    blob = " " + normalize(text) + " "
    return {w.lower() for w in ALL_DISTINCTIVE if " " + w.lower() + " " in blob}

def extract_first_word(title: str) -> str:
    """Pull the first 'name'-ish token from a title.
       Examples:
         'GUARDIAN | Gold Ring'   -> 'GUARDIAN'
         'Guardian Black Brushed' -> 'GUARDIAN'  (case-insensitive)
         "Men's Tungsten Carbide..." -> 'MENS' (low signal but caught)
    """
    t = (title or "").strip()
    # Pattern A: ALL CAPS prefix followed by | or ,
    m = re.match(r"^([A-Z][A-Z0-9 \-]{2,})\s*[|,]", t)
    if m:
        return m.group(1).strip().upper()
    # Pattern B: Single capitalized word at start, followed by space then capital letter or descriptor
    m = re.match(r"^([A-Za-z]{3,})(?:\s|$|[,|])", t)
    if m:
        word = m.group(1).upper()
        # Filter out very common non-name words
        if word not in {"MEN", "MENS", "BLACK", "SILVER", "GOLD", "ROSE", "YELLOW",
                        "BLUE", "GREEN", "RED", "PURPLE", "WHITE", "TUNGSTEN", "CERAMIC",
                        "TITANIUM", "DAMASCUS", "WOOD", "RING", "BAND", "FOR", "THE",
                        "MAN", "AND", "WITH", "PERSONALIZED", "CUSTOM"}:
            return word
    return ""

# Load Shopify with COMPOUND codename support
print("Loading Shopify with compound codename support...")
shop = defaultdict(lambda: {"title": "", "description": "", "tags": "",
                             "handle": "", "first_sku": "", "widths": set(), "sizes": set(),
                             "option_color": ""})
codename_aliases = defaultdict(set)  # alias-codename -> primary-codename
shop_by_name = {}  # NAME -> primary codename
shop_by_handle_tokens = defaultdict(set)
shop_distinctive = {}
word_to_codenames = defaultdict(set)
title_first_word_to_codename = {}

with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        if not sku: continue
        primary = primary_codename(sku)
        all_cns = all_codenames_in_sku(sku)

        d = shop[primary]
        if not d["title"]:
            d["title"] = (r.get("title") or "").strip()
            d["description"] = (r.get("description") or "").strip()
            d["tags"] = (r.get("tags") or "").strip()
            d["handle"] = (r.get("handle") or "").strip()
            d["first_sku"] = sku
            d["option_color"] = (r.get("option_color") or "").strip()
        # Map every codename in the SKU to the primary (so 'JDTR061' -> 'FPR-JDTR061' primary)
        for c in all_cns:
            codename_aliases[c].add(primary)
        vt = (r.get("variant_title") or "").strip()
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m:
            d["widths"].add(m.group(1))
            d["sizes"].add(m.group(2))

# Build name + distinctive + handle indexes
for cn, d in shop.items():
    title_name = extract_first_word(d["title"])
    if title_name and title_name not in title_first_word_to_codename:
        title_first_word_to_codename[title_name] = cn
    if title_name and title_name not in shop_by_name:
        shop_by_name[title_name] = cn
    for tok in re.split(r"[-_]", d["handle"].lower()):
        if len(tok) >= 4:
            shop_by_handle_tokens[tok].add(cn)
    text = f"{d['title']} {d['tags']} {d['description']}"
    shop_distinctive[cn] = extract_distinctive_words(text)
    for w in shop_distinctive[cn]:
        word_to_codenames[w].add(cn)

print(f"Shopify primary codenames: {len(shop)}")
print(f"Total aliased codenames: {len(codename_aliases)} (incl. compound matches like JDTR061 -> FPR-JDTR061)")
print(f"Title first words indexed: {len(title_first_word_to_codename)}")

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

def attempt_match(L):
    # Get all codenames from Etsy variant SKUs
    etsy_codenames = set()
    primary_cn = ""
    for r in L["rows"]:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            etsy_codenames |= all_codenames_in_sku(vs)
            if not primary_cn:
                primary_cn = primary_codename(vs)

    etsy_text = f"{L['title']} {L['section']} {L['description'][:500]}"
    etsy_words = extract_distinctive_words(etsy_text)
    etsy_name = extract_first_word(L["title"])

    # 1: Any Etsy codename matches a Shopify primary codename
    for c in etsy_codenames:
        if c in shop:
            return ("codename_exact", c)
    # 2: Any Etsy codename matches a Shopify ALIAS codename
    for c in etsy_codenames:
        if c in codename_aliases:
            candidates = list(codename_aliases[c])
            if len(candidates) == 1:
                return (f"codename_aliased:{c}->{candidates[0]}", candidates[0])

    # 3: Etsy-title-name matches Shopify-title-name
    if etsy_name and etsy_name in shop_by_name:
        return (f"name:{etsy_name}", shop_by_name[etsy_name])

    # 4: Etsy-title-name matches Shopify-title-first-word
    if etsy_name and etsy_name in title_first_word_to_codename:
        return (f"shop_first_word:{etsy_name}", title_first_word_to_codename[etsy_name])

    # 5: Title contains any Shopify proper-noun codename
    title_words = {w.lower() for w in re.findall(r"[A-Za-z]+", L["title"])}
    for shop_cn in shop:
        if not re.match(r"^(JDTR|AYTR|TR\d|LST|ADC|FPR|AYSS)", shop_cn) and len(shop_cn) >= 4:
            if shop_cn.lower() in title_words:
                return (f"title_contains:{shop_cn}", shop_cn)

    # 6: JDTR/AYTR digit-drop fallback
    if primary_cn and re.match(r"^(JDTR|AYTR|TR)\d+$", primary_cn):
        base, num = re.match(r"^([A-Z]+)(\d+)$", primary_cn).groups()
        if len(num) >= 4:
            candidate = base + num[1:]
            if candidate in shop:
                return (f"jdtr_drop_lead:{candidate}", candidate)

    # 7: Distinctive-word overlap
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

    # 8: Handle-token overlap
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
                cn_local = primary_codename(vs)
                if cn_local: break
        unmatched_log.append({
            "lid": L["lid"], "codename": cn_local, "section": L["section"],
            "title": L["title"][:120], "first_word": extract_first_word(L["title"]),
        })

OUT.write_text(json.dumps(xref, ensure_ascii=False, indent=2), encoding="utf-8")
DIAG.write_text(json.dumps({"unmatched": unmatched_log}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"\n=== TOTAL: {len(xref)}/502 ({len(xref)/502*100:.0f}%) ===")
print("Strategy counts:")
for s, n in strategy_counts.most_common():
    print(f"  {n:3d}  {s}")
print(f"\nStill unmatched: {len(unmatched_log)}")
print("=== Still unmatched samples (first 15) ===")
for u in unmatched_log[:15]:
    print(f"  LID {u['lid']:<12}  cn={u['codename']!r:<14}  firstword={u['first_word']!r:<15}  sec={u['section']!r:<25}  {u['title']!r}")
