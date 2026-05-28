# (C) OpenClaw — install summary

> Hetzner CPX22 · Ubuntu 24.04 · `178.105.131.33` · installed 2026-05-11

Bot identity: **@Amir Command Center Claw** 🦀 (Discord)

---

## What's running

| | |
|---|---|
| Server | Hetzner CPX22 · 4 vCPU · 4 GB RAM · 2 GB swap (swappiness 10) |
| Disk | 75 GB · 5 GB used (7%) |
| OS | Ubuntu 24.04 · kernel 6.8.0-90 |
| Node | v24.15.0 (via nvm — system stays clean) |
| OpenClaw | **2026.5.7** (`eeef486`) |
| Gateway | `127.0.0.1:18789` · **loopback only** · token auth |
| Firewall | UFW active · only SSH (22/tcp, rate-limited) open |
| sshd | password auth off · root login off · pubkey only |
| Service | `systemd --user` · lingering enabled · auto-restart |
| Backup | `/home/openclaw/backups/2026-05-12T02-59-23.313Z-openclaw-backup.tar.gz` (3.7 MB, verified) |

## Models

- **Primary:** `anthropic/claude-sonnet-4-6` (live, verified)
- **Fallback:** `openrouter/minimax/minimax-m2.7` (reasoning model, `openai-completions` API, `reasoning.effort` enabled; 196k ctx, 131k max output)
- Default timeout: 300s · thinking: adaptive

## Channels

- **Discord** — `Amir Command Center` account, `dmPolicy: pairing`
  - Status: **bot online, websocket disconnected pending intents toggle** (you fix this in 30 sec — see below)

## Scheduled jobs (cron)

| Name | Schedule | Job |
|---|---|---|
| `daily-standup` | `0 9 * * *` America/New_York | Sends morning check-in to Discord — Yesterday / Today's one thing / Watch out for / Next action. Hard cap 600 chars. |

## Persona files (`~/.openclaw/workspace/`)

- `IDENTITY.md` — Claw, blunt operator daemon, 🦀
- `USER.md` — Amir, Aydins Jewelry + Thunder Returns, blunt-direct preferences from `CLAUDE.md`
- `SOUL.md` — Push execution not planning, lead with the answer, end with the next action
- `HEARTBEAT.md` — Silent unless a real signal (failed cron / due commitment / health degradation)

---

## Daily ops cheat sheet

All commands run as `openclaw` user via SSH.

```bash
# Quick status (channels, model, gateway, sessions)
openclaw status

# Live status with probes (Discord websocket, etc.)
openclaw channels status --probe

# Tail gateway logs
journalctl --user -u openclaw-gateway -f

# Restart gateway (preserves config)
systemctl --user restart openclaw-gateway

# List cron jobs
openclaw cron list

# Run a cron job now (debug)
openclaw cron run <id>

# See last cron runs (deliveries, errors)
openclaw cron runs

# Test the model from CLI
openclaw agent --message "ping"

# Backup with verify
openclaw backup create --output ~/backups --verify

# Inspect / patch config without breaking it
openclaw config validate
echo '{ agents: { defaults: { timeoutSeconds: 360 } } }' | openclaw config patch --stdin
```

## SSH tunnel (for browser dashboard from your laptop)

```bash
# From your local machine — opens dashboard on localhost
ssh -N -L 18789:127.0.0.1:18789 openclaw@178.105.131.33
# Then open: http://localhost:18789/  (paste the gateway token when asked)
```

---

## Final action you still owe (Discord intents)

The bot **logged in successfully**, but Discord rejected the websocket with **code 4014** because the privileged intents are off. One toggle fixes it:

1. https://discord.com/developers/applications → your app → **Bot**
2. Scroll to **Privileged Gateway Intents**
3. Turn ON: **MESSAGE CONTENT INTENT**, **SERVER MEMBERS INTENT** (PRESENCE optional)
4. Save → wait ~10 seconds → DM the bot "hi"

Once you DM the bot, I'll pull your real Discord user ID from the logs and set:

```bash
openclaw config patch --stdin <<< '{commands:{ownerAllowFrom:["discord:<your-id>"]}}'
```

This locks down `openclaw`-style commands so only **you** can run them via Discord. Strangers get the pairing-code dance (`dmPolicy: pairing`).

---

## Credential rotation — do these within 7 days

Three secrets are sitting in plaintext config and in the chat history above. They were exposed for setup; rotate them now and keep them rotating quarterly.

| Credential | Why | How |
|---|---|---|
| Anthropic API key | Pasted into chat | console.anthropic.com → Settings → API Keys → create new → patch config → revoke old |
| OpenRouter API key | Pasted into chat | openrouter.ai → Keys → create new → patch config → revoke old |
| Discord bot token | Pasted into chat | Discord Dev Portal → Bot → **Reset Token** → patch config → done (the old one is dead) |

Patch flow for each:

```bash
# Anthropic
echo '{models:{providers:{anthropic:{apiKey:"sk-ant-NEW"}}}}' | openclaw config patch --stdin
# OpenRouter
echo '{models:{providers:{openrouter:{apiKey:"sk-or-v1-NEW"}}}}' | openclaw config patch --stdin
# Discord (auto-reloads, no restart needed)
echo '{channels:{discord:{token:"NEW.TOKEN.HERE"}}}' | openclaw config patch --stdin
```

After Discord rotation, also revoke the old token in the dev portal (Reset Token kills it instantly).

## OpenRouter spend cap (recommended)

You're not capped. Set one before the bot accidentally goes wild on M2.7:

- openrouter.ai → Settings → **Set credit limit** → \$20/month is plenty for fallback duty.

---

## Outstanding (low priority)

- `doctor` flags system Node 22 vs Node 24 mismatch — cosmetic. nvm path resolves it. Address later if you want a clean `openclaw doctor`.
- Auto-renewing system snapshots on Hetzner — \$0.011/GB/mo. Enable in Hetzner console under **Snapshots** if you want belt-and-suspenders.
- `plugins.allow` is empty — discord auto-loaded. Optionally pin: `{plugins:{allow:["discord","anthropic","openrouter"]}}`.

---

## Files & locations

```
~/.openclaw/openclaw.json          ← config (mode 600)
~/.openclaw/.gateway-token.secret  ← gateway token (mode 600)
~/.openclaw/workspace/             ← SOUL/USER/IDENTITY/HEARTBEAT
~/.openclaw/agents/main/           ← agent state, sessions, models.json
~/.openclaw/devices/               ← paired device tokens
~/.openclaw/logs/                  ← config health
~/backups/                         ← backup archives
~/.config/systemd/user/openclaw-gateway.service
```

---

## Next action

**Toggle the two Discord privileged intents and DM the bot.** Everything else is wired.
