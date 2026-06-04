---
to: BETA
from: Amir (via Claudian)
date: 2026-06-02
priority: High
type: Meta Ads stabilization + tracking verification + creative pipeline kickoff
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Meta_Ads_Stabilization_2026-06-02.md
mode: DRAFT-ONLY for any Meta Ads change. READ-ONLY for tracking diagnostics. WRITE allowed for Shopify-side Pixel/CAPI config only after explicit Amir approval.
---

# Meta Ads Stabilization, Tracking Verification, Creative Pipeline Kickoff

## Why this is happening

Aydins Meta Ads account (act_23304577) went dark roughly 2026-05-25 through 2026-06-02 morning. $0 spend for ~7 days. Shopify revenue cliff hit 06/01. GA4 traffic did NOT fall during the cliff, conversion did. Most likely cause: Meta delivery stopping removed a converting demand source from the mix.

Account is delivering again as of this morning. Operator already paused the weakest ad set (Gym Images) inside the only active campaign (Couples Engraved). The winner inside that campaign is now absorbing full $50/day. Catalog Sales is paused and staying paused.

Two parallel needs:
1. Verify tracking is clean after the 8-day disruption. Highest-leverage free move in the account.
2. Build a creative production pipeline so we have the next wave ready when the winner stabilizes.

## Locked decisions (do not redesign)

1. **Active campaign:** `1|AY|6.3|Couples engraved| - 30` (ID 6929192369326), Sales objective, $50/day. STAYS LIVE. Do not edit the campaign, ad set, or ad creative directly.
2. **Protected winner inside that campaign:** ad set `1|AY|6.3|Couples engraved| - 30|*|All mobile devices|1|US`, ad `Single image|3`. ROAS 5.44, CPA $78.69, CTR 2.45%, Freq 2.29. Do not touch.
3. **Paused as of 2026-06-02:** ad set `1|AY|6.29|Gym Images| - 30|*|All mobile devices|2|US` inside Couples Engraved. Stays paused.
4. **Catalog Sales campaign (ID 52566193429730):** paused 2026-06-02 09:50 PT. Stays paused for 60 days minimum. Do not edit, do not test reset. Root cause was structural (retargeting pool too small at 827 LPV/month). Fix is scaling prospecting, not editing catalog.
5. **No budget increase for 14 days.** Hold $50/day on the active campaign. Even if ROAS spikes early, do not scale until 14 stable delivery days are confirmed.
6. **No new ad sets for 14 days.** New creatives, when shipped, go into the existing winning ad set to keep Learning signal consolidated. Do not duplicate the winner into a new ad set.
7. **Advantage+ Shopping Campaigns: not now.** Revisit in 30 days after tracking is verified, creatives are live, and the manual campaign has 30 stable days post-restart.

## Hard rules (carry forward)

- **No Meta Ads spend changes without explicit Amir approval.** Same hard rule as Google Ads. BETA can READ everything. BETA can DRAFT ad copy, ad set settings, audience adjustments. BETA cannot push budget changes, pause changes (beyond what is already done), audience changes, or creative changes on its own. Drafts go to Slack `#beta-daily` for Amir review.
- **No new ads pushed live without Amir approval.** Creative production is allowed (briefs, mockups, copy drafts). Publishing is not.
- **Shopify Pixel/CAPI config changes require explicit Amir approval before push.** Read access is unrestricted. Write requires sign-off.
- **No em dashes anywhere.** Locked rule.
- **No bare "lifetime warranty".** Use "Aydins Lifetime Warranty" or the trust pillars from the brand profile.
- **No third-party brand names.** No supplier names. No "handcrafted/handmade/forged."
- **All ad copy validated against BETA Check rules.** If a Meta-specific validator does not exist yet, build it as part of this work (Task 6 below).
- **$15/day OpenRouter cap shared across all phases.** Stay inside it.

## Credentials inventory

### What BETA already has
- Shopify Admin API (read/write)
- GA4 OAuth (`/home/openclaw/.openclaw/agents/beta/google/ga4-oauth-token.json`)
- Slack fallback poster (`scripts/slack_post.js`)
- Klaviyo access
- Merchant Center service account

### What BETA needs for full Meta work (Amir provides if missing)
- Meta Marketing API access token for act_23304577 (Amir already verified this works as of 2026-06-02 audit pull; token was pasted in Discord and should be rotated soon)
- Meta Business Manager admin access for Events Manager diagnostics
- Pixel ID and dataset ID for Aydins
- Drop credentials at `/home/openclaw/.openclaw/agents/beta/credentials/meta-ads.env` mode 600 with: META_ACCESS_TOKEN, META_AD_ACCOUNT_ID, META_PIXEL_ID, META_DATASET_ID, META_BUSINESS_ID

**If the Discord-pasted token is the only credential available:** rotate it before doing any work. Pasted secrets are compromised. Generate fresh long-lived token via System User on Business Manager and drop into the env file above.

## Setup tasks (execute in this order)

### Task 1: Rotate Meta token, confirm API access

- Generate fresh System User token in Meta Business Manager with scopes: `ads_read`, `ads_management`, `business_management`, `read_insights`.
- Drop into `/home/openclaw/.openclaw/agents/beta/credentials/meta-ads.env` mode 600.
- Verify access by pulling account-level metadata for act_23304577.
- Output token rotation receipt (no token contents, just confirmation + timestamp + scopes verified) to `/home/openclaw/.openclaw/command-center/work/meta/token-rotation-2026-06-02.md`.
- Notify Amir via Slack `#beta-daily` once rotated. Old token can be revoked after confirmation.

### Task 2: Pixel / CAPI / EMQ tracking audit (READ-ONLY)

Pull Events Manager diagnostics for Aydins Pixel:

| Signal | Target | Action if Below |
|---|---|---|
| EMQ score for Purchase | 8.0+ | Flag Shopify CAPI payload gaps |
| EMQ score for ATC | 7.0+ | Flag missing customer match params |
| EMQ score for ViewContent | 6.0+ | Flag client-side dedup gaps |
| Dedup rate Pixel vs CAPI | 90%+ | Flag event_id matching break |
| AEM Purchase priority | 1 | Flag if reset during dark period |
| Test Events Purchase fires from both Pixel + CAPI with matching event_id | Yes | Flag broken integration |
| Diagnostics tab warnings on Purchase, ATC, IC, VC | None | Flag any |
| Account quality flags from dark period | None | Flag any |

Output to `/home/openclaw/.openclaw/command-center/work/meta/tracking-audit-2026-06-02.md` with:
- All numbers above
- Severity-ranked list of fixes (Critical / High / Medium)
- For each fix: exact remediation step (Shopify app setting, Klaviyo integration toggle, AEM reset action, etc.) WITHOUT executing the fix
- Estimated impact of each fix (CPM reduction, attribution accuracy improvement)

Post 1-paragraph summary + top 3 issues to Slack `#beta-daily` tagged "Amir approval required" if any fixes need executing.

### Task 3: Daily Meta delivery monitor (build + cron)

Build a daily cron job that runs at 7:00 AM Central:

- Pull yesterday's spend, impressions, reach, purchases, ROAS for act_23304577
- Detect "delivery failure" condition: spend < 50% of campaign daily budget, OR zero impressions, OR account spend disabled
- If failure detected: post hard alert to Slack `#beta-alerts` AND `#beta-daily` with "Meta delivery failure" tag
- If healthy: include 1-line health stat in the morning digest
- Log to `memory/meta-delivery-YYYY-MM-DD.md`

Cron line proposed: `0 12 * * * cd /home/openclaw/.openclaw/agents/beta && node scripts/meta_delivery_check.mjs`

This is the operational gap that allowed the 8-day blackout to happen. Closing it is the second-highest-leverage move in this whole package.

### Task 4: Daily Meta performance digest (build + cron, separate from delivery monitor)

Build a daily report that runs after the delivery monitor (8:00 AM Central) and pulls:

- Yesterday: spend, purchases, ROAS, CPA, CTR, CPC, CPM, frequency per active ad set
- Rolling 7-day: same metrics
- Rolling 14-day: same metrics
- Learning Phase status per active ad set
- Frequency trend (alert if any ad set crosses 3.5)
- ROAS trend (alert if 7-day ROAS drops below 2.0 on the winner)
- Spend trend (alert if daily spend deviates more than 20% from target)

Output to Slack `#beta-daily` as a structured digest. Log to `memory/meta-perf-YYYY-MM-DD.md`. Include "scale-eligible?" boolean: TRUE only if (winner 7-day ROAS > 3.0) AND (CPA < $75) AND (frequency < 3.0) AND (14 stable delivery days passed since 2026-06-02).

### Task 5: Catalog Sales post-mortem documentation

One-time task. Write a clean post-mortem to `/home/openclaw/.openclaw/command-center/work/meta/catalog-sales-postmortem-2026-06-02.md`:

- Final 30-day stats (spend $536.53, 6 purchases, ROAS 2.09, freq 9.21, CPM $26.49)
- Final 14-day stats showing degradation (ROAS 1.16, CPA $126.24, freq 5.04)
- Root cause: retargeting pool too small (827 LPV/month) for $25/day catalog budget
- Recovery conditions (LPV from Meta at 3,000+/month, prospecting at $75-100/day with ROAS holding above 3.0)
- Lockout: do not test reset for 60 days minimum
- Filed for the record so this does not get relitigated in 3 weeks

### Task 6: Meta Ads BETA Check validator (build, do not activate for live pushes yet)

Same pattern as the Google Ads validator from Phase 3 kickoff. Build the rule set for Meta-specific ad copy validation. Save at `/home/openclaw/.openclaw/command-center/scripts/beta_check_meta.mjs`.

Rule set:
- Primary text: max 125 chars before "See more" truncation, hard max 2200
- Headline: max 27 chars before truncation, hard max 40
- Description: max 27 chars before truncation, hard max 30
- No em dashes
- No bare "lifetime warranty"
- No supplier names (Universal Jewelry, JCK, Thorsten)
- No "handcrafted/handmade/forged"
- Must include at least one trust pillar (free engraving / free U.S. shipping / Aydins Lifetime Warranty / since 2011 / engraved in Texas)
- Landing URL on shopaydins.com domain
- No misleading claims ("best price", "100% pure" unless literally true)
- Engraving claims must match Zepto availability tag on the product
- Pixel firing check: validate the landing page has Pixel ID matching account Pixel ID

Validator runs against any draft creative produced by Task 7 before it goes to Amir for approval.

### Task 7: Creative production pipeline (4 concepts, DRAFT-ONLY)

Produce structured creative briefs for 4 concepts, branched from the winning "Couples Engraved" angle. Save each brief at `/home/openclaw/.openclaw/command-center/work/meta/creative-briefs/`.

| Priority | Brief filename | Concept | Format | Production complexity |
|---|---|---|---|---|
| 1 | `01-ugc-testimonial.md` | Real customer talking about why Aydins for husband/partner | 15-30s phone video OR single image + customer quote overlay | Low (needs 1 real customer) |
| 2 | `02-before-after-engraving.md` | Plain ring frame -> engraving in progress frame -> finished ring frame -> wearing it frame | Carousel (4 frames) OR 10-15s video | Medium |
| 3 | `03-story-narrative.md` | Carousel arc: hook (emotion) -> product (engraving capability) -> proof (review/testimonial) -> CTA | Carousel (4 frames) narrative arc | Medium |
| 4 | `04-price-anchored-dr.md` | Direct response. "Personalized. Ships in 3 days. Under $X." | Single image | Low |

Each brief includes:
- Concept summary
- Visual direction (specific shots, framing, lighting notes)
- Copy: 3 primary text variants, 3 headline variants, 1 description variant (all validated through Task 6 BETA Check)
- CTA button choice
- Landing page URL with UTM (utm_source=facebook, utm_medium=paid_social, utm_campaign=couples_engraved_test_<concept>)
- Production checklist (what assets are needed, source of each)
- Test plan: which ad set it ships into (the winning ad set), what kill rule applies ($30 spent + 0 purchases, OR CTR <1%, OR no ATC), what success looks like (ROAS >3.0 within $100 spend)

NO PRODUCTION OF ACTUAL ASSETS YET. Briefs only this week. Asset production waits on Amir green-light after reviewing briefs.

**Cut from earlier brainstorm:** engraving close-up (too similar to winner, algorithm will cluster), hand-on-hand (generic lifestyle, doesn't differentiate). Do not produce these.

### Task 8: Aydins Meta Ads operational state file

Same pattern as the existing `(C) Beta Operations State` files for Aydins. Save at:
`/home/openclaw/.openclaw/command-center/work/meta/meta-ads-state-2026-06-02.md`

Captures:
- Account ID, currency, timezone, attribution window
- Active campaign + ad set + ad inventory with current status
- Paused inventory with reason
- Last 30/14/7-day performance per campaign
- Pixel/CAPI status from Task 2
- Open issues + pending Amir decisions
- Active cron jobs related to Meta (Tasks 3 + 4)
- Credential locations (paths only, never contents)
- Hard rules

This becomes the source-of-truth file Beta references on every Meta-related task going forward.

### Task 9: Digest integration

Update the 6:00 AM Central digest to include a Meta section:

```
*Meta Ads Daily - Aydins - <date>*

Delivery health: <OK | FAILURE>
Yesterday: $<spend> | <purchases> purch | <roas> ROAS | <cpa> CPA | <ctr>% CTR
7-day: $<spend> | <purchases> purch | <roas> ROAS | <cpa> CPA
14-day: $<spend> | <purchases> purch | <roas> ROAS | <cpa> CPA

Winner ad set: <name>
  Last 7-day: ROAS <x.xx>, CPA $<xx>, Freq <x.xx>, Learning <status>

Scale-eligible? <YES | NO>
  Conditions: ROAS >3.0 (<actual>), CPA <$75 (<actual>), Freq <3.0 (<actual>), 14d post-restart (<days>)

Pending Amir:
  - <action> on <thing>

Creative pipeline: <count> briefs drafted, <count> awaiting Amir review, <count> approved for production

Tracking health (last check <date>): EMQ <x.x>, Dedup <xx>%, <warnings count> warnings
```

### Task 10: Documentation

Update `/home/openclaw/.openclaw/command-center/agents/beta-meta.md` (create if it does not exist) with the Meta agent prompt. Sections:

- Scope (Aydins Meta Ads only)
- Hard never-do rules (no spend changes, no new live ads, no audience changes, no Pixel config push without Amir approval)
- Output contract (JSON same format as BETA Shop / BETA Google)
- Required brand rules
- Validator chain (Task 6 must pass before Slack post)

## Verification protocol

When Tasks 1-10 are done (or as far as possible without specific creds), report back with:

1. Token rotation receipt path + confirmation timestamp
2. Tracking audit path + 5-line summary + top 3 issues
3. Delivery monitor cron line + first test run result
4. Performance digest cron line + first test run result
5. Catalog Sales post-mortem path
6. BETA Check Meta validator path + rule count
7. Creative briefs folder path + filename list (4 briefs)
8. Meta Ads operational state file path
9. Digest integration confirmation
10. beta-meta.md agent prompt path + md5
11. Cost spent on this task batch (USD)

Post receipts to Slack `#beta-daily` and write full report to `/home/openclaw/.openclaw/command-center/work/meta/meta-stabilization-receipts-2026-06-02.md`.

## Operator delegation framework

Amir's stated context: not a Meta Ads expert, not hiring a freelancer, wants Beta to run the account day-to-day with him as approval-only.

Beta operates as the de-facto Meta Ads manager. Amir is the spend authorizer, not the operator. Translate everything into binary decisions for him. Never ask him to think strategically unless something happens that the playbook does not cover.

### Decision translation rules

Every decision Beta surfaces to Amir must follow this format in Slack:

```
*Meta Ads decision required - <date>*
What: <one sentence>
Why: <one sentence with the number that drove it>
Risk if approved: <one sentence>
Risk if rejected: <one sentence>
Beta's recommendation: <APPROVE | REJECT>
Reply: approve / reject / hold
```

Never give Amir 3 options. Give him a recommendation and a yes/no. If the situation is genuinely ambiguous (rare), say so and pause for direction. Otherwise pick the call and let him reverse it.

### Auto-approved (Beta executes without asking)

- Internal reporting, digest posting, log writing
- Drafting ad copy, creative briefs, audience suggestions (drafts only, not pushes)
- Pulling diagnostics, performance data, tracking audits (read-only)
- Killing an ad in the winning ad set that hits the kill rule ($30 spent + 0 purchases, OR CTR <1% for 48hrs, OR no ATC at $20 spend). Notify Amir same day, do not require pre-approval.
- Catalog Sales stays paused (decision already made, no future approval needed for the next 60 days)

### Requires Amir approval (always)

- Any spend increase or decrease
- Pushing a new creative live to any ad set
- Launching a new campaign, ad set, or audience
- Pixel / CAPI config changes on Shopify
- Revival of Catalog Sales after the 60-day lockout
- Any Advantage+ test launch
- Audience expansion or exclusion change

### Weekly Meta operator brief

Every Monday at 8:00 AM Central, Beta posts a weekly brief to Slack `#beta-daily` titled "Meta Weekly - Aydins - <week ending>". Structure:

```
*Meta Weekly - Aydins - Week ending <date>*

Spend this week: $<x> / $<target>
Purchases: <n>
Revenue: $<x>
ROAS: <x.xx> (<trend vs last week>)
CPA: $<x> (<trend>)
Frequency on winner: <x.xx>

Health:
- Delivery: <OK | INTERRUPTED on <date>>
- Tracking: <EMQ x.x, Dedup xx%, <warnings>>
- Learning Phase: <stable | reset on <date>>

Decisions for Amir this week:
1. <decision in binary format above>
2. <decision in binary format above>
(or "No decisions required this week.")

Beta's read in 2 sentences: <what's happening, what to expect next week>
```

Amir reads this once per week. If there are decisions, he replies yes/no/hold. If there are none, he does nothing.

### Escalation rules

Beta escalates outside the normal cadence (to `#beta-alerts` plus `#beta-daily`) when:

- Account goes dark for more than 6 hours (detected by Task 3 monitor)
- Daily spend deviates more than 30% from target for 2 consecutive days
- 7-day ROAS on winning ad set drops below 1.5
- Pixel / CAPI dedup drops below 60% (broken tracking)
- Any disapproval, policy flag, or account quality drop
- Any payment method failure or billing block

Escalation format same as decision format but tagged `URGENT - Meta`.

### What Beta does NOT bring to Amir

- Tactical questions Beta can answer itself by reading the state file
- "Should I run this report?" type questions (just run it)
- Reframings of decisions already made in Locked Decisions section above
- Speculative strategy questions (Beta drafts a recommendation; only escalates if the recommendation needs spend approval)

The principle: Amir's role is approve / reject / hold. Beta's role is everything else.

## What Amir does next

1. **Today / tomorrow morning:** review the tracking audit Beta posts. Reply approve / reject on any Pixel/CAPI fixes. Highest priority decision.
2. **This week:** review the 4 creative briefs. Reply approve / reject / edit on each. Once approved, give the go-ahead for asset production.
3. **Every morning (after this is live):** glance at the Meta line in the 6am Slack digest. If "OK," do nothing. If "Amir approval required," reply yes/no.
4. **Every Monday:** read the weekly Meta operator brief. If decisions are listed, reply. If not, do nothing.
5. **Always:** "approve" / "reject" / "hold" in Slack `#beta-daily` is the authoritative trigger.

Estimated Amir time on Meta after this is set up: under 30 minutes per week if nothing breaks. Under 10 minutes per week once the creative pipeline stabilizes in month 2.

## Cautions

- Do NOT expose Meta tokens, Pixel access tokens, or System User credentials anywhere outside `/home/openclaw/.openclaw/agents/beta/credentials/` with mode 600.
- Do NOT push any Meta Ads change without explicit Amir approval. DRAFT-ONLY for all spend, creative, audience, and campaign-level changes.
- Do NOT revive Catalog Sales for 60 days even if it looks tempting.
- Do NOT confuse the operator's creative fatigue with audience saturation. Winner is at 2.29 freq, audience has runway.
- Do NOT skip Task 2 (tracking audit). It is the highest free leverage in the account and gates the value of every other task.

End of prompt. Execute setup tasks 1-10, post receipts.
