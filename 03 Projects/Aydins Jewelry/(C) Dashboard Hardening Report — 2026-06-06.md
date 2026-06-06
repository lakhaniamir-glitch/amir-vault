# Dashboard refresh pipeline hardening — 2026-06-06

## Status
Completed.

## Root cause addressed
Next.js could cache a pre-write `/docs/...json` 404. Later file writes under `command-center-dashboard-tmp/public/docs/` could exist on disk while the dashboard kept serving cached 404s.

## Changes made
- Created executable cache buster: `/home/openclaw/.openclaw/command-center/scripts/bust_dashboard_cache.sh`
  - Checks port `3456`.
  - Tries `POST http://127.0.0.1:3456/api/revalidate?path=/docs`.
  - Falls back to restart via `/home/openclaw/.openclaw/command-center/scripts/start-dashboard.sh` if revalidate is unavailable or health fails.
  - Verifies `/api/version` or `/` returns HTTP 200.
  - Logs to `command-center/logs/dashboard_cache_bust.log`.
- Added dashboard route: `app/api/revalidate/route.ts`.
- Added dynamic docs route: `app/docs/[...path]/route.ts` as extra protection for dashboard-visible docs.
- Created executable health checker: `/home/openclaw/.openclaw/command-center/scripts/dashboard_health_check.sh`.
- Installed 10-minute cron via `cron_run.sh`, logging to `command-center/logs/dashboard_health_check.log`.
- Patched docs-touching scripts:
  - `dashboard_data_updater.py` calls cache bust in `finally`.
  - `action_webhook.py` calls cache bust inline after IG draft JSON edits in `public/docs`.
  - `phase2_daily_drafter.py` calls cache bust in `finally` defensively after drafter output generation.
- Added “WRITING FILES THE DASHBOARD READS” to Beta, Beta-Insta, Beta-Shop, Beta-Design, and Beta-Etsy AGENTS.md files.

## Verification
- `python3 -m py_compile` passed for patched Python scripts.
- `npm run build` passed for the dashboard Next.js app.
- Dashboard restarted once using `start-dashboard.sh` wrapper so new routes are live.
- `bust_dashboard_cache.sh` executable and returned success.
- `dashboard_health_check.sh` returned exit code 0.
- `crontab -l | grep dashboard_health_check` confirmed the 10-minute cron.
- `/` → HTTP 200; `/api/version` → HTTP 200.
- Cached-404 smoke test: requested a missing `/docs/cache-bust-smoke-20260606T172728Z-fresh.json` first (HTTP 404), wrote it to `public/docs`, ran cache bust, then fetched the same URL successfully (HTTP 200) within 30 seconds.
- `dashboard_data_updater.py` completed and ran cache bust successfully.

## Backups
Snapshots were written under `/home/openclaw/.openclaw/agents/beta/backups/` with suffix `.pre-cache-bust-2026-06-06` where files already existed.

## Stop-listed actions
None performed. No dashboard port, action secret, or action URL was changed. No drafter outputs were deleted. No cron was paused.
