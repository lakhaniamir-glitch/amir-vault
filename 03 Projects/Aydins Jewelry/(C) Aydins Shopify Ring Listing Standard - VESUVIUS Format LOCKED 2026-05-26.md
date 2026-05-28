---
title: Aydins Shopify Ring Listing Standard (VESUVIUS Format)
status: LOCKED, authoritative
version: VESUVIUS-approved
date_locked: 2026-05-26
supersedes: "(C) Shopify Listing Standard — Brief for Beta-Shop.md (2026-05-12, CREDO format)"
applies_to: All Aydins Jewelry Shopify ring listings, going forward
---

# Aydins Shopify Ring Listing Standard

Use the VESUVIUS-approved format for every ring listing. Do not use the failed generic FAQ/policy-heavy format.

## 1. Description body structure

Keep the product description lean and buyer-facing:

- Strong opening paragraph
- Short supporting paragraph if needed
- Key Features bullet list
- "Why [CODENAME]" closing section
- No standalone duplicate Engraving section if engraving is already in Key Features/FAQ
- **No warranty, returns, shipping, sizing, or exchange policy blocks in the product body**

## 2. Key Features

Include only product-specific selling points:

- Material
- Inlay/feature
- Widths
- Fit
- Profile
- Engraving location
- Color/finish when relevant
- Daily wear/care note if product-specific

## 3. Quick Specs metafields

Use this exact format for `custom.keywords`:

```
Material: [material name]
Inlay/Feature: [feature name]
Widths: [list widths]
Fit: [fit type]
Profile: [profile detail]
Engraving: [location]
```

Add this line only when relevant:
```
Color: [visible colors]
```

Use this format for `custom.quick_specs`:
```
[Material] • [Feature] • [Widths] • [Fit] • [Profile] • [Engraving]
```

Example:
```
Tungsten Carbide • Real Dinosaur Bone Inlay • 4mm/8mm • Comfort Fit • Beveled Edges • Inside Engraving
```

## 4. Product FAQ

FAQ must be **product/material-specific only**. Do not include generic policy questions.

**Required 6 questions:**

1. What is [CODENAME] made of?
2. Is [material] good for daily wear?
3. What does the [inlay/feature] look like?
4. Can [CODENAME] be engraved?
5. Is it comfort fit?
6. How do I care for a [material] ring with [feature]?

**Exclude:**
- Warranty
- Returns
- Shipping
- Sizing/exchanges
- General engraving process
- Custom order policy

Those are handled by global PDP accordions.

## 5. FAQ schema

The structured FAQ schema must match the visible `custom.custom_faq` exactly.

Do not leave old generic FAQ schema in place.

## 6. SEO fields

Every listing needs:

- Product title
- Meta title
- Meta description
- Image alt text
- Quick Specs/keywords
- Product-specific FAQ
- FAQ schema

Meta descriptions may mention:
"Aydins Lifetime Warranty. See policy page for terms."

**Never use bare "lifetime warranty."**

## 7. Category/taxonomy metafields

Set these correctly for Google SEO:

- Color
- Ring size
- Jewelry material
- Age group
- Jewelry type
- Ring design
- Target gender
- Ring Size Chart
- Gemstone type / Stone shape only when truthful and valid

Do not fake unavailable taxonomy values.

## 8. Material information page metafield

Select the correct material info page.

Examples:
- Ceramic products -> `custom.ceramic_ring_information`
- Tungsten products -> tungsten ring information metafield if available
- Titanium/Damascus/etc. -> correct equivalent material page

## 9. Tags

Apply locked Aydins Shopify ring tags:

- Offered widths: `6mm`, `8mm`, etc.
- Engraving: `Inside` or `Inside & Outside`
- Material collection: `Ceramic Rings`, `Tungsten Rings`, etc.
- Visible colors: `Black`, `Blue`, `Orange`, `Green`, etc.
- Feature/inlay tags: `Lava Rock`, `Carbon Fiber`, `Dinosaur Bone`, `Wood`, `Opal`, `Meteorite`, etc.

Tags must match actual product facts.

## 10. Variants, SKUs, inventory

For all vendor-sourced ring listings (Universal Jewelry and Jewelry Depot):

- Variants must match vendor/source exactly.
- Do not invent sizes or widths.
- **Inventory quantity:** `10` per variant.
- **Inventory policy:** continue selling when out of stock (`CONTINUE`).
- **Inventory tracking:** ON (`tracked: true`) on every variant.

### SKU format depends on vendor source

Aydins sources rings from two different vendors. Each has its own SKU convention. Use the right one based on the source.

#### Universal Jewelry rings (universal-jewelry.com source)

- **SKU format:** `CODENAME-WIDTH-SIZE`
- **Examples:** `VESUVIUS-6-5`, `CREDO-6-9`, `FLETCHER-8-10.5`
- Codename in ALL CAPS, then width in mm (no "mm" suffix), then size.
- Vendor field on Shopify: `Universal J` (or the existing vendor value, leave as-is per CLAUDE.md rule).

#### Jewelry Depot rings (Jewelry Depot source)

- **SKU format:** `JDTR{NUMBER}-{WIDTH}-{SIZE}`
- **Examples:** `JDTR901-8-7`, `JDTR902-6-5`, `JDTR213-6-5`, `JDTR164-8-5.5`
- `JDTR` prefix is literal. `{NUMBER}` is the Jewelry Depot product number (e.g. 901, 902, 213, 164). Each width gets its own JDTR number even within the same Aydins product (e.g. IMPRINT 8mm = JDTR901, IMPRINT 6mm = JDTR902).
- Width in mm (no "mm" suffix), then size.
- Vendor field on Shopify: leave as-is (often `Aydins Creations` for custom Jewelry Depot products like fingerprint-engraved rings; or other existing value). Do not change vendor.

### How to identify the source

- If the ring SKU starts with `JDTR`, it is a Jewelry Depot ring.
- If the ring source page is `universal-jewelry.com`, use the Universal Jewelry SKU format.
- If unclear, default to checking the existing live SKU pattern on the same Aydins product. Do not mix conventions on a single product.

### Variant restructure rules

- Do not delete variants unless source verification, snapshot, rollback coverage, and approval/scope exist.
- When a product has multiple widths, both `Width` and `Size` are Shopify option dimensions. Option order: `Width` first, then `Size`.
- Width values displayed natural order (smallest first, e.g. `6mm, 8mm`).
- Size values displayed natural numeric order (e.g. `5, 5.5, 6, 6.5, ..., 14, 15`).
- Custom-engraved products (e.g. fingerprint, personalized text) may have vendor `Aydins Creations` and ship under Aydins manufacturing/engraving even if the ring blank is sourced from a vendor.

## 11. Image alt text

Every image needs truthful alt text with:
- Product codename/name
- Material/product type
- Key feature
- View/angle only if known

Do not invent scenes like "on hand," "velvet," "marble," "lifestyle," or "close-up" unless the image/source proves it.

## 12. Hard bans

Do not include:
- Generic warranty/returns/shipping/sizing FAQ in product-specific FAQ
- Duplicate standalone Engraving section
- Supplier or third-party brand names
- Unsupported claims
- Em dash characters
- Bare "lifetime warranty"
- Fake taxonomy/metafield values
- Invented image descriptions

## 13. Verification after writing

After any Shopify write, verify:

- Admin fields
- Live storefront URL
- Rendered description
- Quick Specs
- Product FAQ
- FAQ schema
- Material/category metafields
- Tags
- Variants/SKUs/inventory if in scope
- Snapshot and write-log entry

---

**The VESUVIUS listing is the approved reference model.**
