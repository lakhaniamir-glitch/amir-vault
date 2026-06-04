---
status: live
created: 2026-05-29
owner: Claudian
review_cadence: monthly
---

# Standing Tasks — 16 Recurring Jobs Live on VPS

Shipped 2026-05-29. These run automatically on the Hetzner VPS without you doing anything. **9 are content creators that draft real marketing assets.** **6 are monitors that watch systems and send alerts.** Plus **1 hybrid pipeline for IG Reels** (you + BETA + GMC). Everything lands in the vault for you to approve.

## IG Reels Hybrid Pipeline (free + 2-3 min/day from you)

After testing direct Veo 3.1 ($6/reel, motion issues) and Runway ($same+markup), we settled on the right architecture: BETA does the creative heavy lifting + GMC's free Veo does the video generation + you do quality control.

| Step | When | Who | What |
|---|---|---|---|
| 1 | Daily 4:00am CT | `beta_insta_daily_gmc_brief.py` | Picks one Aydins product, Nano Banana restages it into a cinematic scene (7 rotating themes: beach_zen, dark_walnut_workshop, slate_stone_mountain, leather_library, marble_minimal, moss_forest, concrete_industrial), generates 3 Veo prompt variants via DeepSeek. Drops image + prompts.md in `vault/brands/aydins/gmc-briefs/YYYY-MM-DD-{handle}/`. Telegram pings you. |
| 2 | When you have 2-3 min | **You** | Open GMC → Product Studio → Animate Images → upload `restaged.jpg` → paste recommended prompt → download MP4 → drop in `vault/brands/aydins/reel-videos/pending/` |
| 3 | Every 30 min | `beta_insta_reel_watcher.py` | Detects new MP4 → reads matching brief for product context → generates IG caption + hashtags via DeepSeek → uploads MP4 to Shopify Files (public CDN) → adds slot to IG calendar with `media_type: REELS` → moves MP4 to `approved/` |
| 4 | Every 15 min | `phase2_publisher.py` (patched 2026-05-29) | Picks up REELS slots from calendar → POSTs to Meta Graph API `/{ig_id}/media` with `media_type=REELS + video_url + share_to_feed=true` → polls container ~3 min → publishes via `/media_publish` → verifies media_type=VIDEO → marks slot published |

**Cost**: ~$0.05/day for Nano Banana + DeepSeek = **$1.50/month** for 30 reels  
**Your time**: 2-3 min/day in GMC  
**Result**: 30 GMC-quality reels per month, real Aydins products in cinematic scenes, auto-posted to IG

### Folder structure

- `vault/brands/aydins/gmc-briefs/YYYY-MM-DD-{handle}/restaged.jpg` + `brief.md` — daily image + prompts for you
- `vault/brands/aydins/reel-videos/pending/` — where you drop completed MP4s
- `vault/brands/aydins/reel-videos/approved/` — watcher moves files here after processing
- `vault/brands/aydins/reel-videos/published/` — publisher will move after IG posting

### Why not full automation via paid Veo API?

We tested: Runway Gen-4 Turbo (distorted rings), Runway Gen-4.5 (no audio, slow, marble-only staging), Runway Veo 3.1 (letterboxed), direct Gemini Veo 3.1 (motion issues + ring color shifted). All cost $3-6/reel. Quality was inconsistent. GMC's Product Studio is purpose-built for product showcase and Google subsidizes the Veo cost since it drives Shopping Ads — output quality is consistently higher than raw API. The 2-3 min/day of your time is the right tradeoff.

## Content creators (these produce assets)

| Schedule (CT) | Agent | Script | What it drafts | Where it lands |
|---|---|---|---|---|
| Daily 4:00am | BETA Shop | `beta_shop_listing_enricher.py` | Picks weakest active Aydins listing. Drafts new meta_title + meta_description + 3 benefit bullets + 6 FAQs. Validated against BETA Check rules + VESUVIUS standard. | `vault/brands/aydins/listing-enrichment/YYYY-MM-DD-{handle}.md` + review queue |
| Daily 5:00am | BETA Insta | `beta_insta_reel_script_writer.py` | 1 complete Reels script: hook + 5-shot list + on-screen text per shot + VO + CTA + caption + hashtags + audio direction. Theme rotates by weekday (educational, BTS, customer story, product, myth-bust, lifestyle, comparison). | `vault/brands/aydins/reel-scripts/YYYY-MM-DD-{theme}-reel.md` |
| Tue 10:00am | BETA Klaviyo | `beta_klaviyo_email_drafter.py` | Picks one live Aydins Klaviyo flow on rotation. Pulls its first email, drafts 3 subject-line A/B variants + 2 preview-text variants + new 100-word opening body + recommendation on which to test first. | `vault/brands/aydins/klaviyo-email-drafts/YYYY-MM-DD-{flow_id}-{slug}.md` + review queue |
| Fri 10:00am | BETA Klaviyo | `beta_klaviyo_weekly_campaign.py` | Drafts THIS WEEK's email campaign for the Aydins newsletter list. Picks angle on rotation (new arrivals, educational, customer story, soft promo, BTS). Creates a true Draft campaign **inside Klaviyo via API** (subject + preview + from set; status=Draft; scheduled_at=null). Body content sits in vault for paste-into-template. | `vault/brands/aydins/klaviyo-campaigns/YYYY-MM-DD-weekly-{angle}.md` + Klaviyo draft + review queue |
| Wed 9:00am | BETA Google | `beta_google_blog_drafter.py` | 800-word SEO blog post on the highest-traffic Aydins landing-page topic that doesn't have a supporting blog yet. Includes meta tags + 4 H2 sections + 3 FAQs + image prompt + internal link suggestions. | `vault/brands/aydins/blog-drafts/YYYY-MM-DD-{slug}.md` + review queue |
| Thu 9:00am | BETA Shop | `beta_shop_collection_describer.py` | Picks weakest Aydins collection page (empty or thin description). Drafts 500-700-word collection description with meta + hero intro + 3 H2 sections + 3 FAQs + hero image alt-text. | `vault/brands/aydins/collection-descriptions/YYYY-MM-DD-{handle}.md` + review queue |
| Daily 6:00am | BETA Insta | `beta_insta_carousel_writer.py` | Daily 8-slide IG carousel script (cover + 6 content slides + CTA). On-image text per slide, design system notes, caption, hashtags. Theme rotates by weekday (guide, comparison, myth-vs-truth, checklist, journey, process, story). | `vault/brands/aydins/carousel-scripts/YYYY-MM-DD-{theme}-carousel.md` |
| Every 30 min | BETA Etsy | `beta_etsy_aydins_rewriter.py` | Watches `brands/aydins/etsy-exports/` for new VELA CSV. When detected, drafts rewrites for the 5 weakest Aydins Etsy listings: new title (140 chars max) + 13 tags + opening sentence + 200-word description + rationale. | `vault/brands/aydins/etsy-rewrites/YYYY-MM-DD-{listing_id}.md` + review queue |

After 30 days: **30 listing enrichments, 30 reels, 30 carousels, 4 blogs, 4 Klaviyo A/B kits, 4 weekly Klaviyo campaign drafts (ready to send in Klaviyo), 4 collection descriptions, and 5 Aydins Etsy rewrites per CSV you drop.** Your only job is review + click publish.

## Weekly Klaviyo campaign — safety design

The weekly campaign drafter is the only standing task that writes to a paid customer-facing system (Klaviyo). Three safeguards prevent any accidental send:

1. **Always created as Draft.** Klaviyo's API only accepts a future datetime, so BETA passes one 14 days out. But because no template is attached, Klaviyo holds the campaign in Draft state until you explicitly schedule it.
2. **No template assigned.** You pick your brand template inside Klaviyo. BETA won't auto-style emails.
3. **Telegram alert.** Every Friday after creation you get a deep link to the new draft + a review-queue entry. Reject by deleting the Klaviyo draft.

If you ever want to change the target list (currently `WqHHmn` = Email List), set `KLAVIYO_CAMPAIGN_LIST_ID` in `agents/beta/credentials/klaviyo.env`.

## How BETA Etsy Aydins Rewriter Works (since Etsy denied your API key)

Etsy denied your developer app. VELA has no public API. Scraping VELA stores your password + breaks on every UI update. So instead:

1. You log into VELA, hit Export, get a CSV. (~30 seconds)
2. Drop the CSV in `brands/aydins/etsy-exports/` in your local vault
3. Your local vault auto-syncs to the VPS via GitHub every 10 min
4. BETA Etsy runs every 30 min, sees the new CSV, drafts 5 rewrites
5. **Max time from drop to drafts ready: ~40 minutes**
6. Telegram pings you with the count

Zero credentials stored. Zero scraping. Your only friction is one CSV export per week. See README in `etsy-exports/` folder for column-name auto-detection details.

## Monitors (these watch + alert)

| Schedule (CT) | Agent | Script | What it watches | Where it lands |
|---|---|---|---|---|
| Daily 6:30am | BETA Google | `beta_google_organic_snapshot.py` | GA4 organic sessions diff vs prior day. Alerts on >30% total drop or >40% top-page drop. | `work/beta-google/organic-snapshots/` + Telegram only on alert |
| Daily 7:00am | Claudian | `claudian_morning_brief.py` | Yesterday's wins, items needing your call, today's IG slots, recommended first action. | `vault/01 Journals/2026 Journals/morning-briefs/` + Telegram (always) |
| Daily 7:30am | BETA Klaviyo | `beta_klaviyo_flow_health.py` | Pulls all flows, diffs status vs yesterday. Alerts on live→draft transitions or new archives. | `work/beta-klaviyo/snapshots/` + Telegram only on alert |
| Sun 9:00am | BETA Shop | `beta_shop_pricing_snapshot.py` | Top 25 active Shopify products. Diffs price (≥5%) and stock state week-over-week. | `work/beta-shop/pricing-snapshots/` + Telegram only on changes |
| Sun 6:00pm | BETA Insta | `beta_insta_engagement_review.py` | Last 7 days of published IG posts (like_count + comments_count). Ranks top 3 / bottom 3, recommends category mix tilt. | `vault/brands/aydins/insta-weekly-reviews/` + Telegram (always) |
| Sun 8:00pm | Claudian | `claudian_weekly_review.py` | Week's numbers across IG, listings, review queue. Wins, misses, one strategic question, action list. | `vault/04 Reviews/l Weekly Reviews l/` + Telegram (always) |

## What you get on the phone

**Daily**: 7am Telegram with morning brief. Plus alerts if Google traffic dropped or a Klaviyo flow flipped.

**Sunday**: 6pm IG performance summary, then 8pm strategic weekly review.

Quiet days stay quiet. The pricing snapshot, organic snapshot, and Klaviyo health all stay silent unless something actually changed. Morning brief and weekly review always send because they're scheduled checkpoints, not alerts.

## Known limitations

- **IG engagement is shallow**: Meta app doesn't have `instagram_manage_insights` permission, so the engagement review tracks `like_count` + `comments_count` only. No reach, no saves, no shares. Apply for that permission in Meta dev console to upgrade (or it stays "good enough" forever — likes + comments is usually enough signal for category-level decisions).
- **Google = GA4 only**: There's no Merchant Center API wired, so disapproval scans aren't automated yet. The organic snapshot replaces it as the daily Google signal because it actually uses what's connected.
- **Shop snapshot = Aydins only, no competitors**: Foundation is laid (it diffs your own catalog). Adding competitor URLs later is a 30-line patch to the same script.
- **Klaviyo monitors flow status, not send volume**: A flow could be live but sending 0 emails because the segment broke. That'd need the Klaviyo events endpoint, which is heavier. Add later if a stuck-but-live flow ever burns you.

## Klaviyo wiring (done same day)

- Key written to `/home/openclaw/.openclaw/agents/beta/credentials/klaviyo.env` (mode 600)
- BETA Klaviyo flipped from `not live` to `active` on dashboard (`scripts/dashboard_data_updater.py` line 174)
- 7 flows currently tracked: 5 live, 2 draft

## Crontab footprint

Six new entries in openclaw's crontab. View with `ssh openclaw@178.105.131.33 'crontab -l | tail -14'`. Logs in `command-center/logs/{script_name}.log`.

## To kill or pause any of them

```bash
ssh openclaw@178.105.131.33 'crontab -l > /tmp/cron.txt; nano /tmp/cron.txt; crontab /tmp/cron.txt'
```

Comment out the line, save, done. No restart needed.

## Files smoke-tested today

All six executed successfully against real data on the VPS before crontab install. Receipts in:
- `vault/01 Journals/2026 Journals/morning-briefs/2026-05-29-morning-brief.md`
- `vault/04 Reviews/l Weekly Reviews l/2026-05-29-weekly-review.md`
- `vault/brands/aydins/insta-weekly-reviews/2026-05-29-engagement.md`
- `command-center/work/beta-shop/pricing-snapshots/2026-05-29-snapshot.json`
- `command-center/work/beta-google/organic-snapshots/2026-05-29-snapshot.json`
- `command-center/work/beta-klaviyo/snapshots/2026-05-29-flow-snapshot.json`

## What to watch for in the first week

1. **Volume on Telegram**: if morning briefs feel noisy, we cut the bullet list shorter or move to silent push.
2. **GA4 false-alarm rate**: 30% drop threshold may be too sensitive at current low organic volume (yesterday=26 sessions, prior=22). Re-tune after a week of data.
3. **Klaviyo flow churn**: 2 flows in draft right now. If those stay draft for weeks, the daily check will keep flagging them as expected baseline — silence them by editing the diff function to only alert on transitions, not steady state. (Already does this — confirm it stays clean.)
4. **Weekly review usefulness**: The "one strategic question" is templated by metrics right now. After 2-3 weeks of data, swap the templated question for an LLM-generated one based on actual patterns.
