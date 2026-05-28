---
status: draft-ready
created: 2026-05-13
supersedes: live abandoned cart emails in flow TrNjjf (Email 1 / Email 2 / Email 3)
flow_id: TrNjjf
flow_name: Abandoned Cart Reminder (Email)
related:
  - "[[(C) Recart Flows — Complete V5 Voice Rebuild]]"
  - "[[(C) Aydins Policies — Source of Truth]]"
  - "[[(C) Ring Care Guide — Shopify Page Content]]"
---

# Klaviyo Abandoned Cart Rewrites: V5 Voice

## Why this matters

The three currently-live Klaviyo abandoned cart emails (flow `TrNjjf`) contain at least two banned/false claims that are actively being sent to thousands of customers a month:

- ❌ **"30-day free returns & exchanges"**: Aydins returns carry a $25 restocking fee and customer pays inbound shipping. Engraved items are not eligible for returns (exchanges only).
- ❌ **"Lifetime fit guarantee & warranty"**: Bare-word "lifetime" warranty/sizing is a policy violation. Real program is **tiered**: Aydins Lifetime Warranty (free 6mo / $34.50 6–12mo / $54.50 12+mo) and Aydins Lifetime Sizing ($34.50 yr1 / $54.50/yr after, original purchaser only).

This is higher exposure than Recart because:
1. Email reaches more sessions than SMS (larger list, higher delivery, archived).
2. Wrong policy claims in email = chargeback ammo and screenshot fuel.
3. Abandoned cart is the highest-intent moment. If the buyer references the email at the support desk, the gap between promise and policy gets messy fast.

Fix this **first**, then the Recart spec.

---

## Voice anchors (V5 system)

Match the live page at `/pages/lifetime-sizing-lifetime-warranty` and the V5 lifetime-sizing CTA block. Defaults below. Do not deviate without a reason.

- **Tone:** confident, calm, family-owned, not pushy. No exclamation marks in subject lines. No "Hey there!" energy.
- **Voice patterns:**
  - "Engraving and shipping rings from our shop in Irving, Texas since 2011."
  - "The Aydins Family"
  - "Built for daily life."
  - "If something happens, we'll take care of it."
- **Banned words/phrases:**
  - "handcrafted", "forged", "made by hand" → Aydins engraves and ships, does not forge
  - "free lifetime resizing" / "lifetime fit guarantee" → use **Aydins Lifetime Sizing program**
  - "lifetime warranty" bare → use **Aydins Lifetime Warranty (tiered)**
  - "30-day free returns" → use **30-day returns ($25 restocking, customer pays inbound)**
  - "free returns" → never
  - "price match guarantee" in marketing → no
  - "2-day shipping" → not until verified with carrier data
  - "Aydin's" (apostrophe) → always "Aydins"
  - "Hey!", "Hi friend!", "exclamation overload" → no
- **Approved trust pillars** (use any of these, never invent new ones):
  1. Free engraving (inside / inside & outside)
  2. Free US shipping
  3. 30-day returns (with restocking)
  4. Aydins Lifetime Warranty (tiered)
  5. Aydins Lifetime Sizing program
  6. Engraved items eligible for exchange
  7. Family-owned since 2011
  8. Engraved and shipped from Irving, Texas
  9. Real humans on phone (1-800-214-7345) and email (sales@shopaydins.com)
  10. Self-serve returns/exchanges portal (aydins.thunderreturns.com)
  11. Over 10,000 orders processed

---

## Klaviyo merge tags (verify in account)

| Use case | Merge tag |
|---|---|
| First name (with fallback) | `{{ first_name|default:'there' }}` |
| Cart items loop | `{% for item in event.extra.line_items %}…{% endfor %}` |
| Item title | `{{ item.product.title }}` |
| Item image | `{{ item.product.images[0]|default:'' }}` |
| Item URL | `{{ item.product.url }}` |
| Cart total | `{{ event.extra.value|floatformat:2 }}` |
| Checkout URL | `{{ event.extra.checkout_url }}` |

If your Klaviyo account uses different field names for the abandoned cart metric, open one of the live emails in the editor → click any merge tag → grab the actual path from the variable picker.

---

# Email 1: sent 1 hour after abandon

**Goal:** Soft nudge. Assume forgot, not rejected. No discount.

**Subject line (A/B test 2):**
- A: `You left something in your cart`
- B: `Still thinking it over?`

**Preview text:** `Your ring is saved. Free engraving included.`

**From name:** `Aydins Jewelry`
**Reply-to:** `sales@shopaydins.com`

---

### Body copy

**Hero headline:**
> Your ring is still in your cart.

**Subheadline:**
> No pressure. We saved it for you. Engraving included if you decide to come back.

**[ Cart Item Block: show product image, title, price ]**

**[ CTA Button ]** `Return to your cart` → `{{ event.extra.checkout_url }}`

---

**Body, short editorial block:**

> A few things worth knowing before you decide:
>
> – **Free engraving** inside the band (or inside & outside). Added to your order at no charge.
> – **Free US shipping** on every order.
> – **Engraved is not a dead end.** Engraved rings are eligible for exchange if the size or style isn't right.
> – **Aydins Lifetime Sizing program** keeps your fit dialed in for as long as you own the ring.
>
> Take your time. The ring will still be here.

---

**Signature block:**

> The Aydins Family
> Engraving and shipping rings from our shop in Irving, Texas since 2011.

**Footer (kept compact):**
- Questions? `sales@shopaydins.com` · `1-800-214-7345`
- Returns & exchanges: `aydins.thunderreturns.com`
- {% unsubscribe %}

---

# Email 2: sent 24 hours after abandon

**Goal:** Address objections. Lead with proof. Still no discount.

**Subject line (A/B test 2):**
- A: `About your cart. A few things to know`
- B: `Sizing, engraving, returns. Answered`

**Preview text:** `What happens if it doesn't fit? Read this before you decide.`

---

### Body copy

**Hero headline:**
> Still on the fence? Here's what happens if it isn't perfect.

**Subheadline:**
> Most ring purchases live or die on three questions. We answer all three below.

**[ Cart Item Block ]**

**[ CTA Button ]** `Finish checking out` → `{{ event.extra.checkout_url }}`

---

**Three-up block (style as cards or a stacked list; match the V5 `.apg-split` pattern in email):**

**1. What if it doesn't fit?**
Send it back through our self-serve portal (`aydins.thunderreturns.com`). Engraved or not, we'll get you into the right size. Sizing is covered under our **Aydins Lifetime Sizing program** ($34.50 the first year, $54.50/year after. Original purchaser).

**2. What if I want my name on it?**
Free engraving. Inside the band, or inside & outside. Added to your order at no charge. Engraved rings are eligible for exchange.

**3. What if something goes wrong later?**
**Aydins Lifetime Warranty** is tiered: free in the first 6 months, $34.50 between 6–12 months, $54.50 after 12 months. We handle re-engraving, refinishing, and most damage that isn't loss or impact crushing.

---

**Body, closer:**

> We've been engraving and shipping rings from our shop in Irving, Texas since 2011. Over 10,000 orders. Real humans on the phone if you'd rather just call: **1-800-214-7345**.
>
> Your ring is still saved. Whenever you're ready.

**Signature:**
> The Aydins Family

**Footer:** same as Email 1.

---

# Email 3: sent 48–72 hours after abandon

**Goal:** Last touch. Optional discount. Hard close on the policy story.

**Subject line (A/B test 2):**
- A: `Last note about your cart`
- B: `One more thing before we let it go`

**Preview text:** `Free engraving is still on the table. So is your ring.`

---

### Body copy

**Hero headline:**
> One more note, then we'll stop.

**Subheadline:**
> Your cart is still saved. We didn't want to let it expire without making sure you had the full picture.

**[ Cart Item Block ]**

**[ CTA Button ]** `Complete my order` → `{{ event.extra.checkout_url }}`

---

**Body, recap in plain language:**

> Everything you'd want to know in one paragraph:
>
> Free engraving inside the band (or inside & outside). Free US shipping. **30-day returns**. A $25 restocking fee applies and you cover inbound shipping, but if the size or style isn't right, an exchange is always an option, engraved or not. **Aydins Lifetime Sizing** keeps your fit dialed in for as long as you own the ring. **Aydins Lifetime Warranty** is tiered and covers most damage outside of loss. Real humans on the phone at **1-800-214-7345**.
>
> If price is the issue, here's a one-time **20% off** code: `WELCOME20`, valid for the next 48 hours on this cart.
>
> Otherwise, no hard feelings. The ring will still be here when you're ready.

---

**Signature:**
> The Aydins Family
> Irving, Texas · since 2011

**Footer:** same as Email 1.

---

## What's deliberately NOT in here

- ❌ "Free returns". Never used. We have **30-day returns with $25 restocking**, customer pays inbound. Said plainly in Email 3.
- ❌ "Lifetime warranty" bare. Replaced with **Aydins Lifetime Warranty** (named program, tiered).
- ❌ "Free lifetime resizing". Replaced with **Aydins Lifetime Sizing program** (named, original purchaser).
- ❌ "Handcrafted / forged / made by hand". Aydins engraves and ships. Doesn't forge.
- ❌ "Flower Mound, TX" in **body copy / brand voice / trust lines**. Marketing line is always **Irving, Texas** (workshop). EXCEPTION: Flower Mound, TX IS correct in the email's legal mailing-address footer block (CAN-SPAM requirement, real PMB address). Two-context rule, locked 2026-05-15. See [[(C) Aydins Policies — Source of Truth]] rule 7.
- ❌ Apostrophe in "Aydin's". Always **Aydins**.
- ❌ "2-day shipping". Not claimed.

---

## Deploy checklist (in Klaviyo UI, flow `TrNjjf`)

For each of the three emails:

- [ ] Open flow `TrNjjf` → click into Email 1 / 2 / 3
- [ ] Paste new subject line + preview text
- [ ] Replace headline block with the V5 headline above
- [ ] Replace the "30-day free returns & exchanges" line wherever it appears with the approved language from Email 1/2/3
- [ ] Replace the "Lifetime fit guarantee & warranty" line with the **Aydins Lifetime Sizing program** and **Aydins Lifetime Warranty (tiered)** language
- [ ] Confirm signature reads "The Aydins Family" + "Irving, Texas since 2011"
- [ ] Confirm reply-to is `sales@shopaydins.com` (not no-reply)
- [ ] Confirm checkout URL merge tag actually populates in preview mode
- [ ] Send preview to yourself + 1 other person before saving live
- [ ] Save → Live
- [ ] Note the change date in `(C) Recart Knowledge Base + Revamp Diagnostic.md`

---

## After deploy: verify in 14 days

Pull the flow report from Klaviyo:
- Open rate vs current baseline (should hold or improve; clearer subjects)
- Click rate (should improve; clearer CTA logic)
- Revenue per recipient (the real metric)
- Unsubscribe rate (should NOT spike. If it does, Email 2 is too long, trim the three-up block)

If revenue per recipient drops more than 15% after 14 days with statistically meaningful volume, revert to the prior version while we diagnose. Otherwise leave running and apply the same voice pass to the broader email program.

---

## Open items

1. **Confirm the actual three live subject lines and bodies** before deploy so the A/B test framing has a baseline (open the flow in the Klaviyo UI; the MCP doesn't expose flow-action message bodies in this environment).
2. **Confirm `WELCOME20` exists as a Shopify discount code at 20% off with a 48-hour expiry rule.** If only `WELCOME10` exists, edit it to 20% and rename to `WELCOME20`, or create `WELCOME20` fresh and disable `WELCOME10`. Do not run both.
3. **Decide whether Email 3's discount stays at 10% or moves to a higher tier.** Current Recart welcome flow Msg 2 carries 83% of welcome revenue on a similar discount; the email equivalent should not undercut it.
4. **Once these are live, audit the rest of the Klaviyo email program** for the same banned phrases. Welcome series, post-purchase, browse abandonment if it exists.
