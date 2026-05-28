# (C) Brief to BETA: Christian Rings Collection

> **Created:** 2026-05-18
> **From:** Amir (via Claude)
> **To:** BETA
> **Priority:** Normal. Not a launch blocker, but needed before the Christian Rings homepage module + any traffic push.

---

## TL;DR

Add 34 listed rings to the **Christian Rings** smart collection on the Aydins Jewelry Shopify store, and finish the collection page to full Aydins standard.

The collection already exists:

- **Name:** Christian Rings
- **GID:** `gid://shopify/Collection/467763036397`
- **Type:** Smart collection
- **Rule:** `tag EQUALS "Christian Rings"` (single condition, auto-join)

If anything in this brief is missing on the live collection, BETA fills it.

---

## Step 1: Tag audit (the only way these rings actually join the collection)

The smart collection joins any product whose tags include the exact string `Christian Rings`. Case-sensitive. No quotes. No parens.

For each of the 34 rings below, BETA does:

1. Pull the product from Shopify (use the title or handle to match).
2. Read the current tag list.
3. If `Christian Rings` is already present, skip.
4. If missing, append `Christian Rings` to the tag list (do not remove or reorder existing tags).
5. Save.
6. Confirm the product now appears in the collection's product list.

Do not strip the `Inside` engraving tag, the `Comfort Fit` tag, the material tags, or any other existing tag. Append only.

### Ring list (34 total)

These are the titles as they appear in Shopify (codename + descriptor):

**Batch A. Original Christian Rings batch (most should already be tagged, verify anyway):**

1. CREDO | Gold Tungsten Wedding Band, Woven Cross Pattern, Beveled Edges
2. PARISH | Men's Tungsten Cross Wedding Band, Woven Pattern, Flat Profile
3. CHANCEL | Tungsten Cross Wedding Band, Deep Woven Cross Pattern, Flat
4. CRUX | Gold Tungsten Sideways Cross Wedding Band, Domed Profile
5. STEADFAST | Black Tungsten Iron Cross Wedding Band, Comfort Fit
6. CREED | Black Tungsten Minimalist Cross Wedding Band, Flat
7. VESPER | Black Tungsten Sideways Cross Wedding Band, Flat
8. SUMMIT | Black Tungsten Mountain Landscape Wedding Band, Flat
9. ADVENT | Black Tungsten Nativity Scene Wedding Band, Christian
10. CHAPLET | Black Tungsten Rosary Wedding Band, Catholic Christian
11. PSALM | Black Tungsten Lord's Prayer Wedding Band, Scripture
12. PALM | Tungsten Palm Branches Wedding Band, Christian, Silver
13. VOTIVE | Tungsten Rosary Wedding Band, Catholic Christian, Silver
14. ORATE | Tungsten Lord's Prayer Wedding Band, Christian, Silver
15. RIDGE | Tungsten Mountain Landscape Wedding Band, Silver, Christian
16. EVE | Gold Tungsten Nativity Scene Wedding Band, Domed Profile

**Batch B. Newer Christian listings (probably missing the tag, confirm and add):**

17. AVE | Tungsten Ave Maria Engraved Wedding Band, Spanish
18. MARIAN | Tungsten Hail Mary Engraved Wedding Band
19. CENACLE | Black Tungsten Last Supper Wedding Band, Flat
20. EUCHARIST | Tungsten Last Supper Wedding Band, Flat
21. COVENANT | Black Tungsten Cross Pattern Wedding Band, Flat
22. CONSECRATE | Tungsten Cross Pattern Wedding Band, Flat Classic
23. ECCLESIA | Black Tungsten Dotted Cross Wedding Band, Flat
24. DEVOUT | Tungsten Dotted Cross Wedding Band, Flat
25. CALVARY | Black Tungsten Thorn Crown Wedding Band, Domed
26. GOLGOTHA | Tungsten Thorn Crown Wedding Band, Flat Classic
27. MARTYR | Tungsten Thorn Crown Wedding Band, Black Center, Beveled Edges
28. SACRED | Gold & Black Tungsten Thorn Crown Wedding Band, Beveled Edges
29. VIGIL | Black Tungsten Brushed Cross Wedding Band, Domed, 8mm
30. IONA | Tungsten Celtic Cross Wedding Band, Flat, 8mm
31. TRIUNE | Tungsten Raised Center Wedding Band, Engraved Crosses, 8mm
32. HOST | Gold & Black Tungsten Multi-Cross Wedding Band, Two-Tone
33. SANCTUS | Gold Tungsten Sunburst Cross Wedding Band, Beveled Edges
34. FLEUR | Rose Gold Tungsten Fleur Cross Wedding Band, Beveled Edges

### Tag rules (locked, do not deviate)

- Tag spelling: `Christian Rings` (capital C, capital R, single space, no trailing or leading whitespace).
- Do not add `Christian` as a separate tag, do not add `Faith` or `Catholic` as a substitute, do not pluralize differently. The smart collection matches the exact string.
- If a ring already has a near-miss tag like `christian rings` (lowercase) or `Christian Ring` (singular), normalize it to `Christian Rings` and remove the bad variant.

---

## Step 2: Build the collection page to Aydins standard

The smart-collection rule is fine. What is probably missing is everything that makes the page sell. Fill all of the following on the Christian Rings collection record itself.

### 2a. Title (Shopify "Title" field)

Use exactly:

```
Christian Rings
```

No suffix. No "Collection". No "Faith Rings."

### 2b. Handle (URL)

Confirm the handle is:

```
christian-rings
```

If something different is live, leave it (do not break SEO with a redirect). Just verify and report back.

### 2c. SEO title (Shopify "Page title" field)

**Limit: 70 characters.** Use:

```
Christian Wedding Bands — Cross, Faith & Scripture Rings | Aydins
```

Count: 64 characters. Within limit.

If em dashes are not allowed in the current Aydins voice rule (they are not: rule locked 2026-05-15), rewrite to:

```
Christian Wedding Bands: Cross, Faith & Scripture Rings | Aydins
```

Count: 64 characters. Use this version.

### 2d. Meta description (Shopify "Meta description" field)

**Limit: 150 characters.** Use:

```
Christian wedding bands for men. Cross, Lord's Prayer, Rosary, and Scripture rings. Free engraving and free U.S. shipping. Engraved in Texas.
```

Count: 144 characters. Within limit.

### 2e. Collection description (the body content on the storefront)

Write fresh in the Aydins voice. No em dashes. No "handcrafted." No third-party brand names. Use this draft (BETA may polish but must keep all trust pillars and the no-em-dashes rule):

```
Faith you can wear every day.

Aydins Christian Rings are built for the men who carry their faith into the work, the family, and the rest of their lives. Crosses, Lord's Prayer scripture, Rosary patterns, Last Supper engravings, Thorn Crown details, and Celtic cross designs. Each ring is comfort fit, available in tungsten (silver, black, gold, rose gold, and two-tone), and ready for free inside engraving.

Every Aydins ring includes:

- Free laser engraving (text, symbols, or handwriting) on the inside band
- Free U.S. shipping
- Comfort fit on every width
- Engraved and shipped from our workshop in Irving, Texas
- 30-day returns and the Aydins Lifetime Sizing program for the original owner
- Operating since 2011

Engrave a verse, a name, or a date. Make it his.
```

Notes for BETA:

- Headline ("Faith you can wear every day.") goes in an H2 or bold lead, not H1 (Shopify's collection title is the H1).
- Bullet block stays as a real `<ul>`, not paragraph fragments. Mobile readability.
- Do NOT add "lifetime warranty" or "free lifetime resizing" as bare phrases. Use the exact wording above.
- Do NOT name Thorsten, Universal Jewelry, or any wholesale source.

### 2f. Hero / collection image

The collection needs an image (used in social previews, internal navigation, and on the homepage module).

- **Source:** pull the hero image from CREDO (`9362184962285`) as a placeholder if no dedicated collection image exists. CREDO is the flagship Christian ring and the gold woven-cross hero already photographs well.
- **Dimensions:** 1200 x 1200 minimum, square preferred.
- **Alt text:** `Aydins Christian wedding bands collection — cross and scripture rings in tungsten`
- If BETA can flag this to me as "needs a dedicated lifestyle shot," do that. Placeholder is acceptable for now.

### 2g. Sort order

Set to **Manual** so the top of the page can be merchandised.

For the initial manual order, lead with the visual heroes and price anchors. Use this order at the top of the collection (then let everything else flow alphabetical or by best-seller):

1. CREDO (gold woven cross, flagship, $329)
2. SANCTUS (gold sunburst cross, $329)
3. HOST (gold and black multi-cross, $359)
4. SACRED (gold and black thorn crown)
5. CRUX (gold sideways cross)
6. FLEUR (rose gold fleur cross)
7. EVE (gold nativity)
8. MARTYR (thorn crown, black center, beveled)
9. PARISH (silver woven cross)
10. CHANCEL (black deep woven cross)

Remaining 24 rings: alphabetical by codename underneath. BETA can refine after live data comes in.

---

## Step 3: Verify

Once Steps 1 and 2 are done, BETA confirms:

- [ ] All 34 rings carry the tag `Christian Rings` (exact spelling).
- [ ] All 34 rings appear in the live collection on the storefront.
- [ ] No ring outside the 34 is incorrectly tagged with `Christian Rings` (false positives).
- [ ] Collection title, handle, SEO title (≤70 chars), meta description (≤150 chars), description body, hero image, alt text, and manual sort order are set.
- [ ] Mobile check on the live collection URL: hero image renders, description reads cleanly, first row of products is the merchandised lead-with set, no broken cards.
- [ ] No em dashes anywhere on the page.

Report any ring in the list of 34 that BETA cannot find in Shopify (title or handle mismatch). Do not guess and do not create new product records.

---

## Step 4: Hand back

When done, reply with:

1. Confirmed count of rings now in the collection (target: 34).
2. Anything skipped or unresolved (with reason).
3. Live collection URL.
4. A note flagging whether a dedicated hero / lifestyle photo is still needed (yes if CREDO product shot is being used as placeholder).

---

## Reference (source-of-truth files)

- [[03 Projects/Aydins Jewelry/CLAUDE.md]] (project rules, voice, no-em-dash rule)
- [[03 Projects/Aydins Jewelry/(C) Shopify Listing Standard — Brief for Beta-Shop.md]] (collection assignment rule, SEO limits)
- [[03 Projects/Aydins Jewelry/(C) Aydins Policies — Source of Truth]] (warranty, returns, lifetime sizing wording)
- [[03 Projects/Aydins Jewelry/04 Launch/(C) christian-rings-batch.md]] (original 19-ring batch tracker, including the smart-collection GID and tag rule)
