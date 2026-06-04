# BETA GOOGLE STRATEGIST FRAMEWORK + PRIORITIZED RECOMMENDATIONS

**Date**: 2026-06-03 | **Account**: Aydins Jewelry (shopaydins.com)  
**Frameworks**: Campaign Structure, Keyword, Bid, Merchant Center, PMax, SEO, Scale/Kill, Cadence

---

## FRAMEWORK 1: CAMPAIGN STRUCTURE

### Aydins Recommended Campaign Architecture

```
Aydins Google Ads Account
|
+-- Brand Search (Exact Match only)
|   Budget: 10-15% of total
|   Bid: Target Impression Share 80%
|   Keywords: [aydins jewelry], [shopaydins], [aydins wedding band], [aydins ring]
|
+-- Non-Brand Search (Phrase + Exact)
|   Budget: 30-35% of total
|   Bid: Target CPA ($80-$100) or Target ROAS (400%+)
|   Structure: Ad group per product category (tungsten, titanium, ceramic, gold, wood inlay)
|
+-- Standard Shopping OR PMax (Pick ONE)
|   Budget: 40-50% of total
|   Decision: See Framework 1.2 below
|
+-- Demand Gen (YouTube + Discover, optional)
|   Budget: 5-10% when brand awareness needed
|   Audience: Retargeting + Similar segments
```

### PMax vs Standard Shopping Decision Tree

```
Does Aydins have clean, high-quality feed (85%+ approval rate)?
  NO  -> FIX FEED FIRST. Do not launch PMax with 27% approval rate.
  YES -> Can PMax get conversion data from other channels?
           NO  -> Start with Standard Shopping + Search
           YES -> Test PMax with 20% budget allocation 
                  Monitor: PMax ROAS vs Standard Shopping ROAS
                  If PMax ROAS < Standard Shopping ROAS for 14 days -> Kill PMax
                  If PMax ROAS >= Standard Shopping ROAS for 14 days -> Scale PMax
```

**Current Status**: Feed at 27.3% approval. **Do not launch PMax**. Fix feed first.

### When to Add Demand Gen

- Only after Search + Shopping are running at 400%+ ROAS for 30+ days
- Budget must be incremental, not cannibalized
- Start with retargeting audiences only (no prospecting)
- Prospecting only after retargeting shows 300%+ ROAS for 21 days

---

## FRAMEWORK 2: KEYWORD STRATEGY

### Match Type Tier

| Tier | Match Type | Use Case | Aydins Priority |
|------|-----------|----------|-----------------|
| Core | Exact Match | [tungsten wedding band], [mens wedding ring] | HIGH |
| Expansion | Phrase Match | "mens titanium wedding ring", "black tungsten ring" | MEDIUM |
| Discovery | Broad (Smart Bidding) | mens wedding ring unique material | LOW - only with Max Conv Value |
| Long Tail | Exact Match | [8mm black tungsten wedding band for men] | HIGH - strongest intent |

### Negative Keyword Library Structure

**Sitewide Negatives**:
```
-free, -cheap, -wholesale, -bulk, -used, -vintage, -antique, 
-engagement ring, -earrings, -necklace, -bracelet, -pendant,
-ladies, -women, -hers, -girlfriend, -wife (unless targeting women)
-silver (unless Aydins carries silver)
```

**Campaign Negatives (Non-Brand Search)**:
```
-aydins, -shopaydins (avoid cannibalizing Brand campaign)
-repair, -fix, -resize (unless service offering exists)
```

**Ad Group Negatives**:
```
Product-category specific: 
  Tungsten group: [-titanium, -ceramic, -wood, -carbon fiber]
  Custom group: [-standard sizes, -stock]
```

### Search Term Review Cadence

| Cadence | Action | Filter |
|---------|--------|--------|
| Daily | Review new search terms | 10+ impressions, 0 conversions |
| Weekly | Add negatives | Irrelevant, high spend ($10+), 0 conversions in 7 days |
| Bi-weekly | Add positives | Low volume high intent, CPA under target |
| Monthly | Full search term report audit | All terms with spend > $50 |

---

## FRAMEWORK 3: BID STRATEGY

### Decision Tree

```
How many conversions in last 30 days?
  < 15 conversions:
    -> Maximize Conversions (no target)
    -> Let Google learn without constraint
    -> Set daily budget as ceiling
  
  15-50 conversions:
    -> Target CPA (if profit margin known)
    -> Set CPA at 20-25% of AOV ($80-$100)
    -> Monitor learning phase (7-14 days)
  
  50+ conversions AND value tracking set up:
    -> Target ROAS (400% minimum)
    -> OR Maximize Conversion Value
  
  Value tracking NOT set up:
    -> Stay on Target CPA until value tracking is live
```

### When to Switch Strategies

| Current | Switch To | Trigger |
|---------|-----------|---------|
| Max Conv | Target CPA | 15+ conversions in 14 days AND CPA stable for 7 days |
| Target CPA | Target ROAS | 50+ conversions in 30 days AND value tracking confirmed |
| Target ROAS | Max Conv Value | ROAS above target for 21 days AND impression share < 50% |
| Any | Switch back | Performance drops 30%+ in 7 days after switch |

### Jewelry-Specific Bidding Notes

- AOV varies ($100-$1,000): Use value-based bidding to favor higher AOV products
- Wedding band buying cycle: Research 7-14 days > Purchase. View-through conversions may undercount impact
- Consider view-through conversion window: 14-30 days for jewelry category

---

## FRAMEWORK 4: MERCHANT CENTER STRATEGY

### Feed Quality Rules

**Titles** (Target: 70-120 chars):
```
Pattern: [Product Name] | [Key Feature] [Material] [Finish] [Width] | Mens Wedding Band
Example: SHERIFF | Domed Titanium Wedding Ring Brushed Finish Blue Grooves 8mm | Mens Wedding Band
Rule: Include material + finish + width + collection name
Rule: Max 150 chars, no keyword stuffing
```

**Descriptions** (Target: 200-500 chars):
```
Pattern: Unique product description > 200 characters minimum
Include: Material, width options, finish, comfort fit, care instructions
Avoid: Truncation (fix 498 text_value_truncated errors)
```

**Images**:
- Minimum: 800x800px (fix 161 image_too_small)
- Target: 2000x2000px (avoid upcoming 169 image_too_small_for_high_resolution enforcement)
- Format: JPEG or PNG, no broken links (fix 49+ image_link_broken)
- Background: White or transparent for primary image

**Attributes**:
- Age group: ALL products -> "adult" (~1,496 fix needed)
- Gender: ALL products -> "male" or "unisex" (~1,496 fix needed)
- Color: Define per product (~1,629 fix needed)
- GTIN: Assign where available (improves Shopping placement)
- Product weight: Fill missing values (fix 442 missing_unit)

### Disapproval Resolution Priority Order

| Priority | Issue | Fix Time | Urgency |
|----------|-------|----------|---------|
| P0 | Missing color, age group, gender | 1-2 days with Vela | CRITICAL - blocks 68% of feed |
| P0 | Identity/belief policy violations | Immediate removal | CRITICAL - account risk |
| P1 | Landing page errors (293) | Fix broken URLs | CRITICAL - products disapproved |
| P1 | Missing price (202) | Fill pricing | CRITICAL - products disapproved |
| P2 | Currency mismatches (914) | Standardize shipping | HIGH - 90+ day countdown |
| P2 | Image quality issues (420) | Re-upload high-res | HIGH - upcoming enforcement |
| P3 | Korea market issues | Add KR shipping + business reg | MEDIUM - market-specific |
| P3 | UTF-8 encoding errors | Fix descriptions | MEDIUM - affects rankings |

### Promotion Feed Strategy

- Not currently using Merchant Promotions
- Consider: Free shipping threshold ($100+ orders), seasonal (wedding season May-Oct)
- Promotions can improve CTR by 10-20% on Shopping

### Custom Labels for Budget Segmentation

| Label | Use | Criterion | Goal |
|-------|-----|-----------|------|
| Label 0 | Margin tier | Products with >50% margin | Bid higher, scale aggressively |
| Label 1 | Best sellers | Top 20% by revenue over 90 days | Defend impression share |
| Label 2 | New arrivals | Added <30 days ago | Test new products |
| Label 3 | Clearance | >180 days with zero sales | Reduce bid to minimum |
| Label 4 | Custom/engraved | Customizable products | Differentiate bidding for higher AOV |

---

## FRAMEWORK 5: PERFORMANCE MAX

### Implementation (Only After Feed Fix)

PMax should only be activated when:
1. Feed approval rate >= 85%
2. Shopping campaign has 30 days of conversion data
3. Value tracking is confirmed working

### Asset Group Structure

| Asset Group | Theme | Products | Audience Signals |
|------------|-------|----------|-----------------|
| AG 1 | Bestsellers | Top 50 by revenue | Past purchasers, In-market: Wedding Bands |
| AG 2 | Tungsten Rings | Tungsten products | In-market: Tungsten Rings, Men's Jewelry |
| AG 3 | Titanium Rings | Titanium products | In-market: Titanium Rings |
| AG 4 | Custom/Engravable | Custom products | Custom audiences, retargeting |
| AG 5 | Gold/High AOV | Gold/Platinum >$500 | Affinity: Luxury, In-market: Gold Jewelry |

### Audience Signal Seeding

- Start with: In-market audiences (Weddings & Events, Apparel & Accessories)
- Add: Custom segments (mens wedding band, tungsten ring interest)
- Add: Retargeting (30-day site visitors, 14-day cart abandoners)
- Never: Competitor audiences (policy violation)

### Brand Exclusions

- Add brand names to negative keywords at campaign level: `-shopaydins, -aydins`
- PMax will otherwise show brand terms across Shopping/YouTube/Display

### Asset Rotation Rules

- All assets must be "approved" before PMax launch
- Minimum 5 headlines, 5 descriptions, 3 images, 1 video per asset group
- Rotate creative monthly to avoid ad fatigue
- Pause underperformers (CTR below 50% of group average)

---

## FRAMEWORK 6: SEO STRATEGY

### Content Priority Tiers

| Tier | Type | Aydins Example | Frequency |
|------|------|----------------|-----------|
| P0 | Money pages | Product pages (12,500) | Optimize feed/structured data first |
| P1 | Category/collection | Tungsten Wedding Bands, Titanium Rings | Improve, add unique content |
| P2 | Hub guides (SEO focus) | "Ultimate Guide to Mens Wedding Bands" | 1-2/month |
| P3 | Supporting content | Material guides, size guides, care | 1-2/quarter |

### Technical SEO Check Cadence

| Frequency | Checks | Owner |
|-----------|--------|-------|
| Weekly | Index coverage, new 404s, mobile usability | BETA GOOGLE |
| Bi-weekly | Crawl stats, sitemap changes | BETA GOOGLE |
| Monthly | Core Web Vitals, structured data errors, backlinks | BETA GOOGLE |
| Post-deploy | Schema validation, canonical checks | BETA GOOGLE |

### Schema Coverage Targets

| Schema Type | Target Coverage | Current | Gap |
|-------------|----------------|---------|-----|
| Product | 100% of product pages | ~12,500 pages | Structured data quality unknown |
| Organization | 1 page | Homepage | Should be present |
| BreadcrumbList | All category pages | Unknown | Should be present |
| FAQ | Hub guide pages | Unknown | Optional but helpful |
| Review/Rating | Top products | Unknown | Improves rich results |

### Internal Link Strategy

- Link from hub guides to specific product pages (contextual, not sidebar)
- Category pages link to product pages, subcategories up to parent categories
- Avoid linking every product from every page (thin links)
- Use descriptive anchor text (not "click here" or "shop now")

---

## FRAMEWORK 7: SCALE + KILL RULES

### Auto-Scale Criteria

Scale campaign budget +20% when ALL conditions met:
1. 14-day ROAS consistently above target (>400%)
2. CPA stable (within 20% of 14-day average) for 7+ consecutive days
3. Impression share has headroom (<85% IS)
4. Budget not hitting daily cap (spending <95% of budget)

**Max daily budget change**: +/-20% per adjustment (never exceed)
**Cooldown**: 48 hours minimum between adjustments

### Auto-Kill Criteria

Kill campaign (pause immediately) when ANY condition met:
1. 7-day ROAS below 1.5 (150%)
2. $50 spend with 0 conversions
3. Quality Score crashes below 4 on top 10 keywords
4. Landing page error rate >20% - fix URLs first, then reactivate
5. Policy violation (identity/belief, misinformation)

### Reactivation Rules

- Killed campaign can reactivate only after ALL issues resolved
- Start at 50% of previous budget
- Monitor for 7 days before scaling up
- If same conditions recur within 30 days, permanent kill

---

## FRAMEWORK 8: OPERATING CADENCE

### Daily (7am Telegram)

| Check | What | Action if Red |
|-------|------|--------------|
| Account health | Any disapprovals/account warnings | Surface in Telegram |
| Spend tracking | Daily spend vs budget | Flag if > budget/30 |
| ROAS by campaign | Tracks to target | Kill candidate assessment |
| Top scale candidates | Campaigns meeting auto-scale criteria | Surface for approva |
| Top kill candidates | Campaigns meeting auto-kill criteria | Surface for approval |
| MC issues | New disapprovals overnight | Flag count and reason |
| GSC alerts | Coverage drop, manual action | Immediate Telegram |

### Weekly (Monday Brief)

| Item | Detail |
|------|--------|
| Full performance review | All campaigns, all metrics |
| Top 3 strategic decisions | Most impactful choices this week |
| Feed quality check | Approval rate change, new issues |
| Keyword expansion | Search term report new positives |
| Competitor moves | Notable changes in auction landscape |

### Pre-Action Checklist

Before ANY spend change:
1. [ ] Confirm current ROAS trend (7d and 14d)
2. [ ] Check learning phase status (if in learning, do not change)
3. [ ] Verify conversion tracking firing correctly in last 24h
4. [ ] Review if any campaign-level cap hit
5. [ ] Check for Google outages or known issues
6. [ ] Confirm no pending policy violation or suspension risk
7. [ ] Document before/after state for accountability

---

## FRAMEWORK 9: PRO-LEVEL DECISION FRAMEWORK

### Telegram Decision Format

```
DECISION: [Campaign Name] - [Action]
WHAT: In plain language
WHY: Data-driven rationale with numbers
RISK ACCEPTED: What could go wrong (explicit)
RISK REJECTED: What risk we're choosing to avoid
BETA REC: Clear yes/no/wait
REPLY: Amir types APPROVE / DISCUSS / REJECT
```

### Decision Flow

```
Amir sends decision request
    -> BETA GOOGLE responds with Decision Format
    -> Amir reviews and replies
    -> BETA GOOGLE executes or adjusts
    -> Confirmation + before/after state in Telegram
```

---

## TOP 10 PRIORITIZED RECOMMENDATIONS

### P0: URGENT (Execute This Week)

**1. FIX GA4 OAuth Token**
- **Current**: Token expired 2026-06-02. No analytics data accessible.
- **Proposed**: Run fresh OAuth 2.0 flow with `analytics.readonly` scope. Create long-lived refresh token.
- **Expected ROI**: 30-day traffic, conversion, funnel, and revenue data becomes available. Critical for all decisions.
- **Risk**: Low. Read-only scope.
- **Dependencies**: Human to complete OAuth flow (browser redirect).
- **Time**: 15 minutes.
- **Recommendation**: APPROVE

**2. APPLY ATTRIBUTE FIXES (Color, Age Group, Gender)**
- **Current**: ~1,629 missing color, ~1,496 missing age group, ~1,496 missing gender. 68% of feed demoted.
- **Proposed**: Use Claude bot + Vela bulk editor to apply age group="adult", gender="male" across all products. Define color per product type.
- **Expected ROI**: Move ~3,000-4,000 products from demoted to approved. Free Listing traffic increase 2x-3x.
- **Risk**: Low. Age group "adult" and gender "male" are correct for wedding bands.
- **Dependencies**: Vela bulk editor access confirmed, color mapping defined.
- **Time**: 2-3 days.
- **Recommendation**: APPROVE

**3. REMOVE IDENTITY/BELIEF POLICY VIOLATIONS**
- **Current**: 4 ash holder pendant products flagged under "Personalized advertising: Identity and belief".
- **Proposed**: Remove these 4 products from Merchant Center feed entirely.
- **Expected ROI**: Eliminate account-level suspension risk. One policy violation can trigger account suspension.
- **Risk**: None. Products are not core wedding band inventory.
- **Dependencies**: None.
- **Time**: 1 hour.
- **Recommendation**: APPROVE

### P1: HIGH (This Month)

**4. FIX 293 LANDING PAGE ERRORS**
- **Current**: 293 products show landing pages as unreachable. These products are fully disapproved.
- **Proposed**: Identify common URL patterns. Fix broken URLs in feed or in Shopify.
- **Expected ROI**: 293 products become eligible. Estimated additional impressions: 5,000-15,000/month.
- **Risk**: Low. Products are already disapproved, no downside.
- **Dependencies**: URL audit, Shopify access.
- **Time**: 2-4 hours.
- **Recommendation**: APPROVE

**5. SET UP GOOGLE ADS API ACCESS**
- **Current**: No developer token, no OAuth, no customer ID. Full Ads audit blocked.
- **Proposed**: Complete phase3 checklist: apply for developer token, run OAuth, create credentials file.
- **Expected ROI**: Unlocks Ads campaign audit, keyword performance, Quality Scores, CPC data.
- **Risk**: Low. Read-only scope initially.
- **Dependencies**: Developer token approval (1-2 days), human for OAuth flow.
- **Time**: 1-2 days for approval, 30 min for setup.
- **Recommendation**: APPROVE

**6. GRANT SERVICE ACCOUNT GSC ACCESS**
- **Current**: Service account can authenticate to Search Console API but has no site access.
- **Proposed**: Add `beta-agent@amirs-command-center.iam.gserviceaccount.com` as owner/restricted user on `scod` (shopaydins.com).
- **Expected ROI**: Unlocks index coverage, query data, Core Web Vitals, mobile usability. Critical for SEO strategy.
- **Risk**: Low. Read-only permission.
- **Dependencies**: GSC owner to add the service account.
- **Time**: 10 minutes.
- **Recommendation**: APPROVE

### P2: MEDIUM (Next 30 Days)

**7. FIX SHIPPING CURRENCY MISMATCHES (914 products)**
- **Current**: 914 products have mismatched currency in shipping info. Products are "unaffected" but at risk of future enforcement.
- **Proposed**: Standardize shipping currency settings to align with product currency per country.
- **Expected ROI**: Prevent future disapprovals. Prepare for new market enforcement.
- **Risk**: Low. Data-only fix.
- **Dependencies**: Shipping configuration access in MC.
- **Time**: 4-8 hours.
- **Recommendation**: APPROVE

**8. RE-UPLOAD LOW-QUALITY IMAGES (420+ products)**
- **Current**: 90 low quality, 161 too small, 169 too small for high-res (upcoming enforcement).
- **Proposed**: Re-upload all product images at 2000x2000px minimum. Fix 49 broken image links.
- **Expected ROI**: Prevent upcoming image quality enforcement. Improve listing CTR.
- **Risk**: Medium - requires image pipeline.
- **Dependencies**: Batches of high-res product images.
- **Time**: 1-2 weeks.
- **Recommendation**: DISCUSS (needs image production budget)

**9. LAUNCH SHOPPING CAMPAIGN (After Feed Fix)**
- **Current**: No Shopping campaign data available. Feed at 27.3% approval.
- **Proposed**: After feed reaches 85%+ approval, launch Standard Shopping campaign. $500 initial daily budget. Target ROAS 400%.
- **Expected ROI**: If feed is clean, Shopping is highest-intent ad format for wedding bands.
- **Risk**: Low urgency (feed must be fixed first). Risk of low ROAS if feed is weak.
- **Dependencies**: Feed fix (#2 completed), Shopping campaign structure defined.
- **Time**: 2-3 hours after feed fix.
- **Recommendation**: WAIT (blocked by feed fix)

**10. BUILD BRANDED SEARCH CAMPAIGN**
- **Current**: No brand search campaign. Competitors may bid on Aydins brand terms.
- **Proposed**: Launch exact-match brand search campaign for [aydins jewelry], [shopaydins], [aydins wedding band]. Budget: $5-$10/day. Target Impression Share 80%.
- **Expected ROI**: Protect brand traffic at very low cost. Brand search typically converts at 10-20%. Estimated $300-$500/month in protected revenue for $150-$300 ad spend.
- **Risk**: Low. Brand search is cheapest/most efficient ad spend.
- **Dependencies**: Google Ads API setup (#5) to confirm customer ID.
- **Time**: 1 hour after Ads setup.
- **Recommendation**: DISCUSS (confirm no existing brand campaign)

---

## EXECUTION ROADMAP

```
Week 1 (Jun 3-9):     Fix #1 (GA4 OAuth) + #2 (Attributes) + #3 (Policy removals)
Week 2 (Jun 10-16):   Fix #4 (Landing page errors) + #5 (Ads API) + #6 (GSC)
Week 3 (Jun 17-23):   Fix #7 (Shipping currency) + #8 (Images begin)
Week 4 (Jun 24-30):   Monitor feed approval rate. Decide #9 (Shopping) + #10 (Brand Search)
```

---

## ADHERENCE TO GUARDRAILS

- All reads, no writes to any Google API or MC products
- No spend changes, no MC product removals (except #3 policy removal recommendation)
- No keyword changes
- Flags clearly surfaced: GA4 token expired, Ads API missing, GSC missing
- Rate limits: No API rate limits hit during audit (low volume requests)
- No em dashes used
- No third-party brand names (except standard industry terminology)
- No bare warranty references

---

*Generated by BETA GOOGLE Strategist*  
*Frameworks based on Google Ads best practices, MC feed management standards, and jewelry ecommerce patterns*