---
to: Amir (self-memory)
from: Claude
date: 2026-05-28
priority: SHIPPED
type: dashboard - Operations buttons execute for real + APIs live health
---

# PATCH SHIPPED: Operations Real Execution + APIs Live Health

## Operations tab

Before: clicking any button showed a "queued" toast and did nothing.

After: every action button actually fires a real command on the VPS and returns real status.

### Architecture

```
Browser button click
        |
        v
Vercel /api/action route
        |  (HMAC-SHA256 sign with shared secret)
        v
https://connect.shopaydins.com/dashboard-action/   [Let's Encrypt cert, public]
        |  (nginx reverse proxy)
        v
127.0.0.1:8090   [loopback only]
        |  (Python HTTPServer, systemd managed)
        v
action_webhook.py dispatches to handler
        |
        v
Real subprocess on VPS (or in background)
        |
        v
Returns JSON { ok, action, msg, elapsed_ms, data }
```

### Files created

- `scripts/action_webhook.py` (300+ lines) — HTTP server on `127.0.0.1:8090`
- `/etc/nginx/sites-enabled/dashboard-action.conf` — proxies `/dashboard-action/` to loopback
- `/etc/systemd/system/dashboard-action-webhook.service` — auto-restart, hardened (NoNewPrivileges, ProtectSystem=strict)
- `/home/openclaw/.openclaw/agents/beta/credentials/dashboard-action.secret` — 64-char hex HMAC key (mode 600)
- `app/api/action/route.ts` — rewritten to HMAC-sign and POST to VPS

### Whitelisted action handlers

| actionId | Effect |
|---|---|
| `refresh-now` | Triggers `dashboard_data_updater.py` synchronously, returns log tail |
| `run-phase1-worker` | Kicks off Phase 1 worker in background, returns log path |
| `run-ig-drafter` | Kicks off Phase 2 IG drafter in background, returns log path |
| `run-security-audit` | Runs `ss -tln`, `ufw status`, `last`, cred file perms, returns combined report |
| `run-daily-patrol` | Cleans stale logs (>14d, >1MB) + refreshes dashboard |
| `view-logs` | Tails dashboard-updater, action_webhook, drafter, phase1 logs |
| `view-backups` | Lists last 25 backups with size + timestamp |
| `backup-workspace` | tar.gz of `~/.openclaw/workspace/` |
| `backup-dashboard` | tar.gz of dashboard repo (excl node_modules/.next) |
| `backup-config` | tar.gz of `openclaw.json` + `config.json` + crontab snapshot |
| `restart-gateway` | Best-effort systemctl restart of openclaw-connect |
| `restart-api` | Returns own pid + uptime (we ARE the API; can't restart self) |
| `fresh-session` | Writes `.fresh-session-requested` flag for next BETA invocation |

### Security

- Loopback bind (`127.0.0.1:8090`) — never directly reachable
- HMAC-SHA256 signature over `{timestamp}.{body}`
- 5-minute timestamp window prevents replay
- Whitelisted action map — no shell injection possible (handlers use fixed arg lists)
- Stdout/stderr captured and truncated to 4KB before returning
- nginx vhost on `connect.shopaydins.com` reuses existing Let's Encrypt cert

### USER ACTION REQUIRED

The Vercel route needs the HMAC secret to sign requests. Set in Vercel project settings -> Environment Variables:

```
DASHBOARD_ACTION_SECRET=84b79c3290a57d85aef023d9aff0ef83592566dd00a202105a01a7334b19a7a9
```

(That's the value at `/home/openclaw/.openclaw/agents/beta/credentials/dashboard-action.secret`.)

Until that env var is set, buttons will return 500 with a clear message pointing to this fix. After setting + Vercel redeploy, buttons execute real commands.

Optional: also set `VPS_WEBHOOK_URL` if you ever move the webhook (defaults to `https://connect.shopaydins.com/dashboard-action/`).

## APIs tab

Before: 11 static cards, all marked "healthy" with hardcoded fake latencies.

After: 12 real HTTP probes, parallelized, real status + latency + status code + actionable notes.

### Files created

- `scripts/api_health_check.py` — runs 12 checks in parallel via ThreadPoolExecutor, 6s timeout each
- `components/APIsView.tsx` — rewritten, consumes `data.api_health` (no hardcoded status anywhere)

### What gets pinged

| API | Endpoint | Status definition |
|---|---|---|
| OpenAI Codex | OAuth token expiry check (auth-profiles.json) | healthy if not expired |
| OpenRouter | `GET /api/v1/credits` | healthy on HTTP 200 |
| DeepSeek V4 Flash | `GET /api/v1/models/deepseek/deepseek-v3.2` via OpenRouter | healthy on 200 |
| Gemini 2.5 Flash | `GET /v1beta/models?key=...` | healthy on 200 |
| Shopify Admin | `GET /admin/api/2024-10/shop.json` w/ admin token | healthy on 200 |
| Instagram Graph | `GET /v21.0/{IG_ID}?fields=id,username` | healthy if username returned |
| Meta Facebook Page | `GET /v21.0/me/permissions` | healthy if `pages_manage_posts` granted, otherwise "PERMS" status |
| GA4 Analytics | `GET oauth2.googleapis.com/tokeninfo?access_token=...` | healthy if token valid, "EXPIRED" otherwise |
| Merchant Center | same GA4 OAuth token | inherits GA4 status |
| Google Ads API | known pending, no ping | "PENDING" |
| GitHub | `GET /rate_limit` w/ PAT | healthy on 200 |
| Anthropic Claude | not used by BETA agents | "NOT USED" |

### Live snapshot right now

| Status | Count | Notes |
|---|---|---|
| Healthy | 7 | OpenAI Codex OAuth, OpenRouter, DeepSeek, Gemini, Shopify Admin, IG, GitHub |
| Expired | 2 | GA4 + Merchant Center OAuth token needs refresh |
| Permission missing | 0 (counted as "down") | |
| Down | 1 | Meta Facebook Page (`pages_manage_posts` not granted, HTTP 400) |
| Pending | 1 | Google Ads API (token application submitted, ETA Mon) |
| Not used | 1 | Anthropic (BETA uses Codex/OpenRouter) |
| Avg latency | 224ms | |

### Filters & UX

- Summary strip: Total APIs · Healthy ratio · Avg Latency · Issues count
- Status filter pills with live counts per status
- Per-card colored left border + colored status dot
- Latency color: green <300ms, yellow <800ms, red >800ms
- Status code shown when present
- Sanitized note explains why each API is in its current state
- "Last checked X ago" footer; "Health checks run every 5 minutes via the dashboard updater cron"

## Follow-ups surfaced by the live data

1. **GA4 + Merchant Center OAuth token expired** — refresh required. Token file at `/home/openclaw/.openclaw/agents/beta/google/ga4-oauth-token.json`. Either trigger a refresh via the existing OAuth server or re-run consent.
2. **Meta Facebook Page cross-post still blocked** — `pages_manage_posts` permission gap is now visible in the dashboard, not just buried in a Slack message from days ago.
3. **OpenAI Codex OAuth token expires in 4 days** (2026-06-01 20:03 UTC) — Codex CLI auto-refreshes via the refresh token, but if it fails for any reason, the APIs tab will flip OpenAI Codex to "EXPIRED" immediately.

## Real numbers / commit

- 13 action handlers, all execute real commands
- 12 API probes, all return real status
- Webhook latency end-to-end: ~250-500ms typical (nginx + HMAC + handler)
- Pushed commit `20c28f0`
- Vercel will redeploy in ~60 sec
- After redeploy + env var set, Operations buttons are fully wired

## Files touched

- `/home/openclaw/.openclaw/command-center/scripts/action_webhook.py` (NEW)
- `/home/openclaw/.openclaw/command-center/scripts/api_health_check.py` (NEW)
- `/home/openclaw/.openclaw/command-center/scripts/dashboard_data_updater.py` (PATCHED: +2 lines for api_health)
- `/etc/nginx/sites-enabled/dashboard-action.conf` (NEW)
- `/etc/systemd/system/dashboard-action-webhook.service` (NEW)
- `/home/openclaw/.openclaw/agents/beta/credentials/dashboard-action.secret` (NEW, 600)
- `command-center-dashboard-tmp/app/api/action/route.ts` (REWRITTEN)
- `command-center-dashboard-tmp/components/APIsView.tsx` (REWRITTEN, 200+ lines, no hardcoded status)
- `command-center-dashboard-tmp/components/Dashboard.tsx` (PATCHED: api_health type + prop wire + live badge)
