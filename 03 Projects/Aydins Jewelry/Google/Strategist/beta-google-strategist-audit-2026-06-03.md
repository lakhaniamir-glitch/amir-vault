# BETA GOOGLE STRATEGIST AUDIT 2026-06-03

**Account**: Aydins Jewelry (shopaydins.com) | **Audit Date**: 2026-06-03  
**MC ID**: 122065428 | **GA4 Property**: 317174854  
**Revenue**: $40K CY (2023) | **Target**: $0K/month  
**AOV**: $100-$1,000 (mens wedding bands)

---

## CREDENTIAL STATUS

| Surface | Status | Severity | Action Required |
|---------|--------|----------|-----------------|
| Merchant Center API | WORKING | OK | Service account `beta-agent@...` authenticated |
| GA4 OAuth Token | EXPIRED | CRITICAL | Refresh token expired at ~1.67h; needs new OAuth flow |
| Google Ads API | NOT SET UP | CRITICAL | No developer token, no credentials file. See phase3 checklist |
| Google Search Console API | NOT CONFIGURED | CRITICAL | Service account has no GSC access. Needs OAuth with webmasters.readonly scope |

---

## SECTION 1: MERCHANT CENTER AUDIT

### 1.1 Feed Health

| Metric | Value | Source |
|--------|-------|--------|
| Total products estimated | 12,500 | Phase 3 checkpoint (2026-05-12) |
| Approved (Shopping) | 3,418 (27.3%) | Phase 3 checkpoint |
| Disapproved | 9,082 (72.7%) | Phase 3 checkpoint |
| Pending | 40 | Phase 3 checkpoint |

### 1.2 Disapproval Reasons (Grouped)

| Issue Category | Est. Count | Severity | Servability |
|----------------|-----------|----------|-------------|
| Missing age group | 1,496 | Critical | Demoted |
| Missing color | 1,629 | Critical | Demoted |
| Missing gender | 1,496 | Critical | Demoted |
| Mismatched currency in shipping | 914 | Critical | Unaffected |
| Missing shipping for country | 178 | Warning | Disapproved (KR) |
| Invalid currency for country | 176 | Warning | Disapproved (KR) |
| Image too small / low quality | 251 | Warning | Unaffected |
| Landing page error | 293 | Critical | Disapproved |
| Missing product price | 202 | Critical | Disapproved |
| Image link broken | 49 | Warning | Unaffected |
| Missing unit pricing measure | 178 | Warning | Unaffected |
| Price mismatch / appealed | 13 | Warning | Disapproved / Pending |
| Identity & belief policy | 4 | Critical | Disapproved |

### 1.3 Account-Level Issues

Account status check returned **no account-level issues** and **no website status** from API.  
The `accountstatuses().get()` API returns null for websiteStatus, suggesting the endpoint is not fully serving this account or requires additional permissions.

### 1.4 Feed Quality Analysis

**Title Length**: Titles follow pattern `PRODUCT_NAME | Description | Aydins - Aydins Jewelry`.  
Most titles are adequate length (50-120 chars) but some may exceed Google limits (150 chars for Shopping).

**Description Quality**: 498 products have `text_value_truncated` errors on descriptions, indicating some descriptions exceed Google's length limit.

**Image Quality**:
- 169 products flagged `image_too_small_for_high_resolution` (upcoming enforcement)
- 161 products flagged `image_too_small`
- 90 products flagged `low_image_quality`
- 8 products with image_link_broken
- 41 products with image_link_broken in additional_image_link

**Attributes Coverage**:
- 68% of sampled products missing age group, color, or gender
- Shipping configuration has currency mismatches across 914 products
- Product weight missing for some products
- UTF-8 encoding errors in descriptions (28 products)

### 1.5 Program Status

| Program | Status | Notes |
|---------|--------|-------|
| Free Listings | State: null | API method not available or requires additional permissions |
| Shopping Ads | State: null | API method not available |
| Regions | Empty | No regional configurations found |

### 1.6 Prior 14 Pending MC Removals

**Cannot verify via API** - requires MC UI check or prior checkpoint reference.  
The Phase 3 disapproval report (dated 2026-05-12) identified 1,480 products needing fixes.  
Status of the 14 pending removals from prior work is unknown from API alone.

### 1.7 Shopping Performance Report

**NOT AVAILABLE** - The Content API v2.1 reports().search() endpoint returned:
- `product_view`, `product_performance_view`, `price_performance_view` all rejected as invalid table names
- Performance data requires either: (1) Google Ads API access, or (2) the Shopping Performance Center in MC UI

---

## SECTION 2: GOOGLE ADS AUDIT

### STATUS: UNAVAILABLE

Google Ads API credentials have **not been set up**. No developer token, no OAuth refresh token, no customer ID are available.

**Setup prerequisites from phase3 checklist**:
- [ ] Apply for developer token at ads.google.com/aw/apicenter (Basic tier)
- [ ] Create/reuse OAuth 2.0 credentials in Google Cloud project
- [ ] Run OAuth with scope adwords
- [ ] Note Google Ads customer ID (XXX-XXX-XXXX format)
- [ ] Create google-ads.env with developer token, refresh token, client ID, secret, customer ID

**Pending tasks when Ads API activates**:
1. Audit Tier 2 negative keywords applied to PMax campaigns
2. Audit paused Holiday-Sales-Search campaign
3. Evaluate branded search campaign need

---

## SECTION 3: GOOGLE ANALYTICS 4 AUDIT

### STATUS: DATA UNAVAILABLE

GA4 OAuth token refresh **failed**. Token was refreshed at 2026-06-02 19:13 UTC and the refresh token had a 1.67-hour expiry (6,029 seconds), which has since expired.

**Error**: `invalid_grant - Token has been expired or revoked`

**Action Required**: Run a fresh OAuth 2.0 flow with `https://www.googleapis.com/auth/analytics.readonly` scope to generate a new refresh token.

### What Would Be Audited (Template Ready)

When token is restored, the following reports are pre-configured in `/tmp/pull_ga4_comprehensive.js`:

| Report | Dimensions | Metrics | Purpose |
|--------|-----------|---------|---------|
| Traffic by channel | sessionDefaultChannelGroup | sessions, users, purchases, revenue | Channel mix analysis |
| Device performance | deviceCategory | sessions, users, purchases, revenue | Mobile vs desktop split |
| Top landing pages | landingPagePlusQueryString | sessions, purchases, revenue, CVR | Where conversions happen |
| Funnel counts | eventName (filtered) | eventCount, totalUsers | ViewItem to Purchase drop-off |
| Funnel by channel | channelGroup + eventName | eventCount | Where each channel drops |
| Demographics age | userAgeBracket | users, sessions, purchases | Audience age |
| Demographics gender | userGender | users, sessions, purchases | Audience gender |
| Geo performance | country | sessions, purchases, revenue | Country-level ROI |
| Bottom products | landingPagePlusQueryString | sessions, purchases, CVR, revenue | High traffic, low CVR |

---

## SECTION 4: GOOGLE SEARCH CONSOLE AUDIT

### STATUS: CONFIGURED BUT NO ACCESS

Search Console API was tested with the service account. The token was obtained successfully but the sites list returned empty `{}`.

**Root cause**: The service account `beta-agent@...` has not been granted access to the Search Console property `scod` (shopaydins.com).

**Action Required**:
1. Add `beta-agent@amirs-command-center.iam.gserviceaccount.com` as an owner or restricted user in Google Search Console for `https://shopaydins.com`
2. Enable the Search Console API in Google Cloud Console if not already enabled

**What would be audited (when access is granted)**:

| Area | Purpose |
|------|---------|
| Indexation status | Indexed vs excluded vs error counts |
| Sitemap status | Last crawl, submitted vs indexed |
| Top 50 queries | Impressions, clicks, CTR, position |
| Top 50 landing pages | Clicks and conversions |
| Core Web Vitals | LCP, INP, CLS by page group |
| Mobile usability | Issues per page |
| Coverage errors | 404s, soft 404s, server errors |
| Rich results | Schema markup status |

---

## SECTION 5: PRIOR PHASE 3 WORK STATUS

### Completed (as of 2026-05-12):
- Merchant Center audit of ~2,500 products
- Identified 1,480 products needing attribute fixes
- Generated fix pipeline plan (Weeks 1-3)
- SEO opportunities documented

### Still Pending:
- Attribute fixes not yet applied (color, age group, gender)
- Shipping currency mismatches not corrected
- Image quality issues not addressed
- Google Ads API setup not completed
- GSC access not granted
- GA4 token re-auth not done

---

## SECTION 6: DATA GAPS SUMMARY

| Data Point | Available | Workaround |
|------------|-----------|------------|
| MC feed health (product counts) | Yes (checkpoint) | Use checkpoint from Phase 3 |
| MC disapproval reasons | Yes (checkpoint) | Use checkpoint from Phase 3 |
| MC performance data | No | Grant Ads API or use MC UI reports |
| Google Ads campaign structure | No | Set up Ads API, provide customer ID |
| Google Ads keywords / QS | No | Set up Ads API |
| GA4 traffic data | No | Run fresh OAuth flow |
| GSC index / queries / CWV | No | Add service account to GSC |
| Organic CTR benchmarks | Partially | Industry-level data from WordStream |

---

## SECTION 7: CRITICAL FLAGS

| Flag | Type | Detail |
|------|------|--------|
| GA4 OAuth expired | CRITICAL | Need fresh OAuth flow. 24h stale. |
| Google Ads API not set up | CRITICAL | No developer token. Blocking all Ads audit. |
| GSC not accessible | CRITICAL | Service account needs GSC owner permission. |
| 72.7% feed disapproval rate | CRITICAL | 9,082 of ~12,500 products disapproved or demoted. |
| Missing attributes | CRITICAL | ~1,600 products missing color, age group, gender. |
| Prior fixes not applied | WARNING | Phase 3 fix plan (2026-05-12) still unexecuted. |
| 4 identity/belief violations | CRITICAL | Ash holder pendants flagged. Needs policy review. |
| 293 landing page errors | CRITICAL | Products showing landing page 404s or unreachable. |
| 90 pending initial policy review | INFO | In review pipeline for KR market. |
| KR market issues | INFO | 176 invalid currency + 178 missing shipping + 90 missing business reg for South Korea. |

---

*Generated by BETA GOOGLE Strategist*  
*Data sources: Merchant Center API v2.1, Phase 3 checkpoint files, WordStream 2026 benchmarks*  
*Guardrails observed: All reads, no writes, no spend changes, no keyword changes*