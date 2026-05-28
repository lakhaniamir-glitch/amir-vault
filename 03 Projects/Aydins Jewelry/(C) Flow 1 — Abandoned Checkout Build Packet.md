# Flow 1 — Abandoned Checkout Build Packet

**Created:** 2026-05-09
**Author:** Claude
**Status:** Ready to execute — 90-minute build
**Parent doc:** [[(C) Klaviyo Email Playbook]]
**Companion:** [[(C) Traffic & Conversion Audit]]

---

## Pre-flight verification (already done — confirmed 2026-05-09)

- ✅ Shopify integration enabled in Klaviyo
- ✅ Loox, Recart, Doofinder all enabled
- ✅ All 13 Shopify metrics mapped (Checkout Started, Placed Order, Added to Cart, etc.)
- ✅ Checkout Started firing ~5/day, 30-60 trackable abandons/month
- ⚠️ Onsite tracking ("Viewed Product", "Active on Site") — NOT YET INSTALLED. Needed for Browse Abandonment (Flow 3) but NOT for Abandoned Checkout (Flow 1). Build Flow 1 first, then come back and install onsite tracking before Flow 3.

---

## Realistic revenue expectation

**Flow 1 monthly lift estimate: $1,500–$4,000 in recovered revenue.**

Math: 30-60 trackable abandons/mo × 25-35% recovery rate × ~$200 AOV.

Hit "Live" and forget it. Compounds every month with no further work.

---

## DECISIONS YOU NEED TO MAKE BEFORE BUILDING

These are 4 quick calls. Make them now, don't delay:

### Decision 1 — From email
**Recommended:** `amir@shopaydins.com`
- Personal name = 15-20% better open rate than `support@`
- You'll get ~5-10 replies/week (mostly fit/material questions). Reply yourself or forward to support.
- If you don't want replies hitting your inbox: use `support@` instead.

### Decision 2 — Discount codes
Recommended (codes already in the playbook):
- `AYDINS5` — 5% off, used in email 3 (48hr expiry)
- `READY10` — 10% off, used in email 4 (24hr expiry)

**Action:** Create both codes in **Shopify → Discounts → Create discount → Discount code**:
- AYDINS5: Percentage → 5% → Active dates leave open → No min purchase → No usage limit per customer
- READY10: Percentage → 10% → Active dates leave open → No min purchase → No usage limit per customer

(We're using static codes here for simplicity. Klaviyo's "dynamic unique codes" are more secure but require Shopify Plus to fully wire up. Static codes are fine for v1.)

### Decision 3 — Logo
You need a transparent-background PNG of the Aydins logo, ~600px wide. Drop it somewhere accessible. We'll upload it during the master template step.

### Decision 4 — DKIM authentication
Before going Live, the From email's domain must have DKIM authenticated in Klaviyo. Check **Account → Settings → Email**. If DKIM shows red/not-authenticated:
- Click the DKIM setup wizard
- Klaviyo gives you 3 CNAME records
- Add them to your Shopify domain DNS (Settings → Domains → manage DNS, or wherever your DNS lives)
- Wait 1-24 hours for DNS to propagate
- Klaviyo re-checks automatically

**Without DKIM, your emails go to spam. This is non-negotiable.**

---

## Step 1 — Build the master template (15 min)

1. **Klaviyo → Templates → Create Template → Drag and Drop**
2. Name it: `Aydins Master 2026`
3. Layout settings (top-right gear icon):
   - **Background color:** `#FAFAF7`
   - **Content area width:** 600px
   - **Content area background:** `#FFFFFF`
   - **Padding:** 24px all sides
4. **Drag in a Header block:**
   - Upload your logo PNG
   - Width: 140px
   - Center-aligned
   - Padding: 24px top, 24px bottom
5. **Body text settings (right panel → Styles):**
   - Font family: **Poppins** (if not available, use **Helvetica Neue** as fallback)
   - Font size: 16px
   - Line height: 1.6
   - Color: `#1A1A1A`
   - Headlines (H1): 28px, weight 600
6. **Drag in a Button block (just to set the default styling):**
   - Background: `#1A1A1A`
   - Text color: `#FFFFFF`
   - Border radius: `0px` (square corners — non-negotiable)
   - Letter spacing: 1px
   - Text transform: UPPERCASE
   - Font weight: 500
   - Padding: 16px vertical, 32px horizontal
   - Save the button as a "Saved Block" → name it `Aydins CTA Button`
7. **Drag in a Footer block:**
   - Line 1: `Aydins Jewelry · Irving, TX 75063` (use your real registered address — required by CAN-SPAM)
   - Line 2: `You received this email because you subscribed at shopaydins.com or made a purchase.`
   - Line 3: `{% unsubscribe %}` link + `{% manage_preferences %}` link
   - Line 4: Small social row (Instagram + Facebook icons if active)
   - Footer text color: `#666666`, 12px
8. **Save**

---

## Step 2 — Build the flow shell (10 min)

1. **Klaviyo → Flows → Create Flow → Create from Scratch**
2. Name: `Abandoned Checkout — 4 emails`
3. Tag: `revenue` and `abandoned`
4. **Add Trigger:** Click "Metric" → select **"Checkout Started"** (the Shopify-piped metric)
5. **Trigger Filters tab:**
   - No filters at trigger level
6. **Flow Filters tab** (these check at every step):
   - `Has placed an order Zero times since starting this flow`
   - `Has Email is true`
   - (Don't add subscription status filter here — abandoned checkout is treated as transactional and can legally email non-subs in early emails)
7. **Smart Sending** (right panel): Set to **ON, 16 hours**
8. Save the flow shell

---

## Step 3 — Build Email 1 (12 min)

### Position in flow
- **Time delay before Email 1:** 40 minutes after trigger
- Click the **+** below the trigger → **Time Delay** → 40 minutes → Save

### Email setup
- Click **+** below the time delay → **Email**
- Click into the email → **Edit Content**
- Click **"Choose Template"** → select `Aydins Master 2026`

### Email 1 settings (top of editor):
- **From email:** `amir@shopaydins.com` (or your chosen sender)
- **From label:** `Amir at Aydins`
- **Reply-to:** Same as From
- **Subject line:** `Did you forget something?`
- **Preview text:** `A small reminder before the tab closes.`
- **A/B test subjects (click "A/B test" toggle):**
  - Variant A: `Did you forget something?`
  - Variant B: `Your ring is still in your cart`
  - Variant C: `{{ first_name|default:'Hey' }} — your cart is waiting`

### Email 1 body content
Paste this into the email body (replace the template's placeholder text):

```
Hi {{ first_name|default:'there' }},

Looks like you didn't finish checking out. Your cart is still saved — pick up right where you left off.

[CART BLOCK HERE]

[BUTTON: Return to checkout]

Lifetime warranty. Free US shipping. 30-day exchanges if the size isn't right.

If you have any questions about fit, finish, or material — just reply to this email. A real human reads every reply.

— Amir
Aydins Jewelry
```

### Email 1 dynamic blocks
- **[CART BLOCK]** → Drag in Klaviyo's "Show abandoned products" block (it's a pre-built block under "Catalog" in the block library). It auto-pulls the abandoned cart items, image, name, size, price.
- **[BUTTON]** → Drag in your saved `Aydins CTA Button`. Set the link to: `{{ event.checkout_url }}`. Set the button text to: `Return to checkout`

### Save
- Click **"Save and continue"**
- Set the email status to **"Manual"** (we'll switch to Live after testing all 4)

---

## Step 4 — Build Email 2 (12 min)

### Position
- After Email 1, drag in a **Time Delay** → set to **22 hours** → Save
- Drag in another **Email** node

### Email 2 settings
- From email / label: same as Email 1
- **Subject A/B set:**
  - Variant A: `A few things worth knowing about your ring`
  - Variant B: `Three reasons buyers come back to Aydins`
  - Variant C: `Before you decide — read this`
- **Preview text:** `Lifetime warranty, free resizing, 30-day exchanges.`

### Email 2 body content
```
Hi {{ first_name|default:'there' }},

Picking a wedding ring isn't a small decision. Here's what you should know before you buy from anyone — us or otherwise.

Fit is everything. If the size is off, you won't wear it. Every Aydins ring is exchangeable for 30 days, no questions, no restocking fees. We've shipped 10,000+ rings since 2011 — about 60% need a size swap on the first try. That's normal.

The metal matters. Tungsten won't scratch. Titanium is the lightest you can wear daily. Ceramic is hypoallergenic and fingerprint-resistant. 14k gold is the heirloom — pricier, but it stays in the family. If you're not sure which fits your work and lifestyle, reply and tell me what you do for a living. I'll tell you which holds up.

The warranty is real. Damage it on a job site? Snag it on equipment? We replace it. Lifetime, on us. The link is on every order page.

Your cart is still here when you're ready:

[BUTTON: Finish your order]

— Amir
Aydins Jewelry
```

### Formatting tips
- Make "Fit is everything." / "The metal matters." / "The warranty is real." **bold** at the start of each paragraph
- Button link: `{{ event.checkout_url }}`

### Save → status Manual

---

## Step 5 — Build Email 3 (15 min — discount + dynamic logic)

### Position
- After Email 2, **Time Delay** → **26 hours** (so total = 48 hours after trigger)
- Drag in **Email** node

### Email 3 settings
- **Subject A/B set:**
  - Variant A: `Your shipping is on us`
  - Variant B: `Take 5% off — for the next 48 hours`
  - Variant C: `A small thank you for your patience`
- **Preview text:** `Free shipping or 5% off, whichever fits the order better.`

### Email 3 body
```
Hi {{ first_name|default:'there' }},

If you've been on the fence, here's a small nudge.

Use code AYDINS5 at checkout for 5% off your order. Valid 48 hours.
(Or get free expedited shipping by selecting it at checkout — no code needed if your cart is over $150.)

[CART BLOCK]

[BUTTON: Finish your order]

One ring. One decision. We'll make it easy.

— Amir
Aydins Jewelry
```

### Make `AYDINS5` stand out
- Bold it in the body
- Optionally wrap it in a small colored "code chip" using a styled text block — background `#F4F2EC`, padding 8px 16px, monospace font

### Save → status Manual

---

## Step 6 — Build Email 4 (15 min — gold conditional)

### Position
- After Email 3, **Time Delay** → **4 days** (total = 6 days after trigger)
- **Conditional Split** node BEFORE Email 4:
  - Click **+** → Conditional Split
  - Condition: `What people did or did not do → Started Checkout → where Vendor equals "Jewelry Depot"`
  - **YES branch (gold cart):** send Email 4-Gold (5% / free shipping version)
  - **NO branch (tungsten/other):** send Email 4-Standard (10% version)

### Email 4-Standard (NO branch — tungsten cart, 10% off)
- **Subject A/B:**
  - A: `Last call on your cart — closing in 24h`
  - B: `10% off, expires tomorrow`
  - C: `We're going to release your size back to inventory`
- **Preview:** `Final reminder, then the cart auto-releases.`
- **Body:**
```
{{ first_name|default:'There' }},

Your cart has been saved for almost a week. To free up the size for other shoppers, we're going to release it tomorrow at noon CT.

If you still want it, here's the final push: code READY10 for 10% off, expires in 24 hours.

[CART BLOCK]

[BUTTON: Use code & finish]

If the size, finish, or width isn't quite right — reply and tell me what you'd change. We carry 1,191 styles. There's a better one for you in the catalog.

— Amir
Aydins Jewelry
```

- **Button link** (auto-applies discount): `https://shopaydins.com/discounts/READY10?redirect=/checkout/{{ event.checkout_token }}`

### Email 4-Gold (YES branch — Jewelry Depot, 5% only)
- **Subject A/B:**
  - A: `Last call on your cart — closing in 24h`
  - B: `Free expedited shipping, this week only`
  - C: `Your size releases tomorrow`
- **Preview:** `Final reminder before we release the cart.`
- **Body:**
```
{{ first_name|default:'There' }},

Your cart has been saved for almost a week. To free up the size for other shoppers, we're going to release it tomorrow at noon CT.

If you still want it, two options:
- Code AYDINS5 for 5% off — expires in 24 hours
- Free expedited shipping at checkout — no code, applies on carts $300+

[CART BLOCK]

[BUTTON: Finish your order]

If the size, finish, or width isn't quite right — reply and tell me. We carry over 200 14k gold styles.

— Amir
Aydins Jewelry
```

### Save both → status Manual

---

## Step 7 — Test the flow end-to-end (10 min)

1. **In Klaviyo**, click the flow → **"Preview & Test"** dropdown → **"Send Preview"** → enter your own email address
2. Check that all 4 emails render correctly in Gmail / Outlook
3. **Live abandoned cart test:**
   - Open shopaydins.com in **incognito mode**
   - Add a tungsten ring to cart → proceed to checkout
   - Enter your email at the email step → DON'T complete payment → close the tab
   - Wait 40 minutes
   - Email 1 should arrive at your inbox
4. **Verify the cart block populated correctly:**
   - The product image, name, size, and price should match what you abandoned
   - The "Return to checkout" button should take you back to the live checkout page with the items still there
5. **Check the event fired:**
   - In Klaviyo: **Profiles → search your test email → Activity tab**
   - You should see "Checkout Started" event
   - You should see the flow showing as "Active" for that profile

If anything's broken at this stage — check this list:
- Is the Shopify integration still showing "Connected"?
- Does the checkout token variable work? Try `{{ event.extra.checkout_url }}` instead of `{{ event.checkout_url }}` (Klaviyo sometimes uses a different path)
- Did the cart block dynamic content load? If not, you may need to wait 5-10 min after abandoning for Klaviyo to pick up the cart contents.

---

## Step 8 — Switch to Live (2 min)

Once tests pass:
1. Click each of the 4 emails → toggle status from **"Manual"** to **"Live"**
2. Click the flow itself → toggle status from **"Draft"** to **"Live"**
3. **Done.** Flow is now firing on every Checkout Started event.

---

## Step 9 — Monitor (ongoing — 5 min/week)

After 7 days, check the flow dashboard:

| Metric | Target | Red flag if |
|--------|--------|-------------|
| Email 1 open rate | 50%+ | Under 35% → subject line problem OR DKIM not authenticated |
| Email 1 click rate | 8%+ | Under 4% → CTA placement, body length, or images broken |
| Flow placed-order rate | 5%+ | Under 2% → likely bot traffic or pricing/trust issue (not email's fault) |
| Recovered revenue (30d) | $1,500+ | Below $500 after 30 days → check trigger filter logic, may not be firing on real abandons |

After 14 days, **check the A/B test winners** for each email's subject lines:
- Klaviyo dashboard shows which variant won (statistically significant after ~50 sends)
- Pause the losers, keep only the winner
- Set up a NEW A/B test on a different subject for the next round of optimization

---

## Step 10 — Loop back when Flow 1 is stable

Don't move to Flow 2 (Welcome Series) until Flow 1 has run for at least 7 days clean and you've seen recovered revenue land.

When ready, the playbook section for Flow 2 is here: [[(C) Klaviyo Email Playbook]]

---

## Cheat sheet — variables reference

If any of the dynamic variables don't work, here are the alternates Klaviyo accepts for Checkout Started events:

| Goal | Primary variable | Fallback |
|------|------------------|----------|
| First name | `{{ first_name|default:'there' }}` | `{{ person.first_name|default:'there' }}` |
| Checkout URL | `{{ event.checkout_url }}` | `{{ event.extra.checkout_url }}` |
| Checkout token | `{{ event.checkout_token }}` | `{{ event.extra.checkout_token }}` |
| Cart total | `{{ event.subtotal_price }}` | `{{ event.extra.subtotal_price }}` |
| Item count | `{{ event.line_items|length }}` | `{{ event.extra.line_items|length }}` |
| First item product name | `{{ event.line_items.0.title }}` | `{{ event.extra.line_items.0.title }}` |
| First item image | `{{ event.line_items.0.image_url }}` | `{{ event.extra.line_items.0.image_url }}` |

If unsure, use Klaviyo's built-in "Insert variable" dropdown in the email editor — it shows you what's available for the current trigger event.

---

## Done state

When this packet is fully executed and 7 days have passed, you should have:

- ✅ A live 4-email Abandoned Checkout flow
- ✅ Master template saved and reusable for the other 6 flows
- ✅ At least 1 test email confirmed working end-to-end
- ✅ Initial revenue attribution showing in Klaviyo flow dashboard
- ✅ A/B test data starting to accumulate

That's Flow 1. The single biggest revenue automation in the entire e-commerce email playbook, now wired into your store.

— End of build packet —
