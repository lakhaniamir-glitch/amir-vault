# Aydins Meta Ads Operational State - 2026-06-02

Status: source of truth for Beta Meta operations
Owner: Beta
Business: Aydins Jewelry
Mode: operator managed, Amir approval-only

## Account and asset IDs

| Item | Value | Status |
|---|---|---|
| Meta ad account | `act_23304577` | Known, API blocked pending App Review |
| Active campaign | `1|AY|6.3|Couples engraved| - 30` | Live, protected |
| Active campaign ID | `6929192369326` | Known |
| Protected winner ad set | `1|AY|6.3|Couples engraved| - 30|*|All mobile devices|1|US` | Do not edit |
| Protected winner ad | `Single image|3` | Do not edit |
| Paused Gym Images ad set | `1|AY|6.29|Gym Images| - 30|*|All mobile devices|2|US` | Paused, keep paused |
| Catalog Sales campaign ID | `52566193429730` | Paused, 60-day lockout |
| Pixel candidate | `1151493648281503` | Found in storefront source, API access blocked |
| Aydins Business ID visible to token | `229198364454380` | Visible via business_management |

## Current performance anchors

Protected winner baseline from handoff:

- ROAS: 5.44
- CPA: $78.69
- CTR: 2.45%
- Frequency: 2.29

Catalog Sales final state:

- 30-day spend: $536.53
- 30-day purchases: 6
- 30-day ROAS: 2.09
- 30-day frequency: 9.21
- 30-day CPM: $26.49
- 14-day ROAS: 1.16
- 14-day CPA: $126.24
- 14-day frequency: 5.04
- Root cause: retargeting pool too small at about 827 Meta LPV/month

## Locked decisions

1. Active Couples Engraved campaign stays live at $50/day.
2. Protected winner ad set and `Single image|3` ad are not touched.
3. Gym Images ad set stays paused.
4. Catalog Sales stays paused for 60 days minimum from 2026-06-02.
5. No budget increase for 14 days.
6. No new ad sets for 14 days.
7. New creatives, after approval, go into the existing winning ad set.
8. Advantage+ Shopping is not considered for 30 days.

## Credential paths

Never expose credential contents.

| Path | Purpose | Current status |
|---|---|---|
| `/home/openclaw/.openclaw/agents/beta/credentials/meta.env` | Existing Meta token file | Present, but lacks Marketing API scopes |
| `/home/openclaw/.openclaw/agents/beta/credentials/meta-ads.env` | Desired Meta ads credential file | Missing as of latest check |
| `/home/openclaw/.openclaw/agents/beta/google/ga4-oauth-token.json` | GA4 OAuth token | Present, used for proxy monitor |
| `/home/openclaw/.openclaw/agents/beta/google/ga4-oauth-client.json` | GA4 OAuth client | Present |
| `/home/openclaw/.openclaw/command-center/.env` | Slack bot/channel config | Present |

## Token and App Review status

Meta App Review submitted by Amir on 2026-06-02.

Pending scopes:

- `ads_read`
- `ads_management`
- `read_insights`

Expected approval window: 3 to 7 days.

Current VPS token scopes visible through `/me/permissions`:

- `business_management`
- `pages_show_list`
- `instagram_basic`
- `instagram_content_publish`
- `pages_read_engagement`
- `public_profile`

Current scope gaps:

- Missing `ads_read`, so ad account reads fail.
- Missing `read_insights`, so performance reporting via Meta API fails.
- Missing `ads_management`, so write access is unavailable and should stay unused without approval.
- Pixel/Dataset `1151493648281503` returns `Missing Permission` for stats and metadata.

## Task status

| Task | Status | Notes |
|---|---|---|
| Task 1 token rotation | Blocked | Waiting on App Review and fresh approved token |
| Task 2 tracking audit | Blocked partial | Storefront pixel evidence collected, Events Manager signals blocked |
| Task 3 Meta API delivery monitor | Blocked | Requires `ads_read` or `read_insights` |
| GA4 proxy delivery monitor | Complete | Runs daily at 7:00 AM Central as interim blackout check |
| Task 4 Meta performance digest | Blocked | Requires `read_insights` |
| Task 5 Catalog Sales post-mortem | Complete | Filed |
| Task 6 BETA Check Meta validator | Complete | 15 rules |
| Task 7 creative briefs | Complete draft-only | 4 briefs, validator pass |
| Task 8 state file | Complete | This file |
| Task 9 digest integration | Pending | Can integrate proxy line now, full Meta section waits for API scopes |
| Task 10 beta-meta prompt | Complete | Agent prompt created |

## Active operational checks

GA4 proxy monitor cron:

`0 12 * * * cd /home/openclaw/.openclaw && node /home/openclaw/.openclaw/command-center/scripts/meta_delivery_proxy_check.mjs >> /home/openclaw/.openclaw/logs/meta_delivery_proxy_check.log 2>&1`

Rule: if GA4 Paid Social sessions are 0 for 2 consecutive days, hard alert Slack `#beta-alerts` and `#beta-daily` with Meta delivery probable failure.

Latest test run:

- Date tested: 2026-06-01
- Paid Social sessions: 12
- Status: OK

## Hard never-do rules

- No spend changes without Amir approval.
- No live ad pushes without Amir approval.
- No audience changes without Amir approval.
- No campaign or ad set edits without Amir approval, except pre-approved kill rules when active.
- No Pixel/CAPI Shopify config writes without Amir approval.
- No Catalog Sales revival before the 60-day lockout review.
- No Advantage+ launch until the locked revisit window.
- No em dashes in ad copy or operator posts.
- No bare `lifetime warranty`; use `Aydins Lifetime Warranty`.
- No supplier or third-party brand names in customer-facing ad copy.
- No `handcrafted`, `handmade`, or `forged` claims.
- All draft ad copy must pass BETA Check Meta before Slack review.

## Current pending Amir decision

*Meta Ads decision required - 2026-06-02*
What: Wait for App Review approval, then install a fresh approved Beta System User token for Meta API access.
Why: Current token lacks `ads_read`, `read_insights`, and Pixel/Dataset stats access, blocking Tasks 1 to 4.
Risk if approved: Low credential handling risk if stored mode 600 and old token is revoked.
Risk if rejected: Beta remains blind to Meta delivery, EMQ, dedup, AEM, diagnostics, and performance.
Beta's recommendation: APPROVE
Reply: approve / reject / hold
