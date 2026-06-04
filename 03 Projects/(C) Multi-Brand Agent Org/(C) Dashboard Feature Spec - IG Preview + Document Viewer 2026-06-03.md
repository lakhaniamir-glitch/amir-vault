---
to: BETA (execute on Amir approval)
from: Amir (via Claudian)
date: 2026-06-03
priority: High
type: dashboard feature additions
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Dashboard_IG_Preview_Doc_Viewer_2026-06-03.md
status: DRAFTED, AWAITING AMIR APPROVAL TO EXECUTE
trigger phrase: "ship the dashboard features"
---

# Dashboard Feature Additions: IG Preview + Document Viewer

## Why this is happening

Two real product gaps surfaced 2026-06-02 night to 2026-06-03 morning:

1. The 8am CT IG post on 2026-06-03 fired with quality issues. Amir caught it fast, deleted it, had Beta correct and repost. Without a pre-flight preview surface on the dashboard, Amir cannot intervene before bad posts go live. The fix is reactive when it should be preventive.

2. The Documents section on the BETA Command dashboard displays files as raw JSON. Amir cannot read JSON on phone or desktop without a viewer. He wants click-to-open formatted previews for JSON, markdown, images, and PDFs.

Both are scoped, additive changes to the existing Next.js dashboard at `/home/openclaw/.openclaw/command-center/dashboard/`. Neither requires backend changes, both ship to production.

## Locked decisions (do not redesign)

1. **Add the Scheduled IG Posts surface as a NEW section on the dashboard**, sitting next to or near the existing Briefs section. Do not nest it inside Briefs (it has its own data shape and intervention flow).
2. **Preserve the existing Documents section behavior for power users**, but add a clickable preview layer on top. Raw JSON view stays available as a fallback for debugging.
3. **Mobile-first responsive design**. The PWA on phone is where Amir reviews most posts. Desktop is a bonus.
4. **No new backend services**. Read from existing files already in the dashboard's public/data and public/docs directories.
5. **Additive only. Do not refactor existing components.** Snapshot the dashboard codebase before any change. Rollback ready.

## Feature 1: Scheduled IG Posts Preview Section

### Data source

Pull from `~/.openclaw/command-center/command-center-dashboard-tmp/public/docs/phase2-drafts_*.json` files. Each draft JSON includes slot time, format, image path, caption, source_product, and status.

Today's slots and any future drafted slots (Jun 4, Jun 5 if available) should be displayed in chronological order.

### Card structure

Each scheduled post card shows:

| Field | Source |
|---|---|
| Slot time | filename: `phase2-drafts_2026-06-03-0800-ct-ugc.json` -> "8:00 AM CT" |
| Format badge | `ugc`, `carousel`, `product_showcase`, `reel`, etc. |
| Preview image | corresponding `phase2_2026-06-03-0800-ct-ugc.png` thumbnail |
| Caption preview | first 200 chars + "...read more" expander |
| Anchored product | source_product handle + product image thumbnail |
| Status pill | `Approved` (green), `Pending` (yellow), `Failed` (red) |
| Time until fire | computed countdown ("Fires in 6h 23m") |
| Action buttons | Edit caption / Replace image / Reject post / Approve (for ones still pending) |

### Action button behavior

- **Edit caption**: opens a modal text editor, saves back to the draft JSON, marks as edited
- **Replace image**: file picker, uploads to phase2 work dir, swaps image path in draft JSON
- **Reject post**: sets slot status to `rejected` so publisher skips it, optional reason field
- **Approve**: sets status to `approved-queued` (publisher will publish at scheduled time)

All actions hit a small webhook endpoint that updates the source JSON files. No backend rewrite needed.

### Visual layout

Three cards side by side on desktop (one per slot of the day), stacked vertically on mobile. Cards are ~320px wide on desktop. Use existing dashboard color palette.

Section title: "Scheduled IG Posts Today" with a subtitle showing date and total count.

If no slots are scheduled: show empty state "No IG posts scheduled. Check the brief drafter ran." with a refresh button.

## Feature 2: Document Viewer

### Behavior

In the Documents section, every file row gets a click target that opens a viewer modal (desktop) or full-screen viewer (mobile). The viewer renders content based on file extension.

### Supported file types

| Extension | Rendering |
|---|---|
| `.json` | Pretty-printed with collapsible nested objects. Syntax highlighted. Search box at top. |
| `.md` | Rendered as formatted markdown (use existing markdown library, e.g., `react-markdown`) |
| `.png`, `.jpg`, `.jpeg`, `.webp` | Inline image with pinch-to-zoom on mobile |
| `.pdf` | Embedded PDF viewer (use `react-pdf` or browser native iframe) |
| `.txt`, `.log` | Monospace text viewer with line numbers and search |
| `.csv` | Table view with sortable columns |

### Fallback

For unsupported types: show file metadata (name, size, modified date) and a Download button.

### Action bar in the viewer

- Download original file
- Copy file path to clipboard
- Toggle "raw" view (shows source for JSON/MD as a debug fallback)
- Close

### Mobile considerations

- Viewer takes full screen on mobile, not modal
- Swipe down to dismiss
- Tap outside (where possible) to dismiss
- Pinch-to-zoom on images and PDFs
- Word-wrap for long lines in JSON

## Implementation plan

### Phase A: Discovery (5-10 min)

- Read current dashboard file structure
- Identify which components own the Briefs section and the Documents section
- Identify the data fetching pattern (static JSON read, or API route)
- Identify the routing pattern
- Identify the styling system (Tailwind classes visible in existing UI suggest yes)
- Document findings before writing any code

### Phase B: Snapshot (mandatory before any write)

- Copy dashboard codebase to `~/.openclaw/agents/beta/backups/dashboard-pre-igpreview-{TIMESTAMP}/`
- Confirm backup is non-zero size
- Confirm existing dashboard still builds: `cd dashboard && npm run build`. Record build success.

### Phase C: Feature 1 (Scheduled IG Posts)

- Add `components/ScheduledIGPosts.tsx`
- Add `app/api/ig-posts/route.ts` (or equivalent) that reads from the public/docs JSON files
- Add `app/api/ig-posts/action/route.ts` for edit/replace/reject/approve actions
- Wire into the existing dashboard page layout next to or near the Briefs section
- Test on dev server before deploying

### Phase D: Feature 2 (Document Viewer)

- Add `components/DocumentViewer.tsx` modal component
- Add file-type detection utility
- Add renderers per extension (lazy load to keep bundle small)
- Wire into existing Documents section click handler
- Test all 6 file types on dev server

### Phase E: Build verification

- `cd dashboard && npm run build` must succeed
- If build fails, roll back from Phase B snapshot, do NOT deploy
- If build succeeds, deploy via existing deployment process (Vercel auto-deploy on git push, or manual)

### Phase F: Smoke test

- Hit live URL, confirm new IG Posts section renders today's 3 slots
- Click into a JSON file, confirm pretty-print
- Click into a markdown file, confirm rendering
- Click into an image, confirm inline
- Mobile responsive check at 375px viewport

### Phase G: Roll-up

- Post to Slack #beta-daily with deployment URL, screenshots of both new features, build size impact, any caveats
- Telegram push to Amir: "Dashboard features shipped: IG preview + document viewer"

## Hard rules

- Do not refactor existing components. Additive only.
- Do not change the dashboard color scheme, layout grid, or navigation structure.
- Do not introduce a new state management library (Redux, Zustand) if the existing dashboard does not use one.
- Do not add a new backend database. Read from existing files.
- Do not break the dashboard build under any circumstances. If build fails, roll back immediately.
- No em dashes anywhere in UI copy or code comments.
- No bare "lifetime warranty" in any sample text used in the UI.
- All UI strings should be polished, masculine, direct (match the Aydins brand voice).

## What Amir does next

1. Wake up
2. Read this spec while drinking coffee
3. If acceptable, reply "ship the dashboard features" in Slack or to Claudian
4. Beta executes, posts roll-up when done (estimated 60-90 min)
5. Review the live dashboard, iterate if needed

## Estimated cost and time

- Time: 60-90 minutes Beta execution
- Code change: ~400-600 lines across 4-6 files
- Build size impact: estimated +30-60 KB gzipped (mostly the markdown and PDF rendering libraries)
- OpenRouter cost: $1-2 for Beta agent time
- Risk if rolled back: zero. Snapshot in place.

End of spec.
