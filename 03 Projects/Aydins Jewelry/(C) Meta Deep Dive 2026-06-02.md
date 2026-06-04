# (C) Meta Deep Dive — Aydins Jewelry — 2026-06-02

Account: act_23304577 | Attribution: 7-day click / 1-day view | Currency: USD | TZ: America/Los_Angeles
Generated: 2026-06-02 | Status: Account restarted this morning after ~8-day dark period (approx 2026-05-25 to 2026-06-02)

---

## 1. Pixel / CAPI / EMQ Health Check

**The account went dark for ~8 days and just restarted. That gap is a tracking red flag, not just a delivery red flag.**

When Meta delivery stops, the Pixel keeps firing on organic traffic, but there are zero paid event signals feeding the learning system. When you restart, Meta has to re-establish its event signal baseline. If tracking has any pre-existing issues (dedup gaps, EMQ degradation, mismatched event_id), they get amplified on restart because the algorithm is recalibrating from a cold state. This is the moment to fix tracking, not ignore it.

### Checks to run right now, in order

**Step 1: Events Manager > Data Sources > Pixel**
- Open the Diagnostics tab. Look for any warnings on Purchase, AddToCart, InitiateCheckout, ViewContent. A warning here means degraded signal going into the auction.
- Check "Event Match Quality" for Purchase specifically. Target: 8.0+. If it's below 7.0, you have a real problem that's capping delivery quality before you even get to creative.
- What to look for in EMQ detail: are you sending email, phone, first name, last name? All four together push EMQ above 8. Missing phone alone typically costs 0.5-1.0 EMQ points. If Shopify is only passing email by default, you're leaving points on the table.

**Step 2: CAPI deduplication rate**
- Events Manager > Data Sources > select your Pixel > Event Match Quality > scroll to dedup section.
- Target: 90%+ dedup rate on Purchase. Below 70% means Meta is counting some conversions twice, which inflates reported ROAS and causes the algorithm to overspend against phantom signal.
- Dedup works via event_id matching between browser Pixel and CAPI. If your Shopify CAPI integration isn't sending event_id on order confirmation, dedup breaks silently.
- Given you've been dark for 8 days and are restarting, run the dedup check before trusting any of the ROAS numbers you see in the first 48-72 hours post-restart.

**Step 3: Test Events tool**
- Events Manager > Test Events. Put a real order through on a test product ($1 item or use an existing product with a coupon). Verify you see: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase all firing in sequence with correct parameters (value, currency, content_ids).
- If Purchase fires from both browser Pixel and CAPI, confirm both show up in Test Events with matching event_id. If the event_id doesn't match between the two, dedup is broken.

**Step 4: Check the dark period didn't create a signal void warning**
- Meta sometimes flags accounts that have extended periods of zero events from paid traffic as "signal quality reduced." This doesn't show up obviously but affects auction eligibility. Check Account Quality in Business Manager for any flags. Clear these before assuming delivery is normal.

**Step 5: iOS 14.5+ Aggregated Event Measurement**
- Verify your Purchase event is set as the highest-priority event in AEM (Events Manager > Aggregated Event Measurement). For a sales-objective account this should always be Purchase at priority 1. If it somehow got reset (rare but happens after account disruptions), you'll be running blind on iOS traffic.

**The specific numbers to verify:**

| Signal | Target | Warning Zone | Action if Below Target |
|---|---|---|---|
| EMQ (Purchase) | 8.0+ | 6.0-7.9 | Add phone + address to CAPI payload |
| Dedup rate | 90%+ | 70-89% | Fix event_id matching in CAPI integration |
| AEM Priority | Purchase = #1 | Any other event at #1 | Reset AEM priority immediately |
| CAPI active | Yes | N/A | If no CAPI: install Shopify Meta app natively |

**Connection to the Shopify conversion cliff on 06/01:** GA4 traffic held steady but conversions cratered. Meta going dark is the most likely cause (demand source removed, not site problem), but low EMQ or broken CAPI can also cause phantom conversions to disappear from reporting when the algorithm recalibrates. Verify tracking is clean before attributing the cliff purely to spend levels.

---

## 2. Learning Phase Strategy on Restart

**Bottom line: the winner will likely stay in Learning for 7-10 more days post-restart. Do not touch it. The budget is tight but workable.**

### Where the winner stands

The winning ad set (Couples Engraved, All mobile devices) has 4 purchases at the ad-set level in 30 days. Meta needs 50 optimization events per ad set per 7-day window to exit Learning. At 4 purchases per 30 days, this ad set is nowhere near 50/week on Purchase optimization.

This raises a critical question: what is this ad set actually optimizing for? If it's optimizing for Purchase at the campaign level with a Sales objective, the ad set likely has fewer than 50 purchase events and has been in Learning or Learning Limited. The 5.44 ROAS is real, but the ad set may have been running on limited optimization signal the entire time.

### What changes now that Gym Images is paused

Gym Images was eating 67% of $50/day ($33.55/day) while the winner got roughly $16.45/day. With Gym Images paused, the winner now absorbs the full $50/day. This is the right move. But understand what happens mechanically:

1. Meta treats a significant budget increase as a Learning reset trigger if the increase is more than 20% in a short window. Going from effectively $16/day to $50/day is a 3x increase. **Expect a Learning reset on the winning ad set.** This is normal and correct. Do not panic and pause it.
2. The restart from 8 days dark is also a reset signal. So you're stacking two reset triggers: dark period restart plus budget reallocation.
3. Learning phase at $50/day for a Purchase-optimized ad set targeting jewelry: expect 7-14 days before stable delivery. The first 48-72 hours will show volatile CPA. That's expected.

### Should the operator consolidate further?

No. The current structure (one active ad set, one campaign) is already the right consolidation. Adding another ad set right now would split the learning signal and slow down the restart. Hold the single ad set until it shows 3-4 stable days of delivery, then evaluate.

**The budget question:** $50/day is workable but not generous for exiting Learning on Purchase optimization. The threshold Meta needs is roughly 50 purchases in 7 days, which would require a $3-5 CPA, which is obviously impossible for jewelry. This means this account will likely never fully exit Learning in the traditional sense. The practical standard for jewelry at this ticket size: stable delivery with consistent CPA over 7+ days without the Learning Limited flag = good enough. Watch for the Learning Limited flag specifically. If it appears on the winning ad set, that's a problem.

**Do not increase budget to accelerate Learning exit.** The decision to hold at $50/day for 48 hours is correct. Increasing budget while Learning is unstable just burns money faster with no targeting improvement.

---

## 3. Audience Saturation Read

**Couples Engraved winner is healthy. You have runway. Catalog Sales was cooked.**

### Catalog Sales: already past the ceiling

Frequency 9.21 over 30 days for a prospecting/retargeting catalog campaign is severe fatigue. The last 14-day ROAS of 1.16 confirms it. This audience has seen these ads 9+ times on average and stopped converting. At $26.49 CPM (catalog vs $11.94 for Couples Engraved), you were paying premium auction prices for an exhausted audience. Pausing was correct.

### Couples Engraved: where the ceiling is

The winner is at 2.29 frequency over 30 days and 2.79 over 14 days. For a prospecting campaign targeting US, the frequency is rising slightly but not alarming.

The frequency threshold for a cold prospecting campaign on a jewelry product: **3.5 is the warning line, 5.0 is where ROAS typically starts degrading materially.** At 2.29/30 days, you're well inside the window.

**Spend ceiling estimate:** The winner has spent $314.76 with 2.29 frequency. That means approximate reached audience size is around $314.76 / ($11.94 CPM / 1000) / 2.29 = roughly 11,500 unique users reached. 

For couples engraved jewelry in the US, the realistic interest-based audience is likely 500K to 2M+ depending on targeting breadth (couples, gifts, anniversaries, engagements, jewelry buyers). At 11,500 reached out of potentially 500K-2M, you have significant headroom.

**Rough spend ceiling before frequency drag:** If audience is 500K, you have room to 10-15x current unique reach before hitting frequency walls. At $50/day that's 100-150+ more days of room on this audience without frequency becoming the bottleneck. Frequency is not your constraint right now. Creative fatigue and budget are.

**One flag:** If the targeting is narrow (tight interest stack or a small custom audience), those audience size estimates collapse. Verify the ad set's audience size estimate in Ads Manager. If it shows under 200K, start thinking about a broader audience test in the next 30-60 days.

---

## 4. Advantage+ Assessment

**Call: not yet. Run the manual campaign for 30 more days and build a clean creative signal first. Then test ASC.**

### Why not now

Advantage+ Shopping Campaigns (ASC) are a strong move for e-commerce, but they perform best when the algorithm has a clear purchase signal to learn from. This account has:

- 12 purchases in 30 days total across both campaigns (6 from the clean winner)
- Just restarted from 8 days dark
- No creative diversity (effectively 1 active creative after today's pauses)
- Unknown EMQ and CAPI health (not verified yet)

Running ASC on thin purchase signal with one creative and unverified tracking is setting it up to fail. ASC needs breadth to work: multiple creatives, clean signal, and enough volume for its algorithm to find patterns. You don't have that today.

### When to test ASC

After the manual campaign proves out for 30 more days post-restart and the 5 new creatives are live and have 7+ days of signal each. Target entry point: late June / early July. At that point you'll have:
- Clean tracking verified
- 3-5 creatives with real performance data
- A stable cost base to compare against

### How to structure the ASC test when ready

Do not merge the winning manual campaign into ASC. Run them in parallel with an existing customer budget cap set in the ASC settings (typically 10-20% of ASC budget allocated to existing customers, so 80-90% goes to prospecting). This keeps ASC from cannibalizing your retargeting. Budget split for the test: $25/day ASC, keep manual at $50/day. Run for 14-21 days before drawing any conclusions. The metric to watch: ASC CPA vs manual campaign CPA at the same time window. If ASC CPA is within 20% of manual after 21 days, scale ASC. If it's worse, kill it and stay manual.

---

## 5. Creative Pipeline Validation

**The 5 planned angles, ranked by expected value. Cut two.**

Ranking based on: (a) what the winning creative signal tells you, (b) how Meta's Andromeda retrieval system clusters creatives, and (c) what converts in jewelry/gifting categories.

### Keep and prioritize

**1. UGC testimonial (highest priority)**
The winner is a single image with presumably brand-produced creative at 2.45% CTR and 5.44 ROAS. UGC testimonial is a genuinely distinct concept from polished brand imagery. It introduces social proof, a different visual texture, and a different copy register (real person voice vs brand voice). Meta's algorithm treats UGC as high-trust creative, and in jewelry it converts because the purchase decision is emotional and social-proof-driven. This is the one format where a weaker production quality actually helps because it signals authenticity. Shoot this week. Real customer, real ring, real quote. 60 seconds max for video, or a still with overlaid text in the customer's own words.

**2. Before/after engraving reveal (second priority)**
This works for a specific reason: it's a transformation narrative. Customer sees a plain ring, then sees the engraved ring with the message. The emotional payoff is in the reveal. This is fundamentally different from a product close-up because it tells a story in a single frame or short sequence. It also aligns directly with the winner's angle (engraving is the core value prop). Produce this as a 3-5 frame carousel or a 10-15 second video. Do not do a static single image for this one; the "reveal" is the hook and it needs motion or sequence to land.

**3. Story/reveal carousel (third priority, but execute carefully)**
Carousel is mechanically distinct from single image and forces swipes, which is a higher engagement signal. The risk: if each frame is just a product shot with slight variation, Andromeda will cluster it as a single concept and you get no algorithm diversity benefit. Each frame needs to serve a distinct narrative function: frame 1 is the hook (problem/emotion), frames 2-3 are the product story, frame 4 is the proof/CTA. If you execute it as "5 product photos in a row," cut it. If you execute it as a mini story arc, it earns its slot.

### Cut

**Engraving close-up (cut):** This is likely too similar to your existing winner. If the winner is already showing the engraved product, a close-up is a variation, not a distinct concept. Andromeda will cluster it with the winner and you get suppression rather than additive reach. The only reason to keep it is if the winner does NOT show engraving detail, in which case it becomes useful. Check what the winner actually shows before cutting entirely.

**Hand-on-hand (cut):** This is lifestyle/model creative. It's a common format in jewelry and it's not distinct enough from standard jewelry advertising to break through as a new concept. More importantly, your data shows the winner has 2.45% CTR without needing lifestyle imagery. Adding a generic "couple holding hands" shot does not meaningfully change the value proposition the audience is responding to. This slot in your creative roster would be better used for a second UGC or a price/offer-anchored single image (e.g., "Custom engraved for under $X" with urgency framing).

**What's missing from your plan:** You have no direct response hook creative. Every planned angle is brand-forward or story-forward. Add one ad that leads with a specific offer or anchor: "Personalized. Ships in 3 days. Under $150." or whatever the honest version is for Aydins' pricing. Price-anchored DR creative typically has lower CTR but higher purchase intent per click. It filters the audience for you. One DR hook ad rounds out the creative set.

**Final creative lineup to produce:**

| Priority | Format | Concept | Production complexity |
|---|---|---|---|
| 1 | Single image or 15s video | UGC testimonial, real customer | Low |
| 2 | 3-5 frame carousel or 10-15s video | Before/after engraving reveal | Medium |
| 3 | Carousel (story arc) | Emotion hook > product > proof > CTA | Medium |
| 4 | Single image | Price-anchored DR hook | Low |

That is 4 creatives. Ship 4 that are genuinely distinct over 5 that blur together.

---

## 6. Catalog Sales Post-Mortem

**Call: keep it dead for at least 60 days. Do not reset it in its current form. If you revive it, it needs to be rebuilt from scratch as a different campaign, not edited.**

### Why it failed

Frequency 9.21 in 30 days means the audience was extremely small relative to spend. Catalog campaigns typically retarget site visitors or past customers with dynamic product ads. If the audience was just site visitors (a standard DPA retargeting pool), and your site was not getting heavy paid traffic to replenish that pool, the audience size was probably a few thousand users. Showing that small pool your catalog ads 9 times in a month means the audience was exhausted within the first 2 weeks, and the last 2 weeks of spend were waste. The 1.16 ROAS in the final 14 days confirms this.

The underlying structural problem: a catalog retargeting campaign needs a constant flow of fresh visitors (cold traffic) to retarget. If your prospecting (Couples Engraved) is running at $50/day with limited scale, you're not filling the retargeting pool fast enough to sustain a separate catalog campaign. The tail eats itself.

### Reset conditions (if you bring it back)

Do not revive until:
1. Couples Engraved is running stably at $50/day for 30+ days and generating meaningful LPV (Landing Page Views). The current 30-day LPV is 827 for Couples Engraved. That is the pool. 827 people visiting your landing page per month is not enough to sustain a separate retargeting catalog campaign at $25/day without hitting frequency walls.
2. Site traffic is materially higher (either from organic, Etsy, Google, or scaled Meta prospecting). Target: 3,000+ LPV/month from paid before spinning up catalog retargeting again.
3. When you do rebuild it: new campaign, not a restart of the old one. Fresh campaign means fresh audience, fresh learning, no carry-over of the fatigued signal. Target audience: ViewContent in last 30 days OR AddToCart in last 60 days OR InitiateCheckout in last 90 days, EXCLUDING purchasers. Layer exclusion of the Couples Engraved winner's audience by ad set to avoid overlap.

---

## 7. Top 3 Highest-Leverage Moves for the Next 30 Days

**Ranked by impact on revenue. No ties, no hedging.**

### 1. Verify and fix tracking before anything else (do this today)

EMQ, dedup, CAPI health. If your tracking is broken, everything downstream is guesswork. The 8-day dark period is the perfect excuse to audit this now before it silently corrupts the data from the restart. One afternoon in Events Manager. Fix whatever needs fixing. Then you know your numbers are real.

**Why this is #1:** A 1-point EMQ improvement (e.g., 7.0 to 8.0) meaningfully improves your auction eligibility and can reduce CPM by 10-20% by itself. That is a free performance lift with no new spend.

### 2. Let the winner breathe at $50/day for 14 days, then validate creative tests

Do not touch the winning ad set for 14 days. Let it re-establish delivery. The new creatives (produce 4 as recommended above) should be ready in 7-10 days. Hold them until the winner has at least 7 stable days of delivery post-restart before launching the new creative test. When you launch, add each new creative to the existing winning ad set, do not create a new ad set. This keeps learning consolidated and lets Meta's system compare all creatives within the same auction context.

**Why this is #2:** Every day you run without a creative test running alongside the winner is a day you're not building toward the next winner. The gap between "winner found" and "next winner identified" is the growth constraint. Closing that gap is more valuable than any structural change.

### 3. Build the retargeting pool before worrying about retargeting campaigns

The right move for Catalog Sales is not to fix it, it is to build the precondition (site traffic volume) that makes retargeting viable. At 827 LPV/month from Meta prospecting, retargeting is a sideshow. Focus on scaling Couples Engraved toward 2,000-3,000 LPV/month before re-introducing a retargeting layer. That happens by: (a) the winner proving out creative longevity, (b) adding new winning creatives that expand reach without cannibalization, and (c) potentially bumping budget to $75-100/day in 30-45 days if ROAS holds.

**Why this is #3:** Catalog Sales failing was a symptom of an undersized retargeting pool, not a problem with catalog campaigns. Fix the root cause, not the symptom.

---

## Next 7 Days: Action List

Ordered by sequence dependency. Do not skip steps or reorder.

**Day 1 (today, 2026-06-02)**
1. Open Events Manager > Diagnostics. Screenshot any warnings. Fix any flagged events before day ends.
2. Check EMQ score for Purchase. Log the number.
3. Check dedup rate. Log the number. If below 90%, escalate to Shopify CAPI integration fix.
4. Verify AEM has Purchase at priority 1.
5. Check Account Quality in Business Manager for any flags from the dark period.

**Day 2-3 (2026-06-03 to 06-04)**
6. Run a test purchase through Test Events tool. Verify Purchase fires from both Pixel and CAPI with matching event_id.
7. Monitor winning ad set delivery. Expect volatile CPA. Do not touch it. Log spend and purchases each day.
8. Begin shooting UGC testimonial creative. Real customer if possible, or genuine founder-voice testimonial if no customer footage is accessible this week.

**Day 4-5 (2026-06-05 to 06-06)**
9. Shoot/produce before/after engraving reveal. Carousel format preferred.
10. Produce price-anchored DR single image. Write 3 headline variants, pick the most direct one.
11. Monitor winning ad set. If Learning Limited flag appears, report it (do not act unilaterally).

**Day 6-7 (2026-06-07 to 06-08)**
12. If winner has shown 5+ stable delivery days, begin producing story/reveal carousel creative.
13. Finalize all 4 creatives for upload. Do not upload yet if winner is still in unstable delivery.
14. Review frequency on winning ad set at 7-day mark. If it exceeds 3.0, note it but do not pause.
15. Document EMQ, dedup, CPA, ROAS, and frequency numbers for the week-over-week comparison going into week 2.

**Do not do this week:** Increase budget, add new ad sets, revive Catalog Sales, launch ASC test, edit the winning ad or ad set.

---

*File: `(C) Meta Deep Dive 2026-06-02.md` | Account: act_23304577 | Aydins Jewelry*
