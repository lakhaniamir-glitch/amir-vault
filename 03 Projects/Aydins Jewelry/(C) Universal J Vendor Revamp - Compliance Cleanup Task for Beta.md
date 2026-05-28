# (C) Universal J Vendor Revamp - Compliance Cleanup Task for Beta

> **Created:** 2026-05-19
> **From:** Claudian (vault-side)
> **To:** Beta (orchestrator) -> Beta-Shop (Shopify specialist)
> **Why this exists:** Earlier Claude sessions revamped a large batch of Universal J vendor listings using old policy wording and brand-voice rules that are now wrong. Standards locked 2026-05-08. Drift needs a sweep.

---

## 1. The Task in One Sentence

In Shopify, filter products where **vendor = "Universal J"**, audit each listing against the current Aydins Compliance standard, and rewrite anything that fails. Full autonomous overnight push. Safety is the rollback machinery (section 7), not human review.

---

## 2. What "Aydins Compliant" Means Right Now

Canonical, in this order. If they conflict, the higher one wins.

1. [[(C) Aydins Policies - Source of Truth]] (policy wording, locked 2026-05-08)
2. [[(C) Shopify Listing Standard - Brief for Beta-Shop]] (15-section spec)
3. [[(C) Aydins Shopify Listing Optimization Handoff for Beta]] (process + lessons)
4. [[03 Projects/Aydins Jewelry/CLAUDE.md]] (project rules, including no-em-dash rule locked 2026-05-15)

Beta-Shop must read these four before touching a listing.

---

## 3. Scope

- **Vendor filter:** Shopify product `vendor` field equals **"Universal J"** (or any variant: "Universal J ", "universal-j", "Universal Jewelry" if it leaked into vendor).
- **Do NOT change the vendor field itself.** It is internal-only, not shown on storefront. Leave it as "Universal J".
- Estimated count: ~398 from the Apr 22-25 overnight revamp, plus anything earlier under the same vendor. Beta-Shop pulls the live count first.

---

## 4. The Non-Compliance Signatures (what to grep for)

These are the exact strings that mark a listing as non-compliant. Each one is a hit.

### 4.1 Brand-voice violations (white-label leaks)

| Find | Action |
|---|---|
| `Thorsten` | Delete + rewrite sentence |
| `Universal Jewelry` (customer-facing copy) | Delete + rewrite sentence |
| `JCK` | Delete + rewrite sentence |
| `Handcrafted` / `handcrafted` | Delete the word, rewrite around material/finish |
| `forged` | Delete, rewrite |
| `made by hand` / `hand-made` / `handmade` | Delete, rewrite |
| `artisan-made` / `hand-finished` / `hand-cut` / `hand-polished` | Delete, rewrite |
| `built one ring at a time` / `we'll start cutting your ring` | Delete, rewrite |
| `crafted in our workshop` / `we make every ring` | Delete, rewrite |
| `built in our workshop` / `made in our workshop` | Replace with "engraved and shipped from our workshop in Irving, Texas" |

Aydins **engraves and ships**. That is the only truthful manufacturing claim. Approved phrasing: "engraved and shipped from Irving, Texas," "your engraving applied at our workshop," "we set up your engraving the day your order comes in," "engraving wedding bands in Irving, Texas since 2011."

### 4.2 Policy-wording violations (locked 2026-05-08)

| Find | Replace with |
|---|---|
| `lifetime warranty` (bare) | Tiered warranty wording: free first 6 months, $34.50 flat 6-12 months, $54.50 flat after. Covers breakage and material defects ONLY. Excludes wear, intentional damage, loss, theft. |
| `free lifetime resizing` | "Lifetime Sizing program" with $34.50 year one, $54.50 every year after, original purchaser only, not transferable |
| `lifetime fit guaranteed` / `lifetime fit guarantee` | Same as above. Different program from warranty. Do not conflate. |
| `30-day free returns` / `30-day free returns & exchanges` | "30-day returns. $25 restocking, customer pays return shipping. Engraved rings excluded." (Mixes two policies. Exchanges are free in first 30 days on unengraved. Returns are NOT free.) |
| `free returns` | Returns are never free. Rewrite. Exchanges in first 30 days on unengraved rings ARE free. |
| `2-day shipping` (alone, without processing window) / `arrives in 2 days` | "Free FedEx 2Day shipping in the U.S., on top of our 1-3 business day processing time." Aydins DOES offer free 2-business-day FedEx in the U.S. (confirmed by Amir 2026-05-19). The violation is when a listing surfaces the 2-day shipping claim without the processing window, which implies arrival in 2 days from order. Always pair the two. Total order-to-door window is 3-5 business days. |
| `$100 14k gold fee` / `$100 gold surcharge` | 25% surcharge on items over $1,000. Not a flat $100. Most inventory is under $1,000 so omit from default PDP copy. |
| `Price Match Guarantee` in PDP copy or ad headlines | Remove from PDP. Lives on its own soft policy page only. Never headlined. |
| `Lowest price guaranteed` / `We'll beat any competitor` | Remove. Aydins does not promise specific match terms. |
| `5% bonus on every order` / `5% rewards on returns` | Conditional, refund-to-store-credit only, one-time. Remove from PDP. Belongs on returns policy page only. |
| `Built-in protection` / `All rings come with shipping protection` | Aydins Protection Plan is a PAID add-on, not included. Reframe as optional checkout add-on. |
| `We replace lost packages free` / `Theft covered` (in default copy) | Aydins is NOT responsible for packages lost or damaged in transit by default. Only covered if customer bought the Protection Plan AND has FedEx proof of delivery. |
| `Hassle-free returns` / `No-questions-asked returns` | Returns have a $25 restocking fee and customer pays inbound shipping. Not hassle-free. |
| `30-day satisfaction guarantee` | Remove. Use the actual return wording. |

### 4.2.1 Exchange / Sizing / Warranty fee tables (use the canonical wording, do not paraphrase)

The three programs are distinct. Listings frequently conflate them. Each has its own fee table:

**Exchanges + Lifetime Sizing (single program):**

| Window | Unengraved | Engraved |
|---|---|---|
| 0-30 days | Free | $34.50 surcharge |
| 30-365 days | $34.50 flat | $34.50 flat |
| 365+ days | $54.50 flat | $54.50 flat |

Original purchaser only. Not transferable. Add 25% if item >$1,000. Re-engraving on the replacement is always free.

**Aydins Lifetime Warranty (automatic, every customer):**

| Window | Cost |
|---|---|
| 0-6 months | Free |
| 6-12 months | $34.50 flat |
| 12+ months | $54.50 flat |

Covers breakage and material defects. Excludes normal wear, intentional damage, shipping loss/theft.

**Aydins Protection Plan (paid add-on at checkout, $9.75 to $99.75 by cart total):**

Covers shipping loss, in-transit damage, and theft (with FedEx proof of delivery) for 6 months. Adds one free engraved-ring sizing within 30 days. **Not automatic. Mention only as optional checkout add-on.**

### 4.2.2 Shipping split (critical, frequently mis-stated)

- Customer pays INBOUND shipping (their ring -> Aydins workshop)
- Aydins pays OUTBOUND shipping (replacement -> customer)
- Never write "free returns" or "we cover return shipping" (only half true)
- Tracking included on every shipment. Don't promise lost-package replacement in default copy.

### 4.3 Location violations

| Find | Action |
|---|---|
| `Grapevine Mills` (any context, listings) | Delete. Kiosk is CLOSED. Never mention. |
| `Flower Mound` in listing copy / brand voice | Replace with "Irving, Texas". (Flower Mound is only correct in email footers and the Returns & Exchanges page legal address block. Not in listings.) |

### 4.4 Engraving tag violations

| Find | Replace with |
|---|---|
| Tag `(Inside)` (with parens) | `Inside` (bare word) |
| Tag `(Inside & Outside)` | `Inside & Outside` (bare word) |
| Tag `(Inside and Outside)` | `Inside & Outside` |

Zepto reads bare-word tags. Parens break the personalizer UI. Verified 2026-05-07.

### 4.5 Em dash violations (locked 2026-05-15)

| Find | Replace with |
|---|---|
| `—` (em dash) in any customer-facing copy | Period, comma, colon, semicolon, or parens depending on context |

Em dashes tolerated only in filename references where renaming would break wikilinks. Not in PDP copy, SEO fields, alt text, tags, or any listing field.

### 4.6 Structural violations

A listing is non-compliant if it is missing any of these:
- Title in the current format (see Listing Standard section 1)
- SEO title <= 70 chars
- Meta description <= 150 chars
- Opening + Key Features bullets + Why CODENAME close + 5-Q FAQ block
- Image alt text on every image (formula per Listing Standard section 7)
- Engraving tag set correctly (`Inside` or `Inside & Outside`, no parens)
- Cost-per-item on every variant
- Variants matching the universal-jewelry.com source page widths and sizes exactly

---

## 5. Prioritization (do them in this order)

1. **Top 20 by revenue (last 90 days).** Pull from `sales-by-product-90d.csv`. These earn the most, so compliance bugs cost the most. Fix first.
2. **Top 20 by sessions (last 90 days).** Pull from `sessions-by-product-90d.csv`. High-traffic listings with policy fabrications are litigation/refund risk.
3. **The remaining Universal J vendor pool**, batched by 25-50 at a time.

Do not fix in random order. Revenue first.

---

## 6. Per-Listing Workflow

For each listing:

1. **Snapshot current state** to JSON per section 7.1. No snapshot, no write.
2. **Run the non-compliance grep** against all six categories in section 4.
3. **Read the universal-jewelry.com source page** for that product. Confirm widths, sizes, and engraving rule ("Engravable In Only" -> `Inside` tag; "Inside and Outside" -> `Inside & Outside` tag; any outside inlay -> `Inside` only).
4. **Rewrite** to current standard using the [[(C) Shopify Listing Standard - Brief for Beta-Shop]] section 1-7 formulas. CREDO is the reference exemplar. FAQ + trust lines render from metafields (section 8); body becomes opening + Key Features + Why CODENAME close.
5. **Pricing math check.** Confirm retail >= 3x landed cost. If price is below 3x landed, flag it and skip the price field. Do NOT change the price.
6. **Push to Shopify.** Append the write to `write-log.jsonl`. Move to the next listing.

---

## 7. Execution Mode - Full Autonomous Push (rollback-protected)

**Decision 2026-05-19, Amir (late-night green-light):** Beta runs solo. No canary, no per-batch approval. Maximize the number of listings rewritten before Shopify rate limits cap the night. Safety is the rollback machinery, not human review.

### 7.1 Snapshot before write (non-negotiable, every listing, every time)

Before ANY field is changed on a Shopify product, Beta-Shop dumps full current state to JSON. **No snapshot, no write.** Snapshot must include:

- `id`, `handle`, `vendor`, `productType`, `status`, `title`
- `descriptionHtml` (full body, raw)
- `seo.title`, `seo.description`
- Full `tags` array
- All `variants` (id, title, sku, price, compareAtPrice, costPerItem, inventoryQuantity, inventoryPolicy, weight, weightUnit, option1/2/3 values, barcode)
- All `media` (image src URL, alt text, position)
- All existing `metafields` (namespace, key, type, value)
- All `collections` membership

File path: `02 Build/listing-revamp-overnight-2026-04-22/universal-j-custom/compliance-cleanup/snapshots/{handle}-{ISO-timestamp}.json`

Also write a flat append-only log: `compliance-cleanup/write-log.jsonl` with one line per write action: `{timestamp, handle, productId, action, fieldsChanged, snapshotPath, beforeHash, afterHash, success, error}`.

### 7.2 Rollback procedure (must be ready before any write)

Beta-Shop ships a `rollback.mjs` script alongside the work, in `compliance-cleanup/`. The script must:

- Accept a handle (or `--all`, or `--since {timestamp}`, or `--from-log {path}`)
- Read the corresponding snapshot JSON
- Restore EVERY snapshotted field on the live Shopify product via GraphQL `productUpdate` + `productVariantsBulkUpdate` + media + metafield mutations
- Verify post-restore by re-fetching and diffing against the snapshot
- Log every restore action to `compliance-cleanup/rollback-log.jsonl`

**Test the rollback script on 1 throwaway product end-to-end BEFORE any production write.** If rollback doesn't work, the safety net doesn't exist, and the task is paused. This test costs 5 minutes. It is not optional.

### 7.3 Rate-limit awareness (run hot but don't trip)

- Use GraphQL Admin API, not REST. Higher throughput per request.
- Throttle by cost-tracking the `extensions.cost.throttleStatus.currentlyAvailable` field. Back off when below 200 points.
- For bulk reads (the initial vendor pull), use `bulkOperationRunQuery`. Async, no rate cost.
- For writes, batch in chunks of ~20 mutations per HTTP request where possible (parallel sub-mutations within a single operation).
- If `THROTTLED` is returned, exponential backoff starting at 2s, max 60s.
- Goal: maximize throughput without getting the app temporarily banned. Speed comes from efficient queries, not from hammering.

### 7.4 Daily progress note (morning audit only, no approval needed)

Beta-Shop drops a one-page status file each day work happens:
- File: `compliance-cleanup/(C) progress-YYYY-MM-DD.md`
- Content: count touched today, cumulative count, current position in priority list, flagged products (see 7.5), any decisions deviating from this brief, link to current snapshot and write-log

Amir reads this in the morning. No reply needed unless flags require a decision.

### 7.5 Hard stops (these stay - Beta flags, does not guess)

Even with full autonomy, Beta-Shop pauses and logs (not blocks) on:

- Any price change up or down. Pricing math needs Amir. Default: leave price untouched in this pass.
- Any listing where the universal-jewelry.com source page is gone or changed substantively.
- Any product where variant widths/sizes on Shopify do not match the source page. Could be intentional past customization, could be drift. Either way, flag.
- Any product where the engraving rule is genuinely ambiguous on the source page.
- Anything not explicitly covered by sections 1-6 of this brief or the canonical docs in section 2.

Flagged products are written to `compliance-cleanup/flagged.jsonl` with reason. They get skipped in this pass, picked up after Amir reviews the flag list.

### 7.6 Stopping conditions (when to call it a night)

Beta-Shop stops the autonomous run when ANY of:
- Shopify returns sustained `THROTTLED` even with max backoff (rate-limit ceiling hit)
- Shopify returns auth errors (token expired or app limit)
- >5 consecutive write failures with the same error class (something systematic is broken)
- The flagged.jsonl grows past 30 entries in a single batch (pattern Beta-Shop is hitting may need clarification)
- All Universal J vendor products are processed

In any stop case, write a final summary file: `compliance-cleanup/(C) final-summary-YYYY-MM-DD.md` with counts, errors, flagged list, and exact rollback instructions for anything written.

---

## 8. Policy Metafields (approved 2026-05-19, build before listings)

**Decision 2026-05-19, Amir:** Build the metafield structure first, then reference it from every listing. Policy text lives in one place. Future policy moves become one edit instead of 398.

### 8.1 Required metafields (build these in Shopify Admin first)

| Namespace.key | Type | Content |
|---|---|---|
| `custom.warranty_tier_summary` | multi_line_text | Aydins Lifetime Warranty: free first 6 months, $34.50 flat 6-12 months, $54.50 flat after. Covers breakage and material defects. Excludes normal wear, intentional damage, shipping loss, theft. |
| `custom.sizing_program_summary` | multi_line_text | Lifetime Sizing for the original purchaser: $34.50 in year one, $54.50 every year after. Not transferable. Re-engraving on the replacement is always free. |
| `custom.exchange_summary` | multi_line_text | Free exchange in the first 30 days on unengraved rings. Engraved rings: $34.50 surcharge. After 30 days, the Lifetime Sizing program applies. Customer pays inbound shipping. Aydins pays outbound. |
| `custom.returns_summary` | multi_line_text | 30-day returns from delivery. $25 restocking fee. Customer pays return shipping. Engraved rings cannot be returned but can be exchanged for $34.50. |
| `custom.engraving_summary` | multi_line_text | Free laser engraving on every Aydins ring: text, symbols, handwriting, or fingerprint. Engraving is set up the day your order comes in. |
| `custom.shipping_summary` | multi_line_text | Free FedEx 2Day shipping on every U.S. order. Free international shipping to Canada, UK, Germany, and Australia on all wedding bands. We ship worldwide. Most orders ship in 1-3 business days from our workshop in Irving, Texas. Tracking included. U.S. total: 3 to 5 business days order to door. Free-international total: approximately 2 to 8 business days. |
| `custom.about_aydins` | multi_line_text | Engraving wedding bands in Irving, Texas since 2011. |
| `custom.codename` | single_line_text | The single-word codename for this product (e.g., CREDO, VANTA, FLETCHER). |
| `custom.material_primary` | single_line_text | Primary metal (Tungsten, Titanium, Ceramic, Damascus, Cobalt, Gold Plated Tungsten, 14k Gold). |
| `custom.material_inlay` | single_line_text | Inlay material if any (Wood, Opal, Meteorite, Carbon Fiber, Dinosaur Bone, etc.). Blank if none. |
| `custom.width_mm` | number_decimal | Numeric width in mm. For multi-width products, leave blank and rely on variant options. |

### 8.2 Theme integration (one-time work, then it scales)

Update the Shopify product description template (theme code) to render these metafields in the standard places:
- FAQ block: each Q answer pulls from the matching metafield
- Trust line block (Key Features section): pulls from `engraving_summary`, `shipping_summary`, `about_aydins`
- Returns / warranty FAQ: pulls from `warranty_tier_summary`, `returns_summary`, `sizing_program_summary`, `exchange_summary`

Beta-Shop confirms the theme block structure before populating metafields on listings. If the current theme template doesn't support metafield references, Beta-Shop builds that first.

### 8.3 Migration order

1. Create the metafield definitions in Shopify Admin
2. Update the theme template to reference them
3. Verify rendering on one test product before populating broadly
4. Populate metafields on every Universal J vendor product as part of the per-listing rewrite

**Critical:** Once metafields drive the policy text, the product description body itself stops repeating policy fee numbers. Body copy becomes: opening narrative + Key Features bullets + Why CODENAME close. The FAQ + trust lines render from metafields. That is the single-source-of-truth payoff.

---

## 9. Done Criteria (per listing)

A listing is "compliant and shipped" only when every box is checked:

- [ ] Snapshot written before any field change (section 7.1)
- [ ] Zero hits on the 4.1-4.6 grep
- [ ] Title, SEO title, meta description in current format and within character limits
- [ ] Opening + Key Features + Why CODENAME + 5-Q FAQ all present (FAQ pulls from metafields)
- [ ] Policy metafields (section 8.1) populated
- [ ] Engraving tag is bare-word (no parens), matches source page rule
- [ ] All variant widths and sizes match the universal-jewelry.com source page exactly (or product flagged if mismatch)
- [ ] Cost-per-item set on every variant (if available; flag if missing)
- [ ] Price NOT changed (flagged if below 3x landed cost)
- [ ] Image alt text on every image, using the formula
- [ ] Collection(s) assigned
- [ ] Zepto engraving preview renders correctly
- [ ] Write logged to `write-log.jsonl`

---

## 10. Hard Stops

- Do NOT change the vendor field. Leave "Universal J" as-is.
- Do NOT write to a product without writing a snapshot first.
- Do NOT change prices. Flag and skip the price field if it is below 3x landed cost.
- Do NOT fabricate performance data. If asked "did the rewrite lift conversion," the answer is "we haven't pulled the post-cutoff data yet" until the data is actually pulled.
- Do NOT touch products outside the Universal J vendor filter in this task. Anything else is a separate task.
- Do NOT run any production write until `rollback.mjs` has been verified on a throwaway product (section 7.2).

---

## 11. Execution Sequence for Beta-Shop (overnight run, autonomous)

1. **Read** the four canonical docs in section 2. Policies wins on any conflict.
2. **Build rollback machinery FIRST.** Write `compliance-cleanup/rollback.mjs` per section 7.2. Test it on one throwaway product (snapshot, mutate, restore, verify). If rollback fails, stop. No rollback = no run.
3. **Pull** all Shopify products where vendor = "Universal J" via bulk GraphQL operation. Dump full snapshots (section 7.1 fields) to `compliance-cleanup/snapshots/`.
4. **Grep** that pull against all six categories (4.1-4.6) plus the table conflations in 4.2.1. Save report as `(C) UJ compliance grep report - YYYY-MM-DD.md`.
5. **Build metafields** per section 8. Create definitions, update theme template to render them. Verify rendering on one test product before populating broadly.
6. **Run autonomous.** Order: top revenue first (`sales-by-product-90d.csv`), then top sessions (`sessions-by-product-90d.csv`), then the rest. Snapshot before every write. Append to write-log.jsonl after every write. Flag-don't-block on section 7.5 hard stops.
7. **At any stop condition** (section 7.6), write the final summary file with full restore instructions.

---

## 12. Source Page Verification Per Product (required, do not skip)

For every product, before rewriting:

1. Open the universal-jewelry.com source page for that handle (most are linked in the original revamp JSONs in `02 Build/listing-revamp-overnight-2026-04-22/universal-j-custom/products/`).
2. Confirm widths offered (do not extend or shrink the range).
3. Confirm size range per width (some rings have different size ranges per width).
4. Confirm engraving rule: "Engravable In Only" -> `Inside` tag; "Inside and Outside" -> `Inside & Outside` tag.
5. Confirm any ring with outside inlay -> force `Inside` only.

If the source page is gone or changed, flag the product. Do not guess specs.

---

## 13. Approved Trust Pillars (use only these in PDP copy)

Pulled from [[(C) Aydins Policies - Source of Truth]]. Do not invent new pillars.

1. Free engraving on every order
2. Free FedEx 2Day shipping in the U.S. (after 1-3 business day processing, total 3-5 business days order to door). Free international shipping to Canada, UK, Germany, and Australia on all wedding bands. We ship worldwide.
3. Engraved and shipped from our workshop in Irving, Texas
4. 30-day returns ($25 restocking, customer pays inbound shipping, engraved excluded)
5. Free exchanges within 30 days on unengraved rings ($34.50 on engraved)
6. Lifetime Sizing program for the original purchaser ($34.50 year one, $54.50 every year after)
7. Aydins Lifetime Warranty (free first 6 months, $34.50 flat 6-12 months, $54.50 flat after). Breakage and material defects only.
8. 3-5 business day refund / replacement processing once the ring arrives
9. Operating since 2011
10. Engraved exchanges accepted ($34.50 surcharge) (most jewelers refuse engraved-ring exchanges)

Do NOT use the Protection Plan or the 5% store-credit bonus as default trust pillars. They are conditional / paid add-ons. Mention only in their proper contexts (checkout for Protection Plan; refund processing for store-credit bonus).

---

## 14. Status

**Task: green-lit, FULL autonomous overnight run approved 2026-05-19.**

- Metafield route: APPROVED. Build first.
- Per-batch approval gate: REMOVED.
- Canary gate: REMOVED. Safety is rollback machinery, not review.
- Beta-Shop has full push authority once `rollback.mjs` passes the throwaway-product test.

Goal: maximize listings rewritten before Shopify rate-limits the run.

Amir reads the progress note in the morning. Rollback any regressions found.

Next unblock: Beta-Shop builds + tests `rollback.mjs`, then starts the pull.

*Created by Claudian, 2026-05-19. Update this file as scope or rules change. Beta-Shop should always work from the current version.*
