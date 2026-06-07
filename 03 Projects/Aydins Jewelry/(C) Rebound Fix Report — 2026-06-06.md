# Rebound Fix Report — 2026-06-06

## Status
Completed. The square video generation bug is fixed, 8 approved wrong Shopify media items were removed, the wrong calendar slots were blocked, and corrected rebound squares were regenerated. Five corrected videos were re-attached to the correct Shopify PDPs. NEVAN remains blocked by Shopify 10-media limit.

## Code change
- Updated `/home/openclaw/.openclaw/command-center/scripts/reel_pending_watcher.py`.
- Snapshot: `/home/openclaw/.openclaw/agents/beta/backups/reel_pending_watcher.py.pre-rebound-fix-2026-06-06`.
- Square generation now uses a real rebound graph: 1080x1080 center crop, forward segment, reversed segment, `xfade` 0.4s transition, 0.3s ease-in, 0.3s ease-out, `libx264`, `yuv420p`, `+faststart`.

## 8 wrong Shopify media deleted
- `gid://shopify/Video/40292242948333` on `auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay` — status `deleted_verified` — count `10` → `9`.
  - Alt: Aydins AURIC | Gold Tungsten Ring square product video auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay-square.mp4
  - URL: https://cdn.shopify.com/videos/c/vp/96442fa915564443986f7e0ad19652bf/96442fa915564443986f7e0ad19652bf.SD-480p-0.9Mbps-85887273.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay-pre-cleanup-20260606T235415Z.json`
- `gid://shopify/Video/40292243341549` on `meridian-flat-titanium-ring-purple-blue-diamond-pattern` — status `deleted_verified` — count `8` → `7`.
  - Alt: Aydins MERIDIAN | Flat Titanium Ring, Purple and Blue Diamond Pattern square product video meridian-flat-titanium-ring-purple-blue-diamond-pattern-square.mp4
  - URL: https://cdn.shopify.com/videos/c/vp/e4872479f77b44d8a773350e387713d1/e4872479f77b44d8a773350e387713d1.SD-480p-1.2Mbps-85887276.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/meridian-flat-titanium-ring-purple-blue-diamond-pattern-pre-cleanup-20260606T235416Z.json`
- `gid://shopify/Video/40292243439853` on `mirage-black-tungsten-ring-alexandrite-and-goldstone-inlay-flat` — status `deleted_verified` — count `9` → `8`.
  - Alt: Aydins MIRAGE | Black Tungsten Ring, Alexandrite and Goldstone Inlay, Flat square product video mirage-black-tungsten-ring-alexandrite-and-goldstone-inlay-flat-square.mp4
  - URL: https://cdn.shopify.com/videos/c/vp/69f2c643749243bcb635add507ffa2d0/69f2c643749243bcb635add507ffa2d0.SD-480p-0.9Mbps-85887278.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/mirage-black-tungsten-ring-alexandrite-and-goldstone-inlay-flat-pre-cleanup-20260606T235417Z.json`
- `gid://shopify/Video/40292286562541` on `nurgle-black-diamond-titanium-wedding-ring` — status `deleted_verified` — count `8` → `7`.
  - Alt: Aydins KNIGHT | Black Titanium Steel Chain Black Diamond Wedding Ring — 8mm square product video nurgle-black-diamond-titanium-wedding-ring-square.mp4
  - URL: https://cdn.shopify.com/videos/c/vp/566db342a994419185c41f8f72d21778/566db342a994419185c41f8f72d21778.SD-480p-0.9Mbps-85887324.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/nurgle-black-diamond-titanium-wedding-ring-pre-cleanup-20260606T235418Z.json`
- `gid://shopify/Video/40292243767533` on `odyssey-black-ceramic-ring-carpathian-elm-wood-inlay` — status `deleted_verified` — count `8` → `7`.
  - Alt: Aydins ODYSSEY | Black Ceramic Ring, Carpathian Elm Wood Inlay square product video odyssey-black-ceramic-ring-carpathian-elm-wood-inlay-square.mp4
  - URL: https://cdn.shopify.com/videos/c/vp/36314018a3bb4fb0bea0ffeab587fa4b/36314018a3bb4fb0bea0ffeab587fa4b.SD-480p-0.9Mbps-85887280.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/odyssey-black-ceramic-ring-carpathian-elm-wood-inlay-pre-cleanup-20260606T235419Z.json`
- `gid://shopify/Video/40258677145837` on `leporis-black-tungsten-ring-round-cut-white-cz` — status `deleted_verified` — count `5` → `4`.
  - Alt: Aydins LEPORIS | Black Tungsten Ring, Diamond Stimulant CZ Eternity, Flat cinematic showcase video, leather library aesthetic, seamless loop
  - URL: https://cdn.shopify.com/videos/c/vp/ca08b09e155649a4b53961b01d6bbd15/ca08b09e155649a4b53961b01d6bbd15.SD-480p-1.5Mbps-85730421.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/leporis-black-tungsten-ring-round-cut-white-cz-pre-cleanup-20260606T235420Z.json`
- `gid://shopify/Video/40292237967597` on `devilblood-black-tungsten-ring-red-groove-with-red-tungsten-inside` — status `deleted_verified` — count `7` → `6`.
  - Alt: Aydins DEVILBLOOD | Red Ring, Black Tungsten Ring, Red Groove, Stepped Edge cinematic showcase video, moss forest aesthetic, seamless loop
  - URL: https://cdn.shopify.com/videos/c/vp/68c64e5eb3c04c92a308e1a5cc831103/68c64e5eb3c04c92a308e1a5cc831103.SD-480p-1.2Mbps-85887251.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/devilblood-black-tungsten-ring-red-groove-with-red-tungsten-inside-pre-cleanup-20260606T235421Z.json`
- `gid://shopify/Video/40292244783341` on `devilblood-black-tungsten-ring-red-groove-with-red-tungsten-inside` — status `deleted_verified` — count `6` → `5`.
  - Alt: Aydins DEVILBLOOD | Red Ring, Black Tungsten Ring, Red Groove, Stepped Edge cinematic showcase video, moss forest aesthetic, seamless loop
  - URL: https://cdn.shopify.com/videos/c/vp/e1b9a4fd33d74979a270a38ac9768a02/e1b9a4fd33d74979a270a38ac9768a02.SD-480p-1.2Mbps-85887286.mp4
  - Snapshot: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/shopify-snapshots/devilblood-black-tungsten-ring-red-groove-with-red-tungsten-inside-pre-cleanup-20260606T235422Z.json`

## Calendar slots canceled
- Target slots: `2026-06-05-0800-ct`, `2026-06-11-0800-ct`, `2026-06-11-1300-ct`.
- Calendar backup: `/home/openclaw/.openclaw/agents/beta/backups/insta-content-calendar.json.pre-rebound-cleanup-2026-06-06`
- Calendar entries changed: `5`. Note: `2026-06-05-0800-ct` had duplicate calendar entries, so all matching duplicates were marked safe.
- `2026-06-05-0800-ct` — Meridian video on Leporis tag — set `status=canceled-wrong-product-video`, `mode=DRAFT_ONLY`, `auto_publish_blocked=true`, `do_not_publish=true`.
- `2026-06-05-0800-ct` — Meridian video on Leporis tag — set `status=canceled-wrong-product-video`, `mode=DRAFT_ONLY`, `auto_publish_blocked=true`, `do_not_publish=true`.
- `2026-06-05-0800-ct` — Meridian video on Leporis tag — set `status=canceled-wrong-product-video`, `mode=DRAFT_ONLY`, `auto_publish_blocked=true`, `do_not_publish=true`.
- `2026-06-11-0800-ct` — Nurgle video on Devilblood tag — set `status=canceled-wrong-product-video`, `mode=DRAFT_ONLY`, `auto_publish_blocked=true`, `do_not_publish=true`.
- `2026-06-11-1300-ct` — Auric video on Devilblood tag — set `status=canceled-wrong-product-video`, `mode=DRAFT_ONLY`, `auto_publish_blocked=true`, `do_not_publish=true`.
### Draft files changed
- `/home/openclaw/.openclaw/command-center/work/phase2/drafts/2026-06-05-0800-ct-product-showcase.json` — backup `/home/openclaw/.openclaw/agents/beta/backups/2026-06-05-0800-ct-product-showcase.json.pre-rebound-cleanup-2026-06-06` — DRAFT_ONLY/canceled-wrong-product-video.

## Regenerated rebound squares
- `auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay` — duration `7.125s`, duration_ok `True`, Shopify `True`, media `gid://shopify/Video/40292483825901`.
- `meridian-flat-titanium-ring-purple-blue-diamond-pattern` — duration `7.125s`, duration_ok `True`, Shopify `True`, media `gid://shopify/Video/40292485431533`.
- `mirage-black-tungsten-ring-alexandrite-and-goldstone-inlay-flat` — duration `7.125s`, duration_ok `True`, Shopify `True`, media `gid://shopify/Video/40292487037165`.
- `nevan-black-tungsten-ring-espresso-groove` — duration `7.125s`, duration_ok `True`, Shopify `False`, media `None`.
- `nurgle-black-diamond-titanium-wedding-ring` — duration `7.125s`, duration_ok `True`, Shopify `True`, media `gid://shopify/Video/40292490477805`.
- `odyssey-black-ceramic-ring-carpathian-elm-wood-inlay` — duration `7.125s`, duration_ok `True`, Shopify `True`, media `gid://shopify/Video/40292492574957`.

## Shopify re-attach results
- Attached corrected rebound square: `auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay` → `gid://shopify/Video/40292483825901`.
- Attached corrected rebound square: `meridian-flat-titanium-ring-purple-blue-diamond-pattern` → `gid://shopify/Video/40292485431533`.
- Attached corrected rebound square: `mirage-black-tungsten-ring-alexandrite-and-goldstone-inlay-flat` → `gid://shopify/Video/40292487037165`.
- Attached corrected rebound square: `nurgle-black-diamond-titanium-wedding-ring` → `gid://shopify/Video/40292490477805`.
- Attached corrected rebound square: `odyssey-black-ceramic-ring-carpathian-elm-wood-inlay` → `gid://shopify/Video/40292492574957`.
- Blocked: `nevan-black-tungsten-ring-espresso-groove` — Shopify product already has 10 media items, queued to NEEDS AMIR for media cleanup before retry.

## Verification
- `python3 -m py_compile` passed for `reel_pending_watcher.py`.
- All 8 deleted media IDs verified absent from their products.
- Five newly attached corrected Shopify videos verified present and READY.
- Six regenerated square MP4s verified at ~7.125s.
- Dashboard package index count is 6 and Shopify badge state is true for 5, false for NEVAN.
- Verification artifact: `/home/openclaw/.openclaw/command-center/work/reel-pipeline/rebound-fix-verification.json`.

## Stop-listed safety
- No product media was deleted beyond the 8 explicitly approved media GIDs.
- No product title, description, tags, price, inventory, or status changed.
- Source landscape MP4 files were not deleted. AURIC and ODYSSEY were copied back from `approved/` to `pending/` for processing only.
- Dashboard component was not modified. Package/index writes were limited to Shopify status updates from the watcher.
- No Instagram, TikTok, YouTube, or public social posts were made.
