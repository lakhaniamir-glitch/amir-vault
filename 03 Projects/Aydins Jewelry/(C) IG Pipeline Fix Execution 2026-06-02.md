# IG Pipeline Fix Execution, 2026-06-02

## Result

WILL TOMORROW POST: NO with current state.

Confidence: high.

Reason: the approved changes were executed, but Jun 3 image slots now have status approved-queued with no draft_path. The publisher requires an existing draft file. At publish time it will hit its No draft skip branch.

## Scope executed

Approved changes executed only:

1. Gemini fallback config corrected.
2. GMC brief cron env var placement corrected.
3. Jun 3 draft-failed image slots reset to approved-queued.

No Gemini API generation call was made. No Shopify write was made. No Meta change was made. No theme write was made.

## Step 1 snapshots

Required backups created and verified non-zero:

```text
73235 /home/openclaw/.openclaw/command-center/scripts/phase2_daily_drafter.py.bak-2026-06-02-igfix
9348 /home/openclaw/.openclaw/agents/beta/backups/crontab-2026-06-02-igfix.txt
42402 /home/openclaw/.openclaw/command-center/work/phase2/backups/insta-content-calendar-20260603T025350Z-igfix.json
```

Additional safety backup for the effective Gemini config:

```text
342 /home/openclaw/.openclaw/agents/beta/credentials/gemini.env.bak-2026-06-02-igfix
```

## Step 2 Gemini fallback fix

Finding during execution: the bad fallback model was not hardcoded in phase2_daily_drafter.py. The script loads it from:

/home/openclaw/.openclaw/agents/beta/credentials/gemini.env

Effective line changed:

```diff
-GEMINI_FALLBACK_MODEL=imagen-3.0-generate-002
+GEMINI_FALLBACK_MODEL=gemini-2.5-flash-image
```

Rationale: gemini-2.5-flash-image is the same model that previously succeeded in this script's v1beta generateContent image path. This avoids the invalid fallback 404 while keeping behavior deterministic.

Python syntax validation:

```text
python3 -m py_compile /home/openclaw/.openclaw/command-center/scripts/phase2_daily_drafter.py
PASS
```

## Step 3 GMC brief cron env var placement

Crontab installed cleanly and verified with crontab -l.

Exact crontab diff:

```diff
--- /home/openclaw/.openclaw/agents/beta/backups/crontab-2026-06-02-igfix.txt	2026-06-03 02:53:50.977864193 +0000
+++ /tmp/crontab-after-igfix.txt	2026-06-03 02:54:15.103687302 +0000
@@ -49,7 +49,8 @@
 
 # === GMC hybrid reel pipeline (added 2026-05-29) ===
 # BETA Insta daily GMC brief - daily 4am CT (09:00 UTC CDT)
-0 9 * * * /home/openclaw/.openclaw/command-center/scripts/cron_run.sh beta-insta-daily-gmc-brief BETA_INSTA_BRIEFS_PER_RUN=3 /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/beta_insta_daily_gmc_brief.py >> /home/openclaw/.openclaw/command-center/logs/beta_insta_gmc_brief.log 2>&1
+BETA_INSTA_BRIEFS_PER_RUN=3
+0 9 * * * /home/openclaw/.openclaw/command-center/scripts/cron_run.sh beta-insta-daily-gmc-brief /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/beta_insta_daily_gmc_brief.py >> /home/openclaw/.openclaw/command-center/logs/beta_insta_gmc_brief.log 2>&1
 # BETA Insta reel watcher - every 30 min
 */30 * * * * /home/openclaw/.openclaw/command-center/scripts/cron_run.sh beta-insta-reel-watcher /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/beta_insta_reel_watcher.py >> /home/openclaw/.openclaw/command-center/logs/beta_insta_reel_watcher.log 2>&1
 # Claudian Command Center Inbox refresh - every 15 min

```

Current verified crontab lines:

```text
BETA_INSTA_BRIEFS_PER_RUN=3
0 9 * * * /home/openclaw/.openclaw/command-center/scripts/cron_run.sh beta-insta-daily-gmc-brief /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/beta_insta_daily_gmc_brief.py >> /home/openclaw/.openclaw/command-center/logs/beta_insta_gmc_brief.log 2>&1
```

## Step 4 Jun 3 slot reset

Changed count: 3.

Only statuses changed versus the calendar backup:

```json
{
  "status_changes": [
    [20, "2026-06-03-0800-ct", "2026-06-03", "draft-failed", "approved-queued"],
    [21, "2026-06-03-1300-ct", "2026-06-03", "draft-failed", "approved-queued"],
    [22, "2026-06-03-1900-ct", "2026-06-03", "draft-failed", "approved-queued"]
  ],
  "count": 3
}
```

Full reset receipt:

```json
{
  "changed_count": 3,
  "changes": [
    {
      "index": 20,
      "slot_id": "2026-06-03-0800-ct",
      "before_status": "draft-failed",
      "after_status": "approved-queued",
      "before": {
        "slot_id": "2026-06-03-0800-ct",
        "date": "2026-06-03",
        "time_central": "08:00",
        "category": "ugc",
        "status": "draft-failed",
        "post_id": null,
        "draft_path": null,
        "_composition_id": "single_finger",
        "last_draft_error": "Gemini error 404: {\n  \"error\": {\n    \"code\": 404,\n    \"message\": \"models/imagen-3.0-generate-002 is not found for API version v1beta, or is not supported for generateContent. Call ModelService.ListModels to see the list of available models and their supported methods.\",\n    \"status\": \"NOT_FOUND\"\n  }"
      },
      "after": {
        "slot_id": "2026-06-03-0800-ct",
        "date": "2026-06-03",
        "time_central": "08:00",
        "category": "ugc",
        "status": "approved-queued",
        "post_id": null,
        "draft_path": null,
        "_composition_id": "single_finger",
        "last_draft_error": "Gemini error 404: {\n  \"error\": {\n    \"code\": 404,\n    \"message\": \"models/imagen-3.0-generate-002 is not found for API version v1beta, or is not supported for generateContent. Call ModelService.ListModels to see the list of available models and their supported methods.\",\n    \"status\": \"NOT_FOUND\"\n  }",
        "approved_by": "BETA IG pipeline fix 2026-06-02",
        "approved_at": "2026-06-03T02:54:00+00:00"
      }
    },
    {
      "index": 21,
      "slot_id": "2026-06-03-1300-ct",
      "before_status": "draft-failed",
      "after_status": "approved-queued",
      "before": {
        "slot_id": "2026-06-03-1300-ct",
        "date": "2026-06-03",
        "time_central": "13:00",
        "category": "ugc",
        "status": "draft-failed",
        "post_id": null,
        "draft_path": null,
        "_composition_id": "leaning_canvas",
        "last_draft_error": "Caption self-check failed for 2026-06-03-1300-ct: ['close repeats recent: Wear the edge at Aydins.', 'source_product missing or empty \u2014 every draft must anchor to a real product']"
      },
      "after": {
        "slot_id": "2026-06-03-1300-ct",
        "date": "2026-06-03",
        "time_central": "13:00",
        "category": "ugc",
        "status": "approved-queued",
        "post_id": null,
        "draft_path": null,
        "_composition_id": "leaning_canvas",
        "last_draft_error": "Caption self-check failed for 2026-06-03-1300-ct: ['close repeats recent: Wear the edge at Aydins.', 'source_product missing or empty \u2014 every draft must anchor to a real product']",
        "approved_by": "BETA IG pipeline fix 2026-06-02",
        "approved_at": "2026-06-03T02:54:00+00:00"
      }
    },
    {
      "index": 22,
      "slot_id": "2026-06-03-1900-ct",
      "before_status": "draft-failed",
      "after_status": "approved-queued",
      "before": {
        "slot_id": "2026-06-03-1900-ct",
        "date": "2026-06-03",
        "time_central": "19:00",
        "category": "product_showcase",
        "status": "draft-failed",
        "post_id": null,
        "category_changed_at": "2026-05-31",
        "category_changed_reason": "Killed faq_visual format (weak image hook). Replaced with product_showcase.",
        "_composition_id": "macro_texture",
        "last_draft_error": "OpenRouter caption returned empty content: {\"id\": \"gen-1780390863-TrbLi0xxBf2N1jXFW0FM\", \"object\": \"chat.completion\", \"created\": 1780390863, \"model\": \"deepseek/deepseek-v4-flash-20260423\", \"provider\": \"SiliconFlow\", \"system_fingerprint\": null, \"service_tier\": null, \"choices\": [{\"index\": 0, \"logprobs"
      },
      "after": {
        "slot_id": "2026-06-03-1900-ct",
        "date": "2026-06-03",
        "time_central": "19:00",
        "category": "product_showcase",
        "status": "approved-queued",
        "post_id": null,
        "category_changed_at": "2026-05-31",
        "category_changed_reason": "Killed faq_visual format (weak image hook). Replaced with product_showcase.",
        "_composition_id": "macro_texture",
        "last_draft_error": "OpenRouter caption returned empty content: {\"id\": \"gen-1780390863-TrbLi0xxBf2N1jXFW0FM\", \"object\": \"chat.completion\", \"created\": 1780390863, \"model\": \"deepseek/deepseek-v4-flash-20260423\", \"provider\": \"SiliconFlow\", \"system_fingerprint\": null, \"service_tier\": null, \"choices\": [{\"index\": 0, \"logprobs",
        "approved_by": "BETA IG pipeline fix 2026-06-02",
        "approved_at": "2026-06-03T02:54:00+00:00"
      }
    }
  ]
}

```

## Step 5 dry-run validation

No real Gemini API call was made.

There is no safe dry-run flag visible for phase2_daily_drafter.py, so validation was static and no API:

```json
{
  "dry_run_type": "static_no_api",
  "script_compiles": true,
  "generateContent_path_present": true,
  "primary_model": "gemini-2.5-flash-image",
  "fallback_model": "gemini-2.5-flash-image",
  "invalid_model_present_in_env": false
}
```

This confirms the invalid fallback model is removed from the effective config and no 404 fallback path is present from the previous bad model string.

## Publish readiness check

Jun 3 image slots after reset:

```json
[
  {
    "slot_id": "2026-06-03-0800-ct",
    "status": "approved-queued",
    "draft_path": null,
    "draft_exists": false
  },
  {
    "slot_id": "2026-06-03-1300-ct",
    "status": "approved-queued",
    "draft_path": null,
    "draft_exists": false
  },
  {
    "slot_id": "2026-06-03-1900-ct",
    "status": "approved-queued",
    "draft_path": null,
    "draft_exists": false
  }
]
```

Publisher behavior requires slot draft_path to exist for image posts. With the current state, Jun 3 slots will be candidates when due, but each will skip at this branch:

```python
if not slot.get("draft_path") or not os.path.exists(slot["draft_path"]):
    log(f"  No draft. Skip."); continue
```

## Remaining blocker

The approved status reset alone does not create or attach valid draft JSON files. To actually save tomorrow, one additional approved action is needed:

- Create or regenerate valid draft files for the Jun 3 slots and attach their draft_path, or reset them to queued and run a controlled drafter pass that can generate real drafts.

That additional action would involve generation and likely Shopify file upload, so it was not performed under the hard rules of this approval.
