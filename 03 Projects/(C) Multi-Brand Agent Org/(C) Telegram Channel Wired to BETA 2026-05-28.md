---
to: Amir (self-memory)
from: Claude
date: 2026-05-28
priority: SHIPPED
type: telegram channel wiring - BETA reachable on phone via @amir_beta_bot
---

# Telegram Channel Wired to BETA

## What

`@amir_beta_bot` ("BETA Command Center") is now a fully wired OpenClaw channel for BETA. Send a Telegram DM, BETA responds with same brain, same tools, same memory as Discord and the dashboard chat.

## Live state

| Field | Value |
|---|---|
| Bot username | `@amir_beta_bot` |
| Bot display name | `BETA Command Center` |
| Bot ID | `8346745502` |
| Your Telegram user ID | `8101774399` |
| Token file (mode 600) | `/home/openclaw/.openclaw/agents/beta/credentials/telegram.env` |
| Mode | polling (no public webhook needed) |
| DM policy | `pairing` (first DM gets a pairing code) |
| Group policy | `disabled` (DMs only, no group chats) |
| Permission level | `owner` (same as Discord) |

## Routing config in openclaw.json

```jsonc
"channels": {
  "telegram": {
    "enabled": true,
    "botToken": "<redacted>",
    "dmPolicy": "pairing",
    "name": "Beta",
    "groupPolicy": "disabled"
  }
},
"plugins": {
  "allow": [..., "telegram"]   // added
},
"tools": {
  "elevated": {
    "allowFrom": {
      "discord": ["802593004389007391"],
      "telegram": ["8101774399"]   // added
    }
  }
},
"commands": {
  "allowFrom": {
    "discord": ["802593004389007391"],
    "telegram": ["8101774399"]   // added
  },
  "ownerAllowFrom": [
    "discord:802593004389007391",
    "telegram:8101774399"        // added
  ]
}
```

## Persistence (for "forever" reliability)

- OpenClaw gateway runs as **systemd-user service**: `openclaw-gateway.service`
- User has `Linger=yes` (loginctl) so service persists even when not SSH'd in
- Auto-restarts on crash via systemd
- Survives VPS reboots
- Cron jobs (also under user systemd) keep firing
- Telegram polling reconnects automatically on network blip

## Dashboard channel health monitoring

Both channels show up as live cards on the dashboard APIs tab:
- `Discord · @Amir Command Center Claw · HEALTHY · connected, last msg Xm ago`
- `Telegram · @amir_beta_bot · HEALTHY · connected, last msg Xm ago`

Pulled every 5 min by `api_health_check.py -> chk_chat_channels()` via `openclaw channels status --probe --json`. If either goes silent, you'll see it immediately in the dashboard instead of finding out hours later when a message doesn't get a reply.

## How to use

**DM the bot from Telegram on your phone or desktop.** That's it. Native push notifications via Telegram app, replies appear inline, multimodal (images work).

Useful commands BETA understands via Telegram (same as Discord):
- Plain questions: "What did you ship today?"
- Status checks: "How is Aydins doing this week?"
- Operational asks: "Run a BETA Check on the IMPRINT listing"
- @-mention other agents (when wired): "Tell @beta-shop to push the EASTWOOD updates"

## What's still pending

1. **Rotate the bot token** — leaked in chat during setup. Open Telegram → @BotFather → `/token` → select your bot → "Revoke current token" → send me the new token, I'll update `telegram.env` + openclaw.json.
2. **Add Telegram to alert routing** — when BETA posts to Slack `#beta-daily` digest, also send a copy to your Telegram. ~10 min once you want it.
3. **Maybe consider**: making Telegram the PRIMARY notification channel (since it's faster on mobile than Slack) and Slack stays as the audit/team channel.

## Files touched

- `/home/openclaw/.openclaw/agents/beta/credentials/telegram.env` (NEW, mode 600)
- `/home/openclaw/.openclaw/openclaw.json` (PATCHED: plugins.allow, channels.telegram, routing)
- `/home/openclaw/.openclaw/openclaw.json.bak-pre-telegram-*` (backup)
- `/home/openclaw/.openclaw/command-center/scripts/api_health_check.py` (chk_chat_channels added)

## Commit / next dashboard build

The api_health_check change has already been pushed via the cron's auto-commit (Discord+Telegram cards visible in APIs tab after Vercel redeploy).

Bot URL: https://t.me/amir_beta_bot
