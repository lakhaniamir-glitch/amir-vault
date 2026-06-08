#!/usr/bin/env python3
"""ATOMIC rebuild of listings-corrected.csv from clean pre-sku-fix snapshot:
1. Apply SKU fix ({CODENAME}-{WIDTH}-{SIZE})
2. Apply policy scrub (em dashes, handcrafted, lifetime warranty)
3. Apply playbook treatment (title + tags) per listing
Writes to /tmp then atomic mv to avoid vault-sync conflicts."""
import csv, re, shutil
from pathlib import Path
from collections import OrderedDict, Counter

ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04')
SRC = ROOT / 'listings-corrected.csv.pre-sku-fix-2026-06-08'
OUT = ROOT / 'listings-corrected.csv'
TMP = Path('/tmp/listings-corrected-rebuild.csv')

# === Policy scrub ===
REPLACEMENTS = [
    (r'—', ','),
    (r'(?i)\bhand-?crafted\b', 'engraved'),
    (r'(?i)\bhand-?made\b', 'designed'),
    (r'(?i)\bhand[- ]?finished\b', 'finished'),
    (r'(?i)\bhand[- ]?cut\b', 'cut'),
    (r'(?i)\bforged\b', 'crafted'),
    (r'(?i)\bbuilt by hand\b', 'built'),
    (r'(?i)\bmade by hand\b', 'designed'),
]
PROTECT = '␟-ALW-␟'

def scrub(text):
    if not text: return text
    p = re.sub(r'(?i)aydins\s+lifetime\s+warranty', PROTECT, text)
    p = re.sub(r'(?i)\blifetime\s+warranty\b', 'Aydins Lifetime Warranty', p)
    out = p.replace(PROTECT, 'Aydins Lifetime Warranty')
    for pat, rep in REPLACEMENTS:
        out = re.sub(pat, rep, out)
    return out

# === SKU fix ===
def norm_width_sku(w):
    s = w.lower().strip()
    m = re.match(r'^(\d+(?:\.\d+)?)\s*mm?$', s) or re.match(r'^(\d+(?:\.\d+)?)$', s)
    return m.group(1) if m else None

def norm_size_sku(s):
    s = s.strip()
    m = re.match(r'^(\d+)\s+1/2$', s)
    if m: return f'{int(m.group(1))}.5'
    m = re.match(r'^(\d+)\s+1/4$', s)
    if m: return f'{int(m.group(1))}.25'
    m = re.match(r'^(\d+)\s+3/4$', s)
    if m: return f'{int(m.group(1))}.75'
    m = re.match(r'^(\d+(?:\.\d+)?)$', s)
    return m.group(1) if m else None

def extract_codename(raw):
    if not raw: return ''
    s = raw.strip().upper()
    while True:
        new = re.sub(r'-\d+(?:\.\d+)?$', '', s)
        if new == s: break
        s = new
    return s

# === Playbook title + tags ===
MATERIAL_TITLE = {'tungsten': 'Tungsten', 'titanium': 'Titanium', 'damascus': 'Damascus Steel',
                  'ceramic': 'Ceramic', 'aluminum': 'Aluminum', 'stainless': 'Stainless Steel', 'silver': 'Silver'}
COLOR_TITLE = {'black': 'Black', 'silver': 'Silver', 'gold': 'Gold', 'rose gold': 'Rose Gold',
               'blue': 'Blue', 'green': 'Green', 'red': 'Red', 'purple': 'Purple',
               'white': 'White', 'yellow gold': 'Yellow Gold', 'orange': 'Orange',
               'pink': 'Pink', 'gunmetal': 'Gunmetal', 'two tone': 'Two Tone', 'brown': 'Brown'}
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
    for m in ['tungsten', 'titanium', 'damascus', 'ceramic', 'aluminum', 'stainless']:
        if m in blob: return m
    return 'tungsten'

def detect_color(blob):
    blob = blob.lower()
    for c in ['rose gold', 'yellow gold', 'two tone', 'gunmetal', 'gun metal',
              'black', 'silver', 'gold', 'blue', 'green', 'red', 'purple',
              'white', 'orange', 'pink', 'brown']:
        if c in blob: return c.replace('gun metal', 'gunmetal')
    return None

def detect_width(v_opt, title):
    if v_opt:
        m = re.match(r'^(\d+(?:\.\d+)?)\s*mm?$', v_opt.lower().strip())
        if m: return m.group(1).rstrip('0').rstrip('.') if '.' in m.group(1) else m.group(1)
    m = re.search(r'(\d+(?:\.\d+)?)\s*mm', title.lower())
    if m: return m.group(1).rstrip('0').rstrip('.') if '.' in m.group(1) else m.group(1)
    return None

def detect_feature_label(blob):
    blob = blob.lower()
    for k, label in FEATURE_LABEL.items():
        if k in blob: return label
    return None

def detect_feature_kw(blob):
    blob = blob.lower()
    for k in FEATURE_LABEL.keys():
        if k in blob: return k
    return None

def is_dog_tag(title, var_sku):
    return 'dog tag' in title.lower() or 'dog-tag' in (var_sku or '').lower()

def is_signet(title, var_sku):
    return 'signet' in title.lower()

def is_fingerprint(title):
    return 'fingerprint' in title.lower()

def build_title(material, color, width, feature_label, old_title, var_sku):
    if is_dog_tag(old_title, var_sku):
        return 'Personalized Fingerprint Dog Tag Necklace, Mens Engraved Stainless Steel Dog Tag Pendant, Memorial Gift'[:140]
    if is_signet(old_title, var_sku):
        return 'Mens Signet Ring, Personalized Engraved Signet Ring, Custom Laser Engraved Gold Silver Black Signet Ring'[:140]
    if is_fingerprint(old_title) and 'wedding' not in old_title.lower()[:30]:
        return 'Fingerprint Wedding Band, His and Hers Couples Ring, Mens Tungsten Personalized Engraved Promise Anniversary Ring'[:140]
    mat_t = MATERIAL_TITLE.get(material, 'Tungsten')
    color_t = COLOR_TITLE.get(color or '', '') if color else ''
    width_t = f'{width}mm' if width else ''
    opening = 'Damascus Steel Ring for Men' if material == 'damascus' else f'{mat_t} Wedding Band for Men'
    parts = []
    if width_t: parts.append(width_t)
    if color_t: parts.append(color_t)
    parts.append(f'Mens {mat_t} Ring' if material != 'damascus' else 'Mens Damascus Ring')
    if feature_label: parts.append(feature_label)
    middle = ' '.join(parts)
    full = f'{opening}, {middle}, Personalized Engraved Ring, Comfort Fit'
    if len(full) > 140: full = f'{opening}, {middle}, Comfort Fit'
    if len(full) > 140 and feature_label:
        no_feat = ' '.join(parts[:-1])
        full = f'{opening}, {no_feat}, Comfort Fit'
    if len(full) > 140: full = full[:140].rstrip(', ')
    return full

def clean_tag(t):
    t = re.sub(r'[^A-Za-z0-9 ]+', '', t).strip().lower()
    return t[:20]

def build_tags(material, color, width, feature_kw, old_title, var_sku):
    if is_dog_tag(old_title, var_sku):
        return [clean_tag(t) for t in ['fingerprint tag', 'dog tag necklace', 'mens dog tag', 'engraved dog tag',
                'personalized tag', 'stainless steel', 'mens necklace', 'gift for him', 'fingerprint jewelry',
                'memorial dog tag', 'custom dog tag', 'mens pendant', 'engraved necklace']]
    if is_signet(old_title, var_sku):
        return [clean_tag(t) for t in ['mens signet ring', 'signet ring mens', 'engraved signet',
                'personalized ring', 'custom signet ring', 'gold signet ring', 'mens ring', 'gift for him',
                'engraved ring', 'fingerprint ring', 'mens jewelry', 'custom ring', 'silver signet ring']]
    if is_fingerprint(old_title) and 'wedding' not in old_title.lower()[:30]:
        return [clean_tag(t) for t in ['fingerprint ring', 'mens wedding band', 'personalized ring',
                'engraved ring', 'mens ring', 'tungsten ring', 'mens tungsten ring', 'wedding band men',
                'comfort fit ring', 'couples ring', 'his and hers ring', 'promise ring', 'anniversary ring']]
    base = [f'{material} ring', 'mens wedding band', 'mens wedding ring',
            f'mens {material} ring', f'mens {material} band', 'personalized ring',
            'engraved ring', f'{material} band', 'mens ring', 'wedding band men',
            'comfort fit ring']
    if color:
        opts = [f'{color} {material} ring', f'{color} {material} band', f'{color} ring mens', f'{color} mens band']
        slot12 = next((o for o in opts if len(o) <= 20), 'mens wedding bands')
    else:
        slot12 = 'mens wedding bands'
    base.append(slot12)
    feat_tag = None
    fkw = (feature_kw or '').lower()
    if 'meteorite' in fkw: feat_tag = 'meteorite ring'
    elif 'damascus' in fkw and material != 'damascus': feat_tag = 'damascus ring'
    elif any(w in fkw for w in ['wood', 'koa', 'olive', 'walnut', 'iron wood']): feat_tag = 'wood inlay ring'
    elif 'opal' in fkw: feat_tag = 'opal ring mens'
    elif 'celtic' in fkw: feat_tag = 'celtic ring'
    elif 'hammered' in fkw: feat_tag = 'hammered ring'
    elif 'spinner' in fkw: feat_tag = 'spinner ring mens'
    elif 'carbon fiber' in fkw: feat_tag = 'carbon fiber ring'
    elif 'beveled' in fkw: feat_tag = 'beveled ring'
    elif 'brushed' in fkw: feat_tag = 'brushed ring'
    elif 'diamond' in fkw: feat_tag = 'mens diamond ring'
    if feat_tag: base.append(feat_tag)
    elif width: base.append(f'{width}mm wedding band')
    else: base.append('mens wedding ring')
    seen, out = set(), []
    for t in base:
        c = clean_tag(t)
        if c and c not in seen and len(c) <= 20:
            seen.add(c); out.append(c)
        if len(out) >= 13: break
    return out

# === Process ===
with open(SRC, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

print(f'Source rows: {len(rows)} (from {SRC.name})')

# Track listing context
current_meta = None  # dict with material, color, width, feature for current listing
current_codename = ''
current_v1_label = ''
current_v2_label = ''

listings_updated = 0
sku_rewrites = 0

for row in rows:
    lid = (row.get('Listing ID') or '').strip()
    if lid:
        # New listing block: detect metadata
        old_title = (row.get('Title') or '').strip()
        old_tags = (row.get('Tags') or '').strip()
        old_materials = (row.get('Materials') or '').strip()
        section = (row.get('Section') or '').strip()
        old_desc = (row.get('Description') or '').strip()
        var_sku = (row.get('Var SKU') or '').strip()
        master_sku = (row.get('SKU') or '').strip()
        current_codename = extract_codename(var_sku) or extract_codename(master_sku) or f'LST{lid}'
        current_v1_label = (row.get('Variation 1') or '').strip()
        current_v2_label = (row.get('Variation 2') or '').strip()

        # detect from this row
        v1_opt = (row.get('V1 Option') or '').strip()
        v2_opt = (row.get('V2 Option') or '').strip()
        width = None
        if current_v2_label.lower() == 'width':
            width = detect_width(v2_opt, old_title)
        elif current_v1_label.lower() == 'width':
            width = detect_width(v1_opt, old_title)
        else:
            width = detect_width('', old_title)

        blob = f'{old_materials} {old_title} {old_tags} {section}'
        material = detect_material(blob)
        color = detect_color(blob)
        feature_label = detect_feature_label(f'{old_title} {old_tags}')
        feature_kw = detect_feature_kw(f'{old_title} {old_tags}')

        # Apply playbook
        row['Title'] = build_title(material, color, width, feature_label, old_title, var_sku)
        row['Tags'] = ','.join(build_tags(material, color, width, feature_kw, old_title, var_sku))
        # Scrub description (preserve existing prose)
        row['Description'] = scrub(old_desc)
        listings_updated += 1

    # Apply SKU fix to every row (variant rows too)
    v1_label = (row.get('Variation 1') or current_v1_label).strip().lower()
    v2_label = (row.get('Variation 2') or current_v2_label).strip().lower()
    v1 = (row.get('V1 Option') or '').strip()
    v2 = (row.get('V2 Option') or '').strip()
    width_v, size_v, extra = None, None, None
    if v1_label == 'width':
        width_v = norm_width_sku(v1)
    elif v1_label in ('ring size', 'size'):
        size_v = norm_size_sku(v1)
    elif v1:
        extra = re.sub(r'[^A-Za-z0-9]+', '', v1).upper()[:12]
    if v2_label == 'width':
        width_v = norm_width_sku(v2) or width_v
    elif v2_label in ('ring size', 'size'):
        size_v = norm_size_sku(v2) or size_v
    elif v2 and extra is None:
        extra = re.sub(r'[^A-Za-z0-9]+', '', v2).upper()[:12]

    parts = [current_codename] if current_codename else []
    if width_v is not None: parts.append(width_v)
    if size_v is not None: parts.append(size_v)
    if extra: parts.append(extra)
    if parts:
        new_var_sku = '-'.join(parts)
        if new_var_sku != (row.get('Var SKU') or ''):
            row['Var SKU'] = new_var_sku
            sku_rewrites += 1

# Atomic write to /tmp then mv
with open(TMP, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
TMP.replace(OUT)

print(f'\nlistings updated (Title+Tags+Description scrub): {listings_updated}')
print(f'Var SKU rewrites: {sku_rewrites}')
print(f'total rows preserved: {len(rows)}')

# Verify
with open(OUT, encoding='utf-8') as f:
    reader = csv.reader(f)
    col_counts = Counter(len(r) for r in reader)
print(f'col counts: {dict(col_counts)}')

# Quick compliance check
text = OUT.read_text(encoding='utf-8')
print(f'em-dashes: {text.count(chr(0x2014))}')
print(f'handcrafted/handmade: {len(re.findall(chr(40)+chr(63)+chr(105)+chr(41)+chr(92)+chr(98)+"hand-?(crafted|made|finished|cut)"+chr(92)+chr(98), text))}')
