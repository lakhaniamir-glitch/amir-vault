# AYDINS-RECART-POPUP-V5.md

Status: Deployable draft for Amir review  
Brand: Aydins Jewelry  
Channel: Recart popup entry point → Recart Welcome SMS flow  
Date: 2026-05-15  
Implementation status: Not implemented. Do not deploy until Amir approves the selected variant and Recart editor build.

---

## Recommended Variant

**Recommend Variant A — discount-led.** The live Recart Welcome flow Msg 1 delivers **WELCOME10 for 10% off with a 7-day expiry**, so the popup should make the same promise cleanly and immediately. Discount-led is the strongest entry-point offer because it matches shopper intent at the moment of hesitation, creates a clear reason to submit, and avoids overloading the popup with policy detail. The V5 trust lines below the form carry the Aydins proof without competing with the offer.

---

## 1. Popup Structure Decision

### Recommended structure

**Two-step popup: email → SMS upsell**

Step 1 captures email first. Step 2 asks for phone with the 10% off SMS delivery promise.

Rationale:

- Lower friction than asking for email + phone in one screen.
- Keeps the visual clean and V5 premium instead of looking like a generic lead form.
- Lets shoppers who only want email submit without abandoning the entire popup.
- Aligns with Recart as the SMS entry point while preserving future Klaviyo welcome/email use.
- The SMS step can make the compliance language visible without crowding the first screen.

### Trigger

**Scroll trigger: 35% page scroll, with an 8-second minimum delay.**

Rationale:

- Works on both mobile and desktop. Exit intent is unreliable on mobile.
- Avoids interrupting the hero immediately.
- Captures shoppers after they have seen enough product/category context to care.
- Better fit for a premium V5 experience than an instant discount blast.

### Desktop sizing

- Modal max width: **520px** image-free, **720px** if using optional split image layout.
- Recommended final build: **520px image-free**.
- Modal background: bone `#FAF8F4`.
- Outer padding: **32px**.
- Border: `1px solid #E5E2DB`.
- Border radius: **2px**.
- Close icon: top-right, 24px hit area minimum, ink `#1A1A1A` at 60% opacity.

### Mobile sizing

- Width: **calc(100vw - 32px)**.
- Max width: **360px**.
- Outer padding: **24px** on screens under 480px.
- Keep fields full width.
- CTA full width.
- Disclaimer visible without horizontal scroll.
- Avoid fixed-height content; allow natural height with safe bottom padding.

### Dismiss behavior

- Dismiss via close icon, backdrop click, or “No thanks” link.
- If dismissed without submit: suppress for **14 days**.
- If Step 1 email is submitted but Step 2 phone is skipped: suppress for **30 days**.
- If full SMS opt-in is completed: suppress for **90 days**.
- Do not show on cart/checkout pages if Recart abandoned cart capture or Shopify checkout overlays are active.
- Do not stack with other campaign popups.

---

## 2. Copy — Three Variants

## Variant A — Discount-led

### Step 1: Email capture

**Headline**  
`10% Off Your <em>Band</em>`

**Subheadline**  
Get WELCOME10 by text after signup. Good for 7 days.

**Email field label**  
Email address

**CTA button text**  
Claim 10%

**Trust pillar lines below form**

- Free U.S. shipping on every order.
- Engraving included on every order.

**No thanks dismiss copy**  
No thanks, I’ll keep browsing

### Step 2: SMS upsell

**Headline**  
`Send My <em>Code</em>`

**Subheadline**  
Enter your phone number and Recart will text WELCOME10 now.

**Phone field label**  
Mobile phone number

**CTA button text**  
Text My Code

**SMS opt-in disclaimer**  
By submitting, you agree to receive automated marketing texts from Aydins Jewelry at the number provided. Consent is not a condition of purchase. Msg frequency approx. 4–6/mo. Msg & data rates may apply. Reply STOP to opt out. See Terms and Privacy Policy.

**Post-submit confirmation message**  
WELCOME10 is on its way. Use it within 7 days on the band you keep coming back to.

**No thanks dismiss copy**  
No thanks, I’ll keep browsing

---

## Variant B — Trust-led

### Step 1: Email capture

**Headline**  
`Engraving Is <em>Included</em>`

**Subheadline**  
Get WELCOME10 by text, plus the details that matter before you choose.

**Email field label**  
Email address

**CTA button text**  
Get The Code

**Trust pillar lines below form**

- Engraving included on every order.
- Engraved exchanges accepted with a $34.50 surcharge — most brands won’t.

**No thanks dismiss copy**  
No thanks, I’ll keep browsing

### Step 2: SMS upsell

**Headline**  
`Text The <em>Code</em>`

**Subheadline**  
Add your phone number and Recart will send WELCOME10 now.

**Phone field label**  
Mobile phone number

**CTA button text**  
Send My Code

**SMS opt-in disclaimer**  
By submitting, you agree to receive automated marketing texts from Aydins Jewelry at the number provided. Consent is not a condition of purchase. Msg frequency approx. 4–6/mo. Msg & data rates may apply. Reply STOP to opt out. See Terms and Privacy Policy.

**Post-submit confirmation message**  
Your WELCOME10 code is on the way. Free engraving is included when you order.

**No thanks dismiss copy**  
No thanks, I’ll keep browsing

---

## Variant C — Story-led

### Step 1: Email capture

**Headline**  
`From <em>Irving</em> Since 2011`

**Subheadline**  
Get WELCOME10 by text from the family-owned shop behind your band.

**Email field label**  
Email address

**CTA button text**  
Start Here

**Trust pillar lines below form**

- Family-owned, operating since 2011.
- Engraved and shipped from our Irving, Texas workshop.

**No thanks dismiss copy**  
No thanks, I’ll keep browsing

### Step 2: SMS upsell

**Headline**  
`Your <em>Code</em> Is Ready`

**Subheadline**  
Enter your phone number and Recart will text WELCOME10 for 10% off.

**Phone field label**  
Mobile phone number

**CTA button text**  
Text My Code

**SMS opt-in disclaimer**  
By submitting, you agree to receive automated marketing texts from Aydins Jewelry at the number provided. Consent is not a condition of purchase. Msg frequency approx. 4–6/mo. Msg & data rates may apply. Reply STOP to opt out. See Terms and Privacy Policy.

**Post-submit confirmation message**  
WELCOME10 is on its way. We’ve been engraving and shipping from Irving, Texas since 2011.

**No thanks dismiss copy**  
No thanks, I’ll keep browsing

---

## 3. Visual Design Spec

### Palette

- Popup background: bone `#FAF8F4`.
- Body text: ink `#1A1A1A`.
- CTA background: brass `#B08D57`.
- CTA text: bone `#FAF8F4` or white if Recart editor requires it.
- Accent italic text: brass `#B08D57`.
- Secondary block background: cream `#F2EBDC`.
- Borders / hairlines: `#E5E2DB`.

### Typography

**Headline**

- Font: Cormorant Garamond.
- Fallback: Georgia, serif.
- Desktop size: 42–48px.
- Mobile size: 34–38px.
- Weight: 500 or 600.
- Line height: 0.95–1.05.
- Key word wrapped in italic brass accent: `<em>`.

**Body / form / disclaimer**

- Font: Poppins.
- Fallback: Helvetica, Arial, sans-serif.
- Subheadline: 15–16px, line-height 1.45.
- Field labels: 12px, uppercase or small caps optional, letter spacing 0.06em.
- Disclaimer: 10.5–11px, line-height 1.45.
- Trust lines: 12–13px, line-height 1.45.

### Spacing

- Outer padding: **32px** desktop.
- Outer padding mobile: **24px**.
- Gap between headline and subheadline: **12px**.
- Gap between subheadline and first field: **24px**.
- Form gap: **24px**.
- CTA padding: **14px 32px**.
- CTA radius: **2px**.
- Trust line block top margin: **18px**.
- Disclaimer top margin: **12px**.
- “No thanks” top margin: **16px**.

### Fields

- Field height: 48–52px.
- Border: `1px solid #E5E2DB`.
- Background: white or bone `#FAF8F4` if contrast is sufficient.
- Text: ink `#1A1A1A`.
- Placeholder: ink at 45% opacity.
- Radius: 2px.

### CTA button

- Background: brass `#B08D57`.
- Text: bone `#FAF8F4`.
- Font: Poppins, 12–13px.
- Letter spacing: 0.08em.
- Text transform: uppercase acceptable.
- Hover desktop: darken brass slightly or invert to ink background with bone text.
- Radius: 2px.

### Image or pattern recommendation

**Recommend image-free for launch.**

Reason:

- Faster load.
- Cleaner mobile rendering.
- Less risk of using imagery that does not match V5.
- Recart popup has limited real estate; the offer, trust lines, and compliance copy matter more.
- Aydins V5 already has strong typography and palette, so it does not need an image to feel branded.

Optional future test:

- Use a narrow right-side desktop image only, hidden on mobile.
- Image direction: single men’s band on cream linen over walnut workbench, soft natural light, brass detail in frame, no hands, no marble, no velvet, no diamonds, no visible third-party branding.

### Layout recommendation

**Image-free layout**

1. Small eyebrow: `Aydins Jewelry`
2. Headline with brass italic accent.
3. Subheadline.
4. Field.
5. Brass CTA.
6. Trust line block on cream background.
7. SMS disclaimer on Step 2.
8. Quiet dismiss link.

### Mobile breakpoint behavior

Breakpoint: **480px**.

Under 480px:

- Modal width: `calc(100vw - 32px)`.
- Padding: 24px.
- Headline max size: 38px.
- CTA full width.
- Keep trust lines to 1–2 lines each.
- Disclaimer remains visible; do not hide compliance text behind accordion.
- Hide optional desktop image if used later.

---

## 4. Pre-Launch QA Checklist

### Copy and compliance

- [ ] Banned phrase audit complete against Recart SMS Standard Section 4.
- [ ] No prohibited manufacturing-origin claims.
- [ ] No prohibited warranty or sizing shortcuts.
- [ ] No prohibited returns or shipping-speed claims.
- [ ] No prohibited price-match language.
- [ ] Brand name spelling is correct everywhere.
- [ ] Founding year and location claims match the canonical spec.
- [ ] No third-party vendor or marketplace names.
- [ ] No customer reply CTA beyond required STOP compliance language.
- [ ] STOP language appears only in required compliance disclaimer.
- [ ] No exclamation marks in headlines.
- [ ] No emoji in headlines.
- [ ] No generic newsletter/update framing.

### Trust pillar verification

- [ ] Trust lines use only approved Recart Section 5 pillars.
- [ ] Free engraving claim uses approved wording: “Engraving included on every order.”
- [ ] Free shipping claim uses approved wording: “Free U.S. shipping.”
- [ ] Family-owned / Irving / since 2011 claims match approved pillars.
- [ ] Engraved exchange claim includes the $34.50 surcharge if mentioned.

### Discount and welcome flow match

- [ ] Popup promise matches live Welcome Msg 1: **WELCOME10, 10% off, 7-day expiry**.
- [ ] WELCOME10 exists in Shopify/Recart with correct 7-day expiry behavior.
- [ ] Post-submit confirmation does not promise anything beyond WELCOME10.
- [ ] If Recart Welcome Msg 1 changes later, popup copy is updated before launch.

### SMS disclaimer

- [ ] Disclaimer includes automated marketing text consent.
- [ ] Disclaimer states consent is not a condition of purchase.
- [ ] Disclaimer states approx. 4–6 messages/month.
- [ ] Disclaimer states message and data rates may apply.
- [ ] Disclaimer includes STOP opt-out language.
- [ ] Terms link points to the actual Aydins terms page.
- [ ] Privacy Policy link points to the actual Aydins privacy page.

### Design QA

- [ ] Palette matches V5: bone, ink, brass, cream, hairline.
- [ ] Headline uses Cormorant Garamond with Georgia fallback.
- [ ] Body uses Poppins with Helvetica/Arial fallback.
- [ ] Brass italic accent appears on the key headline word.
- [ ] CTA uses brass background and 2px radius.
- [ ] Outer padding is 32px desktop / 24px mobile.
- [ ] Form gap is 24px.
- [ ] CTA padding is 14px × 32px.
- [ ] Image-free version loads quickly and does not feel generic.

### Device QA

- [ ] Mobile preview tested at **375px**.
- [ ] Desktop preview tested at **1440px**.
- [ ] Form fields are tappable on mobile.
- [ ] CTA is visible without awkward scrolling on Step 1.
- [ ] Step 2 disclaimer is readable on mobile.
- [ ] Close icon is tappable on mobile.
- [ ] No horizontal scroll.

### Recart trigger and campaign logic

- [ ] Trigger set to 35% scroll with 8-second minimum delay.
- [ ] Suppression after dismiss: 14 days.
- [ ] Suppression after email-only submit: 30 days.
- [ ] Suppression after SMS opt-in: 90 days.
- [ ] Popup does not show on checkout.
- [ ] Popup does not conflict with existing campaign popups.
- [ ] Popup does not stack with cart drawer, Doofinder search overlay, or Recart abandoned cart capture.
- [ ] Existing live Recart Welcome flow receives the SMS opt-in as expected.
- [ ] Test opt-in confirms Msg 1 sends WELCOME10.

---

## Final Build Note

Build **Variant A** first in Recart’s editor using the image-free layout. Keep Variants B and C as later A/B test candidates after the V5 welcome flow has collected enough baseline popup conversion data.
