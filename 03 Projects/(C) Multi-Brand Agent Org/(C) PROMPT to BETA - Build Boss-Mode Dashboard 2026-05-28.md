---
to: BETA
from: Amir
date: 2026-05-28
priority: HIGH
type: build the boss-mode gamified dashboard - Vercel deploy
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Build_Boss_Mode_Dashboard_2026-05-28.md
---

# BUILD: Boss-Mode Gamified Dashboard (Vercel deploy)

## Why now

Amir wants the gamified one-glance Command Center dashboard built. Original kickoff spec'd Next.js on Vercel reading from agent status JSON. Functional needs are currently met by OpenClaw native dashboard + Slack digests, but the boss-mode view spec'd in the kickoff never got built. Build it now.

## End-state target

A web app at `https://command-center-XXX.vercel.app` (XXX = whatever Vercel assigns or custom domain) that shows in a single glance:

1. **Header bar**: "Command Center" title + Amir avatar/initial + live status indicator
2. **Brand KPI strip**: Aydins revenue today vs yesterday vs 7-day average, sessions today, key conversion deltas
3. **Agent grid**: 8 agent cards — BETA, BETA Shop, BETA Insta, BETA Google, BETA Klaviyo, BETA Book, BETA Etsy, BETA Check. Each card: name, emoji avatar, current status (idle/working/blocked/escalated), current task, today's task count, streak in days, last action timestamp
4. **Big "NEEDS YOUR CALL" panel** (top of layout if any items): list of decisions pending Amir (with one-click links to context)
5. **Cost footer**: today's OpenRouter spend, today's Gemini spend, month-to-date for both, with progress bars vs caps

Mobile-responsive (Amir checks on phone). Dark theme. Editorial typography.

## Build plan

### 1. Create GitHub repo `command-center-dashboard`

- Private repo under Amir's GitHub
- License: proprietary (no public reuse)
- README.md with deployment instructions for Amir
- `.gitignore` for node_modules, .env, .vercel

### 2. Scaffold Next.js 14+ app with App Router

- TypeScript
- Tailwind CSS
- Server components where possible
- Single page `/` (no routing needed)
- Auth: simple bearer-token via env var (set in Vercel dashboard). URL like `/?token=XXX` checks against `process.env.DASHBOARD_TOKEN`. If no token or wrong: show login form.

### 3. Data fetching architecture

**Source of truth**: `/data/dashboard.json` in the same Vercel deployment.

**Update mechanism**: VPS cron job runs every 5 minutes. Reads:
- `agents/status/*.json` (agent state)
- `tasks/done.json` (compute streaks, today's task counts)
- `tasks/needs-amir-review.json` + `tasks/rollbacks.json` + `tasks/blocked-needs-amir.json` (pending items)
- `brands/aydins/state.md` or GA4 quick query (brand KPIs)
- OpenRouter API for today's spend (use existing OPENROUTER key)
- `credentials/gemini.env` daily cost tracking file

Assembles sanitized JSON. Pushes to GitHub repo via git commit + push. Vercel auto-redeploys (or fetches at runtime via revalidation).

**NEVER commit secrets, customer data, full Shopify product data, full done.json, full tasks history. Only summary stats safe for a publicly-routable URL (token-gated).**

### 4. Page layout (single page, dark theme)

```
+-----------------------------------------------------------+
|  COMMAND CENTER          [token-auth]      [live: 10:47]  |
+-----------------------------------------------------------+
|                                                           |
|  [NEEDS YOUR CALL (red border, only shows if >0 items)]  |
|   - 14 MC products pending removal                       |
|   - 4 Tier 2 negatives for Ads API review                |
|   - Holiday-Sales-Search reactivation decision           |
|                                                           |
+-----------------------------------------------------------+
|  AYDINS KPIs                                              |
|  Today    | Yesterday | 7-day avg | Revenue delta        |
|  $X,XXX   | $X,XXX    | $X,XXX    | +X.X%                |
+-----------------------------------------------------------+
|  AGENT GRID                                               |
|  +----------+ +----------+ +----------+ +----------+      |
|  | BETA  🦞 | | BETA Shop| | BETA Insta| | BETA Google|   |
|  | idle     | | working  | | idle      | | drafted    |   |
|  | streak 4 | | task: ABC| | next: 1pm | | 12 SEO opps|   |
|  +----------+ +----------+ +----------+ +----------+      |
|  +----------+ +----------+ +----------+ +----------+      |
|  | BETA     | | BETA     | | BETA     | | BETA Check |   |
|  | Klaviyo  | | Book     | | Etsy     | | idle       |   |
|  | not live | | not live | | not live | | 4 pass 0 fail   |
|  +----------+ +----------+ +----------+ +----------+      |
+-----------------------------------------------------------+
|  COST                                                     |
|  OpenRouter today: $0.42 / $15  [====-----] 2.8%         |
|  Gemini today: $0.51 / $5       [=====----] 10.2%        |
|  Month-to-date OpenRouter: $X | Gemini: $X                |
+-----------------------------------------------------------+
```

### 5. Streak calculation

For each agent: look at `tasks/done.json`, find consecutive days where that agent successfully completed at least one action without a rollback or rejection. Show as "streak: N days".

### 6. Status icons / emoji

- 🦞 BETA (commander)
- 🛍️ BETA Shop
- 📷 BETA Insta
- 🔍 BETA Google
- 📧 BETA Klaviyo
- 📘 BETA Book
- 🎨 BETA Etsy
- ✅ BETA Check

### 7. Cost data sources

- OpenRouter: query `https://openrouter.ai/api/v1/auth/key` and `https://openrouter.ai/api/v1/credits` with the API key in env. Returns usage stats.
- Gemini: maintain a daily counter file `credentials/gemini-daily-usage.json` on VPS that drafter scripts increment after each call. Sum for today + month.

### 8. Deploy instructions for Amir (output in README.md)

```
1. Create Vercel account at https://vercel.com/signup (if needed)
2. Connect GitHub account to Vercel
3. Click "New Project" -> Import from GitHub -> select `command-center-dashboard`
4. Add environment variables in Vercel dashboard:
   - DASHBOARD_TOKEN: any random string (you create), used to gate the URL
   - GITHUB_REPO_RAW_URL: the raw URL of dashboard.json in the repo
5. Click Deploy
6. Vercel gives you a URL: https://command-center-XXX.vercel.app
7. Access it at: https://command-center-XXX.vercel.app/?token=YOUR_DASHBOARD_TOKEN
8. Optional: add custom domain in Vercel project settings
```

### 9. VPS cron for data updater

Add to crontab:

```
*/5 * * * * /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/dashboard_data_updater.py >> /home/openclaw/.openclaw/command-center/logs/dashboard-updater.log 2>&1
```

The script:
1. Assembles dashboard.json from various VPS data sources (sanitized)
2. git pulls the dashboard repo
3. Writes dashboard.json
4. git commits with message "data update YYYY-MM-DD HH:MM"
5. git pushes

Use a deploy key on the VPS for the GitHub repo (read+write to dashboard-data branch, or main with restricted scope).

### 10. Auth / security

- Vercel env var `DASHBOARD_TOKEN` (Amir sets a random string)
- All pages check token against env var server-side
- Bad/missing token shows a clean login form
- No PII, no secrets, no customer data ever in the JSON

## Out of scope (defer)

- Real-time WebSocket updates (5-min refresh is fine)
- Historical charting / graphs (text stats only)
- Multi-brand view (Aydins only for now; Theonar/AWB come in Phase 6)
- Mobile push notifications (Slack already covers this)

## Verification protocol

Report back with:
1. GitHub repo URL (e.g., `https://github.com/<user>/command-center-dashboard`) — Amir to confirm he sees it
2. Path to dashboard_data_updater.py + cron line installed
3. Sanitized sample dashboard.json (paste contents — confirm NO secrets)
4. Vercel deployment instructions in README.md (paste the README section)
5. Confirmation the first dashboard.json was successfully pushed to GitHub
6. Estimated time for Amir to complete the Vercel deploy step (~5 min)
7. Confirmation no auth/PII/secret leaks

Keep response under 600 words.

## Constraints

- $0 ongoing hosting cost (Vercel free tier handles this)
- No new credentials (use existing OpenRouter key, GitHub if Amir already has it)
- Mobile-responsive (Amir checks on phone)
- Dark theme (Aydins aesthetic)
- No em dashes anywhere in UI copy
- Read-only dashboard - no actions performed from it; clicking "needs your call" items opens Slack or relevant page in new tab

## What you need from Amir if you hit a blocker

- GitHub account username (to create repo under his account, or you create under shared org)
- Decision: create repo under Amir's personal GitHub, or create new GitHub org for Aydins

If Amir hasn't provided a GitHub setup, you can:
- Create a temporary placeholder repo and put deployment instructions for Amir to fork/clone
- OR pause and request Amir to provide GitHub account auth

Execute now. Report receipts to Slack #beta-daily.
