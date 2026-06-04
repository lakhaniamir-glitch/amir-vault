# Aydins Meta Upload Package, Round 3 Coffee Shop UGC

Date: 2026-06-03  
Status: Ready for manual Meta Ads Manager upload by Amir  
Scope: V2 DEVITO coffee cup and V4 AVITUS couples  
Guardrail: No Meta upload performed by Beta

## Shared ad setup

- Campaign test: Couples Engraved UGC test
- Recommended ad set: `1|AY|6.3|Couples engraved| - 30|*|All mobile devices|1|US`
- CTA button: `Shop Now`
- Budget recommendation: keep the current winning ad at full budget. Add each new UGC variant into the same ad set with no extra budget so Meta can optimize the split organically.
- Kill rules:
  - 0 purchases after meaningful spend review threshold
  - CTR under 1% for 48 hours
  - No add to cart after meaningful spend review threshold

Note: Amir's prompt said "0 spent + 0 purchases" and "no ATC at 0 spend." That cannot be evaluated at zero spend, so this package treats it as a review threshold rule instead of a literal zero-spend rule.

## Validation summary

- Image dimensions verified: both selected assets are `1080x1350`.
- Shopify Admin API verification:
  - DEVITO handle exists, status `ACTIVE`, inventory `438`.
  - Requested AVITUS handle `avitus-carbon-fiber-ring-handle-verified` does not exist.
  - Verified AVITUS handle is `asher-blue-black-carbon-fiber-inlay`, status `ACTIVE`, inventory `839`.
- `beta_check_meta.mjs` validation: PASS for both ads.
- Validator warning: pixel ID match was not checked because expected and detected live pixel IDs were not supplied.

---

## V2, DEVITO coffee cup

### Asset

- Image file path: `/home/openclaw/.openclaw/vault/brands/aydins/meta-ads/01-ugc-testimonial/round3-coffee-shop/v2.png`
- Dimensions: `1080x1350`
- Format: 4:5 portrait feed image
- Product anchor: `DEVITO | Green Ring, White Tungsten Ring, Brushed, Flat`
- Shopify handle: `devito-white-tungsten-ring-with-green-tungsten-inside`
- Shopify status: `ACTIVE`
- Shopify inventory: `438`

### Meta fields

- Primary text:
  > The white tungsten catches light at breakfast, then the green inside shows when I grab coffee.

- Headline, max 27 chars:
  > Make His Ring Personal

- Description, max 27 chars:
  > Free U.S. shipping

- CTA:
  > Shop Now

- Landing page URL with UTM:
  > https://shopaydins.com/products/devito-white-tungsten-ring-with-green-tungsten-inside?utm_source=facebook&utm_medium=paid_social&utm_campaign=couples_engraved_ugc_test&utm_content=devito_coffee_cup

### Upload checklist

- [ ] Upload `v2.png` into Meta Ads Manager.
- [ ] Paste primary text exactly as above.
- [ ] Paste headline exactly as above.
- [ ] Paste description exactly as above.
- [ ] Select CTA: `Shop Now`.
- [ ] Paste landing page URL exactly as above.
- [ ] Place into ad set `1|AY|6.3|Couples engraved| - 30|*|All mobile devices|1|US`.
- [ ] Do not increase ad set budget for launch.
- [ ] Monitor against kill rules after launch.

---

## V4, AVITUS couples

### Asset

- Image file path: `/home/openclaw/.openclaw/vault/brands/aydins/meta-ads/01-ugc-testimonial/round3-coffee-shop/v4.png`
- Dimensions: `1080x1350`
- Format: 4:5 portrait feed image
- Product anchor: `AVITUS | Black Ceramic Ring, Blue & Black Carbon Fiber Inlay, Beveled`
- Shopify handle: `asher-blue-black-carbon-fiber-inlay`
- Shopify status: `ACTIVE`
- Shopify inventory: `839`

### Meta fields

- Primary text:
  > We wore our bands for coffee on our anniversary. His carbon fiber ring still feels personal.

- Headline, max 27 chars:
  > Make His Ring Personal

- Description, max 27 chars:
  > Free U.S. shipping

- CTA:
  > Shop Now

- Landing page URL with UTM:
  > https://shopaydins.com/products/asher-blue-black-carbon-fiber-inlay?utm_source=facebook&utm_medium=paid_social&utm_campaign=couples_engraved_ugc_test&utm_content=avitus_couples

### Handle correction

The requested URL used `avitus-carbon-fiber-ring-handle-verified`, but Shopify Admin API returned `null` for that handle. The verified active AVITUS handle is `asher-blue-black-carbon-fiber-inlay`, so this package uses the corrected URL above.

### Upload checklist

- [ ] Upload `v4.png` into Meta Ads Manager.
- [ ] Paste primary text exactly as above.
- [ ] Paste headline exactly as above.
- [ ] Paste description exactly as above.
- [ ] Select CTA: `Shop Now`.
- [ ] Paste landing page URL exactly as above.
- [ ] Place into ad set `1|AY|6.3|Couples engraved| - 30|*|All mobile devices|1|US`.
- [ ] Do not increase ad set budget for launch.
- [ ] Monitor against kill rules after launch.

## Validator record

Input file: `/home/openclaw/.openclaw/agents/beta/tmp/round3-coffee-shop/upload-validator-input.json`  
Result file: `/home/openclaw/.openclaw/agents/beta/tmp/round3-coffee-shop/upload-validator-results.json`

Result summary: PASS for both V2 and V4. Pixel ID warning only.
