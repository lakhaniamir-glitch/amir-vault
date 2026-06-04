# Meta Blackout Root Cause - Aydins - 2026-06-02

Status: confirmed
Account: act_23304577
Window: roughly 2026-05-25 through 2026-06-02 morning
Mode: read-only review only

No payment method changes, threshold changes, billing setting writes, spend changes, campaign changes, ad set changes, ad changes, audience changes, or account setting writes were made.

## Confirmed cause

Billing, confirmed directly by Amir.

Delivery resumed after Amir settled payment on the morning of 2026-06-02.

## Specific failure mode found

Meta threshold billing charge failures.

The ad account uses threshold billing:

- Current billing threshold: $900.00
- Current balance at review: about $7.91 to $8.16
- Funds/prepay balance: $0.00
- Billing mode: threshold billing, not prepaid funding and not monthly invoicing from the visible billing screen

Visible payment methods:

- Default: American Express ending 1004, expires 6/27
- Backup or alternate: PayPal sales@aydins.com, active from visible billing screen
- Backup or alternate: MasterCard ending 4041, expired 02/26
- Ad credit: $0.02

Visible payment activity from May 2026 through 2026-06-02:

- 2026-05-26: $903.00 failed via PayPal sales@aydins.com
- 2026-05-26: $903.00 failed via MasterCard ending 4041
- 2026-05-26: $903.00 failed via American Express ending 1004
- 2026-05-26: $903.00 failed via PayPal sales@aydins.com
- 2026-05-26: $903.00 failed via MasterCard ending 4041
- 2026-05-30: $903.00 failed via PayPal sales@aydins.com
- 2026-05-30: $903.00 failed via MasterCard ending 4041
- 2026-05-30: $903.00 failed via American Express ending 1004
- 2026-06-01: $903.00 failed via American Express ending 1004
- 2026-06-02: $903.00 paid via PayPal sales@aydins.com

Account Quality showed no account or asset issues in the last 30 days, so policy enforcement was not the visible cause.

## Resolution

Amir settled the payment on 2026-06-02 morning. Meta payment activity shows a successful $903.00 payment on 2026-06-02 via PayPal, which matches delivery resuming.

## Prevention measures shipped

Created daily read-only Meta billing health check:

- Script: `/home/openclaw/.openclaw/command-center/scripts/meta_billing_health_check.mjs`
- State file: `/home/openclaw/.openclaw/command-center/work/meta/meta-billing-health-state.json`
- Capture file: `/home/openclaw/.openclaw/command-center/work/meta/meta-billing-health-capture-YYYY-MM-DD.json`
- Screenshots: `/home/openclaw/.openclaw/agents/beta/screens/meta-billing-health/`
- Cron: daily at 6:00 AM Central using `CRON_TZ=America/Chicago`
- Log: `/home/openclaw/.openclaw/logs/meta_billing_health_check.log`

The health check pulls:

- Billing payment method status: active, expired, declined or failed indicators
- Current balance versus billing threshold, with alert if balance reaches 80 percent of threshold
- Last successful charge date and method
- Pending issues from Account Quality
- Billing type, funds balance, visible payment methods, recent failed rows

Alert behavior:

- Healthy: silent, writes state and capture logs only
- Warning: hard alert to Slack alerts channel and Telegram push to Amir with subject line `BILLING RISK`
- Morning digest: Phase 1 daily digest now includes the latest Meta billing health section from the state file

## Open risks

- MasterCard ending 4041 is expired and still visible as an alternate payment method.
- The account appears dependent on American Express 1004 plus PayPal after the expired MasterCard.
- Meta showed a daily spending limit pause warning on 2026-06-02 after payment recovery.
- Cookie-based browser checks can break if Meta expires the session, triggers verification, or changes UI structure.
- No manual weekly billing review cadence exists yet.

## One-line recommendation

Replace or remove the expired MasterCard 4041, keep PayPal as a working backup, and review Meta Billing every Monday until API access is approved.
