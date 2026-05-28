# (C) Theme Migration — Kalles v4.2.1 → v5.4.0

> Source of truth for rebuilding the unpublished `kalles-v5-4-0-official` theme to match the current live v4 theme.
> Live theme ID: `136614478061`  ·  New theme ID: `159068061933`
> Generated 2026-04-21 from live theme settings_data.json + templates.

**DO NOT PUBLISH the new theme** until the product page checklist (section at bottom) passes QA on a test product.

---

## 0. Diff summary

- **118 live settings keys → 107 new settings keys. Only ~19 overlap.**
- v5 rebuilt the color system (individual vars → `color_schemes`), typography (new h0–h6 scale + spacing/line-height controls), and button system (new `button_radius`, `padding_btn_1`, `thickness_btn`).
- v5 removed: `header_design`, `general_layout`, `font_source`, `use_rtl`, many swatch/badge/tooltip settings.
- v5 added: `color_mode`, `color_schemes`, `animations_reveal_on_scroll`, badge system (`badge_new`, `badge_sale`, `badge_soldout`, `badge_preorder`, `badge_custom`), page width, spacing_grid, predictive search, free ship bar, compare/wishlist modes.
- **Naive copy of `settings_data.json` WILL break the theme** — don't do it.

---

## 1. Brand Assets (drop these into v5 settings → Favicon / Layout / Header)

| Asset | v4 key | Current value |
|---|---|---|
| Logo (main) | `logo` | `shopify://shop_images/Aydins_1_copy.png` — width 150px |
| Logo (mobile) | `logo_mb` | `shopify://shop_images/jbn.jpg` — width 95px |
| Transparent logo | `logo_tr` | `shopify://shop_images/header-logo-01.png` — width 95px |
| Checkout logo | `checkout_logo_image` | `shopify://shop_images/Aydins_500x140_ccdf46d2-5cbe-4348-9aee-8ea286b63f10.png` |
| Favicon | `favicon` | `shopify://shop_images/android-chrome-192x192.png` |
| Apple touch icon | `favicon_apple` | `shopify://shop_images/android-chrome-192x192.png` |
| Shop author | `shop_author` | `Aydins Jewelry` |

---

## 2. Colors

v4 used individual color vars. v5 uses **color schemes** (palette objects). Build a "Primary" scheme in v5 with these values:

| Role | v4 var | Hex | Map to v5 |
|---|---|---|---|
| Accent / Primary | `accent_color` | `#0f75bc` | Scheme `color_primary_button` / accent |
| Link hover | `link_color_hover` | `#0f75bc` | Same scheme `color_link` |
| Body bg | `body_bg` | `#ffffff` | Scheme `color_background` |
| Body text | `text_color` | `#333333` | Scheme `color_foreground` |
| Heading | `heading_color` | `#333333` | `heading` scheme color |
| Secondary | `secondary_color` | `#333333` | Scheme secondary |
| Border | `border_color` | `#333333` | Scheme `color_borders` |
| Button bg | `btn_bg` | `#333333` | `color_primary_button` |
| Sale price / primary price | `price_primary` | `#fff301` *(bright yellow — confirm this is still intentional)* | `color_sale` |
| Lazyload placeholder | `bg_lazyload` | `#333333` | v5 handles this automatically |
| Tooltip bg | `bg_tooltip` | `#333333` | `tooltip_bg` |
| Swatch border | `sw_border` | `#dddddd` | Scheme border |
| Lazyload indicator | `cl_lazyload` | `#fff301` | v5: `color_event` or remove |

**⚠️ Flag:** `price_primary = #fff301` (bright yellow) — is that correct for your live sale price color? Verify on storefront before copying.

---

## 3. Typography

v4 used Kalles' custom font picker. v5 uses Shopify's native font picker + explicit size controls.

**Live font choices:**
- Heading family (`hd_ffamily`): `1` (Kalles internal — **Poppins**)
- Body families (`fnt_fm_gg2`, `fnt_fm_gg3`): **Poppins**
- Specific fallbacks (`fnt_fm_sp1/sp2/sp3`): `poppins_n4` (Poppins 400)
- Button font (`fnt_fm_button`): `1`
- Source (`font_source`): Google Fonts

**In v5 set:**
- `font_base` → **Poppins Regular** (via Shopify font picker)
- `font_custom_heading` → **Poppins 500** (or whatever weight your H1s currently render at)
- `font_custom_sheading` → **Poppins 400**
- `hd_fweight` → 500 (confirm against live site inspecting an H2)
- Keep sizes at v5 defaults initially, then tune if needed.

---

## 4. Social Media Links

Drop these into v5 Social Media settings:

| Network | URL |
|---|---|
| Facebook | http://facebook.com/aydinsjewelry |
| Instagram | https://www.instagram.com/aydinsjewelry/ |
| Pinterest | https://www.pinterest.com/AydinsJewelry/ |
| TikTok | https://www.tiktok.com/@aydinsjewelry |
| Twitter/X | http://twitter.com/aydinsjewelry → **in v5 use `social_x_link` (renamed)** |

WhatsApp share enabled (`share_whatsapp: true`). No LinkedIn/YouTube/Telegram/Tumblr configured.

---

## 5. Currency / Language

- `currency_code_enabled: true`
- `currency_type: 1` (Shopify native)
- `currency_pos: 0` (code after amount)
- `round_currency: true`
- `notify_currency: true`
- `flag_currency: true` (show flag)
- `size_currency: md`
- **Supported currencies:** EUR, USD, GBP, CAD, AUD, AED

---

## 6. Header / Layout

- Header design: `inline` (v4) — v5 has new presets, pick closest match "Inline logo" or "Classic inline"
- Layout width: `wide` (v4 `general_layout=wide`) → v5 `page_width` = 1440–1600 (set to 1600)
- **Sticky ATC enabled:** `sticky_atc: true` (keep on in v5)
- **Cart drawer:** `cart_type: disable` → cart opens as PAGE not drawer (unusual — confirm this is still desired)
- Search hotkeys: `show_search_hotkey: true` · hotkey list: `Mens, Tungsten, Wedding Band, Black, Silver, Gold, Diamonds,` (trailing comma intentional? clean up in v5)
- Predictive search suggestion collection: `aydins-jewelry`

---

## 7. Product Card / Listing Behavior

| Setting | Live value | Keep/change in v5 |
|---|---|---|
| Product border style | `pr_border_style: 1` | v5 → `pr_card_radius` + `effect_secondary_image` |
| Second image on hover | `pr_img_effect: 0` | Off → v5 `effect_secondary_image: false` |
| Swatch style | `swatch_item_style: 1` | Keep |
| Show color variant as swatch | `show_color_type: 1` | Map to v5 `color_type` |
| "New" badge | `use_new_badge: true` | v5 `badge_new: true` |
| Variant picker shows color label | `color_ck: Color` | Keep |
| Variant labels (size) | `size_ck: Width, Size` | Keep |
| Variant change via image | `use_change_variant_by_img: true` | Keep |
| Group media by variant | `use_group_media: true` | Keep |
| Rating enabled | `enable_rating: true` | v5 `show_rating: true` |
| Quickview type | `type_qv: 2` | Map to v5 quickview |
| Free ship bar | `enable_shipbar: true` | v5 `free_ship_pr` (value = threshold) |
| Min quantity | `min_qty: 1` | Keep |
| Variant remove when OOS | `variant_remove: 1` | Keep |
| Unavailable products | `unavailable_prs: show` | v5 `hide_sold_out: false` |
| Wishlist mode | `wishlist_mode: 1` | v5 `hidden_wishlist: false` |
| Compare | _(on)_ | v5 `hidden_compare: false`, `enable_compare_popup: true` |

---

## 8. Custom CSS

**Your current `assets/custom.css` is empty** (template comments only). Nothing to port. ✓

---

## 9. 🚨 CRITICAL — Custom code in theme.liquid (WILL BE LOST)

Your live `layout/theme.liquid` has 14 custom `<script>` tags injected. These are NOT in the new theme. Copy-paste each into the v5 `theme.liquid` in the same position (use the Shopify code editor → Edit Code → layout/theme.liquid):

### 9.1 Google Merchant Customer Reviews widget (floating badge)
```html
<script id='merchantWidgetScript' src="https://www.gstatic.com/shopping/merchant/merchantwidget.js" defer></script>
<script type="text/javascript">
  merchantWidgetScript.addEventListener('load', function () {
    merchantwidget.start({
      position: 'RIGHT_BOTTOM',
      sideMargin: 21,
      bottomMargin: 200,
      mobileSideMargin: 11,
      mobileBottomMargin: 200
    });
  });
</script>
```

### 9.2 Microsoft Bing UET tag (conversion tracking) — `ti: 187151969`
```html
<script>(function(w,d,t,r,u){var f,n,i;w[u]=w[u]||[],f=function(){var o={ti:"187151969", tm:"shpfy_ui", enableAutoSpaTracking: true};o.q=w[u],w[u]=new UET(o),w[u].push("pageLoad")},n=d.createElement(t),n.src=r,n.async=1,n.onload=n.onreadystatechange=function(){var s=this.readyState;s&&s!=="loaded"&&s!=="complete"||(f(),n.onload=n.onreadystatechange=null)},i=d.getElementsByTagName(t)[0],i.parentNode.insertBefore(n,i)})(window,document,"script","//bat.bing.com/bat.js","uetq");</script>
```

### 9.3 Bing enhanced conversions (email/phone) — **⚠️ NEEDS LIQUID VARIABLE WIRING**
The stub below has `contoso@example.com` hardcoded. Replace with Shopify customer Liquid vars or remove:
```html
<script>
  window.uetq = window.uetq || [];
  window.uetq.push('set', { 'pid': {
    'em': '{{ customer.email | default: "" }}',
    'ph': '{{ customer.default_address.phone | default: "" }}'
  }});
</script>
```

### 9.4 Bing purchase event — **BROKEN, needs rewrite**
The existing block has `REPLACE_WITH_PRODUCT_ID` / `Replace_with_Variable_Revenue_Function()` placeholders — it never fired properly. Either fix it on v5 or delete. Recommend moving purchase tracking to Shopify's "Additional Scripts" in checkout settings instead (cleaner).

### 9.5 Google Customer Reviews opt-in — **broken too**
Current live block has hardcoded `order_id: AJ5197`, `email: cmmoore68@yahoo.com`, `estimated_delivery_date: 2023-10-23` from 2023 — this was left stuck on one past order. Rewrite as Liquid:
```html
{% if template contains 'thank_you' or template contains 'order' %}
<script src="https://apis.google.com/js/platform.js?onload=renderOptIn" async defer></script>
<script>
  window.renderOptIn = function() {
    window.gapi.load('surveyoptin', function() {
      window.gapi.surveyoptin.render({
        "merchant_id": 122065428,
        "order_id": "{{ order.name }}",
        "email": "{{ order.email }}",
        "delivery_country": "{{ order.shipping_address.country_code }}",
        "estimated_delivery_date": "{{ 'now' | date: '%s' | plus: 604800 | date: '%Y-%m-%d' }}"
      });
    });
  };
</script>
{% endif %}
```

### 9.6 Schemaapp JSON-LD injection
Your theme injects `{{ schema_app_markup }}` — confirm the **SchemaApp app** is installed on the store (it's referenced in product metafield `schemaapp.schema`). If the app's Liquid snippet isn't in the new theme, the JSON-LD won't fire. Re-embed:
```html
<script type="application/ld+json">{{ schema_app_markup }}</script>
```
(Place in `<head>` of v5 `layout/theme.liquid`.)

---

## 10. Homepage Layout (rebuild in v5 Theme Editor)

**v4 order → v5 equivalent mapping:**

| # | v4 section | v4 content | v5 equivalent |
|---|---|---|---|
| 1 | slideshow | 4 slides (Cyber Week 2025, Fingerprint Rings, Ash Holder Pendants, Beaded Bracelets) | `slideshow` ✓ (same name) |
| 2 | shipping | "AYDINS COMMITMENT" — 4 icons (Free Shipping, Lifetime Warranty, Free Engraving, Exchanges) | `shipping` ✓ (same name) |
| 3 | image-gallery | "AYDINS COMMITMENT" — 4 image tiles linking to pages | **No direct equivalent** — use `banners` or `collections-list-manual` |
| 4 | line (divider) | — | No v5 equivalent — remove |
| 5 | featured-collection | "Featured collection" → `unique-inlay-wedding-bands`, 4 items, 1:1 | `featured-collection` ✓ |
| 6 | featured-collection | "Just Added" → `recently-added`, 12 items | `featured-collection` ✓ |
| 7 | banner | 4-panel banners (Whiskey Barrel, Celtic, Titanium, Carbon Fiber) | `banners` (renamed) |
| 8 | line | — | Remove |
| 9 | featured-collection | "Trending Bestsellers!" → `best-sellers`, 12 items | `featured-collection` ✓ |
| 10 | line | — | Remove |
| 11 | image_text | "Satisfaction, Honesty, Shipping" + text about Texas warehouse | **No direct equivalent** — rebuild using v5 `rich-text` + `image-with-text` (standard Shopify sections) |
| 12 | blog-post | "LATES FROM BLOG" → `wedding-band-materials`, 3 posts | `blog-post` ✓ |
| 13 | instagram-shop | "Tag @AydinsJewelry" — 8 Instagram shoppable images | **No direct equivalent in v5** — use `lookbook-carousel` (new v5 section) with same images |
| 14 | line | — | Remove |
| 15 | apps | _(empty)_ | Remove |
| 16 | apps | _(empty)_ | Remove |
| 17 | image_text | "AYDINS JEWELRY — We Would Like to Tell You A Little About Our Store" | Rebuild as rich-text |

### Homepage content detail (copy into v5 sections)

**Slideshow slides:**
1. `shopify://shop_images/Cyber_week_2025.jpg` — no link, center-aligned
2. `shopify://shop_images/Fingerprint_rings.png` → `shopify://collections/fingerprint-handwritten`
3. `shopify://shop_images/Ash_Holder_Jewelry_-_Aydins_Jewelry.png` → `shopify://collections/ash-holder-pendants`
4. `shopify://shop_images/Fingerprint_rings_2.png` → `shopify://collections/mens-womens-beaded-bracelets`

Settings: desktop 600px tall, tablet 400px, mobile 250px · slide effect · 5s autoplay · hover pause · default owl nav · elessi dot style.

**Shipping bar (AYDINS COMMITMENT):**
- Heading: `AYDINS COMMITMENT` / Subheading: `Elevate Your Experience with Every Purchase!` · Icon: `las la-gem` · Primary color `#0f75bc`
- 4 items:
  1. 🚚 **FREE US, CANADA, AUSTRALIA, GERMANY & UK SHIPPING** — "Get Ready to Soar! Free Standard US Shipping, Express Shipping Available Worldwide*!"
  2. ☂️ **Lifetime Warranty/Sizing** — "Amplify Your Confidence! Every Purchase Comes with a Lifetime Warranty and Sizing!"
  3. ⛵ **Free Laser Engraving** — "Engrave Your Memories for Free! Personalize Your Purchase at No Extra Cost!"
  4. 🔄 **Exchanges/Returns** — "Your Peace of Mind! Rings with Lifetime Size Exchanges or 30-Day Returns – Always Your Call!"

**Image gallery tiles (Aydins Commitment extended):**
1. `1_Free_Shipping.png`
2. `2_Lifetime_sizing.png` → `/pages/lifetime-sizing-lifetime-warranty`
3. `3_Exchanges_and_Returns.png` → `/pages/free-laser-engraving`
4. `4_Free_Laser_Engraving.png` → `/pages/returns-exchanges`

**4-panel banners (after Just Added):**
1. `Untitled_500_x_250_px_b283a872-...jpg` → `/collections/genuine-whiskey-barrel-collection`
2. `Celtic_Banner.jpg` → `/collections/celtic-wedding-bands`
3. `Titanium_Collection.jpg` → `/collections/titanium-rings-wedding-bands-for-men-and-women-aydins-jewelry`
4. `Carbon_Fiber.jpg` → `/collections/carbon-fiber-wedding-bands`

**"Satisfaction, Honesty, Shipping" image_text block:**
- Image: `shopify://shop_images/Satisfaction_Honesty_Shipping.jpg`
- Copy: _"We ship all of our products from our Texas warehouse..."_ (pull full text from v4 editor before deleting — truncated in export)

**Blog posts section:**
- Heading: `LATES FROM BLOG` (fix typo → "LATEST FROM BLOG")
- Subheading: `The freshest and most exciting news`
- Blog source: `wedding-band-materials` · 3 posts · 4:3 ratio

**Instagram / Lookbook (8 shoppable images):**
| Image | Tagged product |
|---|---|
| Active_Couple.png | `burnsley-black-tungsten-flat-with-black-tungsten-inside` |
| Hand.png | `brave-blue-tungsten-ring-blue-brushed-flat` |
| Marriage_Coffee_Mug.png | `hyde-damascus-steel-silver-ring-with-blue-and-yellow-box-elder-wood-sleeve` |
| Couple_Holding_Hands.png | `ajax-blue-dinosaur-bone-ring-inlaid-with-ceramic-wedding-band` |
| Groom_Wedding_Band.png | `sol-traditional-domed-rose-gold-plated-tungsten-carbide-wedding-ring-4mm` |
| Better_than_pizza.png | `viking-purple-ring-silver-hammered-titanium-ring` |

---

## 11. Product Page Layout (the critical one)

**v4 block order on main-product section** (rebuild in v5 exact order):
1. `title`
2. `sold` (scarcity badge)
3. `price_review` (price + Loox star rating)
4. `custom_liquid` — **check content of this block in Shopify admin before deleting; may contain Klarna/Afterpay or other inserts**
5. Loox Trust Badge app block
6. Loox Snippets widget
7. `img` (product image / variant image section inside main)
8. **Zepto Product Personalizer** (critical for engraving — must be present)
9. Klarna on-site messaging app block
10. `form` (add-to-cart form)
11. `size_delivery_ask` (size chart / delivery ask widget)
12. `meta` (SKU, vendor, type, tags)
13. `tab_des` (description tab)
14. `tab_html` × 5 (custom HTML tabs — open each in v4 editor and copy content verbatim)
15. `tab_rivui` (reviews tab)
16. `social` (share buttons)
17. `tab_html` (another custom tab)

**Also on product page template:**
- `brc-nav-product` (breadcrumbs)
- `image-gallery` (3 image_items below main product)
- `sidebar-product` with blocks: `category`, `collection`, `instagram`, `shipping`, `image`
- `product-recommendations` → v5 = **`related-products`** (renamed)
- `recently_viewed` → v5 = **`recently-products`** (renamed)
- `apps` — contains Loox dynamic section (reviews gallery)

### Product metafield references (CRITICAL — verify all wire-ups survive)

These metafields exist on products and the theme must render them:

| Metafield | Purpose | Used by |
|---|---|---|
| `custom.keywords` | Quick Specs display | Theme product block or custom_liquid |
| `custom.tungsten_ring_information_` | Page link → "Tungsten Ring Information" | Theme conditional — check which block |
| `shopify--discovery--product_recommendation.related_products` | Related products override | `related-products` section |
| `schemaapp.schema` | JSON-LD | Schemaapp widget or theme.liquid injection |

**Acceptance test (MUST pass before publishing v5):**
- [ ] Open PROOF product preview on v5 → Quick Specs shows `Width: 8mm / Gold Tungsten Carbide / Whiskey Barrel Oak / etc.`
- [ ] Tungsten Ring Information page link renders somewhere visible
- [ ] Zepto engraving popup fires when `(Inside)` tag is present
- [ ] Loox star rating + reviews widget render
- [ ] 6 related products shown from the metafield list
- [ ] JSON-LD present in page source (`schema.org/Product`)
- [ ] Add to cart works, cart opens as **page** (not drawer — per `cart_type: disable`)

---

## 12. Collection Page

v4 layout:
- `heading-template` (large collection banner) → **v5 `main-heading`** (renamed)
- `main-collection` (product grid + filters)
- `sidebar-collection` → **removed in v5**, use `main-collection` sidebar settings
- `top-collections` (featured collections strip at top) → **v5 `top-list-collections`** (renamed)

---

## 13. Page / Blog Templates

- `page.json` — standard page template (996 bytes, minimal customization — v5 defaults are fine)
- `blog.json` — blog listing template (4 KB — 2-3 sections beyond default; review in v4 editor)

---

## 14. Apps to re-wire on v5 (app embeds don't transfer)

Confirm each app's "Embed" toggle is ON in v5 theme settings → App embeds:

- [ ] **Loox Reviews** — trust badge, snippets widget, dynamic reviews section
- [ ] **Zepto Product Personalizer** — engraving popup (watch for `(Inside)` tag)
- [ ] **Klarna on-site messaging**
- [ ] **SchemaApp** — JSON-LD injection
- [ ] **Growave social login** (live had `growave_social_login: true`)
- [ ] **Klaviyo** (if installed — live had `ajax_klaviyo` key)

---

## 15. Ordered punch list (do it in this order)

1. **[ ] Back up v4** — duplicate the published theme once more as a safety net (`Copy of Kalles v4.2.1 ...`) before touching anything
2. **[ ] Paste custom `<script>` blocks** from §9 into v5 `layout/theme.liquid` (edit code view)
3. **[ ] Set brand assets** (§1): logo, favicon, checkout logo
4. **[ ] Build Primary color scheme** (§2): accent `#0f75bc`, text `#333`, bg `#fff`, button bg `#333`
5. **[ ] Set typography** (§3): Poppins base + headings
6. **[ ] Social links** (§4): FB, IG, Pinterest, TikTok, Twitter (rename to X)
7. **[ ] Currency settings** (§5): USD + 5 others, EUR/USD/GBP/CAD/AUD/AED
8. **[ ] Header config** (§6): inline layout, sticky ATC on, cart = page, search hotkeys
9. **[ ] Product card behavior** (§7): badges, swatches, quickview, compare, wishlist
10. **[ ] Enable app embeds** (§14)
11. **[ ] Rebuild homepage** (§10) — slideshow → shipping → image tiles → featured collections → banners → best-sellers → image_text → blog → lookbook → about
12. **[ ] Rebuild product page** (§11) — match v4 block order exactly
13. **[ ] Test product page on PROOF and HYDRA** with the acceptance checklist
14. **[ ] Rebuild collection page** (§12)
15. **[ ] Preview on staging URL** — click through: home, collection, product, cart, checkout
16. **[ ] Verify UET fires** (DevTools → Network → `bat.js`)
17. **[ ] Verify Loox widget renders**
18. **[ ] Verify Zepto fires on PROOF** after adding `(Inside)` tag
19. **[ ] Only then → Publish v5**
20. **[ ] Within 24h of publish: monitor Bing Ads UET, Google Merchant reviews, Loox review submission**

---

## Files generated

- `theme-migration/live/` — exported v4 configs (settings_data, templates, custom.css, theme.liquid)
- `theme-migration/new/` — exported v5 configs (for reference / diff)

## Next action

Work through §15 sequentially. Ping me at any step you hit friction — I can pull more data from either theme via API, push specific settings back via the Shopify Admin API where the schema is compatible, or script any repetitive work.
