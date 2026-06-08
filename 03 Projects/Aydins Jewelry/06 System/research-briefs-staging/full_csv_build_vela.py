#!/usr/bin/env python3
"""Build new-shopify-listings.csv in proper Vela 41-column per-variant format.
Row 1 of each listing has all metadata + Photos + first variant.
Row 2+ only have variant fields (V1 Option, V2 Option, Var SKU, Var Visibility)."""
import csv, json, re, shutil
from pathlib import Path
from collections import OrderedDict, Counter

ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04')
JSON_PATH = ROOT / 'top50-shopify-sellers.json'
AI_URLS = ROOT / 'ai-image-cdn-urls.json'
OUT = ROOT / 'new-shopify-listings.csv'
SNAP = ROOT / 'new-shopify-listings.csv.pre-vela-format-2026-06-08'

if OUT.exists() and not SNAP.exists():
    shutil.copy(OUT, SNAP)
    print(f'snapshot: {SNAP.name}')

products = json.loads(JSON_PATH.read_text())
ai_urls = json.loads(AI_URLS.read_text())
print(f'loaded {len(products)} products, {len(ai_urls)} AI URLs')

# Full 41-column Vela format matching listings-corrected.csv exactly
COLUMNS = ['Listing ID', 'Title', 'Description', 'Category', 'Who made it?',
           'What is it?', 'When was it made?', 'Renewal options', 'Product type',
           'Tags', 'Materials', 'Production partners', 'Section', 'Price',
           'Quantity', 'SKU', 'Variation 1', 'V1 Option', 'Variation 2', 'V2 Option',
           'Var Price', 'Var Quantity', 'Var SKU', 'Var Visibility', 'Var Photo',
           'Shipping profile', 'Weight', 'Length', 'Width', 'Height',
           'Return policy', 'Video 1', 'Photo 1', 'Photo 2', 'Photo 3', 'Photo 4',
           'Photo 5', 'Photo 6', 'Photo 7', 'Photo 8', 'Photo 9', 'Photo 10']

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

def fix_url(u):
    return u.replace('https:https://', 'https://').replace('http:https://', 'https://')

def extract_codename(sku):
    s = sku.strip().upper()
    while True:
        new = re.sub(r'-\d+(?:\.\d+)?$', '', s)
        if new == s: break
        s = new
    return s

def norm_width_mm(w):
    """Return width in '8mm' format."""
    s = w.lower().strip()
    m = re.match(r'^(\d+(?:\.\d+)?)\s*mm?$', s) or re.match(r'^(\d+(?:\.\d+)?)$', s)
    return f'{m.group(1)}mm' if m else w

def norm_size_label(s):
    """Etsy displays sizes as fractions ('7 1/2') in the live listing per existing data."""
    return s.strip()

def width_for_sku(w):
    """For SKU suffix: strip 'mm' and decimals (8mm -> 8, 8.5mm -> 8.5)."""
    s = w.lower().strip()
    m = re.match(r'^(\d+(?:\.\d+)?)\s*mm?$', s) or re.match(r'^(\d+(?:\.\d+)?)$', s)
    return m.group(1) if m else w

def size_for_sku(s):
    """Decimal sizes for SKU: '7 1/2' -> '7.5'."""
    s = s.strip()
    m = re.match(r'^(\d+)\s+1/2$', s)
    if m: return f'{int(m.group(1))}.5'
    m = re.match(r'^(\d+)\s+1/4$', s)
    if m: return f'{int(m.group(1))}.25'
    m = re.match(r'^(\d+)\s+3/4$', s)
    if m: return f'{int(m.group(1))}.75'
    return s

SECTION_MAP = {
    'Black': 'Black Wedding Bands', 'Silver': 'Silver Wedding Bands',
    'Gold': 'Gold Wedding Bands', 'Rose Gold': 'Rose Gold Wedding Bands',
    'Blue': 'Blue Wedding Bands', 'Green': 'Green Wedding Bands',
    'Red': 'Red Wedding Bands', 'Purple': 'Purple Wedding Bands',
    'White': 'White Wedding Bands',
}

# === Playbook tag generator (eRank-validated, from earlier work) ===
MAX_TAGS = 13
MAX_TAG_LEN = 20

def clean_tag(t):
    t = re.sub(r'[^A-Za-z0-9 ]+', '', t).strip().lower()
    return t[:MAX_TAG_LEN]

def material_of(p):
    blob = f'{p.get("primary_material","")} {p.get("title","")} {p.get("tags","")}'.lower()
    for m in ('tungsten', 'titanium', 'damascus', 'ceramic', 'aluminum', 'stainless'):
        if m in blob: return m
    return 'tungsten'

def color_of(p):
    c = (p.get('primary_color') or '').lower().strip()
    if c == 'white': return 'silver'
    if c == 'yellow gold': return 'gold'
    return c if c else None

def primary_width_of(p):
    widths = []
    for v in p.get('variants', []):
        o = (v.get('option1') or '').lower()
        m = re.match(r'^(\d+(?:\.\d+)?)\s*mm', o)
        if m: widths.append(m.group(1))
    return Counter(widths).most_common(1)[0][0] if widths else None

def has_kw(p, *kws):
    blob = f'{p.get("title","")} {p.get("tags","")}'.lower()
    return any(k in blob for k in kws)

def build_tags(p):
    h = (p.get('handle') or '').lower()
    title = (p.get('title') or '').lower()
    if 'dog-tag' in h or 'dog tag' in title:
        return [clean_tag(t) for t in [
            'fingerprint tag', 'dog tag necklace', 'mens dog tag',
            'engraved dog tag', 'personalized tag', 'stainless steel',
            'mens necklace', 'gift for him', 'fingerprint jewelry',
            'memorial dog tag', 'custom dog tag', 'mens pendant', 'engraved necklace'
        ]]
    if 'signet' in h:
        return [clean_tag(t) for t in [
            'mens signet ring', 'signet ring mens', 'engraved signet',
            'personalized ring', 'custom signet ring', 'gold signet ring',
            'mens ring', 'gift for him', 'engraved ring',
            'fingerprint ring', 'mens jewelry', 'custom ring', 'silver signet ring'
        ]]
    if 'fingerprint' in h and 'signet' not in h:
        return [clean_tag(t) for t in [
            'fingerprint ring', 'mens wedding band', 'personalized ring',
            'engraved ring', 'mens ring', 'tungsten ring',
            'mens tungsten ring', 'wedding band men', 'comfort fit ring',
            'couples ring', 'his and hers ring', 'promise ring', 'anniversary ring'
        ]]

    mat = material_of(p)
    color = color_of(p)
    width = primary_width_of(p)
    base = [
        f'{mat} ring', 'mens wedding band', 'mens wedding ring',
        f'mens {mat} ring', f'mens {mat} band', 'personalized ring',
        'engraved ring', f'{mat} band', 'mens ring', 'wedding band men',
        'comfort fit ring',
    ]
    if color:
        opts = [f'{color} {mat} ring', f'{color} {mat} band', f'{color} ring mens', f'{color} mens band']
        slot12 = next((o for o in opts if len(o) <= MAX_TAG_LEN), 'mens wedding bands')
    else:
        slot12 = 'mens wedding bands'
    base.append(slot12)
    feat = None
    if has_kw(p, 'meteorite'): feat = 'meteorite ring'
    elif has_kw(p, 'damascus') and mat != 'damascus': feat = 'damascus ring'
    elif has_kw(p, 'wood inlay', 'koa', 'olive wood', 'walnut', 'iron wood'): feat = 'wood inlay ring'
    elif has_kw(p, 'opal'): feat = 'opal ring mens'
    elif has_kw(p, 'celtic'): feat = 'celtic ring'
    elif has_kw(p, 'hammered'): feat = 'hammered ring'
    elif has_kw(p, 'spinner'): feat = 'spinner ring mens'
    elif has_kw(p, 'carbon fiber'): feat = 'carbon fiber ring'
    elif has_kw(p, 'beveled'): feat = 'beveled ring'
    elif has_kw(p, 'brushed'): feat = 'brushed ring'
    elif has_kw(p, 'diamond'): feat = 'mens diamond ring'
    if feat:
        base.append(feat)
    elif width:
        wnum = width.rstrip('0').rstrip('.') if '.' in width else width
        base.append(f'{wnum}mm wedding band')
    else:
        base.append('mens wedding ring')
    seen, out = set(), []
    for t in base:
        c = clean_tag(t)
        if c and c not in seen and len(c) <= MAX_TAG_LEN:
            seen.add(c); out.append(c)
        if len(out) >= MAX_TAGS: break
    return out

# === Playbook title generator ===
MATERIAL_TITLE = {'tungsten': 'Tungsten', 'titanium': 'Titanium', 'damascus': 'Damascus Steel',
                  'ceramic': 'Ceramic', 'aluminum': 'Aluminum', 'stainless': 'Stainless Steel'}
COLOR_TITLE = {'black': 'Black', 'silver': 'Silver', 'gold': 'Gold', 'rose gold': 'Rose Gold',
               'blue': 'Blue', 'green': 'Green', 'red': 'Red', 'purple': 'Purple',
               'white': 'White', 'yellow gold': 'Yellow Gold'}
FEATURE_LABEL = {
    'meteorite': 'Meteorite Inlay', 'damascus': 'Damascus Pattern',
    'wood inlay': 'Wood Inlay', 'koa': 'Koa Wood', 'olive wood': 'Olive Wood',
    'walnut': 'Walnut Inlay', 'iron wood': 'Ironwood', 'opal': 'Opal Inlay',
    'celtic': 'Celtic Dragon', 'hammered': 'Hammered', 'spinner': 'Spinner Ring',
    'carbon fiber': 'Carbon Fiber', 'beveled': 'Beveled', 'brushed': 'Brushed Finish',
    'diamond': 'with Diamonds', 'turquoise': 'Turquoise Inlay',
    'fingerprint': 'Fingerprint', 'antler': 'Deer Antler',
    'dinosaur bone': 'Dinosaur Bone', 'whiskey barrel': 'Whiskey Barrel', 'abalone': 'Abalone',
}

def detect_feature(p):
    blob = f'{p.get("title","")} {p.get("tags","")}'.lower()
    for k, label in FEATURE_LABEL.items():
        if k in blob: return label
    return None

def build_title(p):
    h = (p.get('handle') or '').lower()
    title = (p.get('title') or '').lower()
    if 'dog-tag' in h or 'dog tag' in title:
        return 'Personalized Fingerprint Dog Tag Necklace, Mens Engraved Stainless Steel Dog Tag Pendant, Memorial Gift'[:140]
    if 'signet' in h:
        return 'Mens Signet Ring, Personalized Engraved Signet Ring, Custom Laser Engraved Gold Silver Black Signet Ring'[:140]
    if 'fingerprint' in h and 'signet' not in h:
        return 'Fingerprint Wedding Band, His and Hers Couples Ring, Mens Tungsten Personalized Engraved Promise Anniversary Ring'[:140]
    mat = material_of(p)
    color = color_of(p)
    width = primary_width_of(p)
    feat = detect_feature(p)
    mat_t = MATERIAL_TITLE.get(mat, 'Tungsten')
    color_t = COLOR_TITLE.get(color or '', '') if color else ''
    width_t = (width.rstrip('0').rstrip('.') + 'mm') if width and '.' in width else (width + 'mm' if width else '')
    opening = 'Damascus Steel Ring for Men' if mat == 'damascus' else f'{mat_t} Wedding Band for Men'
    parts = []
    if width_t: parts.append(width_t)
    if color_t: parts.append(color_t)
    parts.append(f'Mens {mat_t} Ring' if mat != 'damascus' else 'Mens Damascus Ring')
    if feat: parts.append(feat)
    middle = ' '.join(parts)
    full = f'{opening}, {middle}, Personalized Engraved Ring, Comfort Fit'
    if len(full) > 140: full = f'{opening}, {middle}, Comfort Fit'
    if len(full) > 140 and feat:
        no_feat = ' '.join(parts[:-1])
        full = f'{opening}, {no_feat}, Comfort Fit'
    if len(full) > 140: full = full[:140].rstrip(', ')
    return full

# === Material list for Vela (comma-separated) ===
def build_materials(p):
    mat = material_of(p)
    primary = MATERIAL_TITLE.get(mat, 'Tungsten Carbide')
    if mat == 'tungsten': primary = 'Tungsten Carbide'
    secondaries = []
    blob = f'{p.get("title","")} {p.get("tags","")}'.lower()
    if 'gold' in blob and 'gold' not in primary.lower(): secondaries.append('Gold')
    if 'silver' in blob and 'silver' not in primary.lower(): secondaries.append('Silver')
    if 'wood' in blob: secondaries.append('Wood')
    if 'opal' in blob: secondaries.append('Opal')
    if 'meteorite' in blob: secondaries.append('Meteorite')
    if 'diamond' in blob: secondaries.append('Diamond')
    if 'damascus' in blob and 'damascus' not in primary.lower(): secondaries.append('Damascus Steel')
    if 'turquoise' in blob: secondaries.append('Turquoise')
    if 'abalone' in blob: secondaries.append('Abalone')
    if 'antler' in blob: secondaries.append('Deer Antler')
    return ','.join([primary] + secondaries[:2])  # primary + up to 2

# === Etsy display size formatting (e.g., '7.5' -> '7 1/2') ===
def display_size(s):
    """Convert decimal to fraction display for Etsy size dropdown."""
    s = s.strip()
    if '.5' in s:
        whole = s.split('.')[0]
        return f'{whole} 1/2'
    if '.25' in s:
        return f'{s.split(".")[0]} 1/4'
    if '.75' in s:
        return f'{s.split(".")[0]} 3/4'
    return s

# === Determine which codenames already exist on Etsy (in listings-corrected.csv) ===
# Per Amir 2026-06-08: skip Shopify products that already have Etsy listings to avoid duplicates.
existing_codenames = set()
existing_csv = ROOT / 'listings-corrected.csv'
if existing_csv.exists():
    with open(existing_csv, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            sku = (r.get('Var SKU') or '').strip()
            cn = extract_codename(sku)
            if cn: existing_codenames.add(cn)
    print(f'detected {len(existing_codenames)} existing Etsy codenames; will skip overlaps')

# === Build all rows ===
all_rows = []
skipped_overlapping = []
for p in products:
    handle = p['handle']
    variants = p.get('variants', [])
    if not variants: continue

    codename = extract_codename(variants[0].get('sku', f'LST{p["shopify_product_id"]}'))
    if codename in existing_codenames:
        skipped_overlapping.append((codename, handle, p.get('title', '')[:60]))
        continue
    title = scrub(build_title(p))
    desc = scrub(p.get('description_text_clean', '') or '')
    tags = ','.join(build_tags(p))
    materials = build_materials(p)
    color = p.get('primary_color', '') or ''
    section = SECTION_MAP.get(color, 'Tungsten Rings')
    prices = [v.get('price') for v in variants if v.get('price')]
    base_price = min(prices) if prices else 0

    # Photos: AI 1-4 + Shopify 5-10
    ai_hero = ai_urls.get(f'{handle}/hero.jpg', '')
    ai_2 = ai_urls.get(f'{handle}/image-2.jpg', '')
    ai_3 = ai_urls.get(f'{handle}/image-3.jpg', '')
    ai_4 = ai_urls.get(f'{handle}/image-4.jpg', '')
    shop_imgs = [fix_url(i['src']) for i in p.get('images', [])]
    photos = [ai_hero, ai_2, ai_3, ai_4] + shop_imgs
    photos = [x for x in photos if x][:10]
    while len(photos) < 10: photos.append('')

    # Iterate variants (size outer, width inner — matching MAUI pattern)
    # Collect distinct widths and sizes from variants
    widths_seen = []  # list of mm
    sizes_seen = []   # list of size labels (raw)
    width_size_to_variant = {}
    for v in variants:
        w_raw = (v.get('option1') or '').strip()
        s_raw = (v.get('option2') or '').strip()
        if not (w_raw and s_raw): continue
        w_mm = norm_width_mm(w_raw)
        if w_mm not in widths_seen: widths_seen.append(w_mm)
        if s_raw not in sizes_seen: sizes_seen.append(s_raw)
        width_size_to_variant[(w_mm, s_raw)] = v

    # Sort sizes numerically by size_for_sku
    def size_sort_key(s):
        try: return float(size_for_sku(s))
        except: return 999
    sizes_seen = sorted(sizes_seen, key=size_sort_key)

    # Build rows: for each size, for each width
    is_first = True
    for s_raw in sizes_seen:
        for w_mm in widths_seen:
            v = width_size_to_variant.get((w_mm, s_raw))
            if not v: continue
            var_sku = f'{codename}-{width_for_sku(w_mm)}-{size_for_sku(s_raw)}'
            var_price = v.get('price', base_price)
            var_qty = 10  # Aydins default

            row = OrderedDict({c: '' for c in COLUMNS})
            if is_first:
                # Metadata row
                row['Listing ID'] = ''
                row['Title'] = title
                row['Description'] = desc
                row['Category'] = 'Jewelry > Rings > Wedding & Engagement > Wedding Bands'
                row['Who made it?'] = 'I did'
                row['What is it?'] = 'A finished product'
                row['When was it made?'] = '2020 - 2026'
                row['Renewal options'] = 'Automatic'
                row['Product type'] = 'Physical'
                row['Tags'] = tags
                row['Materials'] = materials
                row['Production partners'] = ''
                row['Section'] = section
                row['Price'] = f'{base_price:.2f}'
                row['Quantity'] = '10'
                row['SKU'] = ''  # Vela default is to leave master SKU blank
                row['Shipping profile'] = 'All Shipping'
                row['Weight'] = '0.20'
                row['Length'] = ''
                row['Width'] = ''
                row['Height'] = ''
                row['Return policy'] = '30 days to return or exchange'
                row['Video 1'] = ''
                for i in range(10):
                    row[f'Photo {i+1}'] = photos[i]
                is_first = False

            # Variant fields (every row)
            row['Variation 1'] = 'Ring size'
            row['V1 Option'] = display_size(s_raw)  # Etsy displays fractions
            row['Variation 2'] = 'Width'
            row['V2 Option'] = w_mm
            row['Var Price'] = ''  # only fill if differs from base
            row['Var Quantity'] = ''
            row['Var SKU'] = var_sku
            row['Var Visibility'] = 'On'
            row['Var Photo'] = ''

            all_rows.append(row)

# Atomic write
tmp = OUT.with_suffix('.csv.tmp')
with open(tmp, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(all_rows)
tmp.replace(OUT)

# Verify
with open(OUT, encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
print(f'\nWrote {len(rows)-1} variant rows for {len(products) - len(skipped_overlapping)} new products')
print(f'Skipped {len(skipped_overlapping)} products that already exist on Etsy (will be updated via listings-corrected.csv):')
for cn, h, t in skipped_overlapping:
    print(f'  - {cn}: {t}')
print(f'col counts: {Counter(len(r) for r in rows)}')

# Sample first listing's first 3 rows
print('\n=== First 3 rows of first listing ===')
with open(OUT, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, r in enumerate(reader):
        if i >= 3: break
        print(f'--- Row {i+1} ---')
        for k in ('Title', 'V1 Option', 'V2 Option', 'Var SKU', 'Var Visibility', 'Price', 'Tags', 'Photo 1'):
            v = r.get(k, '')
            if v: print(f'  {k}: {v[:90]!r}')
