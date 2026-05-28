---
to: BETA
from: Amir
date: 2026-05-28
priority: HIGH
type: drafter visual composition variety patch
server-path: /home/openclaw/.openclaw/agents/beta/handoffs/IG_Image_Composition_Variety_2026-05-28.md
---

# PATCH: Add visual composition variety to IG drafter

## Problem

All 5 currently queued IG images are flat-lay (top-down product still life on a surface). Gemini image-edit preserves source product photo orientation; source photos on Shopify are all flat-lay; result is 5/5 same composition.

Amir flagged: monotonous on IG grid. Want visual variety in angles, framing, and contextual placement.

## Fix

### 1. Replace the limited "scene options" in phase2_daily_drafter.py with 15 distinct compositions

Replace whatever the current scene list is with this 15-composition pool:

```python
COMPOSITION_OPTIONS = [
    # Surface flat-lay variants
    {"id": "flat_dark_wood", "prompt": "Place the ring flat on a dark walnut wood surface with subtle grain, top-down composition, warm side lighting, shallow depth of field."},
    {"id": "flat_dark_leather", "prompt": "Place the ring flat on aged dark brown leather with visible grain, top-down composition, warm rim lighting from one side."},
    {"id": "flat_dark_stone", "prompt": "Place the ring flat on dark slate stone with subtle texture, top-down composition, single warm overhead spotlight."},
    # Angled / profile variants
    {"id": "tilted_45_wood", "prompt": "Position the ring tilted at a 45-degree angle on warm walnut wood so the ring profile and inside band are partly visible, side lighting, editorial macro style."},
    {"id": "profile_standing", "prompt": "Position the ring standing on its edge on a dark wood surface, showing the full ring profile in side view, soft directional light from upper left."},
    {"id": "leaning_canvas", "prompt": "Lean the ring at an angle against a piece of textured natural canvas or denim on a dark surface, showing the profile partially, warm side lighting."},
    # Macro detail variants
    {"id": "macro_inlay", "prompt": "Extreme macro close-up of the ring focused on the inlay or feature detail, shallow depth of field, rest of ring slightly out of focus, dark background, warm lighting."},
    {"id": "macro_texture", "prompt": "Extreme macro close-up on the ring surface texture and finish detail, top-down angle, dark background, soft directional light revealing surface character."},
    # Contextual / lifestyle (still no full hand or face)
    {"id": "ring_box", "prompt": "Position the ring inside an open dark wooden jewelry box with cream interior, the box partially in shadow, warm overhead spotlight on the ring."},
    {"id": "leather_books", "prompt": "Place the ring on top of a small stack of vintage leather-bound books with brass corners, dark library atmosphere, warm directional light."},
    {"id": "brass_surface", "prompt": "Place the ring on a polished antique brass surface with soft reflections, side lighting picking up both metal and ring detail, editorial macro."},
    {"id": "slate_water", "prompt": "Place the ring on dark natural slate with a few water droplets nearby reflecting warm light, top-down composition with shallow depth of field."},
    {"id": "linen_brass", "prompt": "Place the ring on cream natural linen fabric with brass accent props (antique key or fountain pen) just out of focus in background, warm light."},
    # Held / vertical variants
    {"id": "held_fingertips", "prompt": "Show only the ring held vertically between a thumb and forefinger (no full hand or face visible), dark out-of-focus background, warm lighting, editorial portrait of the ring."},
    {"id": "single_finger", "prompt": "Close-up of a single masculine finger from knuckle to fingertip wearing the ring (no full hand, no face, no skin tone identifiable), dark background, warm directional light, focus on the ring."},
]
```

### 2. Add composition tracking + no-repeat enforcement

Maintain `brands/aydins/recent-insta-compositions.json` with last 14 days of composition IDs used.

When picking a composition for a new draft:

```python
# Read last 14 days of composition IDs from recent-insta-compositions.json
recent_ids = load_recent_composition_ids()
# Filter out any used in last 7 days (more aggressive than captions because visual is faster to spot)
available = [c for c in COMPOSITION_OPTIONS if c["id"] not in recent_ids[-7:]]
if not available:
    available = COMPOSITION_OPTIONS  # if all 15 used recently, allow repeats
selected = random.choice(available)  # or weighted by category fit
```

### 3. Append composition_id to draft JSON and track

In each draft JSON, add a `composition_id` field. After generating, append to `recent-insta-compositions.json`.

### 4. Adapt composition selection to caption / category

Some compositions fit better with certain categories:

- **product_showcase**: any composition works; rotate freely
- **bts (behind-the-scenes)**: skip pure product compositions, prefer workshop / process scenes (text-to-image; do NOT use product image as reference)
- **educational**: prefer compositions that show multiple items or comparison angles (e.g. two rings side by side, ring with measuring tools)
- **ugc**: prefer `single_finger` or `held_fingertips` for lifestyle hand context

### 5. Re-generate the 4 paused drafts with new compositions

The 4 paused drafts (status: `drafted-needs-improvement` or `approved-queued` depending on rebuild state):
- `2026-05-28-1900-ct` (CARPATHIAN)
- `2026-05-29-0800-ct` (VALENTE)
- `2026-05-29-1300-ct` (EASTWOOD)
- `2026-05-29-1900-ct` (KADEN)

KEEP THE CAPTIONS as-is (Amir approved them). REPLACE THE IMAGES with newly generated ones using 4 different compositions. Pick 4 distinct composition IDs from the pool, ideally none from the flat-lay surface group since the existing IMPRINT/Educational/ABYSS are all flat-lay.

Suggested distribution for these 4:
- CARPATHIAN: `tilted_45_wood` (shows profile of the diamond + gold + wood combination)
- VALENTE: `macro_inlay` (highlights the red wood inlay against black tungsten)
- EASTWOOD: `leather_books` (whiskey barrel wood pairs with vintage leather context)
- KADEN: `held_fingertips` (vertical hold shows two-tone profile in 3D)

Update each draft JSON with:
- New `image_url` (after Shopify Files upload)
- New `composition_id`
- New `gemini_prompt_used`
- New `gemini_cost_usd`
- Bump `regenerated_at` timestamp

Move each slot back to `approved-queued` status if status changed during pause.

### 6. Cost cap

4 new image generations at $0.04 each = $0.16. Well under $5/day Gemini cap.

## Verification protocol

Report back with:

1. Updated `phase2_daily_drafter.py` md5
2. Path to `recent-insta-compositions.json` with initial 4 entries logged
3. 4 new image Shopify CDN URLs (so Amir can preview)
4. Confirmation each used a DIFFERENT composition_id
5. Confirmation captions are unchanged (still the Amir-approved versions)
6. Final calendar status: all 4 slots `approved-queued` with `draft_path` populated, `image_url` updated
7. Total Gemini cost for this regeneration
8. Confirmation tonight 19:00 CT slot will fire with the new CARPATHIAN image

Keep response under 400 words.

## Constraints

- Captions stay the same (already approved)
- Only images regenerate
- 4 different compositions, no repeats among the 4
- $5/day Gemini cap (this run ~$0.16)
- ABYSS at 13:00 CT today is untouched (already publishing)
- No em dashes in any new prompts to Gemini
- Tracking on/CONTINUE policy on the source products stays as-is
