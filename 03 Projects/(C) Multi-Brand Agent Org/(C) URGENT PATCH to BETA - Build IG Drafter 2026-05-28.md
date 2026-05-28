---
to: BETA
from: Amir
date: 2026-05-28
priority: URGENT
type: missing Phase 2 IG drafter cron - build now
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Build_IG_Drafter_2026-05-28.md
---

# URGENT: Build the missing Phase 2 IG drafter

## Problem

Phase 2 IG publisher cron is running fine but had nothing to publish overnight because the **pre-dawn drafter cron was never installed**. This was flagged as open follow-up #3 in the 2026-05-27 STATE_HANDOFF but didn't get acted on.

Current state:
- Today 2026-05-28 08:00 CT: empty slot (PASSED, skip)
- Today 2026-05-28 13:00 CT: ABYSS approved-queued (will fire OK at 1 PM)
- Today 2026-05-28 19:00 CT: empty slot (need draft NOW)
- 2026-05-29 onwards: 42 empty slots

## Build the drafter

### Script: `/home/openclaw/.openclaw/command-center/scripts/phase2_daily_drafter.py`

Logic:

1. Source `/home/openclaw/.openclaw/agents/beta/credentials/gemini.env` for GEMINI_API_KEY ($5/day cap).
2. Source Shopify Admin API token (existing config) for Files upload.
3. Read `brands/aydins/insta-content-calendar.json`.
4. Identify slots in the next 72 hours where `status == "queued"` and `draft_path == null`.
5. For each such slot, generate a draft:
   - **Category = product_showcase:** Pick a zero-traffic-eligible Aydins ring (read from `brands/aydins/zero-traffic-skus.json` if exists, else pick a random active product). Pull product image URL from Shopify. Use Gemini `gemini-2.5-flash-image` IMAGE-EDIT mode with prompt: "Use the provided product photo as the exact ring reference. Place this ring in a [scene varies by mood], editorial macro style, 4:5 portrait. Preserve ring material, color, and feature details." Scene options: dark leather, dark wood, dark stone, brass-accented surface, white marble close-up, warm linen, hand on dark background. Preserve product accuracy.
   - **Category = bts (behind-the-scenes):** Text-to-image mode. Prompt themes: engraving station close-up, ring on workshop bench with tools, raw tungsten blank before finishing, laser engraving in progress, polishing wheel detail. Style: editorial macro, warm lighting, dark workshop atmosphere, 4:5 portrait.
   - **Category = educational:** Text-to-image. Topics rotate through: ring width comparison, comfort fit interior, engraving location (inside vs outside), inlay materials, tungsten vs titanium, ring size measurement, daily wear care. Visual: clean editorial still life relevant to topic, 4:5 portrait.
   - **Category = ugc:** Draft a "this customer wore IMPRINT to..." style post. For now (no real UGC), use text-to-image with stock-photography-style "ring on hand in lifestyle setting" prompt. Editorial, 4:5 portrait.
6. Upload generated PNG to Shopify Files via `fileCreate` mutation. Filename pattern: `beta-insta-{slot_id}-{ts}.png`. Tag in filename: `beta-insta-generated`.
7. Write caption: hook (1 line) + body (2-4 short paragraphs) + soft CTA. Pull voice from `brands/aydins/profile.md`. NO em dashes. NO bare "lifetime warranty". NO third-party brand names. NO "handcrafted/handmade".
8. Generate 5-10 hashtags per category mix.
9. Save full draft JSON to `work/phase2/drafts/{slot_id}-{category}.json` with same structure as the existing 3 sample drafts (mode, draft_only, ig_handle, category, scheduled_time_central, image_url, shopify_file_id, caption, hashtags, source_product, gemini_prompt_used, gemini_cost_usd, beta_check, created_at, draft_path).
10. Run BETA Check validator at `scripts/phase3_beta_check_google.mjs` adapted for IG (or build a Phase 2 specific BETA Check).
11. If BETA Check passes:
    - Update calendar slot: `status: "approved-queued"`, set `draft_path`.
    - In AUTO_PUBLISH mode (already active per insta-config.json), the slot is now eligible for the publisher cron to pick up at its scheduled time.
12. If BETA Check fails: log to `tasks/needs-amir-review.json` with the rejection reasons. Do not auto-republish.
13. Track total Gemini cost per run. Hard cap: $5/day. If 80% of cap hit, stop drafting and log remaining slots as deferred.

### Cron line to add

```
0 4 * * * /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/phase2_daily_drafter.py >> /home/openclaw/.openclaw/command-center/work/phase2/drafter-cron.log 2>&1
```

(Cron TZ already set to America/Chicago. This fires at 4 AM Central daily.)

### Manual run NOW

After installing, immediately execute the script once manually to populate:
- Today 2026-05-28 19:00 CT slot
- Tomorrow 2026-05-29 all 3 slots (08:00, 13:00, 19:00)

Total: 4 drafts. Estimated Gemini cost: 4 x $0.04 = $0.16 well under $5/day cap.

## Verification protocol

Report back with:

1. Path to new script + md5
2. Cron line confirmed installed (paste `crontab -l` output)
3. Manual run output: which 4 slots got drafts, total Gemini cost, BETA Check verdict for each
4. Updated calendar status for the 4 slots (status=approved-queued, draft_path populated)
5. Sample paths to the 4 generated drafts
6. Confirmation that tonight 2026-05-28 19:00 CT will fire correctly via the publisher cron
7. Total cost of this build session

## Constraints

- No new credentials needed. Gemini key and Shopify token already in place.
- No publishing during this build. The drafts produced go to approved-queued status only. Publishing happens via the existing publisher cron at scheduled times.
- BETA Check is the only gate. AUTO_PUBLISH mode means drafts that pass Check go live at scheduled time. Per Amir's confirmation 2026-05-27 "BETA did a great job with the instagram post how do I connect and post them" approving auto-publish.
- No em dashes in any caption or alt text.
- Hard cap: $5/day Gemini.

Execute now and report receipts.
