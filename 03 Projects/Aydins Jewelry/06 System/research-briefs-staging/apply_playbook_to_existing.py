#!/usr/bin/env python3
"""Apply Etsy Champion Playbook (title + tags) to listings-corrected.csv (the 501 existing Etsy listings).
Per listing: rewrite Title (Etsy SEO format) and Tags (13-tag eRank stack) based on detected material/color/width/feature.
Preserves: SKU fix, policy scrub, Photo URLs (not touched), Var SKU, all variant rows."""
import csv, json, re, shutil
from pathlib import Path
from collections import OrderedDict, Counter

ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04')
CSV = ROOT / 'listings-corrected.csv'
SNAP = ROOT / 'listings-corrected.csv.pre-playbook-2026-06-08'

if not SNAP.exists():
    shutil.copy(CSV, SNAP)
    print(f'snapshot: {SNAP.name}')

# === Detection helpers (work from row data, not JSON) ===
MATERIAL_TITLE = {
    'tungsten': 'Tungsten', 'titanium': 'Titanium', 'damascus': 'Damascus Steel',
    'ceramic': 'Ceramic', 'aluminum': 'Aluminum', 'stainless': 'Stainless Steel',
    'silver': 'Silver',
}
COLOR_TITLE = {'black': 'Black', 'silver': 'Silver', 'gold': 'Gold', 'rose gold': 'Rose Gold',
               'blue': 'Blue', 'green': 'Green', 'red': 'Red', 'purple': 'Purple',
               'white': 'White', 'yellow gold': 'Yellow Gold', 'orange': 'Orange',
               'pink': 'Pink', 'gunmetal': 'Gunmetal', 'two tone': 'Two Tone',
               'brown': 'Brown'}
FEATURE_LABEL = {
    'meteorite': 'Meteorite Inlay', 'wood inlay': 'Wood Inlay', 'koa': 'Koa Wood',
    'olive wood': 'Olive Wood', 'walnut': 'Walnut Inlay', 'iron wood': 'Ironwood',
    'opal': 'Opal Inlay', 'celtic': 'Celtic Dragon', 'hammered': 'Hammered',
    'spinner': 'Spinner Ring', 'carbon fiber': 'Carbon Fiber', 'beveled': 'Beveled',
    'brushed': 'Brushed Finish', 'turquoise': 'Turquoise Inlay',
    'fingerprint': 'Fingerprint', 'antler': 'Deer Antler',
    'dinosaur bone': 'Dinosaur Bone', 'whiskey barrel': 'Whiskey Barrel',
    'abalone': 'Abalone', 'damascus': 'Damascus Pattern',
}

def detect_material(blob):
    blob = blob.lower()
    if 'tungsten' in blob: return 'tungsten'
    if 'titanium' in blob: return 'titanium'
    if 'damascus' in blob: return 'damascus'
    if 'ceramic' in blob: return 'ceramic'
    if 'aluminum' in blob: return 'aluminum'
    if 'stainless' in blob: return 'stainless'
    return 'tungsten'  # default

def detect_color(section, title, tags):
    blob = f'{section} {title} {tags}'.lower()
    for c in ['rose gold', 'yellow gold', 'two tone', 'gun metal', 'gunmetal',
              'black', 'silver', 'gold', 'blue', 'green', 'red', 'purple',
              'white', 'orange', 'pink', 'brown']:
        if c in blob: return c
    return None

def detect_width(v2_option, title):
    if v2_option:
        m = re.match(r'^(\d+(?:\.\d+)?)\s*mm?$', v2_option.lower())
        if m: return m.group(1).rstrip('0').rstrip('.') if '.' in m.group(1) else m.group(1)
    # Fall back to title scan
    m = re.search(r'(\d+(?:\.\d+)?)\s*mm', title.lower())
    if m: return m.group(1).rstrip('0').rstrip('.') if '.' in m.group(1) else m.group(1)
    return None

def detect_feature(title, tags):
    blob = f'{title} {tags}'.lower()
    for k, label in FEATURE_LABEL.items():
        if k in blob: return label
    return None

def is_dog_tag(title, var_sku):
    return 'dog tag' in title.lower() or 'dog-tag' in (var_sku or '').lower()

def is_signet(title, var_sku):
    return 'signet' in title.lower() or 'SIGNET' in (var_sku or '')

def is_fingerprint(title):
    return 'fingerprint' in title.lower()


def build_title(material, color, width, feature, title_existing, var_sku):
    if is_dog_tag(title_existing, var_sku):
        return 'Personalized Fingerprint Dog Tag Necklace, Mens Engraved Stainless Steel Dog Tag Pendant, Memorial Gift'[:140]
    if is_signet(title_existing, var_sku):
        return 'Mens Signet Ring, Personalized Engraved Signet Ring, Custom Laser Engraved Gold Silver Black Signet Ring'[:140]
    if is_fingerprint(title_existing) and 'wedding' not in title_existing.lower()[:30]:
        return 'Fingerprint Wedding Band, His and Hers Couples Ring, Mens Tungsten Personalized Engraved Promise Anniversary Ring'[:140]

    mat_t = MATERIAL_TITLE.get(material, 'Tungsten')
    color_t = COLOR_TITLE.get(color or '', '') if color else ''
    width_t = f'{width}mm' if width else ''
    opening = 'Damascus Steel Ring for Men' if material == 'damascus' else f'{mat_t} Wedding Band for Men'
    parts = []
    if width_t: parts.append(width_t)
    if color_t: parts.append(color_t)
    parts.append(f'Mens {mat_t} Ring' if material != 'damascus' else 'Mens Damascus Ring')
    if feature: parts.append(feature)
    middle = ' '.join(parts)
    full = f'{opening}, {middle}, Personalized Engraved Ring, Comfort Fit'
    if len(full) > 140: full = f'{opening}, {middle}, Comfort Fit'
    if len(full) > 140 and feature:
        no_feat = ' '.join(parts[:-1])
        full = f'{opening}, {no_feat}, Comfort Fit'
    if len(full) > 140: full = full[:140].rstrip(', ')
    return full


# === Tag generator (playbook 13-stack) ===
MAX_TAG_LEN = 20

def clean_tag(t):
    t = re.sub(r'[^A-Za-z0-9 ]+', '', t).strip().lower()
    return t[:MAX_TAG_LEN]

def build_tags(material, color, width, feature_kw, title, var_sku):
    if is_dog_tag(title, var_sku):
        return [clean_tag(t) for t in [
            'fingerprint tag', 'dog tag necklace', 'mens dog tag',
            'engraved dog tag', 'personalized tag', 'stainless steel',
            'mens necklace', 'gift for him', 'fingerprint jewelry',
            'memorial dog tag', 'custom dog tag', 'mens pendant', 'engraved necklace'
        ]]
    if is_signet(title, var_sku):
        return [clean_tag(t) for t in [
            'mens signet ring', 'signet ring mens', 'engraved signet',
            'personalized ring', 'custom signet ring', 'gold signet ring',
            'mens ring', 'gift for him', 'engraved ring',
            'fingerprint ring', 'mens jewelry', 'custom ring', 'silver signet ring'
        ]]
    if is_fingerprint(title) and 'wedding' not in title.lower()[:30]:
        return [clean_tag(t) for t in [
            'fingerprint ring', 'mens wedding band', 'personalized ring',
            'engraved ring', 'mens ring', 'tungsten ring',
            'mens tungsten ring', 'wedding band men', 'comfort fit ring',
            'couples ring', 'his and hers ring', 'promise ring', 'anniversary ring'
        ]]

    base = [
        f'{material} ring', 'mens wedding band', 'mens wedding ring',
        f'mens {material} ring', f'mens {material} band', 'personalized ring',
        'engraved ring', f'{material} band', 'mens ring', 'wedding band men',
        'comfort fit ring',
    ]
    if color:
        opts = [f'{color} {material} ring', f'{color} {material} band',
                f'{color} ring mens', f'{color} mens band']
        slot12 = next((o for o in opts if len(o) <= MAX_TAG_LEN), 'mens wedding bands')
    else:
        slot12 = 'mens wedding bands'
    base.append(slot12)

    feat_tag = None
    fkw = (feature_kw or '').lower()
    if 'meteorite' in fkw: feat_tag = 'meteorite ring'
    elif 'damascus' in fkw and material != 'damascus': feat_tag = 'damascus ring'
    elif any(w in fkw for w in ['wood', 'koa', 'olive', 'walnut', 'ironwood']): feat_tag = 'wood inlay ring'
    elif 'opal' in fkw: feat_tag = 'opal ring mens'
    elif 'celtic' in fkw: feat_tag = 'celtic ring'
    elif 'hammered' in fkw: feat_tag = 'hammered ring'
    elif 'spinner' in fkw: feat_tag = 'spinner ring mens'
    elif 'carbon fiber' in fkw: feat_tag = 'carbon fiber ring'
    elif 'beveled' in fkw: feat_tag = 'beveled ring'
    elif 'brushed' in fkw: feat_tag = 'brushed ring'
    elif 'diamond' in fkw: feat_tag = 'mens diamond ring'

    if feat_tag:
        base.append(feat_tag)
    elif width:
        base.append(f'{width}mm wedding band')
    else:
        base.append('mens wedding ring')

    seen, out = set(), []
    for t in base:
        c = clean_tag(t)
        if c and c not in seen and len(c) <= MAX_TAG_LEN:
            seen.add(c); out.append(c)
        if len(out) >= 13: break
    return out


# === Read and process ===
with open(SNAP, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

print(f'total rows: {len(rows)}')

# Iterate by listing block. Listing ID changes denote new listings.
# For each listing's first row, rewrite Title + Tags. Preserve everything else.
current_listing_meta = None
listings_updated = 0
samples_before_after = []

for row in rows:
    lid = (row.get('Listing ID') or '').strip()
    if lid:  # start of new listing block
        # Detect material/color/width/feature from this row's data
        old_title = (row.get('Title') or '').strip()
        old_tags = (row.get('Tags') or '').strip()
        old_materials = (row.get('Materials') or '').strip()
        section = (row.get('Section') or '').strip()
        var_sku = (row.get('Var SKU') or '').strip()
        v2_label = (row.get('Variation 2') or '').strip().lower()
        v2_opt = (row.get('V2 Option') or '').strip()

        # Pick whichever V is width
        width = None
        if v2_label == 'width':
            width = detect_width(v2_opt, old_title)
        else:
            # Try V1 if labeled Width
            v1_label = (row.get('Variation 1') or '').strip().lower()
            if v1_label == 'width':
                width = detect_width((row.get('V1 Option') or '').strip(), old_title)
            else:
                width = detect_width('', old_title)

        material = detect_material(f'{old_materials} {old_title} {old_tags}')
        color = detect_color(section, old_title, old_tags)
        feature = detect_feature(old_title, old_tags)

        # Build new title + tags
        new_title = build_title(material, color, width, feature, old_title, var_sku)
        new_tags_list = build_tags(material, color, width, feature, old_title, var_sku)
        new_tags = ','.join(new_tags_list)

        row['Title'] = new_title
        row['Tags'] = new_tags
        listings_updated += 1

        if len(samples_before_after) < 8:
            samples_before_after.append({
                'listing_id': lid, 'old_title': old_title[:80], 'new_title': new_title[:120],
                'old_tags': old_tags[:80], 'new_tags': new_tags[:120],
                'detected': f'mat={material} color={color} width={width} feat={feature}'
            })

# Atomic write
tmp = CSV.with_suffix('.csv.tmp')
with open(tmp, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
tmp.replace(CSV)

print(f'\nlistings updated: {listings_updated}')
print(f'total rows preserved: {len(rows)}')

# Verify structure
with open(CSV, encoding='utf-8') as f:
    rd = csv.reader(f)
    counts = Counter(len(r) for r in rd)
print(f'col counts: {dict(counts)}')

# Sample before/after
print('\n=== Before/After samples ===')
for s in samples_before_after:
    print(f"\nListing {s['listing_id']}:")
    print(f"  Detected: {s['detected']}")
    print(f"  OLD title: {s['old_title']}")
    print(f"  NEW title: {s['new_title']}")
    print(f"  OLD tags: {s['old_tags']}")
    print(f"  NEW tags: {s['new_tags']}")
