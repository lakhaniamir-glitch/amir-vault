"""Aggressive matcher: try every angle to match the 199 unmatched Etsy listings.

Strategies (in order of confidence):
  1. Direct codename match               (already done — 246 matches)
  2. Title-extracted product name match  (already done — 51 matches)
  3. Distinctive feature word overlap    (NEW — fuzzy match using inlay/material/color/finish words)
  4. JDTR partial codename match         (NEW — JDTR1144 -> try JDTR144 / JDTR1144 variations)
  5. Section + feature combo             (NEW — if section says 'Wood Inlay' and title says 'Box Elder', match)

Output: updated etsy-to-shopify-xref.json with as many matches as possible, plus a confidence score.
"""
import csv, json, re, sys
from collections import defaultdict, Counter
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

ETSY = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
EXISTING_XREF = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref.json")
OUT = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v2.json")
DIAGNOSTIC = Path(r"C:\Users\amirl\Downloads\fuzzy-match-diagnostic.json")

# Distinctive feature/inlay/material vocabulary — these are the words that uniquely identify ring types
DISTINCTIVE = {
    "materials":   ["tungsten", "ceramic", "damascus", "titanium", "cobalt", "wood"],
    "colors":      ["black", "silver", "rose gold", "yellow gold", "gold", "blue", "green",
                    "red", "purple", "orange", "white", "gunmetal", "pink", "camo"],
    "inlays":      ["opal", "abalone", "meteorite", "diamond", "antler", "fingerprint",
                    "carbon fiber", "lava rock", "dinosaur bone", "mother of pearl",
                    "mop", "rosewood", "olive wood", "koa", "box elder", "burl wood",
                    "burl", "zebra wood", "ironwood", "iron wood", "ebony", "bocote",
                    "goldstone", "malachite", "turquoise", "shell"],
    "finishes":    ["polished", "brushed", "beveled", "domed", "hammered", "pipe cut",
                    "grooved", "groove", "faceted", "matte", "stepped edge", "knurled",
                    "satin", "flat"],
}
ALL_DISTINCTIVE = set()
for vs in DISTINCTIVE.values():
    ALL_DISTINCTIVE.update(vs)

def codename(vs: str) -> str:
    return vs.strip().split("-")[0].upper() if vs else ""

def normalize(s: str) -> str:
    """Lowercase, single-space, remove punctuation."""
    return re.sub(r"[^\w\s]", " ", (s or "").lower())

def extract_distinctive_words(text: str) -> set[str]:
    """Find distinctive vocabulary words in text. Returns canonical lowercased phrases."""
    blob = " " + normalize(text) + " "
    found = set()
    for w in ALL_DISTINCTIVE:
        if " " + w.lower() + " " in blob:
            found.add(w.lower())
    return found

# Build Shopify product aggregation by codename (1915 codenames)
shop_by_codename = defaultdict(lambda: {"title": "", "description": "", "tags": "",
                                         "handle": "", "first_sku": "", "widths": set(), "sizes": set(),
                                         "option_color": "", "all_skus": set()})

print("Loading Shopify...")
shop_rows = 0
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        shop_rows += 1
        sku = (r.get("sku") or "").strip()
        cn = codename(sku)
        if not cn: continue
        d = shop_by_codename[cn]
        if not d["title"]:
            d["title"] = (r.get("title") or "").strip()
            d["description"] = (r.get("description") or "").strip()
            d["tags"] = (r.get("tags") or "").strip()
            d["handle"] = (r.get("handle") or "").strip()
            d["first_sku"] = sku
            d["option_color"] = (r.get("option_color") or "").strip()
        d["all_skus"].add(sku)
        vt = (r.get("variant_title") or "").strip()
        m = re.match(r"^(\d+(?:\.\d+)?)\s*mm\s*/\s*(\d+(?:\.\d+)?)$", vt)
        if m:
            d["widths"].add(m.group(1))
            d["sizes"].add(m.group(2))
print(f"Shopify rows: {shop_rows}, unique codenames: {len(shop_by_codename)}")

# Pre-compute distinctive word index per codename
shop_distinctive = {}  # codename -> set of distinctive words found
for cn, d in shop_by_codename.items():
    text = f"{d['title']} {d['tags']} {d['description']}"
    shop_distinctive[cn] = extract_distinctive_words(text)

# Also build inverted index: word -> set of codenames containing it (for quick lookup)
word_to_codenames = defaultdict(set)
for cn, words in shop_distinctive.items():
    for w in words:
        word_to_codenames[w].add(cn)

# Load existing xref
with open(EXISTING_XREF, encoding="utf-8") as f:
    xref = json.load(f)
print(f"Existing matches: {len(xref)}")

# Read Etsy export
with open(ETSY, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# Group into listings
listings = []
current = None
for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None:
            listings.append(current)
        current = {"lid": lid, "rows": [r], "section": (r.get("Section") or "").strip(),
                   "title": (r.get("Title") or "").strip(),
                   "description": (r.get("Description") or "").strip()}
    elif current is not None:
        current["rows"].append(r)
if current is not None:
    listings.append(current)

# Identify still-unmatched listings
unmatched = [L for L in listings if L["lid"] not in xref]
print(f"Unmatched listings to attempt: {len(unmatched)}")

# Fuzzy matching for each unmatched listing
new_matches = {}
ambiguous = []
no_match = []

# Build a corpus of Etsy distinctive words for each codename group already matched
# to learn which Etsy phrasings tend to mean which features
for L in unmatched:
    etsy_text = f"{L['title']} {L['section']} {L['description'][:500]}"
    etsy_words = extract_distinctive_words(etsy_text)

    # Get the Etsy Var SKU codename if present
    cn = ""
    for r in L["rows"]:
        vs = (r.get("Var SKU") or "").strip()
        if vs:
            cn = codename(vs)
            if cn: break

    # ATTEMPT A: JDTR partial codename match (JDTR1144 -> try JDTR144 / JDTR1144)
    a_match = None
    if cn and re.match(r"^(JDTR|AYTR|TR)\d+$", cn):
        # Try the same codename in Shopify (exact)
        if cn in shop_by_codename:
            a_match = ("exact_late_match", cn)
        else:
            # Try dropping the leading digit if 4+ digits (JDTR1144 -> JDTR144)
            base, num = re.match(r"^([A-Z]+)(\d+)$", cn).groups()
            if len(num) >= 4:
                candidate = base + num[1:]
                if candidate in shop_by_codename:
                    a_match = (f"jdtr_drop_lead:{candidate}", candidate)

    # ATTEMPT B: distinctive-word overlap scoring
    b_match = None
    if etsy_words:
        # Score each Shopify codename: # of distinctive words shared
        scores = Counter()
        for w in etsy_words:
            for shop_cn in word_to_codenames.get(w, []):
                scores[shop_cn] += 1
        if scores:
            top, top_score = scores.most_common(1)[0]
            # Must have at least 3 shared distinctive words AND clear winner (2+ ahead of second)
            second_score = scores.most_common(2)[1][1] if len(scores) > 1 else 0
            if top_score >= 3 and (top_score - second_score) >= 2:
                b_match = (f"distinctive_overlap:{top_score}of{len(etsy_words)}", top)
            elif top_score >= 4 and (top_score - second_score) >= 1:
                b_match = (f"distinctive_overlap:{top_score}of{len(etsy_words)}", top)

    chosen = a_match or b_match
    if chosen:
        match_via, shop_cn = chosen
        s = shop_by_codename[shop_cn]
        new_matches[L["lid"]] = {
            "codename": shop_cn,
            "match_via": match_via,
            "etsy_section": L["section"],
            "etsy_title": L["title"],
            "shop_handle": s["handle"],
            "shop_title": s["title"],
            "shop_description": s["description"],
            "shop_tags": s["tags"],
            "shop_product_type": "",
            "shop_option_color": s["option_color"],
            "shop_widths": sorted(s["widths"], key=lambda x: float(x)),
            "shop_sizes": sorted(s["sizes"], key=lambda x: float(x)),
            "shop_first_sku": s["first_sku"],
        }
    else:
        no_match.append({
            "lid": L["lid"], "codename": cn, "section": L["section"],
            "title": L["title"][:100], "distinctive_words": sorted(etsy_words),
        })

# Merge new matches into xref
final_xref = {**xref, **new_matches}
OUT.write_text(json.dumps(final_xref, ensure_ascii=False, indent=2), encoding="utf-8")
DIAGNOSTIC.write_text(json.dumps({
    "new_matches": new_matches,
    "still_unmatched": no_match,
}, ensure_ascii=False, indent=2), encoding="utf-8")

# Report
strategies = Counter(d["match_via"].split(":")[0] for d in new_matches.values())
print(f"\n=== FINAL TALLY ===")
print(f"Existing matches: {len(xref)}")
print(f"NEW matches added: {len(new_matches)}")
print(f"  By strategy:")
for s, n in strategies.most_common():
    print(f"    {n:3d}  {s}")
print(f"Total now: {len(final_xref)}/502  ({len(final_xref)/502*100:.0f}%)")
print(f"Still unmatched: {len(no_match)}")
print()
print("=== Sample new fuzzy matches (first 15) ===")
for lid, d in list(new_matches.items())[:15]:
    print(f"  LID {lid:<12}  via={d['match_via']:<35}  codename={d['codename']:<15}  Etsy title={d['etsy_title'][:60]!r}")
print()
print("=== Sample STILL unmatched (first 10) ===")
for n in no_match[:10]:
    print(f"  LID {n['lid']:<12}  cn={n['codename']!r:<14}  distinctive_words={n['distinctive_words'][:6]}")
    print(f"    title: {n['title']!r}")
print(f"\nWrote: {OUT}")
print(f"Diagnostic: {DIAGNOSTIC}")
