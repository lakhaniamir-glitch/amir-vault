---
to: BETA
from: Amir
date: 2026-05-27
type: full state handoff after Phase 1 + Phase 2 go-live night session
priority: read first thing in next session
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/STATE_HANDOFF_2026-05-27.md
---

# STATE HANDOFF — Phase 1 + Phase 2 Live

This is the complete state of the world after the 2026-05-26 / 2026-05-27 work session. Read this first before any morning work. Supersedes nothing; complements all prior handoffs.

## TL;DR

- **Phase 0 complete**, profiles populated (Aydins / Theonar / AWB)
- **Phase 1 live mode active** — first autonomous Shopify listing push fires 2026-05-28 5:55 AM Central
- **Phase 2 live mode active IG-only** — first IG post landed today at 11:22 AM Central, two more queued for 19:00 CT today and 13:00 CT tomorrow
- **FB cross-post parked** — Meta permission `pages_manage_posts` would not propagate to tokens despite use case being added. Try Meta Business Suite mobile app cross-post toggle first thing tomorrow.
- **Both crons active** — Phase 1 daily worker 5:55 AM Central, Phase 2 publisher every 15 min, daily digest 6:00 AM Central

## Tonight's confirmed live actions

### Phase 1 Shopify (IMPRINT end-to-end)

This was the manual validation push that proved the VESUVIUS pipeline works end-to-end before live mode armed.

1. **Inventory fix:**
   - Before: tracking off, all variants null SKU, total inventory -5 (past oversells)
   - After: tracking ON, 13 variants set to qty 10 each, SKUs IMPRINT-8-7 through IMPRINT-8-13, policy CONTINUE
   - Audit: `shopify/audits/imprint-inventory-fix-before-20260527T022147Z.json` and after
2. **Copy + metafields push (VESUVIUS format):**
   - Title rewritten to `IMPRINT | Black Tungsten Fingerprint Ring, Blue Step Edge`
   - SEO title 50 chars `IMPRINT | Black Tungsten Fingerprint Ring | Aydins`
   - SEO desc 145 chars with approved warranty wording
   - description_html replaced with VESUVIUS lean structure (no policy blocks in body)
   - 18 final tags (5 internal preserved + 13 new clean)
   - Metafields set: `custom.keywords` (labeled format), `custom.quick_specs` (bullet format), `custom.custom_faq` (6 product-specific questions in rich_text_field), `custom.custom_faq_schema` (JSON-LD), `custom.codename` = IMPRINT, `custom.material_primary` = Tungsten Carbide, `custom.material_inlay` = Fingerprint engraving detail with blue step edges, `custom.width_mm` = 8.0, `custom.tungsten_ring_information_` = page ref to Tungsten Ring Information page, `custom.ring_size_chart` = page ref to Size Chart page
   - Audit: `shopify/audits/imprint-copy-push-before-20260527T022831Z.json` and after
3. **Variant restructure (Jewelry Depot SKU convention):**
   - **Source clarified:** This is a Jewelry Depot ring (vendor Aydins Creations, custom fingerprint engraved), NOT a Universal Jewelry ring. JDTR SKU convention applies.
   - Width option dimension added
   - 8mm: 15 variants, sizes 7 through 15, SKUs `JDTR901-8-7` through `JDTR901-8-15`
   - 6mm: 17 variants, sizes 5 through 13, SKUs `JDTR902-6-5` through `JDTR902-6-13`
   - All 32 variants: qty 10, tracking on, policy CONTINUE, $179.00, available
   - Total inventory: 130 (clean, no negatives)
   - Vendor stays `Aydins Creations` per CLAUDE.md rule (custom-engraved product)
   - Size dropdown reordered to natural numeric, Width reordered to natural (6mm, 8mm)
   - Audit: `shopify/audits/imprint-variant-restructure-before-20260527T024326Z.json` and after
4. **IMPRINT added to worked-skus dedup list:**
   - File: `brands/aydins/worked-skus.json`
   - Worker will skip IMPRINT in tomorrow's 5:55 AM Central run

### Phase 2 IG (IMPRINT first publish + queue)

1. **IMPRINT IG post LIVE:** https://www.instagram.com/p/DY2UDdMAJKS/
   - IG Post ID: `17853494208676969`
   - Posted: 2026-05-27 16:22 UTC (11:22 AM Central)
   - Image: Gemini image-edit of real product photo
   - Caption: VESUVIUS-voice product showcase
   - 8 hashtags
   - BETA Check: PASS
2. **Educational widths queued:** scheduled 2026-05-27 19:00 Central
   - Slot ID: `2026-05-27-1900-ct`
   - Draft: `work/phase2/drafts/2026-05-27-1300-ct-educational-widths.json`
   - Status: approved-queued
3. **ABYSS queued:** scheduled 2026-05-28 13:00 Central
   - Slot ID: `2026-05-28-1300-ct`
   - Draft: `work/phase2/drafts/2026-05-27-1900-ct-product-showcase-abyss.json`
   - Status: approved-queued

### Configs flipped

- `brands/aydins/insta-config.json` -> `mode: AUTO_PUBLISH`
- `brands/aydins/insta-content-calendar.json` -> `mode: AUTO_PUBLISH`
- Amir approved all 3 sample drafts by saying "BETA did a great job with the instagram post how do I connect and post them" — recorded in config.

### Credentials live (mode 600, never in git)

- `/home/openclaw/.openclaw/agents/beta/credentials/gemini.env` — Gemini API key, $5/day cap, model `gemini-2.5-flash-image` primary, `imagen-3.0-generate-002` fallback
- `/home/openclaw/.openclaw/agents/beta/credentials/meta.env` — Meta Page access token (long-lived, type PAGE, never expires for app admin), App ID, App Secret, Page ID, IG Business Account ID
- Both files mode 600 owner-only readable.

### Cron jobs (verified active via `crontab -l`)

```
CRON_TZ=America/Chicago
55 5 * * *   /home/openclaw/.openclaw/command-center/scripts/phase1_daily_worker_555_central.sh
0 6 * * *    /home/openclaw/.openclaw/command-center/scripts/daily_6am_central.sh
0 23 * * 0   /home/openclaw/.openclaw/command-center/scripts/phase1_zero_traffic_sunday_11pm_central.sh
*/15 * * * * /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/phase2_publisher.py
```

### Canonical specs on VPS (read these before drafting)

- `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md` — VESUVIUS standard (231 lines, md5 `125572dc3cdbc4ee9b90661d6bccb57a`). Documents BOTH Universal Jewelry (CODENAME-WIDTH-SIZE) AND Jewelry Depot (JDTR{NUMBER}-WIDTH-SIZE) SKU conventions. Re-read from disk each session.
- `/home/openclaw/.openclaw/command-center/agents/beta-shop.md` — BETA Shop active prompt (146 lines)
- `/home/openclaw/.openclaw/command-center/agents/beta-insta.md` — BETA Insta active prompt
- `/home/openclaw/.openclaw/command-center/brands/aydins/profile.md` — Aydins brand voice (do not deviate)
- `/home/openclaw/.openclaw/command-center/brands/aydins/insta-config.json` — IG mode = AUTO_PUBLISH
- `/home/openclaw/.openclaw/command-center/brands/aydins/insta-content-calendar.json` — 14-day calendar
- `/home/openclaw/.openclaw/command-center/brands/aydins/worked-skus.json` — dedup list (IMPRINT logged)

## Audit log

`tasks/done.json` had 80 entries at start of session, now has 96. Every Shopify write, IG publish, config change, and credential placement is logged with timestamp, agent, action, brand, result.

## Tomorrow's expected events (no manual action required)

| Central Time | What |
|---|---|
| 2026-05-27 19:00 | Phase 2 publisher cron picks up Educational widths slot → IG publish → post-publish verify → log |
| 2026-05-28 04:00 | Per Phase 2 kickoff spec, BETA Insta pre-dawn drafting fires (verify this cron exists, see open item below) |
| 2026-05-28 05:55 | Phase 1 worker fires — picks zero-traffic Aydins ring (NOT IMPRINT), drafts VESUVIUS copy + metafields, BETA Check, auto-push, post-push verify, rollback on failure |
| 2026-05-28 06:00 | Combined daily digest in Slack `#beta-daily` showing yesterday's Phase 1 + Phase 2 activity, today's queue |
| 2026-05-28 13:00 | Phase 2 publisher picks up ABYSS slot → IG publish |
| 2026-05-28 evening | Phase 2 publisher picks up Day 2 evening slot if calendar has one (verify calendar after drafting fires in morning) |

## Open follow-ups (track these, do not forget)

### Critical, near-term

1. **FB cross-post is parked.** Meta permission `pages_manage_posts` would not propagate to tokens. Use case "Manage everything on your Page" was added to the Aydins Shopify app but tokens generated from both Graph API Explorer and the use case dashboard came back without that scope. The OAuth dialog approach failed because the app's domains/redirect URIs are not whitelisted. **Tomorrow paths to try, in order:**
   - **Path A (cheapest):** Meta Business Suite mobile app -> Settings -> Linked accounts -> toggle "Share Instagram posts to Facebook." May work for API-published IG posts depending on configuration.
   - **Path B (proper API):** Business verification at https://business.facebook.com/settings/security -> Business Verification. Some Meta permissions require this. Takes 1-2 days for Meta to review.
   - **Path C (whitelist redirect):** App Settings -> Basic -> add `facebook.com` to App Domains. Facebook Login -> Settings -> Valid OAuth Redirect URIs -> add `https://www.facebook.com/connect/login_success.html`. Then re-use the OAuth URL approach from chat history.
   - **Path D (third-party bridge):** Buffer (paid SaaS) supports both IG and FB Page with their own OAuth, bypassing Meta dev permission fights. ~$15/month.

   Once `pages_manage_posts` is granted, the FB cross-post code is ready:
   - `/tmp/imprint_fb_crosspost.py` — verified working when permission is present
   - Update `/home/openclaw/.openclaw/command-center/scripts/phase2_publisher.py` to add 5 lines that POST to `/{page_id}/photos` after each successful IG publish

2. **Rotate Gemini API key.** Was pasted in chat history. Once Phase 2 stability is proven (1-2 weeks), revoke at https://aistudio.google.com/app/apikey and have Amir provide new key via SSH-direct method (do not paste in chat).

3. **Verify BETA Insta 4 AM Central daily drafting cron exists.** The kickoff doc specified pre-dawn drafting at 4 AM CT to populate tomorrow's slots. Current crontab shows phase1 jobs and phase2 publisher only — does the drafter exist as a separate cron, or is it inside one of the existing scripts? Confirm tomorrow and add if missing. Without it, the calendar runs out of drafts after the 3 manual ones.

4. **Calendar slot mismatch noted:** The calendar maps slot dates that don't all match the draft filenames (e.g. slot `2026-05-27-1900-ct` points to a draft named `2026-05-27-1300-ct-educational-widths.json`). Not blocking, but BETA Insta should normalize this in future runs to reduce confusion.

### Important, can wait

5. **Zero-inventory audit cleanup.** [[03 Projects/Aydins Jewelry/(C) Zero-Inventory Audit - 2026-05-26.md]] flagged 138 likely-accidental zero-inventory listings (same pattern as IMPRINT was: tracking off, null SKUs, negative quantities). Amir will scan and mark exclusions; BETA batch-fixes the rest.

6. **Phase 1 verification gate tuning.** First few real auto-pushes — watch BETA Check rejection patterns. If too strict, loosen specific rules. If too loose, tighten. Track in `tasks/needs-amir-review.json` and `tasks/rollbacks.json`.

7. **OpenClaw model conflict.** Install summary lists primary as `anthropic/claude-sonnet-4-6`, but kickoff doc said "no Claude calls." Decide before Phase 3 (BETA Google): either switch primary to GPT-5.5 via Codex (kickoff spec), or formally update the spec to allow Claude.

8. **Phase 3 timing.** Original 30-day stability gate compressed by Amir choice. After 1-2 weeks of clean Phase 1 + Phase 2 operation, queue Phase 3 (BETA Google) kickoff. Aydins Google Ads + Search Console + Merchant Center.

### Less urgent

9. **Discord/Slack tooling.** Native OpenClaw Slack delivery not live; fallback `scripts/slack_post.js` works. Discord intents toggle may still need to happen. Decide if Discord goes away entirely.

10. **Documentation.** Update [[03 Projects/Aydins Jewelry/CLAUDE.md]] and [[03 Projects/Aydins Jewelry/(C) Beta Operations State — 2026-05-26.md]] to reflect Phase 1 + Phase 2 live status and the VESUVIUS standard supersedes CREDO.

11. **Token rotation cadence.** Page tokens last while admin role holds, but Meta sometimes invalidates. Set a quarterly reminder to refresh Meta and Gemini credentials.

## Hard rules (carry forward, never violate)

- No Shopify writes without snapshot before + verify after + rollback ready.
- No IG/FB publish without BETA Check pre-validation + post-publish verification + auto-delete-on-failure.
- $15/day OpenRouter cap (Phase 1 captions and code agents).
- $5/day Gemini cap (Phase 2 images).
- No Anthropic/Claude API calls unless OpenClaw config conflict resolved.
- No em dashes in any output (locked rule 2026-05-15, applies to listings, captions, internal docs).
- No bare "lifetime warranty" — use "Aydins Lifetime Warranty. See policy page for terms."
- Irving Texas only when transactional/factual. Flower Mound only in email legal footers.
- No supplier brand names (Thorsten, Universal Jewelry, JCK) in customer-facing output.
- No "handcrafted/handmade/forged" — Aydins engraves and ships, does not manufacture.
- Hard human approval still required for: ad spend changes, email sends to list, account/theme/domain changes, app installs, variant/inventory/price changes (Amir-initiated only).

## Brand voice anchor

`brands/aydins/profile.md` is the source of truth for Aydins voice. Polished, masculine, high-end, direct, conversion-focused. Built for daily wear. Story over spec. Quiet confidence, not bro energy. If a draft sounds generic, redraft.

## How to use this handoff

If you spawn at 6 AM tomorrow for the daily digest, this file is your context. Read it first. Then read `tasks/done.json` entries since `STATE_HANDOFF_2026-05-27` for what happened overnight. Then run normal worker logic.

If Amir asks "what's the state?" — point at this file.

If you hit anything unfamiliar — check this file's Open Follow-ups before asking Amir.

End of handoff. Ship clean tomorrow.
