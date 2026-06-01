---
to: BETA
from: Amir
date: 2026-05-31
priority: High
type: Dashboard infrastructure (fix stale chunk cache so future updates land without manual cache clear)
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Dashboard_Cache_Bust_2026-05-31.md
supersedes: none (follow-up to Dashboard_Queue_Cap_Readability_2026-05-31.md)
---

# PATCH: Dashboard Cache-Bust

## Why this patch

After the Suggested Resolution rollout and Queue Cap fix, the dashboard at port 3334 still served stale JS to Amir's browser across 3 rebuilds. Diagnosis (verified via SSH):

1. `command-center-dashboard-tmp` uses Next.js 16.2.6.
2. The build produces chunks under `.next/static/chunks/` with stable filenames like `12xeu293hxf70.js` that DO NOT include a content hash. Turbopack chunk hashes are derived from module path, not module content. Across builds with new code, the same chunk filename is reused.
3. Next.js serves those chunks with `Cache-Control: public, max-age=31536000, immutable`.
4. Result: browser caches the chunk for 1 year and skips the network entirely on subsequent loads. Even a normal F5 will reuse the cached version because `immutable` tells the browser "you do not need to revalidate, ever." A true hard refresh (Ctrl+Shift+R with DevTools open, or "Empty Cache and Hard Reload") does bypass this, but no normal user does that.

Every dashboard rebuild silently ships new code under the old filename, and the browser silently ignores it.

Amir saw the BETA RECOMMENDS pill only after manually clearing site data. That is unacceptable for ongoing work. Fix the build so future updates land for him on a normal refresh.

## Action 1: Override Cache-Control on chunks

Edit `command-center-dashboard-tmp/next.config.ts` (or `.js`/`.mjs`, whichever is current). Add an `async headers()` function that overrides the default `immutable` directive on `/_next/static/chunks/*` paths:

```ts
async headers() {
  return [
    {
      source: '/_next/static/chunks/:path*',
      headers: [
        { key: 'Cache-Control', value: 'public, max-age=60, must-revalidate' }
      ]
    },
    {
      source: '/_next/static/css/:path*',
      headers: [
        { key: 'Cache-Control', value: 'public, max-age=60, must-revalidate' }
      ]
    }
  ]
}
```

This:
- Lets the browser cache chunks for 60 seconds (still fast for SPA navigation, page refreshes inside that window).
- After 60s, the browser revalidates with the server. If the chunk content is unchanged, server returns `304 Not Modified` (cheap). If changed, server returns fresh content.
- Removes `immutable`, which is the directive that lets browsers skip network even on hard refresh.

Trade-off: tiny extra revalidation request per chunk after 60s of inactivity. Negligible for a single-user dashboard. Worth it to never see stale code again.

## Action 2: Deterministic, time-keyed build ID

Add `generateBuildId` to `next.config.ts` so every build has a unique ID. Even if chunk names collide across builds, the build ID changes:

```ts
generateBuildId: async () => {
  // Use git commit SHA if available (Vercel sets this), else timestamp.
  const sha = process.env.VERCEL_GIT_COMMIT_SHA || process.env.GIT_COMMIT_SHA
  if (sha) return sha.slice(0, 12)
  return `local-${Date.now().toString(36)}`
}
```

The build ID is what Next.js uses internally to invalidate the HMR manifest and route the right page version. A fresh build ID per rebuild guarantees the page's chunk references reload.

## Action 3: Verify behavior across two builds

After applying Actions 1 and 2:

1. `npm run build` once. Note the BUILD_ID and the chunk hashes that contain critical strings (e.g. `BETA RECOMMENDS`).
2. Make a trivial source change to `components/TasksKanban.tsx` (e.g. a benign comment).
3. `npm run build` again. Confirm BUILD_ID changed.
4. Restart `beta-boss-dashboard.service`.
5. `curl -sI http://127.0.0.1:3334/_next/static/chunks/<one-of-them>.js | grep -i cache-control`. Confirm it now says `max-age=60, must-revalidate` (NOT `immutable, max-age=31536000`).
6. Document both BUILD_IDs and the new Cache-Control header in the rollout report.

## Action 4: Consider switching production build off Turbopack

Next.js 16 enables Turbopack by default in `next build`. Turbopack's chunk naming does not include content hash, which is the root cause of this entire problem.

Check `command-center-dashboard-tmp/package.json` `scripts.build`. If it's `"next build"` and Next.js 16 is using Turbopack implicitly, try one of:

- `"build": "next build --no-turbopack"` (if the flag exists in 16.2.6)
- Or set `experimental.turbo: false` in next.config.ts
- Or downgrade the build path to webpack via the Next.js config flag for the version

Test: after the switch, chunks under `.next/static/chunks/` should have content-hashed filenames (e.g. `page-a8f3e2c1b4d.js` instead of `12xeu293hxf70.js`). When content changes, the filename should change.

If switching off Turbopack is not feasible in 16.2.6 (or breaks the build), document why and rely on Action 1 + 2 as the durable fix.

## Action 5: Add a stable health check

Add a simple `/version` or `/api/version` route to the dashboard that returns the BUILD_ID and a timestamp:

```ts
// app/api/version/route.ts
export async function GET() {
  return Response.json({
    build_id: process.env.NEXT_BUILD_ID || 'unknown',
    started_at: process.env.NEXT_START_TIME || new Date().toISOString(),
    revision: process.env.GIT_COMMIT_SHA || 'local'
  })
}
```

Amir can hit `https://connect.shopaydins.com/api/version` (once routed) or `http://127.0.0.1:3334/api/version` to verify which build he is looking at. If the dashboard ever feels stale again, this is the first diagnostic.

## Verification protocol

When complete, report back with:

1. The updated `next.config.ts` contents (paste).
2. Confirmation that `curl -sI http://127.0.0.1:3334/_next/static/chunks/<any>.js` returns `Cache-Control: public, max-age=60, must-revalidate` (no `immutable`).
3. Two consecutive BUILD_IDs from two rebuilds, proving they differ.
4. Whether Turbopack was switched off (yes/no + reason).
5. Sample response from the new `/api/version` endpoint.
6. Slack `#beta-daily` receipt and a summary report at `/home/openclaw/.openclaw/command-center/work/phase3/dashboard-cache-bust-2026-05-31.md`.

Amir does not need to clear browser cache for any future dashboard update after this patch lands. If a future update fails to surface within 60 seconds of a refresh, that is a regression and an alert should fire to `#beta-alerts`.

## Constraints (unchanged)

- $15/day OpenRouter cap.
- No em dashes anywhere.
- Snapshot `next.config.ts` to `backups/next.config.ts.bak-YYYY-MM-DDTHHMMSS` before edits.
- Snapshot the systemd service file if changed.
- Do not touch the existing dashboard data flow, action contract, or suggested_resolution rendering. Caching layer only.
