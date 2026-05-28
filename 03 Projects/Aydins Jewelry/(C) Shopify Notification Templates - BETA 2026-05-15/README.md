---
created: 2026-05-15
source: BETA (server path /home/openclaw/.openclaw/agents/beta/shopify/notification-templates/)
status: PULLED FOR REVIEW. Not deployed. Not yet approved.
files:
  - aydins-order-confirmation-shopify.html (the Shopify "Order confirmation" template)
  - aydins-shipping-confirmation-shopify.html (the Shopify "Shipping confirmation" template)
  - aydins-footer-shopify-new-design.html (richer shared footer block, NOT yet wired into either template above)
related:
  - "[[03 Projects/Aydins Jewelry/CLAUDE.md]]"
  - "[[03 Projects/Aydins Jewelry/(C) Aydins Policies — Source of Truth]]"
  - "[[03 Projects/Aydins Jewelry/08 Brand Assets/Logo - Claw 2026-05-15/README]]"
---

# Shopify Notification Templates (BETA, 2026-05-15)

BETA's first pass at modernizing the Shopify transactional emails to match the V5 brand. Two templates plus a shared footer block.

## What BETA got right

- Voice: family-run, Irving Texas, since 2011. On-brand.
- Structure: hero, summary panel, "what happens next" three-step, shipping panel, signature.
- Step-number circles render in brand brass `#b08d57`.
- Tagline placement matches your approval (`Wedding Bands, Made Personal` under the wordmark).
- Liquid logic is correct and uses Shopify's notification variables properly. Falls back gracefully when fields are blank.
- Mobile responsive media query at 600px breakpoint.
- 680px max width: within email best-practice range.
- `AYDINS` rendered in Georgia serif as the email-safe fallback for Cormorant Garamond. Correct per V5 spec.

## What needs to change before deploy

### Critical (must fix, brand-rule violations)

1. **"Lifetime warranty" bare phrase** appears in all 3 files. This is a banned phrase per project CLAUDE.md and policies source of truth. Aydins does NOT have a free lifetime warranty. The real program is **Aydins Lifetime Warranty** (named, tiered: free 0-6 months, $34.50 6-12 months, $54.50 12+ months). For a transactional email where space is tight, either:
   - **Replace** "Lifetime warranty" with "Aydins Lifetime Warranty" in the trust line (keeps the named-program framing without the policy detail), OR
   - **Replace** the entire trust line with three items instead of four: "Free engraving · Free U.S. shipping · 30-day returns" and link "Aydins Lifetime Warranty" once near the signature with a link to the program page.

   **Locations to fix:**
   - `aydins-order-confirmation-shopify.html` line 50 (topbar) and line 121 (footer)
   - `aydins-shipping-confirmation-shopify.html` line 50 (topbar) and line 124 (footer)
   - `aydins-footer-shopify-new-design.html` line 20

2. **Em dashes in body copy** violate the locked 2026-05-15 brand rule. Five instances across the two templates:
   - `aydins-order-confirmation-shopify.html`
     - Line 15: `<title>Order confirmed — {{ shop.name }}</title>` → use a colon: `Order confirmed: {{ shop.name }}`
     - Line 90: `Discount — {{ discount_application.title }}` → use a colon: `Discount: {{ discount_application.title }}`
     - Line 115: `If anything looks off — size, engraving, shipping address — reply to this email` → use commas: `If anything looks off, whether size, engraving, or shipping address, reply to this email`
   - `aydins-shipping-confirmation-shopify.html`
     - Line 18: `<title>Your order has shipped — {{ shop.name }}</title>` → use a colon: `Your order has shipped: {{ shop.name }}`
     - Line 59: `Good news — order {{ order_label }} has left our shop` → use a period: `Good news. Order {{ order_label }} has left our shop`
   - Footer file: no em dashes detected. Clean.

### High priority (resolved 2026-05-15)

3. ~~Flower Mound vs Irving, Texas inconsistency~~ → **RESOLVED. Two-context rule locked 2026-05-15.**
   - **Body copy / brand voice / trust lines = Irving, Texas** (workshop). Always.
   - **Legal mailing-address block (footer, Returns page) = 2201 Long Prairie Rd., Suite 107, PMB 308, Flower Mound, TX 75022** (the real PMB address, CAN-SPAM compliant). Always.
   - These are NOT a contradiction. Flower Mound is the PMB where mail and returns are received. Irving is where the work happens.
   - **BETA's footer formatting needs a tiny fix**: change `Suite 107-308` to `Suite 107, PMB 308`. The PMB-explicit format is the canonical company address. Same physical box, more accurate label.
   - Rule documented in [[(C) Aydins Policies — Source of Truth]] rule 7. Both BETA training files (Klaviyo Email Standard, Recart SMS Standard) updated with the exception so BETA does not "fix" the rule incorrectly on future templates.

### Polish (recommend fixing, not blockers)

4. **Tagline color is gold `#9a7a45`, brand brass is `#B08D57`.** Close but not the locked V5 brass. Apply brand brass.
5. **Off-palette background/border tones**:
   - Wrapper background `#f7f3ec` → use V5 bone `#FAF8F4`
   - Container `#fffaf2` → use ivory `#FFFFFF` or stay close to V5 bone
   - Panel background `#f2ede4` → use V5 cream `#F2EBDC`
   - Border `#ded6c9` → use V5 hairline `#E5E2DB`
6. **Button color `#1f1b18` is near-black, brand ink is `#1A1A1A`.** Apply ink.
7. **Body text color `#4c453e` is brown-grey, brand ink is `#1A1A1A`.** Decision: keep the softened brown-grey for readability on cream backgrounds (defensible design choice), OR shift to ink for absolute brand consistency. My recommendation is to keep the softened body text. It reads warmer and matches the transactional tone.

### Shared footer file (`aydins-footer-shopify-new-design.html`) — UPDATED 2026-05-15

This is a **design reference**, not a wired-in include. The richer footer block contains:
- Brand wordmark + tagline
- Trust line (Free engraving · Free U.S. shipping · Lifetime warranty · 30-day returns)
- Inline social links (Instagram · TikTok · Pinterest · Facebook)
- "Aydins Jewelry · Irving, Texas · Since 2011" line
- shopaydins.com + copyright line

**Removed 2026-05-15 (Amir's call):** Mailing address column. Transactional Shopify notification emails do not require a postal address (CAN-SPAM applies to commercial/marketing messages, not transactional). The Connect column now spans full width with inline-delimited social links. The mailing address still belongs in Klaviyo marketing email footers (CAN-SPAM) and on the Returns & Exchanges page. Rule documented in `(C) Aydins Policies — Source of Truth` rule 7.

**Action for BETA:** Treat this file as the canonical footer design. **Embed it inline into each new template** (no shared-file include approach). The current 2 templates use their own simpler inline footers and need to be rebuilt with this richer footer baked in.

## Decision options for BETA next steps

### Direction sent to BETA (locked 2026-05-15)

Rebuild the 2 templates AND deliver the remaining transactional templates with the richer footer **embedded inline** in each file. No shared-file include approach.

Fixes to apply on the rebuild:
1. Replace "Lifetime warranty" → **"Aydins Lifetime Warranty"** in topbar and footer trust lines.
2. Remove all 5 em dashes per the substitutions in "Critical" section above.
3. Brass color fix on the tagline (use `#B08D57` not `#9a7a45`).
4. Footer = use the updated `aydins-footer-shopify-new-design.html` design pattern (mailing address removed, Connect column full-width), embedded inline into each template.
5. Build out the next 5 templates after the 2 rebuilds are approved: out-for-delivery, shipping update, order edited, order cancelled, order refund.

## Remaining Shopify notification templates BETA will likely need to build

Shopify has ~25 customer-facing notification templates. The ones that matter most for Aydins:

1. ✅ Order confirmation (this file)
2. ✅ Shipping confirmation (this file)
3. Out-for-delivery notification
4. Shipping update (carrier change, address change, delays)
5. Order edited
6. Order cancelled
7. Order refund
8. Abandoned checkout (Shopify's built-in, separate from Klaviyo `TrNjjf`)
9. Customer account welcome
10. Customer account activation
11. Customer account password reset
12. Gift card created
13. POS exchange receipt (if Aydins ever does in-person)

Recommend prioritizing #3-#7 next (post-purchase journey), then #9-#11 (account management), then the rest as needed.

## Files in this folder

| File | Purpose |
|---|---|
| `aydins-order-confirmation-shopify.html` | Drops into Shopify Admin → Settings → Notifications → Order confirmation |
| `aydins-shipping-confirmation-shopify.html` | Drops into Shopify Admin → Settings → Notifications → Shipping confirmation |
| `aydins-footer-shopify-new-design.html` | Richer shared footer block. Not yet wired into either template above. |
| `README.md` | This file. |
