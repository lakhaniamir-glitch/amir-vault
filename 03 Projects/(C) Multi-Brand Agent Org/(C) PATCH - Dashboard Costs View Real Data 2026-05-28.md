---
to: Amir (self-memory)
from: Claude
date: 2026-05-28
priority: SHIPPED
type: dashboard - real cost analytics replaces hardcoded mocks
---

# PATCH SHIPPED: Dashboard Costs View - Real Data End-to-End

## Why

Amir caught that the Costs view numbers were fake (2,539 entries / 121 sessions / $0.04 avg-session / Cache Write 68% / sessions list with names but placeholder dollar amounts). He said: "Yes make everything real and working not just fake numbers."

## What changed

### 1. New module: `cost_analytics.py`

Path: `/home/openclaw/.openclaw/command-center/scripts/cost_analytics.py`

Pulls real data from THREE sources:

**A. OpenRouter API (live HTTP):**
- `GET /api/v1/auth/key` -> usage_daily, usage_weekly, usage_monthly, usage_lifetime
- `GET /api/v1/credits` -> total_credits, total_usage, remaining

**B. Gemini cost files:**
- Scans `work/phase2/gemini-costs-*.json` written by the drafter
- Sums today + month-to-date

**C. OpenClaw trajectory files:**
- Walks `~/.openclaw/agents/*/sessions/*.trajectory.jsonl`
- For every `model.completed` event in the lookback window, extracts:
  - `provider`, `modelId`, `sessionKey` (-> agent name), `sessionId`
  - `data.promptCache.lastCallUsage.input/output/cacheRead/cacheWrite` tokens
- Computes cost using a pricing table:
  - DeepSeek V4 Flash: $0.07/$0.28 per 1M (input/output)
  - DeepSeek V3.2: $0.27/$0.40
  - MiniMax M2.7: $0.30/$0.55
  - GPT-5.5: $1.25/$10.00
  - GPT-5 Nano: $0.05/$0.40
  - Cache reads at 20% of input rate, cache writes at 125% (per OpenRouter convention)

**Output shape (`costs` in dashboard.json):**
```
{
  "openrouter": {
    "today_spend_usd": 2.3162,
    "week_spend_usd": 5.1974,
    "month_spend_usd": 20.1042,
    "lifetime_spend_usd": 20.1042,
    "credits_total": 40,
    "credits_remaining": 19.8958,
    "daily_cap_usd": 15.0,
    "source": "openrouter_api_v1"
  },
  "gemini": { ... },
  "analytics_7d": {
    "entries": 260,           // real LLM call count
    "sessions": 42,           // real session count
    "total_cost_usd": 1.7248, // sum from trajectories
    "avg_session_usd": 0.0411,
    "avg_entry_usd": 0.006634,
    "by_model": [
      { "model": "gpt-5.5", "cost": 1.4263, "entries": 163, ... },
      { "model": "openrouter/deepseek/deepseek-v3.2", "cost": 0.2888, ... },
      ...
    ],
    "by_agent": [
      { "agent": "BETA", "cost": 1.6826 },
      { "agent": "BETA Shop", "cost": 0.0229 },
      ...
    ],
    "breakdown": {
      "input_tokens": 676774, "input_cost": 0.5139,
      "output_tokens": 104500, "output_cost": 0.3731,
      "cache_read_tokens": 8593775, "cache_read_cost": 0.8376,
      "cache_write_tokens": 0, "cache_write_cost": 0
    },
    "recent_sessions": [ ... top 20 by most-recent activity ... ],
    "daily_series": [
      { "date": "2026-05-22", "cost": 0.0804 },
      ...
      { "date": "2026-05-28", "cost": 0.5932 }
    ]
  }
}
```

### 2. Updater patched

`dashboard_data_updater.py` now:
- Imports `cost_analytics.build_costs_payload`
- Removed `get_openrouter_usage()` (was `random.randint(45000, 65000)`)
- Removed `get_gemini_usage()` placeholder month-spend bump
- Backup: `dashboard_data_updater.py.bak-pre-realcosts`

### 3. CostsView.tsx rewritten

Path: `command-center-dashboard-tmp/components/CostsView.tsx`

Removed:
- Hardcoded `2,539 entries / 121 sessions / $0.04 avg-session / $0.001 avg-msg`
- Hardcoded `dailyValues = [22, 18, 45, 28, 32, 20, ...]` sparkline
- Hardcoded `byModel` percentages (DeepSeek V4 Flash 60% / GPT-5.5 25% / Gemini 12% / MiniMax 3%)
- Hardcoded `bySource` donut (Cron 70% / Manual 20% / Webhooks 10%)
- Hardcoded `breakdown` bars (Cache Write 68% $94.68 / Output 8% $11.78 / Cache Read 24% $32.91 / Input 0%)
- Hardcoded Sessions list (Phase 1 Shopify worker, Wave1 unblock, EASTWOOD regen, etc.)

Added:
- Live OpenRouter today / week / month / lifetime spend cards
- Real daily-cost sparkline computed from per-call timestamps
- Real Sessions panel showing actual session IDs, agent, model, call count, relative timestamp ("3m ago")
- Real By Model donut with actual cost percentages and per-model dollar amounts
- Real Cost Breakdown bars (input vs output vs cache read vs cache write) using real token counts
- Real By Agent grid showing which agent burned what
- "Credits remaining" tile showing live OpenRouter balance
- Defensive empty states ("No LLM activity in the last 7 days") if trajectories haven't fired

### 4. OpenRouter key staged

`/home/openclaw/.openclaw/agents/beta/credentials/openrouter.env` (mode 600)
- Copied from the existing key in `openclaw.json` -> `models.providers.openrouter.apiKey`
- Read by `cost_analytics.py` only; never logged

## Real numbers right now (2026-05-28 ~19:10 UTC)

| Metric | Was (fake) | Is (real) |
|---|---|---|
| OpenRouter today | random $8.40 | **$2.32** |
| OpenRouter 7d | derived from random | **$5.20** |
| OpenRouter month | random $5-17 | **$20.10** |
| Credits remaining | not shown | **$19.90** of $40 |
| Gemini today | $0.35 (was real) | $0.35 |
| Entries (calls) | "2,539" | **260** |
| Sessions | "121" | **42** |
| Avg/session | "$0.04" | **$0.041** (lucky coincidence on a real number close to the fake) |
| Avg/call | "$0.001" | **$0.0066** |
| Top model by cost | "DeepSeek V4 Flash 60%" | **GPT-5.5 ($1.43, 163 calls, 83%)** |
| Top cost component | "Cache Write 68%" | **Cache Read 49% ($0.84)** |

## Verified

- `python3 scripts/cost_analytics.py` runs clean, returns valid JSON
- `python3 scripts/dashboard_data_updater.py` populates `public/data/dashboard.json` with real costs payload
- `npx next build` compiles cleanly with TypeScript
- Pushed commit `e150755` to `lakhaniamir-glitch/command-center-dashboard:main`
- Vercel will auto-redeploy within ~60 sec

## Pending follow-ups

1. The pricing table is a snapshot. When OpenRouter changes a model's price, edit `MODEL_PRICES` in `cost_analytics.py`.
2. Gpt-5.5 (via openai-codex direct, not OpenRouter) cost is estimated — real Codex billing isn't exposed via this API. If Anthropic adds a usage endpoint, wire it.
3. The OpenRouter API key is a regular (not management) key, so `/activity` and `/keys/usage` endpoints return 403/401. We don't need them — we have richer per-call data from local trajectories.
4. `cost_analytics.py` parses every trajectory file under `~/.openclaw/agents/*/sessions/`. At ~260 calls/7d this is fast. If trajectory volume grows 100x, add a date-prefix index or persist a rolling aggregate.

## Files touched

- `/home/openclaw/.openclaw/command-center/scripts/cost_analytics.py` (NEW, 270 lines)
- `/home/openclaw/.openclaw/command-center/scripts/dashboard_data_updater.py` (PATCHED: removed 2 placeholder funcs)
- `/home/openclaw/.openclaw/command-center/command-center-dashboard-tmp/components/CostsView.tsx` (REWRITTEN, 336 lines)
- `/home/openclaw/.openclaw/agents/beta/credentials/openrouter.env` (NEW, mode 600)

## Commit

`e150755 feat(costs): replace hardcoded mock data with real OpenRouter API + trajectory analytics`
