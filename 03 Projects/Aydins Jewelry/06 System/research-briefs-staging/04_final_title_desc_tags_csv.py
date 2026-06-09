"""FINAL builder: title + description + tags overlay on fresh Etsy export.

Formula corrections from user verification:
  - Title uses {Material} in BOTH slots (Wedding Band + Mens {Material} Ring) to match what's
    actually ranking on Aydins's current top listings.
  - Description: eRank hook prepended to Shopify description body.
  - Tags: 13-tag stack tailored per material.

Skip:
  - 13 discontinued listings (titles/desc/tags untouched)
  - 199 active listings without Shopify match (left alone for next pass)

Output:
  - title-desc-tags-FINAL-TEST10.csv   (10 verified for sanity check)
  - title-desc-tags-FINAL-FULL.csv     (502 listings; 290 get full update, 212 untouched)
"""
import csv, json, re, sys
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

FRESH = Path(r"C:\Users\amirl\Downloads\AydinsJewelry_Etsy_502_2026-06-09_16_58_13.csv")
XREF  = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref-v4.json")
SCRAPPED = Path(r"C:\Users\amirl\Documents\Amirs Command Center\brands\aydins\etsy-exports\2026-06-04\listings-to-deactivate-in-vela.txt")
OUT_TEST = Path(r"C:\Users\amirl\Downloads\title-desc-tags-FINAL-TEST10.csv")
OUT_FULL = Path(r"C:\Users\amirl\Downloads\title-desc-tags-FINAL-FULL.csv")

# Load
with open(XREF, encoding="utf-8") as f:
    xref = json.load(f)

scrapped = set()
with open(SCRAPPED, encoding="utf-8") as f:
    for line in f:
        s = line.strip()
        if s.isdigit():
            scrapped.add(s)

# Material extraction — prioritized by signal strength: shop title > description start > all text
def extract_material(tags: str, description: str, shop_title: str = "") -> str:
    # Strongest signal: Shopify product title
    title_l = (shop_title or "").lower()
    if "ceramic" in title_l: return "Ceramic"
    if "damascus" in title_l: return "Damascus Steel"
    if "titanium" in title_l: return "Titanium"
    if "tungsten" in title_l: return "Tungsten"

    # Next: first 200 chars of description (product subject line)
    desc_start = (description or "")[:200].lower()
    if "ceramic" in desc_start: return "Ceramic"
    if "damascus" in desc_start: return "Damascus Steel"
    if "titanium" in desc_start: return "Titanium"
    if "tungsten" in desc_start: return "Tungsten"

    # Fallback: all text — Tungsten wins over Cobalt because Aydins is tungsten-dominant
    blob = (tags + " " + description).lower()
    if "tungsten" in blob: return "Tungsten"
    if "ceramic" in blob: return "Ceramic"
    if "damascus" in blob: return "Damascus Steel"
    if "titanium" in blob: return "Titanium"
    if "cobalt" in blob: return "Cobalt"
    return "Tungsten"

def material_short(material: str) -> str:
    """For the 'Mens X Ring' slot - shorter form."""
    return {"Damascus Steel": "Damascus", "Tungsten": "Tungsten",
            "Ceramic": "Ceramic", "Titanium": "Titanium", "Cobalt": "Cobalt"}.get(material, "Tungsten")

# Color extraction
def extract_color(tags: str, description: str, section: str) -> str:
    blob = " " + (tags + " " + description + " " + section).lower() + " "
    for c in ["Rose Gold", "Yellow Gold", "Gunmetal", "Black", "Silver", "Gold",
              "Blue", "Green", "Red", "Purple", "Orange", "White"]:
        if " " + c.lower() + " " in blob:
            return c
    return "Silver"

# Feature extraction
FEATURE_KEYWORDS = [
    ("Opal Inlay", r"\bopal\b"),
    ("Meteorite", r"\bmeteorite\b"),
    ("Koa Wood", r"\bkoa\b"),
    ("Box Elder Wood", r"\bbox elder\b"),
    ("Olive Wood", r"\bolive wood\b"),
    ("Wood Inlay", r"\bwood\b"),
    ("Carbon Fiber", r"\bcarbon fiber\b"),
    ("Antler", r"\bantler\b"),
    ("Dinosaur Bone", r"\bdinosaur\b"),
    ("Mother of Pearl", r"\bmother of pearl\b|\bmop\b"),
    ("Abalone", r"\babalone\b"),
    ("Diamond", r"\bdiamond\b"),
    ("Fingerprint", r"\bfingerprint\b"),
    ("Hammered", r"\bhammered\b"),
    ("Brushed Finish", r"\bbrushed\b"),
    ("Beveled", r"\bbeveled\b"),
    ("Domed", r"\bdomed\b"),
    ("Pipe Cut", r"\bpipe cut\b"),
    ("Grooved", r"\bgroove[ds]?\b"),
    ("Faceted", r"\bfaceted\b"),
    ("Stepped Edge", r"\bstepped edge\b|\bstep edge\b"),
]
def extract_feature(tags: str, description: str, shop_title: str) -> str:
    blob = (shop_title + " " + tags + " " + description).lower()
    for canonical, pat in FEATURE_KEYWORDS:
        if re.search(pat, blob, re.IGNORECASE):
            return canonical
    return ""

def format_widths(widths: list[str]) -> str:
    if not widths: return "8mm"
    if len(widths) == 1: return f"{widths[0]}mm"
    return f"{widths[0]}-{widths[-1]}mm"

# Title builder — CORRECTED formula matching what's actually ranking on Aydins
def build_title(material: str, widths: str, color: str, feature: str) -> str:
    mshort = material_short(material)
    fpart = f" {feature}" if feature else ""
    title = (f"{material} Wedding Band for Men, {widths} {color} Mens {mshort} Ring"
             f"{fpart}, Personalized Engraved Ring, Comfort Fit")
    if len(title) > 140:
        title = f"{material} Wedding Band for Men, {widths} {color} Mens {mshort} Ring{fpart}, Comfort Fit"
    if len(title) > 140:
        title = title[:140].rstrip(", ")
    return title

# Description builder — eRank hook + Shopify body
def clean_text(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s or "")
    s = s.replace("—", ". ").replace("–", "-")  # em-dash -> period, en-dash -> hyphen
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def build_description(material: str, shop_description: str) -> str:
    hook = (f"{material} wedding band for men, engraved and shipped from our Irving, "
            f"Texas workshop. Free engraving, free 2-day FedEx, lifetime sizing. Comfort fit.")
    body = clean_text(shop_description)
    return f"{hook}\n\n{body}" if body else hook

# Tag builder — 13-tag stack per material (Etsy: 13 tags max, 20 chars each)
def build_tags(material: str, color: str, feature: str) -> str:
    mshort = material_short(material).lower()
    color_l = color.lower()
    base_tungsten = [
        "tungsten ring", "mens wedding band", "mens wedding ring",
        "mens tungsten ring", "mens tungsten band", "personalized ring",
        "engraved ring", "tungsten band", "mens ring",
        "wedding band men", "comfort fit ring",
    ]
    base_ceramic = [
        "ceramic ring", "mens wedding band", "mens wedding ring",
        "mens ceramic ring", "ceramic wedding band", "personalized ring",
        "engraved ring", "ceramic band", "mens ring",
        "wedding band men", "comfort fit ring",
    ]
    base_damascus = [
        "damascus ring", "mens wedding band", "mens wedding ring",
        "damascus steel ring", "damascus band", "personalized ring",
        "engraved ring", "mens ring", "wedding band men",
        "comfort fit ring", "anniversary gift",
    ]
    base_titanium = [
        "titanium ring", "mens wedding band", "mens wedding ring",
        "mens titanium ring", "titanium wedding band", "personalized ring",
        "engraved ring", "titanium band", "mens ring",
        "wedding band men", "comfort fit ring",
    ]
    base = {
        "Tungsten": base_tungsten, "Ceramic": base_ceramic,
        "Damascus Steel": base_damascus, "Titanium": base_titanium,
    }.get(material, base_tungsten)

    # Slots 12 + 13: color-specific tag + feature/width tag
    extra = []
    color_tag = f"{color_l} {mshort} ring"
    if len(color_tag) <= 20: extra.append(color_tag)
    elif len(f"{color_l} ring") <= 20: extra.append(f"{color_l} ring")
    if feature:
        feat_tag = f"{feature.lower()} ring"
        if len(feat_tag) <= 20: extra.append(feat_tag)
        elif len(feature.lower()) <= 20: extra.append(feature.lower())

    tags = base + extra
    # Etsy: each tag <= 20 chars, 13 tags max
    tags = [t for t in tags if len(t) <= 20]
    # Dedup preserving order
    seen, deduped = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t); deduped.append(t)
    return ",".join(deduped[:13])

# Read fresh Etsy export
with open(FRESH, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

blocks = []
current = None
for i, r in enumerate(rows):
    lid = (r.get("Listing ID") or "").strip()
    if lid:
        if current is not None:
            blocks.append(current)
        current = {"lid": lid, "rows": [i]}
    elif current is not None:
        current["rows"].append(i)
if current is not None:
    blocks.append(current)

print(f"Fresh export listings: {len(blocks)}")

# Determine action per block
def get_action(block):
    lid = block["lid"]
    if lid in scrapped:
        return "skip_discontinued"
    if lid in xref:
        return "update"
    return "skip_unmatched"

# Generate updates for matched listings
generated = {}  # lid -> {title, description, tags, debug}
for block in blocks:
    if get_action(block) != "update":
        continue
    x = xref[block["lid"]]
    material = extract_material(x["shop_tags"], x["shop_description"], x["shop_title"])
    color = extract_color(x["shop_tags"], x["shop_description"], x["etsy_section"])
    feature = extract_feature(x["shop_tags"], x["shop_description"], x["shop_title"])
    widths = format_widths(x["shop_widths"])
    title = build_title(material, widths, color, feature)
    desc = build_description(material, x["shop_description"])
    tags = build_tags(material, color, feature)
    generated[block["lid"]] = {
        "title": title, "description": desc, "tags": tags,
        "debug": {"material": material, "color": color, "feature": feature, "widths": widths, "codename": x["codename"]},
    }

print(f"Will update: {len(generated)}")
counts = {"update": 0, "skip_discontinued": 0, "skip_unmatched": 0}
for block in blocks:
    counts[get_action(block)] += 1
print(f"  update: {counts['update']}")
print(f"  skip_discontinued: {counts['skip_discontinued']}")
print(f"  skip_unmatched: {counts['skip_unmatched']}")

def emit(block, out_rows):
    """Emit all rows of a listing block. Apply title/desc/tags only on first row if 'update'."""
    update = get_action(block) == "update"
    gen = generated.get(block["lid"]) if update else None
    for idx_pos, row_i in enumerate(block["rows"]):
        r = dict(rows[row_i])
        if idx_pos == 0 and gen:
            r["Title"] = gen["title"]
            r["Description"] = gen["description"]
            r["Tags"] = gen["tags"]
        out_rows.append(r)

# TEST10 — pick 10 verified ring listings (exclude already-tested + discontinued)
PREV_DONE = {
    "542735340", "522912537", "528037261", "1205810812", "1219759609",
    "575451015", "538386672", "817764707", "650116038", "526238869",
}
test_candidates = [b for b in blocks
                   if get_action(b) == "update" and b["lid"] not in PREV_DONE]
test_blocks = test_candidates[:10]

test_rows = []
for block in test_blocks:
    emit(block, test_rows)

with open(OUT_TEST, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(test_rows)

# FULL — every listing in fresh export
full_rows = []
for block in blocks:
    emit(block, full_rows)

with open(OUT_FULL, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    w.writeheader()
    w.writerows(full_rows)

print()
print(f"TEST: {OUT_TEST.name}  ({len(test_blocks)} updates, {len(test_rows)} rows)")
print(f"FULL: {OUT_FULL.name}  ({len(blocks)} listings, {len(full_rows)} rows)")
print()

# Show TEST10 with full title/desc preview/tags
print("=" * 80)
print("TEST10 — verify before push")
print("=" * 80)
for block in test_blocks:
    g = generated[block["lid"]]
    cur_title = (rows[block["rows"][0]].get("Title") or "")[:120]
    print(f"\nLID {block['lid']}  codename={g['debug']['codename']!r}")
    print(f"  Mat/Color/Feature/Widths: {g['debug']['material']!r} / {g['debug']['color']!r} / {g['debug']['feature']!r} / {g['debug']['widths']!r}")
    print(f"  CURRENT title: {cur_title!r}")
    print(f"  NEW title:     {g['title']!r}")
    print(f"  NEW tags:      {g['tags']!r}")
    print(f"  NEW desc[:200]: {g['description'][:200]!r}")
