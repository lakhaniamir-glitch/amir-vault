---
to: BETA
from: Amir
date: 2026-05-31
priority: High
type: Approval workflow upgrade (add Suggested Resolution to every needs-amir-review payload)
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Approval_Suggested_Resolution_2026-05-31.md
supersedes: none (additive to existing needs-amir-review flow)
---

# PATCH: Approval Suggested Resolution

## Why this patch

Right now every `needs-amir-review` task surfaces in BETA Command with the flagged issues but no recommended action. Amir has to evaluate each one from scratch: read the product, read the issues, decide between APPROVE, SEND BACK, REJECT, and write a note. That is 1 to 3 minutes per task. With 10+ pending reviews per day this is the biggest manual cost in the pipeline.

BETA already detects the issues. BETA can also recommend the resolution. This patch makes every `needs-amir-review` task carry a `suggested_resolution` payload so the dashboard can pre-fill the action and the note. Amir confirms (one click) or overrides. Most reviews drop to under 10 seconds.

This is additive. Nothing existing breaks. Amir always retains final say.

## New payload schema (required on every needs-amir-review task)

Add a `suggested_resolution` block to every task written to `tasks/needs-amir-review.json` (and the equivalent for blog drafts, IG drafts, and any other approval surface):

```json
{
  "task_id": "...",
  "type": "shopify-listing | blog-draft | ig-draft | ...",
  "status": "needs-amir-review",
  "issues_flagged": [...existing...],
  "suggested_resolution": {
    "action": "APPROVE | SEND_BACK_TO_AGENT | REJECT",
    "confidence": "HIGH | MED | LOW",
    "reasoning": "1 to 2 sentences. Why this action vs the other two.",
    "suggested_note": "Pre-written note text Amir can paste or edit. Speaks to the agent that produced the draft.",
    "risk_if_approved_asis": "What breaks if Amir clicks APPROVE without fixing.",
    "risk_if_rejected": "What value is lost if Amir clicks REJECT.",
    "auto_fixable": true,
    "auto_fix_plan": "If auto_fixable=true, exactly what BETA will do on SEND_BACK. If false, why a human is required."
  }
}
```

All fields required. Use `null` only for `auto_fix_plan` when `auto_fixable=false` (and still include the reason in `reasoning`).

## Decision rules (BETA must apply these at suggestion time)

Apply the matching rule by `type` + `issues_flagged`. If multiple issues, take the most severe action (REJECT > SEND_BACK > APPROVE).

### Shopify listing reviews

| Issue flagged | Default action | Confidence | Auto-fixable |
|---|---|---|---|
| Supplier or trade-show name found (Thorsten, Universal Jewelry, JCK, Stuller, Jewelry Depot in customer-facing copy) | SEND_BACK | HIGH | Yes. Strip vendor names, rewrite affected sentence. |
| Bare lifetime warranty wording found | SEND_BACK | HIGH | Yes. Replace with "Aydins Lifetime Warranty. See policy page for terms." |
| Em dash found in copy | SEND_BACK | HIGH | Yes. Replace with period, comma, colon, or parens per context. |
| Meta title > 70 chars | SEND_BACK | HIGH | Yes. Trim to <=70, preserve CODENAME and primary keyword. |
| Meta description > 150 chars | SEND_BACK | HIGH | Yes. Trim to <=150. |
| Missing meta description | SEND_BACK | HIGH | Yes. Generate from product copy. |
| FAQ count != 6 (VESUVIUS) | SEND_BACK | HIGH | Yes. Add or remove FAQs to hit exactly 6 product-specific questions. |
| FAQ contains policy question (warranty, returns, shipping, sizing, exchange) | SEND_BACK | HIGH | Yes. Replace with product-specific question per VESUVIUS Section 4. |
| custom.keywords not in labeled format | SEND_BACK | HIGH | Yes. Reformat to Material:, Inlay/Feature:, Widths:, Fit:, Profile:, Engraving:. |
| SKU format mismatch vs vendor source | SEND_BACK | HIGH | Yes. Rewrite SKU per vendor convention. |
| Standalone Engraving section duplicates Key Features/FAQ | SEND_BACK | MED | Yes. Remove duplicate. |
| Trust-pillar bullets in Key Features (Free U.S. Shipping, etc.) | SEND_BACK | HIGH | Yes. Strip from Key Features. |
| Invented image scene description | SEND_BACK | MED | Yes. Replace with literal description from actual image. |
| Handcrafted / handmade / forged / built / cut wording | SEND_BACK | HIGH | Yes. Replace with neutral verb. |
| Price below cost | REJECT | HIGH | No. Margin decision is human only. |
| Image quality fail | SEND_BACK | MED | No. Needs new shoot. |
| Variant restructure detected in BETA Shop output | REJECT | HIGH | No. Variant work is out of scope for Phase 1 auto-push. |
| Duplicate content vs another live PDP (>80% similarity) | SEND_BACK | MED | Yes. Rewrite. |
| All VESUVIUS checks pass, no other issues | APPROVE | HIGH | N/A |

### Blog draft reviews (BETA Google)

| Issue flagged | Default action | Confidence | Auto-fixable |
|---|---|---|---|
| Source signal < 3 sessions / 7d | REJECT | MED | No. Topic not worth the slot. |
| Source signal 3 to 9 sessions / 7d, all other checks pass | APPROVE | MED | N/A |
| Source signal >= 10 sessions / 7d, all other checks pass | APPROVE | HIGH | N/A |
| Em dash in body | SEND_BACK | HIGH | Yes. Replace per rule. |
| Meta title > 70 chars or meta description > 150 chars | SEND_BACK | HIGH | Yes. Trim. |
| Word count < 600 | SEND_BACK | MED | Yes. Expand to 800+. |
| Missing JSON-LD schema (Article + FAQPage when FAQ exists) | SEND_BACK | HIGH | Yes. Inject schema block. |
| No author byline / E-E-A-T signal | SEND_BACK | MED | Yes. Add "By Amir Lakhani, founder, Aydins Jewelry, est. 2011." |
| Comparison section present as prose, not table | SEND_BACK | MED | Yes. Convert prose comparison to markdown table. |
| No TL;DR / summary block at top | SEND_BACK | LOW | Yes. Add 2-sentence summary. |
| FAQ contains only generic questions (no long-tail intent) | SEND_BACK | MED | Yes. Add 2 long-tail Q&A pairs targeting AI Mode queries. |
| Internal link suggestions broken (404) | SEND_BACK | HIGH | Yes. Swap to live collection URLs. |
| Duplicate vs existing blog (>70% similarity) | REJECT | HIGH | No. Topic burned. |
| All checks pass | APPROVE | HIGH | N/A |

### IG draft reviews (BETA Insta)

| Issue flagged | Default action | Confidence | Auto-fixable |
|---|---|---|---|
| Caption > 2200 chars | SEND_BACK | HIGH | Yes. Trim. |
| Hashtag count outside 8 to 15 range | SEND_BACK | HIGH | Yes. Adjust. |
| Banned hashtag detected | SEND_BACK | HIGH | Yes. Replace. |
| Image composition fail (per IG variety patch) | SEND_BACK | MED | Yes. Regenerate. |
| Caption contains em dash | SEND_BACK | HIGH | Yes. Replace. |
| Off-brand voice (per profile.md) | SEND_BACK | MED | Yes. Rewrite caption. |
| All checks pass | APPROVE | HIGH | N/A |

### Universal fallback

If `issues_flagged` is non-empty and no rule above matches:
- `action: SEND_BACK_TO_AGENT`
- `confidence: LOW`
- `reasoning: "Unrecognized issue type. Defaulting to send-back for human review. Add a rule for this issue type to the decision table."`
- `auto_fixable: false`

Then log to `tasks/missing-resolution-rules.json` so Amir can extend the table.

## Confidence calibration

- **HIGH:** Rule has a deterministic check and a deterministic fix. Amir has accepted this resolution >= 5 times historically with no override, OR the rule is a hard policy (em dashes, supplier names, meta length).
- **MED:** Rule has a deterministic check but the fix involves judgment (rewriting voice, trimming for meaning). Amir has accepted this resolution >= 2 times.
- **LOW:** New rule, ambiguous issue, or Amir has overridden it within the last 7 days.

Track `suggestion_accept_rate` per `(type, issue_flagged)` pair. Recompute confidence weekly. If accept rate drops below 70%, downgrade one level and post to `#beta-daily` for Amir to review the rule.

## BETA Command dashboard UI changes

Above the existing three buttons (REJECT / SEND BACK TO AGENT / APPROVE), render:

```
+--------------------------------------------------------------+
| BETA RECOMMENDS: SEND BACK   [HIGH confidence]               |
| Why: <reasoning text>                                        |
|                                                              |
| Suggested note (editable below, click APPROVE SUGGESTION     |
| to send back with this note as-is):                          |
+--------------------------------------------------------------+
| [ APPROVE SUGGESTION ]   (one-click: takes the suggested     |
|                           action with the suggested note)    |
+--------------------------------------------------------------+
```

Pre-fill the existing "Note" textarea with `suggested_note`. Amir can:
1. Click **APPROVE SUGGESTION** -> fires the suggested action with the suggested note. Logged as `resolution: accepted_suggestion`.
2. Edit the note then click one of the three existing buttons -> fires that action with the edited note. Logged as `resolution: overrode_note`.
3. Click a different button than recommended -> fires that action. Logged as `resolution: overrode_action` with both the suggested and actual action recorded.

Color the "BETA RECOMMENDS" pill:
- HIGH = green
- MED = amber
- LOW = red (forces Amir to read carefully, no one-click acceptance allowed for LOW confidence; require explicit button click)

## Audit + learning loop

Every resolution writes to `needs-amir-review-archive.jsonl` with:

```json
{
  "task_id": "...",
  "resolved_at": "ISO8601",
  "suggested_action": "...",
  "suggested_confidence": "...",
  "actual_action": "...",
  "actual_note": "...",
  "resolution_type": "accepted_suggestion | overrode_note | overrode_action",
  "time_to_resolve_seconds": 12
}
```

Once a week (Sunday 10 PM Central), BETA computes per-rule accept rate and writes a report to `/home/openclaw/.openclaw/command-center/work/approvals/weekly-accept-rate-YYYY-MM-DD.md`. Post summary to `#beta-daily`. Rules with accept rate < 70% over the last 14 days get flagged for Amir review.

## Specific guidance for the current pending task

Apply these rules immediately. The current pending task in BETA Command at the time of this patch:

- **task:** review #0:57:11.876Z
- **product handle:** austin-blue-and-green-opal-inlay
- **product id:** gid://shopify/Product/12182289348
- **issues flagged:** "Supplier or trade-show name found", "Bare lifetime warranty wording found"

Per the table above, both issues default to SEND_BACK with HIGH confidence and are auto-fixable. The `suggested_resolution` payload for this task should be:

```json
{
  "action": "SEND_BACK_TO_AGENT",
  "confidence": "HIGH",
  "reasoning": "Two policy violations detected. Supplier name leaks sourcing and hurts brand. Bare 'lifetime warranty' is an FTC disclosure risk. Both are deterministic copy fixes.",
  "suggested_note": "Fix two issues: (1) Remove the supplier or trade-show name from title/description. We do not expose sourcing. (2) Replace 'lifetime warranty' with 'Aydins Lifetime Warranty. See policy page for terms.' Bare lifetime warranty is an FTC disclosure risk and ambiguous. Resubmit when both are clean.",
  "risk_if_approved_asis": "Brand exclusivity erosion (commodity signal to customers), potential trademark issue with supplier name, FTC Mag-Moss warranty disclosure exposure.",
  "risk_if_rejected": "Listing remains in zero-traffic state, lost SEO/conversion opportunity on a real product (austin-blue-and-green-opal-inlay).",
  "auto_fixable": true,
  "auto_fix_plan": "BETA Shop reruns draft with two patches: (1) regex-strip vendor name patterns from title/desc/Key Features, (2) replace any standalone 'lifetime warranty' phrase with the approved wording. Re-run BETA Check, resubmit to needs-amir-review."
}
```

Surface this on the existing pending task immediately so Amir can validate the format before the rest of the queue is backfilled.

## Verification protocol

Report back with:

1. Updated schema for `tasks/needs-amir-review.json` and its blog-draft and ig-draft equivalents. Paste the JSON schema or TypeScript types.
2. Updated BETA Check / BETA Google / BETA Insta validators that emit `suggested_resolution` on every flag. Paste code path and a sample output for one task of each type.
3. Updated BETA Command dashboard UI showing the new "BETA RECOMMENDS" block above the buttons. Screenshot or screenshot of the local dev render. Confirm color coding (HIGH=green, MED=amber, LOW=red) and confirm one-click "APPROVE SUGGESTION" works for HIGH/MED only.
4. Confirmation that `needs-amir-review-archive.jsonl` schema includes the new fields (`suggested_action`, `suggested_confidence`, `actual_action`, `resolution_type`, `time_to_resolve_seconds`).
5. Confirmation that `tasks/missing-resolution-rules.json` exists (create as empty array if not).
6. Confirmation that the current pending task (review #0:57:11.876Z for austin-blue-and-green-opal-inlay) has been backfilled with the `suggested_resolution` payload above.
7. Backfill plan for the other 9 pending tasks in the queue (apply rules retroactively, write to disk, surface in dashboard).
8. First weekly accept-rate report scheduled for Sunday 2026-06-07 22:00 Central, written to `/home/openclaw/.openclaw/command-center/work/approvals/weekly-accept-rate-2026-06-07.md`.

Post receipts to Slack `#beta-daily` and write a summary to `/home/openclaw/.openclaw/command-center/work/phase3/suggested-resolution-rollout-2026-05-31.md`.

## Constraints (unchanged)

- $15/day OpenRouter DeepSeek cap, non-bypassable.
- No Claude API calls.
- Brand voice rules per Aydins CLAUDE.md and `brands/aydins/profile.md`.
- All Shopify writes preceded by audit/backup JSON.
- No variant/inventory/price changes without Amir.
- No em dashes anywhere (including in suggested notes BETA writes).
- Hard rule preserved: ad spend changes, email sends, account/theme/domain changes, app installs all still require explicit Amir approval. This patch does NOT change the action set; it only pre-suggests which action to take.
- Amir always retains final say. The "APPROVE SUGGESTION" button is convenience, not consent transfer.
