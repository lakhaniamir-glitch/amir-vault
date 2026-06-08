#!/usr/bin/env python3
"""Single-pass build: rebuild new-shopify-listings.csv from clean JSON source,
apply playbook eRank tags, apply AI lifestyle image URLs. Atomic write."""
import csv, json, re, shutil
from pathlib import Path
from collections import OrderedDict, Counter

ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04')
JSON_PATH = ROOT / 'top50-shopify-sellers.json'
AI_URLS = ROOT / 'ai-image-cdn-urls.json'
OUT = ROOT / 'new-shopify-listings.csv'
SNAP = ROOT / f'new-shopify-listings.csv.pre-full-build-2026-06-08'

if OUT.exists() and not SNAP.exists():
    shutil.copy(OUT, SNAP)
    print(f'snapshot: {SNAP.name}')

products = json.loads(JSON_PATH.read_text())
ai_urls = json.loads(AI_URLS.read_text())
print(f'loaded {len(products)} products + {len(ai_urls)} AI URLs')

COLUMNS = ['Title', 'Description', 'Tags', 'Materials', 'Section', 'Price', 'Quantity',
           'SKU', 'Variation 1', 'V1 Option', 'Variation 2', 'V2 Option',
           'Return policy', 'Weight', 'Photo 1', 'Photo 2', 'Photo 3', 'Photo 4',
           'Photo 5', 'Photo 6', 'Photo 7', 'Photo 8', 'Photo 9', 'Photo 10']

# Policy scrub helpers
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

def norm_width(w):
    m = re.match(r'^(\d+(?:\.\d+)?)\s*mm?$', w.lower()) or re.match(r'^(\d+(?:\.\d+)?)$', w)
    return f'{m.group(1)}mm' if m else w

def norm_size(s):
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

# Playbook 13-tag stack builder
MAX_TAGS = 13
MAX_LEN = 20

def clean_tag(t):
    t = re.sub(r'[^A-Za-z0-9 ]+', '', t).strip().lower()
    return t[:MAX_LEN]

def material_of(p):
    blob = f'{p.get("primary_material","")} {p.get("title","")} {p.get("tags","")}'.lower()
    for m in ('tungsten', 'titanium', 'damascus', 'ceramic', 'aluminum', 'stainless'):
        if m in blob: return m
    return 'tungsten'

def color_of(p):
    c = (p.get('primary_color') or '').lower().strip()
    if c in ('white',): return 'silver'
    if c in ('yellow gold',): return 'gold'
    return c if c else None

def width_of(p):
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
    width = width_of(p)

    base = [
        f'{mat} ring',
        'mens wedding band',
        'mens wedding ring',
        f'mens {mat} ring',
        f'mens {mat} band',
        'personalized ring',
        'engraved ring',
        f'{mat} band',
        'mens ring',
        'wedding band men',
        'comfort fit ring',
    ]

    # Slot 12: color + material
    if color:
        opts = [f'{color} {mat} ring', f'{color} {mat} band', f'{color} ring mens', f'{color} mens band']
        slot12 = next((o for o in opts if len(o) <= MAX_LEN), 'mens wedding bands')
    else:
        slot12 = 'mens wedding bands'
    base.append(slot12)

    # Slot 13: feature or width
    feat = None
    if has_kw(p, 'meteorite'): feat = 'meteorite ring'
    elif has_kw(p, 'damascus'): feat = 'damascus ring'
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

    # Dedupe + cap + clean
    seen, out = set(), []
    for t in base:
        c = clean_tag(t)
        if c and c not in seen and len(c) <= MAX_LEN:
            seen.add(c); out.append(c)
        if len(out) >= MAX_TAGS: break
    return out


# Build all rows
rows = []
for p in products:
    title = scrub(p.get('title', '') or '')
    desc = scrub(p.get('description_text_clean', '') or '')
    tags = ', '.join(build_tags(p))
    materials = p.get('primary_material') or 'Tungsten Carbide'
    color = p.get('primary_color', '') or ''
    section = SECTION_MAP.get(color, 'Tungsten Rings')

    variants = p.get('variants', [])
    if not variants: continue
    codename = extract_codename(variants[0].get('sku', f'LST{p["shopify_product_id"]}'))

    widths, sizes, prices, invs = [], [], [], []
    for v in variants:
        w, s = (v.get('option1') or '').strip(), (v.get('option2') or '').strip()
        if w and w not in widths: widths.append(w)
        if s and s not in sizes: sizes.append(s)
        if v.get('price'): prices.append(v['price'])
        if v.get('inventory') is not None: invs.append(v['inventory'])

    widths_n = [norm_width(w) for w in widths]
    sizes_n = [norm_size(s) for s in sizes]
    price = min(prices) if prices else 0
    qty = max(sum(invs), 100) if invs else 100

    v1_label = 'Width' if widths_n else ''
    v1_opt = ', '.join(widths_n)
    v2_label = 'Ring size' if sizes_n else ''
    v2_opt = ', '.join(sizes_n)

    # Photos: AI 1-4 first, then Shopify 5+
    handle = p['handle']
    ai_hero = ai_urls.get(f'{handle}/hero.jpg', '')
    ai_2 = ai_urls.get(f'{handle}/image-2.jpg', '')
    ai_3 = ai_urls.get(f'{handle}/image-3.jpg', '')
    ai_4 = ai_urls.get(f'{handle}/image-4.jpg', '')

    shop_imgs = [fix_url(i['src']) for i in p.get('images', [])]

    photos = [ai_hero, ai_2, ai_3, ai_4] + shop_imgs
    photos = [x for x in photos if x][:10]
    while len(photos) < 10:
        photos.append('')

    row = OrderedDict()
    row['Title'] = title
    row['Description'] = desc
    row['Tags'] = tags
    row['Materials'] = materials
    row['Section'] = section
    row['Price'] = price
    row['Quantity'] = qty
    row['SKU'] = codename
    row['Variation 1'] = v1_label
    row['V1 Option'] = v1_opt
    row['Variation 2'] = v2_label
    row['V2 Option'] = v2_opt
    row['Return policy'] = 'Free exchanges within 30 days. See full policy at shopaydins.com'
    row['Weight'] = '0.4'
    for i in range(10):
        row[f'Photo {i+1}'] = photos[i]
    rows.append(row)

# Atomic write to temp then rename
tmp = OUT.with_suffix('.csv.tmp')
with open(tmp, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)
tmp.replace(OUT)

# Verify
with open(OUT, encoding='utf-8') as f:
    n_lines = sum(1 for _ in f)
with open(OUT, encoding='utf-8') as f:
    reader = csv.reader(f)
    counts = Counter(len(r) for r in reader)

print(f'\nWrote {len(rows)} rows -> {OUT.name}')
print(f'lines in file: {n_lines}')
print(f'col counts: {dict(counts)}')

# Sample preview
with open(OUT, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    samples_shown = 0
    for row in reader:
        title = row.get('Title', '')[:48]
        sku = row.get('SKU', '')
        tags = row.get('Tags', '')
        p1 = row.get('Photo 1', '')[:50]
        if any(s in title for s in ('AURION', 'NURGLE', 'FERRARI', 'RIDGES', 'GALAXY', 'DOG TAG', 'SIGNET')):
            print(f'\n{title}')
            print(f'  SKU: {sku}')
            print(f'  Tags: {tags}')
            print(f'  Photo 1: {p1}...')
            samples_shown += 1
            if samples_shown >= 4: break
