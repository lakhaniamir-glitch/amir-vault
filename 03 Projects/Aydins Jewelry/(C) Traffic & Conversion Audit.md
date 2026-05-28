# (C) Traffic & Conversion Audit — Aydins Jewelry

**Created:** 2026-05-08
**Owner:** Amir
**Source brief:** [[00 Notes/(C) Deep Research Brief — Shopify Traffic & Klaviyo Setup]]
**Linked plan:** [[03 Projects/Aydins Jewelry/30-Day Plan — Strengthen The Core]]

---

## Executive Summary

**Your problem isn't traffic. It's conversion.**

You're running ~0.22% conversion rate against a jewelry e-com benchmark of 1.0–1.5%. That's a 5–7× gap. Closing even half of it doubles your revenue without a single new visitor — which is exactly why "Strengthen the Core" is the right 30-day frame.

### Top 5 actions, ranked by impact / effort

| # | Action | Expected lift | Effort | Time to ship |
|---|---|---|---|---|
| 1 | Add a free, friction-free ring sizer to the PDP (digital sizer + free physical sizer offer) | +0.15-0.40% CVR | Medium | 1 day |
| 2 | Replace flat catalog hero photo with a hand/lifestyle shot above the fold | +0.10-0.25% CVR | Low | 2 hrs/listing — pilot 10 |
| 3 | Add trust strip directly below product title (lifetime warranty, free engraving, 30-day returns, 10K+ rings shipped, 4.x rating) | +0.05-0.15% CVR | Low | 30 min theme edit |
| 4 | Pin a sticky "Add to cart" bar on mobile PDP with shipping/engraving promise | +0.08-0.20% CVR | Low | 30 min theme edit |
| 5 | Reduce the "in-cart hesitation" — switch from Recart 20% popup to a tighter exit-intent on cart page | +0.10-0.20% CVR | Low | 1 hr |

If you do all 5, you're modeling 0.22% → ~0.7-1.0% CVR over 30-60 days. That's **3-4× revenue at the same traffic level.**

The Klaviyo flows in [[(C) Klaviyo Email Playbook]] are the second lever — they recover the 70-95% who leave.

---

## Part 1 — 2026 Jewelry E-Com Benchmarks

You can't fix what you don't measure. Use these as your weekly scorecard ceiling.

### Conversion Rate (CVR)

| Tier | Range | Who hits this |
|---|---|---|
| Top decile (jewelry) | 2.5–4.0% | Brands with strong creative, social proof, mature email/SMS, retargeting machine, repeat-buyer base |
| Strong | 1.5–2.5% | Most established jewelry DTC brands |
| **Industry median (jewelry)** | **1.0–1.5%** | Healthy, growing |
| Below median | 0.5–1.0% | Improvement opportunity |
| **Aydins today** | **~0.22%** | 5–7× gap to median |
| Cold-traffic-heavy stores | 0.1–0.4% | Common when traffic is mostly browse-and-leave SEO + Pinterest |

**Critical context:** Jewelry CVR is naturally lower than apparel/cosmetics because of:
- Sizing uncertainty (especially rings)
- High consideration cycle — average buyer touches the page 3–7 times before purchase
- Wedding-band specific: often 2 buyers researching together, multi-week decision

So the 1.0-1.5% target isn't aspirational, it's normal. You're under it because of friction, not because the category is hard.

### Cart Abandonment Rate

- **Industry median (e-com all):** 70-72%
- **Jewelry specifically:** 76-83% (higher because of sizing + price reflection)
- **What's "good":** below 75% means your cart UX is working
- **Aydins today:** can't compute precisely without Shopify Analytics dashboard, but **0 abandoned checkouts on 2,714 sessions on 5/7** strongly suggests bot-inflated session counts

### Average Order Value (AOV)

- **Aydins today:** ~$200 (verified from May orders)
- **Men's tungsten band benchmark:** $150–$250 — you're in range
- **14k gold band benchmark:** $400–$1,200 — likely under-selling here
- **Lever to raise AOV:** see "Cross-sell" in Part 4

### Bounce Rate

- **Healthy PDP:** 35-50%
- **Healthy collection page:** 45-60%
- **Healthy homepage:** 30-45%
- **Above 60% on a PDP** = high friction, slow load, or wrong-intent traffic

### Revenue Per Visitor (RPV)

- **Industry jewelry RPV benchmark:** $1.50–$3.00
- **Aydins today (estimated):** ~$0.40–$0.50 (5 orders × $200 / 2,714 sessions)
- **Aydins target:** $1.50+ within 90 days

### Email-attributed revenue

- **Industry median:** 20-30% of total revenue
- **Top decile (jewelry with mature flows):** 35-45%
- **Aydins today:** unknown — likely <10% based on "underutilized Klaviyo"
- **This is your biggest unrealized lever.** See Klaviyo Playbook.

---

## Part 2 — Why High-Consideration Stores Fail to Convert

Wedding rings live at the extreme end of considered purchase. Here are the diagnosis buckets, ranked by how often they're the actual cause.

### A. Ring sizing friction (the #1 killer)

The shopper doesn't know their size. They don't want to commit until they're sure it'll fit. So they:
1. Tell themselves they'll come back
2. Don't come back
3. Eventually buy from a brand that solved sizing

**Your current state:** ring_size_chart metafield is on every product (we just verified this). Good baseline. But check on storefront whether the size chart is actually:
- Visible on the PDP without clicking out (modal or expandable section, not a separate page)
- Mobile-friendly (most jewelry traffic is mobile)
- Followed by a "Free physical sizer kit shipped same-day" offer (this is the conversion unlock)

**Action:** Walk to your phone, open shopaydins.com, find a tungsten band PDP, and try to figure out your ring size without leaving the page. If you can't, that's a customer you lose every visit.

### B. Trust signal vacuum above the fold

A new-to-you visitor lands on a product page and within 2 seconds is asking:
- "Is this a real business?"
- "Will this ship on time?"
- "What if it doesn't fit?"
- "What if I don't like it?"
- "Why should I buy from THIS store vs the 12 other tungsten ring shops Google showed me?"

If those questions aren't answered above the fold, they leave.

**Standard jewelry trust strip (proven pattern):**
> 🇺🇸 Free US shipping in 1-3 days   |   ✏️ Free inside engraving   |   ↻ Lifetime warranty + sizing   |   ⭐ 4.8 (10,000+ reviews)

Place it directly below the product title, before the price. No scrolling required.

### C. Photography that looks like a catalog instead of a product in use

Buyers of $200 wedding bands need to picture it on a hand. A flat 3/4 product shot tells them what the ring looks like; a hand shot tells them what they'll look like wearing it.

**Audit checklist per PDP:**
- Image 1: Hero studio shot (you probably have this)
- Image 2: **Hand shot** — ring on a real hand at natural angle
- Image 3: Close-up of inlay or detail (the texture, the wood grain, the dinosaur bone)
- Image 4: Side profile (so they can see how thick it sits on the finger)
- Image 5: Alternate width or color combo if applicable
- Image 6: Lifestyle (writing, at desk, holding coffee, on a guitar — show context)

**Reality check on Aydins:** Most listings have 2-4 images and they're catalog-only. Adding hand shots to your top 50 revenue listings is the single highest-leverage photography lift you can do.

### D. Mobile experience friction

70-80% of jewelry traffic is mobile. Common mobile-only conversion killers:
- "Add to cart" button below the fold
- Variant selectors that require multiple taps
- Size dropdown that's hard to thumb through
- Slow image loads (4+ seconds = 50% bounce)
- Theme that re-renders on every interaction
- Sticky elements that cover the CTA

**Action:** Run [PageSpeed Insights](https://pagespeed.web.dev/) against 3 PDPs. Target Lighthouse mobile performance ≥80, LCP ≤2.5s, CLS ≤0.1. If you're under, your theme or images need work.

### E. Cart-to-checkout leak

Industry pattern: 40-60% of "add to cart" events never start checkout. Common causes:
- Surprise costs (shipping, tax) revealed at checkout
- Required account creation
- Shipping options buried
- No "buy now" / Express checkout
- Trust questions resurface (return policy, security badges)

**Aydins likely state:** Your free US shipping is a strength — but is it CALLED OUT in the cart drawer? If the cart drawer just shows the line item and total, you're missing your own advantage.

### F. Wrong-intent traffic

Some traffic just won't convert. Examples:
- Inspiration / Pinterest browsers
- Image search visitors
- Comparison shoppers who haven't decided on material
- Industry researchers / competitors
- Bots

This isn't all bad — comparison shoppers eventually buy from someone, and you want to be in their shortlist. But you should be able to tell what % of your sessions are bottom-of-funnel vs top-of-funnel. See Part 4.

---

## Part 3 — On-Site Conversion Killers Specific to Wedding Bands

### Killers ranked by likelihood-on-Aydins

| # | Killer | How to spot it | Fix |
|---|---|---|---|
| 1 | Size guidance is one click away | Ring size chart link goes to a separate page | Move to inline expandable + offer free physical sizer |
| 2 | First image is a flat catalog shot | All hero shots look like product shots, not lifestyle | Replace top-50 hero with hand/lifestyle |
| 3 | No "X people bought this in the last 24 hours" social proof | No live activity widget | Add Loox/Judge.me activity feed |
| 4 | Reviews not above the fold | Reviews live below product description | Pull rating + count to right under product title |
| 5 | "Free engraving" is buried in description | Buyer learns about it at checkout, too late | Promote to bullet under product title |
| 6 | Ship-by-date isn't dynamic | Static "1-3 day shipping" | "Order in 4h 22m for delivery by Friday May 15" |
| 7 | No "couples / matching set" cross-sell | Single-product PDP | "Pair with her ring →" widget for every men's listing |
| 8 | Cart drawer doesn't reinforce trust | Just line items | Add the trust strip + "Free engraving still available" |
| 9 | Checkout asks for account creation | Required signup | Set to optional / guest-first |
| 10 | No Apple Pay / Shop Pay express | Standard Shopify checkout | Enable in Shopify Payments settings |

### Wedding-band specific buyer psychology

**The man buying for himself:**
- Often last-minute (proposing this weekend, married next month)
- Wants confidence it'll arrive on time
- Wants confidence it'll fit
- Doesn't care about precious metal heritage — he cares about durability + price
- "I work with my hands" is a common driver — solve for: scratch resistance, comfort, removability in emergency

**The woman buying for her partner:**
- Wants to surprise him — wants secrecy + flexibility
- Wants returnability without him knowing she ordered the wrong thing
- Wants help picking — needs guidance content, not just product listings
- Will pay more for the right thing if she's confident it's right

**Both:**
- Need to know the ring CAN be cut off in an emergency (huge concern with tungsten/ceramic)
- Need lifetime warranty messaging — they expect to wear this every day for 50 years
- Are checking your competitors (Manly Bands, Etsy stores, Larson Jewelers)

**Implication:** Your PDP should answer "What if I order the wrong size?" and "What if it needs to come off in an emergency?" without the buyer having to ask. You already have these answers in your FAQ — surface them above the fold, not buried in a Q&A section.

---

## Part 4 — Diagnostic Framework: What to Watch Weekly

Build this dashboard in `04 Reviews/l Weekly Reviews l/` — same structure every week.

### Layer 1: Funnel health (highest level)

| Metric | Source | Target | Red flag |
|---|---|---|---|
| Sessions | Shopify Analytics > Online store | Compare WoW | -20% WoW |
| Sessions by traffic source | Shopify Analytics > By traffic source | Watch share shifts | Direct >50% (often = bots) |
| Conversion rate | Shopify Analytics > Conversion summary | Target 1.0% in 90 days | Weekly drop >0.05% |
| AOV | Shopify Analytics | Target $230 in 90 days | Drop below $180 |
| Revenue | Shopify Home dashboard | $50k/mo target ($1,650/day) | <$700/day for 3+ days |

### Layer 2: Conversion sub-funnels

| Step | Where to find it | Healthy benchmark |
|---|---|---|
| Sessions → Product page views | Shopify Analytics > Sessions over time vs Product views | 60-75% of sessions view a PDP |
| Product views → Add to cart | Shopify Analytics > Conversion summary > Reached cart | 5-10% of PDP views |
| Add to cart → Checkout started | Shopify Analytics | 35-55% of carts |
| Checkout started → Order | Shopify Analytics | 50-70% of checkouts |
| Each step is a leak point. Find the worst one and fix it first. |

### Layer 3: Traffic source quality

For each source (Google organic, Google Shopping, direct, email, social):

| Metric | Healthy | Diagnosis if low |
|---|---|---|
| Pages per session | 2.5+ | Wrong audience or thin landing pages |
| Session duration | 1:30+ | Bouncing on landing page |
| Bounce rate | <55% on PDP | Page mismatch or slow load |
| CVR for that source | within 50% of overall CVR | Wrong intent (if much lower) or qualified buyers (if much higher — invest more) |

**Heuristic:** A traffic source converting at 2× your average is gold — buy more of it. A source converting at 0.3× your average is window-shoppers — stop optimizing for it.

### Layer 4: Email metrics (after Klaviyo flows are live)

| Flow | Target open rate | Target CTR | Target conversion |
|---|---|---|---|
| Welcome series | 40-55% | 3-5% | 4-8% |
| Abandoned checkout | 50-60% | 8-12% | 8-15% |
| Browse abandonment | 30-40% | 2-4% | 1-3% |
| Post-purchase | 50-65% | 5-8% | n/a |
| Win-back | 25-35% | 2-3% | 1-2% |

If you're not hitting these within 30 days of a flow being live, the issue is subject lines (open rate), copy (CTR), or offer (conversion).

### Layer 5: Search Console (weekly, takes 5 minutes)

- Total impressions WoW (want growth, not flat)
- Total clicks WoW
- Average CTR (ideally 2-4% — below means meta titles/descriptions need work)
- Top 10 ranking pages — are they your money pages or your blog?
- Top 10 queries with highest impressions but low CTR — these are titles that need rewriting

---

## Part 5 — Prioritized Action Plan

### Week 1 (this week)

**Goal:** Stop the bleeding on the highest-leverage friction points.

- [ ] **Audit 3 PDPs on mobile** — one tungsten, one carbon fiber/dinosaur bone, one 14k gold. Use the diagnostic checklist in Part 3.A-E. Time: 30 min.
- [ ] **Add trust strip below product title** — "Free US shipping 1-3 days · Free engraving · Lifetime warranty · 4.x rating (X reviews)". Theme edit, applies sitewide. Time: 30 min.
- [ ] **Pin sticky add-to-cart on mobile PDP** — apps like "Sticky Add To Cart Booster" do this in 5 minutes for free, or theme code edit. Time: 30 min.
- [ ] **Move size guide inline** — make it a click-to-expand section ABOVE the variant selector, not a link to a separate page. Time: 1-2 hrs.
- [ ] **Write the 3 highest-impact emails** — abandoned checkout #1, welcome email #1, browse abandonment #1. Use Klaviyo Playbook. Time: 2 hrs.

### Week 2

- [ ] **Photography sprint** — pick top 10 revenue products. Add a hand shot to each (your phone + good lighting works). Replace the hero image. Time: 4 hrs total.
- [ ] **Set up Klaviyo flows** — abandoned checkout (3 emails), welcome series (4 emails), browse abandonment (2 emails), post-purchase (3 emails). Use [[(C) Klaviyo Email Playbook]]. Time: 1 day.
- [ ] **Free physical ring sizer offer** — add a section to PDP and footer: "Not sure of your size? Order a free ring sizer kit, ships free." Backed by a Shopify product (priced $0, only available with the sizer kit). Time: 2 hrs.
- [ ] **Enable Shop Pay + Apple Pay** if not already on. Settings > Payments. Time: 5 min.
- [ ] **Add a couples-set cross-sell widget** — top of cart drawer or PDP. Apps: "Frequently Bought Together" by Code Black Belt, free. Time: 30 min.

### Week 3 (Traffic push prep)

- [ ] **Establish baseline metrics** — write down current 7-day rolling CVR, AOV, revenue, sessions, and email-attributed revenue. This is the "before" snapshot.
- [ ] **Set up GA4 properly** — link to Shopify, ensure Enhanced Ecommerce events are firing (purchase, add_to_cart, view_item, begin_checkout). Time: 1 hr.
- [ ] **Run a cart-recovery audit** — manually go through checkout on 3 PDPs. Note every friction point. Fix the top 3. Time: 2 hrs.
- [ ] **Write the win-back flow** — for the customer list 6+ months stale. Time: 1 hr.

### Week 4 (Traffic push)

- [ ] **Email blast to existing list** — 1-2 emails featuring 3-5 hero products with a tight offer (free engraving + free express shipping for 72 hours, no discount needed if margin is tight).
- [ ] **Push 1 piece of content** — blog post, social post, or PR push. Focus: "How to figure out his ring size without him knowing" — the kind of guide that ranks AND converts.
- [ ] **Post-push review** — measure CVR, email-attributed revenue, AOV against baseline. Document what worked.

### Month 2-3 (compounding)

- [ ] **Continue photography sprint** — extend hand shots to top 50 listings.
- [ ] **A/B test PDP layout** — move reviews above description, test sticky CTA variants, test trust strip placement. Use Shopify's built-in A/B testing or apps like Intelligems.
- [ ] **Build out remaining Klaviyo flows** — VIP segment, replenishment (for the rare buyer who reorders), birthday/anniversary.
- [ ] **Customer photo / UGC program** — every post-purchase email asks for a photo, gallery on PDP becomes a conversion engine.

---

## Part 6 — Things That Are NOT The Right Lever (Right Now)

Don't get pulled into these until the above is done:

- ❌ **Redesigning the homepage** — most traffic lands on PDPs from Google, not on homepage. Polish PDPs first.
- ❌ **New Shopify theme** — current theme is fine. Theme migration is a 2-week distraction with no conversion lift if friction issues aren't fixed first.
- ❌ **Influencer marketing / paid ads** — pouring traffic into a 0.22% CVR funnel burns money. Fix the funnel, then turn on the tap.
- ❌ **TikTok / Instagram strategy** — same logic.
- ❌ **New product launches** — you have 1,191 active products. Adding more dilutes attention.
- ❌ **Loyalty program** — premature without a healthier repeat-purchase pattern. Revisit at month 4-6.
- ❌ **Subscription / replenishment** — wedding bands aren't subscription-friendly. Skip.
- ❌ **Adding more channels (Wayfair, Amazon, etc.)** — fragments brand and operations. Etsy + Shopify is already two channels; that's enough.

---

## Part 7 — How To Spot Bot Traffic (Since 5/7 Looked Suspicious)

The 0 abandoned checkouts on 2,714 sessions on 5/7 is a flag. Here's how to verify:

1. **Shopify Admin > Analytics > Reports > "Sessions by location"** — if you see >5% of sessions from countries that have never bought from you (e.g. Singapore, India, Vietnam, Russia), filter those out for true CVR.
2. **Shopify Admin > Analytics > "Sessions by device"** — bots often show up as "Other" or unusual screen resolutions.
3. **Shopify Admin > Analytics > "Sessions by referrer"** — if "Direct" is >40-50% of sessions, you have a problem (bots usually show as direct).
4. **Cloudflare dashboard (if you use it)** — look at the Bot Score distribution. >40% bot score on a session = likely bot.
5. **Add bot filtering** — if you confirm bot inflation, install Cloudflare's Bot Fight Mode (free tier) or upgrade to Pro for stricter filtering.

**Why this matters:** If 30-50% of your "sessions" are bots, your real CVR is closer to 0.4-0.6% — still below benchmark, but the gap is half what we feared. Fix the funnel and you're closer to median than the raw numbers suggest.

---

## Part 8 — One-Page Cheat Sheet

Print this and pin it above your monitor.

```
AYDINS 30-DAY CONVERSION CHECKLIST

CURRENT      0.22% CVR · $200 AOV · ~5 orders/day · ~$30k/month
TARGET       1.0% CVR · $230 AOV · ~25 orders/day · ~$150k/month (90 days)

WEEKLY CHECK
  □ Sessions WoW (Shopify Analytics)
  □ CVR (Shopify Analytics > Conversion)
  □ AOV (Shopify Analytics)
  □ Email-attributed revenue (Klaviyo > Performance)
  □ GSC impressions + clicks WoW

PDP MUST-HAVE
  □ Trust strip below title
  □ Hand shot as image 1 or 2
  □ Inline ring size guide
  □ Sticky mobile CTA
  □ Reviews visible above fold
  □ Couples cross-sell

CART/CHECKOUT MUST-HAVE
  □ Free shipping reminder in cart
  □ Engraving option in cart
  □ Apple Pay / Shop Pay enabled
  □ Guest checkout enabled
  □ No surprise costs at checkout

EMAIL MUST-HAVE (KLAVIYO)
  □ Abandoned checkout (3 emails)
  □ Welcome series (4 emails)
  □ Browse abandonment (2 emails)
  □ Post-purchase (3 emails)
  □ Win-back (2 emails)

SAY NO TO
  □ Theme redesign
  □ Paid ads (until CVR > 0.7%)
  □ New channels
  □ New product launches
  □ Loyalty program (revisit M4)
```

---

## Companion document

For all email setup specifics, see [[(C) Klaviyo Email Playbook]].
