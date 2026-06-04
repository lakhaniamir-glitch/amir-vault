# Compliance Issues — New Shopify Listing Templates

**Date:** 2026-06-04
**Severity:** All flagged issues are in `new-shopify-listings.csv` (templates from Shopify scraped descriptions)

## Banned Phrases Found (must be rewritten before Vela import)

### "handcrafted" / "handmade" — 13 occurrences
Shopify descriptions use these. Aydins policy explicitly bans them:
> "Does NOT manufacture, hand-craft, 'build,' 'cut,' 'make by hand,' or 'forge' rings"

**Fix:** Replace with "engraved in Irving, Texas" / "finished at our workshop" / "built with"

### "hand-finished" — 4 occurrences
Same ban as above.

### Bare "lifetime warranty" — 18 occurrences
Must use "Aydins Lifetime Warranty" — NOT bare "lifetime warranty" per policy file.

## Other Issues in Scraped Shopify Descriptions

- **Em dashes (\u2014)** — Found in some HTML-sourced descriptions. Need to replace with plain dashes or commas.
- **"Bought with..." schema** — FAQ schema mixed into descriptions. Strip for Etsy.
- **Unlinked "shopaydins.com/policies"** — Etsy doesn't allow external link in descriptions.
- **"hand-finished in our Irving, Texas shop"** — Should be "engraved and shipped from Irving, Texas" per policy.

## Action Required

For each of the 42 new listing templates in `new-shopify-listings.csv`:

1. **Title** (140 char max): Check for Etsy SEO — should front-load keyword like "Mens Wedding Band | [codename] [feature]"
2. **Description**: Rewrite in VESUVIUS format (lean, feature-focused). Strip all warranty/return/shipping FAQ. Strip FAQ schema.
3. **Tags**: Currently copied from Shopify. Need Etsy-friendly 13 max / 20 char each.
4. **Photos**: Shopify CDN URLs verified working.
5. **Variants**: Width + size mapped correctly.

## Quick-Fix Python Check (run after rewriting)

```python
import re
issues = []
for phrase in ['handcrafted','hand-made','handmade','hand finished','hand-finished',
               'forged','built one','we make every','made by hand']:
    if phrase in description.lower():
        issues.append(phrase)
if 'lifetime warranty' in description.lower() and 'aydins lifetime warranty' not in description.lower():
    issues.append('bare lifetime warranty')
```