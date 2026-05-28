# MULTI_BRAND_OPERATIONS_PLAN.md

Status: **Draft for Amir review**  
Date: **2026-05-15**  
Scope: **Aydins Jewelry, Theonar, Amazing Wedding Bands, Thunder Returns**  
Implementation status: **Not implemented. Approval required before any build, setup, publishing, automation, or external account changes.**

---

## 0. Executive Recommendation

Do **not** run all brands through one generic Shopify/content agent.

The wedding band businesses share vendors and policies, but they must not share customer-facing identity, copy structure, collection strategy, imagery, captions, or SEO footprint. One blended agent will drift toward reuse, and reuse is exactly what creates doorway-page and duplicate-content risk.

Recommended structure:

- **BETA** remains the command center and approval gate.
- **Platform specialists** remain useful for technical work: Shopify, Etsy, Google/Merchant Center.
- Add **brand-specific context agents/workflows** for Aydins, Theonar, and Amazing Wedding Bands.
- Add a **Thunder Returns content/outreach agent** because it is SaaS, not jewelry ecommerce.
- Add a dedicated **Duplicate Content Guardrail workflow** that reviews cross-brand copy before anything is published.
- Add a dedicated **Instagram Content workflow per brand**, not one shared social workflow.

This is slower than cloning stores. Good. Cloning is the risk.

---

## 1. Updated Agent Map

### 1.1 Core Command Agent

| Agent | Brand served | Model | What it does | Not allowed to do |
|---|---|---:|---|---|
| **BETA** | All brands | GPT-5.5 via Codex OAuth, fallback DeepSeek V3.2 | Command center, final synthesis, approval routing, project memory, task prioritization, rollout planning, high-risk decision review | Cannot publish, delete, spend money, send customer/outreach messages, change prices, create stores, buy themes/apps, or bulk-edit without Amir approval |

### 1.2 Current Specialist Agents

| Agent | Brand served | Model | What it does | Not allowed to do |
|---|---|---:|---|---|
| **BETA SHOP** | Primarily Aydins; can advise Shopify patterns for all brands when given brand brief | DeepSeek V3.2 | Shopify theme QA, listing/page audits, product copy drafts, storefront launch checks, app/theme recommendations | Cannot publish themes, bulk edit live products, install apps, change pricing, change policies, or reuse Aydins copy for other brands |
| **BETA ETSY** | Aydins/Theonar/AWB Etsy workflows when instructed | DeepSeek V3.2 | Etsy SEO, listing drafts, tag strategy, Vela CSV prep, Etsy revamp planning | Cannot push Etsy changes, publish listings, reuse Shopify copy verbatim, message buyers, or change prices without approval |
| **BETA GOOGLE** | All brands, separated per property/account | DeepSeek V3.2 | Merchant Center, GA4, Search Console, disapproval triage, SEO risk checks | Cannot modify Merchant Center settings, connect properties, submit feeds, change tracking, or consolidate data across brands without approval |

### 1.3 Recommended New Brand/Workflow Agents

These do not need to be separate always-on autonomous personalities at first. Start as controlled workflow profiles. Promote to persistent agents only when volume justifies it.

| Agent / Workflow | Brand served | Model | What it does | Not allowed to do |
|---|---|---:|---|---|
| **AYDINS BRAND OPS** | Aydins Jewelry | DeepSeek V3.2 for routine, BETA review for final | Aydins-specific product copy, collection content, homepage/social voice, launch QA aligned to existing brand | Cannot write Theonar/AWB copy, cannot alter live Shopify without approval, cannot weaken Aydins trust/policy language |
| **THEONAR BRAND OPS** | Theonar | DeepSeek V3.2 | Theonar Etsy revamp, new Shopify content architecture, minimalist/modern brand voice, product/collection drafts | Cannot copy Aydins/AWB content structure, cannot create Shopify account, buy theme, publish Etsy/Shopify listings, or cross-post content |
| **AWB BRAND OPS** | Amazing Wedding Bands | DeepSeek V3.2 | AWB Shopify build planning, broad-accessible wedding band positioning, product/category/campaign drafts | Cannot copy Aydins/Theonar, cannot create Shopify account, buy theme, publish products, or use identical imagery/captions |
| **THUNDER CONTENT OPS** | Thunder Returns | DeepSeek V3.2 | SaaS content calendar, social posts, founder-led posts, outreach drafts, landing-page copy drafts | Cannot send outreach/emails/DMs, make product claims without review, publish posts, or contact brands without approval |
| **DUPLICATE CONTENT GUARD** | Aydins, Theonar, AWB | DeepSeek V3.2 + BETA final review | Cross-brand comparison for product copy, collection pages, metadata, FAQ, schema, blog topics, Instagram captions | Cannot approve its own work for publishing; only flags risk and recommends rewrites |
| **INSTAGRAM PLANNER — AYDINS** | Aydins | DeepSeek V3.2 | Aydins IG calendar, captions, image direction, post/reel concepts | Cannot post, schedule, reuse Theonar/AWB/Thunder assets, or use customer photos without permission |
| **INSTAGRAM PLANNER — THEONAR** | Theonar | DeepSeek V3.2 | Minimalist Theonar IG calendar, visual direction, captions | Cannot post, schedule, reuse Aydins/AWB assets, or use customer photos without permission |
| **INSTAGRAM PLANNER — AWB** | Amazing Wedding Bands | DeepSeek V3.2 | Value/convenience-driven IG calendar, captions, creative briefs | Cannot post, schedule, reuse Aydins/Theonar assets, or use customer photos without permission |
| **INSTAGRAM PLANNER — THUNDER** | Thunder Returns | DeepSeek V3.2 | B2B SaaS social content, carousel ideas, founder posts, short-form scripts | Cannot post, schedule, send DMs, make unsupported ROI claims, or scrape private data |

### 1.4 Structure Recommendation

Use a **hybrid structure**:

1. **Shared platform specialists** for Shopify/Etsy/Google mechanics.
2. **Separate brand ops profiles** for brand voice, copy, visual direction, SEO strategy, and social.
3. **One Duplicate Content Guard** that checks all three jewelry stores before publishing.

Why this is best:

- Shopify mechanics can be shared.
- Brand voice cannot be shared.
- SEO strategy cannot be shared blindly.
- Instagram cannot be shared without rewrite/redesign.
- A single approval gate prevents accidental publishing/spend.

---

## 2. Brand Identity Briefs

## 2.1 Aydins Jewelry Brand Brief

### Brand name
**Aydins Jewelry**

### Positioning
Aydins is the established, trusted men’s wedding band specialist: premium, editorial, craftsman-forward, and built around confidence. It should feel like the safest high-quality choice for a man who wants a ring with character but does not want to overthink the buying process.

Aydins is the “heritage operator” brand of the group: since 2011, real support, deep catalog, strong trust signals.

### Target customer persona
- Male buyer, 25–45, engaged or replacing/upgrading a ring
- Partner/spouse shopping for him
- Wants something masculine, durable, and memorable
- Values warranty, shipping speed, engraving, size help, and easy exchanges
- Likes materials with story: tungsten, Damascus, meteorite, dinosaur bone, wood, carbon fiber

### Brand voice and tone
- Polished, masculine, direct
- Trustworthy, not hype-heavy
- Editorial/craftsman language
- Confident but not luxury-snobby
- Short, mobile-friendly paragraphs

Example voice: “Built for daily wear. Chosen for the story behind the material.”

### Visual direction
- Colors: warm black, ivory, brass/gold accent, dark charcoal, warm brown
- Fonts: elegant serif for headlines, clean sans-serif for body
- Photography: dramatic macro shots, textured backgrounds, dark leather, stone, wood, warm lighting
- Layout: editorial homepage blocks, trust strips, material cards, product storytelling

### Content style
- Descriptions emphasize material story, comfort, durability, engraving, warranty
- Collection pages feel like buying guides with authority
- Social content mixes product beauty, material education, buyer confidence, and trust proof
- Aydins can own “we know men’s wedding bands” authority

### SEO keyword strategy
Primary territory:
- men’s wedding bands
- tungsten wedding bands
- Damascus steel rings
- meteorite rings
- dinosaur bone rings
- wood inlay rings
- carbon fiber wedding bands
- engraved men’s wedding bands

Aydins should target the broad, high-intent category keywords and material authority terms because it has age, catalog depth, and trust.

---

## 2.2 Theonar Brand Brief

### Brand name
**Theonar**

### Positioning
Theonar should be the minimalist, modern, design-led wedding band brand. It should feel completely different from Aydins: cleaner, quieter, more architectural, less “rugged craftsman,” more “modern object of commitment.”

Theonar’s angle: **refined rings for men who want restraint, precision, and modern design.**

It should not present as a massive catalog warehouse. It should feel curated.

### Target customer persona
- Design-conscious buyer, 25–40
- Urban/suburban professional
- Likes Apple, Muji, watches, architecture, minimal interiors
- Wants a ring that feels understated, not loud
- May prefer black, brushed, satin, beveled, low-profile, monochrome styles
- Values clean sizing guidance, simple policies, and no clutter

### Brand voice and tone
- Minimal, calm, precise
- Sparse but premium
- Less emotional storytelling, more design clarity
- No rugged clichés
- No Aydins-style “forged” or heavy heritage language

Example voice: “Clean lines. Balanced weight. Built for every day.”

### Visual direction
- Colors: off-white, graphite, soft gray, matte black, muted steel, one restrained accent such as sand or slate blue
- Fonts: modern sans-serif, maybe geometric/neo-grotesk; avoid ornate serif-heavy look
- Photography: bright neutral backgrounds, sharp shadows, concrete, linen, brushed metal, clean hand shots
- Layout: airy spacing, fewer products per section, minimalist cards, strong filtering, less copy density

### Content style
- Product descriptions focus on shape, finish, fit, profile, proportion, and daily wear
- Collection pages should be concise and design-led, not long heritage essays
- Social posts should feel like a modern design brand: negative space, close crops, quiet captions
- Educational content: ring profiles, finishes, widths, comfort fit, how to choose a minimal band

### SEO keyword strategy
Primary territory:
- minimalist men’s wedding bands
- modern wedding bands for men
- black minimalist wedding band
- brushed tungsten ring
- matte black wedding band
- simple men’s wedding ring
- low profile wedding band
- comfort fit minimalist ring

Theonar should avoid competing head-on with Aydins for every broad material keyword. It can use material keywords but framed through design intent: minimalist tungsten, modern black bands, brushed finish, clean profile.

---

## 2.3 Amazing Wedding Bands Brand Brief

### Brand name
**Amazing Wedding Bands**

### Positioning
Amazing Wedding Bands should be the accessible, high-convenience, value-forward brand. It should not feel like Aydins’ editorial premium voice or Theonar’s minimalist design studio.

AWB’s angle: **the easiest place to find a great men’s wedding band without overpaying or getting overwhelmed.**

It should feel approachable, clear, deal-aware, and helpful.

### Target customer persona
- Practical buyer, 24–50
- Wants a good-looking ring fast
- Price-conscious but not looking for junk
- May be planning a wedding on a budget
- Wants simple categories, easy comparison, strong shipping/return reassurance
- Responds to “best under $200,” “top-rated,” “durable,” “easy exchange” messaging

### Brand voice and tone
- Friendly, clear, direct
- Benefit-first, less poetic
- Helpful shopping-guide language
- More “find the right ring fast” than luxury storytelling
- Avoid sounding cheap; use “smart value,” not bargain-bin language

Example voice: “Great bands. Clear prices. Easy sizing.”

### Visual direction
- Colors: white, navy, silver, soft gold, light gray, maybe a confident blue accent
- Fonts: clean commerce sans-serif; readable, modern, friendly
- Photography: brighter product grids, lifestyle hand shots, wedding-day practical imagery, comparison graphics
- Layout: conversion-first, strong category tiles, price filters, comparison tables, badges, reviews

### Content style
- Product descriptions focus on durability, comfort, value, shipping, sizing, and why it is a smart pick
- Collection pages should be shopping assistants: “Best for budget,” “Best black bands,” “Best low-maintenance rings”
- Social posts should be practical: top picks, price ranges, ring finder quizzes, before/after engraving, FAQs

### SEO keyword strategy
Primary territory:
- affordable men’s wedding bands
- best men’s wedding bands
- wedding bands under 200
- tungsten rings under 200
- durable men’s wedding rings
- black wedding bands for men affordable
- best wedding rings for men
- cheap men’s wedding bands should be used carefully; prefer “affordable” and “best value”

AWB should target practical shopping-intent keywords and price/value modifiers. This keeps it distinct from Aydins’ authority/material strategy and Theonar’s minimalist/design strategy.

---

## 3. Duplicate Content Prevention Rules

### 3.1 Product Description Rules

For the same vendor ring across multiple stores:

- Do not reuse the same title structure.
- Do not reuse the same opening sentence.
- Do not reuse the same bullet sequence.
- Do not reuse the same “why this ring” angle.
- Do not reuse the same FAQ answers.
- Do not reuse the same meta title or meta description.
- Do not reuse identical alt text.

Per-brand rewrite rules:

- **Aydins:** material story + daily wear + trust/warranty + engraving.
- **Theonar:** design profile + finish + proportions + minimal styling.
- **AWB:** value + durability + easy sizing + fast decision help.

Minimum uniqueness standard:

- Product body copy should be independently written per brand.
- Same specs can match because facts are facts: width, material, comfort fit, engraving availability, sizing.
- Explanatory copy around those facts must differ.

### 3.2 Collection Page Rules

Each brand gets different collection architecture.

Aydins collection structure:
- By material: Tungsten, Damascus, Meteorite, Dinosaur Bone, Wood, Carbon Fiber
- By style: Black, Rose Gold, Celtic, Engraved, Best Sellers
- By trust/use case: Best Sellers, New Arrivals, Custom Rings

Theonar collection structure:
- By design: Minimal, Matte, Brushed, Black, Two-Tone, Low Profile
- By profile: Flat, Domed, Beveled, Stepped Edge
- By finish: Satin, Polished, Brushed, Sandblasted

AWB collection structure:
- By shopping need: Under $200, Best Value, Top Rated, Fast Shipping, Easy Exchange Picks
- By material simplified: Tungsten, Titanium, Black Bands, Wood Inlay, Unique Rings
- By buyer: For Him, For Couples, Budget-Friendly, Premium Picks

Collection copy must differ by brand:

- Aydins = authority and material storytelling.
- Theonar = design clarity and restraint.
- AWB = shopping guidance and practical comparison.

### 3.3 Meta Title and Description Rules

No shared meta templates across stores.

Examples:

- Aydins: “Damascus Steel Rings for Men | Aydins”
- Theonar: “Modern Damascus Wedding Bands with Clean Profiles | Theonar”
- AWB: “Best Damascus Wedding Bands for Men at Great Prices | AWB”

Meta descriptions must use different angles:

- Aydins: material + craftsmanship + warranty
- Theonar: design + finish + fit
- AWB: price/value + durability + sizing help

### 3.4 FAQ Rules

FAQs must not be copied across brands.

Allowed shared facts:
- Tungsten is durable.
- Comfort fit is easier to wear.
- Engraving availability depends on design.
- Returns/exchanges follow policy.

Required differentiation:

- Aydins FAQs answer like a specialist jeweler.
- Theonar FAQs answer like a design studio.
- AWB FAQs answer like a practical shopping assistant.

### 3.5 Schema Markup Rules

Schema can use the same technical types, but content should differ.

Allowed common schema types:
- Product
- CollectionPage
- FAQPage
- BreadcrumbList
- Organization
- WebSite

Required differences:
- Organization names and URLs must be separate.
- FAQ question/answer text must be brand-specific.
- CollectionPage descriptions must be unique.
- Product descriptions in schema must match each brand’s unique product copy.
- SameAs social links must point only to that brand’s accounts.

### 3.6 Theme Strategy

Do **not** use the same Shopify theme across all three stores.

Recommended:

- **Aydins:** Continue Kalles v5 path if final QA passes.
- **Theonar:** Use a minimalist premium theme with strong typography and whitespace.
- **AWB:** Use a conversion/category-focused theme built for filtering, merchandising, and quick comparison.

Different themes reinforce visual separation and reduce clone risk.

### 3.7 Image Strategy

Supplier photos can be used as raw assets, but the presentation should differ.

Rules:

- Do not use the exact same hero images across brands.
- Do not use the exact same homepage/category image crops across brands.
- Do not use the same lifestyle mockups with only logo/color swaps.
- Product gallery overlap is acceptable only when unavoidable, but first image/crop/order should differ where possible.
- Each brand needs unique image treatment:
  - Aydins: dark editorial, macro material texture.
  - Theonar: neutral minimalist, clean backgrounds, architectural crops.
  - AWB: bright commerce, comparison/product clarity, value badges.

Long-term recommendation:
- Build a shared raw asset library.
- Export brand-specific crops/backgrounds/overlays per store.
- Track image usage by SKU and brand.

### 3.8 Blog and Topical Authority Rules

Each brand needs a different content moat.

Aydins blog/content moat:
- Material authority
- Men’s wedding band guides
- Engraving and warranty confidence
- Deep educational material pages

Theonar content moat:
- Minimalist design
- Ring profiles and proportions
- Finish guides
- Modern wedding styling
- How to choose a simple ring that still feels premium

AWB content moat:
- Buying guides by budget
- Best rings under price thresholds
- Comparison posts
- Practical wedding planning ring advice
- Fast decision guides

No article should be rewritten lightly and posted across all three. If the same topic must exist, the angle, structure, examples, title, images, and target keyword must be different.

---

## 4. Shopify Setup Checklist — Theonar and Amazing Wedding Bands

## 4.1 Theonar Shopify Setup

### Theme recommendation
Use a minimalist premium Shopify theme, not Kalles.

Recommended theme direction:
- Clean product pages
- Strong typography
- Excellent mobile spacing
- Minimal visual clutter
- Strong filtering but not marketplace-like

Candidate styles to evaluate before purchase:
- **Prestige** style direction for premium minimal commerce
- **Symmetry** style direction for polished catalog control
- **Impulse** only if configured very minimally

Final theme purchase requires Amir approval.

### Shopify plan recommendation
Start with **Basic Shopify** unless launch needs advanced reports, multiple staff permissions, or custom checkout requirements. Upgrade later only if revenue justifies it.

### App stack
Keep app stack lean.

Required/likely:
- Search/filter app if theme filtering is not enough
- Reviews app
- Email/SMS capture app, likely Klaviyo if brand warrants it
- Personalization/engraving app if needed
- Google & YouTube app
- Feed optimization app only if native feed is insufficient
- SEO/image compression app only if theme/assets need it

Avoid app bloat before launch.

### Domain setup steps
1. Confirm domain ownership and registrar access.
2. Create Shopify account only after approval.
3. Connect domain to Shopify.
4. Set primary domain.
5. Enable SSL.
6. Configure branded email forwarding/sender domain.
7. Verify domain in Google Search Console.
8. Verify domain in Merchant Center.
9. Confirm redirects and canonical behavior.

### Google Merchant Center
- Separate Merchant Center account for Theonar.
- Separate business profile/details.
- Separate shipping/returns settings.
- Separate product feed.
- Separate policy wording.
- Do not reuse Aydins feed descriptions.

### Google Analytics
- Separate GA4 property.
- Separate Google Tag Manager container if GTM is used.
- Separate Search Console property.
- Separate conversion events.
- No blended reporting unless a separate dashboard pulls summaries.

### Shipping and returns policy
Same actual policy can be used, but wording must be different.

Theonar policy tone:
- Minimal, clear, calm
- Fewer marketing claims
- Simple headings
- Plain-language process

---

## 4.2 Amazing Wedding Bands Shopify Setup

### Theme recommendation
Use a conversion-focused, category-friendly theme, not Kalles and not Theonar’s theme.

Recommended theme direction:
- Strong collection filtering
- Comparison-friendly product cards
- Trust badges
- Promo banners
- Fast mobile shopping
- Clear price/category navigation

Candidate styles to evaluate before purchase:
- **Impulse** for merchandising and promotions
- **Broadcast** for conversion/story balance
- **Empire** only if catalog scale and filtering justify it

Final theme purchase requires Amir approval.

### Shopify plan recommendation
Start with **Basic Shopify**. Upgrade only if analytics/staff/API needs justify it.

### App stack
Required/likely:
- Product filter/search app if native is insufficient
- Reviews app
- Email capture/Klaviyo or lighter alternative
- Engraving/personalization app if needed
- Google & YouTube app
- Feed optimizer if Merchant Center needs stronger attribute control
- Bundles/upsell app only after traffic proves demand

### Domain setup steps
1. Confirm domain ownership and registrar access.
2. Create Shopify account only after approval.
3. Connect domain.
4. Set primary domain.
5. Enable SSL.
6. Configure branded sender domain.
7. Verify Search Console.
8. Verify Merchant Center.
9. QA redirects/canonicals.

### Google Merchant Center
- Separate Merchant Center account for AWB.
- Separate feed copy.
- Separate shipping/return settings.
- Separate brand identity.
- Avoid duplicate product descriptions from Aydins/Theonar.

### Google Analytics
- Separate GA4 property.
- Separate GTM container if used.
- Separate Search Console.
- Separate conversion tracking.

### Shipping and returns policy
Same actual policy can be used, but copy should match AWB’s practical voice.

AWB policy tone:
- Clear, friendly, practical
- “Here’s how it works” structure
- Emphasize easy shopping and support without overpromising

---

## 5. Instagram Workflow Per Brand

## 5.1 Aydins Instagram Workflow

### Posting frequency target
- 4 feed posts/week
- 2–3 reels/week
- 3–5 story frames/week

### Content types
- Material closeups
- Best sellers
- Engraving examples
- Customer-style stories with permission
- Ring education
- Warranty/trust proof
- Behind-the-scenes support/process content

### Visual style
- Dark editorial
- Warm metals
- Macro texture
- Leather/stone/wood backgrounds
- Premium masculine feel

### Caption voice
- Direct, confident, material/story-led
- Short hooks
- Trust-forward CTA

### Hashtag strategy
- Mix of category + material + occasion
- Examples: #MensWeddingBands, #TungstenRing, #DamascusRing, #MeteoriteRing, #WeddingBandInspo, #EngravedRing
- Avoid spammy 30-tag blocks

### Approval workflow
1. Agent drafts content calendar.
2. Agent drafts caption + image/reel direction.
3. Duplicate Content Guard checks against Theonar/AWB.
4. Amir approves.
5. Only after approval may content be scheduled/posting prepared.

### Can do
Draft, suggest, organize calendar, create shot lists, write caption options.

### Cannot do
Post without approval, use customer photos without permission, reuse other brand captions/images, make unsupported claims.

---

## 5.2 Theonar Instagram Workflow

### Posting frequency target
- 3 feed posts/week
- 2 reels/week
- 3 story frames/week

### Content types
- Minimal product crops
- Finish/profile education
- Width comparison graphics
- Modern wedding styling
- Quiet design-led reels
- Ring selection tips for minimalists

### Visual style
- Neutral backgrounds
- Negative space
- Matte textures
- Concrete/linen/brushed metal
- Clean shadows

### Caption voice
- Sparse, refined, design-focused
- No hype
- No Aydins-style rugged language

### Hashtag strategy
- Design/minimal/category mix
- Examples: #MinimalistWeddingBand, #ModernWeddingBand, #MensRingStyle, #MatteBlackRing, #BrushedTungsten, #SimpleWeddingBand

### Approval workflow
1. Theonar planner drafts post concept.
2. Image direction must be Theonar-specific.
3. Caption checked against Aydins/AWB for overlap.
4. Amir approves before posting/scheduling.

### Can do
Draft calendars, captions, visual briefs, reel scripts.

### Cannot do
Post, schedule, reuse Aydins/AWB images as-is, copy product descriptions into captions, use customer photos without permission.

---

## 5.3 Amazing Wedding Bands Instagram Workflow

### Posting frequency target
- 4 feed posts/week
- 2 reels/week
- 4 story frames/week

### Content types
- Best rings under price points
- Top 5 lists
- Ring finder quizzes
- Customer review-style graphics with permission
- Durability/value education
- Wedding planning tips
- Fast comparison posts

### Visual style
- Bright, clean, helpful
- Product-first
- Navy/white/silver/gold accent
- Comparison cards
- Price/value badges without looking cheap

### Caption voice
- Friendly, practical, shopping-assistant tone
- Clear CTA
- Less poetic, more useful

### Hashtag strategy
- Value + shopping intent
- Examples: #AffordableWeddingBands, #MensWeddingRings, #WeddingPlanningTips, #BestWeddingBands, #TungstenWeddingBand, #WeddingBudget

### Approval workflow
1. AWB planner drafts calendar.
2. Content marked by buyer intent: budget, style, durability, sizing.
3. Duplicate Content Guard checks against Aydins/Theonar.
4. Amir approves.
5. Post/schedule only after approval.

### Can do
Draft, suggest, build content buckets, create comparison ideas.

### Cannot do
Post without approval, reuse other brand assets, make fake discount claims, use customer photos without permission.

---

## 5.4 Thunder Returns Instagram Workflow

### Posting frequency target
- 3 feed/LinkedIn-style posts per week adapted for IG
- 2 reels/short videos per week
- 3–5 story frames/week

### Content types
- Returns pain points for jewelry brands
- Founder build-in-public updates
- Mini case studies with permission
- Product feature explainers
- Operational tips
- Myth-busting returns/exchanges
- Before/after return flow examples

### Visual style
- SaaS clean
- Dark navy/black/white/electric accent
- UI screenshots/mockups
- Simple diagrams
- Founder/operator tone

### Caption voice
- B2B direct
- Operator-to-operator
- Practical, not corporate
- Pain/problem/solution framing

### Hashtag strategy
- B2B ecommerce/SaaS mix
- Examples: #ShopifyBrands, #EcommerceReturns, #JewelryBusiness, #DTCBrands, #ReturnsManagement, #SaaSFounder

### Approval workflow
1. Thunder planner drafts post/caption/script.
2. Claims reviewed for accuracy.
3. Amir approves.
4. No posting or outreach without approval.

### Can do
Draft content, suggest hooks, write scripts, prepare outreach drafts.

### Cannot do
Post, DM prospects, send emails, claim metrics without evidence, name brands/customers without permission.

---

## 6. Permission Rules for All New Workflows

These are hard rules across every brand and every agent.

### Publishing and changes
- No publishing without Amir approval.
- No Shopify theme publishing without Amir approval.
- No product/listing publishing without Amir approval.
- No Etsy publishing without Amir approval.
- No blog publishing without Amir approval.
- No Instagram posting or scheduling without Amir approval.

### Destructive actions
- No deleting anything.
- No removing products, listings, pages, collections, files, images, menus, redirects, or accounts without approval.
- No overwriting live data without backup and approval.

### Customer/prospect communication
- No customer messages without approval.
- No prospect emails without approval.
- No Instagram DMs without approval.
- No support replies without approval.
- No outreach sequences launched without approval.

### Money and account actions
- No ad spend without approval.
- No price changes without approval.
- No purchases: themes, Shopify plans, domains, apps, subscriptions, plugins, services.
- No account creation unless Amir explicitly approves.
- No payment method changes.

### Bulk work
- No bulk edits unless previewed first.
- Bulk changes require sample approval, backup, and post-change verification.
- Every bulk workflow must produce a rollback note or backup location.

### Content separation
- No cross-posting content between brands.
- No same caption with logo swap.
- No same homepage copy with brand swap.
- No same product description across stores.
- No same collection intro across stores.
- No same FAQ answer blocks across stores.
- No customer photos unless usage permission is confirmed.

### Logging
Every automated task must log:
- Date/time
- Brand
- Agent/workflow
- Input/source data
- Draft output or changed files
- Whether anything was applied
- Approval status
- Verification result

---

## 7. Phased Rollout Plan

## Phase 1 — Guardrails and Planning Foundation

### Recommendation
Build the rules before building the machine.

### What to build first
1. Finalize this multi-brand plan after Amir review.
2. Create brand context files:
   - `projects/AYDINS.md` already exists and should remain source for Aydins.
   - `projects/THEONAR.md`
   - `projects/AMAZING-WEDDING-BANDS.md`
   - `projects/THUNDER-RETURNS.md` already exists and should be expanded for content/social.
3. Create a Duplicate Content Guard checklist/workflow.
4. Create approval templates:
   - Shopify change approval
   - Etsy listing approval
   - Instagram post approval
   - Outreach/email approval
5. Finish Aydins Shopify preview theme QA before any new-store work.

### Timeline estimate
**2–4 days** after approval.

### Success criteria
- Brand briefs locked.
- Permission rules locked.
- Aydins preview theme has a clean publish/no-publish verdict.
- No new store work starts until the guardrails are in place.

---

## Phase 2 — Theonar First, Because It Already Has Etsy

### Why Theonar first
Theonar has an existing Etsy store. That means there is already marketplace presence and likely faster revenue impact than launching AWB from zero.

### Scope
1. Audit Theonar Etsy store.
2. Draft Theonar Etsy revamp plan.
3. Build Theonar Shopify architecture plan:
   - Theme shortlist
   - Collection map
   - Homepage wireframe
   - Product template direction
   - SEO keyword map
   - Instagram visual/caption system
4. Prepare first 10–20 Theonar product/listing drafts.
5. Run Duplicate Content Guard against Aydins.

### What is not included without approval
- No Shopify account creation.
- No theme purchase.
- No Etsy publishing.
- No domain changes.
- No Merchant Center creation.

### Timeline estimate
**1–2 weeks** for planning, copy system, Etsy revamp drafts, and Shopify blueprint.

### Success criteria
- Theonar feels like a different company from Aydins.
- Etsy revamp drafts ready for review.
- Shopify build plan ready for approval.
- Instagram month-one calendar drafted.

---

## Phase 3 — Amazing Wedding Bands Build Plan + Thunder Content Engine

### AWB scope
1. Finalize AWB brand positioning.
2. Theme shortlist and Shopify architecture.
3. Collection strategy based on value/practical shopping.
4. Product copy templates.
5. Instagram calendar.
6. Merchant Center/GA4 setup plan.
7. Duplicate Content Guard against Aydins and Theonar.

### Thunder scope
1. Create Thunder Returns content pillars.
2. Draft 30-day social calendar.
3. Draft founder-led post templates.
4. Draft short-form video scripts.
5. Draft outreach message library for approval.

### Timeline estimate
**2–3 weeks** after Phase 2 planning is stable.

### Success criteria
- AWB is clearly differentiated from Aydins and Theonar.
- Thunder has a consistent B2B content engine.
- No cross-brand content reuse.
- Approval queue is manageable.

---

## Phase 4 — Full Operation

### Scope
Once guardrails and brand systems are proven:

- Weekly Aydins Shopify/SEO QA
- Weekly Theonar Etsy/Shopify build queue
- Weekly AWB build queue
- Weekly Thunder content/outreach queue
- Monthly Duplicate Content Guard audit
- Monthly SEO cannibalization check across wedding band brands
- Monthly Instagram calendar review for all four brands
- Monthly dashboard summary

### Timeline estimate
**4–8 weeks** to reach stable full operation after Phase 1 approval.

### Success criteria
- Each brand has distinct identity.
- No duplicate-content drift.
- No unapproved publishing.
- Every task is logged.
- Amir reviews decisions, not raw chaos.

---

## 8. Approval Gates Before Any Implementation

Before implementation begins, Amir must approve:

1. Agent/workflow structure.
2. Brand positioning for Theonar.
3. Brand positioning for AWB.
4. Duplicate content prevention rules.
5. Theme direction for Theonar.
6. Theme direction for AWB.
7. Instagram workflow rules.
8. Permission rules.
9. Phase 1 start.

No implementation should begin from this document alone. This is a draft operating plan, not execution authorization.

---

## 9. Immediate Next Action

Amir reviews this document and decides one of three paths:

1. **Approve Phase 1 only** — build guardrails/context files/checklists, no stores.
2. **Revise brand positioning** — adjust Theonar/AWB identities before any build.
3. **Pause expansion** — finish Aydins Shopify launch first, then return to this plan.

Recommended path: **Option 1 after Aydins preview theme is publish-safe.**
