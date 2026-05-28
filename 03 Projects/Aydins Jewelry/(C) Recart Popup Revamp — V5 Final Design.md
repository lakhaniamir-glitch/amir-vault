# Aydins Recart Popup: V5 Final Design

Last updated: 2026-05-15
Status: Design spec, ready to build in Recart UI
Supersedes: `(C) Recart Popup Revamp — V5 Spec.md` (which referenced a wrong 10%; actual code is **20%**)

---

## Architecture

**Two-step popup, discount-led, email-first.**

- **Step 1 (Email):** Capture email. Promise 20% off. Soft secondary exit.
- **Step 2 (SMS upsell):** Offer to text the same code for faster delivery + early access. Skippable.
- **Step 3 (SMS consent):** Confirmation code entry. Only shown if user opted into SMS.
- **Step 4 (Success):** Confirms, anchors brand, gives next step.
- **Step 5 (Minimized):** Quiet pill, brass, never red.

**Why two-step, not single-SMS:** Email is the bigger asset. Klaviyo abandoned cart and welcome flows can't fire without emails. Current single-step SMS popup leaks every non-SMS-comfortable visitor.

**Trigger / suppression (unchanged from prior spec):**
- Trigger: 35% scroll OR 8s on page
- Suppression: 14 days after dismiss, 30 days after email submit, 90 days after SMS submit
- Suppress on /cart, /checkout, /account

---

## Voice rules

- Sentence case headlines (no shouting)
- Cormorant Garamond italic for emphasis words, colored brass `#B08D57`
- Poppins for body
- No "EXCLUSIVE" / "UNLOCK" / "YES, PLEASE". They read like every other Shopify popup.
- Family-run, Irving Texas, since 2011. Anchored at least once per flow.
- Discount stays the headline number. We lead with value, just say it like adults.
- **No em dashes (—) in customer-facing copy or internal specs.** Use periods, commas, colons, or parens instead. This is a brand voice rule, locked 2026-05-15.

---

## Screen 1: Email capture (was: "Would you like an exclusive discount?")

**Layout:** Image left (rings on hands; keep current photo). Right column: logo top, headline, sub, body, email field, primary button, secondary link.

**Copy:**

> [Aydins serif wordmark]
>
> ## A note before you go.
> *Engraving and shipping rings from Irving, Texas since 2011.*
>
> Drop your email and we'll send you **20% off** your first ring. Free engraving included, always.
>
> [ email field ]
>
> **[ Send me my 20% off ]** ← brass button
>
> No thanks, I'll browse first ← small text link, ink, underline

**Design notes:**
- Headline: Cormorant Garamond, 28px, ink. The italic line below is also Cormorant, 16px, brass.
- Body: Poppins 15px, ink, line-height 1.5. **20% off** is bold (not a different color).
- Button: full-width inside form column, brass `#B08D57`, white text, 14px Poppins semibold, 2px radius, 14×32 padding.
- Secondary link: 13px Poppins, ink, underlined. Sits 12px below button.
- **Logo: AYDINS wordmark in ink `#1A1A1A`, no yellow triangle.** Decision locked 2026-05-15. Yellow is out of the brand entirely (premium repositioning). Upload a clean ink-only logo to Recart before activating. Tagline "OUT OF THE ORDINARY" under the wordmark is under review; recommendation is to drop it (premium jewelry brands don't tagline their wordmarks: Tiffany, Cartier, Mejuri). If keeping the tagline for now, recolor it to ink, not yellow.

---

## Screen 2: SMS upsell (was: "UNLOCK 20% OFF YOUR ENTIRE ORDER")

Only shown after Step 1 email submit. The discount is **already earned**. This step adds SMS, doesn't gate the discount behind it.

**Copy:**

> [Aydins wordmark]
>
> ## One more thing.
>
> Want your **20% off** code texted to you? You'll get it in seconds, plus first looks at new rings before they hit the site.
>
> [ phone input: country selector + number ]
>
> **[ Text me my code ]** ← brass button
>
> Just email it to me ← secondary link (skips SMS, sends code via Klaviyo welcome flow)
>
> ---
> *By signing up via text, you agree to receive recurring automated promotional and personalized marketing text messages (e.g. cart reminders) from Aydins Jewelry at the cell number used when signing up. Consent is not a condition of any purchase. Reply HELP for help and STOP to cancel. Msg frequency varies. Msg & data rates may apply. View our Privacy Policy and Terms of Service.*

**Design notes:**
- Same layout as Step 1, image left.
- TCPA disclaimer in 10px Poppins, `#6b6b6b`, hairline above it.
- "Just email it to me" link is critical. Without it, you'll lose the email-only audience who don't want SMS. They already gave you the email, don't punish them.

---

## Screen 3: SMS consent (was: "CONFIRM YOUR PHONE NUMBER")

**Copy:**

> [Aydins wordmark]
>
> ## Confirm it's you.
>
> We sent a one-time code to **[phone]**. Enter it below.
>
> [ code input ]
>
> **[ Confirm ]** ← brass button
>
> Didn't get it? Resend ← secondary link

**Design notes:** Same shell as Steps 1 and 2. No image change needed; some popups drop the image on this step to focus attention on the code input. Your call.

---

## Screen 4: Success (was: "THANKS FOR SUBSCRIBING!")

This is the most under-used screen in the current build. Use it to anchor the brand and drop trust signals.

**Copy:**

> [Aydins wordmark]
>
> ## You're in.
>
> Your **20% off** code is on its way. Check your phone and inbox. Use it on any ring.
>
> A few things worth knowing:
>
> - **Free engraving** (inside, or inside & outside)
> - **Free US shipping** on every order
> - **Aydins Lifetime Sizing** keeps your fit dialed in
>
> **[ Start shopping ]** ← brass button, links to /collections/all
>
> *The Aydins Family*

**Design notes:**
- Trust bullets: Poppins 14px, brass bullet markers, ink text. Bold the lead noun.
- Signature: Cormorant Garamond italic, 16px, ink, centered.
- Skip the "Save my contact for a faster opt-in" Recart checkbox. It adds clutter and most people ignore it.

---

## Screen 5: Minimized view (was: red "EXCLUSIVE 20% OFF" badge)

The red badge is the single most off-brand element in the current build. Kill it.

**Spec:**
- Position: bottom-left, 24px from corner
- Shape: pill, 40px tall, auto-width
- Background: brass `#B08D57`
- Border: none
- Text: cream `#F2EBDC`, Cormorant Garamond italic, 14px
- Copy: *"Claim your 20% off →"*
- Close (×): cream, 12px, 8px from right edge
- Hover: background darkens to `#8F7244`

---

## What to change inside Recart UI

Right panel settings (the column on the right of your screenshot):

| Setting | Current | New |
|---|---|---|
| Popup appearance | (default) | Background `#FAF8F4`, border-radius 4px, no shadow or subtle 0 2px 24px rgba(0,0,0,0.06) |
| Background | (image only) | Image left, bone column right |
| Close icon | red? | Ink `#1A1A1A`, 14px, top-right with 16px margin |
| Logo | yellow triangle wordmark | **AYDINS wordmark, ink `#1A1A1A`, no yellow.** Use `08 Brand Assets/Logo - Claw 2026-05-15/aydins-wordmark-transparent.png` (Recart UI accepts PNG; if SVG is supported, prefer `aydins-wordmark.svg`). Approved 2026-05-15. |
| Primary button | black + yellow | Brass `#B08D57` background, white text |
| Secondary button | outlined black | Text link, ink, underline, no border |
| Heading | (default) | Cormorant Garamond, 28px, ink, sentence case |
| Body text | (default) | Poppins, 15px, ink, line-height 1.5 |
| Legal text | (default) | Poppins, 10px, `#6b6b6b` |

If Recart's font picker doesn't include Cormorant Garamond, use Georgia as fallback (specified in Klaviyo email spec for the same reason). For Poppins, Helvetica/Arial fallback.

---

## Code/discount alignment

- Welcome discount: **20% off** (locked 2026-05-15)
- Code name: **WELCOME20** (locked 2026-05-15)
- All copy in this spec uses "20% off". Never references the code name to the customer (the code is delivered via SMS/email after opt-in).
- Pre-deploy: confirm `WELCOME20` exists in Shopify as a 20% discount with appropriate expiry rule. If only `WELCOME10` exists, either (a) edit that code to 20% and rename to `WELCOME20`, or (b) create `WELCOME20` fresh and disable `WELCOME10`. Do not run both.

---

## Files this design supersedes / aligns with

- Supersedes: `(C) Recart Popup Revamp — V5 Spec.md` (Claw's recommendation paper, had 10% error)
- Aligns with: `(C) Klaviyo Abandoned Cart Email Rewrites — V5 Voice.md` (same 20% code, same V5 voice)
- Aligns with: `KLAVIYO-EMAIL-STANDARD.md` (server)
- Aligns with: `RECART-SMS-STANDARD.md` (server)

*(Filename references above retain em dashes because they are accurate filenames; renaming those files is a separate decision.)*

---

## Build order

1. Confirm `WELCOME20` exists in Shopify at 20% off with appropriate expiry. If only `WELCOME10` exists, repurpose or replace per "Code/discount alignment" section above.
2. Update copy in Recart UI for all 5 screens per above
3. Update color settings (right panel) per the table above
4. Test on desktop + mobile preview
5. Activate

---

## Brief to Claw (for context after we ship)

After the popup is live, hand Claw this file plus a note: "This is the V5 design pattern Amir used. Future Aydins popups, banners, and on-site overlays follow this same voice and design system. Cormorant italic for emphasis, brass `#B08D57` for action, never red, never all-caps shouting. Two-step capture (email then SMS upsell) is the default architecture unless we have a specific reason otherwise. **No em dashes in any Aydins copy, ever.**"
