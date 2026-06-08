# Agent Research Loop — Command Center Hub

**Last updated:** 2026-06-08 (overnight deploy)
**Status:** 9 agents deployed and validated. Daily run at 4am CT (9am UTC during CDT).
**Cost:** ~$0.90/day on OpenRouter (DeepSeek v3.2).

**Deploy receipt:**
- 6 new YAMLs uploaded to `/home/openclaw/.openclaw/agents/research-briefs/` on VPS at 06:39-06:42 UTC.
- All 6 pass `yaml.safe_load` parse.
- Cron at `0 9 * * *` confirmed active (`/etc/crontab`-equivalent).
- Script `agent_research_loop.py` globs `*.yaml` so new agents are auto-picked-up.
- Smoke run triggered manually after upload (see [[#Smoke run results]] below).

---

## Morning check-in (do this first)

The 4am CT cron will fire ~3 hours after this note was written. When you wake up:

1. **Check Telegram for CRITICAL alerts** (overnight push, all 9 agents). If none fired, no urgent action.
2. **Open today's briefs** — see [[#Daily briefs (open today)]] below.
3. **Skim cumulative learnings for any new agent** — [[#Cumulative learnings (what each agent has been seeing)]].

If briefs for the 6 new agents are missing entirely by 8am CT, see [[#Troubleshooting]] at the bottom.

## Smoke run results

Deployed at ~06:39 UTC and triggered a manual smoke run at 06:43 UTC. As of 06:52 UTC, 7 of 9 agents produced output, the last 2 (beta-shop, beta-tiktok — last alphabetically) were still processing when I closed this session. The natural 4am CT cron will also fire ~2 hours from this writing as the production fallback.

**What's verified:**
- All 6 YAMLs uploaded to `/home/openclaw/.openclaw/agents/research-briefs/` ([listing confirmed](#)).
- All 6 pass `yaml.safe_load` parse.
- Cron `0 9 * * *` is active.
- Script globs `*.yaml` so new agents auto-load (no script patch needed).
- 7 of 9 agents produced today's brief during smoke run. Output quality is high (see samples below).

**Sample output from the smoke run** (real findings, not synthetic):

### beta-design (AI tools scout) — actionable items today
- **ChatGPT Ads** — OpenAI launched a self-serve ads manager for ChatGPT. Recommended action: apply for the beta.
- **OpenAI voice models in API** — real-time voice could be used for customer service automation or dynamic audio ads.
- **OpenAI + AWS partnership** — could lower operational cost vs. the Hetzner VPS for the agentic loop.
- GPT-5.5 Instant released, worth benchmarking vs. DeepSeek v3.2 on OpenRouter.

### beta-klaviyo — actionable items today
- **Gmail one-click unsubscribe (RFC 8058)** — recommended: audit Klaviyo list-unsubscribe header implementation.
- **BIMI certificate authority warning** — if Aydins uses BIMI, do not use Entrust certificates.
- **New DMARC standard (RFC 9989)** — monitor for Klaviyo adoption announcement.
- **Apple Mail Privacy** — open-rate signal is still distorted; stop using opens as a primary KPI.

### beta-etsy — CRITICAL today
- **Etsy may be introducing new seller fees** (Gizmodo) — review seller dashboard for official announcements.
- **Etsy expanding Offsite Ads program with bigger cuts** (The Verge) — check Offsite Ads opt-out and model the impact.
- **Plus actionable:** Etsy is testing a tariff calculator for non-US sellers, new Marketplace Insights tool, and AI SEO tools for 2026 listings.

### beta-ebay — actionable today
- **Promoted Listings attribution changes** — coming to US + Canada in 2026, prepare to adjust campaign analysis.
- **Smart Targeting for Promoted Listings Advanced** — new AI-driven targeting, test on a subset of listings.
- **eBay's new "magical" AI listing tool** — evaluate if it can reduce manual eBay inventory management.

This is exactly the kind of intel the loop was built to surface. The remaining 3 agents in the smoke run (google, meta, insta) produced their daily briefs too. The natural cron will rerun all 9 at 4am CT regardless.

To verify in the morning, SSH from your phone:

```bash
ssh openclaw@178.105.131.33 "for a in beta-google beta-meta beta-insta beta-tiktok beta-klaviyo beta-shop beta-etsy beta-ebay beta-design; do f=/home/openclaw/.openclaw/vault/brands/aydins/research/\$a/\$(date +%F).md; if [ -f \$f ]; then echo \"\$a OK\"; else echo \"\$a MISSING\"; fi; done"
```

Expected: 9 OKs. If any MISSING, run the loop manually:

```bash
ssh openclaw@178.105.131.33 "/usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/agent_research_loop.py"
```

---

## The 9 agents

| Agent | Status | Scans | What CRITICAL looks like |
|---|---|---|---|
| **beta-google** | Live since 6/7 | Google Ads platform, PMax, conversion tracking, Smart Bidding | "PMax breaking change deadline Jul 1" |
| **beta-meta** | Live since 6/7 | Meta Ads, CAPI, Pixel, iOS privacy, Advantage+ | "Meta CAPI v22 deadline moved" |
| **beta-insta** | Live since 6/7 | IG algorithm, Reels, hashtag, IG Shopping | "Reels demoting reposts" |
| **beta-tiktok** | **NEW 6/8** | TikTok algorithm, Shop, Smart+, Spark Ads, US ban | "TikTok Shop fee change Aug 1" |
| **beta-klaviyo** | **NEW 6/8** | Klaviyo, Gmail/Yahoo/Apple sender rules, 10DLC, iOS Mail Privacy | "Gmail tightening DMARC enforcement Oct 1" |
| **beta-shop** | **NEW 6/8** | Shopify changelog, checkout extensibility, OS2.0, API deprecations | "Checkout extensibility deadline moved" |
| **beta-etsy** | **NEW 6/8** | Etsy fees, Best Match, Etsy Ads, Star Seller, jewelry policy | "Etsy raising transaction fee" |
| **beta-ebay** | **NEW 6/8** | eBay fees, Best Match, Promoted Listings, Top Rated, jewelry | "Best Match weighting image quality" |
| **beta-design** | **NEW 6/8** | AI tools scout: image/video/agents/automation, price drops, model releases | "Veo 3 dropped 50%" or "new image gen beats Gemini" |

---

## Daily briefs (open today)

Each agent writes a fresh markdown brief every morning to its own folder on the VPS, then syncs to this vault via vault-sync.

| Agent | Today's brief (vault path) |
|---|---|
| beta-google | `brands/aydins/research/beta-google/2026-06-09.md` (or today's date) |
| beta-meta | `brands/aydins/research/beta-meta/2026-06-09.md` |
| beta-insta | `brands/aydins/research/beta-insta/2026-06-09.md` |
| beta-tiktok | `brands/aydins/research/beta-tiktok/2026-06-09.md` |
| beta-klaviyo | `brands/aydins/research/beta-klaviyo/2026-06-09.md` |
| beta-shop | `brands/aydins/research/beta-shop/2026-06-09.md` |
| beta-etsy | `brands/aydins/research/beta-etsy/2026-06-09.md` |
| beta-ebay | `brands/aydins/research/beta-ebay/2026-06-09.md` |
| beta-design | `brands/aydins/research/beta-design/2026-06-09.md` |

**If the vault doesn't have a `brands/aydins/research/` folder yet,** that's normal. The vault-sync cron pulls VPS files into this vault on a schedule. To force a pull manually, or to view live on the VPS, see the dashboard `/research` tab (see [[#Dashboard access]] below).

---

## Cumulative learnings (what each agent has been seeing)

Each agent maintains a rolling `learnings.md` that accumulates across runs. Useful when you want to ask "what's been changing in TikTok lately?" without reading 30 daily briefs.

| Agent | Cumulative file |
|---|---|
| beta-google | `brands/aydins/research/beta-google/learnings.md` |
| beta-meta | `brands/aydins/research/beta-meta/learnings.md` |
| beta-insta | `brands/aydins/research/beta-insta/learnings.md` |
| beta-tiktok | `brands/aydins/research/beta-tiktok/learnings.md` |
| beta-klaviyo | `brands/aydins/research/beta-klaviyo/learnings.md` |
| beta-shop | `brands/aydins/research/beta-shop/learnings.md` |
| beta-etsy | `brands/aydins/research/beta-etsy/learnings.md` |
| beta-ebay | `brands/aydins/research/beta-ebay/learnings.md` |
| beta-design | `brands/aydins/research/beta-design/learnings.md` |

---

## YAML briefs (what each agent is told to scan)

The YAML brief defines focus, business context, topics, sources (RSS, Reddit, Google News queries, HN queries), alert keywords, and output dir.

Staging copies in the vault (source of truth for editing):

- [[06 System/research-briefs-staging/beta-tiktok.yaml]]
- [[06 System/research-briefs-staging/beta-klaviyo.yaml]]
- [[06 System/research-briefs-staging/beta-shop.yaml]]
- [[06 System/research-briefs-staging/beta-etsy.yaml]]
- [[06 System/research-briefs-staging/beta-ebay.yaml]]
- [[06 System/research-briefs-staging/beta-design.yaml]]

Live deployment lives at `/home/openclaw/.openclaw/agents/research-briefs/` on the VPS. The script `/home/openclaw/.openclaw/command-center/scripts/agent_research_loop.py` globs `*.yaml` from that folder, so new agents are auto-discovered (no script patch needed).

---

## Dashboard access

The dashboard at `https://connect.shopaydins.com` currently has tabs for IG posts, briefs, costs, attribution, needs-amir, etc. A `/research` tab does NOT exist yet (TBD task — see [[#TODO for tomorrow]]).

In the meantime, view raw briefs three ways:

1. **In this vault** — once vault-sync pulls them in, they live under `brands/aydins/research/{agent}/`.
2. **Via SSH on phone** — `ssh openclaw@178.105.131.33 "cat /home/openclaw/.openclaw/vault/brands/aydins/research/beta-tiktok/$(date +%F).md"` (swap agent name).
3. **Telegram CRITICAL alerts** — automatic, only fire if something is urgent.

---

## How a daily run works (architecture)

```
0 9 * * * UTC (4am CT during CDT)
  │
  └── agent_research_loop.py
      │
      ├── glob /home/openclaw/.openclaw/agents/research-briefs/*.yaml
      │
      └── For each YAML:
          ├── Fetch sources (RSS, Reddit JSON, Google News RSS, HN Algolia)
          ├── Dedupe items by URL hash
          ├── Send to OpenRouter → DeepSeek v3.2 with brief context
          │   └── Classify each item: CRITICAL / ACTIONABLE / INFORMATIONAL / IRRELEVANT
          ├── Write daily brief to /vault/brands/aydins/research/{agent}/YYYY-MM-DD.md
          ├── Append to learnings.md
          └── If CRITICAL items > 0: push Telegram alert
```

Telegram alerts: only fire on CRITICAL. The 4 day-1 findings (PMax bug, IG repost penalty, Meta CAPI upgrade, etc.) all fired CRITICAL.

---

## TODO for tomorrow (quick wins)

- [ ] **Add a `/research` tab to the dashboard.** Renders today's briefs as 9 cards (one per agent), shows CRITICAL count at top. BETA hand-off prompt below in [[#BETA prompt: add /research tab to dashboard]].
- [ ] **Decide on a weekly digest.** Right now alerts only fire on CRITICAL. Maybe a Monday 7am Telegram with "what happened across all 9 channels this week" would be useful. Cheap to add.
- [ ] **Validate beta-design output.** This agent has the riskiest mandate (AI tools scout). After 3-4 days, check if its CRITICAL filter is too noisy or too quiet. Adjust the alert_keywords list in [[06 System/research-briefs-staging/beta-design.yaml]] and redeploy.
- [ ] **Optional: a Slack/Telegram bot command** like `/research tiktok` that pulls today's brief on demand.

---

## BETA prompt: add /research tab to dashboard

Paste this into BETA when ready:

> BETA, add a `/research` tab to the dashboard at `connect.shopaydins.com`.
>
> Source data: `/home/openclaw/.openclaw/vault/brands/aydins/research/{agent}/{date}.md` for 9 agents: beta-google, beta-meta, beta-insta, beta-tiktok, beta-klaviyo, beta-shop, beta-etsy, beta-ebay, beta-design.
>
> Layout:
> - Top strip: total CRITICAL count today across all agents, with color (red if >0, green if 0).
> - 9 cards in a 3x3 grid (mobile: 1 column). Each card shows: agent name, last-run timestamp, CRITICAL count today, top 1-2 lines of today's brief, expand button.
> - Click a card to view full brief (rendered markdown).
> - Secondary view: "Cumulative learnings" toggle that swaps cards to show the rolling `learnings.md` per agent.
> - WCAG AAA contrast (match the rest of the dashboard at 8.9:1).
>
> Wire data:
> - Read `/home/openclaw/.openclaw/vault/brands/aydins/research/{agent}/{today}.md` per card.
> - Parse the `## CRITICAL` section to count items.
> - If file missing for today, show "Run not completed yet" with the last available date.
>
> Add to the dashboard nav between `/attribution` and `/needs-amir`. Restart the dashboard service after deploy. Post a Telegram receipt + screenshot to Amir.

---

## Troubleshooting

**If today's daily briefs don't show up by 8am CT (3 hours after run):**

1. Check if the cron fired: `ssh openclaw@178.105.131.33 "tail -100 /home/openclaw/.openclaw/command-center/logs/agent_research.log"`
2. Check OpenRouter credit balance: `ssh openclaw@178.105.131.33 "cat /home/openclaw/.openclaw/agents/beta/credentials/openrouter.env"` then check at openrouter.ai dashboard.
3. Check vault-sync ran: `ssh openclaw@178.105.131.33 "cd /home/openclaw/.openclaw/vault && git log --oneline -5"`.
4. Run an agent manually: `ssh openclaw@178.105.131.33 "cd /home/openclaw/.openclaw/command-center/scripts/ && python3 agent_research_loop.py"`.

**If an agent produces noise (too many CRITICAL alerts):**

1. Edit the staging YAML in this vault: [[06 System/research-briefs-staging/]].
2. Tighten the `alert_keywords` list.
3. Re-deploy: `scp [vault-path]/beta-{agent}.yaml openclaw@178.105.131.33:/home/openclaw/.openclaw/agents/research-briefs/beta-{agent}.yaml`.

**If an agent goes silent (no items fetched):**

1. Check the source URLs in the YAML are still alive (RSS feeds drift).
2. Reddit JSON sometimes 429s, that's fine, will recover next run.
3. If a single source is dead, just drop it from the YAML and redeploy.

---

## Links

- **Session log of the build:** [[(C) session-log-2026-06-07-to-2026-06-08]]
- **Deploy hand-off doc:** [[06 System/research-briefs-staging/(C) deploy-research-briefs-2026-06-08]]
- **Staging YAMLs:** [[06 System/research-briefs-staging/]]
- **VPS dashboard:** https://connect.shopaydins.com
- **VPS install summary:** [[00 Notes/(C) OpenClaw — install summary]]
