# Merchant Center deletion log - 2026-06-02

Status: SUCCESS
Merchant Center ID: 122065428
Started: 2026-06-02T21:42:21.796Z
Completed: 2026-06-02T21:43:55.212Z

## Summary

- Approved Shopify handles: 14
- Pending MC product rows from 2026-05-28 audit queue: 126
- Shopify pre-check: all 14 still matched approved status.
- Current MC pre-check with products.get: 0 live rows found.
- MC rows already absent before deletion attempt: 126
- MC deletions executed: 0
- Post-check survivors: 0
- Failed removals: 0

Because no target MC product IDs were live at pre-check, no destructive delete calls were needed. This is a no-op success: the pending items are absent from Merchant Center now.

## Shopify status verification

| Handle | Expected | Current | Published |
|---|---:|---:|---:|
| ardent-black-tungsten-ring-diamond-stimulate-white-cz-hammered | DRAFT | DRAFT | none |
| alnair-rose-gold-tungsten-ring-blue-pipe-cut | DRAFT | DRAFT | none |
| supersonic-two-tone-brushed-yellow-gold-black-groove-tungsten-ring-8mm-wide | DRAFT | DRAFT | none |
| bluewave-blue-tungsten-ring-black-brushed-blue-grooved-center | DRAFT | DRAFT | none |
| lunara-silver-tungsten-ring-sleepy-lavender-opal-inlay-beveled | DRAFT | DRAFT | none |
| shavogold-yellow-gold-tungsten-black-resin-gold-shavings-inlay | DRAFT | DRAFT | none |
| bayamon-orange-aluminum-ring-orange-groove | DRAFT | DRAFT | none |
| corkshine-yellow-gold-tungsten-domed-ring-gold-glitter-inlay | DRAFT | DRAFT | none |
| gritedge-black-tungsten-ring-gun-metal-with-domed-brushed-off-center-groove | DRAFT | DRAFT | none |
| rolfe-black-tungsten-ring-blue-beveled-edge | DRAFT | DRAFT | none |
| mens-wedding-band-polished-flat-14k-rose-gold-wedding-ring-with-bubinga-wood-inlay-8mm | ARCHIVED | ARCHIVED | none |
| noirzicon-rose-gold-tungsten-ring-domed-ring-black-cz-ring | ARCHIVED | ARCHIVED | none |
| leonis-two-tone-black-tungsten-ring-with-brushed-rose-gold-dome-4mm-6mm-8mm | ARCHIVED | ARCHIVED | none |
| mens-wedding-band-14k-rose-gold-with-black-carbon-fiber-inlay-flat-polished-design | ARCHIVED | ARCHIVED | none |

## Merchant Center verification by handle

| Handle | Pending MC rows checked | Live at pre-check | Already absent | Deleted now | Post-check survivors |
|---|---:|---:|---:|---:|---:|
| ardent-black-tungsten-ring-diamond-stimulate-white-cz-hammered | 8 | 0 | 8 | 0 | 0 |
| alnair-rose-gold-tungsten-ring-blue-pipe-cut | 10 | 0 | 10 | 0 | 0 |
| supersonic-two-tone-brushed-yellow-gold-black-groove-tungsten-ring-8mm-wide | 3 | 0 | 3 | 0 | 0 |
| bluewave-blue-tungsten-ring-black-brushed-blue-grooved-center | 6 | 0 | 6 | 0 | 0 |
| lunara-silver-tungsten-ring-sleepy-lavender-opal-inlay-beveled | 4 | 0 | 4 | 0 | 0 |
| shavogold-yellow-gold-tungsten-black-resin-gold-shavings-inlay | 4 | 0 | 4 | 0 | 0 |
| bayamon-orange-aluminum-ring-orange-groove | 12 | 0 | 12 | 0 | 0 |
| corkshine-yellow-gold-tungsten-domed-ring-gold-glitter-inlay | 3 | 0 | 3 | 0 | 0 |
| gritedge-black-tungsten-ring-gun-metal-with-domed-brushed-off-center-groove | 7 | 0 | 7 | 0 | 0 |
| rolfe-black-tungsten-ring-blue-beveled-edge | 11 | 0 | 11 | 0 | 0 |
| mens-wedding-band-polished-flat-14k-rose-gold-wedding-ring-with-bubinga-wood-inlay-8mm | 17 | 0 | 17 | 0 | 0 |
| noirzicon-rose-gold-tungsten-ring-domed-ring-black-cz-ring | 4 | 0 | 4 | 0 | 0 |
| leonis-two-tone-black-tungsten-ring-with-brushed-rose-gold-dome-4mm-6mm-8mm | 21 | 0 | 21 | 0 | 0 |
| mens-wedding-band-14k-rose-gold-with-black-carbon-fiber-inlay-flat-polished-design | 16 | 0 | 16 | 0 | 0 |

## Raw run file

`/home/openclaw/.openclaw/command-center/work/mc-deletion-run-2026-06-02.json`
