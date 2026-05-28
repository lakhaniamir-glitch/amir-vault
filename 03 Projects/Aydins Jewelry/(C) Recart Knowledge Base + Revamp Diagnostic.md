# Recart — Knowledge Base + Aydins Revamp Diagnostic

> **Compiled:** 2026-05-13
> **Purpose:** Single source of truth on Recart before we revamp Aydins' SMS marketing
> **Sources:** Recart.com, Recart pricing page, Postscript / Klaviyo benchmarks, TCPA/10DLC compliance docs (2026)

---

## 1. What Recart Is

Recart is a **Shopify-native SMS + list-growth platform** with two distinct product modules that they sell separately or bundled:

1. **OneClick Opt-in (List Growth)** — their "one-tap" popup that captures phone numbers without the buyer typing. Claims **8-12% popup conversion**, **2-5x faster list growth** vs typical popups, and 400% faster popup load.
2. **SMS Marketing** — campaign sends, automation flows, segmentation, A/B testing, analytics.

**Differentiator vs Klaviyo/Postscript/Attentive:**
- **Managed service is included on most plans** — every non-Starter tier comes with a dedicated SMS strategist/CSM who builds your flows, writes copy, and runs split tests *for you*.
- **Flat pricing model** — pay a monthly fee with an included message bucket, instead of pure pay-per-message (Postscript) or subscriber-tier pricing (Klaviyo).
- **Built for non-technical operators** — simpler UI, fewer features than Postscript, less unified than Klaviyo (which has email + SMS in one).

**Where Recart loses:**
- Less deep segmentation than Postscript or Klaviyo
- No native email — you keep your ESP separate
- Smaller automation library than Postscript
- Higher monthly floor than per-message models if you send low volume

---

## 2. Recart Pricing (2026)

### Standalone SMS Plans (12-month commitment)

| Tier | Monthly | SMS Included | SMS Rate | MMS Rate | Strategist? |
|---|---|---|---|---|---|
| Starter | $299 | 23,000 | $0.0100 | $0.0280 | ❌ |
| Pro | $499 | 41,583 | $0.0085 | $0.0265 | ✅ |
| Scale | $999 | 100,000 | $0.0070 | $0.0240 | ✅ |
| Enterprise | Custom | — | from $0.0045 | from $0.0190 | ✅ |

**Base carrier fees included in rates:** $0.003/SMS, $0.006/MMS

### List Growth + SMS Combined Plans

| Tier | Monthly | SMS Rate | MMS Rate | Commit | What's bundled |
|---|---|---|---|---|---|
| Basic | $500 | $0.0085 | $0.0250 | Quarterly | OneClick + email support |
| Standard | $1,000 | $0.0075 | $0.0180 | Quarterly | Custom popups, priority support, toll-free |
| Managed | $2,250 | $0.0055 | $0.0160 | Annual | Dedicated CSM, managed campaigns, A/B testing |
| Premium | $4,250 | $0.0050 | $0.0150 | Annual | Above + shared Slack channel |
| Enterprise | Contact | $0.0045 | $0.0140 | Annual | Custom |

**Short code:** $600/month extra (Scale tier and above).

### Cost math reality check
- Pro plan @ $499/mo + 41,583 SMS included ≈ **$0.012 effective cost per SMS**
- Postscript pay-per-message: typically $0.015-0.02 all-in for similar volume
- Klaviyo SMS: $15-$X based on subscribers, similar effective per-send cost
- **If Aydins sends <23k SMS/mo and doesn't need a strategist, Starter ($299) is the right tier.** If sending 40k+, the Pro tier's strategist pays for itself.

---

## 3. The 5 Recart Flows (where 45%+ of SMS revenue lives)

This is critical: **SMS flows = 7.6% of sends but drive 45.2% of total SMS revenue.** Recart's flow library is the engine. If Aydins doesn't have these dialed in, that's the entire revamp.

### Flow 1 — Welcome Flow
- **Trigger:** New SMS subscriber opt-in
- **Purpose:** Convert the highest-intent subscriber (just gave you their phone)
- **Recart's standard:** 3-5 texts over 24-72 hours
- **Sequence pattern:**
  - Text 1 (immediate): Welcome + discount code + product hero link
  - Text 2 (4-6 hrs): Reminder of offer + social proof (review count)
  - Text 3 (day 2): Best-seller showcase / category sampler
  - Text 4 (day 3): Final urgency push before code expires
- **Benchmark:** Recart shows Her Juice Bar earning **$217,594 from Welcome Series alone**.

### Flow 2 — Abandonment Flow (Browse / Cart / Checkout)
- **Trigger:** Buyer drops off at any of 3 stages
- **Timing:** First text 10-15 minutes after abandonment
- **Sequence pattern:**
  - Text 1: "Hey, your ring is still waiting" + cart/product link
  - Text 2 (4-12 hrs): Reframe ("not sure on size? lifetime sizing has you covered") + soft incentive
  - Text 3 (24-48 hrs): Last-chance + stronger discount if needed
- **Benchmark:** Recart's BulkSupplements case: **$216,641 recovered from cart abandonment flow alone**.

### Flow 3 — Transactional Flow
- **Trigger:** Purchase, then shipment milestones
- **Purpose:** Personalized order updates (receipt → packed → shipped → delivered)
- **Why it matters:** Not directly revenue — but builds trust, reduces "where's my order" tickets, sets up the next flow.

### Flow 4 — Post-Purchase Flow
- **Trigger:** Order completion
- **Purpose:** Increase AOV via cross-sell / up-sell
- **Sequence pattern:**
  - Day 0-2: Thanks + "while you wait, check out [matching product]"
  - Day 5-7 (after delivery): Review request + UGC ask
  - Day 14: Engraving care guide / wearing tips → soft cross-sell

### Flow 5 — Retention Flow (Win-Back / Replenishment)
- **Trigger:** Time-based (90 / 180 / 365 days since last purchase)
- **Purpose:** Re-engage dormant subscribers, reduce churn
- **Sequence pattern:**
  - "Haven't heard from you — here's what's new" + new collection link
  - Personalized "people who bought [SKU] also love [SKU]"
  - Strong incentive for return purchase

---

## 4. SMS Benchmarks (2026) — What Good Looks Like

| Metric | Industry Average | "Good" Target | "Best" Target |
|---|---|---|---|
| Popup opt-in rate | 3-5% | 6-8% | 10-12% (Recart claim) |
| SMS CTR | 21-35% | 30%+ | 40%+ |
| SMS conversion rate (broadcast) | 0.97% | 2%+ | 5%+ |
| SMS conversion rate (flows) | 3.81% | 6%+ | 10%+ |
| SMS revenue ROI | $21:$1 | $36:$1 (Recart claim) | $71:$1 |
| Welcome flow conversion | 8-12% | 15%+ | 20%+ |
| Cart abandonment recovery | 10-15% | 18%+ | 25%+ |

**Jewelry-specific note:** Luxury/jewelry conversions sit at **0.5-1%** baseline (lower than ecom average because of higher consideration + price). That doesn't mean jewelry SMS is weak — it means SMS for jewelry must work harder on **mid-funnel education** (sizing, materials, engraving) and **trust** (warranty, reviews, family business story), not just discount blast.

**Personalization lift:** Recipient-name + recent-activity SMS converts **35% better** than generic sends.

---

## 5. Compliance Landmines (TCPA + 10DLC — 2026)

Skipping these = $500-$1,500 per message in fines. Aydins is US-only so all of this applies.

### Hard Requirements

1. **10DLC registration:** Mandatory for all US business SMS. Carriers block 100% of unregistered A2P traffic as of Feb 2025. Recart handles registration but verify it's done.
2. **Express written consent:** Before any marketing text — must be specific, documented, opt-in language clearly stating:
   - Who is texting (Aydins Jewelry)
   - What type of messages (marketing, order updates, etc.)
   - Frequency disclosure ("up to 6 msgs/mo")
   - "Msg & data rates may apply"
   - How to opt out ("Reply STOP")
3. **One-to-one consent (January 2026 update):** Consent **cannot be shared across brands or sold**. If Aydins ever bought a list — kill those numbers now.
4. **Quiet hours:** No marketing sends before **8 AM** or after **9 PM** local time (per recipient).
5. **Honor STOP / HELP immediately.** Maintain an opt-out log.

### Aydins-specific compliance check (verify before revamp)
- [ ] Recart 10DLC registration status: confirmed active
- [ ] Popup opt-in language audit: covers all 5 disclosure items
- [ ] Welcome flow text 1: includes "Reply STOP to opt out" footer
- [ ] All sends time-windowed to 8 AM - 9 PM recipient local time
- [ ] No purchased lists currently in subscriber base
- [ ] Privacy policy on shopaydins.com references SMS data use

---

## 6. AI / What's New for 2026

Recart's 2026 push is **AI for content generation and send-time optimization**:
- Auto-generated SMS copy variants for A/B testing
- AI send-time picker (sends at each subscriber's most likely engagement window)
- Subject-line / preview-text optimizer
- Predictive segmentation (likelihood-to-convert, likelihood-to-churn)

**Caveat:** This is in line with Klaviyo's AI tools — not Recart-unique. The bigger Recart advantage remains the bundled managed service, not the AI per se.

---

## 7. Aydins SMS Revamp — Diagnostic & Recommendation

### Confirmed state (from 2026-05-13 account screenshots)

| Variable | Status |
|---|---|
| **Plan** | Starter $299/mo (23k SMS included) |
| **Subscribers** | 5,458 total, ~273/mo growth |
| **Active welcome flow** | 1 of 10 (WELCOME FLOW_New 2025) — other 9 are seasonal versions sitting inactive |
| **Klaviyo integration** | ✅ ACTIVE (currently unused for segmentation/suppression) |
| **Compliance status** | ⚠️ UNCONFIRMED — not visible in General Settings; need to check SMS tab + verify 10DLC brand registration directly with Recart support |
| **Registered business address** | 2201 Long Prairie Rd Suite 107-308, Flowermound TX 75022 (⚠️ doesn't match Aydins Policies "Irving, Texas workshop" — reconcile) |
| **Legal docs** | ToS + Privacy via Enzuzo |

### Welcome flow — full message-by-message audit (2026-05-13)

> **Stats note:** Per-node numbers below are **all-time / lifetime** since flow activation (~June 2025, ~11 months running). The dashboard "Last 30 days" view ($7,276 / 193X) is the rolling window. Both are useful — lifetime tells you what each message has produced; 30-day tells you current trend.

**Aggregate (lifetime, ~11 months): ~$64,624 = ~$5,875/mo average.** Last 30 days: $7,276 (+24% vs lifetime average — trending up). Annual run-rate at current pace: ~$87k/yr from welcome flow alone.

Violations to fix don't depend on send window — every future send carries the same risk regardless of whether the lifetime count is 1,496 or 14,960.

#### Hero send (do not touch)

**Msg 2 — Post-opt-in 20% SMS (1hr after opt-in)**
- 2,893 sent / **$53,344 sales** / 11.9% CTR / **608X ROI** / 2.4% opt-out
- Copy: "Aydins Jewelry: It's good to have you on board! Discount code unlocked! Save 20% on your next order with the discount code: SMS20RC. Shop Now: https://shopaydins.recartsms.com/shortlink"
- **Status: protect.** Single highest-revenue SMS in the stack.

#### Critical violations to fix

| Msg | Issue | Action |
|---|---|---|
| **MMS Msg 3 image** | "Family Owned Since 2003" badge | ❌ Factually wrong. Aydins started 2011. Change to "Family Owned Since 2011" or remove the date. |
| **MMS Msg 3 copy** | "For over 20 years, Aydin's Jewelry..." | ❌ Wrong. 15 years (2011→2026). Rewrite as "For over a decade" or "Since 2011." |
| **MMS Msg 3 image** | "Lifetime Warranty" badge | ❌ Forbidden bare claim. Replace with tiered wording or remove the badge entirely. |
| **MMS Msg 3 image** | "Lifetime Sizing" badge | ❌ Same. Replace with "Lifetime Sizing Program" (paid) or remove. |
| **"Has no abandoned cart" SMS** (1,496 sent) | "we include a lifetime warranty with free resizing" | 🚨🚨 **Most exposed message in stack.** Double-forbidden direct claim going to 1,496 people. **Rewrite this week.** |
| **Msgs 3, A, B** | "Aydin's Jewelry" (apostrophe) | ⚠️ Brand consistency — should be "Aydins Jewelry" (no apostrophe). Used 3+ times. |
| **Msgs A, B** | "price match guarantee" | ⚠️ Verify against [[(C) Aydins Policies — Source of Truth]]. Remove if not real. |
| **Path B** | "14k gold custom rings" | ⚠️ Verify Aydins catalog actually carries 14k gold. If not — overclaim, remove. |
| **Msg 3, Path A** | "crafting / craftsmanship / Crafting Memories" | ⚠️ Borderline. Safer to remove — Aydins engraves and ships, not crafts. |

#### Performance snapshot (full flow — lifetime stats, ~11 months)

| Node | Sent (lifetime) | Sales (lifetime) | ROI | Status |
|---|---|---|---|---|
| Compliance message | 2,893 | $0 | — | ✅ Properly formatted |
| **Msg 2 — 20% welcome SMS** | 2,893 | **$53,344** | **608X** | ✅ Hero — protect |
| MMS Msg 3 — Why Choose Aydins | 2,354 | $2,754 | 31X | 🚨 Replace image + copy |
| MMS A — Out of the Ordinary | 1,073 | $3,035 | 75X | ⚠️ Fix apostrophe + verify price-match |
| SMS B — 14k gold custom | 1,045 | $2,731 | 85X | ⚠️ Same + verify 14k claim |
| SMS — abandoned cart | 445 | $956 | 74X | ✅ Clean |
| SMS — no abandoned cart | 1,496 | $1,654 | 35X | 🚨🚨 **Rewrite — most exposed** |
| SMS — last chance 25% | 48 | $150 | 110X | ✅ Clean (deeper discount) |
| Final reminder | 0 | $0 | — | ⚠️ Logic gate too restrictive |

**Read across the flow:** Msg 2 carries 83% of welcome flow lifetime revenue ($53,344 of $64,624). Every other node combined = ~$11k over 11 months. The 20% SMS is the engine; everything after it is a long-tail contributor.

### Compliance audit (Settings → SMS tab, 2026-05-13)

✅ **Toll-free sending number** (+1 833-898-9013) — Active, verified. TFN bypasses 10DLC. Compliance baseline met.
✅ **Quiet hours** — 8 PM – 9 AM subscriber's timezone (TCPA compliant).
✅ **Opt-out AI** — ON. Recart-managed unsubscribe keywords.
✅ **Branded URL** — shopaydins.recartsms.com/shortlink configured.
✅ **Contact card** — Aydins Jewelry, sales@shopaydins.com, shopaydins.com configured.

⚠️ **Smart sending = 0 hours.** **Set to 8 hours.** Prevents same subscriber from receiving multiple promotional SMS back-to-back. Recart's own recommendation. Single biggest opt-out reducer available.

⚠️ **Second TFN (Disconnected)** — Clean up. Remove from account.

### 30-day flow performance (Apr 13 – May 13, 2026)

| Flow | Msgs Sent | Spend | Sales | RPM | ROI | Status |
|---|---|---|---|---|---|---|
| **Welcome** | 1,028 | $38 | **$7,276** | $7.08 | **193X** | ✅ Hero — protect & audit copy |
| **Abandonment** | 170 | $10 | $808 | $4.75 | 82X | ✅ Working — under-volumed |
| **Custom Triggers** | (active) | — | $0 | — | 0X | ❌ Dead — rebuild or kill |
| **Order & Receipt** | (active) | — | $0 | — | 0X | ❌ Dead — copy/CTA missing |
| **Fulfillment Notifications** | (active) | — | $0 | — | 0X | ❌ Dead — copy/CTA missing |
| **Totals** | 1.44K | $55 | $8.08K | — | 146X | 3.2% opt-out |

**Read:** Welcome + Abandonment carry the entire SMS revenue. The other 3 flows are sending but converting nothing — either broken triggers, weak copy, or missing CTA links. That's the fastest-fix gap.

### Popup distribution problem (separate from flow performance)

- **OneClick popup opt-in rate is 4-5x higher** than the regular popup BUT receives **<1% of impressions** (~310 vs 28,165 on mobile).
- The high-converter is starving for traffic. Either trigger logic is wrong, display rules are misconfigured, or it's only firing on a rare segment.
- **Single highest-leverage move on the popup side:** A/B test OneClick as the primary display vs the current regular popup (Recart → Popup A/B Tests).

### Campaign history pattern recognition

- **Best ever broadcast: Black Friday 2023 → $15,649 sales / 147X ROI.**
- Pattern: BFCM is the disproportionate revenue event. Calendar 2026 BFCM campaign now (Nov), don't improvise it in October.

### The revamp plan — locked, 4 phases

**Phase 1 — Popup A/B Test (this week, fastest lift)**
- Set up A/B: OneClick popup vs current regular popup, 50/50 split
- Run 14 days, measure opt-in rate + downstream Welcome-flow revenue per subscriber
- Expected outcome: OneClick wins → make it primary → multiply opt-ins
- **Why first:** This grows the input to the only flow making real money (Welcome at 193X)

**Phase 2 — Resurrect the dead flows (week 2-3)**
- **Custom Triggers, Order & Receipt, Fulfillment** all sending $0
- Audit each: is the trigger firing? Is there a CTA link? Is the copy generic?
- Rewrite using policy-compliant language (no "lifetime warranty," no "handcrafted," Irving TX, tiered warranty/sizing wording)
- Add product-link CTAs to Order & Receipt + Fulfillment (these have captive attention — every "your order shipped" SMS should include a cross-sell or review-ask)
- Goal: each dead flow >$500/mo within 30 days

**Phase 3 — Klaviyo ↔ Recart unlock (week 3-4)**
- **Suppression first** (biggest immediate win): exclude "Klaviyo Email Engaged Last 7 Days" from Recart blast SMS → fewer opt-outs, higher conversion per send
- **Segment-driven sends**: Use Klaviyo's purchase-history + AOV segments as Recart audiences (e.g. "Bought engraved ring 60+ days ago" → Lifetime Sizing reminder)
- **Event-triggered SMS**: Klaviyo events ("viewed product 3+ times," "left review 4+ stars") → Recart trigger
- **Coordinated flows**: Email Day 1 (Klaviyo) → SMS Day 3 (Recart, non-openers only)

**Phase 4 — BFCM 2026 calendar (build in September, execute Nov)**
- Base on 2023 winning pattern (147X ROI, $15,649)
- 5-7 broadcast send schedule: BF teaser → BF early access → BF day → CM teaser → CM day → final reminder → last-chance
- Pre-write all copy in policy-compliant voice
- Pre-segment audiences (VIP buyers get early access, dormant get reactivation offer)

### Compliance — open loop, address before any new sends

- [ ] Check Settings → **SMS tab** (not General) for 10DLC brand registration status
- [ ] If not registered: register immediately or contact Recart support to confirm shared compliance pool coverage
- [ ] Audit current popup opt-in language for all 5 required disclosures (who/what/frequency/rates/STOP)
- [ ] Reconcile registered address (Flowermound TX) vs Aydins Policies (Irving TX) — pick one truth
- [ ] Confirm all sends respect 8 AM – 9 PM recipient local time
- [ ] Pull copy of every active SMS message and find-and-replace forbidden phrasings

### One strong recommendation if I had to pick one move

**Run the OneClick popup A/B test this week.** It feeds the only flow (Welcome at 193X ROI) that's already proven, multiplies subscribers 4-5x at the top of the funnel, and takes <1 hour to set up in Recart. Every other move (dead-flow revamp, Klaviyo unlock, BFCM calendar) depends on a bigger, healthier subscriber list to matter.

---

## 8. Files to read alongside this

- [[(C) Aydins Policies — Source of Truth]] — policy wording for all SMS copy (warranty, returns, sizing must use current tiered language)
- [[(C) Shopify Listing Standard — Brief for Beta-Shop]] — voice/brand rules apply to SMS too
- [[30-Day Plan — Strengthen The Core]] — Week 3 already has a "1 traffic push" slot SMS revamp fits into

---

## Sources

- [Recart homepage](https://recart.com/)
- [Recart flows page](https://recart.com/flows)
- [Recart pricing calculator](https://recart.com/sms-marketing-pricing-ecommerce)
- [Shopify App Store: Recart](https://apps.shopify.com/recart)
- [KeepShoppers Recart 2026 Review](https://keepshoppers.com/reviews/recart-sms-marketing-review-pricing-features-integrations-and-more)
- [Postscript 2026 SMS Benchmarks](https://postscript.io/sms-benchmarks)
- [Klaviyo vs Postscript 2026](https://www.klaviyo.com/compare/klaviyo-vs-postscript)
- [SMS Marketing Benchmarks 2026 — MessageFlow](https://messageflow.com/blog/sms-marketing-benchmarks/)
- [TCPA Text Messages Guide 2026 — ActiveProspect](https://activeprospect.com/blog/tcpa-text-messages/)
- [10DLC + TCPA Compliance — TermsFeed](https://www.termsfeed.com/blog/sms-marketing-privacy-compliant/)
