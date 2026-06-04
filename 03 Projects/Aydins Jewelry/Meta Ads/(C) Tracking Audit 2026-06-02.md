# Aydins Meta Pixel, CAPI, EMQ Tracking Audit - 2026-06-02

Status: browser audit completed through cookie session deep-link bypass
Mode: read-only browser session
Account: act_23304577
Dataset and Pixel: Amir Lakhani's Pixel, ID 1151493648281503
Business: Aydins Jewelry, ID 229198364454380
Audit window shown in Events Manager: May 5, 2026 to Jun 1, 2026
Audit completed: 2026-06-02 20:24 UTC

No spend changes, live ad changes, Pixel config writes, Submit clicks, Save clicks, or Confirm clicks were made.

## Session result

Cookie session was valid. Business Suite home showed an onboarding or verification overlay, but deep-link bypass succeeded.

Successful deep URL:

`https://business.facebook.com/events_manager2/list/pixel/1151493648281503/overview`

Browser capture evidence:

- Bypass result: `/home/openclaw/.openclaw/command-center/work/meta/meta-browser-bypass-result-2026-06-02.json`
- Text capture: `/home/openclaw/.openclaw/command-center/work/meta/meta-browser-text-capture-2026-06-02.json`
- Clean event table text: `/home/openclaw/.openclaw/command-center/work/meta/meta-overview-table-clean-text.txt`

## Screenshots captured

Folder:

`/home/openclaw/.openclaw/agents/beta/screens/meta-audit-2026-06-02/`

Key screenshots:

- `deep-01-https-business-facebook-com-events-manager2-list-pixel-1151493648281503-overview.png`
- `events-overview.png`
- `events-overview-table-clean.png`
- `events-diagnostics.png`
- `overview-view-details-capi-quality.png`
- `events-test-events.png`
- `events-settings.png`
- `events-history.png`
- `events-aem-guess-1.png`
- `events-aem-guess-2.png`
- `account-quality.png`
- `account-quality-settings.png`

## Requested signal table

| Signal | Target | Result | Status |
|---|---:|---:|---|
| EMQ score for Purchase | 8.0+ | 8.0/10 | Pass, exactly at target |
| EMQ score for AddToCart | 7.0+ | 5.1/10 | Fail |
| EMQ score for ViewContent | 6.0+ | 5.2/10 | Fail |
| Pixel plus CAPI dedup rate | 90%+ | Exact dedup rate not visible in UI capture | Blocked in UI |
| CAPI coverage proxy | 75%+ | ViewContent CAPI coverage 71% | Fail |
| AEM Purchase priority | 1 | Not visible. AEM deep links did not expose priority table. | Blocked in UI |
| Test Events Purchase fires from Pixel and CAPI with matching event_id | Yes | Test Events tab accessible, no test events shown without initiating a new event | Not tested |
| Diagnostics warnings on Purchase, ATC, IC, VC | None | Diagnostics show high-priority CAPI and domain tasks. InitiateCheckout has CAPI reporting note. | Fail |
| Account Quality flags from dark period | None | Account Quality shows no account or asset issues in last 30 days | Pass |

## Event activity and EMQ details

From Events Manager event table:

| Event | Status | Integration | EMQ | Total events | Last received |
|---|---|---|---:|---:|---|
| ViewContent | Active | Multiple | 5.2/10 | 507.1K | 27 to 30 minutes ago |
| AddToCart | Active | Multiple | 5.1/10 | 1.6K | 36 to 39 minutes ago |
| InitiateCheckout | Active | Multiple | 5.9/10 | 912 | 33 to 37 minutes ago |
| Purchase | Active | Multiple, used by 5 ad sets | 8.0/10 | 288 | 1 hour ago |
| PageView | Active | Multiple | 5.4/10 | 535.1K | 27 to 30 minutes ago |
| AddPaymentInfo | Active | Multiple | 7.4/10 | 248 | 32 to 35 minutes ago |

Purchase EMQ is acceptable. Upper-funnel and cart events are weak.

## Diagnostics and quality findings

### 1. Low CAPI coverage for ViewContent

Events Manager says:

- Affected ad spend: $101
- Recommendation: improve rate of Meta Pixel events covered by Conversions API
- Event detail: ViewContent
- CAPI coverage: 71%
- Goal: at least 75%
- Potential outcome: 62.9% lower cost per result
- Recommended fix shown: improve deduplication keys for Meta Pixel and Conversions API events

### 2. Low EMQ for AddToCart and ViewContent

Current EMQ:

- AddToCart: 5.1/10, target 7.0+
- ViewContent: 5.2/10, target 6.0+

Settings show automatic website matching is on, but several customer information parameters are off:

- Email: On
- Phone number: Off
- First and last name: On
- Gender: Off
- City, State, ZIP or Postal Code: Off
- Country: Off
- Date of birth: Off
- External ID: Off

This likely limits match quality on non-purchase events.

### 3. Domains need confirmation or allowlist review

Diagnostics show `Confirm domains that belong to you`.

Visible affected domains include temporary preview domains:

- `964aajrft9hdpsyrqm7j1hvgpqzs5mp-18578135.shopifypreview.com`
- `m40cuogka8obqip76je34paz7n1421a-18578135.shopifypreview.com`
- `n2vnv85ilbik7j94ppjmnate3be658t-18578135.shopifypreview.com`
- `qvsdu0kxa764btx0wqum23rb4rxt2x5-18578135.shopifypreview.com`

UI says `See All 6`, detected Jun 2, 2026.

### 4. Custom events need confirmation

Overview shows:

`Confirm custom event(s) that belong to you`

Meta notes custom events cannot be used with ad features until confirming they belong to the business and follow terms.

No confirmation was clicked.

### 5. InitiateCheckout CAPI reporting note

Diagnostics show:

- `You saw more reported conversions by using the Conversions API alongside the Meta Pixel`
- In the last 7 days, Meta says 0% more conversions were reported for InitiateCheckout events by using CAPI alongside Pixel.

This suggests CAPI is connected, but incremental reporting on InitiateCheckout is not adding value right now.

### 6. Test Events status

Test Events tab is accessible. It shows instructions to select a marketing channel to receive corresponding test instructions. No live test event was sent, and no event status was visible without initiating a new event.

### 7. Account Quality

Account Quality page shows:

- Recent account issues, last 30 days: no account or asset issues
- No visible restrictions
- No visible payment or policy block
- Status visible in text capture: Active

This supports the working theory that the dark period was delivery or configuration related, not an account quality enforcement issue.

## Severity-ranked fixes

### Critical: Raise AddToCart EMQ and ViewContent EMQ

Finding:

- AddToCart EMQ is 5.1/10 versus target 7.0+
- ViewContent EMQ is 5.2/10 versus target 6.0+

Exact remediation, not executed:

1. In Shopify Facebook and Instagram channel or the active Pixel/CAPI integration, review advanced matching settings.
2. Confirm that all legally allowed customer match parameters are enabled and being passed where available.
3. Prioritize phone, city, state, ZIP or postal code, country, and external ID if Shopify or the integration can pass them hashed.
4. Confirm server events include `fbp`, `fbc`, event time, event name, action source, user agent, client IP where allowed, and consistent event IDs.
5. Re-check EMQ after 24 to 72 hours.

Estimated impact:

High. Better EMQ should improve match rate, attribution quality, retargeting pool quality, and Meta optimization signal. It is the most direct tracking-quality problem found.

Approval required:

Yes. This may require Shopify Pixel/CAPI integration changes.

### High: Improve ViewContent CAPI coverage from 71% to at least 75%

Finding:

Events Manager flags ViewContent CAPI coverage at 71%, below the 75% goal. Meta estimates 62.9% lower cost per result for advertisers at the 75% coverage benchmark. Affected ad spend shown: $101.

Exact remediation, not executed:

1. Audit whether all ViewContent browser events also send corresponding server events.
2. Confirm product page views from Shopify theme, apps, and collection navigation are covered by CAPI.
3. Confirm Pixel and CAPI use matching `event_id` for ViewContent.
4. Fix missing server-side coverage through the Shopify channel or approved CAPI integration.
5. Re-check coverage after data refresh.

Estimated impact:

High. This is directly called out by Events Manager as high priority and may improve reporting accuracy and optimization quality.

Approval required:

Yes. This may require Shopify or integration configuration changes.

### High: Review and allowlist legitimate domains, remove or ignore preview noise

Finding:

Diagnostics show six domains recently started sending data, including temporary `shopifypreview.com` domains.

Exact remediation, not executed:

1. Open the Review domains flow in Events Manager.
2. Confirm `shopaydins.com` is allowed.
3. Review the six preview domains.
4. If they are only Shopify theme preview domains, do not add them as permanent production domains unless needed.
5. If any legitimate domain is missing from the allowlist, add it after Amir approval.

Estimated impact:

Medium. This reduces noisy diagnostics and prevents unwanted domains from polluting event quality.

Approval required:

Yes if any allowlist or blocklist setting is changed.

### Medium: Confirm custom events that belong to Aydins

Finding:

Overview shows a task to confirm custom events before they can be used with ad features.

Exact remediation, not executed:

1. Open Review events in Events Manager.
2. Document the custom event names and sources.
3. Confirm only events that belong to Aydins and follow Meta terms.
4. Do not confirm unknown app, preview, or test events.

Estimated impact:

Medium. May unlock useful custom events for ad features and reduce account tasks.

Approval required:

Yes. Confirmation changes event governance.

### Medium: AEM priority still needs manual verification

Finding:

AEM priority order was not visible through available browser deep links. Purchase priority 1 could not be confirmed.

Exact remediation, not executed:

1. Manually open Events Manager domain web event configuration or Aggregated Event Measurement from the UI.
2. Screenshot the event priority order.
3. Confirm Purchase is priority 1.
4. If Purchase is not priority 1, prepare a separate decision request before changing it.

Estimated impact:

Medium. Purchase priority protects attribution and optimization under privacy-limited traffic.

Approval required:

Yes for any AEM change.

## Top 3 issues for Amir

1. AddToCart and ViewContent EMQ are below target: 5.1/10 and 5.2/10.
2. ViewContent CAPI coverage is 71%, below the 75% benchmark, with Meta estimating 62.9% lower cost per result at the benchmark.
3. Diagnostics show domain confirmation tasks for six recently detected domains, including temporary preview domains.

## Decision needed

*Meta Ads decision required - 2026-06-02*
What: Approve a read-only Shopify Pixel/CAPI configuration review and draft remediation plan for low EMQ and low CAPI coverage.
Why: AddToCart EMQ is 5.1/10, ViewContent EMQ is 5.2/10, and ViewContent CAPI coverage is 71% versus the 75% benchmark.
Risk if approved: Low, review is read-only and any actual config change will come back for separate approval.
Risk if rejected: Meta keeps optimizing with weak upper-funnel and cart event quality.
Beta's recommendation: APPROVE
Reply: approve / reject / hold
