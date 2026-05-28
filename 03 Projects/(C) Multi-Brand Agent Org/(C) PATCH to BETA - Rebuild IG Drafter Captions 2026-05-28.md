---
to: BETA
from: Amir
date: 2026-05-28
priority: HIGH
type: rebuild IG drafter caption generator - quality fix
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/Rebuild_IG_Drafter_Captions_2026-05-28.md
---

# PATCH: Rebuild IG drafter caption generator

## Problem

The phase2_daily_drafter.py built earlier today produces captions that all use the same template:

> "[CODENAME] is not a basic wedding band. This ring brings [features] into a clean, masculine profile with detail that stands out up close. It is the kind of band that feels personal without trying too hard. Built for daily wear and finished for comfort, it gives him a ring with weight, character, and a story. Find your band at Aydins."

Amir saw all 4 drafts (CARPATHIAN, VALENTE, EASTWOOD, KADEN) and called it out as repetitive AI slop. Same opener, same close, identical middle structure with only the codename and feature list swapped. Audience pattern-recognizes this within 2-3 posts and disengages.

The 4 drafts have been demoted from `approved-queued` to `drafted-needs-improvement`. Publisher will skip them. ABYSS at 13:00 CT today still fires (its caption is high-quality, written by BETA last night).

## Quality bar

Match the original 3 sample captions (IMPRINT, Educational, ABYSS) from 2026-05-27. Distinct openers:

- IMPRINT: "A wedding band should feel personal."
- Educational widths: "Ring width changes the whole feel."
- ABYSS: "Dark metal. Real texture. No basic band energy."

Each opener uses a different rhetorical mode. None repeat.

## Required changes to phase2_daily_drafter.py

### 1. Use V4 Flash model

The OpenClaw allowlist was updated today to include `openrouter/deepseek/deepseek-v4-flash`. Use V4 Flash for caption generation. It's 60% cheaper than V3.2 and has 1M context for longer prompt examples.

### 2. Replace the template generator with a variety-enforced prompt

Change the prompt sent to the LLM to:

- Explicitly forbid repeating phrases used in the last 7 days of captions
- Provide a rotating set of opener archetypes (sentence, question, fragment, stat, observation, etc.)
- Provide a rotating set of close archetypes
- Always pull voice from `brands/aydins/profile.md` (already on disk)
- Reference the IMPRINT, Educational, ABYSS captions as quality examples

Suggested prompt skeleton (Python string):

```python
RECENT_OPENERS_LOOKBACK_DAYS = 7
OPENER_ARCHETYPES = [
    "declarative_truth",  # "A wedding band should feel personal."
    "punchy_observation",  # "Dark metal. Real texture. No basic band energy."
    "rhetorical_question",  # "What makes a ring his?"
    "sensory_fragment",  # "Brushed black. Blue at the edge. Yours engraved inside."
    "comparison",  # "Tungsten holds up. Wood gives in. Together they tell a story."
    "personal_address",  # "Your hand. Your story. Your ring."
    "story_open",  # "He picked it out on a Tuesday. Wore it every day after."
    "category_truth",  # "Ring width changes the whole feel."
]

CLOSE_ARCHETYPES = [
    "soft_invitation",  # "Make it personal at Aydins."
    "value_anchor",  # "Find the ring with a story at Aydins."
    "action_specific",  # "Engrave the inside. Make it his."
    "category_anchor",  # "Choose your fit at Aydins."
    "brand_signature",  # "Aydins. Wedding bands made personal since 2011."
    "direct_link",  # "Shop the [CODENAME] at shopaydins.com."
]

prompt = f'''You write Instagram captions for Aydins Jewelry, an established men's wedding band brand.

Voice: polished, masculine, high-end, direct, conversion-focused. No buzzwords, no filler. Short mobile-friendly paragraphs. The ring should feel personal, not generic.

Hard rules:
- No em dashes. No bare "lifetime warranty." Use "Aydins Lifetime Warranty" if needed.
- No third-party brand names (Thorsten, Universal Jewelry, JCK, competitors).
- No "handcrafted/handmade/forged" - Aydins engraves and ships, doesn't manufacture.
- Use Irving Texas only when transactional. Flower Mound only in email legal footers.

Caption structure:
1. Opener (1 line) - use this archetype: {selected_opener_archetype}
2. Body (2-4 short paragraphs) - tell a story about THIS specific ring
3. Close (1 short line) - use this archetype: {selected_close_archetype}
4. Then a blank line, then 5-10 hashtags

Forbidden phrases (used in recent posts, do not repeat):
{forbidden_phrases_from_recent_captions}

Forbidden patterns:
- "X is not a basic wedding band" - banned
- "feels personal without trying too hard" - banned
- "Built for daily wear and finished for comfort" - banned
- "Find your band at Aydins" - banned in this exact form

Reference examples of GOOD captions (different ring each, distinct voice):

Example 1 (IMPRINT):
A wedding band should feel personal.

IMPRINT pairs black brushed tungsten with blue step edges and fingerprint engraving for a ring that carries more than a look. It carries a mark that is yours.

Built for daily wear, finished with a comfort fit, and made for the guy who does not want a basic band.

Make it personal at Aydins.

Example 2 (Educational widths):
Ring width changes the whole feel.

A 6mm band usually feels cleaner and easier to wear. An 8mm band gives more presence and a stronger masculine profile. Neither is better. The right choice is the one that fits your hand, your style, and how much you want the ring to stand out.

If you are between widths, start with your daily comfort. The best wedding band is the one you actually want to wear every day.

Choose your fit at Aydins.

Example 3 (ABYSS):
Dark metal. Real texture. No basic band energy.

ABYSS brings a sandblasted tungsten profile together with meteorite fragments for a ring that feels rugged, clean, and different without trying too hard.

It is the kind of detail you notice up close, and the kind of weight that feels right every day.

Find the ring with a story at Aydins.

Now write a caption for THIS ring:
- Codename: {codename}
- Material: {material}
- Inlay/feature: {inlay}
- Width: {width}
- Profile: {profile}
- Color: {color}
- Engraving: {engraving}

Make it sound like a different person wrote it from the example captions above. Vary sentence rhythm. Use specific concrete imagery, not abstract category language. The opener should grab attention immediately.

Output ONLY the caption text (no headers, no commentary). Then on a new line, output a JSON array of 5-10 hashtags.'''
```

### 3. Track recent captions to enforce no-repeat

Maintain a JSON file `brands/aydins/recent-insta-captions.json` storing the last 14 days of caption texts + openers + closes used. Before generating a new draft:

- Read the file
- Extract the last 30 caption openers (first 80 chars)
- Add to the `forbidden_phrases_from_recent_captions` list in the prompt
- Extract the last 30 closes (last 50 chars)
- Add to forbidden list

After generating, append the new caption to the file. Trim to last 14 days on each write.

### 4. Vary opener and close archetype selection

Use a deterministic rotating cycle based on day-of-year + slot time so consecutive posts get different archetypes. Or random with no-repeat enforcement vs last 5 posts. Either works.

### 5. Add a quality self-check after generation

After the LLM returns a caption, run a self-check before saving:

- Does it contain any phrase from the forbidden list? Reject and re-generate (max 2 retries).
- Is the opener identical or near-identical (Levenshtein >0.7 similarity) to any opener in the last 14 days? Reject and re-generate.
- Does the close repeat from recent posts? Reject and re-generate.
- Length: caption between 150 and 800 chars. Hashtags 5-10 count.
- Standard BETA Check (em dashes, banned phrases, voice rules) - already in place, keep.

If all 3 retries fail validation: log to `tasks/needs-amir-review.json` and skip this slot. Do not push a bad draft.

### 6. After rebuild, re-draft the 4 paused slots

Once the new drafter is in place:

- Read calendar, find all `drafted-needs-improvement` status slots
- Re-generate drafts for each using the new prompt
- BETA Check
- If pass: move status back to `approved-queued`
- Publisher cron picks them up at their scheduled times

The 4 slots to re-draft:
- `2026-05-28-1900-ct` (TONIGHT - re-draft within next 5 hours so 7 PM CT can fire)
- `2026-05-29-0800-ct`
- `2026-05-29-1300-ct`
- `2026-05-29-1900-ct`

If for any reason CARPATHIAN/VALENTE/EASTWOOD/KADEN are not the actual codenames Aydins uses for the SKUs you picked, re-pick SKUs with verified codenames from the catalog. Do not fabricate codenames.

## Verification protocol

Report back with:

1. Updated phase2_daily_drafter.py md5
2. Path to recent-insta-captions.json after first write
3. 4 re-drafted captions (paste each in full)
4. BETA Check verdict on each
5. Calendar status after re-draft (4 slots back to approved-queued)
6. Confirmation tonight 19:00 CT will fire with the new caption
7. Total Gemini cost for re-draft (should be near $0 if image is reused; new image gen if needed)
8. Total V4 Flash token cost for the new captions

Post receipts to Slack `#beta-daily` with a clear "DRAFTER REBUILT" header so Amir can spot it. Keep response under 600 words.

## Constraints

- Stay within $5/day Gemini cap (likely re-using existing images for the 4 paused slots, so near $0)
- V4 Flash for captions (newly added to allowlist, much cheaper than V3.2)
- No em dashes anywhere
- No bare "lifetime warranty"
- All other brand voice rules from brands/aydins/profile.md
- ABYSS at 13:00 CT today is approved and will publish - do not touch
