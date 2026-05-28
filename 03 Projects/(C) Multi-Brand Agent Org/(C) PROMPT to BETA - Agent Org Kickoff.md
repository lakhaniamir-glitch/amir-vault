---
to: BETA
from: Amir
date: 2026-05-15
priority: High
type: Architecture kickoff, supersedes prior plan
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/C_Agent_Org_Kickoff_2026-05-15.md
---

# Agent Org Kickoff: Channel-Specialist Team + Boss-Mode Dashboard

## What this is

This document defines the agent organization Amir wants you to build. It supersedes the org structure in `MULTI_BRAND_OPERATIONS_PLAN.md` (which proposed per-brand ops agents and per-brand Instagram planners). Brand briefs, duplicate content rules, Shopify setup checklists, and Instagram workflow rules in that plan **stay valid as content rules**. The agent roster and rollout sequence are replaced by this document.

## What changed and why

The prior plan over-fragmented. 9+ workflow agents create coordination overhead that prevents the team from running itself. Research on production multi-agent stacks 2025-2026 (Anthropic subagents, Claude Agent SDK, Lindy, Relevance AI, n8n + Claude case studies) converged on a simpler pattern: **channel-specialist agents with brand-scoped context**, not per-brand agent stacks. One BETA Insta agent that loads `brands/<brand>/profile.md` per task is cheaper, more maintainable, and easier for Amir to oversee than three Instagram planners.

## Locked decisions (do not redesign)

1. **Orchestration pattern:** OpenClaw native subagent invocation. BETA (GPT-5.5 via Codex OAuth, fallback DeepSeek V3.2) is the lead. Channel agents run on DeepSeek V3.2 via OpenRouter and are defined as system-prompt markdown files at `agents/<agent>.md`. BETA invokes them per task with structured input and reads structured output. No Claude Agent SDK, no LangGraph, no CrewAI. Use what you already have.

2. **Agent roster (final):**
   - **BETA** (commander, GPT-5.5 via Codex OAuth, fallback DeepSeek V3.2): plans daily, routes work, posts digest, escalates.
   - **BETA Shop** (DeepSeek V3.2 via OpenRouter): Shopify listings, products, conversion, notifications. Cross-brand.
   - **BETA Insta** (DeepSeek V3.2 via OpenRouter): Instagram organic and paid. Cross-brand.
   - **BETA Google** (DeepSeek V3.2 via OpenRouter): Google Ads and SEO. Cross-brand.
   - **BETA Klaviyo** (DeepSeek V3.2 via OpenRouter): Email. Cross-brand.
   - **BETA Book** (DeepSeek V3.2 via OpenRouter): Facebook organic and paid. Cross-brand.
   - **BETA Etsy** (DeepSeek V3.2 via OpenRouter): Etsy. Aydins primarily, ready for AWB.
   - **BETA Check** (DeepSeek V3.2 via OpenRouter): sanity-check agent. Reviews drafts and proposed changes before they queue for Amir.

3. **Brand handling:** Theonar, Amazing Wedding Bands, and Aydins are markdown brand profiles, not separate agent stacks. Each channel agent reads `/brands/<brand>/profile.md` as step one of every task. Thunder Returns is a separate motion; do not include it in this kickoff.

4. **Memory model:** Markdown plus JSON inside OpenClaw's existing workspace, mirrored to a private GitHub repo for version history. Structure:
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
   No vector DB. No Postgres. Git tracks history. The whole `command-center/` directory is a git repo synced to a private GitHub repo named `command-center-agents` under Amir's GitHub account. Never commit API keys, customer data, or store credentials.

5. **Autonomy triggers (only these three):**
   - **Daily 6am cron**: BETA plans the day, assigns work to channel agents, posts a digest.
   - **Webhooks**: Shopify orders, Klaviyo flow errors, Google Ads spend anomalies, Meta ad pacing alerts. Use n8n or Pipedream as the bridge.
   - **Manual**: Amir issues "BETA, do X" via CLI or Slack slash command.
   No continuous loops. No agent self-deciding when to run.

6. **Human checkpoints (hard):**
   - Any ad budget increase
   - Any post or content going live publicly
   - Any email sent to the list
   - Any product price change on Shopify or Etsy
   - Any new account creation, theme purchase, app install, or domain change
   Everything else is auto-approved or routed through BETA Check first.

7. **Reporting rhythm:**
   - Daily 7am digest in Slack `#beta-daily`. One message, markdown, threaded for details.
   - Weekly Monday `#beta-weekly` deeper review.
   - Hard interrupts to `#beta-alerts` (phone push enabled): revenue down, spend anomaly, customer-facing error, decision the agent cannot make.
   - No per-task notifications. Pull, not push.

8. **Dashboard (boss-mode, gamified):**
   - Lightweight web page, Next.js or Astro on Vercel.
   - Reads from `/agents/status/*.json` and `/brands/<brand>/state.md`.
   - No backend. Static reads.
   - Layout:
     - Top: Amir's commander view, named "Command Center"
     - Agent cards in a grid: avatar, name, current status (idle, working, blocked, escalated), current task, today's score (tasks done), streak (days running)
     - Brand KPI strip: revenue today vs. yesterday per brand
     - Big "Needs your call" panel front and center: anything escalated, with one-click context
     - Footer: cost today, cost this month
   - Observability layer: LangSmith for traces, debugging, cost analysis (private, under the hood, not the public-facing dashboard).

9. **Model tiering and cost discipline:**
   - BETA: GPT-5.5 via existing Codex OAuth subscription. Fallback DeepSeek V3.2 via OpenRouter if GPT-5.5 quota or auth fails.
   - All channel agents and BETA Check: DeepSeek V3.2 via OpenRouter.
   - Weekly Monday strategic synthesis: GPT-5.5 via Codex.
   - Spending controls:
     - OpenRouter budget cap set at **$15/day** on DeepSeek calls. Non-bypassable. If cap hits, log it and wait for next day; do not request a raise in Phase 0 or Phase 1.
     - GPT-5.5 runs inside existing Codex OAuth subscription. No per-day API cap; respect existing Codex quota.
     - No Anthropic API key. No Claude calls. Do not add a Claude tier without explicit Amir approval.
     - Daily cost report from OpenRouter goes into the morning digest, prominently. If yesterday's DeepSeek spend was over $10, flag as a warning.

10. **Brand voice rules carry forward** (already in `MULTI_BRAND_OPERATIONS_PLAN.md` and Aydins CLAUDE.md):
    - No em dashes (`—`) anywhere in customer-facing content or internal docs.
    - No "lifetime warranty" bare; use "Aydins Lifetime Warranty."
    - Irving in transactional contexts. Flower Mound only in marketing email footers.
    - No cross-brand content reuse. Duplicate Content Guard rules from prior plan apply.

## Rollout sequence (do not skip phases)

### Phase 0: Scaffolding (week 1)
Build the foundation. Do not light up any channel agents yet except BETA Check.

Deliverables:
1. `.claude/agents/` directory with system prompts for **BETA only** and **BETA Check only**. Other channel agent files exist as stubs but are not active.
2. `/brands/aydins/profile.md` populated from existing Aydins CLAUDE.md and prior brand brief.
3. `/brands/theonar/profile.md` populated from the Multi-Brand Operations Plan Section 2.2.
4. `/brands/amazing-wedding-bands/profile.md` populated from Section 2.3.
5. `/brands/<brand>/state.md` initialized empty with a header section: KPIs, Recent Decisions, Open Issues.
6. `/tasks/open.json` and `/tasks/done.json` initialized as empty arrays.
7. `/agents/status/*.json` initialized with `{"status":"idle","last_action":null,"streak_days":0}`.
8. Daily 6am cron defined (do not enable yet, just define the script and the trigger).
9. n8n or Pipedream account inventoried, webhook endpoints scoped but not connected.
10. Slack workspace channels created: `#beta-daily`, `#beta-weekly`, `#beta-alerts`. Do not start posting yet.

Approval gate: Amir reviews Phase 0 scaffolding before Phase 1 starts.

### Phase 1: Aydins-only pilot (weeks 2-3)
Activate only **BETA**, **BETA Shop**, **BETA Check**. Only on Aydins. Prove the loop end to end before expanding.

Deliverables:
1. BETA Shop runs one Shopify listing optimization task per day on Aydins.
2. BETA Check reviews every draft before it queues for Amir.
3. BETA posts the daily 7am digest in `#beta-daily`.
4. Boss-mode dashboard goes live with these 3 agents visible.
5. At least 10 listing optimizations completed end to end (draft, check, Amir approval, push) by end of Phase 1.

Approval gate: 30-day stability review before Phase 2. Stability means: zero unapproved publishes, zero broken Shopify listings, daily digest delivered every day, dashboard accurate.

### Phase 2: Add BETA Insta on Aydins (weeks 4-5)
Only if Phase 1 stability holds.

### Phase 3: Add BETA Google (weeks 6-7)

### Phase 4: Add BETA Klaviyo (weeks 8-9)

### Phase 5: Add BETA Book and BETA Etsy (weeks 10-11)

### Phase 6: Layer in Theonar and AWB as brand profiles (week 12+)
Brand profiles only. No new agents.

Do not light up all 7 channel agents on day one. Every documented multi-agent stack that did this in 2025-2026 collapsed within 30 days.

## What you produce first (Phase 0 deliverable)

Report back to Amir with:
1. A directory tree of the scaffolding you built.
2. The full content of every file in `/agents/` (system prompts).
3. The full content of every file in `/brands/<brand>/profile.md`.
4. The Phase 0 cron script and webhook endpoint plan.
5. A working URL to the boss-mode dashboard (can show empty/scaffolded state).
6. Confirmation that no agent has been activated to post, publish, send, or spend.
7. Cost estimate for Phase 1 month one.

Do not start Phase 1 until Amir approves Phase 0.

## How Amir will verify

Amir will:
- Pull every file you create via SCP and read them directly.
- Open the dashboard URL.
- Check that Slack channels exist and are empty.
- Spot-check that no agent has live publishing or spending capability yet.

## Constraints (hard rules, do not violate)

- No publishing of anything during Phase 0.
- No ad spend changes during Phase 0.
- No emails sent during Phase 0.
- No account creation, theme purchase, domain changes, or app installs without explicit Amir approval.
- No deletion of any existing file, listing, page, or asset.
- No em dashes in any output you write.
- Every file you create must include a comment or frontmatter noting "Created by BETA, Phase 0 scaffolding, 2026-05-15."
- Log every action to `/tasks/done.json` with timestamp, agent, action, brand, result.

## Open questions for Amir (answer before Phase 1)

1. Slack vs. Discord for digests? Default to Slack unless Amir says otherwise.
2. Vercel or local hosting for the dashboard? Default to Vercel.
3. n8n or Pipedream for webhook bridge? Default to n8n (cheaper, self-hostable).
4. Daily 6am cron in Amir's local time or UTC? Default Central Time (Irving, TX).

## Reply format when Phase 0 is complete

Use the standard verification protocol: report full output of file listings, md5 hashes of every created file, timestamps, and any errors. Do not just say "done." Show the receipts so Amir can verify independently.
