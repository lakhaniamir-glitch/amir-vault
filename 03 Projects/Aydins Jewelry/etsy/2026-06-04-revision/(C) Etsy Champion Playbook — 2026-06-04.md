# (C) Etsy Champion Playbook — 2026-06-04

> Built from eRank data analysis (6 CSVs: 1 competitor sales, 1 competitor tags, 5 keyword tools across the 5 highest-intent tungsten queries).
> Source data: `etsy/erank-2026-06-04/`

---

## The Brutal Reality (where Aydins stands today)

| Shop | Listings | 30D Sales | Sales / Listing / Month | Shop Age |
|---|---|---|---|---|
| **BrielleShoppe** | 108 | 395 | **3.66** | 10yr 9mth |
| LuxuriaJewelers | 412 | 416 | 1.01 | 10yr 2mth |
| LazerBoyzDesigns | 854 | 458 | 0.54 | 8yr 1mth |
| CavalierJewelers | 264 | 189 | 0.72 | 7yr 8mth |
| ModernWeddingRing | 369 | 71 | 0.19 | 9yr 0mth |
| **AydinsJewelry** | **501** | **12** | **0.024** | 9yr 11mth |
| VeilJewelers | 308 | 160 | 0.52 | 5yr 5mth |

- AydinsJewelry is doing **150x less sales per listing** than BrielleShoppe at nearly the same shop age.
- This is NOT a shop-age or volume problem. It's a **findability + conversion** problem.
- BrielleShoppe is the role model: tight catalog (108 listings), efficient throughput (3.66 sales per listing per month).

**Diagnosis:** Aydins has 501 listings, most with weak titles, suboptimal tag stacks, generic descriptions, and inconsistent images. Etsy's algorithm rewards CTR and conversion, and Aydins is losing both.

---

## The Title Formula (data-backed)

Front-load the highest-volume keyword phrase. Then color + width. Then secondary keyword. Always close with `Comfort Fit` (Aydins differentiator, present in eRank tag data).

```
Tungsten Wedding Band for Men, {WIDTH}mm {COLOR} Mens Wedding Ring {FEATURE}, Personalized Engraved Ring, Comfort Fit
```

**Why this works:**

| Phrase | Avg Monthly Searches |
|---|---|
| mens wedding band | 7,638 |
| wedding band | 6,328 |
| mens wedding ring | 2,466 |
| tungsten ring | 2,161 |
| tungsten ring men | 798 |
| black tungsten ring | 437 |
| mens tungsten wedding band | 495 |

Cap at 140 chars. Drop the "Personalized Engraved Ring" portion if needed.

---

## The Universal 13-Tag Stack

Every men's tungsten listing uses these 11 base tags + 2 swappable slots:

```
1.  tungsten ring          (13 chars, 82 competing shops, 3,700 searches)
2.  mens wedding band      (17, 72 shops, 2,095 searches)
3.  mens wedding ring      (17, 75 shops, 2,095 searches)
4.  mens tungsten ring     (18, 79 shops, 110 searches)
5.  mens tungsten band     (18, 79 shops)
6.  personalized ring      (17, 25 shops, 4,630 searches)
7.  engraved ring          (13, 9 shops only, 7,461 searches) ← BIGGEST UNDERUSED OPPORTUNITY
8.  tungsten band          (13, 78 shops, 50 searches)
9.  mens ring              (9, 9 shops, 35,075 searches)
10. wedding band men       (16, 1,985 searches)
11. comfort fit ring       (16, Aydins differentiator)
12. {color} tungsten ring  ← swap by color (black, blue, rose gold, silver, gold)
13. {width}mm wedding band ← swap by width (8mm, 6mm, etc.) OR {feature} tag (meteorite, hammered, etc.)
```

**Key insight:** `engraved ring` has 7,461 average searches per month but only 9 of 27 audited shops use it. That's a huge gap. Aydins should be on it given engraving is the core service.

---

## The Description Hook (first 160 chars matter most)

This is the Etsy preview snippet AND the Google search-result description. Front-load product type + key trust signals.

**Approved hook (matches Aydins policy, no fabricated claims):**

```
Tungsten wedding band for men, engraved and shipped from our Irving, Texas workshop. 
Free engraving, free 2-day FedEx, lifetime sizing. Comfort fit.
```

145 chars. No em dashes. No bare "lifetime warranty." No "free returns." No third-party brands. Compliant with [[(C) Aydins Policies — Source of Truth]].

Body of description below the hook follows the same structure across all 501 listings: Key Features, Personalization, Shipping, Returns & Exchanges, About Aydins. Standardization helps Etsy's algorithm understand the catalog.

---

## Photo Standard

**Hero (image 1):**
- 2048x2048+ square (Etsy minimum 2000x2000)
- Pure white seamless background
- Single ring, 3/4 angle showing top face + inner band
- Soft drop shadow underneath
- No text overlays, no logos, no hands, no models

**Lifestyle 1 (image 2):**
- Masculine context: workshop, leather, mountains, coffee shop
- Subtle motion / depth of field
- 2048x2048 square

**Lifestyle 2 (image 3):**
- Different context from Lifestyle 1
- Hand or wear-shot OK (subtle wedding moment, holding partner's hand, on guitar)
- 2048x2048 square

**Why white-background heroes matter:** Etsy search-result grid shows thumbnails next to competitor heroes. White background hero with single sharp ring out-clicks lifestyle-heavy thumbnails. BrielleShoppe and LuxuriaJewelers both use this convention.

---

## Pricing

Phase 1 of the 2026-06-04 work matched 9 of 501 Etsy listings to top-50 Shopify products and set Etsy price to exact Shopify price. The other 492 need a full pricing parity pass (running now via Beta-Shop).

**Rule:** Etsy price = current shopaydins.com listed price. Exact match. No Etsy premium. No Etsy discount.

---

## Channel-Specific Constraints

- **Title:** 140 char hard ceiling (Etsy truncates)
- **Tags:** 13 max, 20 char max each, no special characters
- **Description:** No length cap but front-load the 160-char hook
- **Photos:** Minimum 5 per listing. Recommended 7-10. Square 2000x2000+
- **Video:** Optional but boosts ranking. 5-15 seconds, no audio
- **Materials field:** Use real materials (tungsten carbide, abalone, opal, etc.)
- **Variations:** Width × Size, per Universal Jewelry source-of-truth ranges only

---

## The 30-Day Etsy Sprint (after this revision)

| Week | Move |
|---|---|
| Week 1 | Import revised CSV via Vela. Verify titles + tags applied. Spot-check 30 listings. |
| Week 2 | Generate remaining lifestyle images (2 per top-50 product). Replace photos on top-50 listings. |
| Week 3 | Add a 5-15 sec video to top-25 listings (rebound video processor in `command-center/scripts/etsy_video_rebound_processor.py`). |
| Week 4 | Review Etsy stats (visits, conversion, search-term traffic). Identify top 5 winners + top 5 losers. Iterate winners with new images. Cut or reword losers. |

**30-day success metrics:**
- Visits: 10.6k → 15k+ (40%+ lift)
- Orders: 12 → 25+ (2x lift minimum)
- CTR per listing: track baseline now, target 2%+ per impression
- Conversion: 0.8% → 1.5%+

---

## Why eRank Beats Etsy Scraping

The original plan was to scrape Etsy SERPs. eRank gives:
- Pre-computed search volume + click data per keyword (Etsy doesn't publish this)
- Competitor tag occurrence counts (you'd need to scrape and parse hundreds of listings)
- Real sales velocity per competitor (impossible to estimate from SERP)
- Keyword difficulty (KD) scores (Etsy doesn't publish this)

**Lesson for next time:** always check if a SaaS tool has the data before scraping.

---

## Output Files (2026-06-04 work)

| File | Purpose |
|---|---|
| `etsy/2026-06-04-revision/listings-revised.csv` | Final 501-listing CSV. Import via Vela. |
| `etsy/2026-06-04-revision/revision-report.md` | Per-listing change log + compliance audit |
| `etsy/2026-06-04-revision/hero-images-existing/` | 10 hero images already generated |
| `etsy/2026-06-04-revision/(C) Etsy Champion Playbook — 2026-06-04.md` | This doc |

Files on VPS (full set):
- `/home/openclaw/.openclaw/vault/brands/aydins/etsy-exports/2026-06-04/listings-revised.csv`
- `/home/openclaw/.openclaw/vault/brands/aydins/etsy-exports/2026-06-04/pricing-audit-2026-06-04.csv` (when Beta-Shop finishes)
- `/home/openclaw/.openclaw/vault/brands/aydins/etsy-exports/2026-06-04/images/{handle}/hero.jpg` (40 more pending)
- `/home/openclaw/.openclaw/vault/brands/aydins/etsy-exports/2026-06-04/video-prep-2026-06-04.csv`

---

## Next Action for Amir

1. **Review this playbook.** Five-minute read.
2. **Spot-check 5 revised listings** in `listings-revised.csv` to QC title + tag + description.
3. **Decide on hero-image quality** after Phase 2A heroes finish generating.
4. **Approve pricing-audit changes** when Beta-Shop pricing pass completes.
5. **Import the final CSV via Vela** once all 4 above pass QC.
6. **Run the 30-day Etsy sprint** above.
