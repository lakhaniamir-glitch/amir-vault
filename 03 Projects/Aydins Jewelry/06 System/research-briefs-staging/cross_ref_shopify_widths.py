#!/usr/bin/env python3
"""Cross-reference Etsy variant rows in listings-corrected.csv against actual Shopify width/size offerings.
- For each Etsy listing, find matching Shopify product by codename in Var SKU.
- Keep only (width, size) variant pairs that exist on Shopify for that codename.
- Rewrite the listing block with the pruned variant set.
- If no Shopify match: leave listing as-is (don't prune unverified)."""
import csv, json, re
from pathlib import Path
from collections import OrderedDict

ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04')
SRC = ROOT / 'listings-corrected.csv'  # already has playbook applied
INDEX = Path('/tmp/shopify_codename_width_size_index.json')

idx = json.loads(INDEX.read_text())
print(f'Loaded Shopify index: {len(idx)} codenames')

def extract_codename(sku):
    s = (sku or '').strip().upper()
    while True:
        new = re.sub(r'-\d+(?:\.\d+)?$', '', s)
        if new == s: break
        s = new
    return s

def display_size(s):
    """Convert decimal -> fraction display ('7.5' -> '7 1/2')."""
    s = s.strip()
    if s.endswith('.5'): return f"{s.split('.')[0]} 1/2"
    if s.endswith('.25'): return f"{s.split('.')[0]} 1/4"
    if s.endswith('.75'): return f"{s.split('.')[0]} 3/4"
    return s

def size_for_sku(s):
    s = s.strip()
    m = re.match(r'^(\d+)\s+1/2$', s)
    if m: return f'{int(m.group(1))}.5'
    m = re.match(r'^(\d+)\s+1/4$', s)
    if m: return f'{int(m.group(1))}.25'
    m = re.match(r'^(\d+)\s+3/4$', s)
    if m: return f'{int(m.group(1))}.75'
    m = re.match(r'^(\d+(?:\.\d+)?)$', s)
    return m.group(1) if m else None

# Read CSV in listing blocks
with open(SRC, encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)
    rows = list(reader)

# Group rows by listing
listings = []  # list of (first_row_idx, [row_indices])
current = None
for i, r in enumerate(rows):
    lid = (r.get('Listing ID') or '').strip()
    if lid:
        if current is not None: listings.append(current)
        current = (i, [i])
    elif current is not None:
        current[1].append(i)
if current is not None: listings.append(current)

print(f'detected listing blocks: {len(listings)}')

# Process each listing
new_rows = []
pruned_listings = 0
unmatched_listings = 0
total_rows_dropped = 0
total_rows_kept = 0

for first_idx, block_indices in listings:
    first_row = rows[first_idx]
    var_sku = (first_row.get('Var SKU') or '').strip()
    codename = extract_codename(var_sku)
    if not codename:
        # No codename: keep all rows as-is
        for i in block_indices: new_rows.append(rows[i])
        total_rows_kept += len(block_indices)
        unmatched_listings += 1
        continue

    shopify_widths = idx.get(codename)
    if not shopify_widths:
        # No Shopify match: keep all rows as-is
        for i in block_indices: new_rows.append(rows[i])
        total_rows_kept += len(block_indices)
        unmatched_listings += 1
        continue

    # Build the valid (width, size) set for this codename
    valid_pairs = set()
    for w, sizes in shopify_widths.items():
        for s in sizes:
            if s == 'ANY': continue
            valid_pairs.add((w, s))

    # Pre-compute first-row metadata (we'll copy it to the first kept variant row)
    metadata_fields = ['Listing ID', 'Title', 'Description', 'Category', 'Who made it?',
                       'What is it?', 'When was it made?', 'Renewal options', 'Product type',
                       'Tags', 'Materials', 'Production partners', 'Section', 'Price',
                       'Quantity', 'SKU', 'Shipping profile', 'Weight', 'Length', 'Width',
                       'Height', 'Return policy', 'Video 1',
                       'Photo 1', 'Photo 2', 'Photo 3', 'Photo 4', 'Photo 5',
                       'Photo 6', 'Photo 7', 'Photo 8', 'Photo 9', 'Photo 10']
    metadata = {f: first_row.get(f, '') for f in metadata_fields}

    # Update Title to reflect actual Shopify widths. Use 8mm if available (Amir default), else smallest.
    valid_widths_list = list(shopify_widths.keys())
    title_width = '8' if '8' in valid_widths_list else (sorted(valid_widths_list, key=lambda x: float(x) if x.replace('.','').isdigit() else 99)[0] if valid_widths_list else '8')
    old_title = metadata.get('Title', '')
    # Replace the width in title: pattern is "..., {OLD_WIDTH}mm {Color} Mens ..."
    new_title = re.sub(r',\s*\d+(?:\.\d+)?mm\s+', f', {title_width}mm ', old_title, count=1)
    metadata['Title'] = new_title

    # Iterate variants in Shopify-valid order (sort by size then width for Vela compat)
    new_variant_rows = []
    valid_widths = sorted(shopify_widths.keys(), key=lambda x: float(x) if x.replace('.','').isdigit() else 99)

    is_first = True
    # Order: size outer, width inner (matches Etsy export pattern)
    all_sizes_set = set()
    for w in valid_widths:
        for s in shopify_widths[w]:
            if s != 'ANY': all_sizes_set.add(s)
    all_sizes_sorted = sorted(all_sizes_set, key=lambda x: float(x) if x.replace('.','').isdigit() else 99)

    for size_dec in all_sizes_sorted:
        for w in valid_widths:
            if size_dec not in shopify_widths[w]: continue
            # Build variant row
            row = OrderedDict({c: '' for c in fieldnames})
            if is_first:
                # Populate all metadata on first kept row
                for f, v in metadata.items(): row[f] = v
                is_first = False
            row['Variation 1'] = 'Ring size'
            row['V1 Option'] = display_size(size_dec)
            row['Variation 2'] = 'Width'
            row['V2 Option'] = f'{w}mm'
            row['Var SKU'] = f'{codename}-{w}-{size_dec}'
            row['Var Visibility'] = 'On'
            new_variant_rows.append(row)

    if not new_variant_rows:
        # Safety: if Shopify lookup produced no valid pairs, keep original
        for i in block_indices: new_rows.append(rows[i])
        total_rows_kept += len(block_indices)
        unmatched_listings += 1
        continue

    new_rows.extend(new_variant_rows)
    total_rows_kept += len(new_variant_rows)
    total_rows_dropped += len(block_indices) - len(new_variant_rows)
    pruned_listings += 1

# Atomic write
tmp = Path('/tmp/listings-corrected-pruned.csv')
with open(tmp, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(new_rows)
tmp.replace(SRC)

print(f'\npruned listings (cross-ref applied): {pruned_listings}')
print(f'unmatched listings (kept as-is): {unmatched_listings}')
print(f'rows dropped (variants not on Shopify): {total_rows_dropped}')
print(f'rows kept: {total_rows_kept}')
print(f'final row count: {len(new_rows)}')

# Verify HAYDEN
print('\n=== HAYDEN listing after pruning ===')
with open(SRC, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    in_hayden = False
    count = 0
    widths_seen = set()
    for r in reader:
        sku = r.get('Var SKU', '')
        if 'HAYDEN' in sku:
            in_hayden = True
            v1 = r.get('V1 Option', '')
            v2 = r.get('V2 Option', '')
            widths_seen.add(v2)
            count += 1
            if count <= 4:
                print(f'  V1={v1!r:8} V2={v2!r:8} Var SKU={sku!r}')
        elif in_hayden and sku:
            break
print(f'  HAYDEN total variants: {count}')
print(f'  HAYDEN widths: {sorted(widths_seen)}')
