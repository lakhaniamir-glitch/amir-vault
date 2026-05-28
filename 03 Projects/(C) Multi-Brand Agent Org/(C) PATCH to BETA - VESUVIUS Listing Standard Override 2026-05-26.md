---
to: BETA
from: Amir
date: 2026-05-26
priority: High
type: Listing standard override (replaces CREDO format)
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/VESUVIUS_Listing_Standard_Override_2026-05-26.md
supersedes: Phase1_Worker_Zero_Traffic_2026-05-26.md (listing-standard portion only)
---

# PATCH: VESUVIUS Listing Standard Override

## Why this patch

After Amir reviewed the 2 BETA Check rejections from 2026-05-27 01:12 and 01:14, he confirmed the canonical listing standard has changed. The CREDO format (5 policy FAQ questions, trust-pillar bullets in Key Features, AY-prefixed SKUs, body warranty/returns/shipping blocks) is **deprecated.**

The new authoritative spec is the **VESUVIUS-approved format**, now in place at:

```
/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md
```

That file was overwritten 2026-05-26 with the new VESUVIUS standard (md5 `11974f6728e0d40be14c683c5e352696`, 200 lines). Re-read it from disk; do not use any cached/in-memory version of the prior CREDO brief.

## Key differences from CREDO (what BETA Shop and BETA Check must change)

| Field | OLD (CREDO, deprecated) | NEW (VESUVIUS, locked) |
|---|---|---|
| Product description body | Included trust-pillar bullets (Free U.S. Shipping, Engraved in Irving Texas, Operating since 2011), warranty/returns/shipping FAQ blocks | **Lean. No policy blocks in body.** Strong opening + supporting + Key Features + Why CODENAME close. |
| Key Features bullets | Material, Pattern/Inlay, Profile, Comfort Fit, Widths, Engraving, Free U.S. Shipping, Engraved in Irving Texas, Operating since 2011 | Product-specific only: Material, Inlay/Feature, Widths, Fit, Profile, Engraving location, Color/finish if relevant, daily wear/care note if product-specific |
| FAQ count | 5 mandatory policy questions | **6 mandatory product/material-specific questions** |
| FAQ content | Engraving included? Exchange/resize? Return policy? Cracks/breaks? How fast does it ship? | What is [CODENAME] made of? Is [material] good for daily wear? What does the [inlay/feature] look like? Can [CODENAME] be engraved? Is it comfort fit? How do I care for a [material] ring with [feature]? |
| FAQ wording requirement | Verbatim policy phrases ("$25 restocking fee", "free in the first 6 months", etc.) | **None of those phrases in product FAQ.** Policy lives in global PDP accordions, not product body. |
| Quick Specs metafields | Not part of CREDO scope | **Required:** `custom.keywords` (labeled format) and `custom.quick_specs` (bullet-separated) |
| SKU format | `AY-CODENAME-{WIDTH}-{SIZE}` (e.g. `AY-CREDO-6MM-9.00`) | `CODENAME-WIDTH-SIZE` (e.g. `VESUVIUS-6-5`) — no `AY-` prefix |
| Material info page metafield | Not specified | **Required:** select correct material page (e.g. `custom.ceramic_ring_information` for ceramic) |
| Category/taxonomy metafields | Not in CREDO scope | **Required:** Color, Ring size, Jewelry material, Age group, Jewelry type, Ring design, Target gender, Ring Size Chart, Gemstone type (if truthful) |
| Engraving body section | Acceptable as standalone if useful | **No duplicate standalone Engraving section** if engraving is already in Key Features/FAQ |

## Actions for BETA

### Action 1: Update BETA Shop scope and prompt

The Phase 1 handoff said BETA Shop is "copy only" (title, description, meta, tags, alt text). **That scope is now expanded** to match the VESUVIUS standard.

BETA Shop in Phase 1 Aydins context now produces drafts for:

1. `title` (per VESUVIUS Section 1, codename pattern)
2. `meta_title` (per VESUVIUS Section 6, ≤70 chars)
3. `meta_description` (per VESUVIUS Section 6, ≤150 chars)
4. `description_html` (per VESUVIUS Sections 1, 2: lean structure, no policy blocks, product-specific Key Features only)
5. `tags` (per VESUVIUS Section 9)
6. `image_alt_text` (per VESUVIUS Section 11)
7. **`custom.keywords` metafield** (per VESUVIUS Section 3, labeled format)
8. **`custom.quick_specs` metafield** (per VESUVIUS Section 3, bullet-separated)
9. **`custom.custom_faq` metafield** (per VESUVIUS Section 4, 6 product-specific questions)
10. **FAQ schema** matching `custom.custom_faq` exactly (per VESUVIUS Section 5)
11. **Material info page metafield** (per VESUVIUS Section 8, e.g. `custom.ceramic_ring_information`)
12. **Category/taxonomy metafields** (per VESUVIUS Section 7)

Still out of scope: variant changes, SKU rewrites, inventory updates, pricing/cost changes, image replacement, collection assignment, publish action.

Update `/home/openclaw/.openclaw/command-center/agents/beta-shop.md` to reflect the expanded scope AND the new "Required JSON output contract" must add these fields:

```
"custom_keywords": "string",
"custom_quick_specs": "string",
"custom_custom_faq": [
  {"question": "string", "answer": "string"}
],
"faq_schema_jsonld": "string",
"material_info_metafield": {"namespace": "custom", "key": "string"},
"taxonomy_metafields": {
  "color": "string",
  "ring_size": "string",
  "jewelry_material": "string",
  "age_group": "string",
  "jewelry_type": "string",
  "ring_design": "string",
  "target_gender": "string",
  "ring_size_chart": "string",
  "gemstone": "string_or_null"
}
```

And update `approval_risk` value to: `"copy_plus_metafields_no_price_no_image_replacement_no_variant_no_publish"`.

### Action 2: Rewrite BETA Check validation rules

The current BETA Check validator rejected drafts for missing CREDO-era policy phrases. **Remove those checks.** Replace with VESUVIUS validation.

**Remove these rejection rules (CREDO-era, now wrong):**
- Require phrase "Free exchange in the first 30 days on unengraved rings"
- Require phrase "$25 restocking fee"
- Require phrase "customer pays return shipping"
- Require phrase "Engraved rings can't be returned"
- Require phrase "free in the first 6 months"
- Require phrase "$34.50 flat from 6-12 months"
- Require phrase "$54.50 flat after"
- Require phrase "Most orders ship in 1-3 business days"
- Require phrase "Irving, Texas"
- Require FAQ questions: engraving / exchange-resize / return-policy / cracks-breaks / how-fast-ships

**Add these VESUVIUS rejection rules:**
- Reject if product description body contains warranty, returns, shipping, sizing, or exchange policy blocks
- Reject if Key Features list includes "Free U.S. Shipping", "Engraved and shipped from", "Operating since 2011", or any other trust-pillar bullet (these belong in global PDP, not product Key Features)
- Reject if `custom.custom_faq` does not contain all 6 product-specific questions
- Reject if any FAQ question references warranty, returns, shipping, sizing, exchange, custom order policy, or general engraving process
- Reject if `custom.keywords` is missing or malformed (must have Material, Inlay/Feature, Widths, Fit, Profile, Engraving lines)
- Reject if `custom.quick_specs` is missing or not bullet-separated
- Reject if FAQ schema (JSON-LD) does not match `custom.custom_faq` exactly
- Reject if SKU format includes `AY-` prefix (must be bare `CODENAME-WIDTH-SIZE`)
- Reject if standalone Engraving section duplicates info already in Key Features or FAQ
- Reject if taxonomy/category metafields are missing or contain unsupported values
- Reject if material info page metafield is missing (when applicable to product type)

**Keep these rejection rules (carry over from CREDO, still valid in VESUVIUS):**
- No em dash characters
- No supplier or third-party brand names (Thorsten, Universal Jewelry, JCK)
- No "handcrafted/handmade/forged/built/cut/made by hand/made in our workshop"
- No bare "lifetime warranty" — use "Aydins Lifetime Warranty. See policy page for terms."
- No "Flower Mound" in listing copy (listings use Irving Texas — but only when truthfully relevant; do not force it into Key Features)
- No invented image scene descriptions
- Title must follow CODENAME pipe descriptor pattern, codename in ALL CAPS
- Meta title ≤70 chars, meta description ≤150 chars
- Engraving tag bare-word `Inside` or `Inside & Outside`
- Variants match universal-jewelry.com source exactly

### Action 3: Handle the 2 rejected drafts

The 2 drafts rejected at 01:12 and 01:14:
- `finger-print-engraved-mens-wedding-band-two-tone-brushed-black-tungsten-ring-8mm-blue-step-edge-comfort-fit`
- `stainless-steel-fingerprint-dog-tag-gold`

The dog-tag handle is not a ring at all. The VESUVIUS standard is for rings. Exclude this from the worker queue going forward by adding a product-type filter: ring products only (filter by Shopify product type or by handle/tag containing "ring", "band", or by category metafield).

Re-queue the tungsten ring (`finger-print-engraved-mens-wedding-band-...`) for a fresh draft under the VESUVIUS standard. Propose a codename for it (current handle is verbose and not codenamed).

### Action 4: Bump agent timeout

Codex GPT-5.5 timed out at 630s during the prior orchestration turn. Update `/home/openclaw/.openclaw/openclaw.json` config: `agents.defaults.timeoutSeconds: 1200` (from 600). Restart gateway.

### Action 5: Run a single test draft (do not push)

After Actions 1-4 are in place, manually invoke BETA Shop on the re-queued tungsten ring. BETA Check reviews. **Do not push to Shopify.** Drop the draft + Check result into Slack `#beta-daily` so Amir can verify the VESUVIUS format is being produced correctly before the worker resumes the daily loop.

## Verification protocol

When complete, report back with:

1. Confirmation `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md` md5 = `11974f6728e0d40be14c683c5e352696` and contents match the VESUVIUS spec.
2. Updated `agents/beta-shop.md` — paste full contents.
3. Updated BETA Check validator code or rules file — paste full contents. Include the new rejection rules and confirmation that CREDO-era policy checks are removed.
4. Updated timeout config snippet.
5. Re-queued task entry in `tasks/open.json` for the tungsten ring.
6. Slack `#beta-daily` post with the test draft and BETA Check result.
7. md5 hashes and timestamps of every modified file.

Hold the worker loop until Amir reviews the test draft and approves resumption. Stay in shadow mode otherwise.

## Constraints (unchanged)

- No publishing without Amir explicit approval.
- No em dashes anywhere.
- $15/day OpenRouter DeepSeek cap.
- No Claude API calls.
- Brand voice rules per Aydins CLAUDE.md and `brands/aydins/profile.md`.
- All Shopify writes preceded by audit/backup JSON.
