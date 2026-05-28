# C-EDD Widget Revamp Spec

> **Author:** Claude
> **Date:** 2026-05-19
> **Status:** Draft for Amir review
> **Surface:** Every PDP on aydinsjewelry.com (C-EDD app block)
> **Why:** (1) live compliance violation in the message text, (2) generic visual treatment that does not match the Aydins brand voice.

## 1. Do tonight (5-minute clarity fix)

The widget currently says:

> "Free 2 Business Day FedEx shipping to U.S."

The shipping claim is true (free 2-business-day FedEx in the U.S. is real), but it omits the 1-3 business day processing window. A customer reading the current widget can assume "arrives in 2 days from order" when the real window is 3-5 business days total.

**Replace the Message Text field with:**

> Free FedEx 2Day shipping in the U.S. Free international shipping to Canada, UK, Germany, and Australia on all wedding bands. We ship worldwide. Most orders ship in 1 to 3 business days from our workshop in Irving, Texas. Free engraving included.

Or the cleaner three-line version if C-EDD allows line breaks in Message Text:

> Free FedEx 2Day shipping in the U.S.
> Free international shipping to Canada, UK, Germany, and Australia on all wedding bands. We ship worldwide.
> Most orders ship in 1 to 3 business days from our workshop in Irving, Texas. Free engraving included.

International is a real verified offer (confirmed by Amir 2026-05-19) and is a meaningful competitive differentiator. The "we ship worldwide" line keeps the door open for non-free destinations (customer pays carrier rates at checkout). Surface both.

That is the immediate fix. Everything below is the bigger visual revamp.

## 2. Why the widget looks dull

Specific issues:

1. **Three yellow circle badges with stock icons.** Bag, truck, pin. This is the default C-EDD template. It reads as a generic Shopify app, not Aydins.
2. **Yellow `#F5C518` (the C-EDD default) does not exist anywhere else in the Aydins brand palette.** It fights with the navy and gold the rest of the site uses.
3. **Dotted gray connector line between badges** is weak. It pulls the eye sideways instead of letting the dates carry weight.
4. **Date typography is system sans, same weight, same size as everything else.** The dates are the most important data in the widget and they read like form labels.
5. **Status labels ("Order Ready", "Order Shipped", "Order Delivered")** are sentence case, generic, and do not sound like Aydins. They sound like a tracking page from any drop-shipper.
6. **Tooltip copy under "Order Ready"** is generic carrier language ("processed and prepared for shipping").
7. **No visual hierarchy.** Title, status row, date row, message row all weigh the same.

## 3. Target voice for this widget

The widget should read like a quiet promise from a real workshop, not a SaaS countdown. Same voice as the listings:

- Polished, masculine, direct
- Calm confidence, not urgency
- Workshop, not warehouse
- "We" language where appropriate (we ship, we engrave)
- No fake scarcity, no "ORDER NOW" energy

## 4. Visual direction

### 4.1 Color

**Kill the yellow.** Replace with one of:

- **Muted bronze `#8B6F3D`** (preferred, matches the warm metal palette the rings live in)
- **Oxblood `#6B2C2C`** (more masculine, more confident)
- **Charcoal `#1F1F1F` with bronze accent on the active step** (most restrained, most premium)

Pick one and run it everywhere. The Customize Color tab in C-EDD lets you set the badge color directly.

Connector line: solid `#D9D2C5` (warm stone), not dotted gray. Or remove it entirely. A clean gap reads more premium than a dotted line.

### 4.2 Step indicators

Drop the stock bag/truck/pin icons. Two options:

- **Letter glyphs:** `O` `R` `D` (Order, Ready, Delivered) set in a serif at the same size as the badge, vertically centered.
- **Line-weight icons:** if C-EDD will not accept letters, replace the filled stock icons with 1.5px line versions. C-EDD's icon library has line variants under Customize > Icons.

Active step gets the bronze fill. Completed steps get a subtle check. Future steps stay outlined only.

### 4.3 Typography

- **Status labels** ("Order Ready", "Order Shipped", "Order Delivered") → all-caps, letterspaced, small. e.g. `ORDER · READY` at 11px, letter-spacing 0.08em. Same family as the rest of the site.
- **Dates** → serif, larger than status labels, bolder weight. The dates are the data the customer cares about. Make them the visual anchor of each badge.
- **Message text** (the line under the timeline) → regular paragraph weight, same size as PDP body copy. Not bold, not centered if the rest of the PDP is left-aligned.

### 4.4 Layout

Keep the 3-step horizontal row. Do not over-engineer this. Just:

1. Pull the title "Estimated Delivery Date" or replace it with something quieter like "Ships from our workshop" or just remove the title entirely if the badges are self-explanatory.
2. Tighten vertical spacing between the badge row and the message text. Right now it feels stacked rather than composed.
3. Make sure the widget respects the PDP width and does not feel like a card pasted on top.

## 5. Status label and tooltip rewrites

Current C-EDD defaults are generic. Rewrites:

| Position | Current | Replace with |
|---|---|---|
| Step 1 label | Order Ready | `ORDER PLACED` |
| Step 1 tooltip | (generic) | When you complete checkout, your order enters our workshop queue. Engraving details are reviewed the same day if placed before 1:00 PM CT. |
| Step 2 label | Order Shipped | `LEAVES WORKSHOP` |
| Step 2 tooltip | (generic) | Most orders ship in 1 to 3 business days from our workshop in Irving, Texas. Engraved orders may take 1 extra day. Free FedEx 2Day shipping in the U.S. |
| Step 3 label | Order Delivered | `ARRIVES` |
| Step 3 tooltip | (generic) | Estimated arrival window based on free 2-business-day FedEx shipping in the U.S., on top of our 1-3 business day processing time. We do not guarantee a specific date, but most orders arrive within this range. |

Note the "we do not guarantee" language on Step 3. This protects against the same compliance trap that bit us with the "2-day FedEx" claim. The widget is showing an estimate, not a promise.

## 6. Settings tab values to use

From the screenshots you sent:

- **Timezone:** GMT-6 (CT, correct for Irving, TX) — leave as-is
- **Cutoff time:** 13:00 — leave as-is, but the tooltip should reflect this in customer language ("placed before 1:00 PM CT")
- **Working days:** Mon-Fri — leave as-is
- **Holidays list:** verify against the actual 2026 workshop calendar before next push. If we close for any non-standard days (e.g. religious holidays, family days, inventory days), add them so the widget does not promise a date the workshop cannot hit.
- **Ready range:** 1 to 2 business days
- **Delivery range:** 2 to 5 business days
- **Engraved orders:** verify if C-EDD supports a per-tag or per-product offset. If yes, add 1 extra ready-day for products with the `Inside` or `Inside & Outside` tag. If not, the message text already covers it ("Engraved orders may take 1 extra day").

## 7. Message text (final)

Replace the current Message Text with:

```
Free FedEx 2Day shipping in the U.S. Free international shipping to Canada, UK, Germany, and Australia on all wedding bands. We ship worldwide. Most orders ship in 1 to 3 business days from our workshop in Irving, Texas. Free engraving included.
```

If C-EDD supports multiple lines:

```
Free FedEx 2Day shipping in the U.S.
Free international shipping to Canada, UK, Germany, and Australia on all wedding bands. We ship worldwide.
Most orders ship in 1 to 3 business days from our workshop in Irving, Texas. Free engraving included.
```

Why each part has to be in the message:
1. **U.S. line:** "2-day shipping" alone reads as a promised arrival date. Pairing it with the processing window keeps the total order-to-door window honest (3 to 5 business days).
2. **Free international line:** Free shipping to four countries on every wedding band is a real differentiator (most competitors charge $20-50 for international). Surface it.
3. **Worldwide line:** Keeps the door open for customers in non-free countries. They pay carrier rates at checkout.
4. **Processing line:** Tells the truth about when the ring actually leaves the workshop.
5. **Engraving line:** Free engraving is another differentiator and reinforces the workshop value-add.

The C-EDD step-3 "Arrives" date will reflect the full per-country window, so the message text reinforces what the badges already show.

## 8. What this is NOT

- Not a countdown timer. The C-EDD countdown setting should stay off. Countdown pressure does not match the Aydins voice.
- Not a "free returns" or "warranty" surface. Those live in the trust section and the Policies page, not in the delivery widget.
- Not the place to mention engraving as a product feature. Only mention engraving as it affects timing.

## 9. Settings to change in each tab (concrete to-dos)

### 9.1 Appearance tab > Appearance Basic Configuration

- **Message Text Widget > Border > Border line style:** change from `dotted` to `none` (preferred) or `solid` with width 1, radius 4. Dotted reads cheap and fights the rest of the PDP.
- **Progress Bar Widget > Color:**
  - `Icon background color`: change from yellow `#fff301` to bronze `#8B6F3D` (or your chosen palette pick from Section 4.1).
  - `Icon color`: keep dark, around `#1F1F1F`.
  - `Progress line color`: change from pure black `#000000` to warm stone `#D9D2C5`. Black is heavy and pulls the eye sideways.
  - `Order status title color`: dark gray `#1F1F1F` (slightly softer than pure black).
  - `Date title color`: bronze `#8B6F3D` (or chosen accent) so the date itself reads as the visual anchor.
  - `Description tips background color`: keep `#000000` for contrast on the tooltip.
  - `Description tips color`: keep `#FFFFFF`.

### 9.2 Appearance tab > Layout Configuration

- **Widget layout mode:** keep `Message Text Widget & Progress Bar Widget` (current). Both are doing work.
- **Widget placement method:** keep `Automatic` unless we are doing a Theme 2.0 custom placement.
- **Widget placement position:** `Below "ADD TO CART"` (current) is correct. Above ATC pushes the buy button down on mobile.
- **Widget placement page:** `Only on the product page` (current) is correct.

### 9.3 Modal Popup Country tab

- **Show country mode:** keep `All country`. We ship worldwide, so the picker should reflect that. The Message Text already calls out which four countries get free international shipping, so the picker doesn't need to be restricted.
- **Country List Appearance:** the defaults (`#000000` text on `#FFFFFF` bg) are fine. Do not waste cycles here unless we are restyling the country picker.

### 9.4 Advance tab > Cart/Checkout Configuration

Cart/Checkout estimated delivery date message is **enabled**, surfacing on the cart and checkout pages too. Update the copy:

- **Title field:** change from `Estimated between` to `Estimated delivery`
- **Description field:** keep the templated date variables but tighten the wording. From:
  > `{order_delivered_minimum_date} and {order_delivered_maximum_date}`
  to:
  > `{order_delivered_minimum_date} to {order_delivered_maximum_date}, with free 2-business-day FedEx shipping in the U.S.`

That single line on the cart page is high-leverage. Customer is mid-checkout, this is the last shipping reassurance they read.

### 9.5 Advance tab > General Configuration

Confirm whether to set **per-Product** or **per-Category** delivery configs. Recommended:
- Default config covers most rings (1-2 day ready, 2-5 day delivery)
- Add a per-product or per-tag override for engraved orders (+1 day on the ready window). If C-EDD supports targeting by tag, target `Inside` and `Inside & Outside`. If only by product, accept that all rings effectively become +1 ready-day, which is fine.

### 9.6 Other tab > Custom CSS

C-EDD exposes `.delivery-widget__container` as the wrapper selector. Use it for anything the settings UI does not cover:

```css
.delivery-widget__container {
  /* respect site grid, no extra padding on PDP */
  padding: 0;
  margin: 14px 0 0 0;
  font-family: inherit; /* match the rest of the PDP, not C-EDD's default */
}

.delivery-widget__container .order-status-title {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 11px;
  font-weight: 600;
}

.delivery-widget__container .date-title {
  font-family: Georgia, "Times New Roman", serif; /* or whatever the site serif is */
  font-size: 14px;
  font-weight: 500;
}
```

The exact selectors below `.delivery-widget__container` need to be inspected on the live PDP (right-click > Inspect on the status title and the date) and confirmed before writing CSS that targets them. Different C-EDD versions name child elements differently.

### 9.7 Open verification items

1. **Holidays list** — verify the 2026 list in Settings against the actual workshop calendar. Anything missing? (Family / religious / inventory days.)
2. **International windows** — do we have real carrier data for Canada / Australia / Germany / UK? If yes, surface them. If not, switch `Show country mode` to `Only added country` and remove the unverified line.
3. **Engraving offset** — does C-EDD support per-tag offsets? Confirm in Advance > General > Product or Category configs.
4. **C-EDD plan limits** — confirm the current C-EDD plan allows custom colors, custom icons / letter glyphs, multi-line message text, and Custom CSS. If not, that is the upgrade question.

## 10. Rollout order

1. **Tonight:** Replace the Message Text with the line in Section 1. Kills the compliance violation. Zero design work needed.
2. **This week:** Apply the color and typography changes in Section 4. Apply the status label and tooltip rewrites in Section 5. Test on one device per breakpoint.
3. **Next week:** Verify the open items in Section 9. Add the engraving offset if supported.
4. **Ongoing:** Any future shipping or delivery claim added to the widget must be cross-checked against [[(C) Aydins Policies — Source of Truth]] before going live. Same rule as listing copy.

## 11. Why this matters

The widget is on every PDP. It is one of the last things a buyer reads before adding to cart. Three things have to be true:

1. **It cannot lie.** A specific shipping promise we cannot defend is worse than no promise.
2. **It cannot look generic.** A stock C-EDD treatment makes the whole listing feel templated.
3. **It cannot fight the brand.** Yellow badges fight the navy / bronze / charcoal palette the rest of the site lives in.

Fix all three and the widget stops being decoration and starts pulling its weight on conversion.
