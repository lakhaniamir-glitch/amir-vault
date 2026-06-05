# (C) Meta Ads Automation Playbook — 2026-06-04

> Built tonight while you were lifting. Establishes the daily reporting cadence, auto-pause rules, creative pipeline infrastructure, and the full picture of what's automated vs what still needs human approval.

---

## API Access Audit (locked 2026-06-04)

Your Meta System User token has **24 scopes** and **does not expire**. Full automation surface:

| Capability | Scope | What it unlocks |
|---|---|---|
| Ads Management | `ads_management`, `ads_read` | Create / edit / pause / scale ads, ad sets, campaigns. Pull all insights. |
| Pages Posting | `pages_manage_posts`, `pages_manage_metadata`, `pages_manage_engagement` | Auto-post to FB Page, reply to comments |
| Instagram Publishing | `instagram_content_publish`, `instagram_basic`, `instagram_manage_comments` | Auto-post reels, carousels, stories. Reply to DMs / comments. |
| Instagram Insights | `instagram_manage_insights` | Pull engagement + reach data |
| Instagram Shopping | `instagram_shopping_tag_products` | Auto-tag products in posts |
| Branded Content | `instagram_branded_content_ads_brand`, `facebook_branded_content_ads_brand` | Run creator-collab ads |
| **Threads** | `threads_business_basic` | Post to Threads via API |
| Catalog | `catalog_management` | Manage product catalog for DPA |
| Business | `business_management` | Manage business asset access |

Token does not expire (System User type). Stored: `/home/openclaw/.openclaw/agents/beta/credentials/meta-ads.env`.

**Translation:** We can run end-to-end automated ad creation, monitoring, scaling, and pausing without you ever logging into Ads Manager.

---

## What's Automated Now (live as of 2026-06-04)

### Cron schedule

| Time (CT) | Job | What it does | Output |
|---|---|---|---|
| **6:30am daily** | `beta-meta-ads-daily` | Pull yesterday/7d/30d spend, purchases, ROAS, CTR, CPM, frequency at campaign + adset + ad level. Push Telegram summary. | `/command-center/work/meta/daily/meta-ads-daily-{date}.md` + `.json` |
| **6:35am daily** | `beta-meta-ads-auto-pause` | Check for ads with $50+ spend AND 0 purchases in last 7 days. Telegram alert. Fatigue warning if frequency >=4. | `/command-center/work/meta/daily/auto-pause-{date}.json` |
| **6:00am daily** | `meta-billing-health-check` | Browser audit of billing status | `meta_billing_health_check.log` |
| **7:00am daily** | `meta-delivery-proxy-check` | Session count check (just patched - was broken) | `meta_delivery_proxy_check.log` |

### Auto-pause rules (currently in ALERT_ONLY mode)

For first **14 days**, the auto-pause script identifies candidates but does NOT actually pause. Telegram alerts only. After validation period, flip `ALERT_ONLY=0` env to enable hard auto-pause.

**Current rules:**
- Pause candidate: ad with $50+ 7d spend AND 0 purchases
- Fatigue warning: any adset with frequency >=4 AND spend >$10

**Why alert-only first:** Your "Couples engraved Single image" ad has $78.99 last 7d with 0 attributed purchases. But the 30-day data shows the CAMPAIGN got 51 sales. The 7-day zero might be attribution lag, not a dead ad. Need 2 weeks of data to confirm the rule doesn't kill winners.

---

## What's NOT Automated (you decide)

### Budget changes (auto-scale)
Never automated. If an ad hits 5x+ ROAS at scale, the Telegram daily report will surface it but the budget bump needs your call. Reasoning: scaling too fast breaks the Meta learning phase and can crash ROAS overnight.

### New creative generation
The infrastructure exists (see "Creative Pipeline" below). But generating a new creative requires creative judgment:
- Which Shopify product to base it on
- Which UGC vs studio vs lifestyle direction
- Which brief variant to test
- Reference image selection

I refuse to autonomously generate creatives because the output quality is too variable. Better: you tell me "test brief 3 with the rose gold koa wood ring" and I do the technical execution.

### Launching ads (PAUSED → ACTIVE)
Uploader script creates new ads as PAUSED by default. You toggle them on in Ads Manager or by Telegram-replying APPROVE to the upload notification.

---

## Creative Pipeline Infrastructure (installed, ready to use)

### Brief library
```
/home/openclaw/.openclaw/command-center/work/meta/creative-briefs/
  01-ugc-testimonial.md       (Brief 1 - LIVE as ASHER + DEVITO)
  02-before-after-engraving.md (Brief 2 - drafted, not yet executed)
  03-story-narrative.md        (Brief 3 - drafted, not yet executed)
  04-price-anchored-dr.md      (Brief 4 - drafted, not yet executed)
```

Each brief has: concept summary, visual direction, copy variants (3+ primary text + 3+ headlines + description), CTA spec.

### Uploader script
`/home/openclaw/.openclaw/command-center/scripts/meta_ads_upload_creative.cjs`

Usage:
```
node meta_ads_upload_creative.cjs \
  --image=/path/to/hero.jpg \
  --brief=02-before-after-engraving \
  --variant-name="Before-After v1 Damascus" \
  --primary-text-index=0 \
  --headline-index=0 \
  --link=https://shopaydins.com/products/specific-handle \
  --adset-id=6929192369327
```

What it does:
1. Parses brief markdown to extract copy variants
2. Uploads image to your Meta ad account
3. Builds ad creative with copy + image + CTA
4. Creates ad in target ad set as **PAUSED**
5. Telegram alert with ad ID for your approval
6. Writes audit log to `/command-center/work/meta/creative-uploads/`

### Image generation rule
Per locked rule in top-level CLAUDE.md (2026-06-04): all product images must use a Shopify reference image via edit mode. Never text-only generation. See [[CLAUDE]] for full rule.

### Pipeline diagram
```
Brief (markdown)
   |
   v
Shopify reference image (the actual product photo)
   |
   v
image_generate (action=edit, input_images=[ref])  <-- this is the gate
   |
   v
hero.jpg in /tmp
   |
   v
meta_ads_upload_creative.cjs --image=hero.jpg --brief=02-... --status=PAUSED
   |
   v
Telegram alert: "NEW CREATIVE UPLOADED: enable in Ads Manager"
   |
   v
You review, click ACTIVE in Ads Manager (or reply APPROVE)
   |
   v
Daily monitor watches its performance
   |
   v
If hits $50 + 0 sales -> auto-pause alert
If hits 5x ROAS + $30 -> daily report flags as winner
```

---

## Recommended Next Creatives to Test

Based on ASHER hitting 33x ROAS, the winning pattern is: UGC + specific product + couples emotional hook.

Recommended testing order:

### 1. Brief 4 — Price-anchored DR (easiest to execute)
- Product: any top seller with strong perceived value (e.g., a $350-looking ring you sell for $179)
- Visual: hero on white background (we have 50 of these from the Etsy work today)
- Copy: "Real wedding band. Free engraving. Under $200." vibe
- Why first: lowest creative effort, fastest validation

### 2. Brief 3 — Story narrative
- Product: pick a featured ring with emotional history (Damascus = forged-strength angle)
- Visual: lifestyle scene with the ring being put on or held
- Copy: short narrative arc, "Six months ago he proposed with…" style
- Why second: harder visual direction, but higher emotional payoff

### 3. Brief 2 — Before / after engraving
- Product: clean tungsten ring with clear inner band visibility
- Visual: ring before engraving + ring with engraving visible (probably needs 2 images or a carousel)
- Copy: "Just metal. Now it's his." kind of contrast
- Why last: highest production complexity, but biggest differentiator vs every competitor

---

## When You Sit Back Down at Meta Stuff

**The 5-minute version:**

1. Check Telegram tomorrow 6:30am for first daily report
2. Reply to me: "test brief X with product Y" -> I do the technical execution
3. Review the paused ad in Ads Manager, enable when ready
4. Watch daily reports for 3-5 days
5. Repeat

**The Meta money question:**
Your ASHER ad at 33x ROAS means **every $1 spent returns $33 in attributed revenue**. With $50/day campaign budget, that's worth scaling. But scale carefully: bump budget 15-20% at a time, every 3-5 days. More aggressive jumps risk breaking learning.

**The ad-fatigue early warning:**
Watch frequency. When it hits 3+ and CTR drops, you need new creative or new audience. Right now you're fine across all ads. The daily report tracks this.

---

## Files Reference

```
SCRIPTS (executable):
/home/openclaw/.openclaw/command-center/scripts/
  meta_ads_daily.cjs                       <- daily report
  meta_ads_daily_wrapper.sh                <- cron wrapper
  meta_ads_auto_pause.cjs                  <- candidate-pause checker
  meta_ads_auto_pause_wrapper.sh           <- cron wrapper
  meta_ads_upload_creative.cjs             <- creative uploader

WORK PRODUCTS:
/home/openclaw/.openclaw/command-center/work/meta/
  daily/meta-ads-daily-{date}.{md,json}    <- daily reports
  daily/auto-pause-{date}.json             <- daily pause audits
  creative-briefs/                         <- 4 briefs ready to execute
  creative-uploads/                        <- per-upload audit logs

CREDENTIALS:
/home/openclaw/.openclaw/agents/beta/credentials/meta-ads.env
  META_ACCESS_TOKEN (System User, no expiry)
  META_AD_ACCOUNT_ID

LOGS:
/home/openclaw/.openclaw/command-center/logs/
  beta_meta_ads_daily.log
  beta_meta_ads_auto_pause.log
```
