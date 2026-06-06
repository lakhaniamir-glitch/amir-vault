# BETA Insta cleanup report — 2026-06-06

Generated: 2026-06-06T16:56:00.141580+00:00

## What was wrong

- Amir flagged the 2026-06-06 8:00 AM CT Instagram post as a phantom-ring incident: product fields were not guaranteed in the draft schema and product-reference image usage was not explicitly recorded.
- The drafter allowed failed slots to stay `draft-failed`, so the 2026-06-06 7:00 PM CT and 2026-06-07 8:00 AM CT slots had no draft file.
- The cron ran daily with a small max batch. That was not strong enough for a hard 48-hour visible-draft requirement plus backfill after failures.

## New hard rules now codified

- Added locked Beta-Insta rules to `/home/openclaw/.openclaw/command-center/agents/beta-insta.md` and `/home/openclaw/.openclaw/agents/beta-insta/AGENTS.md`.
- Every product-image draft must write `product.handle`, `product.title`, `product.url`.
- Every product-image draft must write `image_generation.used_reference_image: true`, `image_generation.input_images`, and `image_generation.source_reference_url`.
- No text-only product image generation. If product lookup fails, fallback must be quote-card/educational with no product image or NEEDS AMIR.
- Drafting now treats `draft-failed` slots as retryable and uses 48h minimum lead with 72h lookahead.

## Drafts created/repaired

- `2026-06-06-0800-ct` — metadata repaired/verified — `canoli-silver-flat-tungsten-brushed-finish-with-a-comfort-fit-bocote-wood-sleeve-inlay-ring` — reference image verified: `True`
- `2026-06-06-1300-ct` — metadata repaired/verified — `tungsten-wood-ring-red-oak-wood-inlay-polished-edges-8mm-tungsten-carbide-wedding-ring` — reference image verified: `True`
- `2026-06-06-1900-ct` — created — `yoshii-silver-tungsten-ring-blue-groove-stepped-edge` — reference image verified: `True`
- `2026-06-07-0800-ct` — created — `windrose-whiskey-barrel-wood-black-brushed-domed-orange-groove` — reference image verified: `True`
- `2026-06-07-1300-ct` — metadata repaired/verified — `aydins-tungsten-ring-black-shiny-polished-w-celtic-design-cutout-inlay-wedding-band-8mm-tungsten-carbide-wedding-ring` — reference image verified: `True`
- `2026-06-07-1900-ct` — metadata repaired/verified — `centurion-domed-tungsten-wedding-ring-for-men-with-silver-stripe-inlay-polished-finish-8mm` — reference image verified: `True`
- `2026-06-08-0800-ct` — metadata repaired/verified — `mens-wedding-band-polished-14k-yellow-gold-men-s-wedding-ring-with-purpleheart-wood-inlay-diamond-8mm` — reference image verified: `True`
- `2026-06-08-1300-ct` — created — `rutland-gunmetal-damascus-steel-ring-with-green-and-red-box-elder-inside-wood-ring` — reference image verified: `True`
- `2026-06-08-1900-ct` — metadata repaired/verified — `hervey-blue-yellow-wood-ring-purple-groove` — reference image verified: `True`

Newly created draft-only files:
- `2026-06-06-1900-ct` → `/home/openclaw/.openclaw/command-center/work/phase2/drafts/2026-06-06-1900-ct-bts.json` using `yoshii-silver-tungsten-ring-blue-groove-stepped-edge`
- `2026-06-07-0800-ct` → `/home/openclaw/.openclaw/command-center/work/phase2/drafts/2026-06-07-0800-ct-bts.json` using `windrose-whiskey-barrel-wood-black-brushed-domed-orange-groove`
- `2026-06-08-1300-ct` → `/home/openclaw/.openclaw/command-center/work/phase2/drafts/2026-06-08-1300-ct-educational.json` using `rutland-gunmetal-damascus-steel-ring-with-green-and-red-box-elder-inside-wood-ring`

## Cron schedule changes

- Snapshot saved under `/home/openclaw/.openclaw/agents/beta/backups/`.
- Updated user crontab from daily 09:00 UTC to every 6 hours:
  `0 */6 * * * PHASE2_DRAFTER_LOOKAHEAD_HOURS=72 PHASE2_DRAFTER_MAX_DRAFTS=12 ... phase2_daily_drafter.py`
- Script default max drafts increased to 12 and target picker now retries `draft-failed` slots.

## NEEDS AMIR

- Live post review/removal approval needed: 2026-06-06 8:00 AM CT post appears published at https://www.instagram.com/p/DZPs2VwgEBF/. Recommendation: Amir reviews and explicitly approves deletion/removal if the creative shows the fake/non-catalog ring. BETA did not delete or unpublish it.

## Verification

- Ran Python compile on `phase2_daily_drafter.py`: PASS.
- Audited slots 2026-06-06 08:00 through 2026-06-08 19:00 CT: all have draft files; all product-image drafts have `product.handle/title/url` and `image_generation.used_reference_image=true`.
- Ran dashboard data updater so the new draft files surface in Command Center.
