#!/usr/bin/env python3
"""Final dedup pass on both Vela CSVs: ensure unique titles within each file.
For any title that appears 2+ times, append the codename (in parens) to the 2nd+ occurrences."""
import csv, re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04')
FILES = [ROOT / 'listings-corrected.csv', ROOT / 'new-shopify-listings.csv']

def extract_codename(sku):
    s = (sku or '').strip().upper()
    while True:
        new = re.sub(r'-\d+(?:\.\d+)?$', '', s)
        if new == s: break
        s = new
    return s


def is_first_row(row, has_listing_id):
    """First row of a listing block has either Listing ID (UPDATE file) or Title populated (CREATE file)."""
    if has_listing_id:
        return bool((row.get('Listing ID') or '').strip())
    return bool((row.get('Title') or '').strip())


for csv_path in FILES:
    if not csv_path.exists():
        print(f'SKIP missing: {csv_path.name}')
        continue
    with open(csv_path, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    # Determine first-row detection mode:
    # - UPDATE file: Listing ID populated on first row of each listing block
    # - CREATE file: Listing ID always blank; Title populated on first row of each listing block
    sample_lid_populated = any((r.get('Listing ID') or '').strip() for r in rows[:200])
    has_listing_id = 'Listing ID' in fieldnames and sample_lid_populated

    # First pass: collect titles per listing
    title_to_first_indices = defaultdict(list)
    for i, r in enumerate(rows):
        if is_first_row(r, has_listing_id):
            t = (r.get('Title') or '').strip()
            if t: title_to_first_indices[t].append(i)

    # For any title with 2+ occurrences, append codename to all but the first
    dedup_count = 0
    for title, indices in title_to_first_indices.items():
        if len(indices) <= 1: continue
        for idx in indices[1:]:  # keep first as-is
            cn = extract_codename(rows[idx].get('Var SKU') or '')
            if not cn: continue
            # Truncate codename if too long
            cn_clean = re.sub(r'[^A-Za-z0-9]+', '', cn).upper()[:10]
            # Append before the last ', Personalized Engraved Ring, Comfort Fit' part
            new_title = title
            for tail in [', Personalized Engraved Ring, Comfort Fit', ', Comfort Fit']:
                if new_title.endswith(tail):
                    head = new_title[:-len(tail)]
                    new_title = f'{head} {cn_clean}{tail}'
                    break
            else:
                new_title = f'{title} {cn_clean}'
            # Enforce 140 char cap
            if len(new_title) > 140:
                new_title = new_title[:140].rstrip(', ')
            rows[idx]['Title'] = new_title
            dedup_count += 1

    # Atomic write
    tmp = csv_path.with_suffix('.csv.tmp')
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(csv_path)

    # Verify final state
    with open(csv_path, encoding='utf-8') as f:
        rd = csv.DictReader(f)
        new_titles = []
        for r in rd:
            if is_first_row(r, has_listing_id):
                t = (r.get('Title') or '').strip()
                if t: new_titles.append(t)
    dups_left = [(t, c) for t, c in Counter(new_titles).items() if c > 1]
    print(f'\n{csv_path.name}:')
    print(f'  listings: {len(new_titles)}, unique titles: {len(set(new_titles))}, dedup ops: {dedup_count}')
    print(f'  remaining duplicate titles: {len(dups_left)}')
    if dups_left:
        for t, c in dups_left[:3]:
            print(f'    {c}x: {t}')
