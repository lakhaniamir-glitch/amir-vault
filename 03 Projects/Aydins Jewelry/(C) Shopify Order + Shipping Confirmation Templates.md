# (C) Shopify Order + Shipping Confirmation Templates (paste-ready)

> **What this is:** Two paste-ready Shopify notification templates rebuilt to match the Aydins Klaviyo stack — same Bebas Neue / Cormorant Garamond / Poppins typography, same ink + cream + brass-gold palette, same trust pillars, same "A small jewelry shop" footer signature.
>
> **Why this exists:** We deliberately kept Shopify's native transactional emails (Order Confirmation + Shipping Confirmation) instead of building Klaviyo versions, because Shopify owns the receipt math and tracking data. But the default Shopify templates look like a 2015 generic store. These rewrites make the transactional emails visually continuous with the Klaviyo branded flows (Welcome, Thank You, AC, Browse, Winback) — so a customer never gets jolted between "premium branded email" and "generic Shopify email" on the same purchase journey.
>
> **Source of truth for every claim:** [[(C) Aydins Policies — Source of Truth]]. No fabricated warranties. Marketing copy uses approved labels only — "Free Engraving," "Free U.S. Shipping," "Lifetime Warranty," "30-Day Returns" — no fee qualifiers in the email itself.

---

## Critical syntax note

Shopify notification templates use **Liquid** (the original — Klaviyo's template engine is *based on* Liquid but they aren't identical). Differences from Klaviyo:

| Need | Klaviyo syntax | Shopify Liquid syntax |
|---|---|---|
| Print a variable | `{{ event.customer.first_name }}` | `{{ customer.first_name }}` |
| Format currency | `${{ price\|floatformat:2 }}` | `{{ price \| money }}` |
| Conditional | `{% if %}` | `{% if %}` (same) |
| Loop items | `{% for item in event.extra.line_items %}` | `{% for line in line_items %}` |
| Image URL with size | `{{ item.product.images.0.src }}` | `{{ line.image \| img_url: 'medium' }}` |
| Unsubscribe footer | `{% unsubscribe %}` | None — transactional emails don't unsubscribe |

The HTML below uses **Shopify Liquid syntax only.** Do not copy these into Klaviyo — they won't render.

---

## Where to paste in Shopify

| Template | Location |
|---|---|
| Order Confirmation | Shopify Admin → **Settings** → **Notifications** → **Order confirmation** → click **"Edit code"** |
| Shipping Confirmation | Shopify Admin → **Settings** → **Notifications** → **Shipping confirmation** → click **"Edit code"** |

For each template:

1. Click the notification name
2. Click **"Edit code"** in the top-right
3. Two editors appear: **Email subject** and **Email body**
4. Update the subject line (paste from below)
5. **Replace the entire HTML body** with the HTML below
6. Click **"Send test"** to send yourself a preview (uses your most recent order as test data)
7. Open the test email on desktop + mobile and verify
8. Click **Save**

> ⚠️ **Backup the originals first.** Before editing each template, click **"Revert to default"** to confirm the default exists as a fallback, then copy the current HTML to a text file just in case. Shopify also has a built-in "Revert to default" button if you need to start over.

---

## Style locked (matches Klaviyo stack)

| Element | Spec |
|--------|------|
| Primary headline | Bebas Neue, uppercase, letter-spacing 0.04em, line-height 1.0 |
| Subtitle / accent line | Cormorant Garamond italic, 18–20px, hunter green #355E3B |
| Body | Poppins 400, 14px, line-height 1.85 |
| Eyebrow | Poppins 700, 11px, letter-spacing 0.18em, uppercase, gold #B08D57 |
| Button | Poppins 700, ink bg #1A1A1A, stone text, letter-spacing 0.1em |
| Top bar | Ink #1A1A1A bg, gold #B08D57 text, 10px, letter-spacing 0.2em, uppercase |
| Cream background | #F2EDE4 |
| Brass / gold accent | #B08D57 |
| Hunter green | #355E3B (italic serif accents only) |

---

# Order Confirmation

## Email subject

```
Order {{ order_name }} confirmed
```

## Email body (HTML)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light only">
<meta name="supported-color-schemes" content="light only">
<title>Order {{ order_name }} confirmed</title>
<style>
  :root { color-scheme: light only; supported-color-schemes: light only; }
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
    .ay-line-img { width:80px !important; height:80px !important; max-width:80px !important; }
    .ay-line-text { padding:14px 16px !important; }
    .ay-line-name { font-size:12px !important; }
    .ay-totals-pad { padding:18px 22px !important; }
    .ay-order-ref-num { font-size:28px !important; }
  }
  /* Force Gmail/Outlook dark-mode to leave our footer alone */
  [data-ogsc] .ay-dark-footer, [data-ogsb] .ay-dark-footer { background:#1A1A1A !important; }
  [data-ogsc] .ay-dark-footer * { color:#FFFFFF !important; }
</style>
</head>
<body style="margin:0;padding:0;background:#F2EDE4;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Order Confirmed &middot; Free Engraving &middot; Free U.S. Shipping &middot; Lifetime Warranty</p>
          </td>
        </tr>

        <!-- LOGO -->
        <tr>
          <td align="center" style="padding:36px 24px 8px 24px;border-bottom:1px solid #D4CDC0;">
            <p style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:30px;letter-spacing:5px;color:#1A1A1A;font-weight:400;">AYDINS<span style="color:#B08D57;">.</span></p>
          </td>
        </tr>

        <!-- EYEBROW + HEADLINE -->
        <tr>
          <td class="ay-pad" style="padding:48px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Order Confirmed</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:64px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Order<br>confirmed.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">Thank you, {{ customer.first_name | default: 'friend' }}.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 16px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">We've received your order, and it just landed on the bench. Here's everything that's coming your way.</p>
            <p style="margin:0;">A separate note from the shop is on its way to your inbox with what to expect next.</p>
          </td>
        </tr>

        <!-- ORDER REFERENCE CARD -->
        <tr>
          <td class="ay-pad" style="padding:16px 40px 0 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#1A1A1A;">
              <tr>
                <td style="padding:22px 28px;" align="left">
                  <p style="margin:0 0 6px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;">Your Order Number</p>
                  <p class="ay-order-ref-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:34px;letter-spacing:2.5px;color:#FFFFFF;font-weight:400;line-height:1;">{{ order_name }}</p>
                </td>
              </tr>
            </table>
            <p style="margin:8px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.5;">Reference this number if you reach out to the shop.</p>
          </td>
        </tr>

        <!-- ORDER ITEMS -->
        <tr>
          <td class="ay-pad" style="padding:16px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 14px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">Your Order</p>
            {% for line in line_items %}
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;margin:0 0 12px 0;table-layout:fixed;">
              <tr>
                <td width="100" style="padding:0;vertical-align:middle;width:100px;">
                  {% if line.image %}
                  <img src="{{ line.image | img_url: 'medium' }}" width="100" alt="{{ line.title }}" class="ay-line-img" style="display:block;width:100px;max-width:100px;height:100px;object-fit:cover;border:0;">
                  {% endif %}
                </td>
                <td class="ay-line-text" style="padding:16px 20px;vertical-align:middle;word-break:break-word;overflow-wrap:break-word;">
                  <p class="ay-line-name" style="margin:0 0 6px 0;font-family:'Poppins',-apple-system,sans-serif;font-size:13px;letter-spacing:0.3px;color:#1A1A1A;font-weight:600;line-height:1.4;">{{ line.title }}</p>
                  {% if line.variant_title and line.variant_title != "Default Title" %}
                  <p style="margin:0 0 6px 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;letter-spacing:0.5px;">{{ line.variant_title }}</p>
                  {% endif %}
                  {% if line.quantity > 1 %}
                  <p style="margin:0 0 6px 0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#999090;text-transform:uppercase;font-weight:600;">Qty {{ line.quantity }}</p>
                  {% endif %}
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:14px;color:#1A1A1A;font-weight:600;letter-spacing:0.3px;">{{ line.final_line_price | money }}</p>
                </td>
              </tr>
            </table>
            {% endfor %}
          </td>
        </tr>

        <!-- TOTALS BLOCK -->
        <tr>
          <td class="ay-pad" style="padding:16px 40px 0 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;">
              <tr>
                <td class="ay-totals-pad" style="padding:24px 28px;" align="left">
                  <p style="margin:0 0 14px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;">Order Summary</p>
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="font-family:'Poppins',sans-serif;font-size:13px;color:#666060;">
                    <tr>
                      <td style="padding:6px 0;">Subtotal</td>
                      <td align="right" style="padding:6px 0;color:#1A1A1A;font-weight:500;">{{ subtotal_price | money }}</td>
                    </tr>
                    {% if discounts %}
                    {% for discount in discounts %}
                    <tr>
                      <td style="padding:6px 0;color:#355E3B;">Discount ({{ discount.code }})</td>
                      <td align="right" style="padding:6px 0;color:#355E3B;font-weight:500;">-{{ discount.savings | money }}</td>
                    </tr>
                    {% endfor %}
                    {% endif %}
                    <tr>
                      <td style="padding:6px 0;">Shipping</td>
                      <td align="right" style="padding:6px 0;color:#1A1A1A;font-weight:500;">{% if shipping_price > 0 %}{{ shipping_price | money }}{% else %}Free{% endif %}</td>
                    </tr>
                    {% if tax_price > 0 %}
                    <tr>
                      <td style="padding:6px 0;">Tax</td>
                      <td align="right" style="padding:6px 0;color:#1A1A1A;font-weight:500;">{{ tax_price | money }}</td>
                    </tr>
                    {% endif %}
                    <tr>
                      <td style="padding:14px 0 0 0;border-top:1px solid #D4CDC0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:18px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;">Total</td>
                      <td align="right" style="padding:14px 0 0 0;border-top:1px solid #D4CDC0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:18px;letter-spacing:1.5px;color:#1A1A1A;">{{ total_price | money }}</td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- SHIPPING ADDRESS -->
        {% if shipping_address %}
        <tr>
          <td class="ay-pad" style="padding:16px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">Shipping To</p>
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;color:#1A1A1A;line-height:1.7;">
              {{ shipping_address.name }}<br>
              {{ shipping_address.address1 }}{% if shipping_address.address2 != blank %}<br>{{ shipping_address.address2 }}{% endif %}<br>
              {{ shipping_address.city }}, {{ shipping_address.province_code }} {{ shipping_address.zip }}<br>
              {{ shipping_address.country }}
            </p>
          </td>
        </tr>
        {% endif %}

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 24px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ order_status_url }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">View Your Order &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Questions on your order? Reply to this email or call 1-800-214-7345. A real person reads every one.</p>
          </td>
        </tr>

        <!-- TRUST BAR -->
        <tr>
          <td style="background:#FFFFFF;border-top:1px solid #D4CDC0;border-bottom:1px solid #D4CDC0;padding:0;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td width="50%" style="padding:24px 24px;border-right:1px solid #D4CDC0;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Free Shipping</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">All U.S. orders, always</p>
                </td>
                <td width="50%" style="padding:24px 24px;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Lifetime Warranty</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">On every ring we sell</p>
                </td>
              </tr>
              <tr>
                <td width="50%" style="padding:24px 24px;border-right:1px solid #D4CDC0;border-top:1px solid #D4CDC0;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">30-Day Returns</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">Free size exchanges</p>
                </td>
                <td width="50%" style="padding:24px 24px;border-top:1px solid #D4CDC0;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Free Engraving</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">On any order</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- FOOTER -->
        <tr>
          <td class="ay-dark-footer" style="background:#1A1A1A;padding:48px 40px 32px 40px;" align="center" bgcolor="#1A1A1A">
            <p style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:24px;letter-spacing:5px;color:#FFFFFF;font-weight:400;">AYDINS</p>
            <p style="margin:0 0 20px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:16px;font-style:italic;color:#B08D57;letter-spacing:1px;">Out of the ordinary.</p>
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;color:#A8A096;letter-spacing:1px;line-height:1.7;">
              sales@shopaydins.com &nbsp;&middot;&nbsp; 1-800-214-7345
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>
```

---

# Shipping Confirmation

## Email subject

```
Order {{ order_name }} shipped
```

## Email body (HTML)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light only">
<meta name="supported-color-schemes" content="light only">
<title>Order {{ order_name }} shipped</title>
<style>
  :root { color-scheme: light only; supported-color-schemes: light only; }
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
    .ay-line-img { width:80px !important; height:80px !important; max-width:80px !important; }
    .ay-line-text { padding:14px 16px !important; }
    .ay-line-name { font-size:12px !important; }
    .ay-track-pad { padding:24px 22px !important; }
    .ay-track-headline { font-size:30px !important; letter-spacing:1px !important; }
    .ay-order-ref-num { font-size:28px !important; }
  }
  [data-ogsc] .ay-dark-footer, [data-ogsb] .ay-dark-footer { background:#1A1A1A !important; }
  [data-ogsc] .ay-dark-footer * { color:#FFFFFF !important; }
</style>
</head>
<body style="margin:0;padding:0;background:#F2EDE4;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Order Shipped &middot; Free Engraving &middot; Lifetime Warranty &middot; 30-Day Returns</p>
          </td>
        </tr>

        <!-- LOGO -->
        <tr>
          <td align="center" style="padding:36px 24px 8px 24px;border-bottom:1px solid #D4CDC0;">
            <p style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:30px;letter-spacing:5px;color:#1A1A1A;font-weight:400;">AYDINS<span style="color:#B08D57;">.</span></p>
          </td>
        </tr>

        <!-- EYEBROW + HEADLINE -->
        <tr>
          <td class="ay-pad" style="padding:48px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">On Its Way</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:64px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">It's<br>shipped.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">Tracking is below, {{ customer.first_name | default: 'friend' }}.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0;">Your order just left the shop. Here's where to follow it.</p>
          </td>
        </tr>

        <!-- ORDER REFERENCE CARD -->
        <tr>
          <td class="ay-pad" style="padding:16px 40px 0 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;">
              <tr>
                <td style="padding:18px 24px;" align="left">
                  <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">Order Number</p>
                  <p class="ay-order-ref-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:32px;letter-spacing:2px;color:#1A1A1A;font-weight:400;line-height:1;">{{ order_name }}</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- TRACKING PANEL -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 0 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#1A1A1A;">
              <tr>
                <td class="ay-track-pad" style="padding:30px 30px;" align="left">
                  <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;">Tracking Information</p>
                  {% if fulfillment.tracking_company %}
                  <p class="ay-track-headline" style="margin:0 0 6px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:32px;letter-spacing:2px;color:#FFFFFF;font-weight:400;line-height:1;text-transform:uppercase;">{{ fulfillment.tracking_company }}</p>
                  {% endif %}
                  {% if fulfillment.tracking_number %}
                  <p style="margin:0 0 18px 0;font-family:'Poppins',sans-serif;font-size:13px;color:rgba(255,255,255,0.7);letter-spacing:0.5px;">Tracking #: <span style="color:#C9A84C;font-weight:600;letter-spacing:1px;">{{ fulfillment.tracking_number }}</span></p>
                  {% endif %}
                  {% if fulfillment.tracking_url %}
                  <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                      <td style="background:#B08D57;padding:14px 28px;">
                        <a href="{{ fulfillment.tracking_url }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:11px;letter-spacing:2px;color:#1A1A1A;text-decoration:none;text-transform:uppercase;font-weight:700;">Track Package &rarr;</a>
                      </td>
                    </tr>
                  </table>
                  {% endif %}
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- SHIPPED ITEMS -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 14px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">In This Shipment</p>
            {% for line in fulfillment.line_items %}
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;margin:0 0 12px 0;table-layout:fixed;">
              <tr>
                <td width="100" style="padding:0;vertical-align:middle;width:100px;">
                  {% if line.image %}
                  <img src="{{ line.image | img_url: 'medium' }}" width="100" alt="{{ line.title }}" class="ay-line-img" style="display:block;width:100px;max-width:100px;height:100px;object-fit:cover;border:0;">
                  {% endif %}
                </td>
                <td class="ay-line-text" style="padding:16px 20px;vertical-align:middle;word-break:break-word;overflow-wrap:break-word;">
                  <p class="ay-line-name" style="margin:0 0 6px 0;font-family:'Poppins',-apple-system,sans-serif;font-size:13px;letter-spacing:0.3px;color:#1A1A1A;font-weight:600;line-height:1.4;">{{ line.title }}</p>
                  {% if line.variant_title and line.variant_title != "Default Title" %}
                  <p style="margin:0 0 6px 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;letter-spacing:0.5px;">{{ line.variant_title }}</p>
                  {% endif %}
                  {% if line.quantity > 1 %}
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#999090;text-transform:uppercase;font-weight:600;">Qty {{ line.quantity }}</p>
                  {% endif %}
                </td>
              </tr>
            </table>
            {% endfor %}
          </td>
        </tr>

        <!-- VIEW ORDER CTA -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 24px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ order_status_url }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">View Order Details &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Something looks off? Reply to this email or call 1-800-214-7345. A real person reads every one.</p>
          </td>
        </tr>

        <!-- TRUST BAR -->
        <tr>
          <td style="background:#FFFFFF;border-top:1px solid #D4CDC0;border-bottom:1px solid #D4CDC0;padding:0;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td width="50%" style="padding:24px 24px;border-right:1px solid #D4CDC0;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Free Shipping</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">All U.S. orders, always</p>
                </td>
                <td width="50%" style="padding:24px 24px;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Lifetime Warranty</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">On every ring we sell</p>
                </td>
              </tr>
              <tr>
                <td width="50%" style="padding:24px 24px;border-right:1px solid #D4CDC0;border-top:1px solid #D4CDC0;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">30-Day Returns</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">Free size exchanges</p>
                </td>
                <td width="50%" style="padding:24px 24px;border-top:1px solid #D4CDC0;" align="left">
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Free Engraving</p>
                  <p style="margin:3px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;">On any order</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- FOOTER -->
        <tr>
          <td class="ay-dark-footer" style="background:#1A1A1A;padding:48px 40px 32px 40px;" align="center" bgcolor="#1A1A1A">
            <p style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:24px;letter-spacing:5px;color:#FFFFFF;font-weight:400;">AYDINS</p>
            <p style="margin:0 0 20px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:16px;font-style:italic;color:#B08D57;letter-spacing:1px;">Out of the ordinary.</p>
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;color:#A8A096;letter-spacing:1px;line-height:1.7;">
              sales@shopaydins.com &nbsp;&middot;&nbsp; 1-800-214-7345
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>
```

---

## After you paste — sanity check

For each template, after pasting and saving:

- [ ] Click **"Send test"** in the Shopify admin and confirm the email arrives in your inbox
- [ ] Desktop preview shows the Bebas headline + Cormorant subtitle correctly
- [ ] Mobile preview (open the test email on your phone) shows the layout scaling cleanly — no overflow
- [ ] Order number renders correctly (e.g., `#1001` not `{{ order_name }}` raw)
- [ ] Line items appear with images, names, variant titles (if applicable), and prices
- [ ] Order Confirmation: totals block adds up correctly — Subtotal + Shipping + Tax = Total
- [ ] Order Confirmation: discount line only appears if a discount code was used (test with and without)
- [ ] Order Confirmation: shipping address displays correctly
- [ ] Shipping Confirmation: tracking carrier + tracking number both render
- [ ] Shipping Confirmation: "Track Package" button click-through opens the carrier's tracking page
- [ ] Footer reads "A small jewelry shop. Free engraving on every order."
- [ ] No raw `{{ }}` template syntax visible anywhere in the rendered email

## Common Liquid filter gotchas

| Variable | What it returns | Notes |
|---|---|---|
| `{{ order_name }}` | `#1001` (with the #) | Use this, not `order_number` |
| `{{ total_price \| money }}` | `$169.00` | `\| money` adds the currency symbol |
| `{{ total_price }}` (no filter) | `16900` (in cents) | Always pipe through `\| money` for display |
| `{{ line.image \| img_url: 'medium' }}` | Resized image URL | Sizes: `small`, `medium`, `large`, `original` |
| `{{ shipping_price > 0 }}` | true / false | Used to show "Free" when shipping_price is 0 |
| `{% if line.variant_title != "Default Title" %}` | Hides the literal "Default Title" Shopify uses for products with no variants | Important — otherwise customers see "Default Title" on simple products |

## What this gets you

- Customers receive a continuous branded experience: Klaviyo Thank You → Shopify Order Confirmation (now branded) → Klaviyo email touchpoints → Shopify Shipping Confirmation (now branded) — all in the same visual language
- Shopify still owns receipt math and tracking data (no risk of incorrect totals or missing tracking numbers)
- No dual-send risk (you didn't build Klaviyo versions)
- Aesthetically continuous with the Welcome, AC, Thank You, Browse, and Winback flows

## Other Shopify notification templates worth updating (optional, later)

Same shell can be applied to these whenever you have 15 minutes per template:

- **Order canceled** — customer needs reassurance and a refund timeline
- **Refund notification** — confirms refund amount and timing
- **Customer account invite** — first impression for customers creating accounts post-purchase
- **Customer account welcome** — second touchpoint for new account holders
- **Draft order invoice** — for custom orders sent as draft orders

Tell me when you want any of those rebuilt and we'll batch them.

## When this is done

Reply "Shopify templates done" and we can move to the next thing — the `.claude/page-rewrites/` audit was the parallel track that was queued, or you can pick a different priority. Klaviyo + Shopify transactional are both fully aligned at that point.
