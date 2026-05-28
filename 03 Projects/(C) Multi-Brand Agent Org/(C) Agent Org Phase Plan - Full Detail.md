---
title: Agent Org Phase Plan (Full Detail)
status: working-doc
captured: 2026-05-26
last-updated: 2026-05-27
source: Kickoff doc 2026-05-15, Beta Operations State 2026-05-26, install summary, Phase 1+2 go-live 2026-05-26/27
project: Multi-Brand Agent Org (BETA)
type: phase-plan
---

## STATUS SNAPSHOT (as of 2026-05-27)

| Phase | Status | First autonomous run |
|---|---|---|
| Phase 0 — Scaffolding | ✅ COMPLETE | n/a |
| Phase 1 — Shopify Aydins (VESUVIUS) | ✅ LIVE MODE | 2026-05-28 5:55 AM Central |
| Phase 2 — BETA Insta (IG-only) | ✅ LIVE MODE | First post live 2026-05-27 11:22 AM Central |
| Phase 2 FB cross-post | ⏸️ PARKED (Meta permission issue, deferred) | n/a |
| Phase 3 — BETA Google | ⬜ NOT STARTED | n/a |
| Phase 4 — BETA Klaviyo | ⬜ NOT STARTED | n/a |
| Phase 5 — BETA Book + BETA Etsy | ⬜ NOT STARTED | n/a |
| Phase 6 — Theonar + AWB brand profiles | ⬜ NOT STARTED | n/a |

### Live infrastructure (verified working)

- **Phase 1 cron schedule (Central Time):**
  - 5:55 AM daily — zero-traffic SKU picker + BETA Shop draft + BETA Check + auto-push + verify + rollback
  - 6:00 AM daily — combined digest in Slack #beta-daily
  - 11:00 PM Sundays — zero-traffic SKU list refresh
- **Phase 2 cron schedule (Central Time):**
  - */15 minutes — IG publisher (reads calendar, publishes any approved-queued slot due within 30 min)
  - 4:00 AM daily (per kickoff spec) — BETA Insta pre-dawn drafting (verify wired tomorrow)
- **Credentials (mode 600, never in vault, never in git):**
  - /home/openclaw/.openclaw/agents/beta/credentials/gemini.env (Gemini API key, $5/day cap)
  - /home/openclaw/.openclaw/agents/beta/credentials/meta.env (Page token, never expires)
- **First live results:**
  - IMPRINT VESUVIUS push (Shopify): https://shopaydins.com/products/finger-print-engraved-mens-wedding-band-two-tone-brushed-black-tungsten-ring-8mm-blue-step-edge-comfort-fit
  - IMPRINT first IG post: https://www.instagram.com/p/DY2UDdMAJKS/
  - Educational widths queued for 2026-05-27 19:00 CT
  - ABYSS queued for 2026-05-28 13:00 CT

### Open follow-ups (parked, not abandoned)

1. **FB cross-post:** Meta permission `pages_manage_posts` not propagating to tokens despite use case "Manage everything on your Page" being added. Three retry paths logged in chat. Try Meta Business Suite app toggle first, then business verification, then Buffer as fallback.
2. **Rotate Gemini API key:** Was pasted in chat history. Rotate at https://aistudio.google.com/app/apikey once Phase 2 is stable.
3. **Verify BETA Insta 4 AM Central daily drafting cron:** Currently only the publisher cron is wired. The drafter cron should exist per the kickoff spec but I haven't directly verified it. Check tomorrow.
4. **Zero-inventory audit cleanup:** 138 likely-accidental listings flagged at [[03 Projects/Aydins Jewelry/(C) Zero-Inventory Audit - 2026-05-26.md]]. Scan, mark exclusions, batch fix.
5. **30-day Phase 1+2 stability review:** Original spec required 30 days before Phase 3. Amir compressed Phase 2 start; Phase 3 (BETA Google) timing TBD.
6. **OpenClaw model conflict:** install summary lists primary as `anthropic/claude-sonnet-4-6` but kickoff said "no Claude calls." Resolve before Phase 3.

# Agent Org Phase Plan (Full Detail)

Single source of truth for the BETA agent rollout. All 7 phases, the locked decisions, hard rules, current status, and what has to ship for each phase to actually be "done."

Built from:
- `(C) PROMPT to BETA - Agent Org Kickoff.md` (2026-05-15) — original spec
- `(C) Beta Operations State — 2026-05-26.md` — what Beta says shipped
- `(C) OpenClaw — install summary.md` — VPS and infra facts

If anything below conflicts with the kickoff doc, the kickoff doc wins unless this file explicitly says it overrides.

---

## 1. Locked Decisions (do not redesign)

These were decided in the 2026-05-15 kickoff. Do not relitigate without explicit reason.

### 1.1 Orchestration pattern
OpenClaw native subagent invocation. BETA is the lead. Channel agents defined as system-prompt markdown files at `agents/<agent>.md`. BETA invokes them per task. No Claude Agent SDK, no LangGraph, no CrewAI.

### 1.2 Agent roster (final, 8 agents)
- **BETA** (commander): GPT-5.5 via Codex OAuth, fallback DeepSeek V3.2. Plans daily, routes work, posts digest, escalates.
- **BETA Shop** (DeepSeek V3.2 via OpenRouter): Shopify listings, products, conversion, notifications. Cross-brand.
- **BETA Insta** (DeepSeek V3.2): Instagram organic and paid. Cross-brand.
- **BETA Google** (DeepSeek V3.2): Google Ads and SEO. Cross-brand.
- **BETA Klaviyo** (DeepSeek V3.2): Email. Cross-brand.
- **BETA Book** (DeepSeek V3.2): Facebook organic and paid. Cross-brand.
- **BETA Etsy** (DeepSeek V3.2): Etsy. Aydins primarily, ready for AWB.
- **BETA Check** (DeepSeek V3.2): Sanity-check agent. Reviews drafts before they queue for Amir.

### 1.3 Brand handling
Theonar, Amazing Wedding Bands, and Aydins are markdown brand profiles, not separate agent stacks. Each channel agent reads `/brands/<brand>/profile.md` as step one of every task. Thunder Returns is a separate motion; not in this org.

### 1.4 Memory model
Markdown plus JSON inside OpenClaw's workspace, mirrored to a private GitHub repo `command-center-agents`. Structure:

```
/home/openclaw/.openclaw/command-center/
  README.md
  /brands/<brand>/
    profile.md          (voice, audience, products, locked rules)
    state.md            (current KPIs, recent decisions)
    /tasks/
      open.json         (queue of work)
      done.json         (audit log)
  /agents/
    beta.md
    beta-shop.md
    beta-insta.md
    beta-google.md
    beta-klaviyo.md
    beta-book.md
    beta-etsy.md
    beta-check.md
    /status/
      beta-shop.json    (live status: idle, working, blocked, last action)
      ...
```

No vector DB. No Postgres. Git tracks history. Never commit API keys, customer data, or store credentials.

### 1.5 Autonomy triggers (only these three)
1. **Daily 6am cron**: BETA plans the day, assigns work, posts digest.
2. **Webhooks**: Shopify orders, Klaviyo flow errors, Google Ads anomalies, Meta ad pacing. n8n or Pipedream as bridge.
3. **Manual**: Amir issues "BETA, do X" via CLI or Slack slash command.

No continuous loops. No agent self-deciding when to run.

### 1.6 Human checkpoints (hard, all phases)
- Any ad budget increase
- Any post or content going live publicly
- Any email sent to the list
- Any product price change on Shopify or Etsy
- Any new account creation, theme purchase, app install, or domain change

Everything else: auto-approved or routed through BETA Check first.

### 1.7 Reporting rhythm
- **Daily 7am digest** in Slack `#beta-daily`. One message, markdown, threaded.
- **Weekly Monday** `#beta-weekly` deeper review.
- **Hard interrupts** to `#beta-alerts` (phone push on): revenue down, spend anomaly, customer-facing error, decision the agent cannot make.
- No per-task notifications. Pull, not push.

### 1.8 Dashboard (boss-mode, gamified)
- Lightweight web page, Next.js or Astro.
- Reads from `/agents/status/*.json` and `/brands/<brand>/state.md`.
- No backend. Static reads.
- Layout: commander view, agent cards (avatar, status, current task, today's score, streak), brand KPI strip, big "Needs your call" panel, footer with cost today and month-to-date.
- Observability: LangSmith for traces, debugging, cost analysis (private).
- Currently runs at `http://localhost:3333/` on the VPS (loopback only). Reach via SSH tunnel: `ssh -N -L 3333:127.0.0.1:3333 openclaw@178.105.131.33`. Vercel deploy is the long-term spec.

### 1.9 Model tiering and cost discipline
- BETA: GPT-5.5 via existing Codex OAuth. Fallback DeepSeek V3.2 via OpenRouter.
- All channel agents and BETA Check: DeepSeek V3.2 via OpenRouter.
- Weekly Monday strategic synthesis: GPT-5.5 via Codex.

**Spending controls (non-bypassable):**
- OpenRouter budget cap: **$15/day on DeepSeek calls.** If cap hits, log and wait for next day. Do not request raise in Phase 0 or Phase 1.
- GPT-5.5 inside existing Codex OAuth. Respect existing Codex quota.
- **No Anthropic API key. No Claude calls.** Do not add Claude tier without explicit Amir approval.
- Daily OpenRouter cost report goes into the morning digest, prominently. Flag warning if yesterday's DeepSeek spend over $10.

### 1.10 Brand voice rules (carried forward, all phases)
- **No em dashes** anywhere in customer-facing or internal docs.
- **No "lifetime warranty" bare.** Use "Aydins Lifetime Warranty" or correct policy language.
- **Irving in transactional contexts.** Flower Mound only in marketing email footers.
- **No cross-brand content reuse.** Duplicate Content Guard rules apply.

---

## 2. Infrastructure Reference

### 2.1 VPS
- Provider: Hetzner CPX22
- OS: Ubuntu 24.04, kernel 6.8.0-90
- IP: `178.105.131.33`
- User: `openclaw`
- Auth: pubkey only (ed25519), no password
- Firewall: UFW, only port 22/tcp (SSH) open externally
- Installed: 2026-05-11

### 2.2 OpenClaw
- Version: 2026.5.7
- Gateway: `127.0.0.1:18789` (loopback only, token auth)
- Service: `systemd --user`, lingering enabled, auto-restart
- Models: primary `anthropic/claude-sonnet-4-6` (NOTE: kickoff says no Claude. This is a conflict to resolve), fallback `openrouter/minimax/minimax-m2.7`
- Default timeout: 300s, adaptive thinking
- Backup: `~/backups/2026-05-12T02-59-23.313Z-openclaw-backup.tar.gz`

### 2.3 Channels
- **Discord**: bot @Amir Command Center Claw, `dmPolicy: pairing`. Outstanding: privileged gateway intents may still be off (MESSAGE CONTENT INTENT and SERVER MEMBERS INTENT). If off, bot cannot receive DMs.
- **Slack**: `#beta-daily`, `#beta-weekly`, `#beta-alerts` exist. Bot token works via fallback script `scripts/slack_post.js`. Native OpenClaw Socket Mode delivery NOT live (missing `xapp-` app-level token).

### 2.4 SSH tunnel for dashboard
```powershell
ssh -N -L 3333:127.0.0.1:3333 openclaw@178.105.131.33
# Then in browser: http://localhost:3333/
```

### 2.5 Key files on VPS
```
/home/openclaw/.openclaw/openclaw.json          (config the service reads)
/home/openclaw/.openclaw/command-center/        (agent org root, git-tracked)
/home/openclaw/.openclaw/agents/beta/           (BETA agent state)
/home/openclaw/.openclaw/agents/beta/scripts/slack_post.js  (Slack fallback)
```

---

## 3. Phase 0 — Scaffolding (Week 1)

**Goal:** Build the foundation. No channel agents active except BETA Check. Nothing publishes, sends, posts, or spends.

### 3.1 Deliverables (10)

1. `.claude/agents/` directory with system prompts for **BETA only** and **BETA Check only**. Other channel agent files exist as stubs but inactive.
2. `/brands/aydins/profile.md` populated from existing Aydins CLAUDE.md and brand brief.
3. `/brands/theonar/profile.md` populated from Multi-Brand Ops Plan §2.2.
4. `/brands/amazing-wedding-bands/profile.md` populated from §2.3.
5. `/brands/<brand>/state.md` initialized with headers: KPIs, Recent Decisions, Open Issues.
6. `/tasks/open.json` and `/tasks/done.json` initialized as empty arrays.
7. `/agents/status/*.json` initialized as `{"status":"idle","last_action":null,"streak_days":0}`.
8. Daily 6am cron **defined but not enabled** (script and trigger exist, do not run).
9. n8n or Pipedream account inventoried, webhook endpoints scoped, **not connected**.
10. Slack channels created (`#beta-daily`, `#beta-weekly`, `#beta-alerts`). **Silent. No posting yet.**

### 3.2 Hard rules (Phase 0 only)

- No publishing of anything.
- No ad spend changes.
- No emails sent.
- No account creation, theme purchase, domain changes, app installs without explicit Amir approval.
- No deletion of any existing file, listing, page, asset.
- No em dashes in any output.
- Every file created tagged in frontmatter: `Created by BETA, Phase 0 scaffolding, 2026-05-15`.
- Every action logged to `/tasks/done.json` with timestamp, agent, action, brand, result.

### 3.3 Phase 0 completion report (required from BETA)

Before Phase 1 starts, BETA must report:
1. Directory tree of scaffolding built.
2. Full content of every file in `/agents/` (system prompts).
3. Full content of every `/brands/<brand>/profile.md`.
4. Phase 0 cron script and webhook endpoint plan.
5. Working URL to the boss-mode dashboard (empty/scaffolded state acceptable).
6. Confirmation that no agent has been activated to post, publish, send, or spend.
7. Cost estimate for Phase 1 month one.

Verification protocol: full output of file listings, md5 hashes of every created file, timestamps, errors. Not just "done." Receipts.

### 3.4 Approval gate
Amir reviews Phase 0 scaffolding before Phase 1 starts. Amir will:
- Pull every file via SCP and read directly.
- Open the dashboard URL with own eyes.
- Check Slack channels exist and are empty.
- Spot-check no agent has live publishing or spending capability.

### 3.5 Current status (audited 2026-05-26)

| # | Deliverable | Status |
|---|---|---|
| 1 | Agent prompts | UNVERIFIED |
| 2 | Aydins profile | UNVERIFIED (likely exists) |
| 3 | Theonar profile | UNVERIFIED (likely missing) |
| 4 | AWB profile | UNVERIFIED (likely missing) |
| 5 | state.md files | UNVERIFIED |
| 6 | tasks/*.json | Likely exists, likely empty (causing empty digests) |
| 7 | status/*.json | UNVERIFIED |
| 8 | Cron defined NOT enabled | SPEC VIOLATED. Live cron jobs running (BAND20 report, weekly MC audit) |
| 9 | Webhooks scoped | UNVERIFIED |
| 10 | Slack channels silent | PARTIAL. Channels exist. Not silent (daily digests posting since May 17) |

| Verification step | Status |
|---|---|
| Dashboard opened by Amir | NOT DONE |
| File tree + md5 + contents via SCP | NOT RECEIVED |
| Spot-check no live publishing/spending | NOT DONE. Several rules already broken in practice (Shopify page published, email scheduled) |

### 3.6 Phase 0 hard rule violations (current)

- **Email send rule**: BAND20 email scheduled in Klaviyo with 3-day follow-up. Not yet sent at time of audit but queued.
- **Publishing rule**: "How to Choose Men's Wedding Band" Shopify page updated and pushed live on 2026-05-26.
- **Cron enabled rule**: Cron jobs are running daily, not just defined.

### 3.7 What "Phase 0 complete" requires

- [ ] Directory tree of `/home/openclaw/.openclaw/command-center/` in hand
- [ ] `agents/beta.md`, `agents/beta-check.md`, `agents/beta-shop.md` read and confirmed real
- [ ] `brands/aydins/profile.md`, `brands/theonar/profile.md`, `brands/amazing-wedding-bands/profile.md` read and confirmed real
- [ ] Dashboard opened in browser via SSH tunnel and seen to render
- [ ] Decision made and documented: keep Phase 0 hard rules as written, OR formally upgrade spec to allow current live operations
- [ ] Cost estimate for Phase 1 month one

**Cannot proceed to clean Phase 2 until these are checked.**

---

## 4. Phase 1 — Aydins-Only Pilot (Weeks 2-3)

**Goal:** Activate BETA, BETA Shop, BETA Check. Aydins only. Prove the daily loop end to end before expanding.

### 4.1 Deliverables (5)

1. BETA Shop runs one Shopify listing optimization task per day on Aydins.
2. BETA Check reviews every draft before it queues for Amir.
3. BETA posts the daily 7am digest in `#beta-daily`.
4. Boss-mode dashboard goes live with these 3 agents visible.
5. **≥10 listing optimizations** completed end-to-end (draft, check, Amir approval, push) by end of Phase 1.

### 4.2 Stability gate (30 days before Phase 2)

- Zero unapproved publishes.
- Zero broken Shopify listings.
- Daily digest delivered every day.
- Dashboard accurate.

### 4.3 Current status (2026-05-26, day 11 of Phase 1)

| Item | Status |
|---|---|
| Daily listing optimization | NOT RUNNING AS SPEC'D. Morning digest reads "BETA Shop ready. No listing drafted in this digest run." |
| BETA Check review loop | NO EVIDENCE of structured draft → check → approve flow running daily |
| Daily 7am digest | Running, empty content |
| Dashboard live | EXISTS at localhost:3333 but never opened by Amir until 2026-05-26 SSH tunnel test |
| ≥10 listing optimizations done | 0 via the structured loop. Heavy ad-hoc Beta work happening (BAND20, MC audit, men's wedding band page, mobile QA) but not the spec'd cycle |

### 4.4 Root cause of empty digest

Most likely:
1. Cron fires the digest step but not the planner step.
2. `/tasks/open.json` is empty because nothing feeds it. No "next 10 Aydins listings to upgrade" source data exists in the queue.
3. BETA Shop sits in `idle/ready` because no task gets assigned.

### 4.5 Open decision: which Phase 1 do we ship?

**Option A — Original spec.** "1 Aydins listing optimization per day. BETA Check reviews. Amir approves. Push." Requires building the planner and the listing priority feeder. Most aligned with kickoff. Most disciplined.

**Option B — Match reality.** Beta runs structured project work week-by-week plus cron jobs for monitoring. Daily digest reports what shipped, what needs Amir's approval, what is blocked. Easier to ship because most exists. Requires rewriting the Phase 1 spec.

Recommendation: **Option B.** What is actually happening is more useful than the spec. Update the spec to match what works, then enforce the new spec.

### 4.6 What "Phase 1 complete" requires

- [ ] Option A or Option B chosen and documented
- [ ] If Option A: planner script built, listing priority feeder built, `tasks/open.json` populated with 10-15 SKUs from the [[30-Day Plan — Strengthen The Core]]
- [ ] If Option B: rewrite of §4.1 deliverables, 30-day clock restarts
- [ ] 30 consecutive days of: zero unapproved publishes, daily digest with real content, dashboard accurate
- [ ] BETA Check confirmed reviewing every draft before Amir sees it

---

## 5. Phase 2 — Add BETA Insta on Aydins (Weeks 4-5)

**Goal:** Only if Phase 1 stability holds. Activate BETA Insta. Aydins only. Instagram organic and paid.

### 5.1 Deliverables

1. `agents/beta-insta.md` system prompt written and active.
2. Aydins Instagram credentials in `.env` (read access minimum).
3. Webhook for IG comment/DM alerts via n8n.
4. BETA Insta drafts content. BETA Check reviews. Amir approves. Then schedule (no live posting until human approval per spec).
5. First 10 IG post drafts completed end-to-end by end of Phase 2.

### 5.2 Stability gate before Phase 3

- Zero unapproved posts.
- Daily digest still delivered.
- Aydins channel mix doesn't suffer (no Shop regression).

### 5.3 Current status

NOT STARTED. Cannot start until Phase 1 is stable.

---

## 6. Phase 3 — Add BETA Google (Weeks 6-7)

**Goal:** Google Ads and SEO. Cross-brand-capable but Aydins-only at this phase.

### 6.1 Head start (already shipped, will fold in)

- GA4 OAuth connected. Files in `google/ga4-*`.
- Google Merchant Center service-account API access working. Files in `google/service-account.json`, `google/fetch-merchant.js`, etc.
- Weekly MC-Shopify publish audit cron running (Mondays 10:00 UTC).
- 5,000 MC items audited 2026-05-26. 14 products flagged for removal (pending Amir approval).

### 6.2 Deliverables

1. `agents/beta-google.md` prompt.
2. BETA Google reads from GA4 + MC + Search Console + Google Ads API.
3. Drafts: keyword opportunities, ad copy variations, SEO meta improvements, MC issue triage.
4. **Spend changes require Amir approval** (hard gate from kickoff).
5. Weekly MC audit cron folds into this agent's responsibility.

### 6.3 Stability gate before Phase 4

- Zero unapproved spend changes.
- MC issue triage delivers cleaner feed (drop disapproval count over time).

### 6.4 Current status

NOT STARTED as an agent. Foundation pieces exist but not wired as a BETA Google agent.

---

## 7. Phase 4 — Add BETA Klaviyo (Weeks 8-9)

**Goal:** Email. Cross-brand-capable.

### 7.1 Head start

- BAND20 email created and scheduled (2026-05-25, runs as part of Wedding Band Week).
- Klaviyo state snapshot taken May 14: 7 flows, 5 lists, 8 campaigns, 4 templates, 56 metrics.
- Draft template `Aydins Welcome Series - Material Guide (Beta Draft)`, template ID `Uwi4fE` exists.

### 7.2 Deliverables

1. `agents/beta-klaviyo.md` prompt.
2. Read access to flows, lists, segments, campaigns, metrics.
3. Drafts campaigns and flow updates. BETA Check reviews. Amir approves. Send.
4. **All sends require explicit Amir approval** (hard gate).
5. First 5 campaigns or flow updates completed end-to-end by end of Phase 4.

### 7.3 Stability gate before Phase 5

- Zero unapproved sends.
- Email contribution to revenue trending up (baseline before Phase 4, measured after).

### 7.4 Current status

NOT STARTED as an agent. BAND20 work done by Beta directly without a dedicated Klaviyo agent.

---

## 8. Phase 5 — Add BETA Book and BETA Etsy (Weeks 10-11)

**Goal:** Facebook organic and paid (BETA Book). Etsy listing management (BETA Etsy).

### 8.1 BETA Book deliverables

1. `agents/beta-book.md` prompt.
2. Facebook page access (read minimum) and Meta Ads Manager API.
3. Drafts FB posts and ad copy. BETA Check reviews. Amir approves.
4. **Ad spend changes require Amir approval** (hard gate).

### 8.2 BETA Etsy deliverables

1. `agents/beta-etsy.md` prompt.
2. Etsy shop API access for Aydins.
3. Drafts Etsy listings, tags, titles, descriptions matching Shopify variants. BETA Check reviews. Amir approves. Push to Etsy.
4. Etsy is meaningful Aydins revenue channel. Treat with same listing quality bar as Shopify.

### 8.3 Stability gate before Phase 6

- Zero unapproved posts or listings.
- Etsy listing parity with Shopify (no orphan or stale Etsy SKUs).

### 8.4 Current status

NOT STARTED.

---

## 9. Phase 6 — Theonar and AWB Brand Profiles (Week 12+)

**Goal:** Brand profiles only. No new agents. Existing channel agents pick up the brand by reading `/brands/<brand>/profile.md` per task.

### 9.1 Deliverables

1. `/brands/theonar/profile.md` fully populated and verified (this was Phase 0 deliverable #3 — confirm it actually shipped).
2. `/brands/amazing-wedding-bands/profile.md` fully populated and verified (Phase 0 deliverable #4).
3. `/brands/theonar/state.md` initialized with current KPIs.
4. `/brands/amazing-wedding-bands/state.md` initialized.
5. Each existing channel agent (BETA Shop, BETA Insta, BETA Google, etc.) tested loading the new brand profile and producing brand-appropriate output without cross-brand leak.
6. Duplicate Content Guard verified across brands.

### 9.2 Hard rules
- No cross-brand content reuse.
- Theonar and AWB get their own voice, audience, products. Aydins voice does not transfer.

### 9.3 Current status

NOT STARTED. Likely blocked by Phase 0 deliverables #3 and #4 never being verified.

---

## 10. Cross-Phase Hard Rules (Permanent)

### 10.1 Human checkpoints (never bypass)
- Any ad budget increase.
- Any post or content going live publicly.
- Any email sent to the list.
- Any product price change on Shopify or Etsy.
- Any new account, app install, theme purchase, domain change.

### 10.2 Cost discipline
- OpenRouter DeepSeek cap: $15/day. Non-bypassable.
- No Anthropic/Claude API calls (kickoff rule). NOTE: OpenClaw primary model is currently set to `anthropic/claude-sonnet-4-6` per install summary. This is a conflict. Resolve before Phase 2.
- GPT-5.5 via Codex OAuth only. Respect existing quota.
- Daily cost report in morning digest. Warn if yesterday's DeepSeek spend over $10.

### 10.3 Brand voice
- No em dashes anywhere.
- No "lifetime warranty" bare. Use "Aydins Lifetime Warranty" or correct nuanced policy.
- Irving in transactional. Flower Mound only in marketing email footer.
- No cross-brand content reuse. Duplicate Content Guard.

### 10.4 Security
- Never commit API keys, customer data, store credentials to git.
- Never expose Slack tokens, GA4 tokens, MC service account, Shopify tokens, Klaviyo keys in outputs.
- VPS stays SSH-only externally. Loopback services reached via SSH tunnel.

---

## 11. Open Questions (Answer Before Each Phase Advance)

### 11.1 Carried from kickoff
1. Slack vs Discord for digests? Default Slack. DECISION: Slack (Discord intents flaky, Slack bot token works).
2. Vercel or local hosting for dashboard? Default Vercel. CURRENT: localhost:3333 only. Not blocking but should ship before Phase 3.
3. n8n or Pipedream for webhook bridge? Default n8n. NOT YET CONNECTED.
4. Daily 6am cron in local time or UTC? Default Central Time (Irving). VERIFY actual setting.

### 11.2 New (from 2026-05-26 audit)
5. Phase 0 reality vs spec: did we ever formally approve Phase 0 or just drift into Phase 1? RECOMMEND: backfill an approval doc with current state, mark Phase 0 done as-is with violations noted, move on.
6. Phase 1 Option A vs B (see §4.5). RECOMMEND: Option B.
7. OpenClaw model setting `anthropic/claude-sonnet-4-6` violates "no Claude calls" rule. Keep OpenClaw as-is, or switch primary to GPT-5.5 via Codex? RECOMMEND: switch (it's what the spec said).
8. Discord intents toggle: complete or not? If not, drop Discord entirely and Slack-only.

---

## 12. Immediate Next Actions (Today)

In this order:

1. **Open the dashboard.** SSH tunnel command in §2.4. Confirm it loads. Five minutes.
2. **Get the Phase 0 file dump.** Run via direct SSH (not Discord):
   ```bash
   ssh openclaw@178.105.131.33 "cd /home/openclaw/.openclaw/command-center && find . -type f -not -path '*/node_modules/*' -not -path '*/.git/*' | head -100 && echo '---' && cat agents/beta.md 2>/dev/null || echo 'NO beta.md' && echo '---' && cat brands/aydins/profile.md 2>/dev/null || echo 'NO aydins profile' && echo '---' && cat brands/theonar/profile.md 2>/dev/null || echo 'NO theonar profile' && echo '---' && cat tasks/open.json 2>/dev/null || echo 'NO open.json'"
   ```
3. **Decide on the 14 MC products** waiting on your approval (highest-leverage pending decision in the whole system).
4. **Decide Phase 1 Option A vs B.** Tell Claude. Get the rewrite drafted.
5. **Confirm Discord intents** (or formally drop Discord, Slack-only).

Once 1-5 done, Phase 0 closes honestly and Phase 1 can ship under the right spec.

---

## 13. References

- [[(C) PROMPT to BETA - Agent Org Kickoff]]
- [[(C) Multi-Brand Operations Plan]]
- [[(C) Agent Org Research - 2026-05-15]]
- [[03 Projects/Aydins Jewelry/(C) Beta Operations State — 2026-05-26]]
- [[00 Notes/(C) OpenClaw — install summary]]
- [[BETA-AGENT-CONTEXT]]
- [[03 Projects/Aydins Jewelry/30-Day Plan — Strengthen The Core]]
