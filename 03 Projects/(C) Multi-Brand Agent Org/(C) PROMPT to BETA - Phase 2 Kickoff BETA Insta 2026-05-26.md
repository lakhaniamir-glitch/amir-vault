---
to: BETA
from: Amir
date: 2026-05-26
priority: High
type: Phase 2 kickoff - BETA Insta on Aydins with Gemini image gen
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Phase2_Kickoff_BETA_Insta_2026-05-26.md
---

# Phase 2 Kickoff: BETA Insta on Aydins (with Gemini image gen)

## Why this is happening earlier than the kickoff doc said

The original kickoff spec said Phase 2 starts after a 30-day Phase 1 stability gate. Amir is explicitly overriding that timing. Phase 1 went live tonight 2026-05-26; Phase 2 starts in parallel. Amir's call, logged here.

Risk Amir accepts: parallel debugging, possible attribution confusion if Shopify and IG issues compound. Mitigation: BETA must keep Phase 1 and Phase 2 work explicitly separated in logs, status files, and digests.

## Locked decisions (do not redesign)

1. **Account:** @aydinsjewelry on Instagram (business account, connected to Aydins Facebook Page)
2. **Cadence:** 1-2 posts per day, 7 days/week (NOT 3/day, that was reverted)
3. **Initial mode:** Manual approval for first batch. BETA produces 3-6 sample posts tonight/early morning, drops in Slack #beta-daily for Amir review before 7 AM Central 2026-05-27. Amir approves and replies "go auto" once happy. THEN BETA flips to auto mode (same pattern as Phase 1 live mode).
4. **Auto mode (after Amir approval):** BETA Insta drafts -> BETA Check validates -> auto-publish via IG Graph API -> post-publish verification -> auto-delete on failure with #beta-alerts ping
5. **Image strategy (Mix):**
   - **Product showcase posts (~60% of mix):** Use Gemini image-edit. Feed real Aydins Shopify product photo + prompt to add lifestyle scene around it. Preserves product accuracy. Use `gemini-2.5-flash-image` model.
   - **Lifestyle / educational / abstract posts (~40% of mix):** Pure text-to-image generation with Aydins visual direction baked into the prompt. Use `gemini-2.5-flash-image` for cheaper, `imagen-3.0-generate-002` as fallback for quality.
6. **Image hosting:** Upload generated images to Shopify Files (free, IG can read the CDN URL). Use Shopify Admin API `fileCreate` mutation. Tag uploaded files with `beta-insta-generated` for cleanup tracking.
7. **Image specs:** 1080x1350 (4:5 portrait, max IG real estate). Always.
8. **Content category mix:**
   - 40% product showcase (single ring hero shot in a scene + caption telling material/feature story)
   - 25% behind-the-scenes / engraving process / shop atmosphere
   - 20% customer / UGC reshare (if BETA detects a tag of @aydinsjewelry in a post and content is appropriate, draft a regram post)
   - 15% educational ("Tungsten vs titanium: which is right for you?", "How to choose a wedding band width")
9. **Posting times (Central):** 8 AM, 1 PM, 7 PM (jewelry/wedding audience peaks). At 1-2 posts/day, BETA picks 1-2 of these slots.
10. **Caption format:** Hook line (1 line, attention-grabbing) + product/story copy (2-4 short paragraphs) + soft CTA + 5-10 hashtags. Cap caption at 2,200 chars (IG limit).
11. **Hashtag strategy:** mix of brand (#aydinsjewelry), category (#mensweddingband, #tungstenring), material-specific (#fingerprintring, #blackring), niche-community (#weddingring, #grooms, #couples). NO #love spam tags, NO competitor brand tags.
12. **Voice:** Inherit from `brands/aydins/profile.md` (polished, masculine, high-end, direct). No em dashes anywhere. No bare "lifetime warranty". Irving Texas only when transactional.

## Credentials

Gemini API key stored in `/home/openclaw/.openclaw/agents/beta/credentials/gemini.env` (mode 600). Source it before any image gen call. Read `GEMINI_API_KEY`, respect `GEMINI_DAILY_BUDGET_USD=5.00` hard cap.

Instagram and Facebook Page tokens: NOT YET PROVIDED. Setup tasks below.

## Setup tasks (do these FIRST, in order, before any drafting)

### Setup Task 1: Verify Meta Developer App and IG Graph API access

Amir thinks he has a Meta Developer App but isn't sure of its state. Do not assume access works.

a. Inventory: probe what's available. If Amir has shared a Facebook Page admin token or app ID anywhere in `agents/beta/credentials/` or `agents/beta/config/`, find it.
b. If nothing exists, output a clear setup checklist for Amir:
   - Go to https://developers.facebook.com/apps/
   - Confirm there's an app with Instagram Graph API product added
   - Required permissions: `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, `business_management`
   - Generate a long-lived Page access token (System User token preferred for stability)
   - Note the IG Business Account ID (found via Graph API call `/me/accounts` -> page -> `/{page-id}?fields=instagram_business_account`)
   - Paste token + IG account ID into `agents/beta/credentials/meta.env` (Amir will provide; BETA does not create)
c. Until Setup Task 1 is complete, BETA Insta operates in DRAFT-ONLY MODE: drafts captions, generates images, but cannot publish.

### Setup Task 2: Inventory the existing @aydinsjewelry IG feed

Read the last 30 posts from @aydinsjewelry (via Graph API once available, or via public scrape if Graph API not yet wired). Analyze:
- Tone and voice of existing captions
- Hashtag patterns used
- Engagement patterns (likes, comments) by post type
- Visual style (lighting, composition, backgrounds)
- Posting frequency in last 60 days (likely low/none per Amir)

Output a brief baseline report to `work/phase2/aydinsjewelry-baseline-2026-05-27.md`. This becomes BETA Insta's reference for "what's already on-brand" vs "what's new direction".

### Setup Task 3: Gemini API smoke test

a. Source `credentials/gemini.env`.
b. Make a test image-edit call with `gemini-2.5-flash-image`: feed it any existing Aydins Shopify product photo URL + simple prompt like "Place this ring on a dark wood surface with warm side lighting, editorial macro style, 4:5 portrait."
c. Verify response. If image returned, save to `work/phase2/gemini-smoke-test-2026-05-27.png`.
d. Try a pure text-to-image call too: "Editorial photograph of a black tungsten men's wedding band on dark leather, warm lighting, macro composition, 4:5 portrait."
e. Confirm both image gen modes work and stay under budget cap.

### Setup Task 4: Shopify Files upload smoke test

a. Take the test image from Task 3.
b. Use Shopify Admin API `fileCreate` mutation to upload it as a file. Tag with `beta-insta-generated`, `phase2-smoke-test`.
c. Capture the resulting CDN URL.
d. Verify the URL is publicly accessible (curl it, expect 200 OK on the image bytes).
e. Confirm IG Graph API will accept this URL when publishing (Setup Task 1 dependent).

### Setup Task 5: Content calendar template

Build `brands/aydins/insta-content-calendar.json` with 14 days of planned post slots:
```json
{
  "generated_at": "ISO",
  "cadence": "1-2 per day",
  "lookahead_days": 14,
  "slots": [
    {
      "date": "2026-05-27",
      "time_central": "08:00",
      "category": "product_showcase | bts | ugc | educational",
      "status": "queued | drafted | approved | scheduled | published | rolled_back",
      "post_id": null,
      "draft_path": null
    }
  ]
}
```

Categories distributed per the 40/25/20/15 mix. Amir can edit this manually any time.

## Phase 2 worker flow (after Setup Tasks 1-5 complete)

### Pre-dawn drafting (runs at 4 AM Central daily)

1. Read `brands/aydins/insta-content-calendar.json`. Find slots for today with status `queued`.
2. For each slot:
   a. Pick a topic based on category (rotate through product SKUs, BTS topics, recent UGC tags, educational topic backlog).
   b. For product showcase: pull product image from Shopify CDN. Generate edited image via Gemini. For others: generate pure text-to-image.
   c. Upload image to Shopify Files. Get CDN URL.
   d. Draft caption (hook + body + CTA) following voice rules.
   e. Generate hashtag set (5-10 per spec).
   f. Save full post bundle to `work/phase2/drafts/<slot-id>-draft.json` with: image_url, caption, hashtags, scheduled_time, category, source_product_id (if applicable), gemini_prompt_used, gemini_cost_usd.
   g. Status: `drafted`.

### BETA Check (runs after each draft)

Validate against:
- No em dashes anywhere
- No bare "lifetime warranty"
- No third-party brand names (no Thorsten, no Universal Jewelry, no JCK, no competitor jewelers)
- No banned policy phrases in caption (warranty terms, return policy specifics, shipping promises beyond "free U.S. shipping")
- Hashtag count: 5-10
- Caption length: <= 2,200 chars
- Image URL: must be on Shopify CDN (`cdn.shopify.com`), publicly accessible
- Caption voice matches Aydins profile (polished, masculine, direct)
- No invented product claims (don't promise features not in the product data)
- No mention of "handcrafted/handmade/forged" (Aydins engraves and ships, doesn't manufacture)
- Hashtags: no spam tags (#love, #instagood, #photooftheday), no competitor brand tags

If any rule fails: status `rejected`, log reason, drop into `tasks/needs-amir-review.json`, do not publish.

### Pre-publish phase (manual approval first, auto-publish after Amir flips switch)

**Mode: MANUAL_APPROVAL_FIRST (initial state):**
- After each draft passes BETA Check, post the draft to Slack `#beta-daily` thread with:
  - Image (Slack inline render)
  - Caption preview
  - Hashtags
  - Scheduled time
  - Reply prompt: "Reply 'approve' to publish, 'reject [reason]' to redraft, 'edit [field]: [new value]' to patch"
- Wait for Amir's reply. Do not publish without explicit approval.
- After Amir replies "go auto" or "flip to auto mode" (any clear flip-the-switch phrase), update `brands/aydins/insta-config.json`:
```json
{
  "mode": "AUTO_PUBLISH",
  "amir_approved_auto_at": "ISO timestamp",
  "amir_approved_sample_posts": [array of draft IDs that were approved manually before the flip]
}
```

**Mode: AUTO_PUBLISH (after Amir flips):**
- After BETA Check passes, schedule the post via IG Graph API at the slot's scheduled time.
- Use the two-step Content Publishing flow:
  1. `POST /{ig-user-id}/media` with `image_url` and `caption` -> returns container ID
  2. `POST /{ig-user-id}/media_publish` with `creation_id` -> returns post ID
- Log the IG post ID.

### Post-publish verification (auto mode only)

1. Wait 60 seconds for IG to process.
2. Query the post via Graph API `/{ig-post-id}?fields=permalink,media_type,caption,media_url,is_comment_enabled`.
3. Verify:
   - Post is live (permalink resolves)
   - Caption matches draft (allow IG-side trimming for length)
   - Media URL is set (not failed render)
   - is_comment_enabled is true (not auto-restricted)
4. If verification passes: log to `tasks/done.json` with post ID, permalink, scheduled time, actual publish time, Gemini cost.
5. If verification fails: ROLLBACK. Call `DELETE /{ig-post-id}`. Log rollback reason to `tasks/rollbacks.json`. Hard alert to `#beta-alerts` with handle, time, reason, draft snapshot.

### Daily digest (existing 6 AM Central)

Add a Phase 2 section to the existing Phase 1 digest:

```
*Phase 2 Daily - Aydins Insta - <date>*

Yesterday:
- Published: <count> posts
  - 8:00 AM: <post permalink> (category, likes if available)
  - ...
- Rejected by BETA Check: <count>
- Rolled back: <count>
- Pending Amir approval (manual mode only): <count>

Today:
- Scheduled: <count> posts at <times>
  - 8:00 AM: <category> | image: <gemini cost>
  - ...

Queue health:
- Calendar slots filled next 14 days: <X>/<Y>
- Last 7 days published: <int>
- Total IG engagement (last 7d): <likes>, <comments>, <reach if available>

Gemini cost yesterday: $X.XX (cap $5/day)
```

## Cost discipline

- Gemini API cap: $5/day hard. Track every call's cost. If 80% of cap hit, slow down. If 100% hit, queue remaining slots for tomorrow and log.
- OpenRouter cap stays at $15/day for caption drafting (no change).
- No Anthropic/Claude API.

## Constraints (carry forward, do not violate)

- No publishing in AUTO mode until Amir flips the switch in Slack.
- No publishing in MANUAL mode without Amir's "approve" reply.
- No em dashes anywhere.
- No bare "lifetime warranty".
- Use Irving Texas only when transactional. Flower Mound only in marketing email footers (does not apply to IG captions).
- No supplier brand names (Thorsten, Universal Jewelry, JCK).
- No images of competitor products.
- No AI-generated images that misrepresent real Aydins product (rings rendered with wrong material, wrong color, wrong feature).
- Hard rule: ad spend changes, email sends, account/theme/domain changes, app installs all still require explicit Amir approval. This Phase 2 only covers IG organic publishing.

## Verification protocol

Tonight when Setup Tasks 1-5 are done (or as far as you can get without Amir's Meta tokens), report back with:

1. Path to and confirmation of `credentials/gemini.env` (do NOT paste the key).
2. Setup Task 1 result: status of Meta dev app verification. If creds present, confirm IG account ID. If not, list exactly what Amir needs to provide.
3. Setup Task 2: path to `work/phase2/aydinsjewelry-baseline-2026-05-27.md` with summary.
4. Setup Task 3: confirmation both Gemini modes work, total smoke test cost, path to test images.
5. Setup Task 4: Shopify Files CDN URL of the test upload, confirmation IG would accept it.
6. Setup Task 5: path to `brands/aydins/insta-content-calendar.json` with 14 days of slots.
7. First 3 sample post drafts ready in Slack `#beta-daily` thread for Amir review before 7 AM Central tomorrow. Each with: image, caption, hashtags, target slot/time, category.
8. md5 hashes of all new/modified files.
9. Confirm `agents/beta-insta.md` prompt is now active (not stub).
10. Cost spent tonight on setup tasks.

Post receipts to Slack `#beta-daily` and write full report to `/home/openclaw/.openclaw/command-center/work/phase2/phase2-kickoff-receipts-2026-05-27.md`.

## What Amir does next

1. Tomorrow morning: review the 3 sample posts in Slack `#beta-daily`.
2. Approve or send feedback in the thread.
3. Once happy with the format/voice, reply "flip to auto" (or any clear auto-mode signal).
4. From that point on, BETA Insta auto-publishes per the daily content calendar without Amir touching individual posts.
5. Amir watches `#beta-alerts` for rollbacks.

## Note on Meta dev app

If Amir's Meta dev app exists and has the right permissions, drop the tokens into `credentials/meta.env` (mode 600). If it doesn't exist, BETA outputs a setup checklist in tonight's report and operates in draft-only mode until Amir completes the Meta setup.

Either way, the 3 sample posts for tomorrow morning can be DRAFTS only (image generated + caption written, sitting in Slack). They don't need to publish yet. Publishing capability gets unlocked when Meta tokens are in place.
