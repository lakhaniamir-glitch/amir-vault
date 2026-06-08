# Deploy: 6 new agent research briefs

**Date:** 2026-06-08
**What:** Add `beta-tiktok`, `beta-klaviyo`, `beta-shop`, `beta-etsy`, `beta-ebay`, `beta-design` to the daily 4am CT research loop.
**Cost impact:** ~$0.30/day -> ~$0.90/day on OpenRouter (DeepSeek v3.2).

> **STATUS: DEPLOYED (overnight 2026-06-08).**
> All 6 YAMLs uploaded to `/home/openclaw/.openclaw/agents/research-briefs/` on VPS.
> All 6 pass `yaml.safe_load`. Cron at `0 9 * * *` is active and the script globs the directory, so no script patch was needed.
> Schema was rewritten from my first draft to match the actual format used by `beta-google.yaml` / `beta-meta.yaml` / `beta-insta.yaml` (single `focus` + `business_context` + `topics` + `sources` + `alert_keywords` + `output_dir`, not the bloated multi-section format I started with).
> See [[(C) Agent Research Loop — Hub]] for the morning view.
>
> The steps below are kept as reference for future deploys.

---

## Files to deploy

All 6 YAMLs are staged in this folder:

```
03 Projects/Aydins Jewelry/06 System/research-briefs-staging/
  beta-tiktok.yaml
  beta-klaviyo.yaml
  beta-shop.yaml
  beta-etsy.yaml
  beta-ebay.yaml
  beta-design.yaml         (AI tools scout, redefined mandate)
```

**Target on VPS:**
```
/home/openclaw/.openclaw/agents/research-briefs/
```

---

## Deploy steps (manual, if Amir runs it)

### Step 1. Copy YAMLs to VPS

From the local vault on the laptop:

```powershell
# PowerShell
$VPS = "openclaw@<vps-host>"  # use your actual host or shortcut
$SRC = "C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\06 System\research-briefs-staging"
$DST = "/home/openclaw/.openclaw/agents/research-briefs/"

scp "$SRC\beta-tiktok.yaml"  "${VPS}:$DST"
scp "$SRC\beta-klaviyo.yaml" "${VPS}:$DST"
scp "$SRC\beta-shop.yaml"    "${VPS}:$DST"
scp "$SRC\beta-etsy.yaml"    "${VPS}:$DST"
scp "$SRC\beta-ebay.yaml"    "${VPS}:$DST"
scp "$SRC\beta-design.yaml"  "${VPS}:$DST"
```

### Step 2. Match the existing schema (only if first run fails)

Existing briefs (`beta-google.yaml`, `beta-meta.yaml`, `beta-insta.yaml`) were written in the previous session. The new YAMLs use a schema I reconstructed from the session log. If the runner rejects them, run this diff against a known-good brief:

```bash
ssh openclaw@<vps-host>
cd /home/openclaw/.openclaw/agents/research-briefs/
diff <(yq eval '. | keys' beta-google.yaml) <(yq eval '. | keys' beta-tiktok.yaml)
```

If keys differ, normalize the new YAMLs to match the existing schema. Common mismatches to look for:
- `mandate` vs `system_prompt` vs `role_prompt`
- `sources.reddit` vs `sources.subreddits`
- `output.daily_brief` vs `output.path`
- `telegram.on_critical` vs `alert.critical`
- `model.name` vs `model.id`

### Step 3. Verify the runner discovers new YAMLs

```bash
grep -n "research-briefs" /home/openclaw/.openclaw/command-center/scripts/agent_research_loop.py
```

Two possibilities:
- **Good:** the script globs `*.yaml` in the briefs dir -> new agents picked up automatically.
- **Bad:** the script has a hardcoded list `['beta-google', 'beta-meta', 'beta-insta']` -> needs a patch to glob the directory.

If hardcoded, patch the loader to:

```python
brief_files = sorted(Path("/home/openclaw/.openclaw/agents/research-briefs/").glob("*.yaml"))
```

### Step 4. Smoke-test one agent manually

```bash
cd /home/openclaw/.openclaw/command-center/scripts/
python3 agent_research_loop.py --agent beta-tiktok --dry-run
```

Confirm:
- It reads the YAML
- It pulls all listed sources
- It writes to `/home/openclaw/.openclaw/vault/brands/aydins/research/beta-tiktok/{YYYY-MM-DD}.md`
- No Telegram fires unless something is CRITICAL

### Step 5. Confirm cron is unchanged

The existing entry:

```
0 9 * * * /usr/bin/python3 /home/openclaw/.openclaw/command-center/scripts/agent_research_loop.py
```

If the script loops over all YAMLs internally, no cron change needed.

### Step 6. Full run + verify outputs

Wait for the 4am CT run (9:00 UTC during CDT), then check:

```bash
ls -la /home/openclaw/.openclaw/vault/brands/aydins/research/beta-tiktok/
ls -la /home/openclaw/.openclaw/vault/brands/aydins/research/beta-klaviyo/
ls -la /home/openclaw/.openclaw/vault/brands/aydins/research/beta-shop/
ls -la /home/openclaw/.openclaw/vault/brands/aydins/research/beta-etsy/
ls -la /home/openclaw/.openclaw/vault/brands/aydins/research/beta-ebay/
ls -la /home/openclaw/.openclaw/vault/brands/aydins/research/beta-design/
```

All six should have a `2026-06-09.md` file (or next-day date).

---

## Alternative: BETA hand-off prompt

If Amir wants BETA to deploy end-to-end instead of running scp himself, this is the prompt to paste:

> BETA, deploy 6 new agent research briefs.
>
> Source: the 6 YAMLs in the vault at `03 Projects/Aydins Jewelry/06 System/research-briefs-staging/`. Names: beta-tiktok, beta-klaviyo, beta-shop, beta-etsy, beta-ebay, beta-design.
>
> Steps:
> 1. Pull the 6 YAMLs from the vault (vault-sync or direct read).
> 2. Compare schema against the existing `/home/openclaw/.openclaw/agents/research-briefs/beta-google.yaml`. Normalize key names if mine differ. Preserve my source lists, focus areas, and critical signals as-is.
> 3. Copy the normalized YAMLs into `/home/openclaw/.openclaw/agents/research-briefs/`.
> 4. Inspect `/home/openclaw/.openclaw/command-center/scripts/agent_research_loop.py`. If the agent list is hardcoded, patch it to glob `*.yaml` in the briefs dir. Snapshot the script before mutation.
> 5. Run a dry-run smoke test for `beta-tiktok` and `beta-design`. Confirm sources resolve and output paths get created.
> 6. Post a deploy receipt to Telegram (or Slack #beta-daily) with: file names copied, schema deltas applied, script patch yes/no, smoke-test pass/fail, expected next-run timestamp.
> 7. Snapshot to: `/home/openclaw/.openclaw/command-center/work/research-loop/deploy-2026-06-08.md`.
>
> Do NOT change beta-google, beta-meta, beta-insta. Do NOT change the cron schedule. Do NOT change the OpenRouter model.

---

## What "CRITICAL" looks like per agent

Quick reference for Amir to know what to expect in Telegram alerts once these are live.

| Agent | A CRITICAL alert would say |
|---|---|
| **beta-tiktok** | "TikTok Shop fee changed Aug 1" or "TikTok algorithm now demotes watermarked reposts" |
| **beta-klaviyo** | "Gmail tightening sender requirements Oct 1, action needed" or "Klaviyo deprecating flow type X" |
| **beta-shop** | "Shopify Checkout extensibility deadline moved" or "App you use (Zepto) being sunset" |
| **beta-etsy** | "Etsy raising transaction fee 4.5% -> 5%" or "Free shipping guarantee threshold dropping" |
| **beta-ebay** | "eBay final value fee on jewelry going up" or "Best Match weighting shifted to image quality" |
| **beta-design** | "New image gen model beats Gemini on product fidelity at half the cost" or "Veo 3 dropped to $0.15/sec" |

---

## Rollback

Each YAML is its own file. To kill any single agent:

```bash
mv /home/openclaw/.openclaw/agents/research-briefs/beta-<name>.yaml \
   /home/openclaw/.openclaw/agents/research-briefs/.disabled/
```

Or to revert the script patch (if applied):

```bash
ls /home/openclaw/.openclaw/command-center/scripts/snapshots/agent_research_loop/
# pick the timestamp before today's deploy and restore
```

---

## Why these 6, why this design

- **beta-tiktok** and **beta-klaviyo**: high-priority because TikTok and email are active growth lanes with fast-moving platform changes.
- **beta-shop**: Aydins is mid-migration to v5 (Kalles OS2.0). A breaking Shopify change while migrating is the worst kind of surprise.
- **beta-etsy**: Amir is actively pushing Etsy. Fee changes hit margin directly.
- **beta-ebay**: Aydins sells on eBay too. Lower volume, but a Best Match shift could double or kill it.
- **beta-design**: Redefined as AI tools scout. The AI tool landscape changes faster than any other channel. Missing a 10x tool (or a 50% price cut) for a month is a real cost.

Total cost: ~$0.90/day for full coverage across every channel Aydins runs.
