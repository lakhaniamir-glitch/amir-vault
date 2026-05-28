---
status: draft-ready
created: 2026-05-13
for: "[[(C) Ring Care Guide — Shopify Page Content]]"
tool: Gemini (Imagen / Nano Banana — image generation)
output_format: JPG, sRGB, web-optimized
---

# Ring Care Guide — Gemini Image Prompts

## Brand visual reference (use this for EVERY image)

All four images must read as one consistent shoot — the same Aydins V5 aesthetic, the same workbench, the same lighting. Lock these style anchors before generating:

**Palette (must appear in every frame):**
- Warm bone / cream background tones (#FAF8F4 / #F2EBDC)
- Brass accent (#B08D57) — through wood grain, brass lamp light, or a brass tool
- Charcoal / ink shadow detail (#1A1A1A)
- Avoid: cool blue tones, pure white, gray studio backdrops, neon

**Mood:**
- Editorial menswear / quiet luxury — think *Hodinkee* shot in a leather workshop, not Pinterest "ring photography"
- Natural window light from a single direction (left or upper-left), soft shadow
- A real workspace, not a sterile studio. Linen cloth, walnut wood, leather, oxidized brass — visible.
- Masculine, calm, considered. No glitter, no rose petals, no marble slabs, no diamonds-on-velvet vibe.

**Subject hygiene:**
- The rings should be **men's tungsten / ceramic / wood-inlay style bands** — wide profile (6–8mm), brushed or polished finish, dark or natural-wood inlay. NOT engagement rings. NOT thin gold bands.
- If a hand appears, hand is masculine, weathered, clean nails, no rings other than the subject ring, no watch in the same frame.
- No text, no logos, no brand names visible.

**Composition rules:**
- Center-weighted with breathing room on edges (Shopify will crop edges on different breakpoints)
- Shoot wide enough that crops to 16:9, 4:3, and 1:1 all work
- Subject sits in the upper-left or center-third — leave room for headline overlay on the hero

**Image specs (for all four):**
- Output at 2400px on the long edge minimum
- JPG, 80% quality, sRGB
- File names: kebab-case, descriptive (see each section)

---

## Image 1 — Hero (TOP PRIORITY)

**Location in HTML:** Line 237 of the Ring Care Guide HTML
**Current placeholder:** `Return_Exchange_image.jpg`
**Replace with:** `ring-care-hero.jpg`
**Aspect ratio:** 4:3 or 3:2 (web hero, side-by-side with text)
**Crop tolerance:** must survive being cropped to a tall 2:3 on mobile

### Gemini prompt — copy/paste

```
Editorial menswear product photograph for a fine jewelry care guide.

Subject: a single wide men's wedding band — brushed tungsten with a thin natural koa-wood inlay running through the center — resting on a natural linen cloth that sits on a walnut workbench. Beside the ring, slightly out of focus in the background, is a small ceramic dish holding a soft-bristle toothbrush and a folded microfiber polishing cloth in cream.

Lighting: soft natural window light coming from the upper left, golden hour warmth, gentle shadow falling to the lower right. Single light source, no fill flash, no studio softbox.

Color palette: warm bone and cream tones dominate, walnut wood grain in deep brown, the ring shows brushed silver-gray surface with a clear honey-brown wood inlay, a subtle brass tool handle visible at the far right edge for warm accent. Avoid all cool blue, gray, or pure white tones.

Composition: ring sits in the center-left third of the frame. Empty linen space to the right of the ring for headline overlay. Top-down view tilted ten degrees, three-quarter perspective.

Style: editorial, quiet luxury, Hodinkee-meets-craft-workshop. Realistic photography, shallow depth of field on the cleaning supplies, sharp focus on the ring. Looks like the corner of a real workshop in Irving, Texas — not a styled studio.

Aspect ratio: 3:2 horizontal. Resolution: 2400px wide minimum.

No text, no logos, no watermarks, no people, no hands, no jewelry boxes, no diamonds, no other rings, no marble, no velvet, no rose petals.
```

**Why this works:** The toothbrush + cloth telegraph "care guide" without being literal. The wood-inlay ring is your hero SKU style. The linen + walnut + brass anchors the V5 palette and lifts it above generic e-com product photography.

---

## Image 2 — Cleaning Routine (recommended addition)

**Location in HTML:** Inside the `#cleaning` section (around line 285) — add a new `<div class="apg-hero-image">` block or insert above the `.apg-steps` grid.
**File name:** `ring-care-cleaning-routine.jpg`
**Aspect ratio:** 16:9 horizontal banner
**Why add it:** The 30-second routine is your most-shared, most-quoted block — visual makes it screenshot-able. Right now it's three text steps with no image.

### Gemini prompt — copy/paste

```
Editorial overhead flat-lay photograph for a men's ring cleaning routine.

Subject: arranged on a piece of natural cream linen cloth, three objects in a loose triangle composition — (1) a wide brushed tungsten ring with a thin walnut wood inlay, (2) a small soft-bristle toothbrush with a bone-colored handle resting at a slight angle, (3) a small white ceramic dish containing a single bead of soapy water with one or two visible bubbles. To the side, a folded square of cream microfiber cloth.

Background: the linen sits on a walnut workbench surface, visible at the edges of the frame for warmth. A small brass cup or bowl is half-cropped at the top right for accent color.

Lighting: soft natural window light from upper left, warm tone, soft shadows. Single light source.

Color palette: cream linen dominates, walnut brown at the edges, brass accent top right, ring shows brushed silver-gray with honey wood inlay. Warm, calm, editorial.

Composition: dead-overhead flat-lay perspective. Objects arranged with negative space between them — not crowded. Center weighting.

Style: editorial menswear, quiet luxury, real workshop feel. Realistic photography, full focus across all objects.

Aspect ratio: 16:9 horizontal. Resolution: 2400px wide minimum.

No text, no logos, no people, no hands, no jewelry boxes, no diamonds, no other rings, no marble, no foam piles, no excessive suds, no plastic items, no toothpaste tubes.
```

---

## Image 3 — Material Lineup (recommended addition)

**Location in HTML:** Inside the "Material-specific care" section (around line 309) — insert above the `.apg-faq-list` block, or replace the eyebrow row.
**File name:** `ring-care-material-lineup.jpg`
**Aspect ratio:** 21:9 wide banner OR 4:3 horizontal
**Why add it:** Shows the range visually in one frame. Helps the reader self-identify their material before reading the section.

### Gemini prompt — copy/paste

```
Editorial product photograph for a men's wedding ring materials comparison.

Subject: four men's wedding bands arranged in a clean horizontal row on a neutral cream-linen surface, evenly spaced with breathing room between each ring. From left to right:
(1) a brushed tungsten band, wide profile, silver-gray finish
(2) a polished black ceramic band, glossy obsidian-black finish
(3) a brushed tungsten band with a natural koa-wood inlay running through the center, honey-brown wood visible
(4) a brushed titanium band with a thin charcoal-gray stone or lava-rock inlay through the center

All rings are similar width (6 to 8mm), all are men's-style wide bands, all sit upright on their edge so the inlay is visible.

Background: cream linen on walnut wood, visible wood grain at the edges. A subtle brass tool or brass cup half-cropped at the far right for accent color.

Lighting: soft natural window light from upper left, golden hour warmth, soft directional shadows from each ring falling toward lower right. Single light source.

Color palette: cream and bone dominate the surface, deep walnut at edges, brass accent right, rings show their distinct finishes — brushed silver, glossy black, honey wood, charcoal stone. Warm, editorial, no cool blue or pure white.

Composition: rings centered as a row, equal spacing, slight three-quarter perspective rather than full overhead — enough to see the upright profile of each ring.

Style: editorial menswear, quiet luxury, real workshop. Realistic photography, sharp focus across the row.

Aspect ratio: 21:9 cinematic wide OR 4:3 horizontal. Resolution: 2400px wide minimum.

No text, no logos, no people, no hands, no jewelry boxes, no diamonds, no engagement rings, no thin bands, no marble, no velvet.
```

**Note:** If Gemini struggles with four rings in a row (AI sometimes warps multi-object compositions), generate as TWO images — left pair and right pair — and combine in Canva / Figma.

---

## Image 4 — Long-Term Storage (optional, lower priority)

**Location in HTML:** Inside the "Long-term storage" section (around line 378).
**File name:** `ring-care-storage.jpg`
**Aspect ratio:** 4:3 or square 1:1
**Why add it:** Most-skipped section by default. Image gives readers a reason to slow down.

### Gemini prompt — copy/paste

```
Editorial still-life photograph for a men's ring long-term storage section.

Subject: a single wide men's wedding band — brushed tungsten with a natural koa-wood inlay — resting half-inside an open cream-colored leather drawstring pouch on a walnut wood surface. The pouch is soft, slightly worn, drawstring untied and falling naturally. A folded microfiber cloth in bone-cream sits to one side.

Lighting: soft natural window light from upper left, slightly dimmer than direct daylight — late afternoon feel, warm amber tone, soft shadows.

Color palette: cream leather pouch, walnut wood, brushed silver-gray ring with honey-brown wood inlay, optional brass detail at frame edge. Calm, warm, editorial.

Composition: ring and pouch in center-third, three-quarter perspective from slightly above. Breathing room on all sides.

Style: editorial menswear, quiet luxury, real workshop. Realistic photography, shallow depth of field with sharp focus on the ring opening of the pouch.

Aspect ratio: 4:3 horizontal. Resolution: 2400px wide minimum.

No text, no logos, no people, no hands, no jewelry boxes (no hard boxes — soft pouch only), no diamonds, no other rings, no marble, no velvet, no satin lining.
```

---

## Workflow

1. Generate Image 1 (hero) first — that's the must-have to remove the reused `Return_Exchange_image.jpg`.
2. Send me the Gemini output(s).
3. I'll evaluate against the V5 reference (lifetime-sizing-lifetime-warranty page) and tell you which generation to keep, or what to adjust in the prompt and re-roll.
4. Repeat for Images 2, 3, 4 in order.
5. Once approved, upload to Shopify Files. Get the CDN URL (`https://shopaydins.com/cdn/shop/files/{filename}.jpg`).
6. I'll update the Ring Care Guide HTML with the new URLs and the appropriate `alt` text per image.

---

## Prompt-tuning notes (if Gemini misses)

- **If too "studio sterile":** add "in a real working leather and wood craft workshop, slight imperfection visible, lived-in"
- **If too dark / moody:** swap "golden hour" for "late morning natural light, bright but soft"
- **If wrong ring style:** be more specific — "men's wedding band, 7mm width, flat profile, comfort fit interior, contemporary masculine design"
- **If wrong inlay (Gemini sometimes does abalone / mother of pearl by default):** specify exact material — "natural untreated koa wood inlay" or "matte charcoal lava rock inlay" or "do not use abalone, opal, or pearl"
- **If color drift to cool tones:** add "warm color grading throughout, no cool blue cast, no neutral gray, no pure white background"
- **If text or logos appear:** Gemini's habit — re-roll, and add to negative prompt: "no embossed text on ring, no engraved letters visible, no brand stamps, no hallmarks"

---

## Related image needs (outside this page)

While we're here — there's a related image task pending from the Recart V5 Voice Rebuild spec:

- **Recart Welcome MMS Msg 3 badge image** — a V5-styled trust badge graphic for the welcome flow. Different deliverable (it's a graphic, not a photograph), different prompt. Flag if you want me to draft that prompt separately.

---

## Alt text drafts (use these once images are live)

| File | Alt text |
|---|---|
| `ring-care-hero.jpg` | Aydins Jewelry men's tungsten ring with wood inlay on a workshop bench beside a soft toothbrush and polishing cloth |
| `ring-care-cleaning-routine.jpg` | Overhead flat-lay of the Aydins Jewelry weekly ring cleaning routine — ring, soft toothbrush, and microfiber cloth on linen |
| `ring-care-material-lineup.jpg` | Aydins Jewelry men's ring material lineup — tungsten, ceramic, wood inlay, and stone inlay bands side by side |
| `ring-care-storage.jpg` | Aydins Jewelry men's tungsten and wood ring resting in a soft cream leather drawstring pouch |
