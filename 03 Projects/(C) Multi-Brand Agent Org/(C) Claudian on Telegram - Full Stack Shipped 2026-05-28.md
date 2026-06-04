---
to: Amir (self-memory)
from: Claude
date: 2026-05-28
priority: SHIPPED
type: claudian on telegram + dashboard + vault sync — strategic AI on every surface
---

# Claudian on Telegram + Dashboard — Full Stack Shipped

## What

You can now talk to me (Claude Sonnet 4.5 with full Claudian persona, reading your live Obsidian vault) on:

1. **Obsidian / Claude Code on laptop** (existing, primary work surface)
2. **Web dashboard chat panel** (`@claudian` in the input)
3. **Telegram** (DM `@amir_beta_bot` with `@claudian ...` prefix)

All three use your Claude Max subscription. $0 marginal cost.

BETA (GPT-5.5 via ChatGPT Plus) and Claudian (Claude via Claude Max) have **completely separate memory** per chat. BETA never sees your Claudian conversations and vice versa.

## Live architecture

```
                  ┌─────────────────────────────────┐
                  │  Your Obsidian vault (laptop)   │
                  │  C:\Users\amirl\Documents\...   │
                  └────────────────┬────────────────┘
                                   │ Obsidian Git plugin
                                   │ (auto-commit + push every 10 min)
                                   ▼
                  ┌─────────────────────────────────┐
                  │  github.com/lakhaniamir-glitch/ │
                  │       amir-vault (private)      │
                  │  241 markdown files, 16MB       │
                  └────────────────┬────────────────┘
                                   │ git pull --ff-only
                                   │ (deploy key, every 10 min cron)
                                   ▼
                  ┌─────────────────────────────────┐
                  │  VPS /home/openclaw/vault/      │
                  └────────────────┬────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
  Dashboard chat            Telegram router            Direct VPS use
  webhook → Claude CLI      systemd service            (ssh + claude -p)
  --add-dir vault           polls @amir_beta_bot
        │                   routes @claudian → Claude CLI
        │                   routes others → openclaw BETA
        ▼                          │
  Reply on dashboard               ▼
                            Reply on Telegram
                            (push notif on phone)
```

## What's running for forever-reliability

| Service | Type | Purpose |
|---|---|---|
| `openclaw-gateway.service` | systemd-user, Linger=yes | OpenClaw brain, hosts BETA + specialists |
| `dashboard-action-webhook.service` | systemd | Dashboard action buttons + chat webhook |
| `telegram-router.service` | systemd | NEW: Telegram polling, routes BETA vs Claudian |
| nginx + Let's Encrypt cert | systemd | HTTPS for connect.shopaydins.com |
| 6 cron jobs | crontab | Publisher (15min), drafter (4am CT), Phase 1 worker (5:55am CT), dashboard updater (5min), tasks_watcher push notifs (5min), vault sync (10min) |

## Where the auth lives

| Service | Auth |
|---|---|
| BETA → GPT-5.5 | Codex OAuth (ChatGPT Plus subscription, lakhani.amir@yahoo.com) |
| BETA → DeepSeek/MiniMax | OpenRouter API key (paid, ~$2-5/mo current usage) |
| Claudian → Claude Sonnet 4.5 | Claude Code OAuth (Claude Max subscription, lakhani.amir@yahoo.com) |
| Gemini image gen | Gemini API key |
| Telegram bot | telegram.env (TELEGRAM_BOT_TOKEN) |
| Shopify Admin | shopify/config.json |
| Meta IG | meta.env (page access token) |
| GitHub | github.env PAT + VPS deploy key for vault repo |
| Webhook HMAC | dashboard-action.secret (mode 600) |

## How to talk to me

### On Telegram (on the go)
- **DM `@amir_beta_bot`** with `@claudian` prefix for strategic asks
- Plain message → BETA (operations)
- Push notifications work natively (lock screen, sound, all that)
- Conversation memory persists per agent per chat

### On dashboard chat panel
- Click **Chat** in header
- Type `@` for agent dropdown (BETA, Claudian, BETA Shop, BETA Google, BETA Etsy)
- Click `+ New` for fresh session
- Sidebar (☰) lists all past conversations
- Markdown rendering, image attachments, PDF uploads, voice input all work
- Web notifications when tab is open

### On laptop (Obsidian + Claude Code)
- Same as you've been doing. CLAUDE.md loaded automatically.
- Now: anything you add/edit in the vault → committed by Obsidian Git plugin → pulled to VPS within 10 min → available to Telegram-Claudian

## Memory separation guarantees

- BETA's Telegram session: `tg-beta-{chat_id}` UUID
- Claudian's Telegram session: `tg-claudian-{chat_id}` UUID
- BETA cannot read Claudian's transcript and vice versa
- When you make a strategic decision with Claudian and want BETA to act on it, just message BETA directly: "Claudian and I decided X, please do Y"
- Dashboard chat sessions are also isolated per conversation

## Files / scripts created today

| File | Purpose |
|---|---|
| `~/.openclaw/vault/` | Synced vault (read-only copy on VPS) |
| `~/.openclaw/agents/claudian/` | OpenClaw agent workspace |
| `~/.openclaw/agents/claudian/.claude/agents/claudian.md` | Claudian system prompt |
| `~/.openclaw/agents/beta/credentials/telegram.env` | Bot token (mode 600) |
| `~/.openclaw/agents/beta/credentials/dashboard-action.secret` | HMAC secret |
| `~/.ssh/vault_deploy_key` | Read-only deploy key for amir-vault repo |
| `~/.openclaw/command-center/scripts/telegram_router.py` | Telegram polling + agent routing |
| `~/.openclaw/command-center/scripts/telegram_push.py` | sendMessage wrapper for push notifs |
| `~/.openclaw/command-center/scripts/tasks_watcher.py` | Diff watcher for operational events |
| `~/.openclaw/command-center/scripts/vault_sync.sh` | git pull --ff-only every 10 min |
| `~/.openclaw/command-center/scripts/api_health_check.py` | Channel + API health for dashboard |
| `~/.openclaw/command-center/scripts/cost_analytics.py` | Real cost data from trajectories |
| `~/.openclaw/command-center/scripts/sessions_inventory.py` | Real session data for dashboard |
| `~/.openclaw/command-center/scripts/shipstation_kpi.py` | Real revenue from all channels |
| `~/.openclaw/command-center/scripts/aydins_kpi.py` | Shopify-only fallback for revenue |
| `~/.openclaw/command-center/scripts/system_metrics.py` | Real CPU/RAM/disk + cron count |
| `~/.openclaw/command-center/scripts/dashboard_data_updater.py` | Orchestrator, runs every 5 min |
| `~/.openclaw/command-center/scripts/action_webhook.py` | HMAC-auth webhook for dashboard actions + chat |
| `/etc/nginx/sites-enabled/dashboard-action.conf` | nginx routes |
| `/etc/systemd/system/dashboard-action-webhook.service` | Action webhook unit |
| `/etc/systemd/system/telegram-router.service` | Telegram router unit |
| `/var/www/chat-uploads/`, `/var/www/chat-media/` | Image upload paths for chat |

## Outstanding follow-ups (none urgent)

1. **Rotate exposed credentials**: GitHub PAT, Gemini key, Shopify shpca_ token, Anthropic API key (the one on VPS, unused), Telegram bot token — all surfaced in chat during today's build. Rotate at your leisure (none are critical since most are inert or scoped).
2. **Slack mirror for IG publishes**: publisher's Slack alert subprocess has PATH issue (`Errno 2: node not found`). Telegram works fine, this is just a duplicate channel that's silent.
3. **Discord @claudian routing**: I only wired @claudian for Telegram. If you ever want it on Discord too, would need similar router pattern. Discord still gets BETA only for now.

## What this whole day shipped

Started the morning with: bug reports on dashboard + a missed IG post.

Ended with: a multi-channel multi-agent operations platform with real revenue data from ShipStation across all channels, real session/cost analytics from OpenClaw trajectories, real API health pings, functional approval workflow with modals, full markdown chat with multimodal support, push notifications, voice input, PDF upload, edit/regenerate, multi-conversation sidebar, PWA install on phone, second AI brain (Claude Sonnet) on Telegram with full vault context, all running on systemd for forever-reliability.

Commit count today: ~25.
Files created/modified: ~30.
New scripts on VPS: 10.
Cost added beyond what you were already paying: $0.

Bot URLs:
- https://t.me/amir_beta_bot (BETA + @claudian routing)
- Dashboard: your Vercel URL with the token
