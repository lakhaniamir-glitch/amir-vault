#!/usr/bin/env python3
"""Rebuild the Tags column in new-shopify-listings.csv using the Etsy Champion Playbook
13-tag stack, based on eRank keyword research (not generic Shopify tags)."""
import csv, json, re
from pathlib import Path

CSV_PATH = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/new-shopify-listings.csv')
SNAP = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/new-shopify-listings.csv.pre-playbook-tags-2026-06-08')
JSON_PATH = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/top50-shopify-sellers.json')

import shutil
if not SNAP.exists():
    shutil.copy(CSV_PATH, SNAP)
    print(f'snapshot: {SNAP.name}')

products = json.loads(JSON_PATH.read_text())
prod_by_handle = {p['handle']: p for p in products}

# Etsy hard limits
MAX_TAGS = 13
MAX_LEN = 20

def clean_tag(t):
    """Strip special chars, lowercase, truncate to 20 chars."""
    t = re.sub(r'[^A-Za-z0-9 ]+', '', t).strip().lower()
    return t[:MAX_LEN]

def material_from_product(p):
    """Detect primary material from tags/material/title."""
    mat = (p.get('primary_material') or '').lower()
    title = (p.get('title') or '').lower()
    tags = (p.get('tags') or '').lower()
    blob = f'{mat} {title} {tags}'
    if 'tungsten' in blob: return 'tungsten'
    if 'titanium' in blob: return 'titanium'
    if 'damascus' in blob: return 'damascus'
    if 'ceramic' in blob: return 'ceramic'
    if 'aluminum' in blob: return 'aluminum'
    if 'silver' in mat: return 'silver'  # for stainless variants
    if 'stainless' in blob: return 'stainless'
    return 'tungsten'  # default fallback (most Aydins is tungsten)

def color_from_product(p):
    color = (p.get('primary_color') or '').lower().strip()
    # Normalize for tag use
    if color in ('black',): return 'black'
    if color in ('silver', 'white'): return 'silver'
    if color in ('gold', 'yellow gold'): return 'gold'
    if color in ('rose gold',): return 'rose gold'
    if color in ('blue',): return 'blue'
    if color in ('green',): return 'green'
    if color in ('red',): return 'red'
    if color in ('purple',): return 'purple'
    return None

def primary_width_from_product(p):
    """Pick the most common width (mm) from variants."""
    widths = []
    for v in p.get('variants', []):
        o1 = (v.get('option1') or '').lower()
        m = re.match(r'^(\d+(?:\.\d+)?)\s*mm', o1)
        if m: widths.append(m.group(1))
    if not widths: return None
    from collections import Counter
    most_common = Counter(widths).most_common(1)
    return most_common[0][0] if most_common else None

def has_feature(p, *keywords):
    blob = f'{p.get("title","")} {p.get("tags","")}'.lower()
    return any(k in blob for k in keywords)

def is_dog_tag(p):
    return 'dog tag' in (p.get('title') or '').lower() or 'dog-tag' in (p.get('handle') or '')

def is_signet(p):
    h = (p.get('handle') or '').lower()
    return 'signet' in h or ('engraved' in (p.get('title') or '').lower() and 'wedding' not in (p.get('title') or '').lower())

def is_fingerprint(p):
    return 'fingerprint' in (p.get('handle') or '').lower()


def build_tags_for_product(p):
    """Build the playbook 13-tag stack for a product.

    Base structure (for tungsten wedding bands):
    1.  {material} ring         (e.g., tungsten ring)
    2.  mens wedding band
    3.  mens wedding ring
    4.  mens {material} ring
    5.  mens {material} band
    6.  personalized ring        (4,630 searches)
    7.  engraved ring            (7,461 searches - underused)
    8.  {material} band
    9.  mens ring                (35,075 searches)
    10. wedding band men
    11. comfort fit ring         (Aydins differentiator)
    12. {color} {material} ring  swap by color
    13. {width}mm wedding band   swap by width OR feature

    Customizations for special products (dog tag, signet, fingerprint).
    """
    mat = material_from_product(p)  # tungsten / titanium / damascus / etc
    color = color_from_product(p)
    width = primary_width_from_product(p)

    # Special-case: dog tag (not a ring at all)
    if is_dog_tag(p):
        tags = [
            'fingerprint tag', 'dog tag necklace', 'mens dog tag',
            'engraved dog tag', 'personalized tag', 'stainless steel tag',
            'mens necklace', 'gift for him', 'fingerprint jewelry',
            'memorial dog tag', 'custom dog tag', 'mens pendant', 'engraved necklace'
        ]
        return [clean_tag(t) for t in tags][:MAX_TAGS]

    # Special-case: signet ring
    if is_signet(p):
        tags = [
            'mens signet ring', 'signet ring mens', 'engraved signet',
            'personalized ring', 'custom signet ring', 'laser engraved ring',
            'mens ring', 'gift for him', 'engraved ring',
            'fingerprint ring', 'mens jewelry', 'custom ring', 'mens band'
        ]
        return [clean_tag(t) for t in tags][:MAX_TAGS]

    # Special-case: fingerprint couples ring
    if is_fingerprint(p):
        tags = [
            'fingerprint ring', 'mens wedding band', 'personalized ring',
            'engraved ring', 'mens ring', 'tungsten ring',
            'mens tungsten ring', 'wedding band men', 'comfort fit ring',
            'couples ring', 'his and hers ring', 'promise ring', 'anniversary ring'
        ]
        return [clean_tag(t) for t in tags][:MAX_TAGS]

    # Standard wedding band stack
    base = [
        f'{mat} ring',          # 1
        'mens wedding band',    # 2
        'mens wedding ring',    # 3
        f'mens {mat} ring',     # 4
        f'mens {mat} band',     # 5
        'personalized ring',    # 6
        'engraved ring',        # 7 - BIG UNDERUSED OPPORTUNITY
        f'{mat} band',          # 8
        'mens ring',            # 9
        'wedding band men',     # 10
        'comfort fit ring',     # 11
    ]

    # Slot 12: {color} {material} ring (swap by color)
    if color:
        slot12 = f'{color} {mat} ring'
        # If too long, fallback to shorter forms
        if len(slot12) > MAX_LEN:
            slot12 = f'{color} {mat} band'
        if len(slot12) > MAX_LEN:
            slot12 = f'{color} mens ring'
        if len(slot12) > MAX_LEN:
            slot12 = f'{color} ring mens'
        if len(slot12) > MAX_LEN:
            slot12 = f'{color} mens band'
        base.append(slot12)
    else:
        base.append('mens wedding bands')

    # Slot 13: {width}mm wedding band OR feature tag
    feature_tag = None
    if has_feature(p, 'meteorite'): feature_tag = 'meteorite ring'
    elif has_feature(p, 'damascus'): feature_tag = 'damascus ring'
    elif has_feature(p, 'wood inlay', 'koa', 'olive wood', 'walnut'): feature_tag = 'wood inlay ring'
    elif has_feature(p, 'opal'): feature_tag = 'opal ring mens'
    elif has_feature(p, 'celtic'): feature_tag = 'celtic ring'
    elif has_feature(p, 'hammered'): feature_tag = 'hammered ring'
    elif has_feature(p, 'brushed'): feature_tag = 'brushed ring'
    elif has_feature(p, 'beveled'): feature_tag = 'beveled ring'
    elif has_feature(p, 'spinner'): feature_tag = 'spinner ring mens'
    elif has_feature(p, 'carbon fiber'): feature_tag = 'carbon fiber ring'

    if feature_tag:
        base.append(feature_tag)
    elif width:
        # Strip decimal for width tag (8.0mm -> 8mm)
        wnum = width.rstrip('0').rstrip('.') if '.' in width else width
        base.append(f'{wnum}mm wedding band')
    else:
        base.append('mens wedding ring')

    # Clean + dedupe + cap
    seen = set()
    out = []
    for t in base:
        c = clean_tag(t)
        if c and c not in seen and len(c) <= MAX_LEN:
            seen.add(c)
            out.append(c)
        if len(out) >= MAX_TAGS:
            break
    # Pad if needed (shouldn't happen)
    return out


# Apply to CSV
with open(SNAP, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Map: Title -> handle (use SKU codename as bridge)
codename_to_handle = {}
for p in products:
    variants = p.get('variants', [])
    if variants:
        sku = variants[0].get('sku', '').strip().upper()
        s = sku
        while True:
            new = re.sub(r'-\d+(?:\.\d+)?$', '', s)
            if new == s: break
            s = new
        codename_to_handle[s] = p['handle']

updated = 0
for row in rows:
    sku = (row.get('SKU') or '').strip().upper()
    handle = codename_to_handle.get(sku)
    if not handle:
        continue
    p = prod_by_handle.get(handle)
    if not p:
        continue
    tags = build_tags_for_product(p)
    row['Tags'] = ', '.join(tags)
    updated += 1

with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)

print(f'updated tags on {updated}/{len(rows)} rows')

# Sample preview
print('\n=== Sample tag stacks ===')
samples = ['JDTR1166', 'JDTR1146', 'JDTR1115']  # Aurion, Nurgle, etc
with open(CSV_PATH, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sku = row.get('SKU', '')
        title = row.get('Title', '')[:40]
        tags = row.get('Tags', '')
        if any(sku.startswith(s) for s in samples) or len([1]) < 6:
            print(f'\n{title}')
            print(f'  SKU: {sku}')
            print(f'  Tags ({tags.count(",")+1}): {tags}')
        if title.startswith(('AURION', 'NURGLE', 'FERRARI', 'RIDGES', 'GALAXY')):
            pass
