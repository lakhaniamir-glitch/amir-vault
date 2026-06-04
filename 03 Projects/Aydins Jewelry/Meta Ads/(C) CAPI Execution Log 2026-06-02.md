# CAPI EMQ Toggle Execution Log - 2026-06-02

Status: completed with UI note
Mode: approved Events Manager settings write
Pixel and Dataset: 1151493648281503
Business: Aydins Jewelry

## Guardrails followed

No spend changes.
No campaign, ad set, ad, audience, budget, domain allowlist, or custom event changes.
No Shopify data sharing level change.
No Gender change.
No Date of birth change.
Only the four approved Automatic website matching parameters were changed.

## Before state

Screenshot:

`/home/openclaw/.openclaw/agents/beta/screens/meta-capi-execution-2026-06-02/emq-01-before-toggles.png`

| Parameter | Before |
|---|---|
| Email | On |
| Phone number | Off |
| First and last name | On |
| Gender | Off |
| City, State, ZIP or Postal Code | Off |
| Country | Off |
| Date of birth | Off |
| External id | Off |

## Changes made

| Parameter | Before | After | Result |
|---|---|---|---|
| Phone number | Off | On | Changed |
| City, State, ZIP or Postal Code | Off | On | Changed |
| Country | Off | On | Changed |
| External id | Off | On | Changed |
| Gender | Off | Off | Not touched |
| Date of birth | Off | Off | Not touched |

External ID outcome: present and changed from Off to On.

After-toggle screenshot:

`/home/openclaw/.openclaw/agents/beta/screens/meta-capi-execution-2026-06-02/emq-02-after-toggles-before-save.png`

## Save behavior

The UI showed a Save control, but Playwright reported it was disabled and could not click it. No privacy, legal, Confirm, Accept, or Continue modal appeared.

Important: after refreshing the Settings page, the four approved toggles persisted as On. This indicates the UI auto-persisted the parameter changes or saved them without enabling the visible Save control.

Final refreshed verification screenshot:

`/home/openclaw/.openclaw/agents/beta/screens/meta-capi-execution-2026-06-02/emq-05-final-refresh-verification.png`

Final state:

| Parameter | Final |
|---|---|
| Email | On |
| Phone number | On |
| First and last name | On |
| Gender | Off |
| City, State, ZIP or Postal Code | On |
| Country | On |
| Date of birth | Off |
| External id | On |

Raw execution result:

`/home/openclaw/.openclaw/command-center/work/meta/emq-toggle-execution-result-2026-06-02.json`

Final verification result:

`/home/openclaw/.openclaw/command-center/work/meta/emq-toggle-final-verify-2026-06-02.json`

## Post-write verification

Screenshots:

- Overview baseline: `/home/openclaw/.openclaw/agents/beta/screens/meta-capi-execution-2026-06-02/post-overview.png`
- Test Events status: `/home/openclaw/.openclaw/agents/beta/screens/meta-capi-execution-2026-06-02/post-test-events.png`
- Diagnostics: `/home/openclaw/.openclaw/agents/beta/screens/meta-capi-execution-2026-06-02/post-diagnostics.png`

Raw post-write verification:

`/home/openclaw/.openclaw/command-center/work/meta/post-write-verify-2026-06-02.json`

Notes:

- EMQ values are not expected to move immediately.
- Test Events tab was opened read-only. No test event sent.
- Diagnostics still show the pre-existing domain and CAPI quality tasks. No new issue was identified from the screenshots immediately after the change.

## 72-hour EMQ recheck cron

Cron name:

`meta-emq-recheck-2026-06-05`

Schedule:

`0 13 5 6 * cd /home/openclaw/.openclaw && node /home/openclaw/.openclaw/command-center/scripts/meta_emq_recheck_2026_06_05.mjs >> /home/openclaw/.openclaw/logs/meta_emq_recheck_2026_06_05.log 2>&1`

This is 2026-06-05 08:00 Central.

Script:

`/home/openclaw/.openclaw/command-center/scripts/meta_emq_recheck_2026_06_05.mjs`

Output:

`/home/openclaw/.openclaw/command-center/work/meta/emq-recheck-2026-06-05.md`

If cookie session is expired, it will report SESSION_EXPIRED to Slack.

## What to watch in 72 hours

Baseline from Task 2:

- Purchase EMQ: 8.0/10
- AddToCart EMQ: 5.1/10
- ViewContent EMQ: 5.2/10
- InitiateCheckout EMQ: 5.9/10
- ViewContent CAPI coverage: 71%

Desired movement:

- Purchase stays at or above 8.0.
- AddToCart improves toward 7.0.
- ViewContent improves toward 6.0.
- ViewContent CAPI coverage improves toward 75%.
