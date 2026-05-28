# Recart Dead Flows — Revamp Spec

> **Compiled:** 2026-05-13
> **Purpose:** Build out the 3 flows currently sending $0 — Order & Receipt, Fulfillment Notifications, Custom Triggers
> **Execution:** Copy-paste this spec into Recart's flow editor. ~90 minutes total.

---

## Pre-flight (do these once before building any flow)

- [ ] **Settings → SMS → Smart sending: change 0 → 8 hours.** Single biggest opt-out reducer.
- [ ] **Settings → SMS: archive disconnected second TFN.** Clean account.
- [ ] **Confirm with Recart support: which transactional flows respect quiet hours.** Order/fulfillment SMS can typically send 24/7 because they're triggered transactional, but verify.
- [ ] **Verify in `(C) Aydins Policies — Source of Truth`:** is "price match guarantee" a real policy? Does Aydins actually carry 14k gold? (These will affect copy.)

---

## Policy-locked language reference (use exact wording)

| Concept | NEVER write | ALWAYS write |
|---|---|---|
| Warranty | "lifetime warranty" | "Free warranty for the first 6 months. Extended coverage available — $34.50 (6-12mo), $54.50 (12mo+)." |
| Resizing | "free lifetime resizing" | "Lifetime Sizing Program — $34.50 year 1, $54.50 after. Sizing reassurance for the lifetime of your ring." |
| Returns | "30-day free returns" | "30-day returns. $25 restocking fee, customer pays return shipping. Engraved items final sale." |
| Maker | "handcrafted / forged / made by hand" | "engraved and shipped from our Texas workshop" (or just describe what they DO get) |
| Founded | "Since 2003" / "for over 20 years" | "Since 2011" / "Family-owned, established 2011" |
| Brand name | "Aydin's Jewelry" | "Aydins Jewelry" (no apostrophe) |
| Engraving | n/a | "Free laser engraving on every ring" |
| Shipping | n/a | "Free insured 2-business-day shipping" |

---

# FLOW 1 — Order & Receipt

**Why this matters:** Customer just bought. They're in the highest trust + highest anxiety window of the entire journey. Confirmation + reassurance + setup for the next purchase. Currently $0 attributed. Expected ceiling: **$2-5k/mo** once dialed.

## Trigger

`Order placed` (any order, any product)

## Sequence

### Msg 1 — Order confirmation (SMS, immediate)

**Send:** 0 minutes after order placed
**Type:** SMS

> Aydins Jewelry: Order confirmed! 🎉 We've got your ring and we'll send tracking the moment it ships. Questions about your order? Reply to this text — a real person reads every message. Order details: {{order_status_url}}

**Notes:**
- Uses Recart merge tag `{{order_status_url}}` (verify exact syntax in Recart docs — may be `{order_status_url}` or similar)
- "A real person reads every message" — high-trust signal, costs nothing to write, huge for first-time buyers
- No discount code (don't undercut the purchase they just made)
- No "STOP to opt out" needed on transactional, but check Recart's auto-append behavior

### Msg 2 — Engraving confirmation branch (CONDITIONAL — only if order has engraving)

**Send:** 30 minutes after order placed
**Condition:** Order contains line-item property "engraving" OR cart tag includes "engraving"
**Type:** SMS

> Aydins Jewelry: Just confirming the engraving on your order — "{{engraving_text}}" in {{engraving_font}}. If anything looks off, reply here within 24 hours and we'll update before production. After 24 hours, engraving is locked.

**Notes:**
- This single message prevents the #1 customer service ticket category for engraved rings ("wait, did I spell it right?")
- Reduces returns/exchanges on engraved rings (which are final sale per policy)
- If Recart can't pull `{{engraving_text}}` from order properties, fall back to: "Just confirming the engraving on your order. If anything looks off, reply here within 24 hours and we'll update before production."

### Msg 3 — "What happens next" (SMS, 2 hours after order)

**Send:** 2 hours after order placed
**Type:** SMS

> Aydins Jewelry: Here's what's next — your ring is being prepped and engraved (if applicable). You'll get a shipping notification with tracking in 1-2 business days. Total delivery time: typically 3-5 business days from order. Hang tight. 💍

**Notes:**
- Sets expectations explicitly. Reduces "where's my order" tickets.
- "Hang tight 💍" is brand voice — polished but human

### Msg 4 — Care + cross-sell setup (MMS, 24 hours after order)

**Send:** 24 hours after order placed
**Type:** MMS
**Image:** Single ring on hand, lifestyle shot (not the infographic — keep this human and aspirational)

> Aydins Jewelry: While you wait — here's a quick care tip 👇
>
> Tungsten and ceramic rings are nearly indestructible, but engraved details last longest when you remove the ring for: heavy gym sessions, beach sand, swimming pools. That's it. Day-to-day life — including showers, dishes, and sleep — totally fine.
>
> See the full care guide: {{care_guide_link}}

**Notes:**
- Provides value, not a sell
- Sets up trust for the post-purchase / retention flow
- `{{care_guide_link}}` — needs a real URL: build a single page at shopaydins.com/pages/ring-care if it doesn't exist
- DELETE Msg 4 entirely if you don't have a real care guide page yet — empty link kills trust

## Flow 1 — Expected performance

- 4 messages × ~250-500 orders/mo (estimate) = 1,000-2,000 sends/mo
- Conservative ROI target: 30-50X (because there's no discount, just trust-building)
- Expected lift: $2-5k/mo in incremental attribution

---

# FLOW 2 — Fulfillment Notifications

**Why this matters:** Ring is in transit. Customer is checking their phone. Captive attention. Currently $0 attributed. Expected ceiling: **$3-6k/mo**.

## Trigger

`Order fulfilled` (when Shopify marks order shipped)

## Sequence

### Msg 1 — Shipped (SMS, immediate on fulfillment)

**Send:** 0 minutes after fulfillment
**Type:** SMS

> Aydins Jewelry: Your ring is on its way! 📦 Track it here: {{tracking_link}}. Estimated delivery: {{estimated_delivery_date}}. Reply to this text if you need anything.

**Notes:**
- Standard ship notification. Recart should pull tracking from Shopify automatically.
- If `{{estimated_delivery_date}}` isn't a Recart variable, fall back to: "Estimated delivery: 2-3 business days from now."

### Msg 2 — Out for delivery (SMS, triggered on tracking status change)

**Send:** Triggered when tracking status = "Out for delivery"
**Type:** SMS

> Aydins Jewelry: Your ring is out for delivery today 🚚. Make sure someone's around to grab it. Track: {{tracking_link}}

**Notes:**
- Only works if Recart can listen to tracking webhooks from Shopify/your carrier. If not available, skip this message and go straight to Msg 3.
- High open rate window — people watch this one closely

### Msg 3 — Delivered + review setup (SMS, immediate on delivery)

**Send:** 0 minutes after tracking = "Delivered"
**Type:** SMS

> Aydins Jewelry: Delivered! 🎉 Hope it's everything you wanted. Try it on — if the fit isn't perfect, our Lifetime Sizing Program has you covered ($34.50 year 1, $54.50 after). Questions? Reply here.

**Notes:**
- Sets up the Lifetime Sizing program offer at the exact moment they discover fit issues
- Soft mention of the paid program — not aggressive, just informational
- No review ask yet (too early — they haven't worn it)

### Msg 4 — Wear-it-in check-in (SMS, 3 days after delivery)

**Send:** 3 days after `Delivered` status
**Type:** SMS

> Aydins Jewelry: How's the ring fitting after a few days of wear? 💍 Two things worth knowing:
>
> 1. Sizing not perfect? Lifetime Sizing Program — $34.50 year 1, $54.50 after.
> 2. Loving it? A quick review helps other guys find us: {{review_link}}
>
> Either way — thanks for trusting us.

**Notes:**
- Splits intent: dissatisfied → sizing program path; happy → review path
- "Trusting us" — closes the loop on the journey

### Msg 5 — Soft cross-sell (MMS, 14 days after delivery)

**Send:** 14 days after `Delivered` status
**Type:** MMS
**Image:** 2-3 complementary rings (couples' set, matching family band, or stack-mate)

> Aydins Jewelry: Now that you've worn yours in — a thought:
>
> Most of our customers come back within 6 months for a second ring. Anniversary band, gift for a brother, matching set for a partner. If that's on your radar, here are 3 that pair well with what you bought:
>
> {{recommended_products_link}}
>
> Engraving is free, always.

**Notes:**
- Honest framing ("most of our customers come back") — true if it's true; verify against your data before sending
- `{{recommended_products_link}}` — needs a smart link. Easiest version: link to a curated "complete the set" collection
- "Engraving is free, always." — brand reinforcement, no hard sell

## Flow 2 — Expected performance

- 4-5 messages × ~250-500 orders/mo = 1,250-2,500 sends/mo
- Target ROI: 40-80X
- Expected lift: $3-6k/mo

---

# FLOW 3 — Custom Triggers (High-Intent Browse Flow)

**Why this matters:** Browsers who view but don't buy are leaving money on the table. Recart's Custom Triggers let you fire SMS off specific behaviors. Currently $0 attributed — likely because it's not configured against any meaningful event. Expected ceiling: **$1-3k/mo**.

## Trigger options (pick 1-2 to start, don't run all)

| Trigger | Why it works | Setup |
|---|---|---|
| **A. Viewed same product 3+ times in 7 days** | Strong intent signal — they're thinking about it | Recart event: `product_viewed` with frequency rule |
| **B. Added to cart but didn't checkout** | Already in abandonment, but this is a softer touch | Recart event: `added_to_cart` |
| **C. Viewed engravable ring + spent 60+ sec on page** | High-intent engraving consideration | Requires page-time tracking — check if Recart supports |

**Recommendation: Start with Trigger A.** Cleanest signal, easiest to set up, highest expected lift.

## Sequence (assuming Trigger A: 3+ views in 7 days)

### Msg 1 — Soft nudge (SMS, 1 hour after 3rd view)

**Send:** 1 hour after triggering event
**Type:** SMS

> Aydins Jewelry: Caught you looking at {{product_name}} a few times 👀. No pressure — just wanted to make sure you know:
>
> - Free laser engraving included
> - Free insured 2-day shipping
> - 30-day returns (engraved items are final sale)
>
> Take another look: {{product_url}}

**Notes:**
- "Caught you looking" — direct without being creepy. Human voice.
- No discount in Msg 1 — preserves margin and the discount becomes more meaningful in Msg 2 if needed
- `{{product_name}}` and `{{product_url}}` — verify Recart pulls these from the view event

### Msg 2 — Conditional discount (SMS, 48 hours later, if no purchase)

**Send:** 48 hours after Msg 1
**Condition:** Has not purchased
**Type:** SMS

> Aydins Jewelry: Still on the fence about {{product_name}}? Here's 15% off to help you decide — code: BROWSE15. Expires in 48 hours.
>
> {{product_url}}
>
> Reply STOP to opt out.

**Notes:**
- 15% is lighter than the 20% welcome discount — protects the welcome offer's perceived value
- Time-limited (48hr) — creates real urgency
- `BROWSE15` discount code needs to be created in Shopify first

### Msg 3 — Last touch (SMS, 48 hours after Msg 2, if still no purchase)

**Send:** 48 hours after Msg 2
**Condition:** Has not purchased
**Type:** SMS

> Aydins Jewelry: Code BROWSE15 expires tonight. After this, we'll stop bugging you about {{product_name}}. If now's not the right time — totally fine. We'll be here when it is.
>
> {{product_url}}

**Notes:**
- "We'll stop bugging you" — explicit, respects the customer, reduces opt-outs from this flow
- Honest framing builds long-term trust even when they don't buy

### Exit conditions

- Customer purchases → exit flow immediately
- Customer opts out → exit flow
- Flow completes (Msg 3 sent) → exit, don't re-enter for 30 days

## Flow 3 — Expected performance

- 3 messages × ~200-400 triggered subscribers/mo (estimate, depends on traffic volume)
- Target ROI: 20-40X (lower because it includes a 15% discount)
- Expected lift: $1-3k/mo

---

## Execution checklist

### Today (30 min)
- [ ] Settings → SMS → Smart sending = 8 hours
- [ ] Archive disconnected TFN
- [ ] Verify `price match guarantee` is real policy (or remove from existing welcome flow)
- [ ] Verify Aydins actually sells 14k gold (or remove from existing welcome flow)

### This week (90 min — one focused session in Recart)
- [ ] Build FLOW 1 — Order & Receipt (4 messages)
- [ ] Build FLOW 2 — Fulfillment Notifications (4-5 messages)
- [ ] Build FLOW 3 — Custom Triggers (3 messages, Trigger A only to start)
- [ ] Create `BROWSE15` discount code in Shopify
- [ ] Build or confirm `/pages/ring-care` page exists for Flow 1 Msg 4

### Next week (60 min — fix existing welcome flow)
- [ ] Replace MMS Msg 3 image — remove "Family Owned Since 2003," "Lifetime Warranty," "Lifetime Sizing" badges
- [ ] Rewrite "Has no abandoned cart" SMS (the lifetime warranty exposure)
- [ ] Find-replace "Aydin's" → "Aydins" across 5 messages
- [ ] If price-match isn't real: rewrite Path A and Path B without the claim

### Week 3 (verification)
- [ ] Pull 7-day performance on all 3 new flows
- [ ] Adjust copy on weakest message based on CTR
- [ ] Decide if Trigger B (cart-add) should be layered onto Custom Triggers

---

## Total expected impact

| Flow | Current | Target (3-6mo) | Lift |
|---|---|---|---|
| Order & Receipt | $0/mo | $2-5k/mo | NEW revenue |
| Fulfillment Notifications | $0/mo | $3-6k/mo | NEW revenue |
| Custom Triggers (Browse) | $0/mo | $1-3k/mo | NEW revenue |
| **Total new SMS revenue** | **$0/mo** | **$6-14k/mo** | **+$72-168k/yr** |

Combined with welcome flow optimization ($5,875/mo → $7-10k/mo target = +$1.1-1.5k/mo lift), realistic total SMS revenue ceiling within 6 months: **$13-24k/mo** vs current ~$6k/mo baseline.

---

## Open items / decisions needed from Amir

1. **Care guide page** — does shopaydins.com/pages/ring-care exist? If not, do you want me to draft the page content?
2. **Price match guarantee** — real policy or fabrication in current welcome flow?
3. **14k gold catalog** — real product line or overclaim?
4. **`BROWSE15` discount code** — OK to create, or want a different code name?
5. **Cross-sell collection for Flow 2 Msg 5** — do you have a curated "pairs well with" collection, or should we build one?
6. **Recart merge tags** — need to verify exact syntax for `{{order_status_url}}`, `{{tracking_link}}`, `{{product_name}}`, etc. before going live. Easiest: ask Recart support for the variable cheat sheet.
