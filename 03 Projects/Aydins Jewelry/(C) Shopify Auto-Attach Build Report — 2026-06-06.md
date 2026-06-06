# Shopify Auto-Attach Build Report — 2026-06-06

## Status
Completed with one boundary-blocked product.

Amir approved live Shopify product media additions for the square 1:1 processed video only. The pipeline now attempts to attach each `{handle}-square.mp4` to the matching Shopify product page after conversion and package generation.

## Code changes

### Watcher extended
Updated:
`/home/openclaw/.openclaw/command-center/scripts/reel_pending_watcher.py`

Added behavior:
- Verifies product exists by Shopify handle.
- Snapshots current media list before attach to:
  `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/{handle}-pre-attach-{timestamp}.json`
- Uses `stagedUploadsCreate` with `resource: VIDEO`, `mimeType: video/mp4`, and required `fileSize`.
- Uploads the square 1:1 MP4 to Shopify staged storage.
- Calls `productCreateMedia` with `mediaContentType: VIDEO` to add media to the existing product.
- Re-fetches product media to verify a new VIDEO media entry exists.
- Updates canonical and dashboard package JSON with:
  - `posted_on.shopify`
  - `shopify_media_id`
  - `shopify_attached_at`
  - `pdp_url`
- Updates `reel-package-index.json` and busts dashboard cache.
- Adds Shopify 429 retry/backoff on GraphQL calls.
- Marks failed attaches in `state.json` so cron does not keep retrying failures.
- Queues NEEDS AMIR on blocked/failed attaches.
- Ignores helper MP4s in pending with `_vertical`, `_landscape_pp`, `-vertical`, or `-square` suffixes so derived files are not mistaken for Shopify handles.

### Dashboard UI updated
Updated:
`/home/openclaw/.openclaw/command-center/command-center-dashboard-tmp/components/ReelVideosSection.tsx`

Added fourth status badge:
- `On Shopify PDP`
- Green check when `posted_on.shopify === true`
- Gray/empty when false
- Click opens the PDP in a new tab

## Backfill results

Attached successfully to Shopify PDP:
1. AURIC — `gid://shopify/Video/40292242948333`
2. MERIDIAN — `gid://shopify/Video/40292243341549`
3. MIRAGE — `gid://shopify/Video/40292243439853`
4. NURGLE / KNIGHT — `gid://shopify/Video/40292286562541`
5. ODYSSEY — `gid://shopify/Video/40292243767533`

Blocked by explicit boundary:
- NEVAN — existing media count is 10, so auto-attach was skipped and queued to NEEDS AMIR.
  - Recommendation: clean up old product media first, then clear the reel pipeline attach failure state for retry.

## Verification

- `python3 -m py_compile` passed for `reel_pending_watcher.py`.
- Dashboard `npm run build` passed after UI badge update.
- Dashboard restarted through `start-dashboard.sh`.
- Dashboard data updater ran and preserved reel package metadata.
- `reel-package-index.json` count: `6`.
- Public dashboard package JSON shows:
  - 5 products with `posted_on.shopify: true` and `shopify_media_id` populated.
  - NEVAN with `posted_on.shopify: false` and no media id.
- Shopify Admin GraphQL media verification fetched all 6 products:
  - AURIC: media_count 10, video_count 1, attached video READY.
  - MERIDIAN: media_count 8, video_count 1, attached video READY.
  - MIRAGE: media_count 9, video_count 2, attached square video READY.
  - NEVAN: media_count 10, skipped due boundary.
  - NURGLE / KNIGHT: media_count 8, video_count 2, attached square video READY.
  - ODYSSEY: media_count 8, video_count 1, attached video READY.

## Stop-listed safety
- No public posts were made to Instagram, TikTok, or YouTube.
- No source videos were deleted.
- No existing Shopify product media was deleted or replaced.
- No product title, description, tags, price, inventory, or status changed.
- Only square 1:1 processed videos were attached.
