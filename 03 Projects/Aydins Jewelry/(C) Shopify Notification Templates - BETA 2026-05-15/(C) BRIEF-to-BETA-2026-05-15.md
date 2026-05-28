# Shopify Notification Templates: Rebuild + Continue Build

> **Handoff date:** 2026-05-15
> **From:** Claudian (vault-side Claude)
> **To:** BETA (OpenClaw orchestrator)
> **Re:** First two notification templates need a rebuild before continuing. Approved direction below.

---

## Status

Reviewed your first 2 templates (`aydins-order-confirmation-shopify.html`, `aydins-shipping-confirmation-shopify.html`) and the shared footer file. Amir approved the voice and structure. **Not approved as-shipped** because of 3 brand-rule violations and a footer-architecture change. Rebuild both, then continue with the rest of the transactional set.

---

## Canonical sources to read first

1. **`(C) Aydins Policies — Source of Truth.md`** (vault). Locked policy wording. Rule 7 was expanded 2026-05-15 with the two-context location rule. Read rule 7.
2. **`KLAVIYO-EMAIL-STANDARD.md`** (workspace). Updated 2026-05-15 with the WELCOME20 lock and the Flower Mound two-context exception.
3. **`(C) Shopify Notification Templates - BETA 2026-05-15/README.md`** (vault). My full review of your first pass.

If any of those conflict, **Policies (#1) wins.**

---

## Fixes to apply on the rebuild

### 1. Banned phrase: "Lifetime warranty"

Appears in the topbar trust line and the footer trust line on both templates and in the shared footer file. Bare-word "lifetime warranty" is banned per Policies rule 1-2: Aydins's real program is tiered (free 0-6mo, $34.50 6-12mo, $54.50 12+mo).

**Substitute** "Lifetime warranty" → **"Aydins Lifetime Warranty"** (named program) in all trust lines. Keeps the program framing without policy-detail bloat in a transactional email.

**Locations to fix:**
- `aydins-order-confirmation-shopify.html`: topbar line, footer trust line
- `aydins-shipping-confirmation-shopify.html`: topbar line, footer trust line
- `aydins-footer-shopify-new-design.html`: trust line

### 2. Em dashes (5 instances across the two templates)

Brand rule locked 2026-05-15: no em dashes in any Aydins copy. Substitutions:

| File | Line | Current | Replace with |
|---|---|---|---|
| order-confirmation | `<title>` | `Order confirmed — {{ shop.name }}` | `Order confirmed: {{ shop.name }}` |
| order-confirmation | totals row | `Discount — {{ discount_application.title }}` | `Discount: {{ discount_application.title }}` |
| order-confirmation | body | `If anything looks off — size, engraving, shipping address — reply` | `If anything looks off, whether size, engraving, or shipping address, reply` |
| shipping-confirmation | `<title>` | `Your order has shipped — {{ shop.name }}` | `Your order has shipped: {{ shop.name }}` |
| shipping-confirmation | body | `Good news — order {{ order_label }} has left our shop` | `Good news. Order {{ order_label }} has left our shop` |

### 3. Tagline color

Currently `#9a7a45` (gold). V5 brand brass is `#B08D57`. Apply brass to the tagline in both header and footer of both templates plus the shared footer file.

### 4. Footer architecture change (important)

**Embed the footer inline in each template.** Do not deliver a separate shared footer file with the expectation that it gets included. Each template = one self-contained HTML file with footer baked in.

**Footer content** (per the updated `aydins-footer-shopify-new-design.html`):
- AYDINS wordmark (Georgia serif, letter-spacing 5px, ink color)
- Tagline `Wedding Bands, Made Personal` (Poppins, letter-spacing 2px, uppercase, brass `#B08D57`)
- Trust line: `Free engraving · Free U.S. shipping · Aydins Lifetime Warranty · 30-day returns`
- Connect row: `Instagram · TikTok · Pinterest · Facebook` inline, dot-delimited, full width
- Signature line: `Aydins Jewelry · Irving, Texas · Since 2011`
- `SHOPAYDINS.COM` link + copyright line

**Removed 2026-05-15 (Amir's call):** Mailing address column. Transactional Shopify notifications do not require a postal address (CAN-SPAM applies to commercial/marketing messages, not transactional). Keeps the footer clean. The mailing address still goes in Klaviyo marketing email footers and on the Returns & Exchanges page.

### 5. Flower Mound vs Irving (clarification only, no fix needed here)

Locked 2026-05-15 in Policies rule 7. Two contexts:
- **Body copy / brand voice / trust lines** → always Irving, Texas
- **Klaviyo marketing email footers + Returns & Exchanges page** → Flower Mound, TX (PMB), required by CAN-SPAM
- **Shopify transactional notification footers** → NOT required, skip it (this rebuild)
- **SMS** → NOT required, no footer

Do not "fix" the inconsistency in the wrong direction in any future template. Irving in body, Flower Mound only in commercial-marketing-email footers.

---

## Delivery format

- **One `.html` file per Shopify notification template.**
- **Footer embedded inline** in each file. No shared-include approach.
- Drop into `/home/openclaw/.openclaw/agents/beta/shopify/notification-templates/`.
- Keep filenames in the existing pattern: `aydins-<notification-type>-shopify.html`.

---

## Build order

### Phase 1: Rebuild the 2 approved-pattern templates

1. `aydins-order-confirmation-shopify.html` (rebuild with all 4 fixes above)
2. `aydins-shipping-confirmation-shopify.html` (rebuild with all 4 fixes above)

Hand back to Amir for sign-off before Phase 2.

### Phase 2: Post-purchase journey (after Phase 1 approval)

3. `aydins-out-for-delivery-shopify.html`
4. `aydins-shipping-update-shopify.html` (carrier change, address change, delays)
5. `aydins-order-edited-shopify.html`
6. `aydins-order-cancelled-shopify.html`
7. `aydins-order-refund-shopify.html`

### Phase 3: Account management

8. `aydins-customer-welcome-shopify.html`
9. `aydins-customer-activation-shopify.html`
10. `aydins-customer-password-reset-shopify.html`

---

## Open items for BETA to flag back to me if blocked

- If the Shopify Liquid variable names differ from what's in the current 2 templates for any new notification type, surface them and I'll align the copy.
- If the brass `#B08D57` reads too gold on certain mail clients, propose an alternative (`#A07A4A` is a slightly cooler bronze that may render better in dark mode).
- Tagline lockup in the header: keep at the same scale you used on the first 2 templates. Approved.
