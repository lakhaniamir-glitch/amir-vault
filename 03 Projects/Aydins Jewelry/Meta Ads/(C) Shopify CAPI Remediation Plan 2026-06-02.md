# Shopify Pixel and CAPI Remediation Plan - Aydins - 2026-06-02

Status: draft only
Mode: read-only review completed
No Shopify changes executed
No Pixel config writes executed
No Meta live ad changes executed

## Executive summary

Aydins is using Shopify-managed web pixel infrastructure plus Shopify server-side event relay for Pixel and CAPI events. I did not find hard-coded Pixel snippets in the published theme scan, and the active script tags are not Pixel related.

The main tracking problem is not duplicate theme code. The problem is weak event match quality on upper-funnel and cart events, plus below-benchmark CAPI coverage for ViewContent.

Current Events Manager state:

| Signal | Current | Target | Status |
|---|---:|---:|---|
| Purchase EMQ | 8.0/10 | 8.0+ | Pass |
| AddToCart EMQ | 5.1/10 | 7.0+ | Fail |
| ViewContent EMQ | 5.2/10 | 6.0+ | Fail |
| ViewContent CAPI coverage | 71% | 75%+ | Fail |

Current match parameter state:

| Parameter | Current | Target recommendation |
|---|---|---|
| Email | On | Keep On |
| First and last name | On | Keep On |
| Phone | Off | Turn On if collected and hashed by integration |
| City, State, ZIP or Postal Code | Off | Turn On if collected and hashed by integration |
| Country | Off | Turn On if collected and hashed by integration |
| External ID | Off | Turn On if stable Shopify customer ID or equivalent is supported |
| Gender | Off | Keep Off unless Amir explicitly accepts privacy risk |
| Date of birth | Off | Keep Off unless Amir explicitly accepts privacy risk |

Recommendation: enable the low-risk match parameters first: phone, city/state/ZIP, country, and external ID. Keep gender and date of birth off for now unless there is a clear business need and privacy review.

## What is owning the Pixel today

### Primary owner

Shopify-managed web pixel plus Shopify server-side event relay.

### Evidence

1. Storefront HTML contains Shopify `webPixelsManager` configuration.
2. Storefront HTML contains app pixel configuration for Pixel ID `1151493648281503`.
3. Storefront HTML contains Shopify server-side event relay configuration with CAPI enabled.
4. Events Manager settings show Dataset ID `1151493648281503`, owner Aydins Jewelry, connected ad account `23304577`.
5. Published theme scan checked 63 relevant assets and found no hard-coded Pixel ID, no direct `fbq` snippet, and no direct events script override.
6. Shopify script tags list has three storefront scripts and none are Pixel related.
7. The Beta custom Shopify app does not own a web pixel.

### Unknowns

The available Shopify Admin token cannot enumerate installed app names because the `appInstallations` query is access denied. That means I cannot fully prove whether another installed app exists from the app list alone. Storefront and Events Manager evidence still point to Shopify-managed pixel ownership.

Snapshot path:

`/home/openclaw/.openclaw/command-center/work/meta/shopify-pixel-current-state-2026-06-02.json`

Raw read-only evidence:

- `/home/openclaw/.openclaw/command-center/work/meta/shopify-pixel-readonly-raw-2026-06-02.json`
- `/home/openclaw/.openclaw/command-center/work/meta/storefront-pixel-parsed-2026-06-02.json`
- `/home/openclaw/.openclaw/command-center/work/meta/tracking-audit-2026-06-02.md`

## Exact click-by-click remediation paths

### Path A: Shopify native sales channel data-sharing level

Use this path first to confirm the integration is already at maximum sharing level. If it is not, this is likely the highest-leverage Shopify-side fix.

1. Shopify Admin.
2. Settings.
3. Apps and sales channels.
4. Open the native social sales channel connected to Pixel `1151493648281503`.
5. Settings.
6. Data sharing settings.
7. Confirm Customer data-sharing is set to the highest available level, usually Maximum.
8. Confirm the selected Pixel or Dataset is `1151493648281503`.
9. Confirm both browser Pixel and server-side CAPI are active.
10. If the level is not Maximum, change to Maximum only after Amir approves execution.

Current state:

- Storefront evidence shows Shopify server-side event relay is active.
- Events Manager shows integrations as CAPI plus Pixel.
- Exact Shopify UI data-sharing level was not visible through Admin API.

Target state:

- Highest available data-sharing level.
- Pixel `1151493648281503` selected.
- CAPI enabled.

### Path B: Shopify Customer events check

Use this path to confirm there is no competing custom pixel or duplicate Meta pixel.

1. Shopify Admin.
2. Settings.
3. Customer events.
4. Check App pixels.
5. Look for the app pixel connected to Pixel `1151493648281503`.
6. Confirm it is active.
7. Check Custom pixels.
8. Confirm there is no custom hard-coded Pixel using `1151493648281503`.
9. Do not disconnect, delete, or edit anything during review.

Current state:

- Storefront shows Shopify app pixel for `1151493648281503`.
- Beta custom app has no owned web pixel.
- Theme scan found no hard-coded override.

Target state:

- One active Shopify-managed app pixel for `1151493648281503`.
- No duplicate custom pixel for the same ID.

### Path C: Events Manager automatic matching parameter toggles

These are the individual customer match parameters currently visible as off in Events Manager. If Shopify does not expose individual toggles, this is where the parameter switches are most likely controlled.

1. Business tools.
2. Events Manager.
3. Data sources.
4. Select Pixel or Dataset `1151493648281503`.
5. Settings.
6. Website settings.
7. Find Automatic website matching.
8. Click Show customer information parameters.
9. Keep Email On.
10. Keep First and last name On.
11. Turn Phone number On.
12. Turn City, State, ZIP or Postal Code On.
13. Turn Country On.
14. Turn External ID On if the integration sends stable customer IDs.
15. Leave Gender Off unless separately approved.
16. Leave Date of birth Off unless separately approved.
17. Save only after Amir approval.

Current state to target state:

| Parameter | Current | Target |
|---|---|---|
| Phone | Off | On |
| City, State, ZIP or Postal Code | Off | On |
| Country | Off | On |
| External ID | Off | On if available from Shopify integration |
| Gender | Off | Hold |
| Date of birth | Off | Hold |

### Path D: ViewContent CAPI coverage check

This targets the 71% ViewContent CAPI coverage issue.

1. Events Manager.
2. Data sources.
3. Select Pixel or Dataset `1151493648281503`.
4. Overview.
5. Click View details on the high-priority CAPI coverage recommendation.
6. Confirm event shown is ViewContent.
7. Confirm current coverage is still 71% or similar.
8. Go back to Shopify native channel Data sharing settings.
9. Confirm maximum data sharing and CAPI are active.
10. If already maximum, document that coverage may require partner integration support or waiting 24 to 72 hours after parameter changes.

Current state:

- ViewContent CAPI coverage 71%.

Target state:

- 75% or higher.

## Expected EMQ lift per parameter

These are rough estimates based on Meta matching patterns. Actual lift depends on whether Shopify can pass the value on the event type and whether the visitor is logged in, checking out, or anonymous.

| Parameter | Expected lift | Best affected events | Notes |
|---|---:|---|---|
| Phone | +0.5 to +1.5 EMQ | AddToCart, InitiateCheckout, Purchase | Strong match key when collected. May not help anonymous ViewContent much. |
| City, State, ZIP or Postal Code | +0.2 to +0.8 EMQ | AddToCart, InitiateCheckout, Purchase | Useful supporting match signal. |
| Country | +0.1 to +0.3 EMQ | All events with location context | Low risk, modest lift. |
| External ID | +0.3 to +1.0 EMQ | Customer and checkout events | Strong if stable and consistently sent. |
| Gender | +0.0 to +0.3 EMQ | Limited | Not recommended now due privacy sensitivity and likely low availability. |
| Date of birth | +0.0 to +0.3 EMQ | Limited | Not recommended now due privacy sensitivity and likely low availability. |

Expected practical outcome:

- AddToCart could plausibly move from 5.1 toward 6.0 to 7.0 if phone and geography are available at cart or checkout stages.
- ViewContent may improve less because many product views are anonymous. ViewContent CAPI coverage improvement may matter more than match params alone.
- Purchase is already at 8.0, so the goal is to protect it, not aggressively change it.

## Risk per change

| Change | Risk | Notes |
|---|---|---|
| Phone On | Low to medium | Must be hashed and handled through approved integration. More sensitive than email. |
| City, State, ZIP On | Low to medium | Location data is personal data. Confirm privacy policy covers ad measurement and marketing use. |
| Country On | Low | Broad location signal, generally lower sensitivity. |
| External ID On | Medium | Must be stable, pseudonymous, and not expose raw customer data. |
| Gender On | Medium to high | Sensitive profiling risk. Not recommended without privacy review. |
| Date of birth On | High | Sensitive personal data. Not recommended without privacy review. |
| Maximum data sharing in Shopify | Medium | Reversible, but increases data sent for ad measurement. Confirm privacy notice and consent posture. |
| Domain allowlist changes | Low to medium | Wrong allowlist can block valid events or allow noisy preview events. Review before changing. |

Privacy note:

Before execution, confirm the privacy policy and cookie consent posture cover marketing measurement, hashed customer matching, server-side event sharing, and opt-out mechanisms where required. Texas is the home base, but the store sells nationally, so the operational posture should account for stricter state privacy regimes as a baseline.

## Verification plan

### Immediately after execution

1. Screenshot the final Shopify data-sharing screen.
2. Screenshot Events Manager Settings showing updated customer information parameters.
3. Confirm Pixel ID remains `1151493648281503`.
4. Confirm no duplicate custom pixel was created.
5. Confirm no campaign, ad set, or ad creative settings changed.

### 24 to 72 hours later

1. Events Manager.
2. Data sources.
3. Pixel or Dataset `1151493648281503`.
4. Overview.
5. Record EMQ for:
   - Purchase
   - AddToCart
   - ViewContent
   - InitiateCheckout
6. Open the CAPI coverage recommendation and record ViewContent coverage.
7. Open Diagnostics and record whether domain and CAPI tasks remain.
8. Confirm Purchase EMQ did not fall below 8.0.
9. Confirm AddToCart moves toward 7.0.
10. Confirm ViewContent moves toward 6.0 and CAPI coverage moves toward 75%.

### Success criteria

- Purchase EMQ stays at or above 8.0.
- AddToCart EMQ improves from 5.1 toward 7.0.
- ViewContent EMQ improves from 5.2 toward 6.0.
- ViewContent CAPI coverage improves from 71% toward 75%.
- No new diagnostics warnings appear.
- No Account Quality issues appear.

## Rollback plan

If EMQ does not improve after 72 hours, or if diagnostics get worse:

1. Return to Events Manager Settings.
2. Open Automatic website matching customer information parameters.
3. Turn off the last parameter enabled first.
4. Suggested rollback order:
   - External ID
   - Phone
   - City, State, ZIP or Postal Code
   - Country
5. If Shopify data-sharing level was changed, return it to the prior level.
6. Re-check Events Manager after 24 to 72 hours.
7. Keep screenshots before and after rollback.

Do not roll back Email or First and last name because they were already on and Purchase EMQ is at target.

## Execution recommendation

Approve execution of the safe subset only:

- Phone On
- City, State, ZIP or Postal Code On
- Country On
- External ID On if Shopify integration supports stable hashed customer ID

Do not enable yet:

- Gender
- Date of birth

Reason:

The safe subset targets AddToCart and ViewContent EMQ without adding high-sensitivity attributes. Gender and date of birth have lower expected lift and higher privacy risk.
