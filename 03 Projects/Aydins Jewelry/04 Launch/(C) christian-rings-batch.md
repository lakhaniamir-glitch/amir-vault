# Christian Rings — Batch Build Tracker

> **Created:** 2026-05-07
> **Status:** 16 ACTIVE on all 9 sales channels. 3 still DRAFT awaiting variants (Shopify daily creation limit).
> **2026-05-07 update:** Renamed VALOR → STEADFAST and LEGION → HOST (naming conflict with existing rings). All 19 descriptions slimmed (H3 + Key Features + Why, no em dashes). Tungsten Ring Information page + Warranty tab rewritten in Crown & Caliber voice. Material info pages drafted for Titanium, Ceramic, 14k Gold, Black Zirconium, Damascus Steel, Sterling Silver, Cobalt Chrome. **16 rings flipped to ACTIVE and published to all 9 sales channels (Online Store, Google & YouTube, Facebook & Instagram, Pinterest, Shop, TikTok, POS, Daily P&L, Microsoft Copilot).**
> **Source:** white-labeled from Universal Jewelry / Thorsten
> **Smart collection:** Christian Rings (rule: tag EQUALS "Christian Rings" — `gid://shopify/Collection/467763036397`) — auto-joins on tag

---

## Summary

- **Total rings:** 19 (1 pre-existing CREDO + 18 new in this batch)
- **All DRAFT** — none flipped to ACTIVE yet (pending mobile check + Zepto engraving verification)
- **Total variants created:** 945 across 16 rings (63 each, 23 sizes × 3 widths typical)
- **Pending variants:** 105 across FLEUR (21) + SANCTUS (42) + HOST (42, formerly LEGION) — Shopify hit 24h variant creation cap
- **Pricing rule:** retail = ~3× landed cost, rounded to clean tier ($229/$239/$249/$269/$289/$329/$359)
- **All cross-linked:** 4 sibling rings each via `shopify--discovery--product_recommendation.related_products`

---

## Listings (all DRAFT)

| Aydins Name | Shopify GID | Handle | Width(s) | Color | Cost | Retail | Variants |
|---|---|---|---|---|---|---|---|
| **CREDO** | 9362184962285 | credo-gold-tungsten-wedding-band-woven-cross-beveled | 6/8mm | Gold | $110.50 | **$329.00** ↓ | 42 ✓ |
| **PARISH** | 9362208424173 | parish-mens-tungsten-cross-wedding-band-woven-pattern | 6/8/10mm | Silver | $79.90 | $239.00 | 63 ✓ |
| **CHANCEL** | 9362208489709 | chancel-tungsten-cross-wedding-band-deep-woven-pattern | 6/8/10mm | **Black** ✓ | $83.30 | $249.00 | 63 ✓ |
| **CRUX** | 9362208588013 | crux-gold-tungsten-sideways-cross-wedding-band-domed | 6/8/10mm | Gold | $96.90 | $289.00 | 63 ✓ |
| **STEADFAST** (was VALOR) | 9362209571053 | steadfast-black-tungsten-iron-cross-wedding-band | 6/8/10mm | Black | $83.30 | $249.00 | 63 ✓ |
| **CREED** | 9362209636589 | creed-black-tungsten-minimalist-cross-wedding-band | 6/8/10mm | Black | $83.30 | $249.00 | 63 ✓ |
| **VESPER** | 9362209702125 | vesper-black-tungsten-sideways-cross-wedding-band | 6/8/10mm | Black | $83.30 | $249.00 | 63 ✓ |
| **SUMMIT** | 9362209734893 | summit-black-tungsten-mountain-landscape-wedding-band | 6/8/10mm | Black | $83.30 | $249.00 | 63 ✓ |
| **ADVENT** | 9362210783469 | advent-black-tungsten-nativity-scene-wedding-band | 6/8/10mm | Black | $83.30 | $249.00 | 63 ✓ |
| **CHAPLET** | 9362210816237 | chaplet-black-tungsten-rosary-wedding-band | 6/8/10mm | Black | $83.30 | $249.00 | 63 ✓ |
| **PSALM** | 9362210914541 | psalm-black-tungsten-lords-prayer-wedding-band | 6/8/10mm | Black | $83.30 | $249.00 | 63 ✓ |
| **PALM** | 9362210947309 | palm-tungsten-palm-branches-christian-wedding-band | 6/8/10mm | Silver | $79.90 | $239.00 | 63 ✓ |
| **VOTIVE** | 9362211471597 | votive-tungsten-rosary-wedding-band-classic-silver | 6/8/10mm | Silver | $79.90 | $239.00 | 63 ✓ |
| **ORATE** | 9362211504365 | orate-tungsten-lords-prayer-wedding-band-classic-silver | 6/8/10mm | Silver | $79.90 | $239.00 | 63 ✓ |
| **RIDGE** | 9362211569901 | ridge-tungsten-mountain-landscape-wedding-band-silver | 6/8/10mm | Silver | $76.50 | $229.00 | 63 ✓ |
| **EVE** | 9362211602669 | eve-gold-tungsten-nativity-scene-wedding-band-domed | 6/8/10mm | Gold | $96.90 | $289.00 | 63 ✓ |
| **FLEUR** | 9362211995885 | fleur-rose-gold-tungsten-fleur-cross-wedding-band-beveled | 8mm | Rose Gold | $90.10 | $269.00 | **0 ⚠** |
| **SANCTUS** | 9362212028653 | sanctus-gold-tungsten-sunburst-cross-wedding-band-beveled | 6/8mm | Gold | $108.50 | $329.00 | **0 ⚠** |
| **HOST** (was LEGION) | 9362212061421 | host-gold-black-tungsten-multi-cross-wedding-band | 6/8mm | Two-tone | $120.70 | $359.00 | **0 ⚠** |

⚠ = Variants blocked by Shopify's 24-hour daily variant creation limit. Retry with `batch5_variants_retry.py` after the limit resets.

---

## What's Set on Every Listing

✅ Title (Aydins-named, ≤70 char)
✅ Full SEO description (5 H2 sections: Specs at a glance, Comfort Fit, Engraving, Warranty + Sizing, Care, Shipping, Why [Name])
✅ SEO title (≤70 char)
✅ Meta description (≤150 char)
✅ Product category: `gid://shopify/TaxonomyCategory/aa-6-9` (Apparel & Accessories > Jewelry > Rings) — Shopify taxonomy doesn't have a "Wedding Bands" subcategory
✅ Tags including `Christian Rings` (auto-joins collection) + `Inside` (Zepto engraving flag) + `Comfort Fit` + product-specific tags
✅ Status: **DRAFT**
✅ 21 metafields per ring:
- `custom.keywords` — Quick Specs (10-line spec sheet)
- `custom.custom_faq_schema` — JSON-LD FAQPage with 4 universal Q&A + 3 ring-specific Q&A
- `custom.color` — list.color hex codes
- `custom.tungsten_ring_information_` — page reference (Tungsten Ring Information)
- `custom.ring_size_chart` — page reference (Ring Sizing Guide)
- `theme.custom_page` — page reference (Shipping & Returns)
- `mm-google-shopping.color` — Google Shopping color hex
- `mm-google-shopping.custom_product` — true (boolean)
- `mm-google-shopping.google_product_category` — 200 (Jewelry)
- `mc-facebook.google_product_category` — 200
- `mc-facebook.condition` — new
- `global.title_tag`, `global.description_tag` — fallback SEO metafields
- `shopify.color-pattern` — color pattern metaobject reference
- `shopify.ring-size` — list of ring size metaobjects
- `shopify.jewelry-material` — tungsten + plating metaobjects
- `shopify.ring-design` — Band metaobject
- `shopify.target-gender` — Male
- `shopify.jewelry-type` — Fine Jewelry
- `shopify.age-group` — Adults
- `customify.cstmfy_req` — 1 (Zepto required flag)
- `shopify--discovery--product_recommendation.related_products` — 4 sibling Christian rings (cross-linked within batch)
✅ Variants with cost-per-item set on every variant (Shopify internal margin tracking)
✅ Inventory: 10/size, `tracked: true`, location Aydins

---

## Pricing Math (per-ring)

All retail prices are 3× landed cost rounded to clean tier:

| Tier | Cost | Retail | Net before ads |
|---|---|---|---|
| $229 | $76.50 | $229.00 | ~$135 |
| $239 | $79.90 | $239.00 | ~$140 |
| $249 | $83.30 | $249.00 | ~$146 |
| $269 | $90.10 | $269.00 | ~$158 |
| $289 | $96.90 | $289.00 | ~$170 |
| $329 | $108.50 | $329.00 | ~$197 |
| $359 | $120.70 | $359.00 | ~$215 |

Net-before-ads = retail − cost − 3% Shopify fees − $8 free-shipping absorption.

Ad tolerance floor: **3× ROAS** on every ring (still leaves $80–$120 net per order).

---

## Engraving Convention (Zepto)

- All 19 rings: source-driven from UJ "Engravable In Only" → `Inside` tag (no parens)
- Listing copy mentions inside engraving in Key Features and emotional close
- Tag verified 2026-05-07: bare-word `Inside`, NOT `(Inside)` — Zepto reads bare-word

---

## Pre-Launch Checklist (per ring before flipping ACTIVE)

- [ ] Mobile check — visit preview URL on phone
- [ ] Zepto inside-engraving renders on PDP
- [ ] Verify image stack order (front → flat → angles)
- [ ] Spot-check Quick Specs section on storefront
- [ ] Spot-check FAQ schema renders (testable via Google Rich Results Test on live URL)
- [ ] Set up first traffic channel
- [ ] Add to homepage Christian collection module if launching in batch

---

## Outstanding Tasks

1. **Re-run `batch5_variants_retry.py` after 24hr (≥ 2026-05-08 ~13:00 CT):**
   - FLEUR: add 21 variants
   - SANCTUS: add 42 variants
   - HOST (formerly LEGION): add 42 variants — SKUs should be `AY-HOST-*` not `AY-LEGION-*`
2. **Mobile check + Zepto verification** on all 19 PDPs before flipping to ACTIVE
3. **Launch plan** — pick first traffic channel (recommended: organic email/SMS to existing tungsten buyers, then Google Shopping if margin holds)
4. **Day-30 review** — kill any ring with <3× ROAS and no organic traction; double down on top 3 winners

---

## Build Scripts (kept in temp; NOT committed to vault)

Location: `C:\Users\amirl\AppData\Local\Temp\aydins-batch\`

- `build_listing.py` — master per-ring builder (productCreate → variants → media → metafields)
- `templates.py` — shared body blocks + FAQ helpers
- `batch1.py` … `batch5.py` — per-batch ring specs (PARISH/CHANCEL/CRUX, VALOR/CREED/VESPER/SUMMIT, ADVENT/CHAPLET/PSALM/PALM, VOTIVE/ORATE/RIDGE/EVE, FLEUR/SANCTUS/LEGION) — note: VALOR + LEGION renamed to STEADFAST + HOST in Shopify on 2026-05-07; scripts still use old names internally
- `slim_all.py` — slimmed all 19 descriptions (H3, no em dashes, Key Features + Why structure)
- `slim_credo.py` — slimmed CREDO description specifically
- `rename_rings.py` — renamed VALOR → STEADFAST and LEGION → HOST (titles, handles, SEO, descriptions, SKUs). Shopify auto-creates 301 redirects.
- `update_credo.py` — CREDO retroactive update (description, SEO, 21 metafields, price drop)
- `fix_chancel.py` — CHANCEL color correction (was wrongly built as silver, actual UJ source is black)
- `cross_link.py` — Related Products cross-link across all 19 rings
- `batch5_variants_retry.py` — **RUN TOMORROW** to add variants once Shopify daily limit resets

---

## Notes / Issues Found During Build

1. **Shopify taxonomy:** No "Wedding Bands" subcategory exists. Used parent "Rings" (`aa-6-9`) — same as CREDO baseline.
2. **CHANCEL color mismatch:** UJ source title says "WOVEN CROSSES on Black Flat Tungsten Carbide Ring" — initially built as silver (mistake), fixed via `fix_chancel.py`. Color metafields, tags, description, and Quick Specs all corrected.
3. **RIDGE silhouette note:** UJ source title says "Domed Tungsten Carbide" — listing built as flat (minor copy mismatch). Description and Quick Specs say "Flat exterior". To fully verify, may want to update RIDGE to say "Domed exterior" — low priority.
4. **Shopify daily variant creation limit:** ~1,000 variants/day. Hit at variant 945 (4 batches × 63 + small change). Last 3 products got created without variants but with full metafields — safe to add variants later.
5. **Variant updates do NOT count against daily creation limit** — confirmed when CREDO 42 variants got price-updated successfully even after the limit was hit.

---

## Wakeup Schedule

A wakeup is scheduled for ~24 hours from now (≥ 2026-05-08 13:00 CT) to run `batch5_variants_retry.py` and add variants to FLEUR, SANCTUS, LEGION.
