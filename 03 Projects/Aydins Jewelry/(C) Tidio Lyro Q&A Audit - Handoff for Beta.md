# Tidio Lyro Q&A Audit. Handoff for Beta

> **Handoff date:** 2026-05-18
> **From:** Claudian (vault-side Claude)
> **To:** Beta (OpenClaw orchestrator) → Beta-Shop (Shopify / brand-content specialist)
> **Purpose:** Audit 245 stale Lyro Q&As (2 years old, last touched Dec 2024) against current Aydins policy, voice, and brand rules. Produce a clean KEEP / DELETE / REWRITE decision per Q&A so we can purge bad answers from the AI chatbot before it goes live to customers.

---

## 0. Read These First (Canonical Sources of Truth)

Beta-Shop must read these in order before judging any Q&A:

1. **`(C) Aydins Policies. Source of Truth.md`** (verified 2026-05-08). Policy wording is locked. This is the single most important file for the audit. Every Q&A answer touching returns, warranty, resizing, exchanges, shipping, or store credit gets graded against this file.
2. **`CLAUDE.md`** (project root: `03 Projects/Aydins Jewelry/CLAUDE.md`). Voice rules, white-label rule, banned phrase list, em dash rule (locked 2026-05-15), engraving conventions.
3. **`(C) Shopify Listing Standard. Brief for Beta-Shop.md`** (voice section + trust pillars). Same voice applies to chatbot answers.
4. **`(C) Tidio Chatbot Revamp. Build Guide.md`** (`03 Projects/Aydins Jewelry/`). Context for where these Q&As will live (Lyro AI agent, capped at 50/50 on free tier, $62.50/mo upgrade pending audit outcome).
5. **`(C) Tidio Lyro Q&A. Export Wave 1.md`** (`03 Projects/Aydins Jewelry/`). The captured Q&A list (currently 100 of 245). The remaining 145 + all answer bodies are pending capture (see Section 7).

If those files conflict, **Policies (#1) wins**, then CLAUDE.md (#2), then everything else.

---

## 1. Context (Why This Audit Exists)

- Aydins has had Tidio installed for 2+ years. Lyro AI's knowledge base accumulated **245 auto-captured Q&As** (mostly from `Source = Inbox`, meaning Lyro generated them from past live-chat conversations).
- These Q&As were never curated. They reflect whatever was said in chat 2 years ago. Likely contaminated with:
  - **Old policy claims** that are no longer true (lifetime warranty, free 30-day returns, free lifetime resizing, free shipping thresholds, old discount codes).
  - **Third-party brand mentions** (Thorsten, Universal Jewelry, JCK).
  - **"Handcrafted" / "forged" / "made by hand"** language (white-label violation).
  - **Old store location** (Grapevine Mills kiosk, closed) instead of current Irving, Texas workshop.
  - **Expired promo codes** (Black Friday 2024, 25% coupon thresholds, etc.).
  - **Old shipping carriers, payment methods, or stocking statuses** that have since changed.
- Lyro's plan is capped at **50/50 active Q&As** on the current tier. Upgrading to the **$62.50/mo plan** (which raises the cap) is **blocked** until this audit is complete. Reason: paying more money to scale a polluted knowledge base just makes the brand-damage problem bigger faster.
- Goal of this audit: produce a clean shortlist of **≤50 KEEP/REWRITE Q&As** that pass current policy, voice, and brand rules. Everything else gets DELETE.

---

## 2. The Audit Criteria (Hard NEVERs and Pass/Fail Tests)

Each Q&A gets graded against this checklist. **One NEVER violation = automatic DELETE or REWRITE, no exceptions.**

### 2.1 Hard NEVER Phrases (LOCKED, verified 2026-05-08)

Answer fails if it contains any of these:

| Banned phrase | Why | Correct framing |
|---|---|---|
| `lifetime warranty` | Fabrication. Real policy is tiered. | "Tiered warranty: free first 6 months, $34.50 fee 6-12 months, $54.50 after 12 months." |
| `free lifetime resizing` | Fabrication. Real program is paid. | "Lifetime Sizing program: $34.50 year 1, $54.50 after year 1, original purchaser only, 25% surcharge on rings $1,000+." |
| `30-day free returns` | Fabrication. Returns have fees. | "30-day return window. $25 restocking fee. Customer pays inbound shipping. Engraved rings can't be returned but can be exchanged for $34.50." |
| `free returns` | Same as above. | Same. |
| `handcrafted` / `forged` / `made by hand` / `artisan-made` / `hand-finished` | White-label violation. Aydins doesn't manufacture, Aydins engraves and ships from Irving, Texas. | Rewrite the sentence around the actual value (material, design, finish). Delete the manufacturing verb entirely. |
| `Thorsten`, `Universal Jewelry`, `universal-jewelry`, `JCK`, any upstream supplier name | White-label violation. Hard never on the storefront and on Lyro. | Use "Aydins" or describe the ring by material/style. |
| `Grapevine Mills`, `Grapevine Mills kiosk` | Location closed. Outdated. | "Irving, Texas workshop." (Flower Mound is the legal mailing address but never appears in customer-facing chatbot copy.) |
| Any expired promo code (`BLACKFRIDAY2024`, specific dollar thresholds tied to old offers) | Stale. Will confuse customers and trigger support tickets. | DELETE the Q&A entirely. Don't try to rewrite a promo Q&A. Promos belong in active marketing flows, not in a permanent AI knowledge base. |
| `em dash` character (`—`) | Locked rule 2026-05-15. Banned in all Aydins content. | Use periods, commas, colons, semicolons, or parens. |

### 2.2 Voice Check

Answer fails if it sounds like generic AI fluff or off-brand. Per CLAUDE.md voice:

- ✅ Direct, confident, masculine, conversion-focused.
- ✅ Short sentences. Specs and substance over adjectives.
- ❌ "Looking for the perfect ring?" / "We offer exquisite craftsmanship" / "elevate your style" / "luxury for less" / "We hope this helps!"
- ❌ Excessive emoji, excessive exclamation marks, customer-service-bot tone ("I'd be happy to help!").

### 2.3 Policy Accuracy Check

Answer fails if it contradicts current policy on:

- Returns / exchanges / restocking fee
- Warranty tiers and fees
- Lifetime Sizing program (fees, eligibility, $1,000+ surcharge)
- Aydins Protection Plan (paid add-on, $9.75-$99.75)
- Shipping (carrier, free shipping threshold, who pays inbound on returns)
- Engraving (free inside, paid outside, engraved rings cannot be returned but can be exchanged for $34.50)
- 5% store-credit bonus (conditional, refund-to-store-credit path only)
- Pricing (3× landed cost minimum, Price Match Guarantee is quiet/soft)
- Location (Irving, Texas workshop is the only customer-facing location)

If an answer says anything about these topics, verify it against `(C) Aydins Policies. Source of Truth.md`. If it doesn't match exactly, REWRITE or DELETE.

### 2.4 Currency / Freshness Check

Answer fails if it references:

- Specific products that no longer exist on the store.
- Stock or availability claims (Lyro can't know real-time stock, never let it claim it).
- Specific prices in dollars (prices change, will go stale, customer complaints follow).
- Specific dated promos or seasonal offers.
- Old payment methods that may have changed (PayPal availability claims, etc.).

**Rule of thumb:** if the answer would become wrong the moment a price, product, or promo changes, it doesn't belong in a permanent knowledge base. DELETE.

### 2.5 Scope Check (Is Lyro Even the Right Place for This?)

Some Q&As should not be in Lyro at all because the answer is dynamic, account-specific, or risky. Examples:

- "Where is my order?" → Should route to a real order-status flow, not a static AI answer. DELETE from Lyro.
- "Can I get a discount?" → Discount-hunting questions train Lyro to give discounts. DELETE all of them.
- "What is the Black Friday code?" → DELETE. Promos are not knowledge base material.
- Anything that ends with the customer giving an email, address, or order number → DELETE. Lyro is not a CRM.

---

## 3. Output Format (How Beta Delivers Audit Results)

Beta-Shop produces **one master decision file** per audit batch:

**File path:** `03 Projects/Aydins Jewelry/(C) Tidio Lyro Q&A Audit. Decisions Batch [N].md`

**Format:** Markdown table, one row per Q&A.

| # | Question (short) | Decision | Reason (one line) | Rewritten Answer (if REWRITE) | Topic Tag |
|---|---|---|---|---|---|
| 1 | LEGEND ring tarnish / turn finger green? | KEEP | Material claim, evergreen, voice clean. | (n/a) | product-quality |
| 5 | Discount if purchase under $80? | DELETE | Discount hunting. Trains Lyro to give discounts. | (n/a) | discount |
| 8 | Black Friday discount code? | DELETE | Expired promo. Not knowledge-base material. | (n/a) | promo |
| 11 | Replacement for broken product? | REWRITE | Old answer likely used "lifetime warranty." Must use tiered warranty wording. | (full rewritten answer per current policy) | warranty |
| 13 | Where is the store located? | REWRITE | Old answer likely says Grapevine Mills (closed). Update to Irving, Texas workshop. | "Our workshop is in Irving, Texas. We engrave and ship from there. We don't have a retail storefront, but you can reach us anytime via this chat or email." | location |

**Decisions allowed:** `KEEP`, `DELETE`, `REWRITE`.

**Topic tags** (free-form but suggested): `warranty`, `returns`, `resizing`, `sizing`, `engraving`, `shipping`, `payment`, `location`, `promo`, `discount`, `product-quality`, `product-info`, `policy-misc`, `scope-out`, `voice-only`.

### 3.1 Re-import Format (After Decisions Are Final)

Once Amir approves the decision batch, Beta-Shop generates a **CSV ready for Tidio Lyro re-import** with these columns:

```
question,answer,language,enabled
```

- One row per KEEP and per REWRITE.
- Cap the total at **50 rows** (the Lyro free-tier limit) unless Amir has greenlit the $62.50/mo upgrade.
- Prioritize KEEPs and REWRITEs by **inferred volume** (Q&As with the most generic / most-asked topics first: returns, sizing, engraving, shipping, warranty, payment).
- Output path: `03 Projects/Aydins Jewelry/(C) Tidio Lyro Q&A. Re-import Wave 1.csv`.

Amir will manually delete all 245 stale Q&As in Tidio, then re-import the clean CSV.

---

## 4. The Workflow (Step by Step)

1. **Read the four canonical docs** in Section 0.
2. **Open `(C) Tidio Lyro Q&A. Export Wave 1.md`**. That's your input list (100 of 245 captured so far).
3. **For each Q&A, judge against Section 2 checklist.** Grade KEEP / DELETE / REWRITE.
4. **For REWRITEs, write the new answer in the voice and against current policy.** Keep it short (2-4 sentences max). Mobile-first. No em dashes. No banned phrases.
5. **Output the decisions table** at `(C) Tidio Lyro Q&A Audit. Decisions Batch 1.md`.
6. **Surface anything ambiguous to Amir before deciding.** Examples: "this Q&A mentions a product that may or may not still exist, please confirm" or "this answer references a 5% store-credit bonus, can you confirm current policy still applies in this case?"
7. **Wait for Amir's sign-off on Batch 1** before generating the re-import CSV. Don't push to Tidio. Amir does the re-import himself.
8. **After Batch 1 is approved**, repeat the process for Waves 2 and 3 (the remaining 145 Q&As, once captured per Section 7).

---

## 5. What You're NOT Doing

- ❌ Not touching Tidio directly. No API calls, no admin panel changes. Output stays in the vault as markdown + CSV.
- ❌ Not making policy decisions. If an answer requires a new policy interpretation, ask Amir, don't invent.
- ❌ Not adding new Q&As. Audit only. Net-new Q&As are a separate task that comes after the audit.
- ❌ Not capturing answer text yourself. The Wave 1 export only has questions and metadata. Capturing the existing answers is on Amir (see Section 7). If you're judging blind on a Q&A where the answer is critical (returns, warranty, etc.), default to REWRITE so we produce a fresh, policy-correct answer instead of trying to grade what we can't see.

---

## 6. Hot-Spot Q&As (Audit These First)

From the Wave 1 export, these are the highest-risk Q&As. Audit them first because they are the most likely to be wrong AND the most damaging to the brand if Lyro serves the old answer to a customer:

**Returns / Warranty / Resizing (almost certainly contain banned phrases):**
- #11 How can I get a replacement for my broken product?
- #12 What is the company's policy for returning or exchanging a product?
- #22 What is the cost for an exchange if it's been more than 30 days?
- #36 Do I have to pay for shipping to return the ring for exchange?

**Location (almost certainly says Grapevine Mills):**
- #13 Where is the store located?

**Discount / Promo (almost all should be DELETE):**
- #5 Can I get a discount if my purchase amount is below $80?
- #6 What is the minimum purchase amount required to use the 25% discount coupon?
- #8 What is the Black Friday discount code?
- #15 Do you offer any bulk discounts if I order a larger quantity?

**Order Status (scope-out, should not be in Lyro):**
- #26 How can I ensure that both my spouse and I are kept informed about my order?

**Payment Method (probably stale):**
- #14 Why is PayPal not available as a payment option on the checkout page?

**Material / Quality (likely OK, but check voice):**
- #1, #2, #3 (LEGEND ring questions)
- #17 Are your products hypoallergenic?
- #29, #30 (ring material questions)

Knock these out first. They're the ones that will cause the most harm if Lyro answers wrong on day 1.

---

## 7. Pending Capture (What's Not in the Wave 1 Export Yet)

The Wave 1 export has **100 of 245 questions** with metadata only. Still needed before the audit can be considered complete:

- **Pages 2 and 3 of the Q&A list** (145 more questions). Blocked at capture time by a Chrome extension conflict. Three options listed in the Wave 1 export file.
- **Answer text for every Q&A** (all 245). Not in Wave 1. Same blocking reason. Options listed in Wave 1 export.

**Amir's next step before the full audit can run:**

1. Pick Option A, B, or C from the Wave 1 export file's "Next Steps" section to capture the remaining 145 questions + all 245 answers.
2. Save the result as `(C) Tidio Lyro Q&A. Export Wave 2.md` and `(C) Tidio Lyro Q&A. Export Wave 3.md` (or one consolidated file).
3. Tell Beta to proceed with the full audit once captures are complete.

**In the meantime**, Beta can start auditing Wave 1 (100 questions) judging on the question text alone. For Wave 1 Q&As where the question itself is enough to decide (DELETE: all discount/promo questions, all order-status questions), grade them now. For Q&As where the answer matters, mark them `PENDING ANSWER` in the decisions file and revisit once the answer text is captured.

---

## 8. Suggested First 5 Moves for Beta

1. **Read** the five canonical docs (Section 0). Confirm understanding of voice, policy, white-label rule, em dash rule.
2. **Open** `(C) Tidio Lyro Q&A. Export Wave 1.md` and scan all 100 questions. Build a mental map of topic clusters.
3. **Triage the 100 Wave 1 questions** into the decisions table. For ones where the question alone decides it (discount hunting, expired promos, order status), make the call. For ones where the answer matters (warranty, returns, sizing), mark `PENDING ANSWER`.
4. **Draft Batch 1 of the decisions file** at `(C) Tidio Lyro Q&A Audit. Decisions Batch 1.md` covering all 100 Wave 1 questions.
5. **Flag the 5 most ambiguous calls** to Amir in a "Questions for Amir" section at the top of the decisions file. Don't guess on these. Get a ruling, then proceed.

---

## 9. STATUS

**Handoff: ready.** Beta has everything needed to start auditing Wave 1 (100 questions) today.

**Blocking step before full 245 audit:** Amir needs to capture Waves 2 and 3 + all answer text (see Section 7).

**Blocking step before $62.50/mo Tidio upgrade:** This full audit must complete first. No paying to scale a polluted knowledge base.

Anything missing or ambiguous, ask in-vault, don't invent.

*Claudian, 2026-05-18*
