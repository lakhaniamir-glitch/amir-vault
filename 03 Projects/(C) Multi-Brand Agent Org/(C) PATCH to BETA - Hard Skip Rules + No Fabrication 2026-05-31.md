---
to: BETA
from: Amir
date: 2026-05-31
priority: High
type: Worker queue + BETA Shop guardrails (stop drafting copy for non-ring products and stop fabricating when source content is empty)
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Hard_Skip_Rules_No_Fabrication_2026-05-31.md
supersedes: none (additive guardrails to Phase1 worker + BETA Shop + BETA Check)
---

# PATCH: Hard Skip Rules + No Fabrication

## Why this patch

Tonight a BETA Shop draft landed in `needs-amir-review` for product `8975902179565` (handle `shipping-protection`, type `Shipping Protection`, tags include `NOREVIEW`). The draft proposed:

- Meta title: "Aydins Shipping Protection Ring | Durable Comfort Fit"
- Body bullets about "stainless steel with carbon fiber inlay", "comfort fit interior", engraving
- FAQ section including "What is the Shipping Protection made of?", "Is the Shipping Protection comfort fit?", "Can the Shipping Protection be engraved?", "How do I find my ring size?"

None of this is real. The product is a **shipping insurance upsell** with 5 price-tier variants (`0T50` $9.75, `50T100` $19.75, `100T499` $29.75, `499T749` $49.75, `749TN` $99.75), no SKUs, negative inventory, empty `body_html`, and a single generic image. There is no ring, no material, no size, no engraving, no warranty card. Every concrete claim BETA Shop wrote was hallucinated from thin air because the agent had no source content and proceeded anyway.

Three failures stacked:

1. The product carries an explicit `NOREVIEW` tag. BETA ignored it.
2. The product type is literally `Shipping Protection`. The existing "not a ring" filter only checks the handle for keywords like "pendant", "necklace", "bracelet" etc. and missed it.
3. With `body_html` empty and no specs metafields, BETA Shop fabricated material and feature claims instead of routing to a human.

This patch closes all three gaps. They are hard rules, not warnings.

## Action 1: NOREVIEW tag = unconditional skip (everywhere)

Anywhere BETA picks products to work on, add the first gate before any other logic:

**If `product.tags` contains the case-insensitive token `NOREVIEW`, skip the product. Log it once to `tasks/skipped-noreview.json` (append-only). Never queue, never draft, never push, never re-evaluate.**

Apply this gate in:

- `scripts/zero-traffic-picker` (or whichever picker writes to `tasks/open.json`).
- BETA Shop drafting entry point (before reading the product).
- BETA Check (defense in depth: if a NOREVIEW product somehow reached Check, reject with reason `"NOREVIEW tag present; product is opted out of automated edits"`).
- BETA Insta drafter and BETA Google blog drafter, in case they iterate over the product catalog.
- Any future agent that touches the product catalog.

Reasoning: `NOREVIEW` is a human signal that says "leave this alone". Bundle products, shipping upsells, donation SKUs, test products, and intentionally-curated listings all use it. Respecting the tag is non-negotiable.

## Action 2: Expand the "not a ring" filter to cover product_type

The current filter (per Live_Mode_Verification_Gate_2026-05-26.md section 2) checks the handle and product type for keywords like `dog tags`, `pendants`, `necklaces`, `bracelets`, `earrings`, `cuff links`, `chains`. It does not catch service/digital products that are not jewelry at all.

Add these `product_type` strings (case-insensitive, exact match) to the skip list:

- `Shipping Protection`
- `Insurance`
- `Service`
- `Digital`
- `Upsell`
- `Gift Card`
- `Tip`
- `Donation`
- `Bundle`
- `Subscription`

Also add a structural check: **if `product.variants[].sku` is null for every variant AND `body_html` is empty AND inventory is negative on any variant, skip with reason `"non-physical product (no SKUs, no body, negative inventory)"`.**

This catches non-jewelry products that slip through naming-based filters.

## Action 3: No fabrication on empty source

BETA Shop currently drafts copy even when the source product has no descriptive content. That is how we got "stainless steel with carbon fiber inlay" on a shipping insurance product.

Add a precondition check at the top of BETA Shop drafting:

```
if not has_any_source_content(product):
    route_to_needs_amir(
        task_id=..., handle=...,
        reason="no source content to enrich, cannot draft safely",
        details={
          "body_html_empty": True,
          "metafields_empty": True,
          "variant_titles_descriptive": False,
          "image_alt_descriptive": False
        }
    )
    return
```

`has_any_source_content(product)` returns True if ANY of these is true:

- `product.body_html` is non-empty and contains at least 50 characters of plain text.
- Product has at least one descriptive metafield (`custom.material_primary`, `custom.material_inlay`, `custom.quick_specs`, `custom.keywords`, `custom.custom_faq`).
- At least one variant `title` is descriptive (not just numeric, not just size codes like `8.0`, not just price tiers like `0T50`).
- At least one image `alt` text is descriptive (more than 8 chars and not just the handle).

If none of the above is true, BETA Shop must NOT draft. Route to `tasks/blocked-needs-amir.json` with the reason and details payload above. The human (Amir) reviews and either:
- Provides source material (e.g. pastes the universal-jewelry.com page content), or
- Adds NOREVIEW tag if the product should never be touched, or
- Updates the product_type taxonomy to exclude it from future picks.

Companion rule in BETA Check: **reject any draft whose product has `body_html` empty AND no source metafields**, with reason `"fabrication risk: source material is empty, draft cannot be verified against ground truth"`. This is a backstop in case the precondition is bypassed.

## Action 4: Retroactively handle the in-flight Shipping Protection draft

Specifically for the existing draft in the current `needs-amir-review` queue:

- Task: the Shipping Protection draft (product `8975902179565`, handle `shipping-protection`).
- Pre-fill its `suggested_resolution` block:

```json
{
  "action": "REJECT",
  "confidence": "HIGH",
  "reasoning": "Product is shipping insurance, not a ring. Tags include NOREVIEW. Product_type is Shipping Protection. body_html is empty. All content in the draft is fabricated (material, inlay, comfort fit, engraving, ring size, gift box, warranty card do not apply). Multiple rule violations: VESUVIUS not-a-ring filter, NOREVIEW tag, fabrication on empty source, FAQ sizing question (banned).",
  "suggested_note": "Reject. Product is shipping insurance, not a ring. All copy hallucinated. Tags include NOREVIEW. Do not regenerate.",
  "risk_if_approved_asis": "Customer-facing copy fabricates material, dimensions, features, engraving, gift box, and warranty card that do not exist for a shipping insurance product. Trust damage and potential consumer-protection exposure.",
  "risk_if_rejected": "None. This product should never have been queued.",
  "auto_fixable": false,
  "auto_fix_plan": null
}
```

Confidence is HIGH because every claim is verifiable false against the live Shopify product data.

## Action 5: Scrub the queue for similar mistakes (one-time)

Iterate every product currently in `tasks/open.json`, `tasks/in-progress.json`, and `tasks/needs-amir-review.json`. For each, fetch the live Shopify product and check:

1. Does it have NOREVIEW tag? -> archive the task to `tasks/skipped-noreview.json` and remove from the active queue.
2. Is its product_type in the new skip list? -> same as above, with reason `"non-ring product_type"`.
3. Does it pass `has_any_source_content`? -> if not, REJECT the task with reason `"fabrication risk"`.

Report counts: how many were removed for NOREVIEW, how many for product_type, how many for empty source. Post to Slack `#beta-daily` and write summary to `command-center/work/phase3/queue-scrub-2026-05-31.md`.

## Verification protocol

Report back with:

1. Updated picker code (file path + diff or full new contents) showing the NOREVIEW gate is first.
2. Updated BETA Shop entry point showing the `has_any_source_content` precondition.
3. Updated BETA Check rules (paste new rejection rules) showing NOREVIEW + empty-source backstops.
4. The expanded product_type skip list (paste the list as a constant).
5. Confirmation that `tasks/skipped-noreview.json` exists and the queue scrub ran. Include the counts.
6. Confirmation the Shipping Protection task in `needs-amir-review` has the suggested_resolution payload from Action 4.
7. Dry-run output: feed a known NOREVIEW product through the picker and confirm it is skipped without drafting.
8. Dry-run output: feed a product with empty body_html and no metafields through BETA Shop and confirm it routes to blocked-needs-amir instead of drafting.

Slack `#beta-daily` receipt + summary to `command-center/work/phase3/hard-skip-rules-rollout-2026-05-31.md`.

## Constraints (unchanged)

- $15/day OpenRouter cap.
- No em dashes anywhere.
- Snapshot any modified scripts to `backups/<filename>.bak-YYYY-MM-DDTHHMMSS`.
- When committing to the dashboard repo or any repo connected to Vercel, use git author `lakhaniamir-glitch <lakhaniamir-glitch@users.noreply.github.com>`. Commits authored as `beta@openclaw` (or any unverified email) get blocked at the Vercel build step. Lesson from earlier today.
- Do not relax any existing VESUVIUS rejection rule. These guardrails are additive.
- NOREVIEW is a hard rule: never override, never auto-resume after a delay, never re-attempt without explicit Amir instruction.
