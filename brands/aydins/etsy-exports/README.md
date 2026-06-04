---
created: 2026-05-29
purpose: VELA CSV dropbox for BETA Etsy Aydins listing rewrites
---

# Aydins Etsy CSV Dropbox

This folder is monitored by BETA Etsy on the VPS. Drop a VELA CSV export here, BETA picks it up within 30 minutes and drafts rewrites for the 5 weakest listings.

## How to use

1. Log into [vela.codes](https://vela.codes) → open Aydins shop
2. Select your listings (all of them, or a subset you want reviewed)
3. Hit **Export** → save the CSV
4. Drop the CSV file in this folder (this exact folder, your local vault)
5. Wait. Your local vault syncs to the VPS via GitHub every 10 minutes. Then BETA Etsy runs every 30 minutes. **Maximum delay from drop to drafts ready: ~40 minutes.**
6. Drafts land in `brands/aydins/etsy-rewrites/` next to this folder
7. Telegram pings you when drafts are ready

## What BETA picks

The 5 weakest listings in each CSV, scored on:
- Empty or short title (< 50 chars)
- Empty or thin description (< 200 chars)
- Fewer than 13 tags (Etsy lets you use 13, fewer = lost SEO)
- Soft-voice violations ("lovely", "beautiful", "elegant", "stunning")
- Banned manufacturing claims ("handcrafted", "handmade", "forged")
- Low views (more upside on rewrite)

## What BETA drafts per listing

- New title (Etsy 140-char limit, keyword-first, no fluff)
- New 13-tag set (Etsy 20-char-per-tag limit)
- New opening sentence
- New 150-220 word short description
- Rationale: what was wrong + what the rewrite fixes

## What BETA does NOT do

- Push live to Etsy or VELA. Drafts stay in vault for your review.
- Touch listings already in the needs-amir-review queue.
- Process the same CSV twice (tracked by filename in `command-center/work/beta-etsy/processed-csvs.json` on the VPS).

## CSV format BETA can read

BETA auto-detects common column names (case-insensitive):
- TITLE / Title / title / listing_title
- DESCRIPTION / Description / description / desc / long_description
- TAGS / tags / etsy_tags
- LISTING_ID / id / etsy_listing_id
- URL / listing_url / link
- VIEWS / views / view_count
- FAVORITES / favorites / favs

If your CSV uses something exotic, BETA will Telegram you the column names it found so you can rename and re-drop.

## Tested. Live.

Cron entry: `*/30 * * * *` (every 30 min, runs `beta_etsy_aydins_rewriter.py`).
