# (C) Klaviyo Flow Rewrite Plan — v2 (Verified-Policy Rebuild)

> **Source of truth for every claim:** [[(C) Aydins Policies — Source of Truth]]
> **Replaces:** v1 of this doc, which contained fabricated claims ("lifetime warranty included," "30-day free returns," "we resize free for life"). v1 is dead. This is the live plan.
> **Last updated:** 2026-05-08

---

## The locked Aydins Trust Block

This exact paragraph appears (with minor formatting variations) in every customer-facing email. No deviation without re-checking the policies file.

> Free engraving. Free U.S. shipping. Free exchange in the first 30 days. Lifetime Warranty against breaks and defects — free for 6 months, then $34.50, then $54.50 flat. Lifetime Sizing if your finger ever changes — for a small flat fee, no time limit. We've been doing this since 2011, out of our Dallas-area workshop.

**Rules:**
- Use as a single block. Don't break it apart.
- Don't paraphrase the warranty fee structure — the dollar amounts disclose the truth and protect us legally.
- Lifetime Sizing always carries the "small flat fee, no time limit" qualifier — never naked.
- Don't add "lifetime warranty" anywhere outside this block.
- Don't use the word "guaranteed" attached to fit, sizing, or warranty.
- Transactional emails (Order Confirm, Shipping Confirm) get a shortened version at the bottom — not the full block.

---

## Push order (urgency-ranked)

| # | Email | Message ID | Status | Why this order |
|---|---|---|---|---|
| 1 | Abandoned Cart 1 | `SQdgLg` | LIVE — actively shipping false claims | Stop the leak first |
| 2 | Abandoned Cart 2 | `UCDagK` | LIVE — actively shipping false claims | Stop the leak |
| 3 | Abandoned Cart 3 | `UJLFPZ` | LIVE — actively shipping false claims | Stop the leak |
| 4 | Welcome 1 | `TzFzsG` | LIVE | Highest-volume entry point |
| 5 | Welcome 2 | `SWEwQ5` | LIVE | |
| 6 | Welcome 3 | `SjDuds` | LIVE | |
| 7 | Welcome 4 | `VUvfeq` | LIVE | |
| 8 | Thank You 1 | `TQrkhz` | LIVE | |
| 9 | Thank You 2 | `UZQbbr` | LIVE | |
| 10 | Browse Abandonment | `T6q2n5` | LIVE | |
| 11 | Customer Winback 1 | `WiJLsV` | LIVE — pause flow first | Pause flow before edits |
| 12 | Customer Winback 2 | `QQPRA6` | LIVE — pause flow first | Pause flow before edits |
| 13 | Order Confirmation | `RRHrAp` | DRAFT | Push when activating |
| 14 | Shipping Confirmation | `RYus5L` | DRAFT | Push when activating |

---

## Flow 2 — Abandoned Cart (URGENT)

### Email 1 — `SQdgLg`

**Subject:** Still thinking it over? Here's 20% off — code EMK20
**Preview:** Free engraving, free U.S. shipping, free exchange in the first 30 days. Code expires at midnight.

**Body:**

> ## A small thank-you: 20% off, until midnight
>
> Great rings take thought. Here's **20% off — code EMK20**, good through 11:59 PM tonight.
>
> [Return to cart →]
>
> *(cart line items render here)*
>
> ---
>
> *[Trust Block]*
>
> ---
>
> Sizing? Use our [Find Your Ring Size →](https://shopaydins.com/pages/find-your-ring-size) tool on your phone.
> Engraving questions? Just reply to this email.
>
> [Use code EMK20 — return to cart →]

### Email 2 — `UCDagK`

**Subject:** Your handcrafted ring is nearly ready
**Preview:** A few minutes to finish, and we'll start cutting it in the workshop.

**Body:**

> ## Your piece is waiting at the workshop.
>
> Thanks for considering Aydins. Whenever you're ready to finish, we'll start cutting it.
>
> [Resume Checkout →]
>
> *(cart items)*
>
> ---
>
> *[Trust Block]*
>
> ---
>
> ★★★★★ "The engraving came out perfect — couldn't be happier with the craftsmanship and fit." — Michael R., Dallas TX
>
> *(product feed)*

### Email 3 — `UJLFPZ`

**Subject:** Last call — your piece is still set aside
**Preview:** Since 2011, every Aydins ring has been made by hand. Yours is ready when you are.

**Body:**

> ## Last call to reserve your piece
>
> Since 2011, our small team has turned raw metal into rings people wear for the rest of their lives. Yours is set aside, but space in the workshop is limited.
>
> [Complete My Order →]
>
> *(cart items)*
>
> ---
>
> *[Trust Block]*
>
> ---
>
> *(product feed)*

---

## Flow 1 — Welcome Series

### Email 1 — `TzFzsG`

**Subject:** Welcome to Aydins. Here's 20% off your first ring.
**Preview:** Code 20_OFF2 — and a few things you should know about how we make rings.

**Body:**

> ## Welcome to Aydins.
>
> You just joined a workshop that's been making men's wedding bands and custom rings since 2011 — most of it built to order, by hand.
>
> Here's **20% off** your first piece — code **{% coupon_code '20_OFF2' %}** at checkout.
>
> [Shop now →]
>
> ---
>
> *[Trust Block]*
>
> ---
>
> *(product feed: most-ordered pieces)*
>
> Questions on sizing, materials, or a custom idea? Reply to this email — a real person reads every one.
>
> — Aydin

### Email 2 — `SWEwQ5`

**Subject:** Reminder: your 20% Aydins code is still active
**Preview:** Code 20_OFF2 — good for any ring in the workshop.

**Body:**

> ## Still browsing?
>
> Your welcome code is still good. **20% off** any piece — code **{% coupon_code '20_OFF2' %}** at checkout.
>
> [Shop now →]
>
> ---
>
> *[Trust Block]*
>
> ---
>
> *(product feed)*
>
> Reply here if there's a question — sizing, materials, custom work. We answer everything.
>
> — Aydin

### Email 3 — `SjDuds`

**Subject:** A few places to follow the workshop
**Preview:** New pieces, custom rings, and behind-the-scenes from our Dallas-area workshop.

**Body:**

> ## A few places to find us
>
> Most of what we make never makes it to the storefront — custom rings, fingerprint pieces, one-off Damascus builds. If you want to see those, the best place is on our social channels.
>
> *(facebook / instagram / pinterest icons)*
>
> ---
>
> *[Trust Block]*
>
> — Aydin

### Email 4 — `VUvfeq`

**Subject:** A few of our most-ordered pieces
**Preview:** The pieces customers come back for — handpicked from the workshop.

**Body:**

> ## A few of our most-ordered pieces
>
> Out of everything we've made since 2011, these are the rings customers keep coming back for. If you're not sure where to start, start here.
>
> [Shop now →]
>
> *(best sellers feed)*
>
> ---
>
> *[Trust Block]*
>
> ---
>
> Need something custom? Reply to this email — we build a lot of one-off pieces.

---

## Flow 4 — Customer Thank You

### Email 1 — `TQrkhz`

**Subject:** Your order is in the workshop, {{ person.first_name }}.
**Preview:** Here's what happens next — and what's covered for the long run.

**Body:**

> ## Thank you, {{ person.first_name }}.
>
> Your order is in the workshop. Here's how the next few days look.
>
> 1. We start crafting your piece by hand.
> 2. Engraving is cut with a precision laser.
> 3. The piece is inspected and packaged at our Dallas-area workshop.
> 4. Tracking lands in your inbox once it ships — usually within 1–3 business days.
>
> ---
>
> *[Trust Block]*
>
> ---
>
> Engraving questions or anything custom — reply here or write sales@shopaydins.com.
>
> — The Aydins Jewelry Team

### Email 2 — `UZQbbr` (repeat customer)

**Subject:** Thank you for coming back, {{ person.first_name }}
**Preview:** Returning customers are why we still do this.

**Body:**

> ## Thank you for coming back, {{ person.first_name }}.
>
> Returning customers are the reason we've kept the workshop running since 2011. Your order is in good hands.
>
> 1. We start crafting it by hand.
> 2. Engraving is cut with a precision laser.
> 3. The piece is inspected and packaged at our Dallas-area workshop.
> 4. Tracking lands in your inbox once it ships — usually 1–3 business days.
>
> ---
>
> *[Trust Block]*
>
> ---
>
> Anything we can help with — a sizing question, a gift idea, custom work — reply here or write sales@shopaydins.com.
>
> — The Aydins Jewelry Team

---

## Flow 5 — Browse Abandonment

### Email 1 — `T6q2n5`

**Subject:** That piece you were looking at
**Preview:** Free engraving, free shipping, made in our Dallas-area workshop.

**Body:**

> ## That piece is still here.
>
> You were looking at one of our pieces — figured we'd send a quick note in case you still want it.
>
> *(viewed item)*
>
> ★★★★★ "Exactly what I hoped for. The quality was incredible and the service was top-notch. Arrived fast and beautifully packaged." — Marcus G., Verified Buyer
>
> [View My Item →]
>
> ---
>
> *[Trust Block]*
>
> ---
>
> *(product feed)*

---

## Flow 3 — Customer Winback

⚠️ **Pause the flow (`QVt7Vu`) before editing the templates.** Set status to `draft` via API, edit, re-activate. Don't leave a half-edited live flow firing on customers.

### Email 1 — `WiJLsV`

**Subject:** It's been a while
**Preview:** A few new pieces from the workshop you haven't seen yet.

**Body:**

> ## A few new pieces from the workshop
>
> It's been a while. Here are some of the pieces we've made since you last looked.
>
> *(product feed)*
>
> ---
>
> *[Trust Block]*
>
> ---
>
> Reply if there's something specific you're after — we make a lot of custom pieces that never hit the storefront.
>
> — Aydin

### Email 2 — `QQPRA6`

**Subject:** We've missed you — here's what's new
**Preview:** A handful of pieces picked for you.

**Body:**

> ## We've missed you.
>
> Since you've been gone, the workshop has been busy. Here are a few pieces we think you'd like.
>
> *(product feed)*
>
> ---
>
> *[Trust Block]*
>
> ---
>
> If there's anything we can help with — sizing, custom work, a question on a past order — just reply.
>
> — Aydin

---

## Flow 6 — Order Confirmation (DRAFT)

### Email — `RRHrAp`

**Subject:** Order confirmed — thank you, {{ event.customer.first_name }}
**Preview:** Order #{{ event.extra.order_number }} confirmed. Here's what happens next.

**Body:**

> ## Thank you for your order
>
> Your order **#{{ event.extra.order_number }}** is confirmed. We've started preparing it at the workshop.
>
> [Track Your Order →]
>
> ---
>
> *(order details — line items / subtotal / shipping / tax / total)*
> *(shipping address / customer info / order notes)*
>
> ---
>
> Need help? Call **1-800-214-7345** or email **sales@shopaydins.com**.
>
> ---
>
> *[Short Trust Block:]*
> *Free engraving. Free U.S. shipping. Free exchange in the first 30 days. Lifetime Warranty and Lifetime Sizing on every Aydins piece. Since 2011.*

---

## Flow 7 — Shipping Confirmation (DRAFT)

### Email — `RYus5L`

**Subject:** Your Aydins order has shipped
**Preview:** Tracking inside — shipping from our Dallas-area workshop.

**Body:**

> ## Your order is on its way
>
> Hi {{ event.extra.customer.default_address.first_name }},
>
> Order **#{{ event.extra.order_number }}** has shipped:
>
> *(line items)*
>
> Headed to:
> *(shipping address)*
>
> Tracking #: **{{ event.extra.fulfillments.0.tracking_number }}**
>
> [Track Your Package →]
>
> Allow a few hours for the tracking status to update.
>
> ---
>
> *[Short Trust Block:]*
> *Free engraving. Free U.S. shipping. Free exchange in the first 30 days. Lifetime Warranty and Lifetime Sizing on every Aydins piece. Since 2011.*
>
> Thanks again — we appreciate you.
>
> — The Aydins Jewelry Team

---

## API push procedure

For each email above:

1. **Update flow-message subject + preview** via Klaviyo REST API (`PATCH /api/flow-messages/{message_id}`).
2. **Update template HTML body** via `PATCH /api/templates/{template_id}` — replacing the `<body>` content with the rewritten HTML.
3. **For Customer Winback flow only:** PATCH `/api/flows/QVt7Vu/` status → `draft`, edit messages, then PATCH back to `live`.

API key: stored in MCP config. Use the Klaviyo MCP tools (`mcp__klaviyo__*`) where possible, fall back to `curl` for endpoints the MCP doesn't cover.

---

## Self-check protocol (before each push)

For every email body, confirm:

- [ ] No "lifetime warranty included" without the fee disclosure.
- [ ] No "free exchanges" without "within 30 days" qualifier.
- [ ] No "we resize for life" or "free lifetime resizing."
- [ ] No "30-day free returns and exchanges" (returns aren't free).
- [ ] No "guaranteed" attached to fit / sizing / warranty.
- [ ] No third-party brand names (no Thorsten, no Universal Jewelry).
- [ ] No emoji clutter — restraint per Aydins design system.
- [ ] Trust Block is exact, not paraphrased.
- [ ] CTA URLs verified.
