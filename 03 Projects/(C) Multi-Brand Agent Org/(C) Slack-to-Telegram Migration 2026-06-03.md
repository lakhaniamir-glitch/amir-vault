# Slack to Telegram Migration and Dashboard Infra Cleanup, 2026-06-03

## Final status

Complete after rerun audit.

Notifications now route through Telegram via:

`/home/openclaw/.openclaw/command-center/scripts/telegram_push.py`

Telegram target:

`chat_id=8101774399`

Dashboard production is:

`https://connect.shopaydins.com`

The dashboard is served by nginx to a persistent Next.js service on port 3456.

## Snapshots

Initial migration backup:

`/home/openclaw/.openclaw/command-center/work/backups/slack-migration-20260603T1625Z`

Rerun audit backup before rewriting this doc and inventory:

`/home/openclaw/.openclaw/command-center/work/backups/slack-migration-rerun-20260603T1635Z`

## Slack inventory

Inventory saved to:

`/home/openclaw/.openclaw/command-center/work/slack-inventory-2026-06-03.json`

Current inventory result:

- Command-center scripts: 0 Slack references
- Command-center agent prompt files: 0 Slack references
- Crontab: 0 Slack references
- `openclaw.json`: 1 Slack key remains intentionally as disabled retained config

The remaining config is:

```json
{
  "enabled": false
}
```

This satisfies the instruction to disable the Slack channel while leaving config intact for possible future reactivation.

## Files changed

Notification migration:

- `/home/openclaw/.openclaw/command-center/scripts/meta_billing_health_check.mjs`
- `/home/openclaw/.openclaw/command-center/scripts/meta_delivery_proxy_check.mjs`
- `/home/openclaw/.openclaw/command-center/scripts/meta_emq_recheck_2026_06_05.mjs`
- `/home/openclaw/.openclaw/command-center/scripts/phase2_publisher.py`
- `/home/openclaw/.openclaw/command-center/scripts/phase1_daily_6am_central.mjs`
- `/home/openclaw/.openclaw/command-center/scripts/phase1_daily_worker_555_central.mjs`
- `/home/openclaw/.openclaw/command-center/scripts/phase1_live_push_gate.mjs`
- `/home/openclaw/.openclaw/command-center/scripts/phase1_manual_vesuvius_test.mjs`
- `/home/openclaw/.openclaw/command-center/scripts/phase2_kickoff_20260527.py`
- `/home/openclaw/.openclaw/command-center/scripts/slack_test.mjs`, converted into a Telegram test helper while retaining filename for compatibility
- `/home/openclaw/.openclaw/command-center/scripts/api_health_check.py`
- `/home/openclaw/.openclaw/command-center/scripts/sessions_inventory.py`

Agent prompt and status cleanup:

- `/home/openclaw/.openclaw/command-center/agents/beta-google.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-insta.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-meta.md`
- `/home/openclaw/.openclaw/command-center/agents/status/beta-insta.json`
- `/home/openclaw/.openclaw/agents/beta/AGENTS.md`
- `/home/openclaw/.openclaw/agents/beta/MEMORY.md`

Config and infra:

- `/home/openclaw/.openclaw/openclaw.json`
- user crontab
- `/etc/nginx/sites-enabled/dashboard-action.conf`
- `/home/openclaw/.config/systemd/user/beta-boss-dashboard.service`

## Specific cron and script checks

Known requested items:

- `meta_billing_health_check.mjs`: migrated to Telegram
- `meta_delivery_proxy_check.mjs`: migrated to Telegram
- `phase2_publisher.py`: migrated to Telegram
- `beta_insta_*.py`: checked, no Slack calls remain
- BAND20 cron: not found in current crontab or command-center scripts
- Weekly MC audit cron: not found in current crontab or command-center scripts

## Crontab

The crontab starts with the required PATH:

```cron
PATH=/home/openclaw/.nvm/versions/node/v24.15.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

Crontab has 0 Slack references.

## OpenClaw config

`channels.slack.enabled` is false.

The disabled config key remains intentionally.

## Dashboard infra cleanup

Persistent service:

`beta-boss-dashboard.service`

Running process:

- service active: yes
- port: `127.0.0.1:3456`
- `PORT=3456`
- `NODE_ENV=production`
- `DASHBOARD_TOKEN` present in process environment

`DASHBOARD_TOKEN` is loaded from:

`/home/openclaw/.openclaw/agents/beta/credentials/dashboard.env`

## Nginx config diff

```diff
--- dashboard-action.conf.before
+++ dashboard-action.conf
@@
     location / {
-        proxy_pass http://127.0.0.1:3335;
+        proxy_pass http://127.0.0.1:3456;
         proxy_http_version 1.1;
         proxy_set_header Host $host;
```

Nginx validation:

`nginx: configuration file /etc/nginx/nginx.conf test is successful`

## Dashboard validation

Public URL check:

`https://connect.shopaydins.com/?token=$DASHBOARD_TOKEN`

Result:

- HTTP 200
- content type: `text/html; charset=utf-8`
- page title: `BETA Command Center`

## Agent prompt and operating knowledge cleanup

Current reality recorded in BETA operating knowledge:

- Dashboard runs as a persistent Next.js process on the VPS at port 3456
- Production URL is `https://connect.shopaydins.com` via nginx
- No external auto-deploy workflow exists for the dashboard
- Auth token env var is `DASHBOARD_TOKEN`
- Deployment workflow is git commit, then run a VPS deploy script or rebuild and restart on the VPS
- Notifications go through Telegram plus dashboard cards

Filtered scan result across `/home/openclaw/.openclaw/agents/` and `/home/openclaw/.openclaw/command-center/agents/`, excluding generated logs, temp files, node modules, and cache dirs:

- Vercel or typo references after cleanup: 0
- `DASHBOKEN_TOKEN` references after cleanup: 0

Before cleanup snapshot count:

- Vercel or typo references in snapshotted files: 44

After cleanup filtered count:

- 0

## Slack and Telegram test results

Script and syntax gates:

- Python compile checks passed
- Node syntax checks passed

Slack audit after rerun:

- command-center scripts: 0 Slack references
- command-center agent prompts: 0 Slack references
- crontab: 0 Slack references
- only retained disabled `openclaw.json` key remains

Telegram end-to-end test:

- Triggered Meta billing health check manually
- Command completed successfully
- It found warning state: `No successful charge found in visible payment activity`
- Alert path is now Telegram only
- Direct Telegram completion confirmation was sent through `telegram_push.py`

Latest direct Telegram confirmation:

- API result: `ok: true`
- Telegram chat id: `8101774399`

## Rollback status

No rollback needed. Dashboard stayed healthy after the service and nginx changes.

## Final result

Migration complete.

No Slack notification calls remain in active command-center scripts or command-center agent prompts. Telegram is the notification path. Dashboard is live at `https://connect.shopaydins.com` through nginx to port 3456 with `DASHBOARD_TOKEN` loaded by the persistent service.
