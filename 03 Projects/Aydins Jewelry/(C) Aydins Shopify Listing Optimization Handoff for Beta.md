# Aydins Shopify Listing Optimization Handoff for Beta

> **Handoff date:** 2026-05-12
> **From:** Claudian (vault-side Claude)
> **To:** Beta (OpenClaw orchestrator) → Beta-Shop (Shopify specialist)
> **Purpose:** Transfer complete operating context for Aydins Jewelry Shopify listing optimization so Beta-Shop can continue the work without losing institutional memory.

---

## 0. Read These First (Canonical Sources of Truth)

Beta-Shop must read these in order before touching any listing:

1. **`(C) Shopify Listing Standard — Brief for Beta-Shop.md`** — canonical 15-section spec. All listing work routes through this. No exceptions.
2. **`(C) Aydins Policies — Source of Truth.md`** — verified 2026-05-08. Policy wording is locked. Any deviation breaks the listing.
3. **`(C) master-pdp-template-vanta.md`** — PDP structural template (VANTA example). Use the skeleton, but **rewrite the policy lines per #2 — the template still contains old wording.**
4. **`(C) FINAL-REPORT-2026-04-25.md`** — record of the April 22-25 overnight revamp (398 products). Important: those listings need policy-wording corrections (see Section 6 below).

If those four files conflict, **Policies (#2) wins**, then Standard (#1), then everything else.

---

## 1. The Exact Listing Rewrite Framework

### 1.1 Title Formula

```
{Material} {Style/Feature} {Type} {Width} | {CODENAME} | Aydins
```

Examples:
- `14k Gold Black Carbon Fiber Wedding Ring 8mm | VANTA | Aydins`
- `Tungsten Carbide Brushed Wedding Band 6mm | CREDO | Aydins`

Rules:
- **Material first**, then style/feature, then ring type, then width.
- **CODENAME** is a short, memorable, single-word product name. Treat it as the listing's identity — used in URL handle, opening line, and Why-CODENAME close.
- **Aydins** at the end is canonical (not "Aydin's", not "Aydins Jewelry").

### 1.2 SEO Title

- **Max 70 characters** (Google truncates beyond ~60-65, but 70 is the hard ceiling).
- Same shape as the product title above. Front-load the most-searched terms.
- Include the codename — it builds brand-search lift over time.

### 1.3 Meta Description

- **Max 150 characters** (Google truncates ~155-160; 150 is the safety line).
- Format: `{Material/feature claim}. {Comfort/fit}, {free engraving promise}, {warranty hook per CURRENT policy}.`
- Must not say "lifetime warranty" bare — use the tiered framing (see Section 2.4 below).
- Lead with the search-intent answer, not marketing fluff.

### 1.4 Product Description Structure

Three blocks, in this order:

**A. Opening (3 paragraphs max)**
- Paragraph 1 opens with the codename: `The {CODENAME} is...`
- Answer-first. Tell the buyer what it is, what it's made of, and who it's for — in the first 2 sentences.
- No "Looking for the perfect ring?" intros. No questions. No fluff.

**B. Key Features (bullet block)**
- 5-7 bullets. Each bullet = one tangible spec or buyer-relevant fact.
- Material, width, fit type, finish, engraving option, sizing program (per current policy), warranty (per current policy).

**C. Why {CODENAME} (close)**
- 2-3 sentence emotional close. Reinforces the codename and who the ring is for.
- End with the engraving tagline: *Engrave the inside. Make it his.*

### 1.5 FAQ Block (5-6 questions, JSON-LD'd)

Standard FAQ skeleton — adapt the answers to the specific ring but keep these questions:
1. What's the ring made of? / Is the material durable?
2. How do I get the right size? (route to Lifetime Sizing program — per current policy)
3. Can I engrave it? (yes, free inside engraving; outside is paid add-on)
4. What's the warranty? (use tiered wording — see Section 2.4)
5. What's the return policy? (use tiered wording — see Section 2.5)
6. (Optional) Material-specific care question.

Wrap the FAQ in JSON-LD `FAQPage` schema for rich results.

### 1.6 Keyword Strategy

- Primary keyword in: title, SEO title, meta description, H1 (product name), first paragraph, alt text on hero image, URL handle.
- Secondary keywords (material, width, style) sprinkled in Key Features and FAQ answers — never stuffed.
- URL handle = lowercase, hyphenated, includes codename: `vanta-14k-gold-black-carbon-fiber-wedding-ring-8mm`.

### 1.7 Image / Alt Text Rules

- 9-shot image set per product (per the April overnight standard): hero, angled, side profile, on-hand, scale shot, finish detail, engraving option preview, packaging, comparison/lifestyle.
- Alt text formula: `{CODENAME} - {material} {ring type} {width} - {shot type}`. Example: `VANTA - 14k gold black carbon fiber wedding ring 8mm - on-hand shot`.
- Hero image alt = the SEO title (or close to it).

### 1.8 Trust / Value Messaging Rules

Use only approved pillars (Section 13 of the Standard):
- Free inside engraving
- Lifetime Sizing program (paid — see policy wording)
- Tiered warranty (see policy wording)
- Ships from Irving, Texas workshop
- 4.9★ customer rating (only if currently true)
- Secure checkout

**Do not invent trust badges or claims that aren't in the approved list.**

---

## 2. Aydins-Specific Rules (Hard NEVERs and Policy Wording)

### 2.1 Brand Voice

- Direct, confident, masculine. Skews to men's rings.
- No "luxury for less," no "exquisite craftsmanship," no "elevate your style."
- Specs and substance over marketing adjectives.

### 2.2 White-Label / Supplier Rules (CRITICAL)

- **Never name Thorsten, Universal Jewelry, or any upstream supplier on the storefront.**
- **Never say "handcrafted," "forged," "made by hand," "artisan-made," "hand-finished," or any phrasing that implies Aydins manufactures the ring.**
- Aydins **engraves and ships from Irving, Texas.** That's the truthful claim.
- The April overnight revamp violated this with "handcrafted" appearing in the VANTA template — Beta-Shop must rewrite any instance found.

### 2.3 Engraving Rules

- Tag format: bare-word **`Inside`** or **`Inside & Outside`** — no parens, no "(Inside)". Zepto-verified 2026-05-07.
- Free inside engraving is standard. Outside engraving is a paid add-on.
- Engraved rings **cannot be returned** but **can be exchanged** for a $34.50 fee (per current policy).
- Closing tagline: *Engrave the inside. Make it his.*

### 2.4 Warranty Wording (LOCKED — verified 2026-05-08)

Do **not** write "lifetime warranty" bare. Use this tiered phrasing:

- **First 6 months:** Free warranty coverage.
- **6-12 months:** $34.50 coverage fee.
- **After 12 months:** $54.50 coverage fee.

This is non-negotiable. The April revamp listings used "lifetime warranty" — those need correction.

### 2.5 Returns Wording (LOCKED)

- **$25 restocking fee** on returns.
- **Customer pays inbound shipping.** Aydins pays outbound on the original order.
- **30-day window** — but never write "30-day free returns." Returns are not free.
- **Engraved rings: no returns, but exchange available for $34.50.**

### 2.6 Sizing / Resizing Wording (LOCKED)

- Program name: **Lifetime Sizing** (not "free lifetime resizing").
- **Year 1:** $34.50 per resize.
- **After Year 1:** $54.50 per resize.
- **Original purchaser only** — not transferable.
- For rings $1,000+: **25% surcharge** on resize fee (not a flat $100).

### 2.7 Aydins Protection Plan

- Paid add-on, $9.75-$99.75 depending on ring price.
- Optional upsell. Don't make it sound mandatory.

### 2.8 Pricing Rule

- **3× landed cost minimum.** Landed cost = supplier cost + shipping in + any prep.
- If a competitor is below 3×, hold the price — don't race to the bottom.
- Price Match Guarantee: quiet/soft — mentioned in policy, not headlined on PDP.

### 2.9 5% Store-Credit Bonus

- Conditional. Mention only where the policy specifies it applies (refund-to-store-credit path). Don't promote as a general offer.

### 2.10 Locations — Hard Stops

- ✅ **Irving, Texas workshop** — current and only mention.
- ❌ **Grapevine Mills kiosk** — CLOSED. Never mention.
- ❌ **Flower Mound, TX** in listing copy, descriptions, brand voice, or trust lines. Workshop / marketing location is always **Irving, Texas**. (Exception: Flower Mound IS the real legal mailing address and IS required in email footers + Returns & Exchanges page. Not relevant to product listings. Two-context rule locked 2026-05-15. See [[(C) Aydins Policies — Source of Truth]] rule 7.)

### 2.11 Variants

- Variant structure must mirror universal-jewelry.com's option pattern: Size, Width (if multiple), Engraving Location (Inside / Inside & Outside).
- Inventory per variant tracked separately. Do not collapse sizes.

---

## 3. Listings I (Claudian) Have Touched

> **Honesty check:** I did not directly execute the April 22-25 overnight revamp — that was run by a separate process. What I did was:
> 1. Build the canonical **Shopify Listing Standard** (the brief in section 0).
> 2. Build the **master PDP template** using **VANTA** as the worked example.
> 3. Define the **CREDO** reference listing as the canonical pattern.
> 4. Verify and lock the **policy wording** (2026-05-08).

### 3.1 VANTA (master template example)

- **Title:** `14k Gold Black Carbon Fiber Wedding Ring 8mm | VANTA | Aydins` (61 chars ✓)
- **Meta (as-written in template, NEEDS CORRECTION):** `Handcrafted 14k gold men's wedding ring with authentic black carbon fiber inlay. 8mm, comfort fit, free inside engraving, lifetime warranty.` (144 chars)
- **What's wrong with the template:** Uses **"Handcrafted"** (forbidden per 2.2) and **"lifetime warranty"** (forbidden per 2.4).
- **Beta-Shop action:** Rewrite VANTA meta. Proposed replacement (draft, ≤150c):
  `14k gold men's wedding ring with authentic black carbon fiber inlay. 8mm comfort fit, free inside engraving, tiered warranty from Aydins.` (138 chars)
- **Structural skeleton:** Use as-is. Only the policy-wording lines need rewording.

### 3.2 CREDO (reference listing — Section 14 of the Standard)

- Used as the canonical reference pattern across the spec.
- Beta-Shop should use CREDO as the "if in doubt, match this structure" exemplar.

### 3.3 The April 22-25 Overnight Revamp (398 products)

- Executed by a separate autonomous process Apr 22-25, 2026.
- 284 products got the 9-shot image set; ~600 stale media files were purged.
- 114 products still awaiting images (Gemini quota hit mid-run).
- **These 398 listings used the old policy wording.** Anything that says "lifetime warranty," "free lifetime resizing," "30-day free returns," or "handcrafted" is wrong by current standard and needs Beta-Shop rework.

---

## 4. Performance / Traction

**Honest answer: not captured.**

- No conversion-rate or sales-attribution data has been pulled into the vault yet for any specific listing rewrite.
- `sales-by-product-90d.csv` and `sessions-by-product-90d.csv` exist in the Aydins folder but have not been analyzed against the revamp date.
- **Recommended first analytics task for Beta-Shop:** Pull pre/post conversion rate for the 398 revamped products (Apr 22-25 cutoff) and report top 10 winners + bottom 10 losers. That's the real signal.

Do not fabricate performance numbers. If a stakeholder asks "which listings performed better," the honest answer right now is "we haven't measured yet — pulling the data is the next move."

---

## 5. Files, Docs, Shopify Fields, and Naming Conventions

### 5.1 Vault Files Referenced (read these as needed)

- `03 Projects/Aydins Jewelry/(C) Shopify Listing Standard — Brief for Beta-Shop.md`
- `03 Projects/Aydins Jewelry/(C) Aydins Policies — Source of Truth.md`
- `03 Projects/Aydins Jewelry/(C) master-pdp-template-vanta.md`
- `03 Projects/Aydins Jewelry/02 Build/listing-revamp-overnight-2026-04-22/universal-j-custom/(C) FINAL-REPORT-2026-04-25.md`
- `03 Projects/Aydins Jewelry/04 Launch/(C) credo-listing.md`
- `03 Projects/Aydins Jewelry/(C) christian-rings-batch.md`
- `03 Projects/Aydins Jewelry/(C) BATCH-5-REPORT-AND-NEXT-DECISION.md`
- `03 Projects/Aydins Jewelry/(C) UJ rename preview - 55 products.md`
- `03 Projects/Aydins Jewelry/(C) HALSTEN backup before edits 2026-04-21.json`
- `03 Projects/Aydins Jewelry/(C) Week 1 — Focus SKU Shortlist.md`
- `03 Projects/Aydins Jewelry/sales-by-product-90d.csv`
- `03 Projects/Aydins Jewelry/sessions-by-product-90d.csv`

### 5.2 Shopify Fields to Touch

- **Title** (≤70c if you want it to also serve as SEO title fallback)
- **Description** (HTML body — opening / Key Features / Why CODENAME / FAQ block with JSON-LD)
- **SEO title** (≤70c)
- **SEO meta description** (≤150c)
- **URL handle** (codename + key descriptors, lowercase, hyphens)
- **Product type** (e.g., "Wedding Ring")
- **Tags** (Zepto tags — engraving location bare-word, plus material/style)
- **Variants** (Size, Width, Engraving Location)
- **Images + alt text** (9 shots, alt per Section 1.7)

### 5.3 Metafields (if used)

- `custom.codename` — single-word codename
- `custom.material_primary`, `custom.material_inlay` — for filtering
- `custom.width_mm` — numeric
- `custom.warranty_tier_summary` — pre-baked tiered warranty text (single source so a policy update is one edit)
- `custom.sizing_program_summary` — same idea for the Lifetime Sizing wording

If those metafields don't exist yet, Beta-Shop should propose them before manually retyping policy text into 398 listings. **Single source of truth beats find-and-replace.**

### 5.4 Naming Conventions

- AI-generated files: prefix with **`(C)`**.
- Don't overwrite originals — create a new file with a clear suffix (e.g., `(C) VANTA-pdp-v2-2026-05-12.md`).
- Codenames: short, single-word, memorable, no numbers, no punctuation. CREDO, VANTA, HALSTEN — good. "CARBON-8MM-V2" — bad.

---

## 6. Mistakes, Lessons Learned, and Edge Cases

### 6.1 The Big One — Policy Wording Drift

**What happened:** The April 22-25 overnight revamp shipped 398 listings using old policy wording. The 2026-05-08 Policies update locked new wording. Result: a 398-listing-wide correction backlog.

**Lesson:** Policy text must live in a metafield (or at minimum a single template variable) so a policy change is **one edit**, not 398 manual rewrites.

**Beta-Shop action:** Before doing any new listing, propose the metafield structure in 5.3 and a migration plan for the existing 398.

### 6.2 "Handcrafted" Leak

The VANTA template (and any listing derived from it) contains "Handcrafted." That word is a white-label violation. **Search-and-replace across all Shopify product descriptions and SEO meta:**

| Find | Replace with |
|---|---|
| `Handcrafted` | (delete the word — don't replace with a synonym) |
| `handcrafted` | (delete) |
| `forged` | (delete) |
| `made by hand` | (delete) |
| `artisan-made` | (delete) |
| `hand-finished` | (delete) |

Aydins **engraves and ships**. If a sentence relies on a manufacturing verb, rewrite the sentence around the actual value (material, finish, design).

### 6.3 "Lifetime Warranty" / "Free Lifetime Resizing"

Same drill. Find-and-replace across all listings:

| Find | Replace with |
|---|---|
| `lifetime warranty` | `tiered warranty` (then link/reference policy) |
| `free lifetime resizing` | `Lifetime Sizing program` (then link/reference policy) |
| `30-day free returns` | `30-day returns` (then reference $25 restocking + customer-paid inbound) |

### 6.4 Zepto Engraving Tag Format

Old listings sometimes used `(Inside)` with parens. Zepto-verified 2026-05-07: bare-word `Inside` or `Inside & Outside`. Parens break tag matching. Fix on sight.

### 6.5 Image Set Gaps

114 products from the April revamp are missing their 9-shot image set (Gemini quota hit mid-run). Beta-Shop should:
1. Get a current list of products with <9 images.
2. Prioritize by traffic/revenue (use the 90-day CSVs).
3. Generate missing shots in batches that stay under the per-day Gemini quota.

### 6.6 Don't Fake Conversion Data

If asked "did the rewrite work?" — the honest answer today is "we haven't pulled the data." Pull it before answering. Fabricated traction numbers are worse than admitting the measurement gap.

### 6.7 Don't Bulk-Push Without a Diff Preview

Any change touching 50+ listings should produce a **preview file** first (like the existing `(C) UJ rename preview - 55 products.md`). Eyeball it, get a thumbs-up, **then** push to Shopify. Bulk pushes without preview are the single biggest source of regret in this project.

### 6.8 Pricing Edits Need a Margin Check

Don't change a price (up or down) without checking landed cost. 3× landed is the floor. If a competitor is below 3× — hold the price. Don't race them down.

---

## 7. Suggested First 5 Moves for Beta-Shop

1. **Read** the four canonical docs (Section 0).
2. **Audit** the 398 April-revamp listings for the three forbidden phrasings (handcrafted / lifetime warranty / free lifetime resizing) and the parens engraving tag. Output a count + sample list.
3. **Propose** the policy-wording metafield structure (Section 5.3) so the fix is one source, not 398 edits.
4. **Pull** the 90-day sales/sessions CSVs and identify the top 20 revenue-generating SKUs — those get fixed first.
5. **Pick one SKU** (CREDO is the safest reference), rewrite it end-to-end against the current standard, and ship it as the new canonical example. Then scale.

---

## 8. STATUS

**Handoff: ready.** Beta-Shop has everything needed to continue the work without losing context. Anything missing — ask in-vault, don't invent.

*— Claudian, 2026-05-12*
