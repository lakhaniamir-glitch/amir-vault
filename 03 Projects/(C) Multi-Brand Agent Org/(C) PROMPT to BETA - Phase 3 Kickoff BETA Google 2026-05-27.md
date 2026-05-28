---
to: BETA
from: Amir
date: 2026-05-27
priority: High
type: Phase 3 kickoff - BETA Google on Aydins
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Phase3_Kickoff_BETA_Google_2026-05-27.md
---

# Phase 3 Kickoff: BETA Google on Aydins

## Why this is happening earlier than the kickoff doc said

The original kickoff specified Phase 3 (BETA Google) at weeks 6-7 after 30-day Phase 1 stability. Amir is compressing: Phase 1 went live 2026-05-26, Phase 2 went live 2026-05-27, Phase 3 starts now (same night).

Risk acknowledged: parallel agent debug. Mitigation: BETA Google starts in DRAFT-ONLY mode for the SEO/MC work (no auto-push). Google Ads work stays draft-only until Amir provides Ads API credentials.

## Locked decisions (do not redesign)

1. **Scope: Aydins only.** Theonar and AWB come in Phase 6.
2. **Channels under BETA Google:**
   - Google Search Console / SEO
   - Google Merchant Center
   - Google Ads (when credentials provided)
   - GA4 reads (for analysis only, not modifications)
3. **Initial mode: DRAFT-ONLY.** Same pattern as Phase 2 started. After Amir reviews first batch of drafts and is satisfied, flip to AUTO_PUBLISH for low-risk surfaces (SEO metadata pushes to Shopify).
4. **Hard rule preserved: any Google Ads spend change requires Amir explicit approval.** No exceptions. BETA Google can DRAFT ad copy and budget recommendations but cannot push spend changes.
5. **Hard rule preserved: MC product removals require Amir explicit approval.** The 14 pending products from the May 2026 audit are still pending — BETA Google's first task is to re-audit and confirm.
6. **Voice and brand rules: inherit from Aydins CLAUDE.md and `/brands/aydins/profile.md`.** No em dashes, no bare "lifetime warranty", Irving Texas only when transactional, no supplier brand names.

## Credentials inventory

### Already in place

- `/home/openclaw/.openclaw/agents/beta/google/ga4-oauth-token.json` (mode 600). Scope: `analytics.readonly`. Auto-refreshes. Use for GA4 reads.
- `/home/openclaw/.openclaw/agents/beta/google/ga4-oauth-client.json` (OAuth client credentials).
- `/home/openclaw/.openclaw/agents/beta/google/service-account.json`. Project: `amirs-command-center`. Service account email: `beta-agent@amirs-command-center.iam.gserviceaccount.com`. Use for Merchant Center reads + writes (with Amir's explicit approval for writes).
- Prior MC audit artifacts in `/home/openclaw/.openclaw/agents/beta/google/jewelry-depot-*` from 2026-05-12.

### NOT yet in place (Amir provides later)

- Google Ads API: developer token, OAuth refresh token, customer ID -> store at `/home/openclaw/.openclaw/agents/beta/credentials/google-ads.env` (mode 600) when provided.
- Search Console API: OAuth refresh token with scope `webmasters.readonly` -> store at `/home/openclaw/.openclaw/agents/beta/credentials/google-search-console.env` when provided.
- Indexing API (optional, for triggering re-crawls): API key -> same credentials folder.

## Phase 3 setup tasks (do these tonight, in order)

### Setup Task 1: Activate BETA Google agent

Update `/home/openclaw/.openclaw/command-center/agents/beta-google.md` from stub to active prompt. Required sections:

- Scope (Aydins Google Ads + SEO + MC + Search Console + GA4 analytics)
- Non-negotiable rules (carry from BETA Shop + BETA Insta + add Google-specific)
- Phase 3 process (DRAFT-ONLY initial, then AUTO_PUBLISH for SEO metadata after Amir flip)
- Output contract (JSON, similar to BETA Shop)
- Required brand rules (no em dashes, warranty wording, Irving Texas, no supplier names, no "handcrafted")
- Hard never-do rules (no Ads spend changes, no MC product removals, no app installs, no account changes)

### Setup Task 2: Re-audit Merchant Center

Re-run MC audit using existing scripts:
- `python3 /home/openclaw/.openclaw/agents/beta/google/fetch_merchant.py` (or equivalent)
- Compare against current Shopify product list
- Confirm the 14 pending products to remove from MC still exist (10 draft + 4 archived per Beta Operations State 2026-05-26)
- List current GMC disapprovals and issues
- Output: `/home/openclaw/.openclaw/command-center/work/phase3/mc-audit-2026-05-28.md` + `.json`
- Surface the 14-product removal queue to Amir again via Slack #beta-daily morning digest. Do not delete without explicit Amir approval.

### Setup Task 3: GA4 traffic + conversion analysis

Pull last 30 days of GA4 data for Aydins:
- Sessions, conversions, revenue by channel (cross-network, direct, paid social, organic search, paid search, organic social, organic shopping, email, referral, paid shopping, SMS, paid other)
- Top 20 landing pages by sessions
- Top 20 landing pages by revenue
- Bottom 20 product pages by conversion rate (high traffic + low conversion = optimization opportunities)
- Bottom 20 product pages by traffic (low traffic = SEO opportunity, overlaps with Phase 1 zero-traffic worker)

Output: `/home/openclaw/.openclaw/command-center/work/phase3/ga4-30day-analysis-2026-05-28.md`

### Setup Task 4: SEO opportunity detection

Cross-reference:
- Aydins Shopify products (active, published)
- GA4 traffic data (low sessions, low conversion)
- Existing meta titles / descriptions (incomplete, missing, em-dashed)
- Merchant Center disapproval reasons (some are SEO-fixable)

Produce a prioritized list of 20 SEO opportunities (pages with high potential lift if metadata is improved). For each, include:
- Current meta title + length
- Current meta description + length
- Current GA4 sessions / conversions
- Why it's an opportunity (missing keywords, weak description, etc.)
- Draft improvement (VESUVIUS-format meta title and description if it's a product, page-specific format if it's a collection or blog post)

Output: `/home/openclaw/.openclaw/command-center/work/phase3/seo-opportunities-2026-05-28.md`

This becomes the BETA Google daily draft queue (similar to Phase 1's zero-traffic-skus.json).

### Setup Task 5: Google Ads inventory (if credentials available)

If Amir has NOT yet provided Google Ads credentials: skip this task, output a setup checklist for Amir in the digest:
- Apply for developer token at https://ads.google.com/aw/apicenter (1-2 day approval for Basic tier)
- Create OAuth 2.0 credentials in Google Cloud Console (project: amirs-command-center, reuse if possible)
- Run OAuth flow with scopes: `https://www.googleapis.com/auth/adwords`
- Note Aydins Google Ads customer ID (format: XXX-XXX-XXXX)
- Drop into `/home/openclaw/.openclaw/agents/beta/credentials/google-ads.env` mode 600 with: GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET, GOOGLE_ADS_CUSTOMER_ID

If Amir HAS provided Google Ads credentials: inventory the account state:
- Active campaigns (count, budget, status, conversion volume)
- Top spending keywords
- Quality Score distribution
- Recent week spend vs targets
- Disapproved ads / policy issues
- Output to `/home/openclaw/.openclaw/command-center/work/phase3/google-ads-inventory-2026-05-28.md`

### Setup Task 6: Search Console inventory (if credentials available)

If no Search Console credentials: skip, add to Amir setup checklist:
- Verify https://shopaydins.com in Search Console (likely already done)
- Generate OAuth refresh token with scope `https://www.googleapis.com/auth/webmasters.readonly`
- Drop into `/home/openclaw/.openclaw/agents/beta/credentials/google-search-console.env` mode 600

If creds available: pull last 90 days:
- Top 50 queries (impressions, clicks, CTR, position)
- Top 50 pages (impressions, clicks, CTR, position)
- Coverage issues (excluded, error, valid with warnings)
- Mobile usability issues
- Core Web Vitals field data
- Output to `/home/openclaw/.openclaw/command-center/work/phase3/search-console-inventory-2026-05-28.md`

### Setup Task 7: BETA Check rules for Google Ads draft validation (build, do not activate yet)

Build the BETA Check validator for Google Ads copy. Activates when Google Ads credentials are in place.

Rules for ad copy validation:
- Headlines: max 30 chars each, 15 max per RSA
- Descriptions: max 90 chars each, 4 max per RSA
- No em dashes
- No bare "lifetime warranty" - use "Aydins Lifetime Warranty" or trust pillars from brand profile
- No third-party brand names (Thorsten, Universal Jewelry, JCK)
- No "handcrafted/handmade/forged"
- No "Flower Mound" in customer-facing ad copy (Irving Texas is the workshop)
- Must include at least one of: free engraving, free U.S. shipping, lifetime warranty (with proper wording)
- No misleading promises (no "Cheapest", "Best price guaranteed", "100% pure" if not literally true)
- All landing page URLs must be on shopaydins.com domain

For PMax asset groups: same caption/headline rules, plus image alt text validation.

Save the validator at `/home/openclaw/.openclaw/command-center/scripts/phase3_beta_check_google.mjs` or `.py`.

### Setup Task 8: Phase 3 worker script (build, daily-cron-ready)

Build `phase3_daily_worker.py` (or .mjs) that runs at a chosen daily cron time (suggest 6:30 AM Central, after Phase 1's worker but before the 6:00 AM digest, actually 5:30 AM Central is better). Logic:

1. Read GA4 last-7-day data, refresh `work/phase3/seo-opportunities.json` (live priority queue)
2. Pick next unworked SEO opportunity (skip Phase 1 work-in-progress to avoid double-edit)
3. BETA Google drafts: improved meta title, meta description, focus keywords for the page
4. BETA Check validates against rules (length, voice, no em dashes, etc.)
5. Status: `drafted-seo` (DRAFT-ONLY mode default - sits in Slack #beta-daily for Amir review)
6. After Amir flips to AUTO mode (similar to Phase 2): BETA Google auto-pushes via Shopify Admin API + post-push verify + rollback

When Google Ads credentials arrive:
7. Daily check: any campaigns paused unexpectedly, any spend anomalies (>20% deviation from 7-day rolling avg), any disapproved ads
8. If spend anomaly: hard alert to #beta-alerts, freeze any pending draft pushes
9. Daily draft of 1 new ad headline/description variation for the lowest-CTR active ad group

### Setup Task 9: Digest integration

Update the 6:00 AM Central digest script to include a Phase 3 section:

```
*Phase 3 Daily - Aydins Google - <date>*

Yesterday:
- SEO metadata pushed: <count> pages (DRAFT-ONLY: <count> awaiting Amir; AUTO: <count> live)
  - <page>: <change summary>
- MC issues triaged: <count>
- Ad drafts produced: <count> (when Ads creds available)
- Spend anomalies flagged: <count>

Today:
- SEO opportunities in queue: <int>
- Next page in line: <handle>
- MC products still pending Amir removal approval: <count>

Channel snapshot (GA4 7-day):
- Sessions: <int>
- Revenue: $<int>
- Top channel: <name> ($<int>)
- Worst-performing channel: <name>

Pending Amir:
- <action> on <thing>
- ...

Cost yesterday: $X.XX (BETA Google agent runs)
```

## Workflow when credentials are complete

After Amir provides Google Ads + Search Console credentials:

1. **Daily SEO loop** (auto, with verification gate same as Phase 1):
   - Pick high-opportunity page
   - BETA Google drafts SEO metadata
   - BETA Check validates
   - Auto-push to Shopify
   - Post-push verify
   - Rollback on failure

2. **Daily Ads monitoring (manual approval, hard rule):**
   - BETA Google reads spend, CTR, conversion data
   - Drafts new ad variations
   - Drafts pause/scale recommendations
   - Posts to Slack #beta-daily with "Amir approval required" tag
   - Amir replies "approve" / "reject" / "edit"
   - Only Amir-approved changes get pushed via Ads API

3. **Weekly Merchant Center audit (existing Monday 10 UTC cron folds in):**
   - Already wired, but expand the cron to include Search Console coverage report

## Verification protocol

When Setup Tasks 1-9 are done (or as far as possible without Ads/Search Console creds), report back with:

1. md5 of updated `agents/beta-google.md`
2. md5 + content summary of the MC re-audit (confirm 14 still pending or new count)
3. ga4-30day-analysis-2026-05-28.md path and 5-line summary
4. seo-opportunities-2026-05-28.md path and top-5 opportunities
5. google-ads-inventory or setup checklist (depending on creds)
6. search-console-inventory or setup checklist
7. Phase 3 BETA Check validator path and rule count
8. Phase 3 daily worker path + cron line proposed
9. Digest integration confirmation
10. Cost spent tonight

Post receipts to Slack #beta-daily and write full report to `/home/openclaw/.openclaw/command-center/work/phase3/phase3-kickoff-receipts-2026-05-28.md`.

## What Amir does next

1. Tomorrow morning: review the SEO opportunities, MC re-audit, GA4 snapshot
2. **Approve the 14 MC product removals** (or veto specific ones) — this is the longest-pending item
3. **Provide Google Ads credentials** when ready (no rush, BETA Google produces value with what's there)
4. **Provide Search Console credentials** when ready
5. When ready to flip to AUTO mode for SEO metadata pushes: reply in Slack "flip to auto" or equivalent

## Hard rules (carry forward)

- Ad spend changes require explicit Amir approval, no exceptions.
- MC product removals require explicit Amir approval, no exceptions.
- Email sends, account/theme/domain changes, app installs: explicit Amir approval, no exceptions.
- $15/day OpenRouter cap. Phase 3 work shares this budget with Phase 1 and Phase 2.
- No Anthropic/Claude API calls.
- No em dashes anywhere.
- No bare "lifetime warranty".
- Irving Texas only when transactional. Flower Mound only in email legal footers.
- No supplier brand names. No "handcrafted/handmade/forged".
- All Shopify writes preceded by snapshot, followed by verify, with rollback ready.

End of kickoff. Execute setup tasks 1-9, post receipts.
