---
to: BETA
from: Amir
date: 2026-05-26
priority: High
type: Phase 1 mode change (shadow-3 -> live with verification)
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Live_Mode_Verification_Gate_2026-05-26.md
supersedes: shadow-3 rollout mode from Phase1_Worker_Zero_Traffic and VESUVIUS_Listing_Standard_Override handoffs
---

# PATCH: Phase 1 Worker -> Live Mode with Verification Gate

## Why this patch

IMPRINT successfully shipped end-to-end tonight:
- BETA Shop produced a VESUVIUS-format draft
- BETA Check passed it
- Amir approved and pushed manually (with metafields, inventory rebuild, JDTR variant restructure)
- Result is live at https://shopaydins.com/products/finger-print-engraved-mens-wedding-band-two-tone-brushed-black-tungsten-ring-8mm-blue-step-edge-comfort-fit

The shadow-3 rollout mode proved the pipeline works. Time to switch to live mode so the daily worker actually ships changes to Shopify without Amir click-approving every single one.

**However:** the Amir-approval gate is replaced by a stronger BETA-side verification gate. Nothing goes live without passing BETA Check AND a post-push verification step.

## New flow (effective immediately, ongoing)

### Daily Phase 1 worker loop (5:55 AM Central -> 6:00 AM Central)

1. **Pick:** Read `brands/aydins/zero-traffic-skus.json`. Pick next unworked SKU (skip already in open/in-progress/done within 90 days). Selection priority: longest `days_in_catalog`, then highest `shopify_inventory_total`.

2. **Filter (NEW):** Exclude any product whose type or handle indicates it is not a ring (e.g. dog tags, pendants, necklaces, bracelets, earrings, cuff links, chains). Phase 1 VESUVIUS standard applies to rings only.

3. **Source detection (NEW):** Determine vendor source for the SKU before drafting. Check existing variant SKU pattern on the product:
   - If existing SKU matches `JDTR{NUMBER}-{WIDTH}-{SIZE}` -> Jewelry Depot ring -> use JDTR SKU convention.
   - If existing SKU matches `CODENAME-WIDTH-SIZE` -> Universal Jewelry ring -> use VESUVIUS CODENAME convention.
   - If product handle or title contains "fingerprint", "custom engraved", "memorial", or similar custom indicators, treat as a Jewelry Depot custom product unless evidence otherwise.
   - If unclear, route to `tasks/blocked-needs-amir.json` with the reason and skip to next SKU.

4. **Queue:** Write task to `tasks/open.json`. Include `vendor_source: "universal_jewelry" | "jewelry_depot" | "unknown"` so BETA Shop knows which SKU convention to apply.

5. **Draft (BETA Shop):** Produce a VESUVIUS-compliant draft per the updated canonical brief at `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md`. Re-read the brief from disk each time; do not cache. Pay attention to the SKU format section (Section 10) which now documents both Universal Jewelry and Jewelry Depot conventions.

6. **BETA Check (pre-push validation):** Apply all VESUVIUS rejection rules from the prior VESUVIUS_Listing_Standard_Override handoff PLUS these additions:
   - Reject if SKU format does not match the detected vendor source convention (Universal Jewelry vs Jewelry Depot).
   - Reject if meta title exceeds 70 characters (strict, not warning).
   - Reject if any FAQ contains generic policy questions (warranty, returns, shipping, sizing, exchange).
   - Reject if `custom.keywords` is not in labeled format (Material:, Inlay/Feature:, Widths:, Fit:, Profile:, Engraving:).
   - Reject if `custom.custom_faq` count is not exactly 6.
   - Reject if engraving tag is not exactly `Inside` or `Inside & Outside` (capitalized, no parens).

7. **Auto-push (NEW for live mode):** If BETA Check passes, BETA orchestrator pushes the draft to Shopify via Admin API. **No Amir click-approval required.** Push must include:
   - Snapshot of full product state to `shopify/audits/<handle>-before-<ts>.json` BEFORE write
   - `productUpdate` for title, descriptionHtml, seo.title, seo.description, tags (merge with internal Wave1_*, color-*, Brand:* tags preserved)
   - `metafieldsSet` for `custom.keywords`, `custom.quick_specs`, `custom.custom_faq` (rich_text_field), `custom.custom_faq_schema` (json), `custom.codename`, `custom.material_primary`, `custom.material_inlay`, `custom.width_mm`, `custom.{material}_ring_information_` (page reference, look up correct page), `custom.ring_size_chart` (page reference to Size Chart page, gid://shopify/Page/110085636333)
   - Snapshot of full product state to `shopify/audits/<handle>-after-<ts>.json` AFTER write

8. **Post-push verification (NEW, hard gate):** Re-query the product immediately after push. Compare live state to draft. If any of the following are wrong, **trigger rollback**:
   - Title does not match draft `title`
   - SEO title does not match draft `meta_title` or exceeds 70 chars
   - SEO description does not match or exceeds 150 chars
   - descriptionHtml differs significantly from draft `description_html` (allow whitespace normalization)
   - Any required metafield is MISSING after push
   - Any metafield value does not match what was sent
   - Tags do not include all expected new tags
   - Existing internal tags (Wave1_*, color-*, Brand:*) were stripped

9. **Rollback flow:** If post-push verification fails:
   - Use the BEFORE snapshot to restore title, descriptionHtml, seo, tags via `productUpdate`
   - Delete or revert metafields that BETA Shop set in this push
   - Log the rollback with full reason to `tasks/done.json` and `tasks/rollbacks.json`
   - Post hard alert to Slack `#beta-alerts` with handle, time, and rollback reason
   - Mark the SKU as `needs-amir-review` in a new `tasks/needs-review.json` queue
   - DO NOT auto-retry. Wait for Amir.

10. **Log success:** If verification passes, log to `tasks/done.json` with task_id, handle, product_id, before/after audit paths, "auto-pushed-live-mode" tag.

### Variant scope (still excluded from BETA Shop auto-push)

BETA Shop in Phase 1 still does NOT touch:
- Variant changes (add/remove/restructure)
- Inventory levels (changing quantities)
- Prices
- Images
- Variant SKU rewrites for existing variants

If a draft suggests any of these, BETA Check rejects and routes to `tasks/needs-amir-review.json`. Variant/inventory work is a separate flow that requires Amir.

### Updated 6 AM Central digest format

```
*Phase 1 Daily - Aydins - <date>* (Live Mode)

Yesterday:
- Pushed live: <count> listings
  - <handle> (codename: <CODENAME>, source: <vendor>)
  - ...
- Rejected by BETA Check: <count>
  - <handle>: <top 2 rejection reasons>
- Rolled back: <count>
  - <handle>: <reason>
- Blocked needs Amir: <count>

Today:
- BETA Shop is working on: <handle> (zero traffic, <X> days in catalog, source: <vendor>)

Queue health:
- Zero-traffic SKUs remaining: <int>
- Last 7 days: <X> live pushed | <Y> rejected | <Z> rolled back
- Pending Amir review: <int>

Cost yesterday: $X.XX OpenRouter DeepSeek (cap $15/day)
```

If anything was rolled back yesterday, surface that prominently with handle and reason.

### Amir's only manual touchpoint going forward

- `tasks/needs-amir-review.json` — anything BETA Check rejected for ambiguous reasons, anything rolled back, anything that requires variant/inventory/price work.
- Slack `#beta-alerts` for hard interrupts (rollback, repeated failures, etc.).
- Daily digest for situational awareness, not action.

## Updated canonical brief

The canonical listing standard at `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md` has been updated tonight (2026-05-26) with Section 10 changes:
- Documents both Universal Jewelry (CODENAME-WIDTH-SIZE) and Jewelry Depot (JDTR{NUMBER}-{WIDTH}-{SIZE}) SKU conventions
- Adds vendor identification rules
- Adds variant restructure rules (Width before Size, natural ordering)
- Notes Aydins Creations vendor for custom-engraved products

Re-read the brief from disk before next worker run. New md5 to be verified by you.

## Verification protocol for this patch

Report back with:

1. Confirmation `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md` re-read and current md5.
2. Updated `agents/beta-shop.md` prompt — paste contents, confirm it knows about source detection and dual SKU conventions.
3. Updated BETA Check validator — paste rules, confirm Jewelry Depot SKU pattern is accepted.
4. Updated orchestrator script that does the auto-push + post-push verification + rollback flow — paste path and key code.
5. Confirmation `tasks/needs-amir-review.json` and `tasks/rollbacks.json` exist (create as empty arrays if not).
6. Confirmation the daily 6 AM digest format is updated.
7. Confirmation the agent timeout was bumped 600s -> 1200s (carry-over from prior patch).
8. Dry-run output: pick one SKU from `zero-traffic-skus.json`, run the full flow in test mode (no actual push), show what would have been pushed and what BETA Check verdict would have been.

Post receipts to Slack `#beta-daily` and write a summary report to `/home/openclaw/.openclaw/command-center/work/phase1/live-mode-go-live-2026-05-27.md`.

After verification is complete, the next morning cron at 6 AM Central (12:00 UTC) will be the first live-mode worker run. Watch it closely.

## Constraints (unchanged, do not violate)

- $15/day OpenRouter DeepSeek cap, non-bypassable.
- No Claude API calls.
- Brand voice rules per Aydins CLAUDE.md and `brands/aydins/profile.md`.
- All Shopify writes preceded by audit/backup JSON.
- No variant/inventory/price changes without Amir.
- No em dashes anywhere.
- Hard rule preserved: ad spend changes, email sends, account/theme/domain changes, app installs all still require explicit Amir approval. This patch only removes the per-listing approval for copy + metafield pushes.
