
3



# Klaviyo Email Playbook — Aydins Jewelry

**Created:** 2026-05-09
**Author:** Claude
**Status:** Ready to implement
**Companion report:** [[(C) Traffic & Conversion Audit]]
**Project:** [[CLAUDE]]

---

## How to read this document

Every flow below is structured the same way so you can implement them one at a time without re-reading the whole guide:

1. **Why it matters** — revenue logic in one paragraph
2. **Trigger** — exact Klaviyo trigger config
3. **Sequence map** — emails, timing, discount strategy
4. **Per-email spec** — subject A/B set, preview text, body, CTA
5. **Klaviyo UI setup steps** — click-by-click

Voice is locked: **premium, straightforward, no fluff, second-person ("you"), short sentences.** No emojis in subject lines or body. No "Hey there!" openers. No "Don't miss out!" closers. Aydins talks to a grown man buying a wedding band — not a teenager getting a coupon.

---

## Executive summary — top 5 actions ranked by impact/effort

| # | Action | Why | Effort | Expected impact |
|---|--------|-----|--------|-----------------|
| 1 | Build the **Abandoned Checkout** flow (4 emails over 7 days) | This single flow recovers 5–15% of abandoned revenue. Highest dollar-per-hour ROI in email. | 3 hrs | +$2k–$5k/mo |
| 2 | Build the **Welcome Series** (5 emails over 14 days) | Recart popup is firing, but new subs sit in your list with no follow-up. Welcome series converts 50–60% of first-time buyers among email subs. | 4 hrs | +$1.5k–$3k/mo |
| 3 | Build the **Browse Abandonment** flow (2 emails) | Cheapest to ship, plugs a leak you don't see in reports. Catches the "looked but didn't add" segment. | 1.5 hrs | +$500–$1.5k/mo |
| 4 | Build the **Post-Purchase** flow (5 emails over 60 days) | Drives review collection (you need social proof badly per the audit) AND repeat orders. Costs nothing, prints money. | 3 hrs | +$1k/mo + 30+ reviews |
| 5 | Build the **Win-Back** flow (3 emails over 21 days, triggered at 180 days inactive) | Reactivates 2–5% of dormant buyers. Your customer list since 2011 is a dormant goldmine. | 2 hrs | +$800–$2k/mo |

**Order of operations:**
1. Abandoned Checkout (this week)
2. Welcome Series (next week)
3. Browse Abandonment + Post-Purchase (week 3)
4. Win-Back + Price Drop / Back in Stock (week 4)

Total time-to-implement: ~15–18 hours of focused work over 4 weeks. Expected baseline lift: **15–25% of monthly revenue from email channel** within 60 days of going live (industry benchmark for jewelry e-com that sets up the full automation stack from a near-zero baseline).

---

## Section 0 — Pre-flight: confirm Klaviyo ↔ Shopify is wired correctly

**Do this BEFORE building any flow.** A flow on top of broken tracking is worse than no flow.

### 0.1 — Verify the Shopify integration is sending all events

In Klaviyo:
1. **Account → Integrations → Shopify**
2. Check that the integration shows **"Connected"** with green checkmark
3. Click **"Sync settings"** and confirm these are ON:
   - ✅ Sync Shopify products to Klaviyo catalog
   - ✅ Sync Shopify customers
   - ✅ Sync Shopify orders
   - ✅ Subscribe customers at checkout (when they tick the consent box)
   - ✅ Add Klaviyo onsite tracking to your store

### 0.2 — Verify the events are firing

In Klaviyo: **Analytics → Metrics**, you should see all of these with recent activity (last 24 hrs):

| Event | What it powers | If missing → |
|-------|----------------|--------------|
| **Active on Site** | Browse Abandonment | Reinstall onsite tracking snippet |
| **Viewed Product** | Browse Abandonment, segments | Reinstall onsite tracking |
| **Added to Cart** | Abandoned Cart | Verify in theme.liquid |
| **Started Checkout** | Abandoned Checkout (the big one) | Reinstall integration |
| **Placed Order** | Post-Purchase, segments | Should be auto from Shopify |
| **Ordered Product** | Cross-sell logic | Should be auto |
| **Fulfilled Order** | Shipping notifications, review request | Should be auto |
| **Refunded Order** | Suppression for review request | Should be auto |

If any of these are missing or showing zero events: **stop and fix the integration first.** Re-sync Shopify in Klaviyo, paste the onsite tracking snippet into `theme.liquid` right before `</head>`, push the theme, and wait 30 minutes before checking again.

### 0.3 — Make sure your sender identity is verified

In Klaviyo: **Account → Settings → Email**
- **From email:** `support@shopaydins.com` (or `hello@`, your call — but use a real monitored inbox, not `noreply@`)
- **From name:** `Aydins Jewelry`
- **Reply-to:** Same as From
- **DKIM:** Must show **Authenticated**. If not, follow Klaviyo's DKIM setup wizard — paste 3 CNAME records into your domain DNS (Shopify domains or wherever DNS is managed). This is non-negotiable. Without DKIM, your emails go to spam.
- **Dedicated sending domain:** Set up `email.shopaydins.com` (or `mail.shopaydins.com`) as your dedicated sending subdomain. Klaviyo walks you through this. Skipping this means you share Klaviyo's IP reputation with thousands of other brands — many of whom send junk.

### 0.4 — Master template baseline (build once, reuse everywhere)

Build a single master template in **Templates → Create Template → Drag and Drop**. Save it as **"Aydins Master 2026"**. Use it as the starting clone for every flow email so the look stays consistent.

Spec for the master template:
- **Width:** 600px (single column)
- **Background:** `#FAFAF7` (off-white, NOT pure white)
- **Body container:** `#FFFFFF`
- **Header logo:** Aydins logo, centered, ~140px wide, 24px padding top + bottom
- **Body text:** Poppins or system serif fallback, 16px, line-height 1.6, color `#1A1A1A`
- **Headlines:** 28px, weight 600, color `#1A1A1A`
- **Buttons:** Solid black `#1A1A1A` background, white text, no border-radius (square corners), 14px letter-spacing 1px uppercase, 16px vertical padding × 32px horizontal padding
- **Footer:**
  - Two-line address (required by CAN-SPAM): `Aydins Jewelry · Irving, TX`
  - "You received this because you subscribed at shopaydins.com" + Unsubscribe link + Update preferences link
  - Small social row: Instagram, Facebook (if active)

**Hero image rule:** If the email is product-related, use a clean on-hand or on-white shot. Do NOT use stock photography of generic couples. Do NOT use the Recart popup graphic.

---

## FLOW 1 — Abandoned Checkout (THE BIG ONE)

### Why it matters

This is the single highest-ROI automation in e-commerce. A buyer typed in their email and got to the payment step but didn't finish. They are 100x more likely to convert than a cold visitor. Industry data: 30–40% of abandoned checkouts can be recovered with a well-built sequence. For a store doing ~$30k/mo at a 50–60% checkout abandonment rate (typical), that's **$3k–$8k/mo in pure recovered revenue.**

### Trigger config

- **Trigger:** Started Checkout (Shopify metric, auto-piped from integration)
- **Filter at trigger:** None
- **Flow filters (apply at start):**
  - `Placed Order Zero times since Started Checkout` (so the flow exits the second they finish)
  - `Has Email is true`
  - `Email Marketing is set to "Subscribed" OR Email Marketing is unset` (transactional language allowed for non-subs in early emails — see legal note below)
- **Smart Sending:** ON, 16 hours

> **Legal note:** Abandoned checkout emails to people who didn't opt in to marketing are technically "transactional" in most jurisdictions because they're tied to a transaction-in-progress. Klaviyo sends them by default. Keep promotional content out of email 1 and email 2 to stay in transactional territory. From email 3 (which has a discount), apply the filter `Email Marketing equals "Subscribed"` to that specific message.

### Sequence map

| Email | Send delay | Goal | Discount? |
|-------|-----------|------|-----------|
| 1 | **40 minutes** after trigger | Reminder — "you left this behind" | None |
| 2 | **22 hours** after trigger | Trust + objection handling | None |
| 3 | **48 hours** after trigger | Soft offer — free shipping or 5% | 5% off OR free shipping |
| 4 | **6 days** after trigger | Last call | 10% off (final, expires in 24h) |

**Why this timing beats the default Klaviyo template:**
- Klaviyo default is 4h / 24h / 4 days. 4h is too soon — the buyer is probably still on the toilet, on the couch, or comparison shopping. 40 min catches them while the tab is literally still open in their browser. 22h catches them the next day at the same hour they were originally browsing (hugely under-rated trick — people have buying patterns).
- Spacing the discount until email 3 keeps your AOV up. Train buyers that "abandoning = instant 15% off" and you train them to abandon every order.

### Discount strategy notes (margin-aware)

You said: tungsten = high margin, 14k gold = thinner. Klaviyo lets you use **dynamic discount logic** based on the abandoned cart value or the SKU vendor:

- **For tungsten / titanium / ceramic carts** (most of your catalog): 10% in email 4 is fine, margins absorb it.
- **For 14k gold carts** (Jewelry Depot vendor on most gold SKUs): cap discount at 5% OR substitute "Free Priority Shipping ($25 value)" in email 4 instead. Set this as a conditional split in the flow (see UI step 9 below).

### Per-email spec

#### Email 1 — "Did you forget something?" (40 min after trigger)

**Subject lines (pick one, A/B the other two):**
1. Did you forget something?
2. Your ring is still in your cart
3. {{ first_name|default:'There' }} — your cart is waiting

**Preview text:** A small reminder before the tab closes.

**Body:**

> Hi {{ first_name|default:'there' }},
>
> Looks like you didn't finish checking out. Your cart is still saved — pick up right where you left off:
>
> [DYNAMIC PRODUCT BLOCK — Klaviyo's "Cart" content block: image, title, size, price]
>
> [BUTTON: Return to checkout → checkout_url]
>
> Lifetime warranty. Free US shipping. 30-day exchanges if the size isn't right.
>
> If you have any questions about fit, finish, or material — just reply to this email. A real human reads every reply.
>
> — Amir
> Aydins Jewelry

**CTA:** Return to checkout (links to `{{ event.checkout_url }}`)

#### Email 2 — "A few things worth knowing" (22 hours after trigger)

**Subject lines:**
1. A few things worth knowing about your ring
2. Three reasons buyers come back to Aydins
3. Before you decide — read this

**Preview text:** Lifetime warranty, free resizing, 30-day exchanges.

**Body:**

> Hi {{ first_name|default:'there' }},
>
> Picking a wedding ring isn't a small decision. Here's what you should know before you buy from anyone — us or otherwise.
>
> **Fit is everything.** If the size is off, you won't wear it. Every Aydins ring is exchangeable for 30 days, no questions, no restocking fees. We've shipped 10,000+ rings since 2011 — about 60% need a size swap on the first try. That's normal.
>
> **The metal matters.** Tungsten won't scratch. Titanium is the lightest you can wear daily. Ceramic is hypoallergenic and fingerprint-resistant. 14k gold is the heirloom — pricier, but it stays in the family. If you're not sure which fits your work and lifestyle, reply and tell me what you do for a living. I'll tell you which holds up.
>
> **The warranty is real.** Damage it on a job site? Snag it on equipment? We replace it. Lifetime, on us. The link is on every order page.
>
> Your cart is still here when you're ready:
>
> [BUTTON: Finish your order → checkout_url]
>
> — Amir
> Aydins Jewelry

#### Email 3 — Soft offer (48 hours after trigger)

**Subject lines:**
1. Your shipping is on us
2. Take 5% off — for the next 48 hours
3. A small thank you for your patience

**Preview text:** Free shipping or 5% off, whichever fits the order better.

**Body:**

> Hi {{ first_name|default:'there' }},
>
> If you've been on the fence, here's a small nudge.
>
> Use code **AYDINS5** at checkout for 5% off your order. Valid 48 hours.
> (Or get free expedited shipping by selecting it at checkout — no code needed if your cart is over $150.)
>
> [DYNAMIC PRODUCT BLOCK]
>
> [BUTTON: Finish your order → checkout_url]
>
> One ring. One decision. We'll make it easy.
>
> — Amir
> Aydins Jewelry

**Klaviyo discount setup:** Use a **dynamic coupon code** (Klaviyo → Coupons → Create coupon → "AYDINS5" prefix → 5% off → 48-hour expiry). This creates unique codes per recipient — better than static codes that get leaked to coupon sites.

#### Email 4 — Last call (6 days after trigger)

**Subject lines:**
1. Last call on your cart — closing in 24h
2. 10% off, expires tomorrow
3. We're going to release your size back to inventory

**Preview text:** Final reminder, then the cart auto-releases.

**Body:**

> {{ first_name|default:'There' }},
>
> Your cart has been saved for almost a week. To free up the size for other shoppers, we're going to release it tomorrow at noon CT.
>
> If you still want it, here's the final push: code **READY10** for 10% off, expires in 24 hours.
>
> [DYNAMIC PRODUCT BLOCK]
>
> [BUTTON: Use code & finish → checkout_url with discount auto-applied]
>
> If the size, finish, or width isn't quite right — reply and tell me what you'd change. We carry 1,191 styles. There's a better one for you in the catalog.
>
> — Amir
> Aydins Jewelry

**Pro move:** Set up a Klaviyo discount link that pre-applies the code on click. Format: `https://shopaydins.com/discount/READY10?redirect=/checkouts/{{ event.token }}`. Removes one step.

### Klaviyo UI setup — step by step

1. **Flows → Create Flow → Create from Scratch**
2. Name: `Abandoned Checkout — 4 emails`
3. Tag: `revenue` `abandoned`
4. Click **"Add Trigger"** → select **"Metric"** → choose **"Started Checkout"**
5. Click **"Add Filter"** at the top of the flow → "Has not placed order since starting this flow"
6. Click the **+** below the trigger → **"Time Delay"** → set to 40 minutes (Smart Sending ON)
7. Click **+** → **"Email"** → select your master template → paste in Email 1 content → save and click **"Manual"** to put it in draft mode (we'll switch to Live after all 4 are built and tested)
8. Repeat steps 6–7 for emails 2, 3, 4 with the timing from the sequence map above
9. **Conditional split for the discount tier (advanced):**
   - Before email 4, drop in a **"Conditional Split"** node
   - Condition: `Cart total is greater than $300 AND any item vendor equals "Jewelry Depot"`
   - YES branch: send the 5% / Free Shipping version (gold-friendly)
   - NO branch: send the 10% version
10. **Test the flow:**
    - Open an incognito window, go through checkout with a real email you control, abandon at the payment step
    - Wait 40 min — email 1 should arrive
    - In Klaviyo: **Profiles → search your test email → Activity** → confirm "Started Checkout" event fired
11. **Switch each email from Manual → Live** once you've tested
12. **Set the flow to Live**

### What to watch in week 1

- **Open rate:** target 50%+ on email 1 (these are warm). If under 35%, your subject is wrong or sender domain isn't authenticated.
- **Click rate:** target 8%+ on email 1.
- **Placed Order rate:** target 5%+ overall flow attribution within 30 days.
- **Recovered revenue:** Klaviyo shows this on the flow dashboard. Goal is to see it climb past $1k in the first 30 days.

---

## FLOW 2 — Welcome Series (for Recart popup signups)

### Why it matters

The Recart 20% off popup is firing on your store. Every email captured but not converted is rotting in your list. A welcome series is your one chance to convert that subscriber while their intent is highest. Industry benchmark: welcome series convert 50–60% of first-time buyers among email signups.

### Trigger config

- **Trigger:** List → "New subscribers added to Newsletter list"
  - (Make sure Recart is pushing into a Klaviyo list called "Newsletter" or similar — verify in Recart → Integrations → Klaviyo)
- **Filter at trigger:** `Has Email is true`
- **Flow filters:**
  - `Placed Order Zero times since first becoming a subscriber`
- **Smart Sending:** ON

### Sequence map

| Email | Send delay | Goal | Discount |
|-------|-----------|------|----------|
| 1 | Immediately (5 min) | Deliver the 20% code, set expectations | 20% (the popup promise) |
| 2 | 24 hours later | Origin story — why Aydins exists | None |
| 3 | 3 days after trigger | Help them choose a metal | None |
| 4 | 6 days after trigger | Social proof — real customer photos & reviews | None |
| 5 | 13 days after trigger | Final call on the 20% code | Same code, expiring |

### Per-email spec

#### Email 1 — Welcome + 20% code (5 min after signup)

**Subject lines:**
1. Welcome to Aydins — here's your 20% off
2. Your 20% off code is inside
3. Code attached, plus a few things you should know

**Preview text:** Use code WELCOME20 at checkout. Expires in 14 days.

**Body:**

> Welcome.
>
> You're in. Use code **WELCOME20** at checkout for 20% off any ring in our catalog. Code expires in 14 days.
>
> [BUTTON: Shop the catalog → /collections/all]
>
> A few things to know about us:
>
> - Family-owned. Founded 2011 in Irving, Texas.
> - We've shipped 10,000+ rings since.
> - Lifetime warranty on every ring.
> - Free US shipping. 30-day exchanges if the size isn't right.
>
> If you've got a question about fit, finish, or which metal will hold up to your work — just reply. I read every email.
>
> — Amir
> Owner, Aydins Jewelry

#### Email 2 — Origin story (Day 1)

**Subject lines:**
1. Why we started making rings
2. The reason there's a lifetime warranty on every Aydins ring
3. A short story — how Aydins began

**Preview text:** A 90-second read.

**Body:**

> {{ first_name|default:'Hi' }},
>
> Quick story.
>
> Aydins started in 2011 because most wedding bands were built for jewelry counters, not real life. Tungsten and titanium were sold as "novelty" metals — when in fact they're some of the most durable materials a man can wear daily.
>
> A wedding ring should survive everything. Job sites. Workouts. Beach days. The grandkid pulling on your hand at sixty. That's the promise — and it's why every ring carries our lifetime warranty. If yours fails, we replace it.
>
> 14 years later, we make rings in tungsten, titanium, ceramic, 14k gold — over 1,100 styles. All shipped free in the US. All exchangeable in the first 30 days.
>
> If you haven't browsed yet, here's where most guys start:
>
> [BUTTON: Browse the catalog →]
>
> Code **WELCOME20** is still good for 12 more days.
>
> — Amir

#### Email 3 — Metal guide (Day 3)

**Subject lines:**
1. Tungsten vs titanium vs gold — which one fits your life?
2. The 90-second metal guide for your wedding ring
3. Pick the right metal in three bullets

**Preview text:** Tungsten if you work with your hands. Titanium if you want light. Gold if it's heirloom.

**Body:**

> {{ first_name|default:'There' }} —
>
> The metal you pick matters more than the design. Here's the cheat sheet:
>
> **Tungsten** — Heaviest, hardest, scratch-proof. Best for tradesmen, mechanics, contractors, gym lifters, anyone who works with their hands. Polishes back to mirror finish forever. Won't bend or stretch.
> [BUTTON: Shop tungsten →]
>
> **Titanium** — Lightest metal we carry. You won't feel it on your hand. Hypoallergenic. Won't tarnish. Best if you're transitioning from "no ring" to "ring" and want something invisible-feeling.
> [BUTTON: Shop titanium →]
>
> **Ceramic** — Hypoallergenic, fingerprint-resistant, doesn't conduct heat or electricity. Best for medical professionals, electricians, people with metal allergies.
> [BUTTON: Shop ceramic →]
>
> **14k Gold** — The heirloom. Holds value. Refinishes if scratched. The ring you pass down. Higher price reflects real gold content.
> [BUTTON: Shop gold →]
>
> Still on the fence? Reply with what you do for work — I'll tell you exactly which metal will hold up.
>
> — Amir

#### Email 4 — Social proof (Day 6)

**Subject lines:**
1. What 10,000 customers say about their Aydins ring
2. Real photos from the men who wear our rings
3. Three reviews worth reading

**Preview text:** Real reviews. Real photos. Not stock.

**Body:**

> {{ first_name|default:'There' }} —
>
> Don't take our word for it. Here are three reviews from the past 90 days, real photos, real names:
>
> [PULL 3 REVIEWS FROM YOTPO/JUDGE.ME — image, name, star rating, 2-line snippet]
>
> Over 10,000 rings shipped since 2011. 4.8 average rating. The lifetime warranty is the proof we stand behind it.
>
> [BUTTON: Browse the catalog →]
>
> Code **WELCOME20** still works for the next 8 days.
>
> — Amir

**Note:** Use Klaviyo's "Product Block" or "Reviews Block" if you have Yotpo/Judge.me integrated. If not, hand-pick 3 reviews monthly and update the email manually.

#### Email 5 — Last call (Day 13)

**Subject lines:**
1. Code WELCOME20 expires tomorrow
2. Last day for 20% off
3. {{ first_name|default:'Hey' }} — code expires at midnight

**Preview text:** No tricks. The 20% code expires tomorrow at 11:59 PM CT.

**Body:**

> {{ first_name|default:'There' }},
>
> Last call.
>
> Your **WELCOME20** code expires tomorrow at 11:59 PM Central. After that, it's gone.
>
> If you've been thinking about it, this is the moment.
>
> [BUTTON: Shop the catalog →]
>
> Or, if you have a question that's holding you up — reply. I'll answer today.
>
> — Amir
> Aydins Jewelry

### Klaviyo UI setup

1. **Flows → Create Flow → Create from Scratch**
2. Name: `Welcome Series — 5 emails`
3. Trigger: **List Triggered** → "Newsletter" list (or whatever Recart pushes to)
4. Add flow filter: `Placed Order Zero times since first being added to flow`
5. Build the 5 emails using your master template
6. Set timings per the sequence map (5 min, 24h, 3d, 6d, 13d)
7. **Test:** Add yourself to the Newsletter list manually → confirm email 1 arrives in 5 min
8. **Discount setup:** Create a static code `WELCOME20` in Coupons → 20% off → 14-day expiry from issue date
9. Set flow to Live

### Important: deduplicate Recart's automatic emails

Recart has its own welcome email. **Turn it off** in Recart → Automations → "Send welcome email after subscription" → OFF. You only want ONE welcome series running, and Klaviyo's is the better one.

---

## FLOW 3 — Browse Abandonment

### Why it matters

This is the cheapest, fastest flow to ship and one of the highest ROI relative to setup time. It catches people who viewed a product 3+ times but never added to cart. They told you what they want by viewing it. Industry benchmark: 1–3% conversion rate on browse-abandonment emails. For a store doing your traffic volume, that's 100–300 extra orders per year from this one flow alone.

### Trigger config

- **Trigger:** Metric → **"Viewed Product"**
- **Trigger filter:** `Viewed Product at least 2 times in the last 24 hours, where the same product was viewed`
- **Flow filters:**
  - `Has Email is true`
  - `Email Marketing equals "Subscribed"` (cannot legally browse-email non-subs in most jurisdictions)
  - `Started Checkout zero times in last 24 hours` (don't double-up with abandoned checkout)
  - `Placed Order zero times in last 24 hours`
- **Smart Sending:** ON

### Sequence map

| Email | Send delay | Goal | Discount |
|-------|-----------|------|----------|
| 1 | 4 hours after last view | Show the product they viewed + alternatives | None |
| 2 | 48 hours after first view | Soft nudge with social proof for that style | 5% |

### Per-email spec

#### Email 1 — "Still thinking it over?" (4 hrs)

**Subject lines:**
1. Still thinking about the {{ event.product_name }}?
2. The {{ event.product_name }} is still in stock
3. {{ first_name|default:'Hey' }} — about that ring you were looking at

**Preview text:** Plus three similar styles in case it's not quite right.

**Body:**

> {{ first_name|default:'There' }},
>
> You spent some time looking at this one earlier:
>
> [DYNAMIC PRODUCT BLOCK — last viewed product, image, name, price]
>
> [BUTTON: View the {{ event.product_name }} →]
>
> If the design's not quite right, here are three similar styles other customers compared it against:
>
> [DYNAMIC PRODUCT FEED — Klaviyo's "Recommended Products" block, similar items same vendor/material]
>
> If the question holding you up is fit, finish, width, or comfort — reply. I'll answer today.
>
> — Amir

#### Email 2 — Soft offer (48h)

**Subject lines:**
1. Take 5% off the ring you've been looking at
2. Five percent — code valid 48 hours
3. A small nudge from us

**Preview text:** Code RING5 — valid 48 hours.

**Body:**

> {{ first_name|default:'There' }},
>
> Quick one. If the {{ event.product_name }} is the ring, here's a small thank you for your patience:
>
> Code **RING5** — 5% off, valid 48 hours.
>
> [DYNAMIC PRODUCT BLOCK — last viewed]
>
> [BUTTON: Get 5% off →]
>
> Free US shipping. Lifetime warranty. 30-day exchanges if the size isn't right.
>
> — Amir
> Aydins Jewelry

### Klaviyo UI setup

1. **Flows → Create Flow → Browse Abandonment** (Klaviyo has a built-in template — start there to save time)
2. Adjust the trigger filter to `Viewed Product 2+ times in 24h` (the default is sometimes 1)
3. Adjust the flow filter for `Email Marketing = Subscribed` (default may not have this)
4. Replace the default content with the templates above
5. **Critical:** Use Klaviyo's `{{ event.viewed_product.title }}` and `{{ event.viewed_product.url }}` and `{{ event.viewed_product.image_url }}` variables in the dynamic blocks. Test by sending yourself a preview.
6. Set to Live

---

## FLOW 4 — Abandoned Cart (different from Abandoned Checkout)

### Why it matters

Abandoned Checkout fires when someone enters their email at the payment step. Abandoned Cart fires when someone adds to cart but never proceeds to checkout. These are weaker leads but plug a real hole — many users never get to the checkout email field because they bounce earlier.

**Note:** This flow only works if you've captured the user's email before the cart step (Recart popup, account login, or "checkout" with prefilled email). If you don't have an email, the trigger has nothing to send to. So this flow runs lighter than Abandoned Checkout — that's expected.

### Trigger config

- **Trigger:** Metric → **"Added to Cart"**
- **Flow filter:**
  - `Started Checkout zero times since added to cart`
  - `Placed Order zero times since added to cart`
  - `Has Email is true`
  - `Email Marketing equals "Subscribed"`
- **Smart Sending:** ON

### Sequence map

| Email | Send delay | Discount |
|-------|-----------|----------|
| 1 | 6 hours | None |
| 2 | 36 hours | 5% (code: BACK5) |

Keep this one short. If they didn't get to checkout, they likely needed more info — not more emails.

### Per-email spec (condensed — clone & adapt the Browse Abandonment templates)

**Email 1 subject options:**
1. You added the {{ event.product_name }} to your cart
2. Still on the fence?
3. Three minutes to finish

**Email 2 subject options:**
1. Take 5% off — code BACK5
2. Last try — your cart with 5% off
3. Code attached

Body content: mirror the Browse Abandonment language but reference "cart" instead of "viewed."

### Klaviyo UI setup

Use the built-in **"Abandoned Cart"** flow template. Adjust timing and copy. Set to Live.

---

## FLOW 5 — Post-Purchase

### Why it matters

Two jobs at once: (1) generate reviews (you need social proof per the audit report), (2) drive repeat orders + cross-sell. Wedding ring customers don't typically buy multiple rings — but they refer friends, buy gifts, and come back for anniversary upgrades. A polished post-purchase flow earns ~$1k/mo and 30+ reviews/mo for a store at your volume.

### Trigger config

- **Trigger:** Metric → **"Placed Order"**
- **Flow filter:**
  - `Refunded Order zero times since this order` (suppress if refunded mid-flow)
  - `Has Email is true`
- **Smart Sending:** ON

### Sequence map

| Email | Send delay | Goal |
|-------|-----------|------|
| 1 | Immediately (5 min) | Order confirmation companion — premium thank you |
| 2 | When tracking shows "delivered" (use Shopify "Order Fulfilled" event with delay) | Care guide for the metal they bought |
| 3 | 14 days after delivery | Review request |
| 4 | 30 days after order | Cross-sell — matching engraving / second ring / care kit |
| 5 | 60 days after order | Refer-a-friend incentive |

### Per-email highlights (full templates below)

#### Email 1 — Premium thank you (5 min)

**Subjects:**
1. Order confirmed — thank you
2. Welcome to the family, {{ first_name }}
3. Your Aydins ring is on its way

**Body:**

> {{ first_name|default:'There' }} —
>
> Order confirmed. Thank you.
>
> You just joined a list of 10,000+ customers since 2011. We don't take that lightly. Here's what happens next:
>
> 1. **Today / tomorrow** — your ring is inspected, polished, and packed by hand at our Texas warehouse.
> 2. **48–72 hours** — you'll get a tracking number from us.
> 3. **Within 5 business days** — it's at your door.
>
> Your order details:
>
> [DYNAMIC ORDER BLOCK — items, sizes, total]
>
> If the size isn't right when it arrives — reply to this email. We'll send the next size. Free, no questions, no restocking fee. That's the 30-day exchange policy.
>
> Lifetime warranty starts today. We're here for the long run.
>
> — Amir
> Owner, Aydins Jewelry

#### Email 2 — Care guide (delivery + 1 day)

**Subjects:**
1. How to keep your tungsten/titanium/gold ring looking new
2. Care guide — read once, never wonder again
3. Two minutes on care

**Body:**

> {{ first_name|default:'There' }} —
>
> Your ring should be on your hand. Here's how to keep it looking the way it does today.
>
> **[CONDITIONAL — show only the section matching the metal they bought, using Klaviyo dynamic content]**
>
> **Tungsten care:**
> - Soap and water. That's it.
> - Polish with a microfiber cloth weekly. It restores mirror finish in seconds.
> - DON'T hit it with a hammer. Tungsten is hard but brittle. It can fracture under direct impact.
> - DO wear it in the gym. To work. In the shower.
>
> **Titanium care:**
> - Same — soap and water.
> - Won't tarnish. Ever.
> - Resistant to scratches but not scratch-proof. Brushed finish hides wear better than polished.
>
> **Ceramic care:**
> - Hypoallergenic. Fingerprint-resistant.
> - Brittle on direct impact, like tungsten. Don't slam it into hard surfaces.
> - Lifetime warranty replaces it if it ever cracks.
>
> **14k Gold care:**
> - Polish with jewelry cloth or a soft toothbrush + soap.
> - Take it off for the gym to avoid bending.
> - Re-polish service available — reply for details.
>
> Got a question about your specific ring? Reply.
>
> — Amir

#### Email 3 — Review request (delivery + 14d)

**Subjects:**
1. How's the ring treating you, {{ first_name }}?
2. A favor — 30 seconds
3. Quick question about your Aydins ring

**Body:**

> {{ first_name|default:'There' }} —
>
> Two weeks in. How's the ring?
>
> If it's good — we'd be grateful for a quick review. Takes 30 seconds, helps the next guy decide.
>
> [BUTTON: Leave a review →]
>
> If it's not good — reply to this email. Tell me what's wrong. We fix it.
>
> Either way, thank you for the trust.
>
> — Amir
> Aydins Jewelry

**Setup tip:** Link the review button to your Yotpo/Judge.me dynamic review link `{{ review_request_url }}` for that order. Pre-fills the product. Conversion rate doubles vs. a generic "leave a review" page.

#### Email 4 — Cross-sell (30d)

**Subjects:**
1. Custom engraving for your Aydins ring
2. The thing most customers add a month later
3. A polish kit, on us, with your next order

**Body:**

> {{ first_name|default:'There' }},
>
> If you've worn your ring for a month, you've probably figured out you love it (or you'd have exchanged it — and the offer's still open if you do).
>
> A few things customers add after the first month:
>
> 1. **Engraving** — Add wedding date, initials, or a phrase to the inside of the band. $19. We do it in-house, ships in 5 days.
> 2. **Polish kit** — Microfiber cloth + jewelry cleaner. Keeps the mirror finish forever. $12.
> 3. **A second ring** — gym ring, work ring, travel ring. Same comfort fit, different finish.
>
> [BUTTON: Browse →]
>
> No discount code on this one. Just letting you know what's there.
>
> — Amir

#### Email 5 — Refer a friend (60d)

**Subjects:**
1. $25 to you, $25 to a friend
2. Got a friend getting married?
3. A small thank you, plus a referral

**Body:**

> {{ first_name|default:'There' }} —
>
> Customers send us friends every week. We want to make it worth your time.
>
> Forward this email to a friend who's shopping for a wedding band. They get $25 off their first order. You get a $25 credit when they buy. No expiration.
>
> Their code: **AYDINS25-{{ first_name|upper|truncate:6 }}**
>
> [BUTTON: Forward this email →]
>
> Or just send them the link: [shopaydins.com](https://shopaydins.com)
>
> — Amir

**Setup tip:** Klaviyo doesn't natively do referral codes. Use a simple static `AYDINS25` code with a $25 cap, or install **ReferralCandy** or **Yotpo Loyalty** if you want true two-sided tracking. For phase 1, the static code is fine.

### Klaviyo UI setup

1. Create Flow → name `Post-Purchase — 5 emails`
2. Trigger: Placed Order
3. Filter: `Refunded Order zero times since starting flow`
4. Build emails 1, 2, 3, 4, 5 with timings (5 min / Order Fulfilled +1d / +14d / +30d / +60d)
5. **Email 2 timing trick:** Use Klaviyo's **"Wait for Fulfillment Status to be Delivered"** condition (Conditional Split → "Has fulfillment status of Delivered"). If yes → send. If no after 7 days → skip (so customers with delayed shipments don't get the care guide before the ring arrives).
6. **Email 2 dynamic content:** Use Klaviyo's "Conditional Block" inside the email to show only the relevant metal care section based on the order's product tags or vendor. (Tag your products with `material:tungsten`, `material:titanium`, etc., in Shopify so Klaviyo can filter on them.)
7. Set to Live

---

## FLOW 6 — Win-Back

### Why it matters

You've got 14 years of customers. Most haven't bought again. Even a 2% reactivation rate of dormant buyers is significant revenue. This is the lowest-effort, highest-leverage flow you can run on your historical list.

### Trigger config

- **Trigger:** Date-based segment trigger
  - **Segment:** "Inactive Buyers" — defined as: `Placed Order at least once over all time AND Placed Order zero times in the last 180 days`
- **Smart Sending:** ON

### Sequence map

| Email | Send delay | Discount |
|-------|-----------|----------|
| 1 | When entering segment | None — re-engagement |
| 2 | 7 days after email 1 | 10% (code: COMEBACK10) |
| 3 | 14 days after email 1 | 15% (code: WEMISSEDU15) — final |

### Per-email spec

#### Email 1 — Soft re-engage

**Subjects:**
1. Long time, {{ first_name }}
2. We've added 400 new styles since you last shopped
3. {{ first_name|default:'Hey' }} — quick update from Aydins

**Body:**

> {{ first_name|default:'There' }} —
>
> It's been a while. Hope the ring's holding up.
>
> Quick update on what's new at Aydins since you last visited:
>
> - **400+ new styles** — including tungsten meteorite inlays, ceramic carbon fiber, and a new 14k gold collection.
> - **Faster shipping** — most orders out the door in 24 hours.
> - **Lifetime warranty still stands** — if your original ring needs replacement, reply and we'll handle it.
>
> [BUTTON: See what's new →]
>
> — Amir
> Aydins Jewelry

#### Email 2 — Soft offer (Day 7)

**Subjects:**
1. 10% off, on us — code COMEBACK10
2. A small thank you for being a customer
3. Anniversary band? Second ring? 10% off

**Body:**

> {{ first_name|default:'There' }},
>
> If you've been thinking about a second ring — gym ring, anniversary band, gift for a friend — here's a small nudge:
>
> Code **COMEBACK10** — 10% off your next order.
>
> [BUTTON: Browse the catalog →]
>
> No expiration. Use it when you're ready.
>
> — Amir

#### Email 3 — Final 15% (Day 14)

**Subjects:**
1. Last one — 15% off, no expiration tricks
2. Final note from Aydins
3. {{ first_name|default:'Hey' }} — one more

**Body:**

> {{ first_name|default:'There' }},
>
> One more. Then I'll let you go.
>
> Code **WEMISSEDU15** — 15% off any order. The biggest discount we offer.
>
> [BUTTON: Browse →]
>
> If you'd rather not hear from us at all — totally fine, just hit unsubscribe at the bottom. No hard feelings.
>
> — Amir
> Aydins Jewelry

### Klaviyo UI setup

1. **Lists & Segments → Create Segment**
2. Name: `Inactive Buyers (180+ days)`
3. Definition: `Placed Order at least once over all time AND Placed Order zero times in the last 180 days`
4. Save
5. **Flows → Create Flow → Triggered by Segment**
6. Pick the "Inactive Buyers" segment
7. Build 3 emails with the timings above
8. Set to Live

**Important caveat:** Sending to dormant subscribers can spike your spam complaint rate. Klaviyo's deliverability dashboard will flag it. Mitigations:
- Send the win-back in **batches** (limit segment to 5,000/week using Klaviyo's "Sending Rate" setting in Settings → Domain reputation)
- Make sure DKIM and dedicated sending domain are set up (see Section 0.3)
- Monitor unsubscribe and complaint rate after launch — pause if complaint rate goes above 0.3%

---

## FLOW 7 — Back in Stock & Price Drop

### Why it matters

Shopify makes a "Notify me" form trivial to wire to Klaviyo. Anyone who signs up has shown intent on a specific SKU. Conversion rates on back-in-stock notifications are 20–30%. Price drop is similar — flag a customer's wishlist item when it goes on sale.

### Setup overview

This is technically two flows, both triggered by Klaviyo's built-in **"Back in Stock"** subscriber feature.

#### 7a — Back in Stock

1. Install Klaviyo's free **"Back in Stock"** Shopify app from the Shopify app store
2. Configure it to add a "Notify me" button on every sold-out product variant
3. Klaviyo auto-creates the trigger: when inventory > 0 for a SKU someone subscribed to, fire a flow
4. Flow content:

**Email 1 (immediate):**
- Subject: It's back — {{ event.product_name }} is in stock
- Body: Short, urgent. Image, "back in stock" line, button to product page. No discount needed — they wanted it at full price.

#### 7b — Price Drop

Klaviyo doesn't natively support price drop notifications without a third-party app. Skip this for now — the dollar value isn't there for a wedding band store where prices are stable. Revisit only if you start running aggressive sales.

---

## Klaviyo features jewelry stores miss (that you should set up)

### 1. **Predicted Customer Lifetime Value (CLV) — for segmentation**
Klaviyo's predictive analytics calculate expected CLV per customer. Use it to:
- Tag your top 20% predicted CLV as "VIP" → exclusive early access emails, no discounts (preserve margin)
- Tag the bottom 50% as "discount-driven" → only email with promos

**Setup:** Lists & Segments → Create Segment → Filter: `Predicted CLV is greater than $400` → Save as "VIP"

### 2. **SMS opt-in inside email flows**
Layer SMS into your top revenue flow (Abandoned Checkout). Klaviyo lets you add an SMS step inside an email flow. SMS open rate is 95%+, click rate is 19% (vs 2% for email). Even 5% of your subs opting into SMS recovers 10x more abandoned carts than the email alone.

**Setup:** In your Abandoned Checkout flow, add an SMS step at hour 8 (between email 2 and email 3). Use Klaviyo's SMS module ($25/mo at your size). Get TCPA-compliant consent via the Recart popup or checkout SMS opt-in checkbox.

### 3. **Forms — beyond the popup**
Right now your only signup point is Recart. Add a Klaviyo form to:
- The footer of every page (passive — captures the 1-2% who scroll there)
- The order confirmation page (capture the 30-50% of buyers who don't tick the marketing checkbox)
- An exit-intent secondary popup with a different angle (e.g., "Get a free ring sizer" instead of "20% off")

**Setup:** Klaviyo → Sign-Up Forms → Create Form → Choose template → Configure targeting

### 4. **Catalog feed for dynamic product blocks**
Make sure your Shopify products are syncing to the Klaviyo catalog. This is what makes dynamic product blocks possible (the recommended-products grids in your emails). Without it, you're stuck hand-coding every product.

**Verify:** Klaviyo → Catalog → confirm "Shopify" feed is connected and showing 1,191 products.

### 5. **Suppression of recent buyers from campaigns**
When you blast a promotional campaign (Black Friday, anniversary sale), exclude customers who bought in the last 30 days. Nothing screams "I just got ripped off" like buying at full price and then getting a 25%-off email a week later.

**Setup:** Every campaign send → "Exclude" → segment "Placed Order in last 30 days"

### 6. **Engagement-based deliverability protection**
Don't send promotional emails to subscribers who haven't opened anything in 90+ days. They drag down your sender reputation, hurting open rates for the buyers who DO want to hear from you.

**Setup:** Create segment "Highly Engaged" = `Opened Email at least once in last 90 days OR Clicked Email at least once in last 90 days`. Send promotional campaigns ONLY to this segment. Send win-back to the unengaged segment separately.

### 7. **Anniversary date triggers**
For wedding ring customers, the wedding anniversary is the single most powerful date you have. A "Happy 1-year anniversary — here's a polish kit on us" email a year after purchase is gold. Klaviyo lets you trigger flows on a date property.

**Setup:** When an order ships, write `wedding_anniversary` as a custom property on the customer profile (date = order date, since they likely got married within ±2 weeks of buying). Build a flow triggered annually on that date.

---

## Customer segments to create (do these once, use forever)

Build these in **Lists & Segments → Create Segment**:

| Segment | Definition | Use for |
|---------|------------|---------|
| **VIP — Predicted CLV $400+** | `Predicted CLV ≥ $400` | Early access, no-discount campaigns |
| **First-time buyers (last 30d)** | `Placed Order = 1 over all time AND placed within 30d` | Onboarding nurture |
| **Repeat buyers** | `Placed Order ≥ 2 over all time` | Referral asks |
| **Highly engaged** | `Opened or Clicked email in last 90d` | Promotional campaigns |
| **Unengaged (sunset risk)** | `No open or click in last 90d` | Win-back / sunset only |
| **Inactive buyers (180+ days)** | `Placed Order ≥ 1 lifetime AND zero in last 180d` | Win-back flow |
| **Tungsten buyers** | `Ordered Product where vendor = "UJ" OR vendor = "UJC"` | Tungsten-specific care emails, cross-sell tungsten styles |
| **Gold buyers** | `Ordered Product where vendor = "Jewelry Depot"` | Gold-specific care, anniversary upgrade |
| **Cart abandoners (active)** | `Started Checkout in last 7d AND Placed Order zero in last 7d` | Last-resort manual sends |
| **Subscribers who never bought** | `Subscribed AND Placed Order = 0 lifetime` | Welcome series re-runs, conversion campaigns |

---

## Best email templates / layouts for jewelry e-com 2026

These are the patterns that consistently outperform across the jewelry vertical (data from Klaviyo benchmarks, Shopify Plus partner case studies, and 2025 e-com email teardowns):

### Layout A — "Hero + Single Product" (best for new launches, abandoned checkout)
- Full-width hero image (the ring on a hand or in clean macro)
- Single bold headline
- One product card below
- Single CTA
- Short footer

### Layout B — "3-up Grid" (best for collection pushes, browse abandonment)
- Header with logo
- 3-column product grid (image / name / price / "Shop" button per cell)
- Single tagline at top
- Footer

### Layout C — "Letter from Owner" (best for storytelling, welcome, win-back)
- Plain-text-feeling email (less imagery, more body copy)
- Personal sign-off ("— Amir, Owner, Aydins Jewelry")
- Single soft CTA at the bottom
- Often outperforms designed emails 2:1 on click rate for emotional buys (wedding rings are emotional buys)

### What does NOT work for jewelry email in 2026
- ❌ Overly designed "magazine-style" newsletters — feel impersonal
- ❌ Multiple competing CTAs in one email — destroys click rate
- ❌ Stock photography of generic couples — destroys trust
- ❌ Discount-only positioning ("SAVE 30%! BLOWOUT! ENDS SOON!") — destroys brand perception
- ❌ Emojis in subject lines for premium positioning — kills trust
- ❌ All-image emails (no plain text) — flagged by spam filters AND can't be read on slow connections

---

## Master implementation timeline

### Week 1 (Days 1–7)
- ☐ Confirm Shopify ↔ Klaviyo integration is wired (Section 0)
- ☐ Build & verify master template
- ☐ Verify DKIM + dedicated sending domain
- ☐ Build Abandoned Checkout flow (Flow 1) — set Live

### Week 2 (Days 8–14)
- ☐ Turn off Recart welcome email
- ☐ Build Welcome Series (Flow 2) — set Live
- ☐ Audit campaign-suppression segments

### Week 3 (Days 15–21)
- ☐ Build Browse Abandonment (Flow 3) — set Live
- ☐ Build Abandoned Cart (Flow 4) — set Live
- ☐ Tag Shopify products with `material:tungsten`, etc., for dynamic post-purchase content

### Week 4 (Days 22–30)
- ☐ Build Post-Purchase (Flow 5) — set Live
- ☐ Build Win-Back (Flow 6) — set Live (start with batched sending)
- ☐ Install Back in Stock app + build Flow 7
- ☐ Set up the 10 customer segments

### Days 31–60 — optimize
- ☐ Review every flow's open rate, click rate, conversion rate
- ☐ A/B test one subject line per flow (Klaviyo built-in A/B feature)
- ☐ Add SMS module to Abandoned Checkout
- ☐ Build first manual promotional campaign — Memorial Day or Father's Day push, segmented to "Highly Engaged"

---

## What to expect in revenue terms

Conservative monthly lift from this full Klaviyo build, based on industry benchmarks for a store at your size, traffic, and current conversion rate:

| Flow | Conservative monthly $ recovered |
|------|----------------------------------|
| Abandoned Checkout | $2,000–$5,000 |
| Welcome Series | $1,500–$3,000 |
| Browse Abandonment | $500–$1,500 |
| Abandoned Cart | $300–$800 |
| Post-Purchase (review-driven downstream) | $500–$1,000 |
| Win-Back | $800–$2,000 |
| Back in Stock | $200–$500 |
| **Total (low end)** | **$5,800/mo** |
| **Total (high end)** | **$13,800/mo** |

That's email channel attribution. **20–35% of total store revenue should come from email** once this is fully built and seasoned for 60 days. Right now it's almost certainly under 5%.

If after 60 days the email channel is below 15% of total revenue, the diagnosis is one of:
- Deliverability (DKIM, sending reputation, spam complaints) → check Klaviyo's deliverability dashboard
- Subject lines (open rate < 30% on warm flows) → A/B test more aggressively
- Content (click rate < 2% on emails opened) → revisit body copy and CTA placement

---

## Pickup checklist (when you start implementing)

- [ ] Read Section 0 in full and verify the integration before building anything
- [ ] Build the master template ("Aydins Master 2026") and save it
- [ ] Build Flow 1 (Abandoned Checkout) — test with a real abandoned cart from incognito
- [ ] Confirm email arrived and discount code worked end-to-end
- [ ] Set Flow 1 to Live
- [ ] Repeat weekly per the timeline

---

## Companion: see [[(C) Traffic & Conversion Audit]]

That report covers the on-site / paid / SEO side. This one covers the owned-audience / email side. Together they cover the full revenue stack. The two reports should be read as one strategy, not two separate documents.

— End of playbook —
