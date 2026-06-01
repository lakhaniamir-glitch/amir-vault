---
to: BETA
from: Amir
date: 2026-05-31
priority: High
type: UX overhaul of approval modal (suggested_resolution v2 schema + dashboard rewrite)
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Suggested_Resolution_UX_v2_2026-05-31.md
supersedes: extends Approval_Suggested_Resolution_2026-05-31.md (does not replace, adds fields and changes UI)
---

# PATCH: Suggested Resolution UX v2

## Why this patch

The current approval modal shows the BETA RECOMMENDS pill but the text underneath is generic boilerplate ("Multiple fixable review issues were detected. The most severe recommended action is send back."). Amir cannot tell:

1. What the task actually is, in plain English (is it a product draft, a blog post, an Instagram caption, an email campaign, a Shopify listing rewrite?).
2. What the agent did to get here (BETA Shop drafted, BETA Check validated, now Amir's turn).
3. What specifically is wrong (issues_flagged are visible but raw strings, not plain English).
4. What happens if he clicks each of the three buttons (consequences are buried).
5. Who will pick up the work next if he sends it back, and how long until it's redone.

Result: every approval still feels like a research task. Even with one-click acceptance the cognitive load is too high.

This patch (a) adds 5 new fields to the suggested_resolution schema so the agent declares all this up front, (b) restructures the modal so the dashboard reads top-to-bottom like a one-page decision brief.

## Action 1: extend the schema

Append these fields to the existing `suggested_resolution` object on every needs-amir-review task. All required, no nulls.

```json
{
  "what_is_this": "string. 1 short sentence in plain English. What is this task and what product or content does it touch. Example: \"Draft for the FALKOR tungsten ring Shopify listing (6mm and 8mm widths, $146).\"",
  "agent_trail": [
    {"agent": "BETA Shop", "did": "drafted listing copy + metafields", "at": "ISO8601"},
    {"agent": "BETA Check", "did": "validated and flagged 4 issues", "at": "ISO8601"}
  ],
  "whats_wrong": [
    "Each entry is a 1-line plain English statement of one issue.",
    "Replace raw rule names like 'MD_TOO_LONG_177' with 'Meta description is 177 chars, limit is 150'.",
    "If nothing is wrong (action=APPROVE), use one entry: 'No issues. Draft is ready to ship.'"
  ],
  "if_approve": "1 sentence. What happens the moment Amir clicks Approve. Include side effects (Shopify write, email send, ad spend, etc.).",
  "if_send_back": "1 sentence. Which agent picks it up, what they will do, and ETA. Example: \"BETA Shop will redraft with the 4 issues auto-fixed in the next 5-minute worker cycle.\"",
  "if_reject": "1 sentence. What happens to the task. Include whether the underlying product/content will be re-queued later or not.",
  "next_agent": "string or null. Which agent handles the next step if send-back is taken. Example: \"BETA Shop\" or null if no agent action."
}
```

Keep all existing fields (action, confidence, reasoning, suggested_note, risk_if_approved_asis, risk_if_rejected, auto_fixable, auto_fix_plan). The new fields are additive. Existing fields stay accurate but are now secondary in the UI.

## Action 2: rewrite the modal

Restructure the modal body into 4 clear sections, in this exact order:

### Section 1: WHAT IS THIS (top of modal, always visible)

Replace the current title block ("Needs Approval / shopify-listing #5:58:18.611Z") with a 2-line plain-English summary:

```
[Color-coded type badge: SHOPIFY LISTING | BLOG DRAFT | IG POST | EMAIL | etc.]

{what_is_this}

Trail: BETA Shop drafted -> BETA Check flagged 4 issues -> awaiting your decision
```

Use the agent_trail array to render the trail with arrows. Each step shows agent + what they did. Last step is always "awaiting your decision".

### Section 2: WHAT'S WRONG (or "looks good")

```
[icon] X ISSUES TO REVIEW

1. Meta description is 177 chars (limit 150)
2. Engraving tag is "Inside (only)", must be exactly "Inside" or "Inside & Outside"
3. Description uses "handcrafted" — manufacturing language is banned
4. Image alt text invents a scene ("ring resting on autumn leaves") not visible in the actual image

(or, if no issues:)

NO ISSUES FOUND. Draft is ready to ship.
```

Replace the current "Issues flagged" raw bullet list. Use `whats_wrong` array.

### Section 3: WHAT I RECOMMEND

```
[BIG PILL: SEND BACK | green if APPROVE, amber if SEND BACK, red if REJECT]
HIGH CONFIDENCE

Why: {reasoning}

[Primary button: APPLY RECOMMENDATION]   <- pre-fills the note, takes the action
```

This is the existing BETA RECOMMENDS block, but with the primary action button promoted to the top of this section, not buried after risk paragraphs.

### Section 4: IF YOU CLICK (three side-by-side cards)

```
┌─────────────────┬──────────────────┬─────────────────┐
│ ↻ SEND BACK     │ ✓ APPROVE        │ ✕ REJECT        │
│                 │                  │                 │
│ {if_send_back}  │ {if_approve}     │ {if_reject}     │
│                 │                  │                 │
│ [Send back]     │ [Approve]        │ [Reject]        │
└─────────────────┴──────────────────┴─────────────────┘
```

Each card shows the consequence in plain English (from the new fields) and has its own action button. This replaces the current footer with three buttons that don't explain what they do.

### Section 5: ADVANCED (collapsible, off by default)

A collapsed `<details>` block at the bottom containing:
- Full draft preview (current "Draft content" section)
- Metadata grid (current Meta blocks for handle, product ID, task ID, status)
- Raw issues_flagged array (for debugging)
- Risk if approved as-is (existing field)
- Risk if rejected (existing field)

This is for when Amir wants to dig in. Most of the time it stays collapsed.

## Action 3: update all agents that produce needs-amir-review tasks

Every agent (BETA Shop, BETA Check, BETA Google, BETA Insta, BETA Klaviyo) must populate the 5 new fields when writing to `tasks/needs-amir-review.json`. Apply the existing decision tables from Approval_Suggested_Resolution_2026-05-31.md to derive recommended_action and confidence, then write the plain-English fields based on the actual issue context.

Use this default template per agent if it has no better text:

**BETA Shop (Shopify listing drafts):**
- `what_is_this`: `"Draft for the {codename} {material} ring Shopify listing ({widths}, {price})."`
- `agent_trail[0]`: `{"agent": "BETA Shop", "did": "drafted listing copy and proposed metafields", "at": "..."}`
- `agent_trail[1]`: `{"agent": "BETA Check", "did": "validated against VESUVIUS spec, flagged N issues", "at": "..."}`
- `if_send_back`: `"BETA Shop will redraft in the next 5-minute worker cycle with the {N} issues auto-fixed. No human work needed."`
- `if_approve`: `"Shopify listing is updated immediately (title, description, meta, metafields, tags). Audit snapshot is taken before and after."`
- `if_reject`: `"Draft discarded. Listing stays as-is. Product may be re-picked next week if it still scores zero traffic."`
- `next_agent`: `"BETA Shop"` if send-back, else `null`

**BETA Google (blog drafts):**
- `what_is_this`: `"Blog post draft on {topic} ({word_count} words, source signal: {sessions} sessions in last 7d)."`
- `agent_trail[0]`: `{"agent": "BETA Google", "did": "drafted blog post with FAQ + schema", "at": "..."}`
- `if_send_back`: `"BETA Google will redraft on the next daily cycle with the {N} issues fixed."`
- `if_approve`: `"Saved as draft file in brands/aydins/blog-drafts/. You still need to paste into Shopify Blog manually."`
- `if_reject`: `"Topic burned. Next Wednesday's run picks the next-strongest topic."`
- `next_agent`: `"BETA Google"` if send-back, else `null`

**BETA Insta (IG drafts):**
- `what_is_this`: `"Instagram {post_type} for {slot} ({caption_length} chars, {hashtag_count} hashtags)."`
- `agent_trail[0]`: `{"agent": "BETA Insta", "did": "drafted caption + image prompt", "at": "..."}`
- `if_send_back`: `"BETA Insta will redraft in the next cycle."`
- `if_approve`: `"Saved to brands/{brand}/instagram-drafts/. Manual posting required."`
- `if_reject`: `"Slot skipped. Next slot will run normally."`
- `next_agent`: `"BETA Insta"` if send-back, else `null`

**BETA Klaviyo (email drafts):**
- `what_is_this`: `"Email campaign draft: {campaign_name} (segment: {segment}, subject: '{subject_line}')."`
- `agent_trail[0]`: `{"agent": "BETA Klaviyo", "did": "drafted subject + body + CTA", "at": "..."}`
- `if_send_back`: `"BETA Klaviyo will redraft."`
- `if_approve`: `"Saved to brands/{brand}/klaviyo-email-drafts/. Manual send required via Klaviyo dashboard."`
- `if_reject`: `"Campaign idea discarded."`
- `next_agent`: `"BETA Klaviyo"` if send-back, else `null`

## Action 4: backfill existing queue

Walk every entry in `tasks/needs-amir-review.json`. For each, populate the 5 new fields using the agent-specific template above. The existing `suggested_resolution` action/confidence/reasoning stays, just add the new fields.

After backfill, every task in the queue carries the full v2 schema. The dashboard rewrite (Action 2) can rely on those fields existing.

## Action 5: dashboard rewrite

Update `components/TasksKanban.tsx` in `command-center-dashboard-tmp` per Action 2's spec. Keep the existing flex-column / sticky-footer layout from the prior patch (do not regress that). The body content is what changes.

After updating, commit with author `lakhaniamir-glitch <lakhaniamir-glitch@users.noreply.github.com>` and push to GitHub. Vercel auto-deploys.

## Verification protocol

1. Confirm the schema update by showing one example task from `tasks/needs-amir-review.json` with all 5 new fields populated.
2. Confirm the agent updates by pasting the BETA Shop, BETA Google, BETA Insta, BETA Klaviyo prompts (or code changes) showing where they emit the new fields.
3. Confirm the dashboard build passes (`npm run build`) and shows the new modal layout. Take a screenshot of one task modal and save to `command-center/work/phase3/suggested-resolution-v2-screenshot-2026-05-31.png`.
4. Confirm backfill ran by showing the count of tasks updated.
5. Push the dashboard commit to GitHub. Confirm Vercel deploy by hitting `/api/version` and showing the new build_id.
6. Slack `#beta-daily` receipt + summary to `command-center/work/phase3/suggested-resolution-v2-rollout-2026-05-31.md`.

## Constraints (unchanged)

- $15/day OpenRouter cap.
- No em dashes.
- Snapshot every modified file to `command-center/backups/` before edit.
- When committing to dashboard repo: use `lakhaniamir-glitch <lakhaniamir-glitch@users.noreply.github.com>` author.
- Do not remove existing schema fields. Additive only.
- Do not change the action contract (still APPROVE / SEND_BACK_TO_AGENT / REJECT).
