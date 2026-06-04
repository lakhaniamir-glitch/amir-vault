# Beta Meta Strategist Framework and Prioritized Recommendations

Date: 2026-06-03
Purpose: make Beta operate like a Meta strategist, not just an executor.

## 1. Audience strategy framework

### Tier structure

- Cold prospecting: broad US mobile-first, purchase optimized, excluding recent purchasers and hot/warm users when audiences exist.
- Warm engagers: page and profile engagers, video viewers, site visitors, product viewers.
- Hot retargeting: ATC 30d, IC 30d, payment info 30d, high-intent product viewers.
- Suppression: purchasers 60d for prospecting, purchasers 365d for retargeting except upsell or anniversary flows.

### Custom audiences to build

- Website visitors 30d
- ViewContent 30d
- AddToCart 30d
- InitiateCheckout 30d
- AddPaymentInfo 30d
- Purchasers 365d
- Purchasers 60d exclusion
- Video viewers 75%+ 30d
- Page engagers 30d
- IG engagers 30d

### Lookalike strategy

- Primary seed: purchasers 365d once the count is large enough. Start 1%, then test 2% to 5%.
- Secondary seed: ATC 180d or IC 180d if purchaser seed is too small.
- Do not launch multiple lookalikes until exclusions are clean and budget can support learning.

## 2. Campaign structure framework

- Current scale recommendation: 1 prospecting sales campaign plus 1 retargeting sales campaign.
- Prospecting: 70% to 80% of budget. Broad US mobile-first, purchase optimized, 3 to 5 creatives.
- Retargeting: 20% to 30% of budget once audiences exist. ATC, IC, visitors, engagers. Exclude purchasers.
- Keep campaign daily budget at $50 until post-blackout delivery stabilizes.
- Launch automated shopping campaign only after catalog health, exclusions, and current winner stability are clean.

## 3. Creative testing and refresh framework

- Concurrent creative slots per ad set: 3 to 5.
- Minimum test: 1 new creative per active ad set per week.
- Declare winner only after 50 purchases per variant or confidence interval is clearly superior. At Aydins current volume, use directional guardrails first.
- Refresh trigger: frequency above 3.5 or CTR drops 30%+ over rolling 7 days.
- Creative taxonomy: couples engraving, material macro, daily wear, gift emotion, contrast with basic bands, review proof.

## 4. Bid and placement framework

- Lowest cost: default at current $50/day scale. Use while signal is limited.
- Cost cap: only after 14 stable days and at least 30 purchases in a campaign. Cap near target CPA, not below it.
- Bid cap: avoid for now. It can throttle learning.
- ROAS goal: only when purchase volume is stable and catalog/product feed quality is clean.
- Placements: mobile-first is justified for men 25 to 45 wedding band buyers, but monitor network inventory because high CTR without purchases can pollute signal.

## 5. Scale and kill rules

- Auto-scale trigger: 7-day ROAS above 3.0, CPA under target, frequency under 3.0, and at least 14 days after restart.
- Auto-kill trigger: 3-day ROAS under 1.5, or $30 spend with 0 purchases, or CTR under 1% for 48 hours.
- Max daily budget change: plus or minus 20%.
- Hard cap: $200/day Meta until proven scaling above 5.0 ROAS.
- Hard floor: $30/day to maintain learning.

## 6. Operating cadence

- Daily 7am Telegram: delivery, spend, ROAS, CPA, CTR, frequency by active ad set, kill candidates, scale eligibility.
- Weekly Monday brief: full performance, creative winners/losers, top 3 changes, decisions needed.
- Pre-action checklist before any spend change: tracking healthy, budget within limits, audience size sufficient, no policy flags, frequency within range, no billing issue.

## 7. Pro-level decision framework

Every Beta recommendation must include:

- Current state
- Target state
- Expected impact in dollar terms
- Risk if approved
- Risk if rejected
- Monitoring plan
- Rollback plan

Telegram format:

STRATEGIC DECISION
What:
Why:
Risk if approved:
Risk if rejected:
Beta recommendation:
Reply: approve / reject / hold

## 8. Prioritized recommendations for this month

| Rank | Action | Current state | Proposed change | Expected impact | Risk | Dependency | Time | Rec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Build purchaser and funnel exclusions | API returned 0 custom audiences | Create purchaser 60d/365d, visitors 30d, ATC 30d, IC 30d, engagers 30d | 10%+ waste reduction potential, cleaner learning | Low | API write approval | 1 hour | APPROVE |
| 2 | Create retargeting campaign | Only prospecting-style campaign is active | Separate warm/hot retargeting with 20% budget after audiences populate | Lift ROAS by recapturing high-intent users | Medium | Audiences need volume | 1 to 2 hours | APPROVE |
| 3 | Monitor new UGC ads for 72 hours | V2 and V4 just activated | Track spend, CTR, ATC, purchases against winner | Find whether UGC can beat Single Image 3 | Low | Delivery clears review | Daily | APPROVE |
| 4 | Formalize creative test calendar | Reactive creative generation | One new product-anchored UGC per week | Keeps frequency under control | Low | Creative pipeline | Weekly | APPROVE |
| 5 | Placement quality review | Network rows show high CTR, low purchases | If pattern persists, test excluding low-quality inventory | CPA improvement, less noisy traffic | Medium | Need 7 days post-restart | 1 hour | DISCUSS |
| 6 | Keep budget at $50 until stable | Billing blackout just ended | No scale until 14 days stable or ROAS > 3 | Avoids scaling noise | Low | Time | 14 days | APPROVE |
| 7 | Build dashboard daily meta brief | Manual checks today | Automated 7am Telegram with active ad health | Faster kill/scale decisions | Low | Script work | 2 hours | APPROVE |
| 8 | Clean historical account naming/reporting | 129 campaigns, 860 ads history | Archive/reporting map, not deletion | Cleaner analysis, fewer mistakes | Low | Read-only first | 2 hours | DISCUSS |
| 9 | Test material macro creative | Material differentiation is core | One macro per material family: wood, meteorite, carbon fiber | Higher CTR, clearer product value | Low | Product fidelity fix | Weekly | APPROVE |
| 10 | Create lookalike only after exclusions | No audience inventory found | Start purchaser 1% once enough seed exists | Better cold acquisition at scale | Medium | Audience seed size | 2 to 4 weeks | WAIT |

## Immediate next action

Approve audience build plan. It is the highest ROI systems fix and does not require increasing spend.
