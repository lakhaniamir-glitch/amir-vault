"""Step 3: Generate eRank-format titles + clean descriptions from Shopify source data.
Operates on the etsy-to-shopify-xref.json built by step 2.

Title formula (eRank-researched, capped at 140 chars):
  [Material] Wedding Band for Men, [Width] [Color] Mens Wedding Ring [Feature], Personalized Engraved Ring, Comfort Fit

Description: uses Shopify description body. Cleaned for Etsy (no HTML, no em dashes, no double spaces).
"""
import json, re
from pathlib import Path

XREF = Path(r"C:\Users\amirl\Downloads\etsy-to-shopify-xref.json")
OUT = Path(r"C:\Users\amirl\Downloads\generated-titles-descriptions.json")

with open(XREF, encoding="utf-8") as f:
    xref = json.load(f)

# Tag-based extractors (Shopify tags are reliable)
MATERIAL_TAGS = ["Ceramic", "Tungsten", "Titanium", "Damascus", "Cobalt"]
COLOR_TAGS = ["Black", "Silver", "Rose Gold", "Yellow Gold", "Gold", "Blue", "Green", "Red",
              "Purple", "Orange", "White", "Gunmetal", "Camo", "Gunmetal Grey"]

FEATURE_KEYWORDS = [
    # (canonical feature -> regex pattern in description/tags, case-insensitive)
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

def extract_material(tags: str, description: str) -> str:
    blob = (tags + " " + description).lower()
    # Priority: Ceramic > Damascus > Titanium > Tungsten (only one wins; ceramic/damascus are more specific)
    if "ceramic" in blob: return "Ceramic"
    if "damascus" in blob: return "Damascus Steel"
    if "titanium" in blob: return "Titanium"
    if "tungsten" in blob or "tungsten carbide" in blob: return "Tungsten"
    if "cobalt" in blob: return "Cobalt"
    return "Tungsten"  # default for Aydins catalog

def extract_color(tags: str, description: str, etsy_section: str) -> str:
    """Find the dominant color. Prefer specific colors from section/tags first."""
    blob = " " + tags.lower() + " " + description.lower() + " " + etsy_section.lower() + " "
    # Specific colors first (longer phrases)
    for c in ["Rose Gold", "Yellow Gold", "Gunmetal", "Black", "Silver", "Gold",
              "Blue", "Green", "Red", "Purple", "Orange", "White"]:
        if " " + c.lower() + " " in blob:
            return c
    return "Silver"  # default

def extract_feature(tags: str, description: str, shop_title: str) -> str:
    """Pick the most distinctive feature for the title."""
    blob = (shop_title + " " + tags + " " + description).lower()
    for canonical, pat in FEATURE_KEYWORDS:
        if re.search(pat, blob, re.IGNORECASE):
            return canonical
    return ""  # no feature found

def format_widths(widths: list[str]) -> str:
    """['4', '6', '8'] -> '4-8mm', ['8'] -> '8mm'."""
    if not widths: return "8mm"
    if len(widths) == 1: return f"{widths[0]}mm"
    return f"{widths[0]}-{widths[-1]}mm"

def clean_description(desc: str) -> str:
    """Sanitize Shopify description body for Etsy: strip HTML, normalize whitespace, drop em-dashes."""
    if not desc: return ""
    # Strip HTML tags
    out = re.sub(r"<[^>]+>", "", desc)
    # Replace em dashes per Aydins policy
    out = out.replace("—", ". ").replace("—", ". ")
    # Collapse extra whitespace but preserve paragraph breaks
    out = re.sub(r"[ \t]+", " ", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip()

def build_title(xref_entry: dict) -> tuple[str, dict]:
    material = extract_material(xref_entry["shop_tags"], xref_entry["shop_description"])
    color = extract_color(xref_entry["shop_tags"], xref_entry["shop_description"], xref_entry["etsy_section"])
    feature = extract_feature(xref_entry["shop_tags"], xref_entry["shop_description"], xref_entry["shop_title"])
    widths = format_widths(xref_entry["shop_widths"])

    # Title: <Material> Wedding Band for Men, <Width> <Color> Mens Wedding Ring <Feature>, Personalized Engraved Ring, Comfort Fit
    parts_optional_feature = f" {feature}" if feature else ""
    title = (
        f"{material} Wedding Band for Men, {widths} {color} Mens Wedding Ring"
        f"{parts_optional_feature}, Personalized Engraved Ring, Comfort Fit"
    )
    # Cap at 140 chars (Etsy limit)
    if len(title) > 140:
        # Drop the "Personalized Engraved Ring" portion if needed
        title = f"{material} Wedding Band for Men, {widths} {color} Mens Wedding Ring{parts_optional_feature}, Comfort Fit"
    if len(title) > 140:
        title = title[:140]

    return title, {"material": material, "color": color, "feature": feature, "widths": widths}

# Build the generated table
out = {}
for lid, x in xref.items():
    new_title, debug = build_title(x)
    new_desc = clean_description(x["shop_description"])
    out[lid] = {
        "etsy_title_current": x["etsy_title"],
        "new_title": new_title,
        "new_desc_first_200": new_desc[:200],
        "new_desc_len": len(new_desc),
        "shop_codename": x["codename"],
        "shop_handle": x["shop_handle"],
        "shop_title": x["shop_title"],
        "match_via": x["match_via"],
        "debug": debug,
        "new_desc_full": new_desc,
    }

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated titles+descriptions for: {len(out)} listings")
print(f"Wrote: {OUT}")
print()

# Show 10 spot-checks
print("=" * 80)
print("SAMPLE: 10 listings for verification")
print("=" * 80)
samples = list(out.items())[:10]
for lid, d in samples:
    print(f"\nLID {lid}  codename={d['shop_codename']!r}  via={d['match_via']}")
    print(f"  Shop title: {d['shop_title']!r}")
    print(f"  Material/Color/Feature/Width: {d['debug']}")
    print(f"  CURRENT Etsy: {d['etsy_title_current'][:120]!r}")
    print(f"  NEW Etsy:     {d['new_title']!r}")
    print(f"  NEW desc[:160]: {d['new_desc_first_200'][:160]!r}")
print()

# Specific GALACTIC check
print("=" * 80)
print("GALACTIC SPECIFIC CHECK")
print("=" * 80)
for lid, d in out.items():
    if d["shop_codename"] == "GALACTIC":
        print(f"LID {lid}")
        print(f"  CURRENT Etsy: {d['etsy_title_current']!r}")
        print(f"  NEW Etsy:     {d['new_title']!r}")
        print(f"  Debug: {d['debug']}")
        print(f"  New desc[:300]: {d['new_desc_first_200'][:300]!r}")
        break
