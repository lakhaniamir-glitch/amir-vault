#!/usr/bin/env python3
"""Update new-shopify-listings.csv: insert AI image URLs into Photo 1-4 slots,
shift existing Shopify product photos to Photo 5-10."""
import csv
import json
import re
from pathlib import Path

ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04')
CSV_PATH = ROOT / 'new-shopify-listings.csv'
SNAP_PATH = ROOT / 'new-shopify-listings.csv.pre-ai-urls-2026-06-08'
AI_URLS = ROOT / 'ai-image-cdn-urls.json'
JSON_PATH = ROOT / 'top50-shopify-sellers.json'

import shutil
if not SNAP_PATH.exists():
    shutil.copy(CSV_PATH, SNAP_PATH)
    print(f'snapshot: {SNAP_PATH.name}')

ai_urls = json.loads(AI_URLS.read_text())
products = json.loads(JSON_PATH.read_text())

# Build handle ↔ codename mapping from JSON
codename_to_handle = {}
for p in products:
    variants = p.get('variants', [])
    if not variants:
        continue
    sku = variants[0].get('sku', '')
    # Extract codename (strip -W-S suffix)
    s = sku.strip().upper()
    while True:
        new = re.sub(r'-\d+(?:\.\d+)?$', '', s)
        if new == s:
            break
        s = new
    codename_to_handle[s] = p['handle']

print(f'codename map: {len(codename_to_handle)} entries')

with open(SNAP_PATH, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

print(f'rows: {len(rows)}')

updated = 0
missing_handle = 0
missing_ai = 0

for row in rows:
    sku = (row.get('SKU') or '').strip().upper()
    handle = codename_to_handle.get(sku)
    if not handle:
        # Fallback: try matching by title
        title = (row.get('Title') or '').upper()
        for cn, h in codename_to_handle.items():
            if cn in title:
                handle = h
                sku = cn
                break
    if not handle:
        missing_handle += 1
        continue

    hero = ai_urls.get(f'{handle}/hero.jpg')
    img2 = ai_urls.get(f'{handle}/image-2.jpg')
    img3 = ai_urls.get(f'{handle}/image-3.jpg')
    img4 = ai_urls.get(f'{handle}/image-4.jpg')
    if not all([hero, img2, img3, img4]):
        missing_ai += 1
        continue

    # Existing Shopify product URLs are in Photo 1..N (current state)
    existing = []
    for i in range(1, 11):
        url = (row.get(f'Photo {i}') or '').strip()
        if url:
            existing.append(url)

    # Build new photo order: 4 AI + up to 6 existing Shopify product photos
    new_photos = [hero, img2, img3, img4] + existing
    new_photos = new_photos[:10]
    while len(new_photos) < 10:
        new_photos.append('')

    for i in range(10):
        row[f'Photo {i+1}'] = new_photos[i]
    updated += 1

with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)

print(f'\nupdated: {updated}/{len(rows)}')
print(f'missing_handle_match: {missing_handle}')
print(f'missing_ai_urls: {missing_ai}')

# Verify
with open(CSV_PATH, encoding='utf-8') as f:
    rd = csv.DictReader(f)
    sample = next(rd)
print('\nSample first row Photo 1-5:')
for i in range(1, 6):
    print(f'  Photo {i}: {sample.get(f"Photo {i}", "")[:90]}')
