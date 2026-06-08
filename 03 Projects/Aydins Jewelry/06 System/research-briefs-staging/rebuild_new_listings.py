#!/usr/bin/env python3
"""Rebuild new-shopify-listings.csv from clean JSON source.
Fixes structural malformation, applies policy scrub, normalizes SKUs."""
import csv, json, re
from pathlib import Path
from collections import OrderedDict

JSON_PATH = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/top50-shopify-sellers.json')
OUT_PATH = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/new-shopify-listings.csv')

with open(JSON_PATH) as f:
    products = json.load(f)
print(f'Loaded {len(products)} products from JSON')

COLUMNS = ['Title', 'Description', 'Tags', 'Materials', 'Section', 'Price', 'Quantity',
           'SKU', 'Variation 1', 'V1 Option', 'Variation 2', 'V2 Option',
           'Return policy', 'Weight', 'Photo 1', 'Photo 2', 'Photo 3', 'Photo 4',
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
    protected = re.sub(r'(?i)aydins\s+lifetime\s+warranty', PROTECT, text)
    protected = re.sub(r'(?i)\blifetime\s+warranty\b', 'Aydins Lifetime Warranty', protected)
    out = protected.replace(PROTECT, 'Aydins Lifetime Warranty')
    for pat, rep in REPLACEMENTS:
        out = re.sub(pat, rep, out)
    return out

def fix_image_url(url):
    return url.replace('https:https://', 'https://').replace('http:https://', 'https://')

def filter_etsy_tags(tag_str, max_tags=13, max_len=20):
    raw = [t.strip() for t in tag_str.split(',') if t.strip()]
    cleaned, seen = [], set()
    for t in raw:
        if ':' in t: continue
        if '_' in t: continue  # skip Best_Sellers_Wave1 etc
        clean = re.sub(r'[^A-Za-z0-9 ]+', '', t).strip()
        if not clean or len(clean) > max_len: continue
        low = clean.lower()
        if low in seen: continue
        seen.add(low)
        cleaned.append(clean)
        if len(cleaned) >= max_tags: break
    return ', '.join(cleaned)

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

rows = []
img_with = 0
img_missing = 0
all_widths = set()
all_sizes = set()

for p in products:
    title = scrub(p['title'])
    desc = scrub(p.get('description_text_clean', '') or '')
    tags = filter_etsy_tags(p.get('tags', '') or '')
    materials = p.get('primary_material') or 'Tungsten Carbide'
    color = p.get('primary_color', '') or ''
    section = SECTION_MAP.get(color, 'Tungsten Rings')

    variants = p.get('variants', [])
    if not variants:
        continue
    codename = extract_codename(variants[0].get('sku', f'LST{p["shopify_product_id"]}'))

    widths, sizes, prices, inventories = [], [], [], []
    for v in variants:
        w = (v.get('option1') or '').strip()
        s = (v.get('option2') or '').strip()
        if w and w not in widths: widths.append(w)
        if s and s not in sizes: sizes.append(s)
        if v.get('price'): prices.append(v['price'])
        if v.get('inventory') is not None: inventories.append(v['inventory'])

    widths_norm = [norm_width(w) for w in widths]
    sizes_norm = [norm_size(s) for s in sizes]
    all_widths.update(widths_norm)
    all_sizes.update(sizes_norm)

    price = min(prices) if prices else 0
    qty = max(sum(inventories), 100) if inventories else 100

    v1_label = 'Width' if widths_norm else ''
    v1_options = ', '.join(widths_norm)
    v2_label = 'Ring size' if sizes_norm else ''
    v2_options = ', '.join(sizes_norm)

    images = p.get('images', [])
    photos = [fix_image_url(img['src']) for img in images[:10]]
    while len(photos) < 10:
        photos.append('')
    if photos[0]: img_with += 1
    else: img_missing += 1

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
    row['V1 Option'] = v1_options
    row['Variation 2'] = v2_label
    row['V2 Option'] = v2_options
    row['Return policy'] = 'Free exchanges within 30 days. See full policy at shopaydins.com'
    row['Weight'] = '0.4'
    for i in range(10):
        row[f'Photo {i+1}'] = photos[i]
    rows.append(row)

with open(OUT_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)

print(f'\nWrote {len(rows)} clean product rows to: {OUT_PATH}')
print(f'Photos: {img_with} with images, {img_missing} missing')
print(f'Widths found: {sorted(all_widths)}')
print(f'Sizes found (sample): {sorted(all_sizes, key=lambda x: float(x) if re.match(r"^\d", x) else 99)[:10]}')

# Verify
with open(OUT_PATH, encoding='utf-8') as f:
    check = csv.reader(f)
    cleaned_rows = list(check)
col_set = set(len(r) for r in cleaned_rows)
print(f'\nPOST verification: row col counts: {col_set}')
print(f'All rows have {len(COLUMNS)} cols: {col_set == {len(COLUMNS)}}')

text = OUT_PATH.read_text(encoding='utf-8')
em = text.count('—')
hc = len(re.findall(r'(?i)hand-?crafted|hand-?made', text))
ba = len(re.findall(r'(?i)\blifetime\s+warranty\b', text)) - len(re.findall(r'(?i)aydins\s+lifetime\s+warranty', text))
print(f'\nCompliance: em-dashes={em}  handcrafted/handmade={hc}  bare_lifetime_warranty={ba}')
