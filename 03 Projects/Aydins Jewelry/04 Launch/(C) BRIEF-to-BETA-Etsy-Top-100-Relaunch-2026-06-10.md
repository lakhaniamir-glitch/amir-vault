# BRIEF to BETA — Etsy Top 100 Relaunch

**Date:** 2026-06-10
**Owner:** Amir
**Orchestrator:** beta
**Specialists:** beta-shop, beta-etsy, beta-design, beta-check
**Mode:** draft + audit until Amir's explicit go-ahead per batch
**Priority:** HIGH (only Etsy catalog going forward)

---

## Strategic Context

Amir is collapsing Aydins's Etsy catalog from **502 mostly-dead listings → exactly 100 fine-tuned, revenue-proven listings**. The current Etsy traffic dropped from ~1,200 sessions/mo (Jan) to ~200/mo (Jun). Quality over quantity is the play.

**The 100 = 24 keepers (already on Etsy, in top 100 Shopify revenue) + 76 new (top by sessions, not yet on Etsy).**

Every listing must be:
- Materially accurate (no fabrication of metal, color, feature, width)
- eRank-keyword optimized (use validated keyword stack)
- Conform to Aydins voice + locked rules (no em dashes, no "lifetime warranty" lie, no third-party brand names)
- Photographed with a Shopify reference image and an AI lifestyle hero

---

## What's been done so far (claudian's pass)

Working files in `C:\Users\amirl\Downloads\`:

| File | What it is |
|---|---|
| `etsy-keep-list.csv` | 24 Etsy LIDs in top 100 Shopify revenue (the keepers) |
| `top100-by-sessions-verified.csv` | Top 100 active Shopify rings by 90-day sessions, with handles + URLs |
| `etsy-to-shopify-xref-v4.json` | 376 Etsy LIDs mapped to Shopify codenames (for keeper updates) |
| `aydinsjewelry.myshopify.com (2).csv` | Full Shopify export, 45,584 rows, 1,915 codenames |
| `AydinsJewelry_Etsy_502_2026-06-10_00_31_06.csv` | Most recent Etsy export from Vela |
| `image-inventory-top-100.csv` | Per-codename: HAVE / NEED image |
| `vela-update-24-keepers-FINAL.csv` | DRAFT — needs research-grade refinement per ring |
| `24-keepers-FINAL-research.md` | First-pass research; needs verification per ring |
| `validation-report.md` | Documents previous formula errors (53 color mismatches before override pass) |

Reference docs:
- `etsy/2026-06-04-revision/(C) Etsy Champion Playbook — 2026-06-04.md` — eRank title formula + 13-tag stack
- `etsy/erank-2026-06-04/` — raw eRank keyword CSVs (5 keyword tool exports + competitor tags)
- `brands/aydins/etsy-exports/2026-06-04/listings-to-deactivate-in-vela.txt` — 51 discontinued LIDs
- `brands/aydins/etsy-exports/2026-06-04/scrapped-listings-2026-06-08.md` — discontinued rationale
- `03 Projects/Aydins Jewelry/CLAUDE.md` — Aydins policy + locked rules

---

## Scope correction (2026-06-10 evening — Amir's directive + Etsy revenue data added)

**Final catalog = 150 listings.** Amir provided 2026 YTD Etsy Shop Stats showing per-listing revenue. 38 unique LIDs have confirmed $11,052 YTD Etsy revenue (averaging $290 per listing). Amir's standing rule: **never drop a listing that has Etsy revenue, even small.**

## Image standard: 4 images per Etsy listing (LOCKED)

Standard pattern matches existing set at `brands/aydins/etsy-exports/2026-06-04/images/{handle}/`:
- `hero.jpg` (2048×2048 lifestyle hero, uses Shopify reference)
- `image-2.jpg` (alt angle or scene variation)
- `image-3.jpg` (alt angle or scene variation)
- `image-4.jpg` (alt angle or scene variation)

Amir's directive: every listing must follow this 4-image standard for visual consistency across the store.

| Group | Count | Images already done | Images to generate |
|---|---|---|---|
| Existing keepers — confirmed 2026 Etsy revenue | 38 | varies (few overlap) | ~144 |
| Existing keepers — Shopify top 100 | 24 | varies | ~80 |
| Tier A new — proven on Shopify | 42 | ~33 listings complete (4 each) | ~60 |
| Tier B new — sessions ranked | 46 | 0 | 184 |
| **TOTAL** | **150** | **33 listings × 4 = 132 done** | **~468 new images** |

The precise count from the inventory script:
- **33 of 150 listings have complete 4-image sets ready** (in `etsy-exports/2026-06-04/images/`)
- **117 of 150 listings need image generation** (4 images each = **468 new images**)

Source: `image-inventory-150-4per.csv` lists each LID + codename + image_status + images_to_generate count.

## ⚠️ RESCUED FROM PRIOR DELETION LIST

These 4 LIDs were on the earlier "scrapped/discontinued" list but have confirmed 2026 Etsy revenue. **MUST KEEP. Do NOT deactivate.**

| LID | YTD Revenue | Title |
|---|---|---|
| 509712178 | $1,364 | Personalized Fingerprint Dog Tag w/ Two Name |
| 1219745003 | $305 | CLEMATIS Tungsten Ring Purple Inside |
| 556753279 | $292 | Black & Gray Lava Rock Stone Inlay Ceramic |
| 556548493 | $261 | Black Ceramic Purple Goldstone Inlay |

Source data:
- `final-etsy-keep-list-UNIFIED.csv` — **single source of truth** for the 150
- `final-etsy-catalog-summary.md` — readable report
- `etsy-revenue-2026-ytd.csv` — raw revenue data with matched LIDs
- `top100-final-tiered.csv` — Tier A + Tier B Shopify products
- `image-inventory-top-100.csv` — per-codename HAVE/NEED image status

## Follow-up validation task (beta-etsy)

The 38 revenue LIDs came from screenshots of Amir's Etsy Shop Stats (10 pages shown). If there are MORE pages with smaller-revenue listings, pull them all and add to the keep list. Each $ counts — never drop one. Surface count + revenue total before adding to confirm.

## Deliverables (4 batches, each gates on Amir approval before next)

### Batch 1 — 24 keepers (already on Etsy, simplest verification)
- **beta-shop**: Per-ring verification against actual Shopify URL. Confirm material, base color (NOT accent), feature, widths, sizes, price. No invented data.
- **beta-etsy**: Build a per-ring listing draft using:
  - eRank title formula: `{Material} Wedding Band for Men, {Width} {Color} Mens {Material} Ring {Feature}, Personalized Engraved Ring, Comfort Fit` (140 char cap)
  - 13-tag stack per material (Tungsten / Ceramic / Damascus Steel / Titanium / 14k Gold variants)
  - Aydins-voice description with eRank hook + Key Features bullets + Personalization + Shipping
  - Photo URL slots populated from Shopify featured_image + additional_image_url_1-5
- **beta-design**: For the 20 keepers without an AI lifestyle image (24 keepers minus 4 already in Tier A), generate one each.
  - Reference: existing process at `etsy/2026-06-04-revision/lifestyle-hero-remake-report-2026-06-04.md` (gpt-image-2, 2048×2048 JPEG, scene-appropriate hero)
  - **LOCKED RULE 2026-06-04:** Every image MUST use Shopify reference image as input (no text-only generation for real products). Pull from Shopify featured_image_url for each codename.
- **beta-check**: QA pass.
  - Verify: title materially accurate per Shopify, no em dashes, no banned phrases, tag length under 20 chars each, max 13 tags
  - Verify: image visually matches Shopify reference for material/color/inlay
  - Verify: description follows Aydins voice + locked policies

**Output:** `batch-1-vela-update-24-keepers-FINAL-v2.csv` ready for Vela import. Image files saved to `etsy/2026-06-10-relaunch/batch-1/images/{codename}/hero.jpg`.

**Gate:** Amir reviews. Approves → push to Etsy via Vela.

### Batch 2 — Tier A (46 non-keeper handles with existing images)
Vela template format (no Listing ID, fully populated for new-listing import). Images already exist in `gemini-full/`.

### Batch 3 — Tier B first half (25 of 50 sessions-ranked, need image gen)

### Batch 4 — Tier B second half (remaining 25, need image gen)

After all 4 batches, plus any additions surfaced by the Etsy Sold Items follow-up task, final Etsy catalog should be 117+ listings, all curated, all materially accurate, all with proper lifestyle images.

---

## Quality gates (beta-check enforces before any batch leaves draft)

| Gate | Pass condition |
|---|---|
| Material correct | Matches Shopify description's first sentence material |
| Base color correct | Pulled from description's first words (the BASE ring), NOT from accent / inside / inlay color in Shopify title |
| Feature accurate | Real product feature only — no invented inlays, gemstones, or finishes |
| Title under 140 chars | Etsy limit |
| Tag count ≤ 13 | Etsy limit |
| Each tag ≤ 20 chars | Etsy limit |
| No em dashes anywhere | Aydins locked rule 2026-05-15 |
| No "lifetime warranty" / "free returns" / "free lifetime resizing" claims | Aydins policy — see `(C) Aydins Policies — Source of Truth.md` |
| No third-party brand names | Aydins white-label policy |
| Image uses Shopify reference input | Locked rule 2026-06-04 |
| Image hero is 2048×2048+ JPEG | Etsy minimum + Aydins standard |

---

## Anti-pattern reminders (claudian's mistakes to avoid)

1. **Do not match by sales-data title prefix to find Shopify codename.** Sales data has stale titles. Match via:
   - Authoritative current Shopify handle (from sessions URL paths), OR
   - Existing Etsy Var SKU's codename (for keepers)
2. **Do not extract color from Shopify product title.** Aydins's Shopify titles often lead with accent / inside color for searchability. Use description body's first sentence.
3. **Do not use distinctive-word overlap matching for new listings.** Generates false positives (fingerprint dog tag → tungsten ring).
4. **Do not invent product features.** If Shopify description doesn't say "Diamond," don't write "Diamond" in the Etsy title.
5. **Do not push partial batches.** Each batch is atomic — all 24 (or 25) verified before any is published.

---

## Out of scope

- Deleting the 478 non-top-100 Etsy listings (Amir does this manually in Vela)
- Etsy Ads strategy (separate brief)
- Pricing changes (use current Shopify price as-is)
- Adding products to Shopify (catalog gaps — separate)

---

## Approval workflow

For each batch:

1. BETA delivers the draft CSV + research MD + image set to:
   `03 Projects/Aydins Jewelry/04 Launch/etsy-top-100-relaunch/batch-{N}/`
2. BETA notifies Amir with a one-page summary report.
3. Amir spot-checks 5 random listings against Shopify URLs.
4. Amir approves → push. Amir rejects → BETA fixes flagged items only.

---

## Start order

Begin **Batch 1 (24 keepers)** immediately. The keepers are already on Etsy so they're the lowest-risk win and Amir can spot-check fastest against rings he already sells.

beta-design and beta-shop work in parallel (image gen alongside research). beta-etsy assembles the CSV after both finish. beta-check audits last.

If any blocker (codename not in Shopify, image generation failure, ambiguous material) — surface to Amir immediately. Do not guess.
