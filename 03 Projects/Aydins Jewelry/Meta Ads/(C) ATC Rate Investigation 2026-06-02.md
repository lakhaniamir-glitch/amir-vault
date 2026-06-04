# ATC rate investigation - 2026-06-02

Status: read-only investigation completed with partial data access
Store: Aydins Jewelry
Window: last 30 days where ShopifyQL allowed

No PDP edits, theme edits, Meta changes, Merchant Center writes beyond Task A checks, or Shopify setting changes were made.

## Data access

- Meta audit input: 507K ViewContent events and 1.6K AddToCart events, which equals 0.32 percent on a ViewContent event basis.
- GA4 source and page pull: blocked. OAuth refresh returned invalid_grant, token expired or revoked.
- ShopifyQL sessions: available.
- ShopifyQL sales by product: available.
- ShopifyQL product view and cart datasets by product: not exposed to this token. Product views and per product ATC are blocked.
- Mobile PDP screenshots: completed for 10 fallback products.

## Confirmed ATC rate

Two rates are now confirmed, but they use different denominators:

1. Meta pixel event basis from prior audit:
   - ViewContent: 507,000
   - AddToCart: 1,600
   - ATC rate: 0.32 percent

2. Shopify session basis from ShopifyQL:
   - Sessions: 92,889
   - Sessions with cart additions: 517
   - ATC rate: 0.56 percent
   - Conversion rate: 0.17 percent
   - Sales: $31,603.44
   - Orders: 171
   - Average order value: $184.83

These are not directly interchangeable, but both confirm the same problem: cart intent is far too low.

## Source split

ShopifyQL source split shows this is not uniform.

| Source | Sessions | Cart sessions | ATC rate | Conversion rate |
|---|---:|---:|---:|---:|
| Direct | 80,435 | 164 | 0.20 percent | 0.08 percent |
| Search | 8,773 | 324 | 3.69 percent | 0.97 percent |

Conclusion: search traffic behaves normally for jewelry. The collapse is concentrated in direct traffic. That usually means traffic quality, attribution loss, bot or low intent traffic, or ad traffic being classified as direct.

## Mobile PDP diagnostic summary

Fallback basis: top sold products from ShopifyQL sales data, because top viewed product and per product ATC datasets are blocked under the current token.

Across all 10 inspected mobile PDPs:

- Price above the fold: yes, 10 of 10.
- ATC button above the fold: no, 10 of 10.
- Variant selector present: yes, 10 of 10.
- Reviews visible: yes, 10 of 10.
- Product image above the fold: weak signal. The first visible image detected was the header logo, not the ring image.
- Above fold clutter: cookie consent, promo bar, shipping/trust strip, review strip, similar styles, and variant selectors push the cart action down.

## Top 10 inspected PDPs

| Rank | Handle | Price above fold | ATC above fold | Variants | Reviews | Screenshot |
|---:|---|---:|---:|---:|---:|---|
| 1 | nurgle-black-diamond-titanium-wedding-ring | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/01-nurgle-black-diamond-titanium-wedding-ring.png |
| 2 | valor-silver-tungsten-ring-silver-inlay-black-diamonds | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/02-valor-silver-tungsten-ring-silver-inlay-black-diamonds.png |
| 3 | aurion-gold-tungsten-ring-gold-foil-inlay-beveled-8mm | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/03-aurion-gold-tungsten-ring-gold-foil-inlay-beveled-8mm.png |
| 4 | nemesis-black-tungsten-ring-white-round-cz-beveled-edge-ring | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/04-nemesis-black-tungsten-ring-white-round-cz-beveled-edge-ring.png |
| 5 | auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/05-auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay.png |
| 6 | nymeria-tension-set-blue-sapphire-titanium-band-with-blue-stripe-4mm | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/06-nymeria-tension-set-blue-sapphire-titanium-band-with-blue-stripe-4mm.png |
| 7 | elysian-black-titanium-ring-with-polished-beveled-edges-and-brush-finished-center-8mm | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/07-elysian-black-titanium-ring-with-polished-beveled-edges-and-brush-finished-center-8mm.png |
| 8 | smokeylade-black-gun-metal-tungsten-with-domed-brushed-ring | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/08-smokeylade-black-gun-metal-tungsten-with-domed-brushed-ring.png |
| 9 | ironlance-black-tungsten-ring-with-flat-brushed-center-and-8-laser-engraved-crosses-8mm | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/09-ironlance-black-tungsten-ring-with-flat-brushed-center-and-8-laser-engraved-crosses-8mm.png |
| 10 | halsten-platinum-inlaid-beveled-tungsten-carbide-wedding-ring-6mm-or-8mm | yes | no | yes | yes | /home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/10-halsten-platinum-inlaid-beveled-tungsten-carbide-wedding-ring-6mm-or-8mm.png |

## Root cause hypotheses ranked

1. Low quality or misattributed direct traffic is the biggest driver.
   - Direct traffic has 80,435 sessions and only 0.20 percent ATC.
   - Search has 3.69 percent ATC, which is within a healthy range.
   - This strongly suggests the blended rate is being dragged down by direct traffic, not by every shopper seeing a broken product page.

2. Mobile PDP layout hides the cart action too far down.
   - ATC button was not above the fold on 10 of 10 inspected mobile PDPs.
   - Users see price, badges, reviews, similar styles, and selectors before the main purchase action.
   - This hurts mobile conversion even if traffic is qualified.

3. Consent and measurement behavior may inflate the ViewContent denominator.
   - Cookie consent appears before the product content in the mobile render.
   - Meta ViewContent event count is very high relative to Shopify sessions.
   - If repeated views, bots, reloads, or catalog traffic inflate ViewContent, Meta ATC rate looks worse than Shopify session ATC.

4. Product choice friction is high before cart.
   - Ring size, width, and engraving options appear before purchase.
   - That is necessary for custom rings, but the current mobile flow delays the clear cart CTA.
   - A sticky ATC or compressed option stack would likely improve intent capture.

5. Some product imagery may not be strong enough above the fold.
   - Automation detected the header logo before product imagery.
   - Screenshots indicate the product image does not dominate the first mobile viewport.
   - This weakens the product value punch before the shopper has to choose variants.

## Recommendations

### PDP fixes

1. Add or restore a sticky mobile ATC bar after price and required variant selection.
2. Move the main product image and core purchase CTA higher on mobile.
3. Compress the duplicated trust and review sections above the selector area.
4. Keep variant selectors, but reduce vertical height and make the next required choice obvious.
5. Audit the cookie consent placement and height on mobile so it does not consume the first impression.

### Traffic quality fixes

1. Treat direct traffic as the main suspect until proven otherwise.
2. Validate Meta UTMs and landing URL parameters so paid traffic does not collapse into direct.
3. Split reporting into direct, search, paid social, paid search, email, and referral once GA4 token is refreshed.
4. Add a bot and spam traffic check for direct sessions.
5. Compare direct traffic landing paths and geography against real buyer behavior.

## Estimated revenue impact

Using Shopify session basis:

- Current sessions: 92,889
- Current cart sessions: 517
- Current ATC rate: 0.56 percent
- Current orders: 171
- Current AOV: $184.83
- Current cart to order ratio: about 33 percent

If ATC improves to 1.0 percent:

- Expected cart sessions: 929
- Incremental cart sessions: 412
- Estimated incremental orders at current cart to order ratio: 136
- Estimated incremental revenue: about $25,100 per 30 days

If ATC improves to 2.0 percent:

- Expected cart sessions: 1,858
- Incremental cart sessions: 1,341
- Estimated incremental orders at current cart to order ratio: 444
- Estimated incremental revenue: about $82,000 per 30 days

These are directional, not guarantees. The realistic first target is fixing direct traffic attribution and mobile CTA visibility, then moving Shopify session ATC from 0.56 percent to 1.0 percent.

## Raw files

- ShopifyQL raw: `/home/openclaw/.openclaw/command-center/work/atc-shopifyql-raw-2026-06-02.json`
- ShopifyQL probe: `/home/openclaw/.openclaw/command-center/work/shopifyql-probe-2026-06-02.json`
- PDP diagnostics: `/home/openclaw/.openclaw/command-center/work/atc-pdp-diagnostics-2026-06-02.json`
- Screenshots: `/home/openclaw/.openclaw/agents/beta/screens/atc-rate-2026-06-02/`
