---
template: Shopify Order Invoice
paste-into: Shopify Admin → Settings → Notifications → Customer notifications → Order invoice
source-file: aydins-order-invoice-shopify.html
version: V2 (built 2026-05-17, payment terms patch 2026-05-17)
patch-notes: V2 adds payment_terms block (due date + due-on-fulfillment) per Shopify warning banner. Clears the "Due dates may not show correctly when payment is due on fulfillment" alert.
---

# Paste-Ready Code: Order Invoice

**How to use:** Copy everything inside the code block below. In Shopify, replace the entire email body of the **Order invoice** template, then **Save**. **Preview** before going live.

```liquid
{% comment %}
Aydins Jewelry - Shopify Order invoice notification template
Use in Shopify Admin > Settings > Notifications > Customer notifications.
Built for Shopify notification Liquid variables. Test with Shopify preview before saving live.
{% endcomment %}

{% assign customer_name = shipping_address.first_name | default: billing_address.first_name | default: customer.first_name | default: 'there' %}
{% assign order_label = order_name | default: name %}

<!doctype html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <meta name="color-scheme" content="only light">
  <meta name="supported-color-schemes" content="only light">
  <title>Invoice for {{ order_label }}: {{ shop.name }}</title>
  <!--[if mso]>
  <xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml>
  <style>body,table,td,p,a,span{font-family:Arial,Helvetica,sans-serif!important;}h1,h2,.brand{font-family:Georgia,'Times New Roman',serif!important;}</style>
  <![endif]-->
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    body { margin:0; padding:0; background:#f7f3ec; color:#2b2723; font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    table { border-collapse:collapse; }
    img { border:0; max-width:100%; display:block; }
    a { color:#2b2723; }
    .wrap { width:100%; background:#f7f3ec; padding:28px 12px; }
    .container { width:100%; max-width:680px; margin:0 auto; background:#fffaf2; border:1px solid #ded6c9; }
    .topbar { font-size:12px; letter-spacing:.5px; color:#6b6258; padding:14px 28px; text-align:center; border-bottom:1px solid #ded6c9; }
    .header { padding:34px 34px 18px; text-align:center; }
    .brand { font-family: Georgia, 'Times New Roman', serif; font-size:34px; letter-spacing:5px; color:#1d1a17; margin:0; }
    .tagline { margin:8px 0 0; font-family:Poppins,Arial,Helvetica,sans-serif; font-size:12px; letter-spacing:2px; text-transform:uppercase; color:#B08D57; }
    .content { padding:18px 38px 8px; }
    h1 { font-family: Georgia, 'Times New Roman', serif; font-size:34px; line-height:1.15; margin:0 0 18px; color:#1d1a17; font-weight:500; }
    p { font-size:15px; line-height:1.7; margin:0 0 16px; color:#4c453e; }
    .button { display:inline-block; background:#1f1b18; color:#fffaf2 !important; text-decoration:none; padding:15px 24px; font-size:13px; letter-spacing:1.5px; text-transform:uppercase; margin:10px 0 18px; }
    .panel { background:#f2ede4; border:1px solid #ded6c9; padding:22px; margin:20px 0; }
    .panel h2 { font-family: Georgia, 'Times New Roman', serif; font-size:22px; margin:0 0 12px; font-weight:500; color:#1d1a17; }
    .muted { color:#746b61; font-size:13px; }
    .totals { width:100%; margin:12px 0 0; }
    .totals td { padding:6px 0; font-size:14px; color:#4c453e; }
    .totals .right { text-align:right; }
    .total td { border-top:1px solid #ded6c9; padding-top:12px; font-size:16px; font-weight:bold; color:#1d1a17; }
    .footer { padding:26px 38px 34px; text-align:center; color:#746b61; font-size:12px; line-height:1.7; }
    @media screen and (max-width:600px) { .content,.footer { padding-left:22px!important; padding-right:22px!important; } .header { padding-left:22px!important; padding-right:22px!important; } h1 { font-size:29px!important; } }
    @media (prefers-color-scheme: dark) {
      body, .wrap { background:#f7f3ec !important; color:#2b2723 !important; }
      .container { background:#fffaf2 !important; border-color:#ded6c9 !important; }
      .panel { background:#f2ede4 !important; border-color:#ded6c9 !important; }
      .brand, h1, .panel h2 { color:#1d1a17 !important; }
      p { color:#4c453e !important; }
      .tagline { color:#B08D57 !important; }
      .muted, .topbar { color:#6b6258 !important; }
      .footer { color:#746b61 !important; }
      .button { background:#1f1b18 !important; color:#fffaf2 !important; }
      a { color:#2b2723 !important; }
    }
    [data-ogsc] body, [data-ogsc] .wrap { background:#f7f3ec !important; }
    [data-ogsc] .container { background:#fffaf2 !important; }
    [data-ogsc] .panel { background:#f2ede4 !important; }
    [data-ogsc] h1, [data-ogsc] .brand, [data-ogsc] .panel h2 { color:#1d1a17 !important; }
    [data-ogsc] p { color:#4c453e !important; }
    [data-ogsc] .tagline { color:#B08D57 !important; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="container">
      <div class="topbar">Free engraving · Free U.S. shipping · Aydins Lifetime Warranty · 30-day returns</div>
      <div class="header">
        <p class="brand">AYDINS</p>
        <p class="tagline">Wedding Bands, Made Personal</p>
      </div>

      <div class="content">
        <h1>Invoice for {{ order_label }}.</h1>
        <p>Hi {{ customer_name }},</p>
        <p>Here is the invoice for your Aydins order. Use the button below to complete payment.</p>

        {% comment %} Payment terms: shows due date or "due on fulfillment" per Shopify guidance. {% endcomment %}
        {% assign due_date = payment_terms.next_payment.due_at | default: nil %}
        {% if payment_terms.type == 'receipt' and due_date == nil %}
          {% assign due_date = 'now' %}
        {% endif %}

        {% if payment_terms %}
          <div class="panel">
            {% if payment_terms.type == 'fulfillment' and payment_terms.next_payment.due_at == nil %}
              <h2>Payment of {{ order.total_outstanding | money }} is due on fulfillment</h2>
            {% else %}
              <h2>Payment of {{ order.total_outstanding | money }} is due {{ due_date | date: format: 'date' }}</h2>
            {% endif %}
            {% if payment_terms.name %}
              <p class="muted" style="margin:0;">Terms: {{ payment_terms.name }}</p>
            {% endif %}
          </div>
        {% endif %}

        {% if invoice_url %}
          <p><a class="button" href="{{ invoice_url }}">Pay invoice</a></p>
        {% elsif order_status_url %}
          <p><a class="button" href="{{ order_status_url }}">View order</a></p>
        {% endif %}

        {% if custom_message != blank %}
          <div class="panel">
            <h2>A note from Aydins</h2>
            <p>{{ custom_message | newline_to_br }}</p>
          </div>
        {% endif %}

        {% if subtotal_line_items %}
          <div class="panel">
            <h2>Order summary</h2>
            {% for line in subtotal_line_items %}
              <table class="item" role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="{% if forloop.first %}border-top:0;{% else %}border-top:1px solid #ded6c9;{% endif %}">
                <tr>
                  <td width="80" valign="top" style="padding:14px 14px 14px 0;">
                    {% if line.image %}
                      <img src="{{ line | img_url: 'compact' }}" alt="{{ line.title | escape }}" width="72" height="72" style="display:block;border:1px solid #ded6c9;background:#fffaf2;">
                    {% endif %}
                  </td>
                  <td valign="top" style="padding:14px 0;">
                    <p style="font-size:14px;color:#2b2723;margin:0 0 4px;">{{ line.title }} × {{ line.quantity }}</p>
                    {% if line.variant_title != blank and line.variant_title != 'Default Title' %}<p style="font-size:12px;color:#746b61;margin:0;">{{ line.variant_title }}</p>{% endif %}
                  </td>
                </tr>
              </table>
            {% endfor %}
            <table class="totals" role="presentation">
              {% if subtotal_price %}<tr><td>Subtotal</td><td class="right">{{ subtotal_price | money }}</td></tr>{% endif %}
              {% if total_discounts and total_discounts != 0 %}<tr><td>Discounts</td><td class="right">-{{ total_discounts | money }}</td></tr>{% endif %}
              {% if shipping_price %}<tr><td>Shipping</td><td class="right">{{ shipping_price | money }}</td></tr>{% endif %}
              {% if tax_price %}<tr><td>Tax</td><td class="right">{{ tax_price | money }}</td></tr>{% endif %}
              {% if total_price %}<tr class="total"><td>Total</td><td class="right">{{ total_price | money_with_currency }}</td></tr>{% endif %}
            </table>
          </div>
        {% endif %}

        <p>Reply with any questions. We will hold the order open while you sort payment.</p>
      </div>

      <div class="footer">
        <p style="margin:0 0 8px;font-family:Georgia,'Times New Roman',serif;font-size:24px;letter-spacing:5px;color:#1d1a17;font-weight:600;">AYDINS</p>
        <p style="margin:0 0 14px;font-family:Poppins,Arial,Helvetica,sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#B08D57;font-weight:700;">Wedding Bands, Made Personal</p>
        <p style="margin:0 0 14px;">Free engraving · Free U.S. shipping · Aydins Lifetime Warranty · 30-day returns</p>
        <p style="margin:0 0 14px;"><a href="https://www.instagram.com/aydinsjewelry/">Instagram</a> · <a href="https://www.tiktok.com/@aydinsjewelry">TikTok</a> · <a href="https://www.pinterest.com/AydinsJewelry/">Pinterest</a> · <a href="https://facebook.com/aydinsjewelry">Facebook</a></p>
        <p style="margin:0 0 12px;">Aydins Jewelry · Irving, Texas · Since 2011</p>
        <p style="margin:0;"><a href="https://shopaydins.com/" style="font-weight:700;letter-spacing:1px;">SHOPAYDINS.COM</a><br>Copyright © 2026 Aydins Jewelry. All rights reserved.</p>
      </div>
    </div>
  </div>
</body>
</html>
```
