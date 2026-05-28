---
to: Amir (self-memory)
from: Claude
date: 2026-05-28
priority: SHIPPED
type: dashboard - Sessions tab replaced placeholder
---

# PATCH SHIPPED: Dashboard Sessions Tab

## What changed

Replaced the "Coming in next iteration" placeholder on the Sessions tab with a real session inventory pulled from OpenClaw trajectory files.

### New file: `scripts/sessions_inventory.py`

Walks every `~/.openclaw/agents/*/sessions/*.trajectory.jsonl` in the last 14 days and reconstructs per-session telemetry from the trajectory event stream:

- `session.started` -> trigger, channel, agentId, toolCount, started_at
- `prompt.submitted` -> first prompt (used for the row label)
- `model.completed` -> per-call provider, model, input/output/cache_read/cache_write tokens, computed cost
- `trace.artifacts` -> final response text (sanitized)
- `session.ended` -> status (success/aborted/timeout), ended_at

**Critical fix:** A single session can call multiple models (e.g. BETA running on GPT-5.5 spawns a DeepSeek V3.2 subagent mid-session). The inventory tracks ALL models used per session with separate token + cost rows for each. The session's overall `billing` is:
- `subscription` if all calls went to subscription providers (ChatGPT Plus OAuth)
- `metered` if all calls went to OpenRouter pay-as-you-go
- `mixed` if both

This matters because earlier I would have wrongly attributed DeepSeek cost to the GPT-5.5 "primary" model.

**Secret redaction:** Strips OpenAI keys, GitHub PATs, Shopify tokens, Google API keys, Meta long-lived tokens, JWTs from any captured prompt/response text before they touch the dashboard JSON.

### Updated `scripts/dashboard_data_updater.py`

Now calls `build_sessions_inventory()` and embeds the full payload in `dashboard.json` under the `sessions` field.

### New file: `components/SessionsView.tsx`

UI surface:
- **Top stats strip (5 cards):** Total sessions, Live now (pulses green if >0), Cash spend (metered only), Plus tokens (subscription quota usage), Avg/session
- **Search box** matches against agent + label + first_prompt + model + session_id
- **Filter pills:** Status (all/active/done/aborted/timeout), Billing (all/metered/subscription/mixed), Agent (dynamic from data)
- **Session list rows:**
  - Agent emoji + name + trigger/channel
  - Label (derived from first prompt)
  - Models used (color-coded: green for Plus, purple for Cash)
  - Calls + total tokens
  - Duration + relative time
  - Cost (or `$0` for Plus, yellow if >$0.05)
  - Billing tag, status tag
  - Click row -> expands to show: session ID, started/ended timestamps, tool count, full per-model breakdown table, first prompt, final response
- **By-agent footer:** Click any agent card to filter the list
- **Pagination:** 25 sessions default, "Show 25 more" button

### Updated `components/Dashboard.tsx`

- Imports `SessionsView` + `Session` type
- Adds `sessions` field to `DashboardData` type
- Sessions tab badge now shows live count: `data.sessions?.active ?? data.sessions?.total ?? 0`
- Replaced placeholder with `<SessionsView sessions={data.sessions} />`

## Real numbers right now

- **82 sessions** in the last 14 days
- **0 active** (last user activity was 17:47 UTC today)
- **$0.084 cash spend** across all sessions (metered providers only)
- **2.97M Plus tokens** used (408 GPT-5.5 calls, all $0 marginal)
- **Billing split:** 38 metered / 30 subscription / 14 mixed
- **Status split:** 77 done / 3 timeout / 2 aborted
- **By agent:** BETA (45 sessions, 409 calls, $0.34), BETA Shop (29, 40, $0.06), BETA Etsy (3, 9, $0.01), BETA Google (3, 5, $0.005), Main (2, 2, $0.003)

## Verified

- `python3 scripts/sessions_inventory.py` produces valid JSON
- `python3 scripts/dashboard_data_updater.py` writes `sessions` field successfully
- `npx next build` compiles cleanly
- Pushed commit `ab5b738` to `lakhaniamir-glitch/command-center-dashboard:main`
- Vercel auto-redeploys

## Files touched

- `/home/openclaw/.openclaw/command-center/scripts/sessions_inventory.py` (NEW, 250 lines)
- `/home/openclaw/.openclaw/command-center/scripts/dashboard_data_updater.py` (PATCHED, +2 lines)
- `/home/openclaw/.openclaw/command-center/command-center-dashboard-tmp/components/SessionsView.tsx` (NEW, 400 lines)
- `/home/openclaw/.openclaw/command-center/command-center-dashboard-tmp/components/Dashboard.tsx` (PATCHED)

## Commit

`ab5b738 feat(sessions): real session inventory replacing placeholder`
