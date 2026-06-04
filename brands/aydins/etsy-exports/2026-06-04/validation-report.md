# Validation Report
**Date:** 2026-06-04

## File Integrity
| File | Status |
|---|---|
| Original CSV snapshotted | ✅ listings-export-original.csv (45,422 rows) |
| inventory-analysis.md | ✅ Structural analysis + tag dist + Shopify xref |
| classification-report.md | ✅ Per-listing bucket (no dash req'd view data — structural only) |
| delete-recommendations.csv | ✅ SKU duplicate losers flagged |
| fix-in-place-recommendations.md | ✅ Video gap, tag cannibalization, structural issues |
| new-shopify-listings.csv | ✅
| diffs/ | ✅

## Constraints
- CSV export does NOT contain views, orders, or favorites data
- Classification based on: section, tags, SKU, variant count, video presence, Shopify xref
- For view/order/favorite-based classification (DELETE/FIX threshold), need Etsy dashboard export
- All FIX-IN-PLACE assignments are provisional pending Amir's dashboard review

## Known Missing (Amir Dashboard Data — not in CSV)
- 30-day visits per listing
- 90-day orders + revenue per listing
- Favorites count per listing
- Abbandoned cart data per listing

## Tag Validation
Tag cannibalization confirmed: 'wedding ring' on 788 listings (78% of catalog)
New listings from Shopify: 42 templates generated with curated tags
Em dashes: not present in Vela CSV template output (checked programmatically)