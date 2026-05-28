---
to: BETA
from: Amir
date: 2026-05-26
priority: High
type: Phase 0 closeout + Phase 1 worker spec
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Phase1_Worker_Zero_Traffic_2026-05-26.md
---

# Phase 0 Closeout + Phase 1 Worker (Zero-Traffic Listings)

## Context (verified by Amir on 2026-05-26 via direct SSH audit)

Phase 0 scaffolding shipped. Verified contents of `/home/openclaw/.openclaw/command-center/`:

- agents/beta.md, agents/beta-shop.md: exist
- .claude/agents/ parallel structure: exists
- brands/aydins/profile.md: real content, well populated
- brands/theonar/profile.md: STUB. Frontmatter only, body empty.
- brands/amazing-wedding-bands/profile.md: STUB. Frontmatter only, body empty.
- tasks/open.json: exists, empty array (3 bytes)
- tasks/done.json: exists, 19.5 KB
- agents/status/beta.json + beta-shop.json: initialized idle
- Dashboard at localhost:3333: confirmed live via SSH tunnel
- Daily 6am Central cron: firing 11 consecutive days, posts digest only

Issue: `tasks/open.json` is empty. The cron posts the digest but no work is ever queued for BETA Shop. The daily digest reads "BETA Shop ready. No listing drafted in this digest run." 11 days in a row. Phase 1 was never wired to fire actual work.

This handoff closes the two Phase 0 stubs and builds the Phase 1 worker loop.

---

## Work item 1: Populate the two brand profile stubs

Files: `brands/theonar/profile.md` and `brands/amazing-wedding-bands/profile.md`.

Required structure (mirror the existing Aydins profile):
- Positioning
- Target customer
- Voice
- Visual direction
- Product and content rules

Source content: Multi-Brand Operations Plan sections 2.2 (Theonar) and 2.3 (Amazing Wedding Bands). If you do not have that doc on the VPS, reply "need MBOP sections 2.2 and 2.3 pasted" and Amir will SCP them over.

Keep the frontmatter `created_by` field as-is. Add `populated_by: "BETA, 2026-05-26"` on update.

---

## Work item 2: Build the Phase 1 daily worker loop

**Target:** BETA Shop optimizes one Aydins listing per day that has zero traffic.

### 2.1 Data source — zero-traffic SKU list

**Use Shopify Analytics, not GA4.** BETA Shop's own spec (`/home/openclaw/.openclaw/command-center/agents/beta-shop.md`) says: "Use Shopify Analytics for prioritization: sessions, conversion, and orders per product. Do not use GA4 pageviews for Phase 1 listing selection. GA4 access is marked won't-fix for Phase 1." Respect that rule.

Definition of "zero traffic" for Phase 1:
- Shopify product status: ACTIVE and PUBLISHED.
- **Shopify Analytics sessions on the product page over trailing 30 days: 0.**
- Exclude DRAFT, ARCHIVED, HIDDEN status.
- Exclude products with tags: `sunset`, `discontinue`, `hidden`, `do-not-edit` (if any exist).
- Exclude products with zero inventory and `denied` inventory policy (truly unavailable).

Output file: `brands/aydins/zero-traffic-skus.json`. Regenerate weekly, Sunday 11:00 PM Central via cron.

Schema:
```json
{
  "generated_at": "2026-05-26T23:00:00-05:00",
  "lookback_days": 30,
  "data_source": "shopify_analytics",
  "total_skus": 287,
  "skus": [
    {
      "product_id": "gid://shopify/Product/...",
      "handle": "vesuvius-...",
      "title": "...",
      "vendor": "Universal J",
      "tags": ["..."],
      "shopify_sessions_30d": 0,
      "shopify_status": "ACTIVE",
      "shopify_inventory_total": 80,
      "created_at_shopify": "2024-...",
      "days_in_catalog": 412
    }
  ]
}
```

### 2.2 Daily worker (runs at 5:55 AM Central, before the existing 6:00 AM digest)

Sequence:
1. Read `brands/aydins/zero-traffic-skus.json`.
2. Pick the next unworked SKU. Skip anything already present in `tasks/open.json`, `tasks/in-progress.json`, or `tasks/done.json` within the last 90 days.
3. Selection priority order (when ties exist):
   a. Longest `days_in_catalog` first (oldest stale listings get attention first).
   b. Then highest `shopify_inventory_total` (more inventory = more lost opportunity).
4. Write a task to `tasks/open.json`:
```json
{
  "task_id": "uuid-v4",
  "created_at": "ISO timestamp",
  "agent": "BETA Shop",
  "brand": "Aydins",
  "type": "listing-optimization-zero-traffic",
  "product_id": "gid://shopify/Product/...",
  "handle": "...",
  "status": "queued"
}
```
5. Invoke BETA Shop with the task. **The canonical listing standard is already on the VPS at `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md`** (301 lines, mirror of Amir's vault canonical brief, compiled 2026-05-12). Worked reference example: CREDO. Real CREDO snapshots exist on disk under `/home/openclaw/.openclaw/agents/beta/02 Build/listing-revamp-overnight-2026-04-22/universal-j-custom/compliance-cleanup/snapshots/credo-*`.

**BETA Shop scope for Phase 1 is COPY ONLY.** Per BETA Shop's own spec: "Draft copy only unless Amir explicitly approves a higher-risk change. Price, image replacement, schema, inventory, app, theme, email, ad, domain, and publish changes are out of scope."

BETA Shop produces drafts for these 6 fields only:
- `title` (Section 1 of the brief)
- `meta_title` / SEO title (Section 2, ≤70 chars)
- `meta_description` (Section 3, ≤150 chars)
- `description_html` (Section 4: opening paragraph, labeled Key Features bullets, Why CODENAME close, FAQ block from Section 5 with exact mandatory wording)
- `tags` (Section 6: engraving bare-word, material, profile, inlay, audience, theme)
- `image_alt_text` (Section 7: pull current alt text first, keep existing OR write generic-truthful that's true of any product photo. Never invent scene descriptions like "on hand", "on velvet", "marble", "display", "lifestyle", "close-up" unless source image data proves it.)

**Out of scope for BETA Shop Phase 1 (do not draft):** Quick Specs metafields, Google category metafields, variant changes, SKU rewrites, inventory updates, pricing math, cost-per-item, image replacement, schema, collection assignment, publish action.

**Code names:** Each zero-traffic SKU needs a codename if the product handle doesn't already follow the CODENAME pattern (CREDO, FLETCHER, PALEO, NAUTILUS, VESUVIUS, etc.). Beta-Shop proposes one in the draft and flags it for Amir approval. Codename must be a single short evocative word in ALL CAPS, ideally a Latin or mythological root tied to the ring's material/pattern/feel.

**Output format:** BETA Shop must return the JSON object defined in its own spec at `/home/openclaw/.openclaw/command-center/agents/beta-shop.md` under "Required JSON output contract." Specifically the `status: "ok"` shape with `approval_risk: "copy_only_no_price_no_image_replacement_no_schema_no_publish"`. Or the `status: "error"` shape with `needs_beta_digest_surface: true` if input is missing. No prose. No markdown. No code fences outside the JSON.

6. BETA Check reviews the draft against the canonical brief at `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md`. Scope-appropriate checklist (copy-only Phase 1):

**Copy quality checks (Phase 1 scope):**
- Title follows Section 1 pattern: `CODENAME | [Material] [Product Type], [Pattern/Inlay], [Profile/Feature]`
- SEO title ≤70 chars (Section 2)
- Meta description ≤150 chars (Section 3)
- Description has opening paragraph + labeled Key Features bullets + Why CODENAME close (Section 4)
- FAQ block present with all 5 mandatory questions and exact approved wording (Section 5)
- Engraving tag is bare-word `Inside` or `Inside & Outside`, matches universal-jewelry.com source rule (Section 6)
- Image alt text either matches existing or is generic-truthful (no invented scene descriptions)
- Comfort Fit declared in Key Features (default on every Aydins ring)

**Section 12 (Hard Rules — automatic rejection if violated):**
- No em dashes anywhere
- No mentions of Thorsten, Universal Jewelry, JCK, or any supplier
- No "handcrafted / handmade / forged / built / cut / made by hand / made in our workshop" language — Aydins **engraves and ships**, does not manufacture
- No reference to Grapevine Mills Mall kiosk (closed)
- No "Flower Mound" as workshop/brand-voice location in listings — only `Irving, Texas` (Flower Mound is legal address only, used in email legal footers and Returns page)
- No bare "lifetime warranty" — use "free first 6 months, $34.50 flat 6-12mo, $54.50 flat after"
- No "free lifetime resizing" or "lifetime fit guaranteed" — use approved Lifetime Sizing language
- No "30-day free returns" — use "30-day returns. $25 restocking, customer pays return shipping. Engraved rings excluded."
- No "free returns" (returns are never free)
- No "2-day shipping" — use "Free U.S. shipping. Most orders ship in 1-3 business days."
- No "$100 14k gold fee" — correct: 25% surcharge on items over $1,000
- No "Price Match Guarantee" trumpeted on PDP
- No "5% bonus on every order" (conditional only)

If BETA Check rejects: status becomes `rejected`, log reason to `tasks/done.json`, drop into Slack `#beta-alerts`, and move to next SKU tomorrow.

If BETA Check passes: status becomes `pending-amir-approval`. Drop draft into Slack `#beta-daily` morning digest.

7. **Hard rule. Do not push to Shopify without Amir's explicit Slack thread approval.** Wait for "approved" reply in the thread. No exceptions.

8. On Amir approval: push to Shopify via Admin API, log to `tasks/done.json` with new entry:
```json
{
  "timestamp": "ISO",
  "agent": "BETA Shop",
  "action": "publish listing optimization",
  "brand": "Aydins",
  "product_id": "...",
  "handle": "...",
  "task_id": "...",
  "result": "published, audit at shopify/audits/<handle>-update-<ts>.json"
}
```

Always create a Shopify audit file before write: `shopify/audits/<handle>-before-<ts>.json` and `<handle>-after-<ts>.json`. Standard backup protocol.

9. Move SKU from `zero-traffic-skus.json` to `worked-skus.json` so it does not get re-picked next week.

### 2.3 Replace the empty 6 AM Central digest

Current digest reads: "BETA Shop ready. No listing drafted in this digest run."

New digest format:
```
*Phase 1 Daily — Aydins — <date>*

Yesterday:
- Pushed: <handle> (if any)
- Approved by Amir: <handle>
- Pending your approval: <handle> [link or paste of draft]
- Rejected by BETA Check: <handle> — reason

Today:
- BETA Shop is working on: <handle> (zero traffic, <X> days in catalog, <Y> units in stock)

Queue health:
- Zero-traffic SKUs remaining: <int>
- This week pace: <X> drafts | <Y> approved | <Z> pushed
- Backlog awaiting Amir approval: <int>

Blockers:
- <BETA Check rejections, API failures, anything that needs Amir>

Cost yesterday: $X.XX OpenRouter DeepSeek (cap $15/day)
```

If a draft is pending Amir approval from a previous day, surface it in every morning digest until resolved.

---

## Constraints (carry forward, do not violate)

- No publishing to Shopify, no email sends, no ad spend changes, no account/theme/domain changes without Amir explicit approval.
- No em dashes anywhere in BETA output (drafts, code comments, logs).
- $15/day OpenRouter DeepSeek cap, non-bypassable.
- No Anthropic/Claude API calls. (NOTE: OpenClaw config shows `anthropic/claude-sonnet-4-6` as primary. Confirm whether this is actually being called or is dormant. If active, switch primary to GPT-5.5 via Codex OAuth.)
- Brand voice rules from Aydins CLAUDE.md and brands/aydins/profile.md.
- All Shopify writes preceded by an audit/backup JSON.

---

## Verification protocol

When complete, report back with receipts. Do not just say "done."

1. Paste full body of `brands/theonar/profile.md` after population.
2. Paste full body of `brands/amazing-wedding-bands/profile.md` after population.
3. Path to the new daily worker script.
4. Path to the new Shopify Analytics + Shopify Admin cross-reference script (the zero-traffic picker).
5. First run of `zero-traffic-skus.json` — paste `generated_at`, `total_skus`, and first 10 entries.
6. Sample of the new digest format using yesterday's data (even if empty queue).
7. Confirm the 5:55 AM Central cron job now calls: zero-traffic-picker -> BETA Shop draft -> BETA Check review -> 6:00 AM digest, in that order.
8. md5 hash and last-modified timestamp of every new or modified file.
9. Confirm `tasks/in-progress.json` exists (create if not).

Post receipts to `#beta-daily` and also write a summary report to `/home/openclaw/.openclaw/command-center/work/phase1/phase1-worker-go-live-2026-05-XX.md`.

---

## Open question to confirm before going live

Should the first draft go live in BETA-Check-then-Amir mode immediately, or run for 3 days in "draft only, no even surface to Amir" shadow mode so we can sanity check the picker and the BETA Shop output quality without flooding the Slack digest?

Default: run in shadow mode for 3 days. Then surface to Amir for approval flow.

Reply with "shadow-3" to confirm default, or "live" to skip shadow mode.
