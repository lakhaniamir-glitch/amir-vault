# Size Chart — Redesign Spec

> **Surface:** `/pages/size-chart` — opens as a modal/popup next to the Add to Cart button on PDP, also accessible as a standalone page
> **Job to be done:** Kill sizing anxiety in <30 seconds so the customer hits Add to Cart with confidence
> **Context:** Mobile-first (70% of Aydins traffic). Modal must feel calm, not like a spreadsheet.
> **Status:** Spec — not yet built
> **Created:** 2026-05-06
> **Owner:** Amir
> **Design system:** [[.claude/DESIGN.md]] v1.1

---

## Why this redesign exists

The current page (`shopaydins.com/pages/size-chart`) is a bare 8-column international conversion table dropped into a popup with no header copy, no measuring instructions, no reassurance, and no CTA. For a customer hovering over Add to Cart on a $1,200 tungsten band, this *creates* sizing anxiety instead of killing it. On mobile, the 8-column table forces horizontal scroll — the exact moment the customer abandons.

The redesign flips the surface from "here's a table, figure it out" to "here are three ways to find your size, here's the safety net if you get it wrong."

---

## Spec Block

| Element | Value | Source |
|---|---|---|
| Background | Bone `#FAF8F4` | DESIGN.md §Color |
| Body text | Ink `#1A1A1A` | DESIGN.md §Color |
| Accents | Brass `#B08D57` (1× — eyebrow rule + numeral marks only) | DESIGN.md §Color |
| Border | Hairline `#E5E2DB` (table rules, card borders) | DESIGN.md §Color |
| Reassurance band background | Stone `#EEEAE2` | DESIGN.md §Color |
| Display font | Cormorant Garamond 500 — only on H1 | DESIGN.md §Typography |
| Body / UI | Poppins 400 / 500 / 600 | DESIGN.md §Typography |
| Modal width | 720px desktop / full-width mobile | DESIGN.md §Layout |
| Section padding | 56px tight inside modal / 80px standalone page | DESIGN.md §Layout |
| Primary CTA | Ink `#1A1A1A` bg, Bone text, 2px radius, 14px Poppins 500 +0.12em UPPERCASE | DESIGN.md §Buttons |
| Secondary CTA | Transparent bg, Ink border, Ink text — same type spec | DESIGN.md §Buttons |
| Modal entry | Backdrop fade + scale 0.98→1, 220ms ease-out | DESIGN.md §Animation |

**Color count: 4** (Bone bg, Ink text, Brass accent, Hairline borders) ✓
**Font count: 2** (Poppins + Cormorant) ✓

---

## Wireframe — Section by Section

### A. Hero — anxiety killer (top of modal, mobile-first)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│     RING SIZING                                              │  ← Eyebrow, Brass underline
│     ─────                                                    │     12px, +0.18em UPPERCASE
│                                                             │
│     Find your ring size.                                     │  ← Cormorant 500
│                                                             │     32px mobile / 40px desktop
│                                                             │
│     Not sure? Use a ring you already own — or measure with   │
│     a string. Standard rings (no engraving) can be exchanged │
│     free within 30 days. After that, our Lifetime Sizing     │
│     program keeps you covered.                               │  ← Body 16px, line-height 1.65
│                                                             │
│     ┌─────────────────────────────┐                         │
│     │     SEE HOW TO MEASURE      │  ← Primary CTA, Ink
│     └─────────────────────────────┘                         │
│                                                             │
│     Already know your size? Use the chart below.             │  ← Tertiary link, Ink underline
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Why it works:** Resolves anxiety in the first 5 seconds. The unsure customer gets a clear primary action (jump to the measuring methods). The customer who already knows their size gets a link to skip past the reassurance.

---

### B. Three ways — cards

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│     THREE WAYS TO FIND YOUR SIZE                             │  ← Eyebrow
│                                                             │
│     ┌─────────────────┬─────────────────┬─────────────────┐ │
│     │  01              │  02              │  03              │ │
│     │  Use a Ring      │  Measure at Home │  Convert a Size │ │
│     │  You Own         │                  │                  │ │
│     │                  │                  │                  │ │
│     │  Most accurate.  │  String + ruler. │  If you know     │ │
│     │  Measure inside  │  Takes 2 minutes.│  your UK / EU /  │ │
│     │  diameter.       │  See method →    │  Asia size.      │ │
│     │                  │                  │                  │ │
│     │  [Show method →] │  [Show me how →] │  [See chart →]   │ │
│     └─────────────────┴─────────────────┴─────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Layout:** 3-up desktop, single-column stacked mobile. 1px Hairline border, 2px radius, no shadow. Eyebrow numerals (`01 / 02 / 03`) in Brass — this is the only place Brass appears as a numeral (counts toward the 1× Brass rule alongside the hero rule under "RING SIZING").

---

### C. How to measure — two methods (collapsible)

**Method A — Use a ring you already own (most accurate)**

Three quick steps:
1. Take a ring that fits the correct finger comfortably.
2. Trace the inside of the ring on paper, or measure the inside diameter directly with a ruler in millimeters.
3. Match the diameter to the chart in section D.

> *Tip: place the ring on paper, trace the inside, and measure the line across the widest point.*

---

**Method B — Measure at home with a string and a ruler**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│     HOW TO MEASURE AT HOME                                   │
│     Two minutes. Need a string and a ruler.                  │
│                                                             │
│     ┌──────────┐     ┌──────────┐     ┌──────────┐          │
│     │  [diagram │     │ [diagram │     │ [diagram │          │
│     │   step 1] │     │  step 2] │     │  step 3] │          │
│     └──────────┘     └──────────┘     └──────────┘          │
│     01                02               03                    │
│     Wrap snug at      Mark where it    Measure the           │
│     the base of       overlaps.        marked length         │
│     the finger.                        in inches.            │
│                                                             │
│     ─────────────────────────────────────────────────       │
│                                                             │
│     A few notes from the workshop:                           │
│     • Measure at the end of the day — fingers are larger.    │
│     • Measure the hand the ring will live on.                │
│     • A wider band wears a half-size tighter. Size up.       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Imagery direction:** 3 hand-illustrated line drawings on Bone background — clean, monochrome Ink strokes. **Not** stock photos of a ruler on white. Editorial, like a Filson or Buck Mason care guide.

---

### D. International conversion chart — the actual table, redesigned

**The mobile fix:** the current 8-column table requires horizontal scroll on phone. Solution: segmented tabs above the table.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│     INTERNATIONAL CONVERSION                                 │
│                                                             │
│     [ US ]  UK   EU   ASIA                                   │  ← Tabs, Ink underline on active
│                                                             │
│     ┌──────────────────────────────────────────────┐        │
│     │  US Size │ Diameter (in) │ Circumference (in)│        │
│     ├──────────────────────────────────────────────┤        │
│     │   4       │  0.586         │  1.84           │        │
│     │   5       │  0.611         │  1.92           │        │
│     │   6       │  0.635         │  2.00           │        │  ← Hairline rules between rows
│     │   7       │  0.660         │  2.07           │        │     Alternating Bone / Stone bg
│     │   8       │  0.684         │  2.15           │        │     for readability
│     │   …       │  …             │  …              │        │
│     └──────────────────────────────────────────────┘        │
│                                                             │
│     [ Show all regions ]                                     │  ← Tertiary, expands 8-col view
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Tab behavior:** each tab swaps in only the columns relevant to that region. The customer in Germany doesn't need to see UK + Switzerland + Asia + France at once — they tap **EU**, see Germany / France / Switzerland in 4 columns, done.

**Desktop:** keep the full 8-column "all regions" table available via "Show all regions" toggle below the tabbed view.

**Type:**
- Headers: Poppins 500, 12px, +0.18em UPPERCASE, Charcoal
- Rows: Poppins 400, 14px, Ink
- Active tab: Ink text, 2px Ink underline. Inactive: Charcoal, no underline.

---

### E. Reassurance close

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│         ┌──────────────────────────────────────────┐        │
│         │                                          │        │
│         │     30-DAY EXCHANGES & LIFETIME SIZING   │  ← Eyebrow
│         │                                          │        │
│         │     Wrong size? Standard tungsten,       │        │
│         │     ceramic, cobalt, or titanium (no     │        │
│         │     engraving) exchanges free within     │        │
│         │     30 days. Engraved or after 30 days?  │        │
│         │     Our Lifetime Sizing & Warranty       │        │
│         │     Program ($34.50 first year, $54.50   │        │
│         │     after) keeps you covered for life.   │        │
│         │                                          │        │
│         │   [ EMAIL US ]   [ CALL 1-800-214-7345 ] │        │  ← Two Secondary buttons
│         │                                          │        │
│         └──────────────────────────────────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Stone `#EEEAE2` band background to set this section apart without adding a 5th color.

---

## What changed vs. the current page

| Current | Redesigned | Why |
|---|---|---|
| Naked 8-column table, no header copy | H1 + reassurance subhead at top | DESIGN.md §Voice — sizing copy must be calm, not anxious |
| One way to "figure it out" (read a table) | Three explicit paths (use a ring you own, measure with string, convert) | The customer with sizing anxiety doesn't want a table — they want permission to be unsure |
| Zero measuring instructions | Visual 3-step "measure at home" with workshop notes | Removes the "how do I even use this" question |
| 8-column horizontal-scroll table on mobile | Region tabs (US default) + slim 3-col table | Mobile is 70% of traffic. Horizontal scroll = abandonment |
| No reassurance about getting it wrong | 30-day free exchange (no engraving) + Lifetime Sizing program block | This is the actual buying-decision unlock |
| No CTAs anywhere on the page | Primary "See How to Measure" + tertiary helpers (anchored to method sections) | The popup must convert the moment of doubt into the next action |
| Promo banner above (`20% OFF`) | Removed inside the modal | The modal is a *trust* surface, not a sales surface — repeating the discount cheapens the moment |

---

## 10-Rule Self-Check

| # | Rule | Pass | Note |
|---|---|---|---|
| 1 | Whitespace ≥56px desktop / ≥40px mobile per section | ✓ | 56px tight inside modal; 80px standalone |
| 2 | ≤4 colors visible | ✓ | Bone, Ink, Brass, Hairline (Stone is tonal bg variant) |
| 3 | ≤2 fonts | ✓ | Poppins + Cormorant (1× on H1 only) |
| 4 | Mobile 375px — tap targets ≥44px, no horizontal scroll | ✓ | Tabbed table eliminates the horizontal-scroll fail |
| 5 | No banned tells (gradients, drop shadows, pure black, `#fff301`, ribbons, bursts, clip art) | ✓ | None present |
| 6 | Hierarchy unambiguous (squint test) | ✓ | H1 dominates, single primary CTA, supporting cards secondary |
| 7 | Photography first (or zero) | ✓ | Hand-drawn line diagrams in §C — not stock photos |
| 8 | Eyebrow above every section H2 | ✓ | "RING SIZING," "THREE WAYS…," "HOW TO MEASURE…," etc. |
| 9 | Premium gut-check (Hodinkee/Gear Patrol-adjacent) | ✓ | Editorial structure, calm copy, no panic markers |
| 10 | Trust gut-check (would a man spending $1,800 feel safe) | ✓ | Reassurance is the spine of the redesign |

**All 10 pass.**

---

## Implementation notes

### Shopify

- This is a Shopify page (`/pages/size-chart`) — needs a `page.size-chart.liquid` template using a custom `size-chart.liquid` section, or composed of `rich-text` + `image-with-text` + a custom `size-chart-table.liquid` section for the tabbed conversion table.
- The tabbed table requires a small piece of vanilla JS for tab switching (no framework). Keep it under 30 lines.
- **No sizing kit is offered.** Aydins does not ship sizing kits. Every CTA and method on this page must work without one. The two anchor methods are: (1) measure a ring the customer already owns, (2) measure with a string and a ruler.

### Modal vs. standalone

- The same Liquid renders both contexts. In modal context (opened from PDP), the page chrome (header / footer / promo banner) is hidden via the `?view=modal` template suffix or an `if request.page_type` check.
- Standalone access keeps the full chrome.

### Engraving + size relationship

- Engraved rings cannot be returned and cannot be exchanged free under the 30-day policy — they are covered by the Lifetime Sizing & Warranty Program ($34.50 first year, $54.50 after; $100 for 14k gold). Add one supporting line below the reassurance block: "Engraved rings are covered for life through our Lifetime Sizing program — re-engraving included."

---

## Open questions before build

1. **Is the modal opened by an existing app (e.g., a popup app), or is it a custom theme block?** Determines whether we have layout control or whether it's constrained to an app's container.
2. **Do we keep `/pages/size-chart` AND `/pages/ring-size-guide` as separate pages?** See note below.

---

## Duplication flag

There is an existing build-ready HTML artifact at [[03 Projects/Aydins Jewelry/03 Assets/(C) ring-size-guide-page.md]] targeting `/pages/ring-size-guide`. That URL doesn't exist on the current site — `/pages/size-chart` does.

**Two options:**

1. **Consolidate** — kill `/pages/ring-size-guide` plan, ship this redesign at `/pages/size-chart`, and the existing PDP popup link doesn't need to be re-pointed.
2. **Replace** — ship this redesign at `/pages/ring-size-guide` (per the older spec's URL), update the PDP popup link, and 301-redirect `/pages/size-chart` → `/pages/ring-size-guide`.

**Recommendation:** option 1. The existing URL has whatever indexing / inbound links it has — don't break it for a slug change.

---

## Next steps

1. Resolve the 3 open questions above.
2. Run `/shopify-design-qa` against this spec before code is written.
3. Write the Liquid section + page template.
4. Test on mobile 375px viewport.
5. Replace the live page.

---

## Honest note on priority

The highest-leverage move toward $50k/month is the 10–15 listing rebuild from the active 30-day plan ([[03 Projects/Aydins Jewelry/30-Day Plan — Strengthen The Core]]) — not a sizing-page redesign. This redesign helps conversion across every PDP, but if the listings aren't done yet, finish those first and ship this when they are.
