"""For listings with duplicate titles (after SKU strip), extract a distinguishing
descriptor from the ORIGINAL pre-fix title and inject it into the playbook title.
Uses an expanded feature/finish vocabulary."""
import csv, re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")
CURRENT = ROOT / "listings-corrected.csv"
ORIGINAL = ROOT / "listings-corrected.csv.pre-sku-fix-2026-06-08"

# Expanded distinguishing descriptors (these go in the FEATURE slot of the title formula)
# Ordered by specificity - more specific first
DISTINGUISHERS = [
    # Inlays / wood specifics (already mostly handled by playbook but keep for fallback)
    ("box elder",     "Box Elder Wood"),
    ("bocote",        "Bocote Wood"),
    ("wenge",         "Wenge Wood"),
    ("zebrawood",     "Zebrawood"),
    ("rosewood",      "Rosewood"),
    ("whiskey barrel","Whiskey Barrel"),
    ("burl wood",     "Burl Wood"),
    ("red burl",      "Red Burl Wood"),
    ("koa",           "Koa Wood"),
    ("olive wood",    "Olive Wood"),
    ("walnut",        "Walnut Inlay"),
    ("iron wood",     "Ironwood"),
    ("ironwood",      "Ironwood"),
    ("oak wood",      "Oak Wood"),
    ("redwood",       "Redwood Inlay"),
    ("sequoia",       "Sequoia Wood"),
    # Stones / unique inlays
    ("mother of pearl","Mother of Pearl"),
    ("dinosaur bone", "Dinosaur Bone"),
    ("meteorite",     "Meteorite Inlay"),
    ("opal",          "Opal Inlay"),
    ("abalone",       "Abalone Inlay"),
    ("turquoise",     "Turquoise Inlay"),
    ("antler",        "Deer Antler"),
    ("sapphire",      "Sapphire"),
    ("ruby",          "Ruby"),
    ("alexandrite",   "Alexandrite Inlay"),
    ("goldstone",     "Goldstone Inlay"),
    ("tiger cowrie",  "Tiger Cowrie"),
    ("lava rock",     "Lava Rock"),
    ("malachite",     "Malachite"),
    ("carbon fiber",  "Carbon Fiber"),
    ("damascus",      "Damascus Pattern"),
    # Patterns / styles
    ("celtic",        "Celtic Dragon"),
    ("fingerprint",   "Fingerprint"),
    ("cross",         "Cross Pattern"),
    ("rune",          "Rune Pattern"),
    ("fleur",         "Fleur de Lis"),
    ("octagon",       "Octagon Cut"),
    ("hexagon",       "Hexagon"),
    # Profiles / cuts
    ("pipe cut",      "Pipe Cut"),
    ("stepped edge",  "Stepped Edge"),
    ("stepped",       "Stepped Edge"),
    ("beveled edge",  "Beveled Edge"),
    ("beveled",       "Beveled"),
    ("rounded",       "Rounded"),
    ("dome",          "Domed Profile"),
    ("domed",         "Domed Profile"),
    ("flat",          "Flat Profile"),
    ("rounded edges", "Rounded Edges"),
    # Finishes
    ("hammered",      "Hammered"),
    ("brushed",       "Brushed Finish"),
    ("polished",      "Polished Finish"),
    ("matte",         "Matte Finish"),
    ("satin",         "Satin Finish"),
    # Special elements
    ("spinner",       "Spinner Ring"),
    ("groove",        "Grooved"),
    ("inlay",         "Inlay"),
    ("two tone",      "Two Tone"),
    ("two-tone",      "Two Tone"),
    ("eternity",      "Eternity Band"),
    ("milgrain",      "Milgrain"),
    ("diamond",       "with Diamond"),
    ("cz",            "with CZ"),
    ("crystal",       "with Crystal"),
]

def find_distinguisher(old_title, current_title):
    """Find first matching distinguisher from old_title that ISN'T already in current_title."""
    if not old_title: return None
    old_lower = old_title.lower()
    current_lower = current_title.lower()
    for kw, label in DISTINGUISHERS:
        if kw in old_lower and label.lower() not in current_lower:
            return label
    return None

# Load original titles by listing ID
original_titles = {}
with open(ORIGINAL, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        lid = (r.get("Listing ID") or "").strip()
        if lid:
            original_titles[lid] = r.get("Title","")

# Load current CSV
with open(CURRENT, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Group by current title
title_groups = defaultdict(list)
for i, r in enumerate(rows):
    lid = (r.get("Listing ID") or "").strip()
    if not lid: continue
    t = (r.get("Title") or "").strip()
    if t:
        title_groups[t].append(i)

# For each group with >=2 listings, try to differentiate each
distinguished = 0
unable_to_distinguish = 0
samples_distinguished = []
samples_unable = []

for title, indices in title_groups.items():
    if len(indices) < 2: continue
    for idx in indices:
        r = rows[idx]
        lid = (r.get("Listing ID") or "").strip()
        old_title = original_titles.get(lid, "")
        distinguisher = find_distinguisher(old_title, title)
        if distinguisher:
            # Insert distinguisher before ", Personalized Engraved Ring"
            new_title = title
            tail = ", Personalized Engraved Ring, Comfort Fit"
            if new_title.endswith(tail):
                new_title = new_title[:-len(tail)] + f" {distinguisher}" + tail
            elif new_title.endswith(", Comfort Fit"):
                new_title = new_title[:-len(", Comfort Fit")] + f" {distinguisher}, Comfort Fit"
            else:
                new_title = new_title + " " + distinguisher
            # Enforce 140-char cap
            if len(new_title) > 140:
                new_title = new_title[:140].rstrip(", ")
            r["Title"] = new_title
            distinguished += 1
            if len(samples_distinguished) < 6:
                samples_distinguished.append((lid, title, new_title))
        else:
            unable_to_distinguish += 1
            if len(samples_unable) < 4:
                samples_unable.append((lid, title, old_title[:80]))

# Write back
tmp = CURRENT.with_suffix(".csv.tmp")
with open(tmp, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
tmp.replace(CURRENT)

print(f"distinguished: {distinguished} listings")
print(f"unable_to_distinguish: {unable_to_distinguish} listings (will remain as dup-titles)")

if samples_distinguished:
    print("\n=== Samples DISTINGUISHED ===")
    for lid, old, new in samples_distinguished:
        print(f"L:{lid}")
        print(f"  OLD: {old}")
        print(f"  NEW: {new}")
        print()

if samples_unable:
    print("=== Samples UNABLE to distinguish (no descriptor found in old title) ===")
    for lid, current, old in samples_unable:
        print(f"L:{lid}")
        print(f"  Current: {current}")
        print(f"  Old: {old}")
        print()

# Final dup count
with open(CURRENT, encoding="utf-8") as f:
    rows2 = list(csv.DictReader(f))
titles = [r.get("Title","").strip() for r in rows2 if (r.get("Listing ID") or "").strip()]
from collections import Counter
c = Counter(titles)
dups = sum(1 for n in c.values() if n > 1)
total_dup_listings = sum(n for n in c.values() if n > 1)
print(f"\nfinal: {len(set(titles))} unique titles, {dups} dup groups covering {total_dup_listings} listings")
