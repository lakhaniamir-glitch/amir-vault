# (C) Shopify Listing Standard — Brief for Beta-Shop [SUPERSEDED 2026-05-26]

> **⚠️ SUPERSEDED 2026-05-26.** This CREDO-format brief is no longer authoritative. The current locked standard is the **VESUVIUS-approved format** at [[(C) Aydins Shopify Ring Listing Standard - VESUVIUS Format LOCKED 2026-05-26]]. Key changes: no policy blocks (warranty/returns/shipping/sizing) in product body; 6 product-specific FAQ questions instead of 5 policy questions; Quick Specs metafields in `custom.keywords` + `custom.quick_specs`; SKU format `CODENAME-WIDTH-SIZE` not `AY-CODENAME-{WIDTH}-{SIZE}`. Use the VESUVIUS standard for all new work. This file is kept for archive only.

> **Purpose:** Hand this to Beta. Beta routes it to Beta-Shop as the canonical spec for how every Aydins Jewelry Shopify listing must be built. Mirrors the way these listings have already been done (see CREDO, the 57 UJ rename batch, the Christian Rings batch).
> **Source files this brief was distilled from:**
> - [[03 Projects/Aydins Jewelry/CLAUDE.md]]
> - [[03 Projects/Aydins Jewelry/(C) Aydins Policies — Source of Truth]]
> - [[03 Projects/Aydins Jewelry/04 Launch/(C) credo-listing]] (working example)

---

## 1. TITLE FORMAT

**Pattern:**
```
CODENAME | [Material] [Product Type], [Pattern/Inlay], [Profile/Feature]
```

**Rules:**
- Codename in ALL CAPS first (e.g. CREDO, FLETCHER, PALEO, NAUTILUS)
- Pipe `|` separates codename from descriptor
- Descriptor is plain-English, comma-separated, mobile-readable
- No third-party brand names (no Thorsten, no Universal Jewelry, no JCK)
- No "handcrafted / handmade / forged" — Aydins engraves and ships, does not manufacture

**Examples (live and approved):**
- `CREDO | Gold Tungsten Wedding Band, Woven Cross Pattern, Beveled Edges`
- `NAUTILUS | Satin Tungsten Ring, 3 Blue Sapphires`
- `FLETCHER | Bow Archery Engraved Flat Tungsten Wedding Band`

---

## 2. SEO TITLE (Shopify "Page title" field)

**Hard limit: ≤ 70 characters.** Google truncates at ~60 in SERP.

**Pattern:**
```
CODENAME | [Material + Key Feature] – [Trust Hook] | Aydins
```

**Rules:**
- Front-load primary keyword
- Brand suffix `| Aydins` (8 chars) only if it fits
- Count every character including spaces
- Shorter beats over-budget

**Example (54 chars):**
`CREDO | Gold Tungsten Cross Ring – Comfort Fit | Aydins`

---

## 3. META DESCRIPTION

**Hard limit: ≤ 150 characters.** Google truncates around 155 on mobile.

**Must include:** material + width or finish + key feature + trust signal (comfort fit / free engraving / free U.S. shipping).

**Example (143 chars):**
`Gold-plated tungsten wedding band with woven cross pattern, beveled edges, comfort fit. Free engraving + free U.S. shipping. Engraved in Texas.`

---

## 4. PRODUCT DESCRIPTION (live in Shopify)

**Required structure — in this order:**

### Opening paragraph (2–4 sentences)
A short narrative hook. Visual + emotional. Material + pattern + finger feel. No filler. Direct, masculine, polished. No "elevate / exquisite / timeless".

### Key Features (bolded bullet list — keep it skim-able on mobile)
Always include these labeled bullets when applicable:
- **Material:**
- **Pattern / Inlay:**
- **Profile:**
- **Comfort Fit:** (default on all Aydins rings — always mention)
- **Widths Available:**
- **Engraving:** (free, inside-only OR inside + outside per source rule)
- **Free U.S. Shipping**
- **Engraved and shipped from Irving, Texas**
- **Operating since 2011**

### Why [CODENAME] (1–3 sentences emotional close)
The naming story or "who it's for". Engraving CTA. Example:
> *"From Latin* I believe. *A ring built for the people who wear their faith quietly — through the work, through the years, through every promise kept. Engrave the inside. Make it his."*

---

## 5. FAQ BLOCK (use the same 5 questions on every PDP)

These five are mandatory. Wording must match the policy source of truth — no "lifetime warranty" / no "free lifetime resizing" / no "30-day free returns" framing.

**Q1. Is engraving included?**
> Yes. Free laser engraving on every Aydins ring — text, symbols, handwriting, or fingerprint. We set up your engraving the day your order comes in.

**Q2. Can I exchange or resize this ring?**
> Free exchange in the first 30 days on unengraved rings. Engraved rings: $34.50 exchange surcharge. After 30 days, our Lifetime Sizing program continues for the original purchaser — $34.50 in year one, $54.50 every year after.

**Q3. What's your return policy?**
> 30-day returns from delivery. $25 restocking fee, customer pays return shipping. Engraved rings can't be returned but can be exchanged (see above).

**Q4. What if my ring cracks or breaks?**
> Aydins Lifetime Warranty covers breakage and material defects automatically — free in the first 6 months, $34.50 flat from 6–12 months, $54.50 flat after that. Excludes normal wear, intentional damage, and shipping loss/theft (those are covered only by the optional Aydins Protection Plan).

**Q5. How fast does it ship?**
> Free U.S. shipping on every order. Most orders ship in 1–3 business days from our workshop in Irving, Texas.

---

## 6. TAGS (Shopify product tags — these drive collections + Zepto engraving)

Always include the category, material, profile, and audience tags. Plus the **engraving tag** that controls the Zepto personalizer UI:

| Engraving type | Tag (exact, no parens) |
|---|---|
| Inside only | `Inside` |
| Inside + Outside | `Inside & Outside` |

⚠️ Verified 2026-05-07: the Zepto app reads the bare-word tag (NO parentheses). Older docs that used `(Inside)` are wrong.

Source-driven engraving rule:
- universal-jewelry.com source page says "Engravable In Only" → **inside-only** → tag `Inside`
- Source says "Inside and Outside" → tag `Inside & Outside`
- Any ring with outside inlay → **inside-only**

**Other tag categories to fill in:**
- Material (Tungsten / Titanium / Ceramic / Damascus / Cobalt / Gold Plated Tungsten / 14k Gold)
- Profile / Style (Comfort Fit, Flat, Domed, Beveled, Pipe Cut)
- Inlay / Feature (Wood, Opal, Meteorite, Carbon Fiber, Dinosaur Bone, Diamond, etc.)
- Audience (Mens Rings, Wedding Bands, Couples)
- Theme collection (Christian Rings, Faith, Nature, Animal, Military, Memorial, etc. where applicable)

---

## 7. IMAGES + ALT TEXT

**Alt text formula:**
```
CODENAME [material] [product type] with [key visual feature] – [angle/profile]
```

**Examples:**
- `CREDO gold tungsten wedding band with woven cross pattern and beveled edges – front view`
- `CREDO gold tungsten ring flat profile showing comfort fit interior and beveled edge detail`

**Image order:**
1. Hero (front/center, ring laid flat or 45°)
2. Profile/side (shows comfort fit interior + edge detail)
3. Lifestyle / on-finger (if available)
4. Detail / engraving angle (if available)

**Never launch with a weak first image.**

---

## 8. VARIANTS + INVENTORY

- **Sizes must match the universal-jewelry.com source page exactly.** Do not extend or shrink the range.
- **Per-width sizing respected.** Some rings have multiple widths with different size ranges per width — match the source for each width.
- **Common widths:** 4mm, 6mm, 8mm, 10mm (8mm is the most popular men's wedding band width)
- **Inventory default:** `10` per size
- **Inventory tracking:** `tracked: true` on every variant
- **SKU format:** `AY-CODENAME-{WIDTH}-{SIZE}` (e.g. `AY-CREDO-6MM-9.00`)

---

## 9. PRICING MATH (mandatory before publish)

**Pricing rule:** **Retail = 3× landed cost.**

Every listing must run this math and record it:

| Line | Required |
|---|---|
| Landed cost (per ring, including supplier + shipping in) | $ |
| Retail price (3× landed cost) | $ |
| Compare-at price | none (clean retail, no fake-discount anchor) |
| Shopify payment fees (~3% + $0.30) | calc |
| Free shipping absorbed (avg.) | ~$8 |
| **Net before ad spend** | $ |
| Net margin % | % |

**Ad tolerance bands to evaluate:**

| ROAS target | Allowable CPA |
|---|---|
| 3× | net stays positive — floor |
| 4× | strong |
| 5× | excellent — scale |

**Cost-per-item** must be set on every variant in Shopify (internal field — never customer-facing).

**No product moves forward without pricing math signed off.**

---

## 10. COLLECTION ASSIGNMENT

Assign every product to its smart collection(s) by tag. Examples:
- `Christian Rings` → tag `Christian Rings`
- `Tungsten Wedding Bands` → tag `Tungsten` + `Wedding Bands`
- `Damascus Steel Rings` → tag `Damascus Steel`

---

## 11. PRE-PUBLISH CHECKLIST (the listing isn't done until every box is checked)

- [ ] Final title (codename + descriptor)
- [ ] Product description (opening + Key Features + Why CODENAME close)
- [ ] FAQ block present (5 standard Qs)
- [ ] SEO title ≤ 70 chars
- [ ] Meta description ≤ 150 chars
- [ ] Focus keywords listed in the master file
- [ ] Image alt text written for every image
- [ ] Hero image strong on mobile
- [ ] Pricing math complete (landed cost, 3× retail, ad tolerance)
- [ ] Variants match source widths/sizes exactly
- [ ] Inventory: 10 per size, tracked: true
- [ ] Cost-per-item set on every variant
- [ ] Engraving tag set correctly (`Inside` or `Inside & Outside`, no parens)
- [ ] Personalization instructions clear on PDP
- [ ] Trust messaging present (engraving free, free U.S. shipping, Irving TX workshop, since 2011)
- [ ] Collection(s) assigned
- [ ] **Mobile check passed**
- [ ] Preview URL tested — Zepto engraving renders correctly
- [ ] Launch channel selected (no orphan listings)

---

## 12. HARD RULES — NEVER DO THESE

### Voice / brand
- ❌ Never mention Thorsten, Universal Jewelry, JCK, or any third-party supplier
- ❌ Never say "handcrafted / handmade / forged / built / cut / made by hand / made in our workshop"
- ✅ Aydins **engraves and ships** from Irving, Texas. That's the truthful value-add.

### Location
- ❌ Never reference the Grapevine Mills Mall kiosk — it's CLOSED
- ❌ Never say "Flower Mound" as a current workshop / brand-voice location in listings. Always use **Irving, Texas**. (Flower Mound, TX IS the real legal mailing address and IS correct ONLY in email-footer legal-address blocks and on the Returns & Exchanges page. Not relevant to listings. Two-context rule locked 2026-05-15. See [[(C) Aydins Policies — Source of Truth]] rule 7.)
- ✅ "Irving, Texas" workshop. Origin story may say "started in a North Texas mall kiosk in 2011" (past tense) → "today, engraved and shipped from our workshop in Irving, Texas."

### Policy claims (the big ones — these are fabrications when stated bare)
- ❌ "Lifetime warranty" (bare) → use approved framing: "free first 6 months, $34.50 flat 6–12mo, $54.50 flat after"
- ❌ "Free lifetime resizing" / "Lifetime fit guaranteed" → use: "Lifetime Sizing for the original purchaser — $34.50 in year one, $54.50 every year after"
- ❌ "30-day free returns" → use: "30-day returns. $25 restocking, customer pays return shipping. Engraved rings excluded."
- ❌ "Free returns" → returns are NEVER free; only exchanges in first 30 days on unengraved rings are free
- ❌ "2-day shipping" → use: "Free U.S. shipping. Most orders ship in 1–3 business days." (carrier service-level not verified)
- ❌ "$100 14k gold fee" → there is NO flat $100. The correct figure: 25% surcharge on items over $1,000.
- ❌ "Price Match Guarantee" in marketing copy → it exists but stays on its own policy page only. Don't trumpet it on PDPs, ads, emails.
- ❌ "5% bonus on every order" → store credit bonus is conditional (only when refund → store-credit swap, one-time).

### Listing hygiene
- ❌ No publishing half-finished listings
- ❌ No skipping pricing math
- ❌ No weak first image
- ❌ No "we'll fix SEO later"
- ❌ No launches without a traffic plan

---

## 13. APPROVED TRUST PILLARS (use these freely)

Pull from this list when writing copy:

1. **Free engraving on every order**
2. **Free U.S. shipping**
3. **Engraved and shipped from our workshop in Irving, Texas**
4. **30-day returns** ($25 restocking, customer pays return shipping — engraved rings excluded)
5. **Free exchanges within 30 days on unengraved rings** ($34.50 surcharge on engraved)
6. **Lifetime Sizing program** — $34.50 in year one, $54.50 every year after, original purchaser only
7. **Aydins Lifetime Warranty** — free first 6 months, $34.50 flat 6–12 months, $54.50 flat after. Breakage + material defects.
8. **3–5 business day processing** on refunds and replacements once received
9. **Operating since 2011**
10. **Engraved exchanges accepted** — most jewelers won't take engraved rings back at all

---

## 14. EXAMPLE — A COMPLETE LISTING (CREDO, real and shipped as a draft)

See full reference: [[03 Projects/Aydins Jewelry/04 Launch/(C) credo-listing]]

**Title:** `CREDO | Gold Tungsten Wedding Band, Woven Cross Pattern, Beveled Edges`
**SEO Title (54):** `CREDO | Gold Tungsten Cross Ring – Comfort Fit | Aydins`
**Meta Description (143):** `Gold-plated tungsten wedding band with woven cross pattern, beveled edges, comfort fit. Free engraving + free U.S. shipping. Engraved in Texas.`
**Tags:** `Inside`, `Christian Rings`, `Comfort Fit`, `Faith`, `Gold Plated Tungsten`, `Mens Rings`, `Tungsten`, `Wedding Bands`
**Variants:** 42 (6mm × 21 sizes 4–14 in 0.5 steps; 8mm × 21 sizes 5–15 in 0.5 steps)
**Price:** $331.50 (3× $110.50 landed cost)

---

## 15. WHEN BETA-SHOP IS UNSURE

If Beta-Shop is missing info to complete any field, the answer is:
1. **Read the source page** at universal-jewelry.com — it has the widths, sizes, engraving rule, and inlay details
2. **Read this brief** for voice, tags, policy claims, pricing math, SEO format
3. **Ask Beta** for clarification on anything that isn't in either source — don't guess, don't make up specs, don't fabricate policy

Beta-Shop's prime directive: **build listings that pass the pre-publish checklist (Section 11), follow the hard rules (Section 12), and match the CREDO example (Section 14).**

---

*Brief compiled 2026-05-12. Update this file when policy, voice, or process changes — Beta-Shop should always work from the current version.*
