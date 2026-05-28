# (C) Doofinder Quiz Maker — "Find Your Ring" Build Plan

**Status:** Researched + planned. Build not started.
**Owner:** Amir
**Last updated:** 2026-05-10
**Next prompt to Claude:** "Open Doofinder Quiz Maker Build Plan and let's start building." (See bottom of file.)

---

## 0. Pre-build verification (do this FIRST, 5 minutes)

Before any build work, confirm:

- [ ] **Doofinder plan tier includes Quiz Maker.** Log in → Doofinder admin → left menu should show "Quiz maker". If not, contact Doofinder support to enable it.
- [ ] **Catalog tag coverage.** Open any 5 products in Shopify admin. Each should have tags matching the pattern:
  - `material-tungsten` / `material-titanium` / `material-damascus` / `material-wood` / `material-meteorite`
  - `color-silver` / `color-black` / `color-gold` / `color-two-tone` / `color-rose-gold`
  - `style-classic` / `style-bold` / `style-exotic`
  - `width-6` / `width-7` / `width-8` / `width-9` / `width-10` (or width metafield)
- [ ] **Doofinder Single Script is live** in the theme (already true if Doofinder search is working).
- [ ] **At least one Search Engine** exists in Doofinder admin.

**If tag coverage <90%, run the bulk tagger script (Claude can build this) BEFORE configuring the quiz** — empty result sets are the #1 thing that kills these quizzes.

---

## 1. What Doofinder Quiz Maker actually is

A guided product-finder bound to your Doofinder Search Engine. Each answer **filters down the indexed catalog cumulatively**. Final step renders matching products as `.dfd-card` product cards inside the quiz modal.

### Confirmed capabilities (from docs)

- **Question types:** single-choice OR multi-choice only (toggle per question)
- **Filter modes:** "Individual items" (hand-picked SKUs) OR "Rules" (bulk filter by field/tag values)
- **Trigger:** ONE CSS selector pasted into Doofinder admin — clicking any element matching that selector opens the quiz
- **Analytics provided:** Impressions, Starts, Completions, CTR, Status, Form CSV download (6hr link validity), date-range calendar
- **Lead capture:** optional form slide with CSV export

### Confirmed limitations (from docs)

- ❌ No range sliders → budget must be discrete buckets
- ❌ No conditional branching → every customer answers every question
- ❌ No native image-question type (visual answers come from CSS styling of answer cards)
- ❌ No text-input questions (other than the optional lead form)
- ❌ No dedicated quiz-page URL documented
- ❌ No popup auto-trigger (no exit-intent, scroll, time delay) — manual click only
- ❌ No revenue/conversion tracking, no A/B testing, no per-question drop-off analytics
- ❌ Plan tier requirements NOT documented — verify with Doofinder

### How results connect to your catalog

- Quiz binds to a Doofinder **Search Engine** (the indexed feed)
- "Rules" filters reference fields/tags Doofinder already indexes from your Shopify feed
- No native Shopify Liquid integration documented — it's all JS injection via the Single Script

---

## 2. Quiz design — "Find Your Ring" (5 questions)

Designed around Doofinder's actual constraints. Keep at ≤5 questions to protect completion rate (no branching means everyone answers all of them).

### Q1 — Budget (single-choice)

> **What's your budget?**

| Answer | Doofinder Rule |
|---|---|
| Under $200 | `price < 200` |
| $200–$300 | `price >= 200 AND price <= 300` |
| $300–$400 | `price >= 300 AND price <= 400` |
| $400+ | `price > 400` |

### Q2 — Material (MULTI-choice)

> **What materials are you drawn to?** *(pick all that apply)*

| Answer | Doofinder Rule (or tag) |
|---|---|
| Tungsten | `material = tungsten` OR tag `material-tungsten` |
| Titanium | `material = titanium` OR tag `material-titanium` |
| Damascus Steel | `material = damascus` OR tag `material-damascus` |
| Wood Inlay | tag `material-wood` |
| Meteorite & Exotic | tag `material-meteorite` OR tag `material-dinosaur-bone` OR tag `exotic` |

*Multi-choice on this question is critical — most men want to compare 2-3 materials.*

### Q3 — Style (single-choice)

> **What style fits you?**

| Answer | Doofinder Rule (tag-based) |
|---|---|
| Classic & Clean | tag `style-classic` |
| Bold & Textured | tag `style-bold` |
| Unique & Exotic | tag `style-exotic` |

### Q4 — Width (single-choice)

> **Preferred width?**

| Answer | Doofinder Rule |
|---|---|
| 6mm or thinner | `width <= 6` |
| 7-8mm (most popular) | `width >= 7 AND width <= 8` |
| 9mm or wider | `width >= 9` |

### Q5 — Color (single-choice)

> **What color speaks to you?**

| Answer | Doofinder Rule (tag) |
|---|---|
| Silver / Natural | tag `color-silver` |
| Black | tag `color-black` |
| Gold | tag `color-gold` |
| Two-Tone | tag `color-two-tone` |
| Rose Gold | tag `color-rose-gold` |

### Why we DROPPED the engraving question

Engraving is a free service on every Aydins ring — not a SKU filter. Asking it hurts completion rate without narrowing results.

**Better use:** add it to the optional lead-capture form at the end as a soft upsell prompt — "Want a free engraving sample? Enter your email." Turns it into a list-building lever instead of a wasted filter step.

---

## 3. V4 Editorial CSS — paste verbatim into Doofinder

**Where to paste:** Doofinder Admin → Quiz Maker → [your quiz] → Advanced Configuration → CSS → Customize → paste → Save.

```css
/* ============================================
   AYDINS V4 EDITORIAL — DOOFINDER QUIZ STYLE
   ============================================ */

/* --- Brand tokens (scoped to quiz) --- */
.dfd-website-quiz {
  --v4e-ink: #191919;
  --v4e-stone: #f0ebe1;
  --v4e-gold: #B08D57;
  --v4e-gold-light: #c9a84c;
  --v4e-white: #ffffff;
  --v4e-text-mid: #5e5a56;
  --v4e-text-muted: #9a9590;
  --v4e-stone-border: #cec8bc;
  --dfd-btn-color: #191919;
  --dfd-btn-hover-color: #B08D57;
}

/* --- Modal shell --- */
.dfd-website-quiz .dfd-quiz-modal-content {
  background: var(--v4e-stone) !important;
  border-radius: 0 !important;
  border: 1px solid var(--v4e-stone-border) !important;
  font-family: 'Poppins', sans-serif !important;
  color: var(--v4e-ink) !important;
}

.dfd-website-quiz .dfd-quiz-modal,
.dfd-website-quiz .dfd-quiz-modal-body {
  background: transparent !important;
}

/* --- Question titles (Doofinder wraps them in <b>/<strong>) --- */
.dfd-website-quiz b,
.dfd-website-quiz strong {
  font-family: 'Bebas Neue', sans-serif !important;
  font-weight: 400 !important;
  font-size: 38px !important;
  line-height: 1.05 !important;
  letter-spacing: 0.02em !important;
  color: var(--v4e-ink) !important;
  text-align: center !important;
  text-transform: uppercase !important;
}

/* --- Body / paragraph copy --- */
.dfd-website-quiz p,
.dfd-website-quiz label,
.dfd-website-quiz span {
  font-family: 'Poppins', sans-serif !important;
  color: var(--v4e-text-mid) !important;
  font-size: 14px !important;
  letter-spacing: 0.02em !important;
}

/* --- Answer cards (the choices the user clicks) --- */
.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label .dfd-card {
  background: var(--v4e-white) !important;
  border: 1px solid var(--v4e-stone-border) !important;
  border-radius: 0 !important;
  padding: 22px 18px !important;
  transition: border-color 0.2s ease, background 0.2s ease, color 0.2s ease !important;
  cursor: pointer !important;
  box-shadow: none !important;
}

.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label .dfd-card:hover {
  border-color: var(--v4e-gold) !important;
  background: var(--v4e-white) !important;
  transform: none !important;
  box-shadow: none !important;
}

/* Selected state — Doofinder doesn't document the exact class.
   Covering the four most likely patterns. Verify in DevTools
   after first test render and patch if needed. */
.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label input:checked ~ .dfd-card,
.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label .dfd-card[aria-checked="true"],
.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label .dfd-card.selected,
.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label .dfd-card.is-selected {
  background: var(--v4e-ink) !important;
  border-color: var(--v4e-gold) !important;
  color: var(--v4e-stone) !important;
}

.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label input:checked ~ .dfd-card,
.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label input:checked ~ .dfd-card * {
  color: var(--v4e-stone) !important;
}

/* --- Continue / primary button --- */
.dfd-website-quiz .dfd-quiz-modal-body .dfd-continue-button {
  background: var(--v4e-ink) !important;
  color: var(--v4e-stone) !important;
  border: 1px solid var(--v4e-ink) !important;
  border-radius: 0 !important;
  font-family: 'Poppins', sans-serif !important;
  font-weight: 500 !important;
  font-size: 13px !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  padding: 16px 32px !important;
  cursor: pointer !important;
  transition: background 0.25s ease, color 0.25s ease, border-color 0.25s ease !important;
  box-shadow: none !important;
  text-decoration: none !important;
}

.dfd-website-quiz .dfd-quiz-modal-body .dfd-continue-button:hover,
.dfd-website-quiz .dfd-quiz-modal-body .dfd-continue-button:focus {
  background: var(--v4e-gold) !important;
  border-color: var(--v4e-gold) !important;
  color: var(--v4e-ink) !important;
}

/* --- Product result cards (final step) --- */
.dfd-quiz-modal .dfd-card {
  background: var(--v4e-white) !important;
  border: 1px solid var(--v4e-stone-border) !important;
  border-radius: 0 !important;
  transition: border-color 0.2s ease !important;
  box-shadow: none !important;
}

.dfd-quiz-modal .dfd-card:hover {
  border-color: var(--v4e-gold) !important;
  transform: none !important;
  box-shadow: none !important;
}

/* Price */
.dfd-quiz-modal .dfd-card-price {
  font-family: 'Poppins', sans-serif !important;
  color: var(--v4e-ink) !important;
  font-weight: 500 !important;
  font-size: 16px !important;
  letter-spacing: 0.04em !important;
}

.dfd-quiz-modal .dfd-card-price--sale {
  color: var(--v4e-gold) !important;
  font-weight: 600 !important;
}

.dfd-quiz-modal .dfd-card-price--sale ~ .dfd-card-price {
  color: var(--v4e-text-muted) !important;
  text-decoration: line-through !important;
  font-weight: 400 !important;
}

/* Sale/featured flags on product cards */
.dfd-card-flags .dfd-card-flag {
  background: var(--v4e-ink) !important;
  color: var(--v4e-stone) !important;
  border-radius: 0 !important;
  padding: 4px 10px !important;
  font-family: 'Poppins', sans-serif !important;
  font-size: 10px !important;
  font-weight: 500 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  top: 12px !important;
  left: 12px !important;
}

/* Add to Cart on result cards */
.dfd-card .dfd-cart-add-button {
  background: var(--v4e-ink) !important;
  color: var(--v4e-stone) !important;
  border: 1px solid var(--v4e-ink) !important;
  border-radius: 0 !important;
  font-family: 'Poppins', sans-serif !important;
  font-weight: 500 !important;
  font-size: 11px !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  padding: 10px 16px !important;
  transition: background 0.25s ease, color 0.25s ease, border-color 0.25s ease !important;
  transform: none !important;
  cursor: pointer !important;
}

.dfd-card .dfd-cart-add-button:hover {
  background: var(--v4e-gold) !important;
  color: var(--v4e-ink) !important;
  border-color: var(--v4e-gold) !important;
  transform: none !important;
}

/* --- Lead-capture consent text (form slide) --- */
.dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-form-slide-consent {
  font-family: 'Poppins', sans-serif !important;
  color: var(--v4e-text-muted) !important;
  font-size: 11px !important;
  letter-spacing: 0.04em !important;
  line-height: 1.5 !important;
}

/* --- Form inputs (lead capture) --- */
.dfd-website-quiz input[type="text"],
.dfd-website-quiz input[type="email"],
.dfd-website-quiz input[type="tel"],
.dfd-website-quiz select,
.dfd-website-quiz textarea {
  background: var(--v4e-white) !important;
  border: 1px solid var(--v4e-stone-border) !important;
  border-radius: 0 !important;
  color: var(--v4e-ink) !important;
  font-family: 'Poppins', sans-serif !important;
  font-size: 14px !important;
  padding: 12px 14px !important;
  box-shadow: none !important;
}

.dfd-website-quiz input[type="text"]:focus,
.dfd-website-quiz input[type="email"]:focus,
.dfd-website-quiz input[type="tel"]:focus,
.dfd-website-quiz select:focus,
.dfd-website-quiz textarea:focus {
  border-color: var(--v4e-gold) !important;
  outline: none !important;
}

/* --- Kill default Doofinder rounded corners anywhere we missed --- */
.dfd-website-quiz *,
.dfd-quiz-modal * {
  border-radius: 0 !important;
}

/* --- Mobile --- */
@media (max-width: 720px) {
  .dfd-website-quiz b,
  .dfd-website-quiz strong {
    font-size: 28px !important;
  }
  .dfd-website-quiz .dfd-quiz-modal-body .dfd-continue-button {
    width: 100% !important;
    padding: 14px 24px !important;
  }
  .dfd-website-quiz .dfd-quiz-modal-body .dfd-quiz-modal-choices label .dfd-card {
    padding: 16px 14px !important;
  }
}
```

**Selected-state caveat:** Doofinder docs don't document the selected-state class. The CSS above covers the 4 most common patterns. After publishing a test quiz, inspect the chosen card in DevTools — if Doofinder uses a different class, ping Claude to patch.

---

## 4. Placement strategy — 3 entry points, 1 trigger class

Doofinder triggers on a single CSS selector. Solution: make that selector a class (`.aydins-quiz-trigger`) and add it to every element that should open the quiz.

| Priority | Placement | Why |
|---|---|---|
| **1 (primary)** | Top nav link: "FIND MY RING" | Seen by every visitor; frames the site as easy-to-navigate |
| **2 (secondary)** | Homepage hero, below existing CTAs | Catches cold ad traffic that doesn't know what they want |
| **3 (tertiary)** | Bottom of collection pages | Catches shoppers who bounce around without committing |

All three elements get class `aydins-quiz-trigger`. In Doofinder admin paste `.aydins-quiz-trigger` once as the trigger selector.

---

## 5. Step-by-step build sequence (when ready)

### Phase 1 — Doofinder configuration (30 min)

1. Doofinder admin → confirm Quiz Maker appears in left menu (stop here if not)
2. Left menu → **Quiz maker** → **Add Quiz**
3. Search Engine: select `shopaydins.com` engine
4. Internal name: `Find Your Ring v1`
5. Status: **On**
6. **Where Would You Like to Trigger the Quiz?** → paste: `.aydins-quiz-trigger`
7. **Quiz Builder** — add 5 questions per Section 2 above:
   - Q1 Budget — single-choice — 4 answers with price rules
   - Q2 Material — **toggle MULTI-choice** — 5 answers with material tag rules
   - Q3 Style — single-choice — 3 answers with style tag rules
   - Q4 Width — single-choice — 3 answers with width rules
   - Q5 Color — single-choice — 5 answers with color tag rules
   - **For every answer:** click "choose products" → select **Rules** mode (NOT Individual items — doesn't scale)
8. **Quiz Appearance** — leave stock
9. **Advanced Configuration → CSS → Customize** → paste full CSS from Section 3 → **Save**
10. Optional: configure lead-capture form on final slide with engraving offer
11. **Save quiz** → **Preview**

### Phase 2 — Theme integration (15 min, code minimal)

**Option A — pure menu link, zero code:**
- Shopify admin → Online Store → Navigation → Main menu → add link "Find My Ring" → URL `#quiz` → Save
- In Doofinder change trigger selector from `.aydins-quiz-trigger` to `a[href="#quiz"]`

**Option B — class-based (recommended for multi-placement):**
- Add this snippet near the bottom of `theme.liquid` (before `</body>`):

```liquid
{% comment %} Inject quiz-trigger class on Find My Ring nav link {% endcomment %}
<script>
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href="#quiz"]').forEach(function(el) {
      el.classList.add('aydins-quiz-trigger');
    });
  });
</script>
```

- For homepage and collection-page entry points, hardcode `class="aydins-quiz-trigger"` directly in the section Liquid where the CTAs go
- In Doofinder keep trigger selector as `.aydins-quiz-trigger`

### Phase 3 — Verification (10 min)

- [ ] Quiz opens when nav link is clicked
- [ ] All 5 questions render in Bebas + Poppins, no rounded corners, no blue
- [ ] Selected answer card flips to ink bg + gold border + stone text
- [ ] Continue button is ink/stone, hovers to gold/ink
- [ ] Final step shows actual products (not empty results) for these test paths:
  - [ ] Tungsten + Classic + 7-8mm + Silver + $200-$300
  - [ ] Damascus + Bold + 7-8mm + Black + $300-$400
  - [ ] Meteorite & Exotic + Unique & Exotic + 9mm+ + Two-Tone + $400+
- [ ] Mobile (≤720px): titles drop to 28px, button goes full-width
- [ ] Doofinder analytics show impressions/starts/completions incrementing after self-test
- [ ] Inspect selected state in DevTools — patch CSS if Doofinder uses non-standard class name

---

## 6. Risks logged (already identified, plan handles them)

1. **Tag coverage gap** — #1 cause of empty result sets. Audit BEFORE Phase 1. Claude can build bulk tagger if needed.
2. **Plan tier unverified** — confirm Quiz Maker in Doofinder left menu first.
3. **No conditional branching** — every customer answers all 5. If completion rate <40% after launch, cut to 3 questions (budget/material/style) and re-test.
4. **Selected-state CSS** — confirmed by DevTools inspection after first render; one-line patch if needed.
5. **No revenue tracking** — Doofinder analytics show CTR but not conversion. Add UTM `?utm_source=quiz` to result-card links if we need attribution (requires custom JS — TBD).

---

## 7. Source docs (reference)

- Setup: https://support.doofinder.com/quiz-maker/quiz-maker-setup
- CSS: https://support.doofinder.com/quiz-maker/css-quiz-maker-customization

Both fetched and summarized 2026-05-10.

---

## 8. When ready to build — paste this prompt to Claude

> Open `(C) Doofinder Quiz Maker — Build Plan.md` in `03 Projects/Aydins Jewelry/`. Walk me through Section 0 pre-build verification first. After I confirm tag coverage and plan tier, proceed with Phase 1 build sequence step-by-step. Pause for confirmation between phases.

---

**END OF BUILD PLAN**
