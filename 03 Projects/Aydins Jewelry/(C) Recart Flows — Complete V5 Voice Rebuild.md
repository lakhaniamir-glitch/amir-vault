# Recart Flows — Complete V5 Voice Rebuild

> **Compiled:** 2026-05-13
> **Supersedes:** [[(C) Recart Dead Flows Revamp Spec — 2026-05-13]] (preliminary draft)
> **Authority:** [[(C) Aydins Policies — Source of Truth]] for all policy claims, [[06 System/v5-theme/(C) aydins-design-consolidated-2026-05-09.css]] for voice/aesthetic anchor
> **Purpose:** Complete SMS flow spec for all 4 Recart flows — Welcome (rewrite), Order & Receipt (new), Fulfillment (new), Custom Triggers (new). Abandonment is left alone (working at 82X ROI).
> **Execution:** Copy-paste into Recart's flow editor. ~2 focused sessions, 90 min each.

---

## ⚠️ Critical operational note — Recart SMS is ONE-WAY

**Customer replies to Recart SMS are NOT received.** Recart sends, but doesn't process inbound responses from customers (except `STOP` / `HELP` which are handled at the carrier level for compliance).

**This means:**
- ❌ NEVER write "Reply to this text," "Reply here," "Reply if anything's off," "Reply YES," etc.
- ❌ NEVER promise a human will respond to an SMS reply — they won't see it.
- ✅ ALL "if you need us" CTAs must route to one of: `sales@shopaydins.com` (email), `1-800-214-7345` (phone), or `aydins.thunderreturns.com` (self-serve portal).
- ✅ "Reply STOP to opt out" / "Reply HELP for help" ARE compliance-required and processed automatically — keep these.

**If Aydins ever moves to a two-way SMS platform (Postscript, Attentive, Klaviyo SMS), revisit this constraint and re-enable reply CTAs where they add value.** Until then, every flow message in this spec routes inbound to email, phone, or portal.

---

## Voice reference (use these as your tuning fork)

The Aydins V5 voice is **editorial, masculine, direct, family-run.** Not corporate. Not desperate. Not playful. Confidence without ego. Honesty as a competitive advantage.

**Sound like this** (from the V5 lifetime-sizing page):
> "The same family that engraved and shipped your band is here when your finger changes size, when life knocks the ring against a steel beam, or when a manufacturing defect shows itself two years in."

> "Engraving and shipping rings from our shop in Irving, Texas since 2011."

> "Tungsten is hard but not invincible. If it cracks or shatters, we cover it for life — free first 6 months, low flat fees after."

**Anchors that always work:**
- "Irving, Texas since 2011" — instant trust, family-business signal
- "A real person reads every message" — high-conversion, costs nothing
- Em-dashes (—) not hyphens, used for editorial pacing
- Concrete numbers, never vague claims ("$34.50" not "a small fee")
- Direct contrast framing ("Most brands won't. We will.")

**Banned in all SMS** (per policy):
- "handcrafted / hand-finished / made by hand / forged / built / crafted"
- "free lifetime resizing / lifetime fit guarantee"
- "lifetime warranty" as a bare claim (must be qualified with tiers)
- "free returns / hassle-free / no-questions-asked"
- "lowest price guaranteed / we'll beat any price"
- "2-day shipping" (until carrier service is verified)
- "Aydin's" with apostrophe (it's "Aydins")
- "Since 2003" or "for over 20 years" (it's 2011 / 15 years)
- Emojis (use 0 by default; max 1 per message only if it materially helps comprehension)

**Approved trust pillars** (the 11 verified):
1. Free engraving on every order
2. Free U.S. shipping
3. Dallas–Fort Worth workshop (Irving, TX is the verified workshop city)
4. 30-day returns ($25 restocking, customer pays return shipping, engraved excluded)
5. Free 30-day exchanges on unengraved rings ($34.50 surcharge on engraved)
6. Lifetime Sizing — $34.50 year 1, $54.50 each year after, original purchaser only
7. Aydins Lifetime Warranty — free first 6 months, $34.50 (6-12mo), $54.50 (12+mo)
8. 3-5 business day processing once ring arrives at workshop
9. Operating since 2011
10. Engraved exchanges accepted ($34.50) — most brands won't
11. Aydins Protection Plan — paid add-on at checkout, covers shipping loss/damage/theft

---

## Find-and-replace cheat sheet (apply to ALL existing flows)

| If you see this | Replace with this |
|---|---|
| "lifetime warranty" (bare) | "Aydins Lifetime Warranty — free first 6 months, $34.50 after" |
| "free lifetime resizing" | "Lifetime Sizing — $34.50 in year 1, $54.50 after, for the original purchaser" |
| "30-day free returns and exchanges" | "30-day returns ($25 restocking). Free exchanges on unengraved." |
| "handcrafted / forged / made by hand" | DELETE — substitute with "engraved" or "shipped" |
| "Family Owned Since 2003" | "Family Owned Since 2011" |
| "For over 20 years" | "Since 2011" |
| "Aydin's Jewelry" | "Aydins Jewelry" |
| "price match guarantee" (in marketing) | DELETE entirely — soft/quiet, page-only |
| "14k gold custom rings" (if not verified) | "engraved tungsten, ceramic, and inlay rings" |
| "we make every ring / hand-finished" | "engraved and shipped from our Irving workshop" |
| "Crafting Memories" | DELETE — banned phrase territory |

---

# FLOW 1 — Welcome Flow (rewrite the violations)

**Status:** Working hero, do not rebuild. Fix the 5-7 specific violations.

**Total lifetime revenue:** ~$64,624 over 11 months = ~$5,875/mo. Last 30 days trending +24% ($7,276).

## Msg 1 — Compliance message (KEEP AS IS)

Current copy is properly formatted. No changes.

## Msg 2 — Post-opt-in 20% SMS (KEEP AS IS — HERO)

- 2,893 sent / **$53,344 / 608X ROI**. This message is 83% of welcome flow lifetime revenue.
- **DO NOT TOUCH THE COPY.**

## Msg 3 — "Why Choose Aydins" MMS (REPLACE IMAGE + REWRITE COPY)

**Old image (BANNED):** "Why Choose AYDINS JEWELRY" with badges showing "Lifetime Warranty," "Lifetime Sizing," "Family Owned Since 2003" — 3 critical violations.

**New image spec:**
- Title: "Why Choose Aydins"
- Badges (use exact wording):
  - "Free Laser Engraving"
  - "Free U.S. Shipping"
  - "Aydins Lifetime Warranty *(free first 6 months)*"
  - "Lifetime Sizing Program"
  - "Engraved Exchanges Accepted"
  - "Since 2011"
- Footer line: "Engraved and shipped from Irving, Texas"
- Style: match V5 brass/bone/cream palette — see [[06 System/v5-theme/(C) aydins-design-consolidated-2026-05-09.css]] for color values (`--brass: #B08D57; --cream: #F2EBDC; --bone: #FAF8F4; --ink: #1A1A1A`)

**New copy:**

> Aydins Jewelry: One ring, one family, one workshop in Irving, Texas — since 2011.
>
> What you get with every order:
> — Free laser engraving
> — Free U.S. shipping
> — Aydins Lifetime Warranty (free first 6 months)
> — Lifetime Sizing for the original purchaser
> — Engraved exchanges accepted (most brands won't)
>
> Still have 20% off waiting. Code: SMS20RC
> https://shopaydins.recartsms.com/shortlink

**Notes:**
- Replaces "Crafting Memories... over 20 years... storytellers..." opener (all banned/false)
- Family-business anchor + city + year = instant trust in 12 words
- Concrete trust pillars, not vague claims
- Keeps the 20% recall (most people don't redeem on Msg 2)

## Msg 4 — MMS Path A (REWRITE)

**Old copy violation:** "Aydin's Jewelry," "crafting personalized and custom rings," "price match guarantee" (verify), "Let us help you create something unforgettable" (overclaim).

**New copy:**

> Aydins Jewelry: A few things worth knowing —
>
> Tungsten, ceramic, and inlay rings are nearly indestructible. If yours ever cracks or shatters, the Aydins Lifetime Warranty covers it. Free first 6 months.
>
> Finger size changes? Lifetime Sizing has you covered. $34.50 in year 1.
>
> 20% off still active: SMS20RC
> https://shopaydins.recartsms.com/shortlink

**Notes:**
- Replaces vague "reliability... unique as your story" with concrete pillars
- Drops "price match guarantee" (soft/quiet per policy — never in marketing)
- Keeps the conversion path

## Msg 5 — SMS Path B (REWRITE)

**Old copy violation:** "Aydin's Jewelry," "14k gold custom rings" (unverified), "exceptional jewelry... ultimate destination" (overclaim language).

**New copy:**

> Aydins Jewelry: Engraved tungsten, ceramic, and inlay rings — engraving included on every order, shipped free from our Irving workshop.
>
> Still have 20% off: SMS20RC
> https://shopaydins.recartsms.com/shortlink
>
> Reply STOP to opt out.

**Notes:**
- Concrete materials only (no 14k gold claim until verified)
- Free engraving + free shipping are verified pillars
- Tightened from ~320 chars to ~220 chars

## Msg 6 — Abandoned cart SMS (LIGHT EDIT)

**Current:** Working at 74X ROI. Copy is mostly clean.

**Tweak only:**

> Aydins Jewelry: Your favorites are still in your cart.
>
> 20% off is still active to bring them home — code: SMS20RC. Engraving is free on every order.
>
> https://shopaydins.recartsms.com/shortlink

**Notes:**
- "Engraving is free on every order" is a high-value trust signal that costs zero characters of risk
- Tightened cleaner

## Msg 7 — "Has no abandoned cart" SMS (REWRITE — HIGHEST PRIORITY)

**Old copy (BANNED, sending to ~1,500 people):** "we include a lifetime warranty with free resizing" — DOUBLE forbidden claim.

**New copy:**

> Aydins Jewelry: Sizing can change. We built for it.
>
> Lifetime Sizing — $34.50 in year 1, $54.50 every year after, for the original purchaser. We send a new ring in your new size, same engraving carried over free.
>
> See the details: https://shopaydins.com/pages/lifetime-sizing-lifetime-warranty

**Notes:**
- Replaces banned claim with the actual, more impressive program
- Adds the "same engraving carried over free" hook (most brands won't do this at all)
- Links to the live V5 lifetime-sizing page

## Msg 8 — Last chance 25% (LIGHT EDIT)

**Current:** 110X ROI on 48 sends. Copy is mostly clean.

**Tweak only:**

> Aydins Jewelry: Last chance — your cart's still waiting and the 25% off code expires tonight.
>
> Code: LASTCHANCE25
> https://shopaydins.recartsms.com/shortlink
>
> Reply STOP to opt out.

## Msg 9 — Final reminder (KEEP AS IS, fix logic)

**Current:** 0 sent — flow gate is too restrictive. Verify the conditional split logic so this message can actually fire.

---

# FLOW 2 — Order & Receipt (NEW BUILD)

**Trigger:** `Order placed` (any order, any product)

**Why it matters:** Customer just bought. Highest trust + highest anxiety window of the entire journey. Confirmation + reassurance + setup for the next purchase.

**Target:** $2-5k/mo new revenue.

## Msg 1 — Order confirmation (SMS, immediate)

**Send:** 0 minutes after order placed

> Aydins Jewelry: Order confirmed. We've got your ring and we'll send tracking the moment it ships.
>
> Need to change anything? Email sales@shopaydins.com or call 1-800-214-7345 — a real person reads every message.
>
> Order: {{order_status_url}}

**Char count:** ~210 (1.3 segments)

## Msg 2 — Engraving confirmation (CONDITIONAL — only if engraving present)

**Send:** 30 minutes after order placed
**Condition:** Order line-item property "engraving" exists

> Aydins Jewelry: Quick check on your engraving — "{{engraving_text}}" in {{engraving_font}}.
>
> If anything's off, email sales@shopaydins.com or call 1-800-214-7345 within 24 hours. After that, engraving is locked and the ring goes into production.

**Notes:**
- This single SMS reduces engraving-related returns dramatically (engraved rings are non-returnable per policy)
- Variable syntax: verify in Recart docs. If can't pull engraving text dynamically, fall back to: "Quick check on the engraving you ordered — if anything's off, email sales@shopaydins.com or call 1-800-214-7345 within 24 hours."
- **Phone is included because of the 24-hour urgency window** — email may delay confirmation past production lock, phone gives an immediate path.

## Msg 3 — What happens next (SMS, 2 hours)

**Send:** 2 hours after order

> Aydins Jewelry: Here's the timeline — your ring is being prepped at our Irving workshop (1-3 business days), then ships free.
>
> Most orders arrive within a week of ordering. We'll text you tracking the moment it leaves.

**Char count:** ~225 (2 segments)

**Notes:**
- Sets expectations precisely. Cuts "where's my order" tickets.
- "Irving workshop" reinforces the family-business anchor.
- "Free shipping" is a verified pillar.
- "Within a week" is honest (1-3 days processing + standard ground shipping from DFW = ~5-7 days total) without committing to "2-day" until carrier service is verified.

## Msg 4 — Care guide setup (MMS, 24 hours)

**Send:** 24 hours after order
**Image:** Single ring on textured surface (linen, wood, stone) — lifestyle, not infographic. NO badges.

> Aydins Jewelry: While you wait — one thing worth knowing.
>
> Tungsten, ceramic, and titanium rings are built for daily life. Showers, sleep, dishes, the gym — all fine. The 30-second weekly clean keeps them sharp for years.
>
> Full care guide: https://shopaydins.com/pages/ring-care

**Notes:**
- This is where the new Ring Care Guide page earns its keep
- "Built for daily life" matches the V5 page hero exactly — consistent voice
- Provides value, no upsell

---

# FLOW 3 — Fulfillment Notifications (NEW BUILD)

**Trigger:** `Order fulfilled` (Shopify marks order shipped)

**Why it matters:** Ring is in transit. Customer is checking their phone. Captive attention.

**Target:** $3-6k/mo new revenue.

## Msg 1 — Shipped (SMS, immediate on fulfillment)

> Aydins Jewelry: Your ring is on its way.
>
> Track: {{tracking_link}}
>
> Estimated delivery: {{estimated_delivery_date}}. Questions? Email sales@shopaydins.com.

**Char count:** ~180

## Msg 2 — Out for delivery (SMS, triggered on tracking status)

**Condition:** Tracking status = "Out for delivery"

> Aydins Jewelry: Your ring is out for delivery today. Make sure someone's around to grab it.
>
> Track: {{tracking_link}}

**Notes:**
- High open-rate window. If Recart can't listen to carrier webhooks, skip this message.

## Msg 3 — Delivered + portal handoff (SMS, immediate on delivery)

**Condition:** Tracking status = "Delivered"

> Aydins Jewelry: Delivered. Hope it fits right.
>
> If the size isn't perfect, no stress — start an exchange or sizing claim here: https://aydins.thunderreturns.com
>
> Questions? Email sales@shopaydins.com.

**Char count:** ~215

**Notes:**
- **Why no price reveal at delivery:** Quoting $34.50 at the moment the box arrives primes customers for problems before they've even tried the ring on. Feels transactional ("if you screwed up, this is what it costs") instead of supportive.
- **Why portal-first:** `aydins.thunderreturns.com` handles returns, exchanges, AND sizing claims in one place — a single link routes any post-delivery friction. Cleaner UX than "reply to text + manual triage."
- **Self-serve = lower CX load:** Portal classifies the issue type before it hits the inbox. Sizing claims auto-route, exchanges generate labels, returns get tagged. Saves real CX hours over a year.
- **Brand differentiator:** Most jewelry brands force email-and-wait. Aydins has a self-serve portal — this is the moment to expose it as part of the brand experience, not bury it behind a reply.
- **Pricing is communicated where it belongs:** inside the portal flow and on the live `/pages/lifetime-sizing-lifetime-warranty` page. By the time the customer sees the price, they're already inside an action funnel — context cushions the number.
- **"No stress" framing** turns the worst-case (size is wrong) into a soft handoff, not a transaction.

## Msg 4 — Wear-it-in check (SMS, 3 days after delivery)

> Aydins Jewelry: How's the ring fitting after a few days?
>
> Two things worth knowing:
> 1. Fit not right? Start a claim here: https://aydins.thunderreturns.com
> 2. Loving it? A quick review helps other guys find us: {{review_link}}
>
> Either way — thanks for trusting us.

**Char count:** ~265 (2 segments)

**Notes:**
- **Splits intent cleanly:** dissatisfied → portal; happy → review. Each customer self-routes to the path that matters to them.
- **Mirrors Msg 3 portal-first treatment.** Consistent voice across the post-delivery touchpoints — `aydins.thunderreturns.com` is the universal "if something's off" anchor.
- **No price quoted.** Same logic as Msg 3 — price reveal lives inside the portal flow and on the live `/pages/lifetime-sizing-lifetime-warranty` page, where context cushions the number.
- **3-day timing is intentional.** Long enough for the customer to have actually worn the ring and tested fit; short enough that sizing issues haven't compounded into resentment. Also catches the post-honeymoon window for review intent.
- **"Trusting us" close** keeps the family-business warmth without veering into corporate fluff.

## Msg 5 — Soft cross-sell (MMS, 14 days after delivery)

**Image:** 2-3 complementary rings (couples set, matching family band, stack-mate). Lifestyle composition.

> Aydins Jewelry: Most of our customers come back within 6 months — anniversary band, gift for a brother, matching set for a partner.
>
> If that's on your radar, three that pair with what you have: {{recommended_products_link}}
>
> Engraving is free on every order.

**Notes:**
- "Most of our customers come back" — only use if true. Verify against Shopify repeat-purchase data before sending.
- "Engraving is free on every order" closes with a verified trust pillar
- No discount needed — value-driven, not desperation-driven

---

# FLOW 4 — Custom Triggers / High-Intent Browse (DEFERRED → MIGRATE TO KLAVIYO)

> ⚠️ **Plan-gated in Recart.** Recart Starter ($299/mo) does NOT support custom triggers or browse abandonment. Upgrade to Recart Pro (~$499-799/mo + SMS costs) would unlock this. **DO NOT UPGRADE.**
>
> **Recommended path: build this flow in Klaviyo instead.**
>
> - ✅ Klaviyo is already connected (per the diagnostic)
> - ✅ Browse Abandonment is a **native, free** flow in your existing plan
> - ✅ Email is the better channel for browse-stage research intent (SMS interrupts; email respects the research mode)
> - ✅ Near-zero per-send cost vs. $0.0075-0.015/SMS in Recart
> - ✅ Saves $200-500/mo in subscription, captures same $1-3k/mo revenue → **2x net margin vs. the Recart Pro upgrade path**
>
> **Action:** When ready, port the copy below into Klaviyo as a Browse Abandonment email flow (rewrite from SMS-short to email-long format). Add to the Klaviyo Abandoned Cart rewrite session — same context, same voice anchors. See [[(C) Klaviyo Abandoned Cart Email Rewrites — V5 Voice]] for the V5 email voice template.

**Trigger:** Viewed same product 3+ times in 7 days (start with this; can add cart-add trigger later)

**Why it matters:** Strong intent signal, currently unmonetized.

**Target:** $1-3k/mo new revenue (when built in Klaviyo).

**Status:** SMS copy below is preserved as the conceptual draft. Treat as voice/messaging reference when porting to Klaviyo email. The SMS-tight copy will need to be expanded into proper editorial email format (subject, preview text, body, CTAs, signature).

## Msg 1 — Soft nudge (SMS, 1 hour after 3rd view)

> Aydins Jewelry: Caught you looking at {{product_name}} more than once.
>
> No pressure — just so you have it:
> — Free laser engraving included
> — Free U.S. shipping
> — Lifetime Sizing for the original purchaser
> — Engraved exchanges accepted within 30 days
>
> Take another look: {{product_url}}

**Char count:** ~290 (2 segments)

**Notes:**
- "Caught you looking" — direct, human, not creepy
- No discount in Msg 1 — preserves margin and makes the eventual discount feel earned
- Loads 4 verified trust pillars without overpromising

## Msg 2 — Conditional 15% (SMS, 48 hours later, no purchase)

**Condition:** Has not purchased

> Aydins Jewelry: Still thinking about {{product_name}}? 15% off to help you decide — code: BROWSE15.
>
> Expires in 48 hours. After that, we won't keep bugging you.
>
> {{product_url}}
>
> Reply STOP to opt out.

**Char count:** ~250

**Notes:**
- 15% is lighter than the 20% welcome discount — protects the welcome offer's perceived value
- "We won't keep bugging you" is the V5 voice — respectful, confident, family-business

## Msg 3 — Last touch (SMS, 48 hours after Msg 2, no purchase)

**Condition:** Has not purchased

> Aydins Jewelry: BROWSE15 expires tonight.
>
> If now's not the right time, totally fine. We'll be here when it is — engraving and shipping rings from our Irving workshop since 2011.
>
> {{product_url}}

**Char count:** ~230

**Notes:**
- Honest framing builds long-term trust even when they don't buy
- "Since 2011" closer ties the moment to the brand's longevity

## Exit conditions

- Customer purchases → exit immediately
- Customer opts out → exit
- Flow completes (Msg 3 sent) → exit, don't re-enter for 30 days

---

# FLOW 5 — Abandonment (AUDIT ONLY, working at 82X ROI)

The abandonment flow is currently performing. Don't rebuild. Apply only:

1. **Find-replace any banned phrasings** (especially "lifetime warranty" bare, "Aydin's" apostrophe)
2. **Verify the cart-recovery SMS doesn't reference "price match" or "14k gold"** (per policy violations)
3. **If you can ID the exact messages, paste them into a verification doc** — I'll audit copy-by-copy

---

## Execution checklist

### Settings fixes (5 min, do first)

- [ ] Settings → SMS → Smart sending: 0 → **8 hours**
- [ ] Settings → SMS → Archive disconnected second TFN
- [ ] Settings → SMS → Confirm Branded URL is `shopaydins.recartsms.com/shortlink`
- [ ] Settings → SMS → Verify Quiet hours: 8 PM – 9 AM (already compliant)

### Session 1 — Welcome Flow rewrite (60 min)

- [ ] Replace MMS Msg 3 image (commission new V5-styled badge image)
- [ ] Paste Msg 3 new copy
- [ ] Paste Msg 4 (Path A) new copy
- [ ] Paste Msg 5 (Path B) new copy
- [ ] Paste Msg 6 (abandoned cart) tweaked copy
- [ ] Paste Msg 7 (no abandoned cart) — **CRITICAL, rewrite first**
- [ ] Paste Msg 8 (last chance) tweaked copy
- [ ] Fix Msg 9 conditional split logic so it can fire
- [ ] Test send each message to your own phone before activating

### Session 2 — New flows (90 min)

- [ ] Create discount code BROWSE15 in Shopify
- [ ] Build FLOW 2 — Order & Receipt (4 messages, 1 conditional)
- [ ] Build FLOW 3 — Fulfillment Notifications (5 messages, 2 conditional)
- [ ] ~~Build FLOW 4 — Custom Triggers / Browse~~ **DEFERRED — plan-gated in Recart Starter. Migrate to Klaviyo Browse Abandonment email flow instead (see Session 4).**
- [ ] Verify Recart merge tag syntax for each variable (`{{order_status_url}}`, `{{tracking_link}}`, etc.)
- [ ] Activate flows one at a time, 24-hour observation before activating the next

### Session 3 — Klaviyo abandoned cart fix (HIGHER PRIORITY THAN PARTS OF THIS)

> **Bundled with Session 4 (Klaviyo Browse Abandonment) if doing both in one sitting.**


Per [[(C) Aydins Policies — Source of Truth]], the live Klaviyo Abandoned Cart 1/2/3 emails contain banned claims sending to real customers right now:

| Email | Message ID | Problem |
|---|---|---|
| Abandoned Cart 1 | `SQdgLg` | "30-day free returns & exchanges" — false |
| Abandoned Cart 2 | `UCDagK` | "Lifetime fit guarantee & warranty" — false framing |
| Abandoned Cart 3 | `UJLFPZ` | "Lifetime Warranty & Fit" — same |

**This is higher priority than parts of this Recart spec because it's actively misleading customers in email.** Plan to address in parallel — Klaviyo MCP is available in this session and I can draft those rewrites separately.

### Session 4 — Klaviyo Browse Abandonment build (replaces Recart FLOW 4)

- [ ] Port the Msg 1 / Msg 2 / Msg 3 voice from FLOW 4 above into Klaviyo email format
- [ ] Build Browse Abandonment flow in Klaviyo: trigger on "Viewed Product" event, 3+ occurrences in 7 days
- [ ] Email 1: soft nudge (1 hour after threshold) — no discount
- [ ] Email 2: 15% off BROWSE15 (48 hours later, no purchase)
- [ ] Email 3: last touch (48 hours after Email 2, no purchase) — code expiring
- [ ] Send preview to yourself, verify product variable populates correctly
- [ ] Activate

---

## Total expected impact (revised, realistic)

| Flow | Channel | Current | Target (6mo) | Lift |
|---|---|---|---|---|
| Welcome | Recart SMS | $5,875/mo lifetime avg | $7-10k/mo | +$1-4k/mo |
| Abandonment | Recart SMS | $808 in last 30 days (~$2k/mo steady) | Maintain, audit only | — |
| Order & Receipt | Recart SMS | $0 | $2-5k/mo | +$2-5k/mo |
| Fulfillment | Recart SMS | $0 | $3-6k/mo | +$3-6k/mo |
| Browse Abandonment | **Klaviyo email** (moved off Recart) | $0 | $1-3k/mo | +$1-3k/mo |
| Klaviyo Abandoned Cart fix | Klaviyo email | Already running, lift only from voice rewrite | +5-15% RPR | +$0.5-2k/mo |
| **Total** | | **~$8k/mo** | **~$15.5-28k/mo** | **+$7.5-20k/mo** |

Annualized: **+$90-240k/yr in incremental revenue across SMS + email.**

**Subscription cost change:** $0 (no Recart upgrade — saves $200-500/mo vs. the Pro tier path).

---

## Open items / decisions

1. **Image asset for new Welcome MMS Msg 3:** Need to commission. V5-styled badge image (brass/cream palette). Can draft a Figma spec or written brief if useful.
2. **Care guide page must be live before launching Order & Receipt Flow Msg 4** (which links to it). See [[(C) Ring Care Guide — Shopify Page Content]].
3. **Recart merge tag syntax verification:** Pull the variable cheat sheet from Recart support before going live.
4. **"Most of our customers come back within 6 months" claim** in Fulfillment Msg 5: verify against Shopify repeat-purchase data. If not true, soften to "Some of our customers come back" or delete that opener.
5. **Carrier service / "ships free" wording:** Confirmed verified pillar. "Within a week" is the safe delivery timeframe until carrier service-level is documented.
6. **Klaviyo Abandoned Cart fix:** want me to draft those email rewrites next? It's the highest-exposure copy work on the table.
