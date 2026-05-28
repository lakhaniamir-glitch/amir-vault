---
type: agent-context
agent: BETA
last-updated: 2026-05-17
---

# BETA Agent — Context Reference

Reference info for the autonomous execution agent (BETA) Amir uses for Shopify/ops/long-running tasks.

## Environment

- **Host:** Linux VPS (openclaw user)
- **Cannot see:** Amir's local Windows filesystem / vault directly
- **Can see:** Its own VPS filesystem only

## Filesystem Layout (on BETA's VPS)

| Path | Purpose |
|------|---------|
| `/home/openclaw/.openclaw/agents/beta` | BETA's current working directory / agent workspace |
| `/home/openclaw/.openclaw/workspace` | Git repo (purpose TBD — likely scratch/active work) |
| `/home/openclaw/.openclaw/command-center` | Git repo — mirrors/parallels Amir's vault "Command Center" naming; BETA writes reports here (e.g. `work/phase1/launch-ready-final-2026-05-17.md`, STOP markers) |
| `/home/openclaw/.openclaw/workspace.pre-delete-backup` | Backup of workspace before a prior cleanup |

When BETA runs `git` from its default cwd (`agents/beta`), it resolves to `workspace.pre-delete-backup`.

## Reporting Pattern

BETA writes outputs to:
- `/home/openclaw/.openclaw/command-center/work/phaseN/<task>-YYYY-MM-DD.md` — full report
- `/home/openclaw/.openclaw/command-center/work/phaseN/STOP_<reason>_YYYY-MM-DD.md` — when blocked / needs human review

## Capabilities (observed)

- Shopify Admin API: products, tags, vendors, theme files (write access proven)
- Filesystem ops in its own workspace
- Git ops on its repos
- Unknown: write access to Shopify notification templates (no official public API; would require admin-session cookies or headless browser UI automation)

## Transport for Files From Vault -> BETA

Vault is NOT git-tracked (intentional — contains journals/credentials).
To hand BETA files: stand up a small dedicated repo (folder-scoped), push from Windows, BETA pulls.

Open question to confirm per task: which of BETA's repos has a remote BETA can `git pull` from?

## Stop / Go-Live Guards

BETA uses STOP marker files in `command-center/work/phaseN/` to halt before destructive or one-way operations. Always look for STOP markers before assuming a task completed.
