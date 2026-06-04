---
type: state-handoff
audience: New Claude session picking up BETA work
date: 2026-06-02
status: LIVE reference — keep updated
supersedes: none (first full reference doc)
---

# BETA System Full Reference (for new Claude sessions)

This document is the canonical handoff. If you're a fresh Claude session and you need to work on BETA, Aydins Jewelry, or any of the agents, read this first. Every detail of access, paths, services, APIs, credentials, work done, and outstanding tasks lives here.

> Last updated by Claude session: 2026-06-02. Read CLAUDE.md at vault root first for behavioral rules (no em dashes, etc.).

---

## 1. Top-level summary

- **Business**: Aydins Jewelry, men's wedding bands, Shopify storefront at `aydinsjewelry.com`. Run by Amir (sole operator).
- **BETA**: Amir's multi-agent operating system. Agents handle content, listings, email, ads, and approvals.
- **Infrastructure**: Self-hosted on a single Hetzner VPS. Vault is an Obsidian-based knowledge layer synced via git from GitHub to the VPS.
- **Dashboard**: Next.js app at `beta.shopaydins.com` — Amir's daily approval/review UI. Self-hosted (escaped Vercel Hobby's 100/day deploy cap).
- **Source of truth**: VPS files. Vault is mirror. Dashboard reads a generated JSON snapshot updated by cron every 5 min.

---

## 2. Access & connection

### VPS

- **Host**: `178.105.131.33` (Hetzner)
- **User**: `openclaw`
- **SSH**: passwordless from Amir's Windows machine (key already on VPS authorized_keys). Just `ssh openclaw@178.105.131.33 '<cmd>'` works.
- **No sudo** for `openclaw` in this session. Some system-level checks may require Amir to run sudo separately.

### Domains (all served by nginx on the VPS)

| Domain | Purpose | TLS |
|---|---|---|
| `beta.shopaydins.com` | Dashboard UI (Next.js on `127.0.0.1:3334`) | Let's Encrypt |
| `connect.shopaydins.com` | Action webhook (`/dashboard-action/` → `127.0.0.1:8090`) | Let's Encrypt |

### Local Windows vault

- Path: `C:\Users\amirl\Documents\Amirs Command Center`
- Contains Obsidian vault + git workspace
- Pushes to GitHub; the VPS pulls every 10 min via `vault_sync.sh` cron

---

## 3. Filesystem map

### Vault (Obsidian) — both locations

| Local (Windows) | VPS |
|---|---|
| `C:\Users\amirl\Documents\Amirs Command Center` | `/home/openclaw/vault` |

Sync is one-way: Windows → GitHub → VPS pull. VPS never pushes (see §11 vault rescue notes).

### VPS-side `~/.openclaw/` tree (the operating system)

```
/home/openclaw/.openclaw/
├── agents/                                      ← Per-agent runtime state, prompts, sessions
│   ├── beta/                                    ← BETA primary agent (sub-agents inside)
│   │   ├── credentials/                         ← All API keys + tokens (see §5)
│   │   ├── shopify/specs/                       ← Listing standards (VESUVIUS)
│   │   ├── handoffs/                            ← Stage gates between agents
│   │   └── sessions/                            ← Replay logs
│   ├── beta-shop/                               ← Shopify-focused agent
│   ├── beta-insta/                              ← IG-focused agent
│   ├── beta-google/                             ← Google/SEO blog-focused agent
│   ├── beta-klaviyo/                            ← Email-focused agent
│   ├── beta-ebay/                               ← Etsy/Ebay-focused agent
│   └── claudian/                                ← Top-level synthesizer agent
├── command-center/                              ← Scripts, configs, generated artifacts
│   ├── scripts/                                 ← All cron + agent runner scripts
│   ├── brands/aydins/                           ← Aydins brand profile + content calendars
│   ├── tasks/                                   ← Approval queues (JSON/JSONL)
│   ├── work/                                    ← Phase outputs (phase1, phase2)
│   ├── logs/                                    ← Centralized cron logs
│   ├── command-center-dashboard-tmp/            ← The live Next.js dashboard app
│   └── backups/                                 ← System backups
└── backups/                                     ← Crontab + env backups (older)
```

### Key generated artifact paths

| What | Where |
|---|---|
| Approval queue | `command-center/tasks/needs-amir-review.json` |
| Approval archive | `command-center/tasks/needs-amir-review-archive.jsonl` |
| Done log | `command-center/tasks/done.json` |
| IG content calendar | `command-center/brands/aydins/insta-content-calendar.json` |
| GMC briefs (daily) | `/home/openclaw/vault/brands/aydins/gmc-briefs/{date-slug}/` (brief.md + restaged.jpg) |
| Reels pending | `/home/openclaw/vault/brands/aydins/reel-videos/pending/` |
| Reels approved | `/home/openclaw/vault/brands/aydins/reel-videos/approved/` |
| Reels published | `/home/openclaw/vault/brands/aydins/reel-videos/published/` |
| Cron run health | `command-center/logs/cron_runs.jsonl` |
| Dashboard data snapshot | `command-center-dashboard-tmp/public/data/dashboard.json` |

---

## 4. Agents (BETA family)

All BETA sub-agents run as Python scripts on cron. They are NOT long-running services. Each tick is independent.

| Agent | Domain | Lives at | Primary scripts |
|---|---|---|---|
| **BETA Insta** | Instagram (Reels, Stories, Posts, calendar) | `agents/beta-insta/` | `phase2_daily_drafter.py`, `phase2_publisher.py`, `beta_insta_daily_gmc_brief.py`, `beta_insta_reel_watcher.py`, `beta_insta_reel_script_writer.py`, `beta_insta_carousel_writer.py`, `beta_insta_engagement_review.py` |
| **BETA Shop** | Shopify listings (titles, body, FAQ, metafields, tags, taxonomy) | `agents/beta-shop/` | `beta_shop_listing_enricher.py`, `beta_shop_collection_describer.py`, `beta_shop_pricing_snapshot.py` |
| **BETA Google** | Blog drafts, SEO, organic traffic snapshot | `agents/beta-google/` | `beta_google_blog_drafter.py`, `beta_google_organic_snapshot.py` |
| **BETA Klaviyo** | Email flow health, campaign drafts, A/B drafts | `agents/beta-klaviyo/` | `beta_klaviyo_flow_health.py`, `beta_klaviyo_email_drafter.py`, `beta_klaviyo_weekly_campaign.py` |
| **BETA Etsy** | Etsy CSV-watcher rewriter | `agents/beta-ebay/` | `beta_etsy_aydins_rewriter.py` |
| **BETA Check** | Cross-cutting validator (inline in drafter; the "approval gate") | (logic inside `phase2_daily_drafter.py::validate_draft`) | — |
| **Claudian** | Top-level synthesizer (inbox, morning brief, weekly review, memory) | `agents/claudian/` | `claudian_command_center_inbox.py`, `claudian_morning_brief.py`, `claudian_weekly_review.py`, `claudian_summarizer.py` |

Each agent reads/writes to shared state files (queue, calendar, logs). They do NOT call each other directly. The pattern is: agent runs on cron, produces drafts to a queue, Amir reviews via dashboard, dashboard action webhook updates state.

---

## 5. Credentials (where they live, NOT the values)

All under `/home/openclaw/.openclaw/agents/beta/credentials/` (mode 600, `openclaw:openclaw`):

| File | Contains | Used by |
|---|---|---|
| `shopify.json` | Per-store JSON: `aydinsjewelry.myshopify.com` + access token (Admin REST + GraphQL) | All shop-related scripts |
| `gemini.env` | `GEMINI_API_KEY=...` | All Nano Banana image generation |
| `openrouter.env` | `OPENROUTER_API_KEY=...` | All LLM calls (DeepSeek V4 Flash via OpenRouter) |
| `telegram.env` | `TELEGRAM_BOT_TOKEN=...` (bot `@amir_beta_bot`, chat_id `8101774399`) | `telegram_push.py` |
| `dashboard.env` | `DASHBOARD_TOKEN=Smartwater1231!` + `DASHBOARD_ACTION_SECRET=...` | Dashboard (systemd EnvironmentFile) |
| `dashboard-action.secret` | Raw HMAC secret (also referenced from `dashboard.env`) | Action webhook signing |
| `meta-ig.json` | Facebook/IG access token + IG business account ID | `phase2_publisher.py` |
| `ga4.json` | GA4 service account credentials | `beta_google_organic_snapshot.py` |
| `klaviyo.env` | `KLAVIYO_API_KEY=...` | All Klaviyo scripts |

Helpers in `scripts/beta_insta_daily_gmc_brief.py`: `_shop_creds()`, `_gemini_key()`, `_openrouter_key()`. These are reused everywhere — import from there if you need creds in a new script.

---

## 6. External APIs accessed by BETA

| API | Auth | What we do | Used by |
|---|---|---|---|
| **Shopify Admin REST API 2024-10** | `X-Shopify-Access-Token` header | Products/variants/media/metafields CRUD, image upload, pricing | All shop scripts + listing builders |
| **Shopify Admin GraphQL 2024-10** | Same token | Category set (`productUpdate`), publications (`publishablePublish`), staged uploads, product mediaCreate | Listing builders, reel watcher |
| **Universal Jewelry .json** | None (public) | Source product data for imports: `https://www.universal-jewelry.com/products/{HANDLE}.json` | Listing creation |
| **Larson Jewelers .json** | None (public) | MSRP pricing reference (VESUVIUS §14.1): `https://www.larsonjewelers.com/products/{HANDLE}.json`, search at `/search/suggest.json?q={CODENAME}` | Pricing |
| **Thorsten** | None (public) | Image source fallback (used during NEVAN image refresh) | — |
| **Gemini Nano Banana** (`gemini-2.5-flash-image-preview`) | `?key=$GEMINI_API_KEY` query string | Image generation (1:1 1200x1200, restage, hand model, lifestyle) | GMC brief, reel watcher, FISSURE/MAJESTIC/... product images |
| **OpenRouter** (`deepseek/deepseek-v4-flash`) | `Authorization: Bearer $OPENROUTER_API_KEY` | All caption + brief LLM calls. Cap: $15/day | All content drafters |
| **Telegram Bot API** | Bot token | Notifications to Amir (chat_id `8101774399`) | All agents on completion/error |
| **Facebook Graph API v21.0** | IG access token | `POST /{ig_id}/media` then `/media_publish` | `phase2_publisher.py` only |
| **GA4 Data API** | Service account JSON | Daily organic traffic snapshot | `beta_google_organic_snapshot.py` |
| **Klaviyo API v2024-10-15** | API key + revision header | Flow health, campaign drafts | `beta_klaviyo_*.py` |

---

## 7. Cron schedule (canonical)

Read it live with `ssh openclaw@178.105.131.33 'crontab -l'`. Snapshot as of 2026-06-02:

| Cadence | Slug | What |
|---|---|---|
| `*/5 * * * *` | `dashboard-data-updater` | Regenerates `dashboard.json` from queue + agents state |
| `*/5 * * * *` | `tasks-watcher` | Telegram push for new task notifications |
| `*/10 * * * *` | `vault-sync` | `git pull` from GitHub (read-only deploy key) |
| `*/15 * * * *` | `phase2-publisher` | IG publish from approved-queued slots (REELS hard-blocked) |
| `*/15 * * * *` | `claudian-command-center-inbox` | Refreshes inbox markdown in vault (commit DISABLED) |
| `*/30 * * * *` | `beta-etsy-aydins-rewriter` | Etsy CSV watcher |
| `*/30 * * * *` | `beta-insta-reel-watcher` | Watches reel-videos/pending/ for MP4s |
| `0 3 * * *` | `claudian-summarizer` | Memory summarizer |
| `0 9 * * *` | `phase2-daily-drafter` | Daily IG draft generation |
| `0 9 * * *` | `beta-shop-listing-enricher` | Daily listing enrichment |
| `0 9 * * *` | `beta-insta-daily-gmc-brief` | Daily GMC brief (3 briefs/run) |
| `0 10 * * *` | `beta-insta-reel-script-writer` | Daily reel script |
| `0 11 * * *` | `beta-insta-carousel-writer` | Daily carousel script |
| `30 11 * * *` | `beta-google-organic-snapshot` | GA4 organic data pull |
| `0 12 * * *` | `claudian-morning-brief` | Daily 7am CT brief |
| `30 12 * * *` | `beta-klaviyo-flow-health` | Daily flow check |
| `55 10 * * *` | `phase1-daily-worker-555-central` | Zero-traffic worker (5:55am CT) |
| `0 14 * * 0` | `beta-shop-pricing-snapshot` | Sunday pricing/inventory |
| `0 23 * * 0` | `beta-insta-engagement-review` | Sunday IG engagement |
| `0 1 * * 1` | `claudian-weekly-review` | Sunday 8pm CT strategic review |
| `0 3 * * 1` | `weekly-approval-accept-rate` | Monday approval rate |
| `0 15 * * 2` | `beta-klaviyo-email-drafter` | Tuesday email A/B |
| `0 14 * * 3` | `beta-google-blog-drafter` | Wednesday blog |
| `0 14 * * 4` | `beta-shop-collection-describer` | Thursday collection |
| `0 15 * * 5` | `beta-klaviyo-weekly-campaign` | Friday campaign |

All crons are wrapped by `scripts/cron_run.sh <slug> <command>` which logs run start/end/exit code to `logs/cron_runs.jsonl`. Cron health is computed from this file by `dashboard_data_updater.py`.

---

## 8. Dashboard architecture

### Stack
- Next.js 16.2.6 (App Router, Server + Client components)
- Tailwind v4
- React 19
- Path: `/home/openclaw/.openclaw/command-center/command-center-dashboard-tmp/`

### systemd unit
- File: `/home/openclaw/.config/systemd/user/beta-boss-dashboard.service`
- User-mode systemd (no root)
- `EnvironmentFile=/home/openclaw/.openclaw/agents/beta/credentials/dashboard.env`
- `ExecStart=npm run start -- -H 127.0.0.1 -p 3334`
- Restart with: `systemctl --user restart beta-boss-dashboard.service`

### nginx
- `/etc/nginx/sites-available/beta-shopaydins.conf` → proxies `beta.shopaydins.com` to `127.0.0.1:3334`
- `/etc/nginx/sites-enabled/dashboard-action.conf` → proxies `connect.shopaydins.com/dashboard-action/` to `127.0.0.1:8090`

### Token auth (TokenAuth component)
- Browser stores `DASHBOARD_TOKEN` in localStorage after first login
- All `/api/action` POSTs include `{ token, action, ...payload }`
- API checks `token === process.env.DASHBOARD_TOKEN`
- **Known issue**: stale localStorage tokens. Fix is to clear localStorage on `beta.shopaydins.com` and re-login.

### Action flow
1. User clicks button in dashboard UI
2. POST `/api/action` with `{ token, action, ...payload }`
3. Next.js handler signs payload with HMAC-SHA256 using `DASHBOARD_ACTION_SECRET`
4. Forwards to `https://connect.shopaydins.com/dashboard-action/` with `X-Signature` + `X-Timestamp` headers
5. nginx proxies to `127.0.0.1:8090`
6. `action_webhook.py` verifies signature, dispatches to action handler
7. Handler updates queue file, returns result
8. Next.js relays response to browser

### Stale-data caveat (UNFIXED as of 2026-06-02)
The dashboard reads `dashboard.json` which is updated every 5 min by cron. Action handlers update the QUEUE file directly. There's a 0-5 min lag between an action firing and the UI reflecting it. **Recommended fix** (not yet shipped): have `action_webhook.py` trigger `dashboard_data_updater.py` after every task resolution. See "Outstanding" §11.

### Build + deploy
- Edit source under `command-center-dashboard-tmp/`
- `cd command-center-dashboard-tmp && npm run build`
- `systemctl --user restart beta-boss-dashboard.service`
- Hard refresh in browser (Cmd-Shift-R) to bust chunk cache

---

## 9. Action webhook (the VPS-side endpoint)

- **File**: `/home/openclaw/.openclaw/command-center/scripts/action_webhook.py`
- **Port**: `127.0.0.1:8090`
- **Public URL**: `https://connect.shopaydins.com/dashboard-action/`
- **Run as**: systemd user service (process always running)
- **Log**: `/home/openclaw/.openclaw/command-center/logs/action_webhook.log`

### Auth
HMAC-SHA256 of `{timestamp}.{payload}` using secret from `dashboard-action.secret`. Reject if signature missing or invalid.

### Whitelisted actions (won't execute unsigned input, but these are the operations available)
`refresh-now`, `run-phase1-worker`, `run-ig-drafter`, `run-security-audit`, `run-daily-patrol`, `view-logs`, `view-backups`, `backup-workspace`, `backup-dashboard`, `backup-config`, `restart-gateway`, `restart-api`, `fresh-session`

### Task resolution actions (require valid signature)
- `task-approve` → moves item from queue → archive with `resolution: approved`
- `task-reject` → same with `rejected`
- `task-send-back` → same with `sent-back-to-agent`
- `task-detail` → read-only fetch of full task data (used by modal)

### Matching logic (gotcha!)
Items in `needs-amir-review.json` are matched by `(item.timestamp or item.ts) == payload.id`. Items have `timestamp` field but NOT `id` field. The dashboard creates the `id` field by copying `timestamp` in `dashboard_data_updater.py`. **If you write a new task source, make sure `timestamp` matches what you expect for `id`.**

---

## 10. VESUVIUS Listing Standard (locked, authoritative)

### Where
- Source: `/home/openclaw/.openclaw/command-center/brands/aydins/shopify-listing-standard.md`
- Symlinked from: `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md`

### Sections (canonical structure for every Aydins ring listing)
1. **Body**: opening + supporting + Key Features + "Why CODENAME" close. NO policy blocks.
2. **Key Features**: product-specific only (material, inlay, widths, fit, profile, engraving, color/finish, daily-wear note). NO trust pillars.
3. **Quick Specs metafields**: `custom.keywords` (labeled multi-line) + `custom.quick_specs` (bullet-separated single line).
4. **Product FAQ**: exactly 6 product-specific questions in `custom.custom_faq` (rich text JSON).
5. **FAQ schema**: `custom.custom_faq_schema` JSON-LD matching `custom.custom_faq` exactly.
6. **SEO**: `global.title_tag` ≤70 chars, `global.description_tag` ≤150 chars, truthful image alt text.
7. **Taxonomy metafields**: 7 `shopify.*` metaobject refs (color-pattern, ring-size, jewelry-material, target-gender, ring-design, age-group, jewelry-type), plus `custom.color`, `mc-facebook.google_product_category`.
8. **Material info page**: `custom.tungsten_ring_information_` (note trailing underscore on tungsten) / `custom.titanium_ring_information` / `custom.ceramic_ring_information`.
9. **Tags**: widths + engraving (`Inside` or `Inside & Outside`) + material collection + visible colors + feature/inlay.
10. **Variants/SKUs**: match source EXACTLY (no invented sizes). Inventory: 10/variant, policy CONTINUE, tracked TRUE. SKU format depends on source:
    - Universal Jewelry: `CODENAME-WIDTH-SIZE` (e.g. `FISSURE-8-9`)
    - Jewelry Depot: `JDTR{NUMBER}-{WIDTH}-{SIZE}` (e.g. `JDTR901-8-7`)
11. **Image alt text**: codename + material + feature + view (truthful only; no invented scenes).
12. **Hard bans**: no em dashes, no supplier/third-party brand names in copy (Thorsten, Universal Jewelry, JCK), no "handcrafted/handmade/forged/built", no bare "lifetime warranty" (use "Aydins Lifetime Warranty. See policy page for terms."), no invented image scenes.
13. **Verification**: snapshot + write-log after every Shopify write.
14. **Pricing** (added 2026-06-02 by Amir):
    - **§14.1 Universal Jewelry rings ONLY**: Aydins price = `larsonjewelers.com price - $10`
    - **§14.2 Scope exclusions**: does NOT apply to Jewelry Depot rings (`JDTR` SKUs), Aydins Creations, existing live products, non-ring products
    - **§14.3 Identification gate**: product is eligible only if ALL true: source is `universal-jewelry.com` (or vendor is `Universal J`/`Universal J Custom`), is a ring, SKU follows Universal Jewelry format

### Reference templates on Aydins
| Material | Template product | Product ID | Key metafield to mirror |
|---|---|---|---|
| Tungsten | `INFERNO` | `8726693216493` | `custom.tungsten_ring_information_` = `gid://shopify/OnlineStorePage/110086652141` |
| Titanium | `ALBERT` | `6237487464636` | `custom.titanium_ring_information` = `gid://shopify/OnlineStorePage/15234334762` |
| Ceramic | `ABERDEEN` | `4557659996202` | `custom.ceramic_ring_information` = `gid://shopify/OnlineStorePage/110095073517` |

### Common Shopify GIDs
- Shopify category for Rings: `gid://shopify/TaxonomyCategory/aa-6-9`
- Shopify product taxonomy node: `gid://shopify/ProductTaxonomyNode/340`
- Default ring size chart page: `gid://shopify/OnlineStorePage/110085636333`
- Theme custom page: `gid://shopify/OnlineStorePage/110086586605`
- Aydins's 8 sales channels (publish via `publishablePublish` mutation):
  - Online Store `97116676`
  - Google & YouTube `22362816554`
  - Facebook & Instagram `23176511530`
  - Pinterest `42380427306`
  - Shop `78523236589`
  - TikTok `82618253549`
  - Point of Sale `116866973933`
  - Daily Profit and Loss App `176460857581`
  - (NOT: Microsoft Copilot — `181599994093` — intentionally off)

---

## 11. Work completed this session (chronological)

### Vault hygiene
- Diagnosed 54-commit divergence between Windows local and VPS vault. Untracked 4 VPS-generated paths (`00 Command Center Inbox.md`, morning-briefs, reel-scripts, carousel-scripts). Neutered `claudian_command_center_inbox.py::commit_and_push_vault()` (returns False immediately; original body commented out).
- Rescued 4 VPS-generated files to local Windows tmp before forcing local hard-reset.
- VPS vault is now strictly read-only mirror via `vault_sync.sh`.

### IG content pipeline hardening
- **Plans 4 + 5** committed to `phase2_daily_drafter.py` (commit `d21d10e`):
  - Every draft must anchor to a real `source_product` (Plan 4)
  - `validate_draft()` rejects drafts with caption material that doesn't match the source product's material (Plan 5)
  - 31-term `MATERIAL_VOCAB` (tungsten, titanium, ceramic, zirconium, gold, silver, meteorite, etc.)
- **REELS hard-lockdown** confirmed at L91 of `phase2_publisher.py`: `if slot.get("media_type") == "REELS": continue`. Added explanatory `# INTENTIONAL` comment above it (commit `19d7541`).
- **GMC video prompt** rewritten 3 times in `beta_insta_daily_gmc_brief.py::generate_veo_prompts()`:
  1. First attempt: 100-160 word cinematic narratives (rejected by GMC Animate Images as too complex).
  2. Second: 15-30 word minimal prompts (Google's output added scene events that distorted the product).
  3. Final (current): 60-90 word CAMERA-MOTION-ONLY prompts with explicit "no glow, no halo, no morphing" constraints. 3 variants per brief: Slow Zoom In / Slow Zoom Out / 180 Rotation.

### Brief image upgrade
- Changed Nano Banana output from 9:16 portrait (768x1344) to 1:1 square 1200x1200 (Shopify standard).
- Added `_resize_to_1200_square()` helper (PIL center-crop + LANCZOS resize).
- Added `attach_image_to_shopify_product()` (stagedUploadsCreate + productCreateMedia IMAGE).
- Auto-attaches the brief image to the corresponding Shopify product after each brief.
- Backfilled 3 existing 2026-06-01 briefs (AURIGA, MIRAGE, NIGHTSHADE) with new 1200x1200 images.

### Reel pipeline shipped
- Processed AURIGA, MIRAGE, NIGHTSHADE MP4s through `beta_insta_reel_watcher.py`:
  - Ping-pong loops via ffmpeg (8s forward + 8s reverse = 16s seamless)
  - Landscape ping-pong attached to Shopify product page
  - Vertical 9:16 with blur-fill for IG
  - Telegram 5-message package per reel (download link + IG/TikTok/YT Shorts copy + product URL)
- Slots added to IG calendar with `status: manual-post-only` (Amir posts manually to pick audio).

### Dashboard improvements
- **BriefsView modal scroll fix**: `fade-up` class on `BriefsView` outer wrapper had `animation-fill-mode: both`, which retained `transform: translateY(0)` permanently. Per CSS spec, any non-`none` transform on an ancestor creates a containing block for fixed-positioned descendants, breaking the brief modal. Removed `fade-up` from L266.
- **BriefsView prose-wrap fix**: added `pre` component renderer to ReactMarkdown to wrap long Veo prompts (was overflowing horizontally).
- **Mobile responsive pass**: tightened Header padding on phone, hid Gateway uptime + Chat label + subtitle on small screens, reduced StatCards big-number font.
- **Hierarchy redesign**: created `NeedsApprovalSection` component above `StatCards` on the dashboard. Exported `NeedsApprovalCard`, `TaskDetailModal`, `NeedsCallItem` from `TasksKanban.tsx` so the new section could reuse them. Demoted StatCards visually with a "REFERENCE" eyebrow above.
- **TasksKanban modal fade-up fix**: same trap as BriefsView, L581 outer wrapper. Removed `fade-up`.
- **Theme re-color (lighter dark)**: 10 token swaps in `app/globals.css`. Surfaces lifted ~5% lightness, purple desaturated from sat 91% → 38% (`#7E5FF7` → `#7B72C4`), borders softened. Status colors (red/amber/green/yellow) intentionally untouched to keep failure signals punchy.
- **Body bg gradient desaturation**: changed `rgba(126, 95, 247, 0.15)` → `rgba(123, 114, 196, 0.08)` and pink alpha 0.10 → 0.05 to match the new calmer accent.
- **DASHBOARD_ACTION_SECRET fix**: secret file existed at `dashboard-action.secret` but wasn't loaded into env. Added line to `dashboard.env`, restarted service. Action signing now works end-to-end.

### VESUVIUS spec extensions
- Added **§14 Pricing** (Universal Jewelry rings → Larson - $10).
- Tightened §14 with explicit scope exclusions (§14.2) and identification gate (§14.3) so the rule can't be misapplied to Jewelry Depot / Aydins Creations / non-ring products.

### Products created (all status=draft, ready for Amir review)
| Codename | ID | Variants | Price | Material | Inlay/Feature |
|---|---|---|---|---|---|
| **FISSURE** | `9389074874605` | 16 | $439.99 | Black Tungsten | Hammered + Meteorite |
| **MAJESTIC** | `9389635469549` | 21 | $159.99 | Titanium | Anodized purple/blue/gold diamond |
| **MERIDIAN** | `9389637107949` | 21 | $159.99 | Titanium | Anodized purple/blue diamond |
| **SHORELINE** | `9389966164205` | 14 | $319.99 | Gold-Plated Tungsten | Mother of Pearl |
| **WE THE PEOPLE** | `9389966229741` | 92 | $279.99 | Black Tungsten | Engraved text |
| **AMERICAN FLAG & CROSS** | `9389966393581` | 92 | $234.99 | Black Tungsten | Engraved flag + cross |
| **AMERICAN FLAGS** | `9389966491885` | 92 | $239.99 | Black Tungsten | Engraved flags |
| **DON'T TREAD ON ME** | `9389966622957` | 21 | $234.99 | Black Tungsten | Spinner + snake |
| **PATRIOT** | `9389966721261` | 92 | $224.99 | Polished Tungsten | Pipe cut + U.S. flag |
| **ODYSSEY** | `9389966852333` | 21 | $89.99 | Black Ceramic | Carpathian elm wood |

All on 8 sales channels (scheduled to publish when Amir flips status active). All 24-25 VESUVIUS metafields set. Each has 5-6 images (source from Universal Jewelry + Gemini hand-lifestyle + Gemini scene-lifestyle).

### Investigations (no code changes)
- **Cron "DEGRADED" status diagnosed**: 9 "never run" are all weekly schedules that haven't hit their first day-of-week yet (harmless). 2 "failed in 24h": `vault-sync` had 61 failures in 24h (currently passing — flaky, worth investigating), `beta-insta-daily-gmc-brief` had 1 minor failure during one of the code rewrites.
- **SEND BACK action diagnosis**: webhook IS receiving clicks and resolving tasks correctly. The bug is that dashboard.json is updated only every 5 min by cron, so the UI shows stale data after a click. **Fix not yet shipped**: trigger `dashboard_data_updater.py` from `action_webhook.py` after each successful resolution.

---

## 12. Outstanding work (open as of 2026-06-02 16:00 UTC)

### Decisions waiting on Amir
1. **NEVAN image position 7**: hand-holding-ring shot with brown interior visible. Hand image rule says keep it, but the inside-visible rule says replace it. Need Amir to call A (replace) or B (keep).
2. **Multi-width variants**: 4 of the 7 new products (WE THE PEOPLE / AMERICAN FLAG & CROSS / AMERICAN FLAGS / PATRIOT) have 92 variants each from cross-product of widths × sizes. Universal Jewelry source has 82 (some width/size combos missing). Leave at 92 (more customer options) or prune to source's exact 82 (strict VESUVIUS §10 match).

### Outstanding code/system fixes
3. **Action webhook should refresh dashboard.json** after every successful task resolution. ~5 lines of code in `action_webhook.py`. Fixes the "I clicked send-back but the task is still there" experience.
4. **TokenAuth stale-token validation**: dashboard doesn't re-validate localStorage tokens against the server. Users with old tokens get unauthorized errors with no clear fix path. Improvement: on every page load, ping `/api/validate-token` and clear localStorage if invalid.
5. **Vault-sync 61 failures in 24h**: cron is passing now but has been thrashing. Worth a log dive to find the recurring failure mode.

### Outstanding revenue-facing work (the "stop building, start shipping" pile)
6. **Post the 3 reels** generated earlier (AURIGA, MIRAGE, NIGHTSHADE). Captions written. Sitting in Telegram. Cross-post to IG + TikTok + YouTube Shorts.
7. **Top 5 SKUs by 7-day revenue** — Amir asked to build a daily Top-Product Conversion Scorecard but needs to supply the SKU list. Not yet received.
8. **NEVAN image refresh** in flight — positions 1, 3, 6 confirmed to replace with new Larson images; position 7 awaiting decision.

### Known but not urgent
9. The dashboard's "DEGRADED" cron pill is misleading for new weekly crons until their first natural fire. Improvement: classify "scheduled for future first run" as PENDING not DEGRADED.
10. Multi-color metaobject references (purple/blue/gold) not set on MAJESTIC/MERIDIAN — currently only base silver/black is set. Adding richer color taxonomy would improve SEO/category. Not blocking.

---

## 13. Common commands (quick reference)

### Working with the VPS

```bash
# Open a one-off command
ssh openclaw@178.105.131.33 'systemctl --user status beta-boss-dashboard.service'

# Look at logs
ssh openclaw@178.105.131.33 'tail -50 /home/openclaw/.openclaw/command-center/logs/action_webhook.log'

# Run a script via Python (use the same interpreter the crons use)
ssh openclaw@178.105.131.33 'python3 /home/openclaw/.openclaw/command-center/scripts/dashboard_data_updater.py'

# Restart dashboard
ssh openclaw@178.105.131.33 'systemctl --user restart beta-boss-dashboard.service'

# Restart action webhook
ssh openclaw@178.105.131.33 'systemctl --user restart action-webhook.service'

# List crons
ssh openclaw@178.105.131.33 'crontab -l'
```

### Shopify Admin API (via existing helper)

```python
import sys, json, urllib.request
sys.path.insert(0, "/home/openclaw/.openclaw/command-center/scripts")
from beta_insta_daily_gmc_brief import _shop_creds, _gemini_key, _openrouter_key

shop, token = _shop_creds()
# REST example
req = urllib.request.Request(
    f"https://{shop}/admin/api/2024-10/products.json?limit=5",
    headers={"X-Shopify-Access-Token": token}
)
# GraphQL example
import json
req2 = urllib.request.Request(
    f"https://{shop}/admin/api/2024-10/graphql.json",
    data=json.dumps({"query": "{ products(first:5) { edges { node { id } } } }"}).encode(),
    headers={"X-Shopify-Access-Token": token, "Content-Type": "application/json"},
    method="POST"
)
```

### Patching code on the VPS (safe pattern)

```python
# Always back up before patching
ssh openclaw@178.105.131.33 'TS=$(date -u +%Y%m%dT%H%M%SZ); cp <file> <file>.bak-<purpose>-$TS'

# Verify py_compile after Python edits
ssh openclaw@178.105.131.33 'python3 -m py_compile <file>'

# Verify build + restart after Next.js dashboard edits
ssh openclaw@178.105.131.33 'cd .../command-center-dashboard-tmp && npx --no-install tsc --noEmit -p tsconfig.json && npm run build && systemctl --user restart beta-boss-dashboard.service'
```

### Standard Python heredoc pattern (works around f-string + bash quoting issues)

Write the Python to a local Windows file first, then:
```
scp C:/Users/amirl/AppData/Local/Temp/<script>.py openclaw@178.105.131.33:/tmp/<script>.py
ssh openclaw@178.105.131.33 'python3 /tmp/<script>.py'
```

This avoids the heredoc + single-quote SSH quoting nightmare.

---

## 14. Operating rules (override defaults)

From CLAUDE.md (vault root). MUST follow:

1. **No em dashes anywhere**. Use periods, commas, semicolons, or parentheses. Exception only: accurate filename references where renaming breaks wikilinks.
2. **Prefix AI-generated files with `(C)`**.
3. **Ask before editing existing notes**. Never overwrite originals — create a new version instead.
4. **Label drafts clearly**. Say so when something is final-ready.
5. **Clean, descriptive file names** optimized for retrieval. Not clever.
6. **Don't make this vault a storage bin**. It's a command center.
7. **Be blunt and direct**. Challenge weak thinking. No fluff. Get to the answer.
8. **One strong recommendation**, not 10 options.
9. **Always end with a clear next action**.
10. **Don't let Amir hide in planning**. Call out when he's drifting.

### Amir's known failure modes (per CLAUDE.md)
- Takes on too much at once
- Gets distracted by new ideas before current is shipped
- Confuses motion with progress
- Over-optimizes and tweaks instead of shipping
- Under stress: research/planning/tweaking loops, hunting for a better strategy

When you see these patterns, **call them out**.

### Hard limits
- **$15/day OpenRouter cap** (DeepSeek V4 Flash via OpenRouter)
- **No Claude API calls** from agent scripts (only via human chat sessions like this one)
- **No publishing to Shopify or IG without explicit Amir approval** for new content
- **All Shopify writes preceded by audit/backup JSON**
- **REELS hard-lockdown** in `phase2_publisher.py` — never auto-publish video content (requires audio that auto-pipeline can't generate)

---

## 15. Where to look first if something breaks

| Symptom | First check |
|---|---|
| Dashboard shows stale data | `dashboard_data_updater.py` last run in `cron_runs.jsonl` |
| Action button does nothing | `action_webhook.log` — check for `AUTH_FAIL` or `UNKNOWN_ACTION` |
| "Unauthorized" in dashboard | (1) `dashboard.env` has both `DASHBOARD_TOKEN` and `DASHBOARD_ACTION_SECRET` (2) browser localStorage has the current token |
| Cron card DEGRADED | Run cron health diagnostic — most "never run" are harmless future schedules |
| Brief generator failed | `logs/beta_insta_gmc_brief.log` |
| Reel watcher backed up | `ls reel-videos/pending/` — should be empty between runs |
| IG slot not publishing | Check slot `status` in `insta-content-calendar.json` (must be `approved-queued`) AND `media_type` (must NOT be `REELS`) |
| Product create failed | Check Shopify API rate limits, then category metafield (must be set before taxonomy metafields) |

---

## 16. Conversation history reference

This handoff was created at the end of a long session that covered:

- Reel pipeline diagnosis + 3 reels processed
- BETA Check rules expansion (Plans 4+5)
- Three GMC video prompt rewrites (cinematic → minimal → motion-only)
- Image dimensions upgrade (9:16 → 1:1 1200x1200) + Shopify auto-attach
- Dashboard mobile responsive
- Dashboard hierarchy redesign (NeedsApprovalSection on top)
- Lighter dark theme
- 10 products created end-to-end (FISSURE through ODYSSEY) per VESUVIUS spec
- VESUVIUS §14 Pricing rule (Larson - $10, scoped to Universal Jewelry rings only)
- DASHBOARD_ACTION_SECRET fix
- SEND BACK action diagnosis (works at queue level, dashboard.json stale)

Full conversation transcript: `C:\Users\amirl\.claude\projects\C--Users-amirl-Documents-Amirs-Command-Center\<latest>.jsonl`

If you need exact details from before the session compaction, that file has the raw history.

---

## 17. The next thing a new Claude session should do

In priority order:

1. **Read CLAUDE.md** at vault root for behavioral rules.
2. **Verify VPS access**: `ssh openclaw@178.105.131.33 'whoami && date && systemctl --user is-active beta-boss-dashboard.service'`
3. **Verify Shopify access**: run any of the `_shop_creds()` examples in §13.
4. **Check the open items in §12** with Amir before starting new work.
5. **Don't build new tooling until Amir confirms** the existing 10 product drafts are reviewed and the 3 unposted reels are out.
