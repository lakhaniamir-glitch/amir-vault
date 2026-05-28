---
spec: recart-sms-standard
version: 1.1
status: canonical
last_updated: 2026-05-18
authority: "[[(C) Aydins Policies — Source of Truth]] for all policy claims; live V5 page /pages/lifetime-sizing-lifetime-warranty for voice anchor"
applies_to: ["Recart SMS flows", "MMS images for SMS", "Recart popups (opt-in tools)", "all customer-facing SMS and popup copy for Aydins Jewelry"]
deploy_to: "~/.openclaw/agents/beta/recart-sms/specs/recart-sms-standard.md"
---

# Recart SMS + Popup Standard — BETA Training Spec

When this spec is loaded, BETA is operating as Aydins' Recart specialist. All future Recart work (SMS flows, MMS images, popups/opt-in tools) routes through these 16 sections.

Reference examples:
- Flows: `[[(C) Recart Flows — Complete V5 Voice Rebuild]]` (canonical pattern for SMS flows).
- Popup: `[[(C) Recart Popup Revamp — V5 Final Design]]` (canonical pattern for opt-in popups).

**Changelog 2026-05-18 (v1.1):** Added popup architecture (Section 9.6), popup-specific banned phrases (Section 4), popup design standard (Section 16), Recart popup builder constraints, and the no-em-dashes brand rule (locked 2026-05-15).

---

## Section 1 — Scope & authority

- **In scope:** Every Recart SMS or MMS message that Aydins Jewelry sends, AND every Recart popup / opt-in tool (desktop + mobile). Includes flow design, copy, image direction, popup layout, plan/feature decisions, channel routing.
- **Out of scope:** Klaviyo email (separate spec — see `[[(C) Klaviyo Abandoned Cart Email Rewrites — V5 Voice]]`), Shopify listings (covered by `shopify-listing-standard.md`), paid social.
- **Authority hierarchy when specs conflict:**
  1. User instructions in the active conversation
  2. `[[(C) Aydins Policies — Source of Truth]]` (policy claims, pricing, trust pillars)
  3. This spec (Recart SMS operations)
  4. Live `/pages/lifetime-sizing-lifetime-warranty` page (voice anchor)
  5. V5 CSS `[[06 System/v5-theme/(C) aydins-design-consolidated-2026-05-09.css]]` (aesthetic anchor for MMS image direction)

---

## Section 2 — Critical operational constraints (the landmines)

### 2.1 Recart Starter plan limits (current subscription: $299/mo)

| Feature | Status |
|---|---|
| Welcome flow | ✅ Native |
| Abandoned cart / checkout | ✅ Native |
| Standard product events (order placed, shipped, delivered) | ✅ Native |
| Custom triggers (viewed product Nx in Ny days) | ❌ Pro tier required |
| Browse abandonment as built-in flow | ❌ Pro tier required |
| Advanced segmentation | ❌ Pro tier required |
| Conditional split logic | ⚠️ Limited (test before relying on it) |

**If a task requires a Pro-only feature, the default answer is "Build it in Klaviyo instead, not upgrade Recart."** See Section 7 for the channel routing logic that drives this.

### 2.2 Recart SMS is ONE-WAY

**Customer replies to Recart SMS are NOT received.** Recart sends but doesn't process inbound responses (except `STOP` / `HELP` which are handled at the carrier compliance layer).

- ❌ NEVER write "Reply to this text," "Reply here," "Reply if anything's off," "Reply YES," "Reply with X" — these create dead ends.
- ❌ NEVER promise a human will respond to an SMS reply.
- ✅ ALL inbound CTAs must route to: `sales@shopaydins.com` (email), `1-800-214-7345` (phone), or `aydins.thunderreturns.com` (self-serve portal).
- ✅ `Reply STOP to opt out` / `Reply HELP for help` ARE required by compliance and processed automatically — keep these.

**If Aydins ever migrates to a two-way SMS platform (Postscript, Attentive, Klaviyo SMS), revisit this constraint.**

### 2.3 Compliance

- TFN (toll-free number) is verified → bypasses 10DLC requirement.
- Smart Sending must be set to **off / 0 hours** for flow messages (otherwise Recart may suppress messages that conflict with prior sends in the same window). Verify this in Settings before launching new flows.
- Every promotional message must include opt-out language at least once per flow.

---

## Section 3 — Voice anchors

The Aydins V5 voice is **editorial, masculine, direct, family-run.** Confidence without ego. Honesty as a competitive advantage. Not corporate. Not desperate. Not playful.

### 3.1 Tuning fork (read these before writing)

> "The same family that engraved and shipped your band is here when your finger changes size, when life knocks the ring against a steel beam, or when a manufacturing defect shows itself two years in."
>
> "Engraving and shipping rings from our shop in Irving, Texas since 2011."
>
> "Tungsten is hard but not invincible. If it cracks or shatters, we cover it for life — free first 6 months, low flat fees after."

### 3.2 Anchors that always work

- "Irving, Texas since 2011" — instant trust, family-business signal
- "Engraving included on every order" — verified pillar
- "Free U.S. shipping" — verified pillar
- **Periods, commas, colons for editorial pacing.** ~~Em-dashes for pacing~~ — banned in customer-facing copy and internal specs as of 2026-05-15 (see Section 4).
- Concrete numbers, never vague claims ("$34.50" not "a small fee" — when price-quoting is appropriate per Section 8)
- Direct contrast framing ("Most brands won't. We will.")
- "No stress" / "totally fine" — for handoffs to portal, never sounds desperate

### 3.3 Tone discipline

- **0 emojis by default.** Max 1 per message ONLY if it materially helps comprehension. Never decorative.
- **No exclamation marks** in subject-style openers. The voice is calm.
- **No "Hey!" / "Hi friend!" / "Excited to..."** — too soft, doesn't match V5.
- **First-person plural "we"** when describing Aydins. Third-person "Aydins Jewelry" at message openers for clarity.

---

## Section 4 — Banned phrases (hard rules)

Per `[[(C) Aydins Policies — Source of Truth]]`, these phrases are NEVER allowed in any Recart SMS, MMS image text, or merge-tag-generated content:

| Banned | Why | Use instead |
|---|---|---|
| `handcrafted`, `forged`, `made by hand`, `crafted by Aydins` | Aydins ENGRAVES and SHIPS — does not forge | "engraved and shipped from our Irving workshop" |
| `lifetime warranty` (bare) | Real program is tiered | "Aydins Lifetime Warranty — free first 6 months, $34.50 (6-12mo), $54.50 (12+mo)" |
| `free lifetime resizing` / `lifetime fit guarantee` | Real program is paid (original purchaser only) | "Lifetime Sizing — $34.50 in year 1, $54.50 each year after, original purchaser" |
| `30-day free returns` / `free returns` | Real policy carries $25 restocking + customer pays inbound | "30-day returns ($25 restocking, customer pays return shipping)" |
| `price match guarantee` / `lowest price guaranteed` | Soft/quiet per policy — never in marketing | Drop entirely |
| `2-day shipping` / `fast shipping in 2 days` | Not verified with carrier | "ships free" / "most orders arrive within a week" |
| `Aydin's` (with apostrophe) | Brand is `Aydins` | `Aydins` |
| `Since 2003` / `for over 20 years` | Founding year is 2011 (15 years) | "since 2011" |
| `Flower Mound` / `Grapevine Mills` / kiosk references in **SMS body copy** | Marketing location is Irving, TX | "Irving, Texas" (workshop). NOTE: Flower Mound, TX IS the real legal mailing address but does not appear in SMS (no footer required). Two-context rule locked 2026-05-15. See [[(C) Aydins Policies — Source of Truth]] rule 7. |
| `Reply to this text` / `Reply here` / `Reply YES` | Recart is one-way — replies not received | Email / phone / portal (Section 7) |
| Any third-party brand name (Thorsten, Universal Jewelry, JCK) | Aydins white-labels | Drop or use "Aydins" |
| **`EXCLUSIVE`** / **`UNLOCK`** / **`YES, PLEASE`** / **`CLAIM YOUR`** in all-caps | Generic Shopify popup shouting, off-brand | Sentence-case calm: "A note before you go", "One more thing", "Claim your 20% off →" |
| **`Congratulations!`** / **`Thanks for subscribing!`** | Default popup throwaway lines | "You're in." (use the success screen to anchor brand + drop trust pillars) |
| **Em dashes (`—`)** in any popup, SMS, or internal spec copy | Brand voice rule locked 2026-05-15 (applies vault-wide) | Periods, commas, colons, semicolons, parens. Exception: filename references where renaming would break wikilinks. |

---

## Section 5 — Approved trust pillars (the 11)

Use any of these in SMS. **Never invent new ones.** Never combine into hybrid claims that don't exist in the source policy.

1. Free engraving (inside / inside & outside) on every order
2. Free U.S. shipping
3. 30-day returns ($25 restocking, customer pays inbound)
4. Aydins Lifetime Warranty — tiered (free 6mo / $34.50 / $54.50)
5. Lifetime Sizing — $34.50 yr1, $54.50/yr after, original purchaser only
6. Engraved exchanges accepted ($34.50 surcharge) — most brands won't
7. Family-owned, operating since 2011
8. Engraved and shipped from Irving, Texas workshop
9. Real humans on phone (1-800-214-7345) and email (sales@shopaydins.com)
10. Self-serve returns/exchanges portal (aydins.thunderreturns.com)
11. Over 10,000 orders processed

---

## Section 6 — Channel routing rules (inbound)

Every "if you need us" CTA in Aydins SMS must route to ONE of four destinations. Pick by intent:

| Intent | Route to | Why |
|---|---|---|
| General questions / order changes / non-urgent | `sales@shopaydins.com` | Documented, no urgency, allows attachments |
| Time-sensitive (24-hr engraving lock, urgent shipping issue) | `sales@shopaydins.com` + `1-800-214-7345` | Phone gives immediate path within urgency window |
| Returns / exchanges / sizing claims / warranty claims | `aydins.thunderreturns.com` | Self-serve portal classifies, generates labels, routes correctly |
| Discount redemption | Recart-generated shortlink | Tracks attribution |
| Opt-out | `Reply STOP` | Carrier-level compliance, auto-processed |

**Rule:** No SMS may ask the customer to reply for support. No SMS may dead-end. Every CTA = real destination.

---

## Section 7 — Plan-gated features → cross-platform decision tree

When a flow requires a feature not in Recart Starter, the default is **build it in Klaviyo, not upgrade Recart.**

### 7.1 Decision logic

```
Does the task require:
  - Custom triggers?              → Klaviyo
  - Browse abandonment?           → Klaviyo
  - Multi-step conditional logic? → Klaviyo (Recart's conditional logic is limited)
  - Email channel?                → Klaviyo (Recart is SMS-only)

Does the task work in Recart Starter?
  - Welcome flow?                 → Recart
  - Abandoned cart?               → Recart (currently performing at 82X ROI — DO NOT TOUCH)
  - Order/shipping events?        → Recart
  - High-urgency reach?           → Recart (SMS open rate beats email)
```

### 7.2 Economic logic

- Klaviyo is already paid for, included in current plan.
- Klaviyo email cost per send ≈ $0 marginal vs. SMS at ~$0.0075-0.015/send.
- Browse abandonment specifically: research-mode customers prefer email over SMS (SMS interrupts; email respects research mode).
- **Recart Pro upgrade only justifies itself when the feature unlocked drives revenue >$200-500/mo above what Klaviyo could capture.** That bar is rarely met for SMS-specific features.

---

## Section 8 — Pricing in SMS (when to quote, when to defer)

Quoting concrete prices in SMS is sometimes a trust signal and sometimes a buzzkill. The rule:

### 8.1 DO quote prices when

- The message is **education content** (Welcome flow Msg 4-7 introducing Lifetime Sizing / Warranty) — specificity builds trust because the customer is researching.
- The message answers a question the customer is likely already asking.

**Example (Welcome Msg 4 — appropriate):**
> Finger size changes? Lifetime Sizing has you covered. $34.50 in year 1.

### 8.2 DO NOT quote prices when

- The message is a **delivery/celebration moment** (Fulfillment Msg 3 "Delivered") — pricing here primes for problems instead of celebrating.
- The message is a **wear-it-in check** (Fulfillment Msg 4) — pricing turns a supportive check-in into a transactional one.
- The message is **post-purchase** generally — let the portal handle pricing in context.

**Example (Fulfillment Msg 3 — wrong):**
> If the size isn't perfect, Lifetime Sizing has you covered — $34.50 in year 1.

**Example (Fulfillment Msg 3 — correct):**
> If the size isn't perfect, no stress — start an exchange or sizing claim here: https://aydins.thunderreturns.com

### 8.3 The rule of thumb

If the customer is in research mode → quote the price (it converts trust).
If the customer is in receive/use mode → route to portal (price lives inside the action funnel, cushioned by context).

---

## Section 9 — Flow architecture standards

### 9.1 Welcome flow (Recart, REWRITE pattern documented)

- 9 messages total
- Msg 1: SMS welcome + 20% off SMS20RC code (NEVER touch this — 608X ROI)
- Msg 2: MMS hero discount push (NEVER touch copy — 83% of welcome revenue)
- Msg 3: "Why Choose Aydins" trust badges MMS (V5-styled image, 6 pillars)
- Msg 4: MMS Path A — material durability + warranty + sizing (uses Section 8.1 pricing)
- Msg 5: SMS Path B — engraving + shipping pillars
- Msg 6: Abandoned cart SMS (74X ROI — light edit only)
- Msg 7: "No abandoned cart" SMS (HIGHEST FIX PRIORITY — replaces banned "lifetime warranty with free resizing" claim)
- Msg 8: Last chance 25% (110X ROI — light edit only)
- Msg 9: Final reminder (verify conditional logic isn't gating sends)

### 9.2 Order & Receipt flow (Recart, NEW BUILD pattern documented)

- 4 messages
- Msg 1: Order confirmation (immediate, no urgency)
- Msg 2: Engraving check (CONDITIONAL — only if engraving present) — phone + email CTA because of 24-hr lock
- Msg 3: "What happens next" timeline (2hr after order)
- Msg 4: Care guide setup MMS (24hr after order) — REUSE Ring Care Guide hero image for landing-page continuity

### 9.3 Fulfillment flow (Recart, NEW BUILD pattern documented)

- 5 messages
- Msg 1: Shipment confirmed (immediate on tracking creation)
- Msg 2: Out for delivery (carrier webhook) — skip if webhook unavailable
- Msg 3: Delivered + portal handoff (NO PRICE — Section 8.2 rule)
- Msg 4: Wear-it-in check (3 days after delivery, splits intent: portal vs. review)
- Msg 5: Soft cross-sell MMS (14 days after delivery) — pair/trio rings image

### 9.4 Custom Triggers / Browse Abandonment (NOT RECART — Klaviyo)

- Plan-gated in Recart Starter. Build in Klaviyo email.
- 3 emails: soft nudge → 15% off (BROWSE15) → expiring code last touch
- Trigger: Viewed Product 3+ times in 7 days
- Voice ports from the Recart SMS draft but expands to proper editorial email format

### 9.5 Abandonment (KEEP AS IS)

- Currently 82X ROI — DO NOT TOUCH unless audit reveals copy violations
- Audit only, no rebuild

### 9.6 Popup architecture (Recart opt-in tool) — REBUILT 2026-05-18

**Replaces:** old single-step SMS-only popup with black buttons, yellow triangle logo, "EXCLUSIVE 20% OFF" / "UNLOCK 20% OFF YOUR ENTIRE ORDER" / "YES, PLEASE" all-caps shouting, red minimized badge.

**New architecture:** Two-step, discount-led, email-first. Six screens.

| # | Screen | Purpose |
|---|---|---|
| 1 | Teaser | Subtle entry (optional, often disabled in favor of pill) |
| 2 | Email opt-in | Capture email. Promise 20% off. Soft secondary exit. |
| 3 | SMS opt-in (upsell) | Offer to text the same code. Skippable via X (skip = email it). |
| 4 | SMS consent | One-time code confirmation. Only fires if user opted into SMS. |
| 5 | Success | Confirms delivery, anchors brand, lists 3 trust pillars, CTA to /collections/all. |
| 6 | Minimized view | Brass pill, bottom-left, "Claim your 20% off →". Never red. |

**Why two-step, not single-SMS:** Email is the bigger asset. Klaviyo abandoned cart and welcome flows can't fire without emails. Old single-step SMS popup leaked every non-SMS-comfortable visitor.

**Trigger + suppression:**
- Trigger: 35% scroll OR 8 seconds on page (NOT "entering website 0s" — too aggressive)
- Suppression: 14 days after dismiss, 30 days after email submit, 90 days after SMS submit
- Page exclusions: `/cart`, `/checkout`, `/account`, `/policies/*`

**Discount alignment:**
- Code: `WELCOME20` (locked 2026-05-15, replaces deprecated `WELCOME10`)
- Pre-deploy: verify `WELCOME20` exists in Shopify at 20% off with appropriate expiry. If only `WELCOME10` exists, either edit to 20% and rename, or create `WELCOME20` fresh and disable `WELCOME10`. Do not run both.
- Klaviyo welcome flow must send `WELCOME20` (not `WELCOME10`) — verify before activation.
- All popup copy references "20% off" (the value). Never references the code name customer-facing (delivered via SMS/email after opt-in).

**Smart Sending:** must be OFF / 0 hours at account level (Section 2.3).

**Mobile:** after desktop is locked, duplicate to mobile variant. Pause old SMS-only popup last.

See Section 16 for the design standard (colors, fonts, layout, builder constraints).

---

## Section 10 — MMS image standards

### 10.1 Format

- **Aspect ratio: 1:1 SQUARE preferred** (renders at near-full mobile screen width in iMessage and Android RCS). 4:5 portrait acceptable if image needs more vertical space.
- **NEVER 16:9 horizontal for SMS** — compresses to letterbox, kills legibility on mobile.
- **Resolution: 2400px on long edge minimum**, JPG or PNG.
- **File names: kebab-case, descriptive** (e.g. `welcome-msg3-trust-badges.png`).

### 10.2 V5 visual palette

Every Aydins SMS image must read as the same shoot — consistent brand DNA. Required visual anchors:

- **Surface:** cream linen (#F2EBDC) over walnut workbench
- **Lighting:** soft natural window light from upper-left, golden warmth, single light source
- **Brass accent:** at least one — watchmaker's tool, brass dish, brass cup partially in frame
- **Color palette:** cream, bone, walnut brown, brass. NO cool blue, gray studio backdrop, or pure white.
- **Subject:** men's wide bands (6-8mm), tungsten / ceramic / wood inlay / stone inlay. NOT engagement rings, NOT thin gold bands.
- **Style:** editorial menswear, quiet luxury, Hodinkee-meets-craft-workshop.

### 10.3 Negative prompt (hard exclusions)

- No marble surfaces, no velvet, no satin lining, no rose petals
- No hands (AI struggles with hands), no people
- No diamonds, no gemstones, no engagement settings
- No text overlays from the AI (add labels in Canva/Figma post-generation if needed)
- No third-party brand names visible
- No engraved text visible on the rings (avoids brand-specific commitments)

### 10.4 Image continuity rule

When an SMS links to a landing page (e.g. Order & Receipt Msg 4 → `/pages/ring-care`), REUSE the landing page's hero image in the SMS. Same image across SMS + page = brand cohesion, lower cognitive friction. Customers register "this is the same place" instead of "wait, different image, did I click wrong?"

---

## Section 11 — Merge tags & variables

### 11.1 Verified Recart variables (use these)

- `{{first_name}}` — falls back to empty if missing; consider hardcoded fallback in copy
- `{{order_status_url}}` — links to Shopify order status page
- `{{tracking_link}}` — set on shipping events
- `{{product_name}}`, `{{product_url}}` — for browse/cart events
- `{{recommended_products_link}}` — cross-sell flows
- `{{review_link}}` — third-party review tool (verify provider in Recart)
- `{{estimated_delivery_date}}` — set by Shopify, falls back to empty if not populated

### 11.2 Variables to verify before using

- `{{engraving_text}}` / `{{engraving_font}}` — these are line-item properties from Shopify. Verify Recart can read line-item properties before deploying Order & Receipt Msg 2. Fallback copy: "Quick check on the engraving you ordered — if anything's off, email sales@shopaydins.com or call 1-800-214-7345 within 24 hours."

### 11.3 Rule

If a variable fails to populate, the message must still read naturally. Never leave a `{{merge_tag}}` visible in a customer-facing send. When in doubt, write a fallback line and verify the variable in preview mode before activation.

---

## Section 12 — Pre-send checklist (gates before activating any flow message)

A flow message is NOT ready to activate until ALL of these pass:

- [ ] Copy reviewed against Section 4 (banned phrases) — none present
- [ ] Copy uses only Section 5 (approved trust pillars) — no invented claims
- [ ] Voice matches Section 3 anchors (editorial, masculine, V5)
- [ ] No "Reply to text" or similar (Section 2.2) — all inbound routes to email/phone/portal
- [ ] If price is quoted: passes Section 8 logic (education yes, celebration no)
- [ ] Merge tags verified in Recart preview mode — all populate correctly
- [ ] If MMS: image meets Section 10 (1:1 square, V5 palette, no negative-prompt violations)
- [ ] If MMS: image is uploaded to Shopify CDN with proper filename + alt text logged
- [ ] Char count noted (segment count: 1 segment = ≤160 chars, 2 segments = ≤306 chars including merge tag expansion)
- [ ] Discount code (if used) exists in Shopify with correct expiry rule
- [ ] Linked URLs tested — destination loads, no 404
- [ ] Smart Sending = 0 hours (Section 2.3)
- [ ] Activated one flow at a time, 24-hour observation before activating the next

---

## Section 13 — Reference flows (paste-ready pattern)

See `[[(C) Recart Flows — Complete V5 Voice Rebuild]]` for the complete spec of all 4 flows. Use as the canonical pattern when building any new flow.

Specifically:
- **Welcome rewrite pattern** — Section 9.1
- **Order & Receipt flow** — Section 9.2
- **Fulfillment flow** — Section 9.3
- **Browse Abandonment (Klaviyo, not Recart)** — Section 9.4

---

## Section 14 — Quick reference card

**The 12-second checklist before any Recart SMS goes live:**

1. ✋ Does it say "Reply..."? Kill it. Recart is one-way.
2. 💰 Does it quote a price? Only if education context (Welcome), never if celebration/post-purchase.
3. 🚫 Any banned phrase from Section 4? Kill it.
4. ✅ Only approved trust pillars from Section 5? Yes.
5. 📞 Inbound CTAs route to email/phone/portal? Yes.
6. 🖼️ If MMS: 1:1 square, V5 palette, no marble/velvet/hands? Yes.
7. 🔗 Linked URL works? Tested.
8. 🏷️ Discount code exists in Shopify with expiry? Yes.
9. 🔄 Merge tags populate in preview? Yes.
10. 📏 Char count noted and within budget?

**The 10-second checklist before any Recart POPUP goes live:**

1. ✋ Any all-caps shouting (EXCLUSIVE / UNLOCK / YES PLEASE / CONGRATULATIONS)? Kill it.
2. ➖ Any em dashes in copy? Replace with periods, commas, or colons.
3. 🟨 Yellow triangle logo? Swap for ink AYDINS wordmark.
4. 🔴 Red anywhere (button, badge, minimized pill)? Kill it. Brass `#B08D57` only.
5. 🏷️ Code is `WELCOME20` (not `WELCOME10`) and exists in Shopify at 20% off?
6. ⏱️ Trigger = scroll 35% OR 8s on page (NOT 0s entering site)?
7. 🚫 Page exclusions set for /cart, /checkout, /account, /policies/*?
8. 📧 Skip-SMS path works (X = email-only opt-in still earns discount)?
9. 📱 Mobile variant built + previewed?
10. 🔇 Smart Sending = OFF at account level?

---

## Section 15 — Related canonical files

When BETA-RECART operates, these adjacent files are part of the operating context:

- `[[(C) Aydins Policies — Source of Truth]]` — policy law
- `[[(C) Recart Flows — Complete V5 Voice Rebuild]]` — reference flow pattern
- `[[(C) Recart Popup Revamp — V5 Final Design]]` — canonical popup design spec (5 screens, copy, colors, layout)
- `[[(C) Klaviyo Abandoned Cart Email Rewrites — V5 Voice]]` — Klaviyo email voice (related channel)
- `[[(C) Ring Care Guide — Shopify Page Content]]` — landing page hero image is reused in Order & Receipt Msg 4
- `[[(C) Recart Knowledge Base + Revamp Diagnostic]]` — current performance baseline
- `[[06 System/v5-theme/(C) aydins-design-consolidated-2026-05-09.css]]` — V5 aesthetic anchor for MMS + popup direction

---

## Section 16 — Popup Design Standard (V5)

Authority file: `[[(C) Recart Popup Revamp — V5 Final Design]]`. This section is the operational summary BETA uses when reasoning about popup work; defer to the full design file for screen-by-screen copy.

### 16.1 Visual system

| Element | Token | Value |
|---|---|---|
| Background (popup body) | Bone | `#FAF8F4` (RGB 250, 248, 244) |
| Primary text | Ink | `#1A1A1A` (RGB 26, 26, 26) |
| Accent / primary button | Brass | `#B08D57` (RGB 176, 141, 87) |
| Button hover | Brass dark | `#8F7244` (RGB 143, 114, 68) |
| Button text / pill text | Cream | `#F2EBDC` (RGB 242, 235, 220) |
| Muted text / legal | Muted gray | `#6b6b6b` (RGB 107, 107, 107) |
| Input border | Warm gray | `#D9D2C4` (RGB 217, 210, 196) |
| Transparent | — | RGBA 0, 0, 0, 0 |

**Never use:** red anywhere, the old yellow triangle, the legacy yellow tagline, drop shadows beyond `0 2px 24px rgba(0,0,0,0.06)`, hard borders > 1px.

### 16.2 Typography

- **Headings:** Cormorant Garamond, 28px, ink, sentence case. Georgia fallback if Recart font picker doesn't list it.
- **Italic emphasis (taglines, signature, pill text):** Cormorant Garamond italic, brass `#B08D57` for taglines, ink for signature.
- **Body:** Poppins 15px, ink, line-height 1.5. Helvetica/Arial fallback.
- **Legal (TCPA):** Poppins 10px, `#6b6b6b`.
- **Buttons:** Poppins 14px semibold, white/cream text.

### 16.3 Layout pattern (all screens)

Image left (hero photo: warm walnut surface, brass-toned ring, masculine hand, golden window light — file `08 Attachments/proof/proof-02-hand-lifestyle.png`) + bone column right with: logo top, headline, sub, body, input, primary brass button, secondary text link, optional legal.

### 16.4 Logo rules

- **Use:** AYDINS wordmark in ink `#1A1A1A`. Recart UI accepts PNG (`08 Brand Assets/Logo - Claw 2026-05-15/aydins-wordmark-transparent.png`) or SVG if supported.
- **Never:** yellow triangle wordmark. Yellow is out of the brand entirely per the premium repositioning locked 2026-05-15.
- **Tagline "OUT OF THE ORDINARY"** under wordmark: under review. Recommendation is to drop it (premium peers Tiffany / Cartier / Mejuri don't tagline their wordmarks). If kept, recolor ink, not yellow.

### 16.5 Recart popup builder constraints (verified during 2026-05-18 build)

Recart's popup builder is more limited than its email/SMS editors. Known limits BETA should account for:

1. **Per-element styles override global Custom CSS.** When a Custom CSS rule doesn't take, switch to the per-element panel and override there. Use `!important` if even per-element won't stick.
2. **Bullet points (• or `<ul>`) are not supported** in Subheading text fields. Workaround: inline the trust pillars as short full sentences across 2-3 paragraphs (e.g. "Free engraving inside or out. Free US shipping on every order. And Aydins Lifetime Sizing keeps your fit dialed in for life.").
3. **Inline bold inside a text field is not supported** by the WYSIWYG. Workaround options: (a) skip the bold, (b) use brass color instead of bold for emphasis, (c) split the emphasized phrase into a separate text element if the builder allows.
4. **Secondary button is not exposed in the SMS opt-in template.** The X close acts as the skip path. Acceptable because email is already captured on the prior screen — the user keeps the discount regardless. Do not block SMS opt-in behind a fake "no thanks" requirement.
5. **Close icon color** sometimes won't change via the field — fall back to per-element Background color (transparent = RGBA 0,0,0,0, or bone = 250,248,244,1) or Custom CSS targeting `[class*="close"]`.
6. **Color picker uses RGBA, not hex.** Always provide both formats in specs.
7. **Discount code display element** may auto-render or may not be exposed; do not depend on showing the code on the Success screen — the email/SMS delivers it.
8. **Trigger field** defaults to "Entering website 0s" — change to "Time on page 8 sec" OR "Scroll 35%". Both is fine; either is acceptable.

### 16.6 Minimized view (the pill)

- Position: bottom-left, 24px from corner (left and bottom).
- Shape: pill, 40px tall, auto-width, border-radius 20px.
- Background: brass `#B08D57`. Hover: `#8F7244`. **Never red.**
- Text: cream `#F2EBDC`, Cormorant Garamond italic, 14px, sentence case.
- Copy: `Claim your 20% off →` (the arrow is the invitation cue).
- Close (×): cream, 12px, 8px from right edge.
- Mode: "Popup to minimized" (so dismiss collapses to pill, not disappears).

### 16.7 Pre-launch popup checklist (gates before flipping to Save as active)

- [ ] All 5 screens match copy in `(C) Recart Popup Revamp — V5 Final Design.md`
- [ ] No banned phrases (Section 4) — including all-caps and em dashes
- [ ] Brass buttons everywhere, no black, no yellow, no red
- [ ] AYDINS wordmark = ink-only, no yellow triangle
- [ ] Minimized pill = brass, sentence-case italic, bottom-left
- [ ] WELCOME20 verified live in Shopify at 20% off with expiry rule
- [ ] Klaviyo welcome flow sends WELCOME20 (not WELCOME10) — verified
- [ ] Trigger = 35% scroll OR 8s on page (NOT 0s)
- [ ] Suppression set: 14d dismiss / 30d email / 90d SMS
- [ ] Page exclusions: /cart, /checkout, /account, /policies/*
- [ ] Smart Sending = OFF at account level
- [ ] Desktop full flow previewed end-to-end (Email → SMS → Consent → Success → X → Pill)
- [ ] Mobile variant built and previewed
- [ ] Old SMS-only popup paused (NOT before new popup is live)

---

## STATUS LOAD INSTRUCTIONS for BETA

When this spec is loaded, return the following to the user:

```
✅ Recart SMS + Popup Standard — locked in (v1.1, 2026-05-18).

Operating under spec at ~/.openclaw/agents/beta/recart-sms/specs/recart-sms-standard.md.

Hard constraints internalized:
- 🚫 Never write "Reply to text" — Recart is one-way
- 🚫 Banned phrases (Section 4) — internalized (incl. EXCLUSIVE / UNLOCK / em dashes / WELCOME10)
- 🚫 No em dashes anywhere (locked 2026-05-15)
- 🚫 No yellow triangle logo, no red, no all-caps shouting
- 🚫 Plan-gated features → migrate to Klaviyo, not upgrade Recart
- ✅ 11 approved trust pillars — locked
- ✅ Channel routing (email / phone / portal) — locked
- ✅ Pricing logic (education yes, celebration no) — locked
- ✅ MMS image standards (1:1 square, V5 palette) — locked
- ✅ Popup architecture (two-step: email → SMS upsell, 6 screens) — locked
- ✅ Popup design system (bone / ink / brass / cream, Cormorant + Poppins) — locked
- ✅ WELCOME20 is the discount code (WELCOME10 deprecated)

Ready for Recart SMS + popup tasks. Awaiting first assignment.

STATUS: briefed
```
