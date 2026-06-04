# Catalog Sales Post-Mortem - Aydins Meta Ads - 2026-06-02

Status: filed for record
Campaign ID: 52566193429730
Campaign: Catalog Sales
Decision: paused 2026-06-02 09:50 PT
Lockout: do not test reset for 60 days minimum

## Final read

Catalog Sales was not a tracking mystery or a small settings issue. It failed because the retargeting pool was too small for the budget being forced through it. The campaign kept showing to the same limited pool until frequency rose, marginal buyers were exhausted, and efficiency degraded.

This campaign stays paused. The fix is not a reset. The fix is larger, healthier prospecting traffic first.

## Final 30-day stats

| Metric | Value |
|---|---:|
| Spend | $536.53 |
| Purchases | 6 |
| ROAS | 2.09 |
| Frequency | 9.21 |
| CPM | $26.49 |

## Final 14-day degradation

| Metric | Value |
|---|---:|
| ROAS | 1.16 |
| CPA | $126.24 |
| Frequency | 5.04 |

## Root cause

Retargeting pool was too small: approximately 827 landing page views per month from Meta.

At $25/day, Catalog Sales was trying to spend into a pool that could not absorb that pressure. The result was high frequency, repeated impressions to the same people, and falling purchase efficiency.

This is structural. Editing copy, resetting learning, duplicating the campaign, or swapping catalog settings does not solve the pool-size problem.

## Why it should stay paused

1. Frequency was already too high at 9.21 over the 30-day window.
2. The 14-day window showed clear deterioration, not recovery.
3. CPA degraded to $126.24, above acceptable operating range.
4. ROAS dropped to 1.16 in the recent window.
5. The active Couples Engraved prospecting winner is the better use of spend right now.

## Recovery conditions before reconsidering Catalog Sales

Do not revive Catalog Sales until all conditions below are met:

1. Meta landing page views reach 3,000 or more per month.
2. Prospecting can hold $75 to $100 per day while ROAS stays above 3.0.
3. Tracking is verified clean: EMQ, Pixel/CAPI dedup, AEM Purchase priority, and diagnostics clear.
4. Fresh creative pipeline has at least one new approved ad concept live in the winning ad set.
5. The current 60-day lockout has passed.

## Lockout rule

Catalog Sales is locked out for 60 days minimum from 2026-06-02.

Earliest review date: 2026-08-01.

Review does not mean restart. Review means check recovery conditions. If recovery conditions are not met, keep it paused.

## Decision record

*Meta Ads decision recorded - 2026-06-02*
What: Catalog Sales remains paused for 60 days minimum.
Why: 30-day frequency hit 9.21 and recent 14-day ROAS degraded to 1.16 with $126.24 CPA.
Risk if kept paused: Miss a small amount of low-volume retargeting revenue.
Risk if revived early: Burn budget into the same exhausted 827 LPV/month pool and repeat the failure.
Beta's recommendation: KEEP PAUSED

## Source notes

Handoff values used:

- Final 30-day stats: spend $536.53, 6 purchases, ROAS 2.09, frequency 9.21, CPM $26.49.
- Final 14-day degradation: ROAS 1.16, CPA $126.24, frequency 5.04.
- Root cause: retargeting pool too small at approximately 827 LPV/month.
- Recovery condition: Meta LPV 3,000+/month and prospecting $75 to $100/day holding ROAS above 3.0.

The requested vault source search did not surface a separate Meta audit document under `/home/openclaw/vault/03 Projects/Aydins Jewelry/`; the post-mortem uses the locked handoff stats and the same-day Meta audit context already present in Beta's workspace.
