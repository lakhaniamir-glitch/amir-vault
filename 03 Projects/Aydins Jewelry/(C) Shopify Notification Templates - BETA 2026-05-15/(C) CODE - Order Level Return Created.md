---
template: Shopify Order Level Return Created
paste-into: Shopify Admin → Settings → Notifications → Customer notifications → Order level return created
source-file: aydins-order-level-return-created-shopify.html
version: V1 (built 2026-05-17)
---

# Paste-Ready Code: Order Level Return Created

**How to use:** Copy everything inside the code block below. In Shopify, replace the entire email body of the **Order level return created** template, then **Save**. **Preview** before going live.

```liquid
{% comment %}
Aydins Jewelry - Shopify Order level return created notification template
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
  <title>Return started for {{ order_label }}: {{ shop.name }}</title>
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
        <h1>Return started for order {{ order_label }}.</h1>
        <p>Hi {{ customer_name }},</p>
        <p>We have created a return for your entire order. The details are below.</p>

        {% if return.return_line_items %}
          <div class="panel">
            <h2>Items being returned</h2>
            {% for line in return.return_line_items %}
              <table class="item" role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="{% if forloop.first %}border-top:0;{% else %}border-top:1px solid #ded6c9;{% endif %}">
                <tr>
                  <td width="80" valign="top" style="padding:14px 14px 14px 0;">
                    {% if line.line_item.image %}
                      <img src="{{ line.line_item | img_url: 'compact' }}" alt="{{ line.line_item.title | escape }}" width="72" height="72" style="display:block;border:1px solid #ded6c9;background:#fffaf2;">
                    {% endif %}
                  </td>
                  <td valign="top" style="padding:14px 0;">
                    <p style="font-size:14px;color:#2b2723;margin:0 0 4px;">{{ line.line_item.title }} × {{ line.quantity }}</p>
                    {% if line.line_item.variant_title != blank and line.line_item.variant_title != 'Default Title' %}<p style="font-size:12px;color:#746b61;margin:0;">{{ line.line_item.variant_title }}</p>{% endif %}
                  </td>
                </tr>
              </table>
            {% endfor %}
          </div>
        {% endif %}

        {% if order_status_url %}
          <p><a class="button" href="{{ order_status_url }}">View order</a></p>
        {% endif %}

        <div class="panel">
          <h2>What happens next</h2>
          <p>Once we receive the package and inspect the items, we will issue your refund or credit per the return terms agreed for this order.</p>
          <p class="muted">Note: returns are accepted within 30 days. Engraved pieces are not eligible for refund (only exchange). A restocking fee may apply per our policy.</p>
        </div>

        <p>Reply to this email with any questions before you ship the package back.</p>
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
