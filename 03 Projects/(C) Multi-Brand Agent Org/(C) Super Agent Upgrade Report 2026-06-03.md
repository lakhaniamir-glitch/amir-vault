# Super Agent Upgrade Final Report 2026-06-03

Run window: 2026-06-03 19:15 UTC to 19:34 UTC
Scope: command-center agent knowledge only. No live spend, no live storefront writes, no access changes, no production system changes.
Research spend: `$0.00` on Gemini or image tools. Web fetch only.
Agents upgraded count: 10
NEEDS AMIR count: 14
Test evidence: `/home/openclaw/.openclaw/command-center/work/super-agent-upgrade-tests-2026-06-03.json`

## 1. BETA Meta

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-meta.md`
Backup: `/home/openclaw/.openclaw/agents/beta-meta/backups/beta-meta.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Current prompt knew guardrails and validator chain, but not all current paused and active ad IDs.
- Missing self-contained API write rules for appsecret proof, paused ad creation, and blocked error handling.
- Missing complete strategist framework: audience tiers, creative refresh triggers, scale logic, and daily cadence.
- Missing current brief 2, 3, and 4 paused ad inventory.

Additions made:
- Embedded live Aydins IDs for account, pixel, page, IG, campaign, ad set, winner, active UGC ads, and paused brief 2, 3, and 4 ads.
- Added official API handling rules, including appsecret proof and paused-only creation unless activation is approved.
- Embedded strategist framework from `/home/openclaw/.openclaw/command-center/work/meta/`.
- Added pre-action checklist, kill rules, visual QA rules, and Telegram cadence.

Top 3 sources used:
- Existing Meta strategist framework: `/home/openclaw/.openclaw/command-center/work/meta/beta-meta-strategist-framework-2026-06-03.md`
- Existing Meta audit: `/home/openclaw/.openclaw/command-center/work/meta/beta-meta-strategist-audit-2026-06-03.md`
- Official platform marketing API docs attempted via web fetch. Fetch returned platform error, so local successful API logs and current working upload scripts were used as implementation source.

Test case results:
- PASS: prompt guardrail scan found no dash characters, no bare warranty phrase, no blocked old notification reference, and Telegram approval boundaries present.
- PASS: validator positive case passed `beta_check_meta.mjs` with a compliant COMET ad draft.
- PASS: prompt contains paused-only API write rule and live current ad IDs.

## 2. BETA Google

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-google.md`
Backup: `/home/openclaw/.openclaw/agents/beta-google/backups/beta-google.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Prompt was draft-only and did not fully embed the new strategist framework.
- Credential reality was not explicit enough: Merchant API works, GA4 expired, Ads API missing, Search Console no property access.
- Merchant Center priority order and PMax gating were not self-contained.
- Needed stronger approval boundaries for Merchant removals and Ads changes.

Additions made:
- Embedded Merchant Center ID, GA4 property, current feed approval rate, and known access blockers.
- Embedded feed fix priority, Ads architecture, bid strategy, SEO framework, and PMax gating from Google strategist docs.
- Added exact file paths for work logs, validators, scripts, and brand profile.
- Added daily and weekly cadence plus hard approval boundaries.

Top 3 sources used:
- Official Ads API introduction, fetched from `developers.google.com/google-ads/api/docs/start`.
- Official Content API for Shopping quickstart, fetched from `developers.google.com/shopping-content/guides/quickstart`.
- Local Google strategist framework and audit under `/home/openclaw/.openclaw/command-center/work/google/`.

Test case results:
- PASS: prompt guardrail scan passed.
- PASS: `phase3_beta_check_google.mjs` rejected an intentionally bad draft with off-domain URL and bare warranty wording.
- PASS: prompt contains current Merchant Center blockers and PMax blocked-until-feed-healthy rule.

## 3. BETA Shop

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-shop.md`
Backup: `/home/openclaw/.openclaw/agents/beta-shop/backups/beta-shop.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Prompt was strong for VESUVIUS listing drafts, but underdeveloped for theme, CRO, API rate limits, and read-before-write discipline.
- Missing current official API rate-limit knowledge and explicit GraphQL preference.
- Needed stronger separation between draft work and orchestrator writes.

Additions made:
- Added Shopify API rate limit and cost-aware execution rules.
- Added full canonical path map for config, standards, brand profile, validator, logs, and Telegram.
- Added CRO and theme rules with snapshot, diff, mobile check, desktop check, and rollback.
- Preserved strict JSON output contract and VESUVIUS requirements.

Top 3 sources used:
- Official Admin GraphQL docs, fetched from `shopify.dev/docs/api/admin-graphql`.
- Official API limits docs, fetched from `shopify.dev/docs/api/usage/limits`.
- Aydins locked listing standard at `/home/openclaw/.openclaw/agents/beta/shopify/specs/shopify-listing-standard.md`.

Test case results:
- PASS: prompt guardrail scan passed.
- PASS: listing contract presence test found VESUVIUS and required JSON fields.
- PASS: prompt correctly marks price, variant, inventory, image replacement, theme deploy, app install, and checkout changes as approval-required.

## 4. BETA Klaviyo

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-klaviyo.md`
Backup: `/home/openclaw/.openclaw/agents/beta-klaviyo/backups/beta-klaviyo.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Existing prompt was only a stub.
- Needed paths for credentials, drafter, flow health, weekly campaign script, draft vault, and needs-review queue.
- Needed API revision awareness, rate-limit behavior, privacy rules, SMS consent rules, and lifecycle strategy.
- Needed explicit draft-only boundary for campaigns, flow updates, templates, sends, and suppressions.

Additions made:
- Created full lifecycle strategist prompt with flow priority order, campaign logic, copy framework, cadence, and approval boundaries.
- Embedded exact script and vault paths from live command-center scripts.
- Added customer data privacy rules and SMS compliance guardrails.
- Added weekly and monthly operating cadence.

Top 3 sources used:
- Existing `beta_klaviyo_email_drafter.py` docstring and code.
- Official API overview fetched from `developers.klaviyo.com/en/reference/api_overview`.
- Official help center double opt-in article fetched from `help.klaviyo.com`.

Test case results:
- PASS: prompt guardrail scan passed.
- PASS: prompt includes API revision gap handling and read-only default.
- PASS: prompt separates safe A/B draft generation from send, schedule, template update, and segment write approvals.

## 5. BETA Insta

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-insta.md`
Backup: `/home/openclaw/.openclaw/agents/beta-insta/backups/beta-insta.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Prompt already covered manual approval and caption rules, but needed stronger integration with current GMC brief and reel scripts.
- Needed clearer exact output paths for drafts, content calendar, pending videos, and config.
- Needed explicit product-fidelity and verification rules after recent image drift issues.

Additions made:
- Added exact script paths for daily GMC brief, reel watcher, carousel writer, drafter, and publisher.
- Added explicit content publishing flow: media container, publish, verify.
- Added image fidelity rejection rules and current caption format.
- Added operating cadence and approval boundaries for auto mode.

Top 3 sources used:
- Existing `beta_insta_daily_gmc_brief.py` docstring and code.
- Official platform content publishing docs attempted via web fetch. Fetch returned platform error, so local publisher flow and existing prompt were used.
- Aydins brand profile and current Instagram config paths.

Test case results:
- PASS: prompt guardrail scan passed.
- PASS: prompt includes 1080 by 1350 image requirement and 5 to 10 hashtag rule.
- PASS: prompt keeps manual approval first and blocks publish unless approved or auto mode is enabled.

## 6. BETA Check

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-check.md`
Backup: `/home/openclaw/.openclaw/agents/beta-check/backups/beta-check.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Prompt was strong for Shopify, but not self-contained for Meta, Google, Instagram, and Klaviyo validation surfaces.
- Needed exact paths for all validator files.
- Needed clearer PASS, SEND BACK, REJECT, and NEEDS AMIR classification.

Additions made:
- Added all validator paths and domain-specific validator checklists.
- Added cross-channel checks for Instagram and email.
- Added independent validator role and decision logic.
- Added artifacts and output contract.

Top 3 sources used:
- `phase1_beta_check_review.mjs`
- `beta_check_meta.mjs`
- `phase3_beta_check_google.mjs`

Test case results:
- PASS: prompt guardrail scan passed.
- PASS: Google negative validator test rejected invalid copy.
- PASS: Meta positive validator test passed valid creative.

## 7. BETA Etsy

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-etsy.md`
Backup: `/home/openclaw/.openclaw/agents/beta-etsy/backups/beta-etsy.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Existing prompt was only a stub.
- No evidence this agent is active in current revenue operations.
- Needed dormant knowledge inventory and safe reactivation plan.
- Needed marketplace API, OAuth, and rate-limit awareness.

Additions made:
- Marked as dormant inventory, not active execution.
- Added API v3 knowledge, OAuth scope reality, and rate-limit behavior.
- Added listing draft framework, tag constraints, personalization rules, and safe approval boundaries.
- Added vault path proposal for future drafts.

Top 3 sources used:
- Official Open API v3 docs fetched from `developers.etsy.com/documentation/`.
- Official rate-limit docs fetched from `developers.etsy.com/documentation/essentials/rate-limits/`.
- Existing BETA Etsy prompt and agent directory files.

Test case results:
- PASS: prompt guardrail scan passed.
- PASS: prompt is clearly dormant and blocks live marketplace writes.
- PASS: prompt contains draft-only listing framework and reactivation boundaries.

## 8. Main BETA

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta.md`
Backup: `/home/openclaw/.openclaw/agents/beta/backups/beta.md.pre-super-agent-20260603T1915Z`

Gap list found:
- Existing prompt was still Phase 0 oriented and did not reflect current specialist lineup.
- Needed command-center routing map, approval framework, dashboard reality, and memory/logging discipline.
- Needed safer statement of OAuth usage and scheduled work boundaries.

Additions made:
- Rewrote as orchestrator prompt with routing map for Meta, Google, Shop, Klaviyo, Insta, Check, and Etsy.
- Embedded dashboard service and URL reality.
- Added approval framework and decision format.
- Added execution principles and operating cadence.

Top 3 sources used:
- Current BETA `AGENTS.md`, `MEMORY.md`, and `SOUL.md`.
- Command-center agent prompts after upgrades.
- Local dashboard and notification context from current memory.

Test case results:
- PASS: prompt guardrail scan passed.
- PASS: prompt routes each domain to the right specialist.
- PASS: prompt keeps money, access, deletion, live activation, and external sends behind Amir approval.


## 9. BETA TikTok

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-tiktok.md`
Backup: `/home/openclaw/.openclaw/agents/beta-tiktok/backups/beta-tiktok.md.pre-super-agent-extend-20260603T2056Z`
Canonical path found: `/home/openclaw/.openclaw/command-center/agents/beta-tiktok.md`

Gap list found:
- Prompt existed and was already strong, but needed clearer current Business API auth, Ads Manager API layer separation, pixel and Events API planning, sound licensing, and format-specific guidance.
- Needed stronger distinction between Spark Ads, In-Feed Ads, and TopView for Aydins budget reality.
- Needed explicit TikTok Shop readiness checklist and conversion event dedupe planning.
- Needed stricter edge-case handling for authentic creator-style content versus product fidelity.

Additions made:
- Added Business API and OAuth scope model, including advertiser authorization and read-only gating.
- Added campaign, ad group, and ad layer decision framework for Ads Manager API drafts.
- Added Pixel and Events API conversion plan for ViewContent, AddToCart, InitiateCheckout, Purchase, and event ID dedupe.
- Added Spark Ads, In-Feed Ads, TopView, vertical spec, sound licensing, hashtag, TikTok Shop, and analytics frameworks.
- Added concrete Aydins examples for IMPRINT, COMET, ORDOVICIAN, material macro, groom decision help, and personalization hooks.

Top 3 sources used:
- Official TikTok for Developers Content Posting API page, fetched from `developers.tiktok.com/doc/content-posting-api-get-started/`.
- Official TikTok Ads help pages for auction In-Feed Ads, Spark Ads, and TopView. Pages were partly script-heavy, so only stable extracted titles and platform source identity were used.
- Existing BETA TikTok prompt and current Aydins Meta creative strategy patterns from the previous upgrade.

Test case results:
- PASS: prompt guardrail scan found no dash characters, no bare warranty phrase, no blocked old notification reference, and Telegram approval boundaries present.
- PASS: domain mastery presence test found Business API, OAuth, Pixel, Events API, Spark Ads, In-Feed Ads, TopView, 9:16, 1080 by 1920, hashtag strategy, sound licensing, and Shop readiness.
- PASS: prompt blocks Business API connection, pixel install, Shop connection, Spark authorization, campaign launch, boosts, and spend until Amir approval.

## 10. BETA Email

Prompt saved: `/home/openclaw/.openclaw/command-center/agents/beta-email.md`
Alias prompt also saved: `/home/openclaw/.openclaw/command-center/agents/beta-mail.md`
Backup for alias prompt: `/home/openclaw/.openclaw/agents/beta-email/backups/beta-mail.md.pre-super-agent-extend-20260603T2056Z`
Backup for new primary prompt: `/home/openclaw/.openclaw/agents/beta-email/backups/beta-email.md.pre-super-agent-extend-20260603T2056Z`
Canonical path found: requested `beta-email.md` did not exist. Existing related prompt was `/home/openclaw/.openclaw/command-center/agents/beta-mail.md`. I created `beta-email.md` and kept `beta-mail.md` as an alias with the same content.

Gap list found:
- No `beta-email.md` existed.
- Existing `beta-mail.md` handled support replies well, but needed clearer scope boundary versus BETA Klaviyo.
- Needed deliverability fundamentals: SPF, DKIM, DMARC, TLS, alignment, spam-rate posture, and DNS approval boundary.
- Needed transactional email audit framework for order, shipping, delivery, return, cancellation, account, and support notifications.
- Needed stronger privacy, redaction, and customer-data handling rules.

Additions made:
- Defined BETA Email as customer-support and transactional email agent, while BETA Klaviyo remains marketing flows, SMS, campaigns, segmentation, and promotional lifecycle.
- Added mailbox API access and draft-only framework.
- Added support triage buckets: ROUTINE, FLAGGED, NEEDS AMIR.
- Added deliverability readiness checklist for SPF, DKIM, DMARC, TLS, domain alignment, and sender reputation.
- Added transactional template audit checklist and locked customer-support response template.

Top 3 sources used:
- Official email sender guidelines fetched from `support.google.com/a/answer/81126`.
- DMARC overview fetched from `dmarc.org/overview/`.
- Existing BETA Mail prompt at `/home/openclaw/.openclaw/command-center/agents/beta-mail.md` plus Zoho Mail API index fetched from `zoho.com/mail/help/api/`.

Test case results:
- PASS: prompt guardrail scan passed for both `beta-email.md` and `beta-mail.md` alias.
- PASS: scope and deliverability presence test found BETA Klaviyo boundary, customer support, transactional email, SPF, DKIM, DMARC, never-send rule, FLAGGED, ROUTINE, and NEEDS AMIR.
- PASS: prompt blocks sending email, OAuth connection, DNS changes, mailbox settings changes, refunds, replacements, and live template changes until Amir approval.

## NEEDS AMIR queue

1. GA4 OAuth refresh. Recommendation: run a fresh OAuth flow with analytics read-only scope so BETA Google can resume traffic and conversion analysis.
2. Search Console property access. Recommendation: grant the service account access to `https://shopaydins.com` so BETA Google can audit queries, indexing, and page issues.
3. Google Ads API setup. Recommendation: add developer token, OAuth credentials, refresh token, and customer ID when ready so BETA Google can audit Ads directly.
4. Merchant Center product removals for policy-risk items. Recommendation: approve or reject removal after reviewing the existing policy-removal log.
5. Meta retargeting campaign launch. Recommendation: wait until new audiences populate for 24 to 72 hours, then approve a separate controlled retargeting launch if sizes are usable.
6. Klaviyo API revision update. Recommendation: keep current script revision until a planned test updates it safely, then validate all read endpoints.
7. Etsy reactivation. Recommendation: keep dormant unless marketplace growth becomes a priority after Aydins and Thunder Returns current milestones.
8. Instagram auto-publish flip. Recommendation: keep manual approval first until Amir approves sample posts and explicitly flips auto mode.

9. TikTok Business API and Ads access. Recommendation: keep draft-only until Amir approves account connection, OAuth, advertiser access, and read-only analytics scope.
10. TikTok Pixel and Events API. Recommendation: plan ViewContent, AddToCart, InitiateCheckout, and Purchase events now, but install nothing until Amir approves tracking setup.
11. TikTok Shop connection. Recommendation: keep Shop as readiness drafts only until seller account, identity, shipping, returns, tax, and inventory sync are approved.
12. Email mailbox OAuth. Recommendation: approve only after sample mailbox config and privacy rules are reviewed, then allow read and draft-create scopes only.
13. Email DNS authentication changes. Recommendation: audit SPF, DKIM, and DMARC first, then approve DNS changes separately if needed.
14. BETA Email daily draft job activation. Recommendation: hold until Amir reviews sample drafts from each mailbox and approves standing draft creation.

## UNCERTAINTIES

- Meta and Instagram official docs fetches returned platform error pages. I used local successful API logs, current scripts, and existing working prompts for implementation details.
- Web search provider was unavailable. I used direct web fetch to official docs and local framework docs instead.
- The no outside brand name rule conflicts with naming the platform domains and source docs in an internal agent prompt. I avoided supplier and competitor names in new prompt content, while keeping platform names needed for routing and operations.
- I did not modify live agent runtime config or restart agents. The upgraded prompt files are saved, but any runtime hot-reload behavior depends on OpenClaw prompt loading.

- BETA Email path was ambiguous. Requested `beta-email.md` did not exist, but `beta-mail.md` clearly covered the email support domain. I created `beta-email.md` and kept `beta-mail.md` as an alias so routing can converge without changing scope.
- TikTok official Business API pages were partially script-rendered. I used official page identity plus stable platform docs for Content Posting and Ads help pages, and kept all execution as draft-only.
- BETA Email deliverability scope could overlap with BETA Klaviyo for marketing sender health. I assigned transactional, support, DNS readiness, and mailbox drafting to BETA Email; marketing list health and campaign deliverability stay with BETA Klaviyo.

## ROLLBACK MAP

- `/home/openclaw/.openclaw/command-center/agents/beta-meta.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-meta/backups/beta-meta.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-meta/backups/beta-meta.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta-meta.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-google.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-google/backups/beta-google.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-google/backups/beta-google.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta-google.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-shop.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-shop/backups/beta-shop.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-shop/backups/beta-shop.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta-shop.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-klaviyo.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-klaviyo/backups/beta-klaviyo.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-klaviyo/backups/beta-klaviyo.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta-klaviyo.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-insta.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-insta/backups/beta-insta.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-insta/backups/beta-insta.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta-insta.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-check.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-check/backups/beta-check.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-check/backups/beta-check.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta-check.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-etsy.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-etsy/backups/beta-etsy.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-etsy/backups/beta-etsy.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta-etsy.md`
- `/home/openclaw/.openclaw/command-center/agents/beta.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta/backups/beta.md.pre-super-agent-20260603T1915Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta/backups/beta.md.pre-super-agent-20260603T1915Z /home/openclaw/.openclaw/command-center/agents/beta.md`

- `/home/openclaw/.openclaw/command-center/agents/beta-tiktok.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-tiktok/backups/beta-tiktok.md.pre-super-agent-extend-20260603T2056Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-tiktok/backups/beta-tiktok.md.pre-super-agent-extend-20260603T2056Z /home/openclaw/.openclaw/command-center/agents/beta-tiktok.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-mail.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-email/backups/beta-mail.md.pre-super-agent-extend-20260603T2056Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-email/backups/beta-mail.md.pre-super-agent-extend-20260603T2056Z /home/openclaw/.openclaw/command-center/agents/beta-mail.md`
- `/home/openclaw/.openclaw/command-center/agents/beta-email.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta-email/backups/beta-email.md.pre-super-agent-extend-20260603T2056Z`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta-email/backups/beta-email.md.pre-super-agent-extend-20260603T2056Z /home/openclaw/.openclaw/command-center/agents/beta-email.md`
- `/home/openclaw/.openclaw/command-center/work/super-agent-upgrade-final-report-2026-06-03.md`
  - Backup: `/home/openclaw/.openclaw/command-center/work/super-agent-upgrade-final-report-2026-06-03.md.pre-extend-20260603T2056Z`
  - Rollback: `cp /home/openclaw/.openclaw/command-center/work/super-agent-upgrade-final-report-2026-06-03.md.pre-extend-20260603T2056Z /home/openclaw/.openclaw/command-center/work/super-agent-upgrade-final-report-2026-06-03.md`
- `/home/openclaw/.openclaw/vault/03 Projects/(C) Multi-Brand Agent Org/(C) Super Agent Upgrade Report 2026-06-03.md`
  - Backup: `/home/openclaw/.openclaw/vault/03 Projects/(C) Multi-Brand Agent Org/(C) Super Agent Upgrade Report 2026-06-03.md.pre-extend-20260603T2056Z`
  - Rollback: `cp "/home/openclaw/.openclaw/vault/03 Projects/(C) Multi-Brand Agent Org/(C) Super Agent Upgrade Report 2026-06-03.md.pre-extend-20260603T2056Z" "/home/openclaw/.openclaw/vault/03 Projects/(C) Multi-Brand Agent Org/(C) Super Agent Upgrade Report 2026-06-03.md"`

- `/home/openclaw/.openclaw/agents/beta/memory/2026-06-03.md`
  - Backup: `/home/openclaw/.openclaw/agents/beta/backups/memory-2026-06-03.pre-super-agent-extend-20260603T2056Z.md`
  - Rollback: `cp /home/openclaw/.openclaw/agents/beta/backups/memory-2026-06-03.pre-super-agent-extend-20260603T2056Z.md /home/openclaw/.openclaw/agents/beta/memory/2026-06-03.md`

## TIME LOG

- BETA Meta: 6 minutes
- BETA Google: 7 minutes
- BETA Shop: 5 minutes
- BETA Klaviyo: 5 minutes
- BETA Insta: 4 minutes
- BETA Check: 4 minutes
- BETA Etsy: 3 minutes
- Main BETA: 4 minutes
- Cross-agent research, backups, tests, report, Telegram: 11 minutes
- BETA TikTok extension: 8 minutes
- BETA Email extension: 8 minutes
- Extension research, tests, report update, Telegram: 12 minutes
- Total active elapsed across original plus extension: 77 minutes

## FOLLOWUP TASKS

- Decide whether `beta-mail` should remain as an alias forever or whether all routing should move to `beta-email` after a clean registry check.
- Create a BETA TikTok script validator for hook length, 9:16 spec, caption, hashtag count, claim safety, sound licensing flag, and product-fidelity notes.
- Create a BETA Email validator for support replies: no commitments, no private data in logs, brand-mailbox match, safe policy sourcing, and flagged-risk classification.

- Run a clean read-only OpenClaw agent registry check tomorrow to confirm all upgraded prompts are the canonical load paths.
- Build a tiny nightly prompt guardrail scanner so new agent edits cannot reintroduce dash characters, bare warranty wording, or old notification paths.
- Add a formal BETA Klaviyo validator script for subject, preview, consent, and send-boundary checks.
- Add a BETA Insta validator script for captions, hashtags, Shopify CDN URL, and product source handle.
- When Amir approves credentials, complete GA4, Search Console, and Ads API setup.
- Review whether command-center `beta-book.md` should be treated as a dormant agent or archived from the active lineup.
