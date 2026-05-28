---
title: Beta Operations State — Aydins Jewelry
status: live-operational-memory
captured: 2026-05-26
source: Beta handoff (OpenClaw)
project: Aydins Jewelry
type: state-summary
---

# Beta Operations State — Aydins Jewelry

**As of 2026-05-26.** This is live operational memory from Beta (the OpenClaw operations agent). Treat as source of truth for what Beta has shipped, what is pending, and what is scheduled. Not generic planning. Update when Beta hands off new state.

---

## Big-Picture Context

Aydins Jewelry is the main revenue engine. Beta's current focus:

1. Improve the Aydins Shopify website and mobile conversion flow.
2. Clean up SEO/content quality across collections, product pages, and guides.
3. Fix Google Merchant Center / Shopify feed mismatch problems.
4. Wire GA4 / Shopify / Merchant Center reporting.
5. Set up BAND20 promo tracking across Klaviyo, Recart/SMS, GA4, Shopify orders, and Slack delivery.
6. Move operational reporting out of Discord DM into Slack `#beta-daily`.

---

## 1. Aydins Website Work

### A. Shopify page: "How to Choose a Men's Wedding Band"

Page updated.

- Shopify page ID: `138482680045`
- Handle: `how-to-choose-a-mens-wedding-band`
- Title: `How to Choose a Men's Wedding Band - The 5-Decision Guide`
- Updated on Shopify: `2026-05-26T08:49:50-05:00`
- Follow-up update: `2026-05-26T08:53:11-05:00`

**What was done:**
- Audited the existing guide page.
- Updated outdated wording.
- Normalized punctuation from em-dash-heavy copy to cleaner hyphen usage.
- Updated schema `dateModified` to 2026-05-26.
- Preserved article/schema structure: Article, Organization, BreadcrumbList, WebPage, FAQPage.
- Confirmed jump links present.
- Updated "lifetime sizing" language so it is accurate and less legally risky. Replaced "lifetime free resizing" with safer "lifetime sizing support" where appropriate.
- Kept the page positioned as a strong SEO guide for men's wedding band buying intent.

**Backup / audit files:**
- `shopify/audits/how-to-choose-mens-wedding-band-before-20260526T134950Z.json`
- `shopify/audits/how-to-choose-mens-wedding-band-update-20260526T134950Z.json`
- `shopify/audits/how-to-choose-before-jumplinks-lifetime-sizing-20260526T135310Z.json`
- `shopify/audits/how-to-choose-jumplinks-lifetime-sizing-20260526T135310Z.json`

**Status:** Completed and verified.

---

### B. Homepage / Collection / Mobile Work

Recent site work:
- Tightened mobile collection layouts.
- Checked mobile viewport rendering for key money collections.
- Screenshots / viewport reports created for:
  - Men's Wedding Bands
  - Best Sellers
  - Inside Ring Engraving
  - Tungsten Rings
  - Black Rings
  - Wood Inlay Rings
  - Meteorite Rings

**Artifacts:**
- `reports/mobile-collections-2026-05-26/results.json`
- `reports/mobile-collections-2026-05-26/*.png`

**Live text confirmed in mobile capture:**

Announcement bar / promo:
> WEDDING BAND WEEK: TAKE 20% OFF PERSONALIZED RINGS THROUGH SUNDAY. USE CODE BAND20.

Trust messaging:
> FREE SHIPPING & LIFETIME WARRANTY ON EVERY BAND
> ENGRAVING AND SHIPPING FROM TEXAS SINCE 2011

Additional work:
- Compacted money collection descriptions for mobile.
- Made collection intro copy less bloated above the product grid.
- Kept mobile SEO copy useful without pushing products too far below the fold.

---

### C. Loox / Reviews Homepage Work

Visual artifacts captured:
- `reports/loox-home-reviews-custom-html-2026-05-26.png`
- `reports/loox-home-reviews-custom-html-scrolled-2026-05-26.png`

**Status:** Homepage review presentation was worked on and visually captured.

---

### D. Navigation / Menu / V5 Site Work

Earlier May work:
- Main navigation and mega-menu changes.
- Collection discovery menu work.
- Guides menu backups.
- Precious stones navigation audit.
- Christian Rings menu/collection work.
- Mobile menu fallback work.
- Doofinder search investigation.

**Important artifacts:**
- `reports/v5-live-qa-2026-05-18.json`
- `reports/v5-menu-http-check-2026-05-18.json`
- `reports/precious-stones-nav-audit-2026-05-19.json`
- `shopify/audits/main-menu-backup-2026-05-15T14-48-56-186Z.json`
- `shopify/audits/guides-menu-backup-2026-05-15T14-49-33-288Z.json`

**Outcomes:**
- V5 live QA checked policy/content pages, menu URLs, footer, product/cart/checkout/ring-sizer/mobile flows.
- Doofinder mobile search had partial work / investigation. Desktop Doofinder was protected after earlier search/menu conflicts.
- Mobile fallback menu work was done to bypass broken Kalles mobile drawer behavior.
- Some preview-only search experiments were reverted when they broke or didn't satisfy Amir's desired Doofinder behavior.

---

### E. Product / Listing Cleanup Rules — LOCKED

Aydins product listing standard is locked around the **VESUVIUS-approved format**.

**Product description structure (lean):**
- Strong opening paragraph
- Short support paragraph
- Key Features bullets
- "Why CODENAME" close
- No duplicate warranty/returns/sizing/shipping text if global PDP accordions already show it

**Quick Specs (metafields):**
- Primary: `custom.keywords`
- Backup/helper: `custom.quick_specs`
- Labeled format, not keyword spam:
  - Material: [material name]
  - Inlay/Feature: [feature name]
  - Widths: [list widths]
  - Fit: [fit type]
  - Profile: [profile detail]
  - Engraving: [location]

**Product FAQ:**
- Lives in `custom.custom_faq`
- Product/material-specific only:
  - What is [CODENAME] made of?
  - Is [material] good for daily wear?
  - What does the [inlay/feature] look like?
  - Can [CODENAME] be engraved?
  - Is it comfort fit?
  - How do I care for a [material] ring with [feature]?
- **Exclude** generic policy questions: warranty, returns, shipping, sizing, general engraving process.
- FAQ schema must match the visible product FAQ.

**Mandatory Google / category metafields:**
- Color
- Ring size
- Jewelry material
- Age group
- Jewelry type
- Ring design
- Target gender
- Ring Size Chart
- Gemstone/stone shape only when truthful and valid

**Shopify tags must include:**
- Offered widths (e.g., 6mm, 8mm)
- Engraving location (e.g., Inside or Inside & Outside)
- Material collection tag (e.g., Ceramic Rings, Tungsten Rings)
- Visible colors (e.g., Black, Blue, Orange)
- Inlay/feature tags (e.g., Lava Rock, Carbon Fiber, Dinosaur Bone, Wood, Opal, Meteorite)

**SKU / inventory rules for Universal J / Jewelry Depot:**
- SKU format: `CODENAME-WIDTH-SIZE` (e.g., `VESUVIUS-6-5`)
- Inventory quantity: 10
- Inventory policy: continue selling when out of stock
- Variants must match vendor/source exactly
- Do not invent widths/sizes

---

## 2. BAND20 Promo

### A. Promo Strategy

Originally TAKE20 (old/evergreen). Replaced with fresh urgency code.

- Code: `BAND20`
- Offer: 20% off
- Theme: Wedding Band Week
- Main CTA collection: https://shopaydins.com/collections/mens-wedding-bands
- UTM campaign: `band20_wedding_band_week`
- Klaviyo UTMs: `utm_source=klaviyo&utm_medium=email&utm_campaign=band20_wedding_band_week`

**Generated HTML email:** `aydins-band20-klaviyo-email-2026-05-25.html`

Email includes: BAND20 code, Wedding Band Week framing, CTA to Men's Wedding Bands collection, UTM tracking on CTA URL, urgency through Sunday.

### B. Klaviyo

**Earlier state (read-only snapshot, May 14):**
- 7 flows
- 5 lists
- 0 segments
- 8 email campaigns
- 4 templates
- 56 metrics
- Draft template created earlier: `Aydins Welcome Series - Material Guide (Beta Draft)`, template ID `Uwi4fE`
- Live flows/templates were NOT deleted or changed in that pass.

**For BAND20:**
- BAND20 Klaviyo-ready HTML was created.
- Handoff says BAND20 email campaign was created and scheduled with 3-day follow-up.
- Report job scheduled to measure performance after send.

### C. Recart / SMS

- Recart BAND20 SMS campaign scheduled May 26 at 12:00 PM subscriber local time.
- Recommendation: avoid 6:34 PM send. Late morning / noon with quiet hours respected.

**Shopify order tags observed:**
- `Recart`
- `RecartSMS`
- `RecartAttributed`

**Recent SMS/Recart discount codes seen on orders:**
- `SMS20RC`
- `SMS25AC7MRG5M`

---

## 3. GA4 / Analytics

### A. GA4 OAuth Connected

Files:
- `google/ga4_fetch.js`
- `google/ga4-oauth-client.json`
- `google/ga4-oauth-token.json`
- `google/ga4-oauth-state.txt`

**Do not expose or paste token contents.**

### B. GA4 30-Day Quick Audit

Report: `reports/aydins-30day-quick-audit-2026-05-26.json`

| Channel | Sessions | Users | Purchases | Revenue |
|---|---|---|---|---|
| Cross-network | 4,897 | 4,555 | 48 | $8,792.25 |
| Direct | 1,666 | 1,405 | 71 | $14,582.93 |
| Paid Social | 702 | 558 | 2 | $328.00 |
| Organic Search | 549 | 478 | 10 | $1,477.41 |
| Unassigned | 324 | 241 | 11 | $4,056.07 |
| Paid Search | 298 | 265 | 6 | $1,441.00 |
| Organic Social | 259 | 249 | 0 | $0 |
| Organic Shopping | 174 | 96 | 2 | $322.20 |
| Email | 60 | 34 | 1 | $331.50 |
| Referral | 32 | 26 | 0 | $0 |
| Paid Shopping | 8 | 8 | 0 | $0 |
| SMS | 2 | 1 | 0 | $0 |
| Paid Other | 1 | 1 | 0 | $0 |

**Interpretation:**
- Cross-network / Google Shopping-style traffic is a major traffic and revenue source.
- Direct revenue is very high. Likely partial attribution leakage / returning buyer / untagged traffic.
- Email was low before BAND20. BAND20 tracking matters.
- SMS attribution in GA4 is weak / underreported. Shopify + Recart tags help identify impact.

### C. BAND20 Performance Report — Scheduled

**Cron job:** `Aydins BAND20 next-day performance report`
- Scheduled: `2026-05-27T15:00:00.000Z`
- One-time job. Delete after run.
- Runs on DeepSeek to avoid burning GPT / Codex quota.

Will pull:
- GA4 traffic / revenue for klaviyo/email and `band20_wedding_band_week`
- Shopify orders / revenue / discount usage for BAND20 if accessible
- Shopify attribution / referrer / source indicators for Klaviyo and Recart/SMS
- Merchant Center quick status only if notable issue
- Recommendation: keep, follow-up, change, or wait

**Logging:**
- `memory/2026-05-27.md`
- Post report to Slack `#beta-daily` via fallback script.

---

## 4. Google Merchant Center

### A. API Access Verified

Service-account access working.

Files:
- `google/service-account.json`
- `google/fetch_merchant.py`
- `google/fetch-merchant.js`
- `google/fetch_all_products.py`
- `google/fetch-disapproved.js`
- `google/fetch-lean.js`
- `google/product_stats.json`
- `google/sample_products.json`

**Do not expose service account file contents.**

### B. Merchant Center / Shopify Publish Audit — Completed

Main report: `reports/mc-shopify-audit-2026-05-26T21-33-36-299Z.json`

Related:
- `reports/mc-shopify-audit-2026-05-26T21-19-14-760Z.json`
- `reports/mc-shopify-audit-remaining-2026-05-26T22-01-15-686Z.json`

**Result:**
- 5,000 Merchant Center items checked across 20 pages
- 1,781 unique handles in Merchant Center feed
- 14 products in Merchant Center that should not be there:
  - 10 draft Shopify products
  - 4 archived Shopify products

### C. Draft Products to Remove from Merchant Center (10)

1. `ardent-black-tungsten-ring-diamond-stimulate-white-cz-hammered`
2. `alnair-rose-gold-tungsten-ring-blue-pipe-cut`
3. `supersonic-two-tone-brushed-yellow-gold-black-groove-tungsten-ring-8mm-wide`
4. `bluewave-blue-tungsten-ring-black-brushed-blue-grooved-center`
5. `lunara-silver-tungsten-ring-sleepy-lavender-opal-inlay-beveled`
6. `shavogold-yellow-gold-tungsten-black-resin-gold-shavings-inlay`
7. `bayamon-orange-aluminum-ring-orange-groove`
8. `corkshine-yellow-gold-tungsten-domed-ring-gold-glitter-inlay`
9. `gritedge-black-tungsten-ring-gun-metal-with-domed-brushed-off-center-groove`
10. `rolfe-black-tungsten-ring-blue-beveled-edge`

### D. Archived Products to Remove from Merchant Center (4)

1. `mens-wedding-band-polished-flat-14k-rose-gold-wedding-ring-with-bubinga-wood-inlay-8mm`
2. `noirzicon-rose-gold-tungsten-ring-domed-ring-black-cz-ring`
3. `leonis-two-tone-black-tungsten-ring-with-brushed-rose-gold-dome-4mm-6mm-8mm`
4. `mens-wedding-band-14k-rose-gold-with-black-carbon-fiber-inlay-flat-polished-design`

### E. Current Blocker

**The 14 products have not been removed yet.** Removal is destructive / external API action. Beta is waiting on Amir's explicit approval before deleting from Merchant Center.

- Do not assume removal has been done.
- If Amir says "approve / remove the 14 MC products," Beta can proceed via API.
- Preserve / report deletion log.

### F. Weekly Merchant Center Audit — Scheduled

**Cron job:** `Weekly MC-Shopify publish audit`
- Schedule: Mondays at 10:00 UTC
- Purpose: catch future draft / archived / unpublished products leaking into MC
- Reports counts, handles, recommendations
- Logs to `memory/weekly-audit-YYYY-MM-DD.md`
- Posts summary to Slack `#beta-daily` via fallback script

---

## 5. Slack Delivery

### A. Desired State

Move operational reports from Discord DM to Slack.

Target channels:
- `#beta-daily` (primary)
- `#beta-weekly`
- `#beta-alerts`

Channel IDs are in command-center `.env`. Do not paste publicly.

### B. Manual Slack Bot Token Works

Slack bot token verified by manual API call.

Fallback Slack poster: `scripts/slack_post.js`

Usage:
```bash
node scripts/slack_post.js --channel daily --text "message"
# or
echo "message" | node scripts/slack_post.js --channel daily
```

Reads Slack env from `~/.openclaw/command-center/.env`.

Aliases: `daily`, `weekly`, `alerts`.

Test: fallback post to `#beta-daily` succeeded. Slack ts `1779838279.272729`.

### C. Native OpenClaw Slack Delivery NOT Live

Blocker:
- OpenClaw service reads `~/.openclaw/openclaw.json`.
- Someone created `~/.openclaw/config.json` (wrong file for the running service).
- Native Slack Socket Mode requires BOTH:
  - Bot token: `xoxb-...`
  - App-level token: `xapp-...` with scope `connections:write`
- Only the bot token is verified. No `xapp-` token found on disk.
- Therefore native OpenClaw Slack connector is not live.

### D. Active Workaround

Critical cron jobs have native OpenClaw Slack delivery set to `mode:none`. Job prompts post final report to Slack via:

```bash
node /home/openclaw/.openclaw/agents/beta/scripts/slack_post.js --channel daily
```

Used by:
- `Aydins BAND20 next-day performance report`
- `Weekly MC-Shopify publish audit`

---

## 6. Phase 0 / Phase 1 Context

### Phase 0 — Safe Scaffolding

Stubs only. Hard rules:
- No publishing
- No ad spend changes
- No emails sent
- No live autonomous channel agents

Included: agent prompt stubs, brand profiles, status files, task files, dashboard shell, cron / webhook plan, Slack channel plan.

### Phase 1 — Aydins-Only Pilot

Activated / considered: Beta, Beta Shop, Beta Check.

Goal: prove daily Aydins task loop before expanding to more agents / platforms.

Earlier Phase 1 notes:
- Shopify smoke test pulled product ABALONX.
- BETA Check reviewed listing drafts.
- GA4 pageview query had a permission issue early; resolved later via OAuth setup.
- Slack posting worked for Phase 1 cron via a separate Slack method.

---

## 7. Key File Index

### Website / Shopify
- `shopify/audits/how-to-choose-mens-wedding-band-before-20260526T134950Z.json`
- `shopify/audits/how-to-choose-mens-wedding-band-update-20260526T134950Z.json`
- `shopify/audits/how-to-choose-before-jumplinks-lifetime-sizing-20260526T135310Z.json`
- `shopify/audits/how-to-choose-jumplinks-lifetime-sizing-20260526T135310Z.json`
- `reports/mobile-collections-2026-05-26/results.json`
- `reports/mobile-collections-2026-05-26/*.png`
- `reports/loox-home-reviews-custom-html-2026-05-26.png`
- `reports/loox-home-reviews-custom-html-scrolled-2026-05-26.png`
- `reports/v5-live-qa-2026-05-18.json`
- `reports/v5-menu-http-check-2026-05-18.json`

### Merchant Center / Google
- `google/ga4_fetch.js`
- `google/ga4-oauth-client.json`
- `google/ga4-oauth-token.json`
- `google/service-account.json`
- `tmp/fix_mc_shopify_audit.js`
- `reports/mc-shopify-audit-2026-05-26T21-33-36-299Z.json`
- `reports/mc-shopify-audit-remaining-2026-05-26T22-01-15-686Z.json`
- `reports/aydins-30day-quick-audit-2026-05-26.json`

### Slack
- `scripts/slack_post.js`
- `~/.openclaw/command-center/.env`
- `~/.openclaw/openclaw.json` (the one the service actually reads)
- `~/.openclaw/config.json` (exists but is NOT read by the service)

### Memory
- `memory/2026-05-26.md`
- `memory/2026-05-25.md`
- `MEMORY.md`

---

## 8. Pending Items

### Pending Approval — Merchant Center Cleanup
Remove 14 draft / archived products from Merchant Center. **Do not act without Amir's explicit approval.**

### Pending Scheduled Report — BAND20
- Scheduled: 2026-05-27 at 15:00 UTC
- Posts to Slack `#beta-daily`
- Logs to `memory/2026-05-27.md`

### Pending Slack Native Fix
To fully fix native OpenClaw Slack delivery:
1. Get / create Slack app-level token (`xapp-...` with `connections:write`).
2. Patch correct config at `~/.openclaw/openclaw.json` under `channels.slack`.
3. Do NOT rely on `~/.openclaw/config.json` unless OpenClaw service is changed to read it.
4. Restart / reload gateway.
5. Verify `channels.slack` appears in OpenClaw config.
6. Test native Slack delivery.
7. Only then remove fallback dependency.

Fallback is working. Not urgent unless Amir wants native routing.

---

## 9. Cautions

- Do NOT expose: Slack tokens, GA4 tokens, Merchant Center service account contents, Shopify tokens, Klaviyo keys.
- Do NOT delete Merchant Center products without Amir's explicit approval.
- Do NOT make Shopify live changes without verifying backups / audit logs.
- Do NOT rewrite Aydins listing format unless it follows the locked VESUVIUS-approved structure.
- Do NOT use generic warranty / sizing claims loosely. Use safer policy language when unsure.

**Revenue priority order for Aydins:**
1. Google Shopping / Merchant Center health
2. BAND20 promo performance
3. Mobile conversion
4. High-intent collection / page SEO
5. Product listing quality / metafields / schema

---

## Next Action

Amir's call: approve or hold on removing the 14 Merchant Center products. That is the highest-leverage pending decision on this state file. If approved, Beta proceeds via API and logs the deletion. If holding, say why so the weekly audit job can flag context next Monday.
