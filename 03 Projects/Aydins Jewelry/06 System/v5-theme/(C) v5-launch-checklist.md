# Kalles v5 Launch Checklist

> **Created:** 2026-05-09
> **Target launch:** Sunday 2026-05-10 EOD
> **Status:** Pre-launch — work this list top-down before flipping the switch
> **Themes involved:**
> - Live: `kalles-4-2-1-official` (v4)
> - Preview to launch: `kalles-v5-4-0-official` (v5, ID 159068061933)

---

## How to use this list

1. Walk Tier 1 to Tier 7 in order. Lower tiers depend on higher ones working.
2. For each item: **check it on v5 preview, mark ✅ or ❌, paste any error in the Notes column.**
3. Do NOT publish v5 until every Tier 1 + Tier 2 item is ✅.
4. Tier 5+ items can be fixed post-launch if needed (note them, don't block).
5. When done, run the **Pre-Flight** section before publishing.

---

## TIER 1 — Revenue Critical
> *If any of these are broken, you lose sales the moment v5 goes live.*

| # | Item | How to Check | Status | Notes |
|---|---|---|---|---|
| 1.1 | Add to Cart works on standard PDP | Open a normal ring PDP → select size → click ATC → cart updates | | |
| 1.2 | Add to Cart works on personalized PDP | PDP with Zepto engraving → fill personalization → ATC → properties save in cart | | |
| 1.3 | Cart page loads | `/cart` renders, items show, quantity editable, remove works | | |
| 1.4 | Cart drawer opens (if used) | Click cart icon → drawer slides in → contents correct | | |
| 1.5 | Discount code applies in cart | Enter test code → see discount line | | |
| 1.6 | Shipping calculator works | Cart → shipping options → see correct rates per country | | |
| 1.7 | Checkout completes | Test order with real card on `?preview_theme_id=159068061933` → buy a $1 product → confirm order in admin | | |
| 1.8 | Shop Pay button fires | On PDP and cart — clicking Shop Pay opens express checkout | | |
| 1.9 | Out-of-stock variants greyed out | Find a sold-out size → confirm it's disabled, not buyable | | |
| 1.10 | Variant switching works | Change size/width → URL updates, image switches, price updates | | |
| 1.11 | Personalizer renders on all engraving types | Test 3 PDPs: inside-only ring, inside+outside ring, non-engravable product | | |
| 1.12 | Personalizer properties pass to checkout | After ATC with engraving → in cart, see "Laser Engraving Options: Inside" line item | | |

**Pause gate:** Don't proceed until 1.1–1.12 are all ✅.

---

## TIER 2 — Tracking & Attribution
> *If broken, sales still happen but you lose all ad attribution and remarketing data. Hidden bleed.*

| # | Item | How to Check | Status | Notes |
|---|---|---|---|---|
| 2.1 | GA4 / Shopify Analytics fires | Open v5 PDP → DevTools Network tab → filter `analytics.shopify` and `google-analytics` → see beacon hits | | |
| 2.2 | Google Ads conversion script | Test order → check Network for `googleadservices` or `gtag` calls on confirmation page | | |
| 2.3 | Bing UET pixel fires | v4 theme.liquid has inline UET (`bat.bing.com/bat.js`) — confirm v5 also has it. If not, copy the `<script>` block from v4 theme.liquid lines ~145-160 into v5 theme.liquid | | |
| 2.4 | Bing UET PRODUCT_PURCHASE event | Test order → on confirmation, Network tab → `bat.bing.com` event with revenue value | | |
| 2.5 | Klaviyo Active On Site fires | v5 PDP → Network → `klaviyo` → see `metric` calls | | |
| 2.6 | Klaviyo "Viewed Product" event | Same — check `Viewed Product` metric fires on PDP | | |
| 2.7 | Klaviyo "Added to Cart" event | ATC on v5 → Klaviyo `Added to Cart` event fires | | |
| 2.8 | Klaviyo signup forms render & submit | Footer/popup signup form → enter email → see in Klaviyo profiles | | |
| 2.9 | Google Customer Reviews opt-in shows post-purchase | v4 has GCR opt-in inline (lines after `</body>`). Confirm v5 has equivalent — needed for review collection | | |
| 2.10 | Google Merchant Widget renders | Bottom-right floating widget on PDP — `merchantwidget.js` should load | | |

**Pause gate:** Don't proceed until 2.1–2.10 are all ✅ or you've consciously decided to launch without specific items.

---

## TIER 3 — Apps & Snippets Migration
> *v4 theme.liquid loads these. v5's stripped-down theme.liquid may be missing some. Each one = a feature that may silently not work.*

| # | App / Snippet | v4 location | v5 status | Action if missing |
|---|---|---|---|---|
| 3.1 | Bold Product Options | `{% render 'bold-options-hybrid' %}` + `{% render 'bold-common' %}` in v4 head | Search v5 theme.liquid + snippets folder | Re-install Bold app on v5 OR copy snippets from v4 |
| 3.2 | SC includes (Shop Circle) | `{% render 'sc-includes' %}` in v4 head | Search v5 | Copy snippet from v4 OR re-install app on v5 |
| 3.3 | Delivery date display | `{% render 'delivery_coder' %}` in v4 head | Search v5 — this is what powers the May 11-12 / May 12-15 delivery box on PDP | Copy snippet from v4 if missing |
| 3.4 | Loox reviews — head | `{{ shop.metafields.loox["global_html_head"] }}` in v4 head | Confirm v5 head includes this metafield render | Add the metafield render line to v5 theme.liquid |
| 3.5 | Loox reviews — body | `{{ shop.metafields.loox["global_html_body"] }}` near bottom of v4 body | Confirm v5 body includes it | Add to v5 theme.liquid |
| 3.6 | SchemaApp JSON-LD | v4: full conditional block ~`{% if template.name == 'product' %}` etc. v5: comment in theme.liquid says "migrated from v4" | Confirm SchemaApp metafield JSON-LD actually outputs on v5 PDP — view source, search for `application/ld+json` | If missing, re-paste the v4 conditional block |
| 3.7 | spdn snippet | `{% render 'spdn' %}` in v4 head | Find out what this app is, confirm v5 status | Likely safe to skip if you don't know what it is — but verify |
| 3.8 | Custom FAQ schema | v4 head: `{% if product.metafields.custom.faq_schema %}` JSON-LD output | Confirm v5 head has it | Copy block from v4 |
| 3.9 | Source.js | v4 body: `{{'source.js' | asset_url | script_tag }}` | Confirm v5 has this asset and loads it | Copy file from v4 assets to v5, add script tag |
| 3.10 | Recart (saw error in console earlier) | Recart 404 in v5 console — confirm Recart still installed/active | Either re-install Recart OR uninstall cleanly so it stops 404'ing | |

**Pause gate:** Each missing app = a feature that won't work. Acceptable to launch with some Tier 3 items broken if they're non-critical (e.g. spdn) but you must KNOW what's broken.

---

## TIER 4 — SEO
> *Won't break sales today, but will tank rankings if missed.*

| # | Item | How to Check | Status | Notes |
|---|---|---|---|---|
| 4.1 | Custom canonical URL logic preserved | v4 has the `preferred_path` block stripping `/en-XX` locale prefixes — confirm v5 has the same. View source on a PDP → check `<link rel="canonical">` matches the clean URL | | |
| 4.2 | Meta title outputs | View source on 3 different page types (PDP, collection, blog) → confirm `<title>` is correct, not generic | | |
| 4.3 | Meta description outputs | Same — `<meta name="description">` populated | | |
| 4.4 | Open Graph tags present | View source → `<meta property="og:title">` etc. — needed for social sharing | | |
| 4.5 | robots.txt accessible | `/robots.txt` returns 200 with sitemap line | | |
| 4.6 | sitemap.xml accessible | `/sitemap.xml` returns 200, products listed | | |
| 4.7 | hreflang tags (if multi-region) | View source → `<link rel="alternate" hreflang="...">` if you serve EU/CA/UK | | |
| 4.8 | No `noindex` on production pages | View source → confirm no `<meta name="robots" content="noindex">` on shippable PDPs (only allowed on hidden products with `_HIDDEN_` type) | | |

---

## TIER 5 — Brand & Design Polish
> *Already covered by `aydins-design.css` and Zepto v8 CSS. Verify on key surfaces.*

| # | Item | How to Check | Status | Notes |
|---|---|---|---|---|
| 5.1 | Aydins palette renders | Bone background, Ink text, no red sale prices, no shadows on cards, brass accents only on focus moments | | |
| 5.2 | Poppins + Cormorant fonts load | Headings serif (Cormorant), body sans (Poppins) — DevTools → Computed → font-family | | |
| 5.3 | Logo correct | Header shows correct Aydins logo, not Kalles default | | |
| 5.4 | Favicon set | Browser tab shows Aydins icon, not Kalles default | | |
| 5.5 | Announcement bar styled | Black bg, bone text, uppercase tracked | | |
| 5.6 | Header nav works | Click each top-level link → page loads | | |
| 5.7 | Footer renders correctly | Columns, links, social icons, payment badges | | |
| 5.8 | Homepage sections render | Hero, featured collections, etc. — match design intent | | |

---

## TIER 6 — Other Page Surfaces
> *Easy to forget these existed. Test each.*

| # | Page | How to Check | Status | Notes |
|---|---|---|---|---|
| 6.1 | Collection page | `/collections/all` → grid renders, filters work, pagination works | | |
| 6.2 | Collection with active filter | Apply size/color/price filter → results update | | |
| 6.3 | Search results | Search box → query → results page | | |
| 6.4 | Account login / register | `/account/login` → form renders, submission works | | |
| 6.5 | Order status page | After test order → click "View order" link in confirmation email | | |
| 6.6 | Blog index (if used) | `/blogs/news` or whatever your blog handle is | | |
| 6.7 | Single blog article | Click into a post — renders correctly | | |
| 6.8 | 404 page | Visit `/this-does-not-exist` — branded 404, not generic Shopify | | |
| 6.9 | Static pages (About, Contact, Policies) | Visit each from footer | | |
| 6.10 | Mobile — all of the above | Resize browser to 375px or use DevTools mobile mode → re-test 1.1, 1.3, 1.7, 5.6 | | |

---

## TIER 7 — Aydins-Specific
> *Things only Aydins cares about — based on your CLAUDE.md, policies, and active workflows.*

| # | Item | How to Check | Status | Notes |
|---|---|---|---|---|
| 7.1 | Engraving tag → Zepto UI mapping | PDP with tag `Inside` → Zepto shows inside-only options. PDP with tag `Inside & Outside` → both options. See [[(C) Aydins Policies — Source of Truth]] | | |
| 7.2 | "Comfort fit is default" mention preserved | Check 2-3 PDPs → Key Features section still mentions comfort fit | | |
| 7.3 | No third-party brand names visible | Spot-check 3 PDPs → no "Thorsten" / "Universal" / "JCK" anywhere customer-facing | | |
| 7.4 | Free shipping bar / messaging | "Free 2 Business Day FedEx shipping" message renders correctly on PDP | | |
| 7.5 | Klaviyo AC1-AC2-AC3 abandoned cart flow | Add to cart → leave → confirm Klaviyo Started Checkout fires (will trigger AC1 in 30min) | | |
| 7.6 | Etsy listings unaffected | v5 launch is Shopify only. Confirm Etsy listings still pull product data correctly via whatever sync app you use | | |
| 7.7 | Google Merchant Center feed unaffected | After launch, check GMC dashboard 24h later → no spike in disapprovals | | |

---

## PRE-FLIGHT — Do these in the 30 minutes BEFORE publishing v5

- [ ] **Backup v4 settings**: in Shopify admin → Themes → v4 → `…` → **Duplicate** → name it `v4-backup-pre-v5-launch-2026-05-10`. This is your nuclear rollback.
- [ ] **Confirm v5 settings**: open v5 in Customize → spot-check 3 pages render as expected.
- [ ] **Note current Shopify Analytics baseline**: write down current 7-day conversion rate so you can detect regressions in the first 48h post-launch.
- [ ] **Notify any active orders/customers**: probably nothing to do, but if you have any in-flight customer chats about page issues, finish them first.
- [ ] **Pick a quiet hour to publish**: late night Sunday (low traffic) is ideal — minimizes the blast radius if something breaks.

## PUBLISH

- [ ] Shopify admin → Online Store → Themes → v5 → `…` → **Publish**.
- [ ] Confirm new theme is live: visit `aydinsjewelry.com` in incognito → no preview banner, looks like v5.

## POST-LAUNCH MONITOR — First 60 minutes

- [ ] **Run a real test order** with a real card on the live site. Confirm everything works end-to-end including order email.
- [ ] **Watch Shopify Live View** for 30 minutes — abnormal session drops, error spikes, cart abandonment spikes.
- [ ] **Watch console** of a live PDP in your own browser — any new JS errors?
- [ ] **Check Klaviyo** → confirm new sessions show up in real-time event stream.
- [ ] **Check ad platforms** (Google, Bing) → confirm conversion events still firing on test purchases.

## ROLLBACK — If anything's on fire

- [ ] Shopify admin → Themes → v4 (or `v4-backup-pre-v5-launch-2026-05-10` if v4 was overwritten) → `…` → **Publish**.
- [ ] You're back live in 30 seconds.
- [ ] Document what broke in [[03 Projects/Aydins Jewelry/09 Iteration Logs/]] for the next attempt.

---

## Post-launch follow-ups (next 7 days, not blocking)

- Monitor GA4 / Shopify Analytics conversion rate vs pre-launch baseline. >5% drop = investigate.
- Monitor GMC for disapproval spikes (24h delay).
- Re-test Klaviyo AC1-AC2-AC3 fires correctly with real cart abandonment.
- Confirm Loox reviews continue collecting and displaying.
- Spot-check 5 random PDPs across product types (rings, women's, sets, etc.) for layout integrity.
