# IG Draft Generation, Jun 3 Slots

Ran at: 2026-06-03 06:53 to 06:56 UTC

## Will the 3 posts fire?

NO. Confidence: high.

Only 1 of 3 slots is now publisher-ready.

## Target slots

| Slot | Final status | Draft path | Publisher-ready at scheduled time? | Notes |
|---|---|---|---|---|
| 2026-06-03-0800-ct | draft-failed | null | NO | Failed after 2 attempts. Final failure: caption self-check rejected close repetition and manufacturing-claim wording. |
| 2026-06-03-1300-ct | approved-queued | `/home/openclaw/.openclaw/command-center/work/phase2/drafts/2026-06-03-1300-ct-ugc.json` | YES | Draft exists, beta_check PASS, source_product present, image_public_ok true. |
| 2026-06-03-1900-ct | approved-queued | null | NO | Not retried after 0800 hit the 2-attempt failure guardrail. Publisher will skip because no draft_path exists. |

## Step 1: Pre-run state

Saved requested pre-run snapshot:

`/home/openclaw/.openclaw/agents/beta/backups/jun3-slots-prerun-2026-06-03.json`

Full calendar backup before live writes:

`/home/openclaw/.openclaw/agents/beta/backups/insta-content-calendar-pre-jun3-drafter-20260603T065340Z.json`

Gemini env check:

- `GEMINI_IMAGE_MODEL=gemini-2.5-flash-image`
- `GEMINI_FALLBACK_MODEL=gemini-2.5-flash-image`
- `GEMINI_API_KEY_PRESENT=true`

## Step 2: Dry validation

The script has no explicit dry-run flag. I did a no-API code-path trace by importing `phase2_daily_drafter.py` and simulating only the three target slots as `queued`.

Result:

- The drafter would target exactly:
  - `2026-06-03-0800-ct`
  - `2026-06-03-1300-ct`
  - `2026-06-03-1900-ct`
- Endpoint template confirmed:
  - `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key=REDACTED`
- Model confirmed:
  - `gemini-2.5-flash-image`

Important finding: the drafter only selects `status=queued`. The target slots were `approved-queued` with `draft_path=null`, so I temporarily marked only the three target slots as `queued` for the run. I restored/normalized statuses after the stopped run so the cron drafter does not keep spending.

## Step 3: Live generation

Primary live log:

`/home/openclaw/.openclaw/command-center/work/phase2/jun3-drafter-live-20260603T065340Z.log`

Retry log:

`/home/openclaw/.openclaw/command-center/work/phase2/jun3-drafter-live-retry-20260603T065554Z.log`

What happened:

1. First pass generated images for all three slots and uploaded them to Shopify Files, but draft creation failed because the drafter's caption self-check validated a temporary probe without `source_product`.
2. I backed up and patched `phase2_daily_drafter.py` narrowly so `caption_quality_failures()` receives and validates the real product anchor.
3. Retry started with the same 3-slot cap.
4. `2026-06-03-0800-ct` failed again after the second attempt, now for caption quality only:
   - close repeated recent caption language
   - manufacturing-claim wording
5. Per guardrail, I stopped instead of continuing retries.
6. During the stop, `2026-06-03-1300-ct` had already completed and produced a passing draft, so I attached that existing successful draft to the calendar. No extra API call was made for that attachment.

## API calls and quota

Gemini image calls recorded in cost ledger:

- 5 Gemini image generations
- Model: `gemini-2.5-flash-image`
- Estimated Gemini quota/cost burned: `$0.195`
- Cost file: `/home/openclaw/.openclaw/command-center/work/phase2/gemini-costs-2026-06-03.json`

Breakdown:

| Slot | Gemini calls | Estimated cost |
|---|---:|---:|
| 2026-06-03-0800-ct | 2 | $0.078 |
| 2026-06-03-1300-ct | 2 | $0.078 |
| 2026-06-03-1900-ct | 1 | $0.039 |

Shopify Files uploads were attempted for each successful generated image before caption validation. No Shopify product/theme writes were made.

## Generated local image files

| Slot | Local image | Size | Corrupt check |
|---|---|---:|---|
| 2026-06-03-0800-ct | `/home/openclaw/.openclaw/command-center/work/phase2/2026-06-03-0800-ct-ugc.png` | 1,375,820 bytes | OK |
| 2026-06-03-1300-ct | `/home/openclaw/.openclaw/command-center/work/phase2/2026-06-03-1300-ct-ugc.png` | 1,548,314 bytes | OK |
| 2026-06-03-1900-ct | `/home/openclaw/.openclaw/command-center/work/phase2/2026-06-03-1900-ct-product_showcase.png` | 1,232,789 bytes | OK |

Preview contact sheet:

`/home/openclaw/.openclaw/command-center/work/phase2/jun3-generated-preview-thumbs.png`

## Draft validation

Passing draft created:

`/home/openclaw/.openclaw/command-center/work/phase2/drafts/2026-06-03-1300-ct-ugc.json`

Validation:

- `beta_check.status=PASS`
- `caption` present, length 577
- `source_product` present
- `image_url` present
- `image_public_ok=true`
- no em dashes found in the passing caption
- no third-party brand names found in the passing caption

No passing draft paths exist for 0800 or 1900.

## Publisher-ready check

Publisher logic requires:

1. `status == approved-queued`
2. `draft_path` exists on disk
3. slot is due within the on-time or catch-up window

Current readiness for scheduled time:

- `2026-06-03-0800-ct`: NO, status is `draft-failed`, draft_path null.
- `2026-06-03-1300-ct`: YES, approved-queued and draft exists.
- `2026-06-03-1900-ct`: NO, approved-queued but draft_path null.

## Script patch made

Backed up script before patch:

`/home/openclaw/.openclaw/agents/beta/backups/phase2_daily_drafter-pre-jun3-source-product-selfcheck-20260603T065554Z.py`

Patch summary:

- `caption_quality_failures(caption, hashtags, recent)` now accepts `product=None`.
- The validation probe now includes `source_product: product or {}`.
- `generated_caption()` passes the selected product into caption validation.

This fixes the false `source_product missing` failure found in the drafter.

## Final outcome

NO, all 3 posts will not fire.

Only the 13:00 CT slot should fire. 08:00 CT failed after two attempts. 19:00 CT remains without a draft because the run was stopped per guardrail after 08:00 failed twice.
