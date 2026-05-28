# 📋 GMC Remediation Playbook — Aydins Jewelry
**Generated:** 2026-05-12 | **Feed size:** 273,390 products | **Total issues:** ~1.46M

---

## 1. EXECUTIVE SUMMARY

Your feed has three distinct problem layers: a **currency mismatch** in shipping config that's blocking 220K products from serving at all, **missing demographic attributes** (gender, age group, color) that are demoting 558K–900K+ variants in rankings, and a **smaller batch of ~1,320 product-level errors** (unavailable pages, missing prices, bad availability flags) that need product-by-product fixes. Fix the currency/shipping setting first — it's a single toggle that unlocks 219,862 disapprovals immediately. Then apply feed rules for gender, age group, and color to wipe out the demotion pile (1.46M issues) in one batch. The remaining ~1,320 hard disapprovals and 6 sensitive-category items need targeted attention but represent under 0.1% of your catalog.

---

## 2. STEP-BY-STEP FIXES

---

### 2a. Currency / Shipping Currency Mismatch
**🔴 KILLS: 219,862 disapprovals + 336 unsupported currency + 338 missing shipping = ~220,536 disapprovals**

**WHERE (Google Merchant Center):**
`GMC → Settings (gear icon, top right) → Shipping and returns → [your shipping service name] → Edit`

**WHAT TO CHECK AND FIX:**

1. Open each shipping service in GMC. Look at the **Currency** field on the shipping service — it must match your product feed currency exactly (`USD`).
2. If any shipping service shows a non-USD currency or blank, change it to `USD`.
3. Check **every shipping service** you have listed (you may have more than one — e.g., "Free US Shipping," "Standard," etc.).

**WHERE (also check — Shopify Google & YouTube channel):**
`Shopify Admin → Sales Channels → Google & YouTube → Settings → Shipping`

Verify that Shopify is syncing your shipping service as USD. If you've recently changed your Shopify Markets primary currency or added a market, it can push a non-USD shipping service to GMC automatically.

**WHY THIS WORKS:**
GMC compares the currency in your product `price` attribute against the currency declared in your shipping service. If they don't match, GMC disapproves for "mismatched currency in shipping information." The 336 "unsupported currency" disapprovals are almost certainly the same root cause — a non-USD currency slipped into shipping or price fields.

**EXPECTED RESULT:** ~220,536 disapprovals resolved after GMC re-crawl (typically 24–72 hrs).

**⏱ TIME ESTIMATE:** 15–20 minutes to audit and fix all shipping services.

---

### 2b. Gender + Age Group Attributes (Feed Rules)
**🟡 KILLS: 451,274 gender demotions + 451,274 age_group demotions = 902,548 demotions**

This is your biggest demotion pile. You don't need to touch individual products — use GMC feed rules to set defaults.

**WHERE:**
`GMC → Products → Feeds → [your Shopify feed name] → Feed rules (tab at top)`

**WHAT TO DO:**

**Set gender = male:**
1. Click **+ Add rule**
2. Attribute to set: `Gender`
3. Rule type: **Set to a static value**
4. Value: `male`
5. Apply to: **All products** (or add a condition to exclude if you carry women's styles — see Risk section)
6. Click **Save**

**Set age_group = adult:**
1. Click **+ Add rule**
2. Attribute to set: `Age group`
3. Rule type: **Set to a static value**
4. Value: `adult`
5. Apply to: **All products**
6. Click **Save**

**WHY THIS WORKS:**
GMC demotes apparel and jewelry items missing `gender` and `age_group` because it can't properly categorize them for Shopping filters. A feed-level rule fills the gap for your entire catalog without touching Shopify.

**⚠️ BEFORE YOU SET gender=male — READ THE RISK SECTION (2e and Section 5)**
If any products are women's rings or unisex, you need a more nuanced rule. If 100% of your catalog is men's wedding bands (which your context suggests), set `male` globally and move on.

**EXPECTED RESULT:** 902,548 demotions cleared. Products eligible for gender/age filtering in Shopping.

**⏱ TIME ESTIMATE:** 10 minutes. Feed rules apply on next feed processing (can trigger manually — see Section 4).

---

### 2c. Color Attribute Mapping
**🟡 KILLS: 558,273 color demotions**

**WHERE:**
`GMC → Products → Feeds → [your Shopify feed name] → Feed rules`

**WHAT TO DO (Option A — Feed Rule from existing Shopify data):**

Shopify likely already sends color data in a variant metafield or option. Check what GMC is receiving:

1. `GMC → Products → All products → click any product → scroll to "Submitted attributes"`
2. Look for `Color`, `Item group ID`, or any variant option that contains color data (sometimes arrives as `custom_label_0` or similar)

**If color data exists in a non-standard field:**
1. Add rule → Attribute: `Color`
2. Rule type: **Map from another attribute**
3. Source attribute: whichever field contains your color data (e.g., `additional_image_link`, a custom label, or variant option)
4. Save

**If Shopify is NOT sending color at all (Option B — Shopify side):**
`Shopify Admin → Sales Channels → Google & YouTube → Product sync settings`

Check if "Variant options" are being synced. If color is a variant option in Shopify (e.g., Option 1 = "Black / Silver"), it should be flowing through. If it's not:

- `Shopify Admin → Settings → Custom data → Products` — verify a `Color` metafield exists
- Or go to `Shopify Admin → Sales Channels → Google & YouTube → [individual product]` and check what's being submitted

**For ring materials (tungsten, titanium, etc.) used as "color":**
If your "color" is actually finish/material (e.g., "Black Tungsten," "Rose Gold Tone"), that's valid for GMC's color field. Map your material/finish option to `Color` in the feed rule.

**EXPECTED RESULT:** 558,273 demotions cleared.

**⏱ TIME ESTIMATE:** 20–30 minutes (15 min diagnosing source field, 10 min setting the rule).

---

### 2d. Remaining Hard Disapprovals (~1,320 items)

These need individual attention. Pull the detailed report first.

**WHERE:**
`GMC → Products → All products → Filter by: "Disapproved" → Export (download icon, top right)`
Export as CSV. Sort by issue type.

---

**🔴 550 — Product page unavailable**

**WHAT TO DO:**
1. Filter the export for this issue
2. Open each product URL from the feed
3. Most common causes:
   - Product deleted in Shopify but still in feed (fix: delete or hide in Shopify, it'll drop from feed on next sync)
   - URL slug changed (fix: set up a 301 redirect in `Shopify Admin → Online Store → Navigation → URL redirects`)
   - Product set to "Draft" (fix: publish it or exclude it from the Google channel)

**⏱ TIME ESTIMATE:** 30–60 min depending on how many are genuinely deleted vs. just draft.

---

**🔴 410 — Missing product price**

**WHERE:**
`GMC export → filter "Missing price" → check each product ID in Shopify`

`Shopify Admin → Products → [product] → Pricing section`

These likely have $0 or blank price on a variant. Fix the price in Shopify and re-sync, or exclude the variant from the Google channel.

**⏱ TIME ESTIMATE:** 20–30 min.

---

**🔴 18 — Missing value [availability]**

**WHERE:**
`GMC → Products → Feeds → Feed rules`

Add rule: Attribute = `Availability`, Set to static value = `in_stock` (assuming they are in stock).

If some are genuinely out of stock, Shopify should be sending `out_of_stock` automatically. The 18 flagged items likely have a blank availability field — the feed rule will fill it.

**⏱ TIME ESTIMATE:** 5 minutes.

---

**🔴 8 — Mismatched product price**

GMC crawled the page and found a different price than what's in the feed. Usually happens when:
- A sale ended but the feed still shows sale price
- Shopify currency rounding differs slightly from the feed

**WHERE:**
`GMC export → filter "Mismatched price" → check each product URL manually`

Compare the price shown on the live product page vs. what GMC shows in "Submitted attributes." Fix whichever is wrong (update Shopify price or wait for re-crawl after sale ends).

**⏱ TIME ESTIMATE:** 20 min.

---

### 2e. 6 Memorial/Keepsake Items — Sensitive Category (Personalized Advertising: Identity and Belief)

These are likely ash/memorial rings or grief-related products. Google flags these under its sensitive advertising categories.

**YOU HAVE TWO PATHS:**

---

**PATH 1 — Appeal (if these are standard rings, not ash/memorial)**
If these products were miscategorized and don't contain ashes or grief-related positioning:

`GMC → Products → All products → filter to these 6 items → click each → "Request review"`

In the review request, state clearly: *"This is a standard tungsten/titanium wedding band. It does not contain ashes, is not memorial jewelry, and is not marketed toward grieving customers."*

**Timeline:** 1–3 business days for GMC review.

---

**PATH 2 — Remove from Shopping (if these ARE memorial/ash keepsake rings)**
If these genuinely contain ashes or are marketed for memorial use:

`Shopify Admin → Sales Channels → Google & YouTube → [each of the 6 products] → toggle off "Sync to Google"`

This removes them from the Shopping feed without deleting the product from your store. They keep their organic search presence.

**⏱ TIME ESTIMATE:** 10 minutes either path.

**RECOMMENDATION:** Check the product titles/descriptions for these 6 items first. If they mention "memorial," "ashes," "loss," "remembrance" — exclude from Shopping. If not, appeal.

---

## 3. SHOPIFY GOOGLE CHANNEL — Settings to Verify

`Shopify Admin → Sales Channels → Google & YouTube`

Work through this checklist:

| Setting | Where | What to verify |
|---|---|---|
| **Primary market currency** | `Settings → Markets → Primary market` | Must be set to **United States / USD**. If a non-US market was accidentally set as primary, your feed ships non-USD prices. |
| **Additional markets** | `Settings → Markets` | If you've enabled CA/GB/AU markets, each gets its own feed in GMC. Confirm you're only actively managing the US feed. Disable or pause other markets if you're not ready to manage them. |
| **Shipping zones** | `Settings → Shipping and delivery → [your shipping profile] → shipping zones` | Confirm "United States" zone exists with Free Shipping set. This is what syncs to GMC's shipping service. |
| **Currency conversion** | `Settings → Markets → Primary market → Currency` | Should show USD. "Auto-convert prices" should be OFF unless you're intentionally serving international markets. |
| **Product sync scope** | `Google & YouTube → Product sync` | Confirm sync is set to "All products" or your intended collection. Draft products should be excluded. |
| **Google channel reconnect** | `Google & YouTube → Overview` | Check for any auth warnings or "reconnect" prompts — a stale connection can cause feed data to stop updating. |

---

## 4. POST-FIX VERIFICATION

**Step 1 — Trigger a manual feed re-fetch:**
`GMC → Products → Feeds → [your feed] → Fetch now (button top right)`

This tells GMC to re-process your Shopify feed immediately instead of waiting for the scheduled crawl.

**Step 2 — Check Diagnostics:**
`GMC → Products → Diagnostics`

After fetch completes (usually 15–30 min for a 273K product feed), look at:
- **Account-level issues** tab — shipping/currency errors should be gone
- **Item-level issues** tab — disapproval counts should drop
- **Feed-level issues** tab — any structural problems with the feed itself

**Step 3 — Spot-check individual products:**
`GMC → Products → All products → search a specific product ID`

Click through to see "Submitted attributes" — confirm `gender`, `age_group`, `color`, `availability`, and `price` are populated and correct.

**Step 4 — Check Shopping ads eligibility:**
`GMC → Overview` — the "Active products" number should climb within 24–48 hrs as crawls complete.

**Expected timeline:**
| Fix type | When you'll see results |
|---|---|
| Feed rules (gender, age, color) | Next feed fetch — same day |
| Shipping currency fix | 24–48 hrs after fix |
| Product page fixes (URLs, prices) | 24–72 hrs after Googlebot re-crawls pages |
| Sensitive category appeals | 1–3 business days |
| Full re-approval of 220K products | 24–72 hrs (GMC re-crawl cycle) |

---

## 5. RISKS / WATCH-OUTS

**🚨 gender=male — confirm your catalog before bulk-applying**
If Aydins carries *any* women's rings, unisex bands, or couples sets, setting `gender=male` globally will mislabel those products. Check your Shopify collections. If you have a "Women's" or "His and Hers" collection, add a feed rule condition: apply `male` only where product type ≠ "Women's Rings." Wrong gender data doesn't disapprove — but it misdirects your Shopping ads to male-targeted audiences, hurting conversion on those products.

**🚨 Feed rules overwrite hand-set values — check before applying**
GMC feed rules can override attributes you've manually set on individual products. Before saving any rule, click **"Preview"** in the feed rules UI to see a sample of what will change. If you've hand-set color on any products, the rule may overwrite them. You can add a condition: "apply only when [attribute] is blank" to be safe.

**🚨 Multiple shipping services in GMC**
If you have more than one shipping service (e.g., one from a previous integration, one from the current Shopify channel), fix the currency on ALL of them — or delete the stale ones. A single bad shipping service can cause currency mismatch across the entire account.

**🚨 Fixing 550 "page unavailable" — don't just delete products**
If those products have any organic search traffic or backlinks, deleting them without a redirect will cause 404s. Add a 301 redirect to the closest matching live product before removing from Shopify.

**🚨 The 273K products in GMC vs. 504 Etsy listings**
Your GMC feed has 273,390 entries because it includes all product variants (size × color). This is correct — but it means fixing one Shopify product fixes potentially hundreds of GMC entries. Don't be discouraged by the issue counts; the actual number of broken *products* is much smaller.

**🚨 After the shipping fix, verify Google Ads campaigns aren't paused**
When GMC has large-scale disapprovals, Google Ads sometimes auto-pauses Shopping campaigns or reduces spend. After fixes propagate, check `Google Ads → Campaigns → Shopping campaigns` to confirm they're active and budgets are running normally.

---

**Total estimated time to execute this playbook: 2–3 hours**
**Total issues resolved when complete: ~1.46M demotions + ~220K disapprovals**
**Remaining after playbook: ~770 hard product-level fixes + 6 sensitive items**

---

*— BETA GOOGLE | Aydins Jewelry GMC Remediation | 2026-05-12*
