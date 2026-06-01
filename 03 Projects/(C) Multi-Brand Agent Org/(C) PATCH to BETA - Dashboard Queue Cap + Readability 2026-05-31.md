---
to: BETA
from: Amir
date: 2026-05-31
priority: High
type: Dashboard bugfix (queue surfacing + readability)
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Dashboard_Queue_Cap_Readability_2026-05-31.md
supersedes: none (follow-up to Approval_Suggested_Resolution_2026-05-31.md)
---

# PATCH: Dashboard Queue Cap + Readability

## Why this patch

After the Approval Suggested Resolution rollout, the on-disk queue `tasks/needs-amir-review.json` has 16 tasks (all carrying `suggested_resolution`). The dashboard at `command-center-dashboard-tmp/public/data/dashboard.json` `needs_call` array only shows 10. Six older tasks (2026-05-27 to 2026-05-29 timeframe) are invisible to Amir.

Confirmed missing from dashboard but present in queue:
- `prussian-blue-inner-ring-with-hawaiian-koa-wood-inlay-beveled-edge-8mm-tungsten-wedding-band` (2026-05-27, shopify-listing)
- `actual-fingerprint-couples-ring-forever-heart-promise-ring-...` (2026-05-28, blog-draft)
- `rose-gold-ip-with-hawaiian-koa-wood-inlay-shiny-beveled-edge-...` (2026-05-28, shopify-listing)
- The Ads API access task (2026-05-28, review, non-standard status string)
- An ig-draft (2026-05-29)
- `tungsten-wood-ring-mahogany-hardwood-inlay-polished-edges-8mm` (2026-05-29, shopify-listing)

Separately: Amir reports the dashboard is hard to read. Font too small, contrast too low.

## Action 1: Fix queue surfacing

Find the regen script that builds `command-center-dashboard-tmp/public/data/dashboard.json` from `tasks/needs-amir-review.json`. Remove whatever is dropping the 6 older tasks. Possible causes to check in order:
1. A `head -10` / `slice(0, 10)` / `LIMIT 10` cap on the `needs_call` array.
2. A date filter (e.g. "last 7 days only" or "since last deploy").
3. A status filter that excludes the non-standard `"needs Ads API access / beta-google follow-up"` status string. Normalize: any task in `needs-amir-review.json` should appear in `needs_call`, regardless of how its `status` field reads.
4. A dedup that collapses tasks with `task_id: "?"` or null IDs.

**Acceptance criteria:** After this patch and a regen, `dashboard.json.needs_call` length must equal `needs-amir-review.json` length. Run a self-check: if counts differ, log the diff to `command-center/work/phase3/dashboard-surfacing-diff-YYYY-MM-DD.json` and post to `#beta-daily`.

Also: ensure every `needs_call` entry exposes the `suggested_resolution` block so the dashboard can render the "BETA RECOMMENDS" pill. If the current static JSON strips it, stop stripping.

## Action 2: Fix readability

Amir reports the dashboard text is too small and too dark. Apply these globals to the dashboard (Tailwind / CSS, whichever the dashboard uses):

1. **Base font size:** raise from current (likely 12 to 13px) to **15px minimum** on body text. Card titles 18px. Section headers 20px. Stat numbers stay large.
2. **Text contrast:** raise muted/secondary text from current low-contrast gray to at least **WCAG AA contrast (4.5:1 against background)**. If the current theme is dark-on-dark, push primary text to `#E6E6E6` or lighter and secondary text to `#B8B8B8` minimum.
3. **Issue list inside the approval modal:** the "Issues Flagged" bullet list needs 15px text and full-white color, not muted. Same for the draft content preview block (currently very dim).
4. **Note textarea:** 15px minimum, white text on a clearly lighter background than the modal so the boundary is visible.
5. **BETA RECOMMENDS pill:** make it more prominent. 16px text, bold, with the action verb (SEND BACK, APPROVE, REJECT) in the appropriate color (red/green/amber) and the confidence (HIGH/MED/LOW) in a smaller secondary tag.
6. **Pending task cards in the kanban:** raise card title to 15px bold, status pill to 12px, timestamp to 12px secondary. Add a subtle border so individual cards are visually separable, not blending into the column.

Do not break the existing color scheme or layout. Just raise type size and contrast.

## Action 3: Quick verification

After both actions:
1. Regen dashboard.json. Confirm `needs_call` count = 16 (or whatever the live queue count is at regen time).
2. Hard refresh BETA Command. Confirm all 16 tasks visible.
3. Confirm BETA RECOMMENDS pill renders on each card.
4. Take a screenshot of the dashboard at default zoom (no browser zoom applied). Save to `command-center/work/phase3/dashboard-readability-after-2026-05-31.png`.
5. Post receipt to Slack `#beta-daily` with screenshot link and queue/dashboard count match confirmation.

## Constraints (unchanged)

- $15/day OpenRouter cap.
- No em dashes anywhere in code, copy, or commits.
- No data loss. If you change the regen script, snapshot the current `dashboard.json` first to `command-center/backups/dashboard-pre-surfacing-fix-YYYY-MM-DDTHHMMSS.json`.
- Do not touch the action contract (APPROVE / SEND_BACK_TO_AGENT / REJECT) or the `suggested_resolution` schema. Visual + surfacing only.
