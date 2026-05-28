# (C) Checkout — Order Status Page Additional Scripts

> These scripts belong in **Shopify Admin → Settings → Checkout → Order status page → Additional Scripts** — NOT in the theme. They only fire on the Shopify-hosted thank-you page, where theme.liquid doesn't load. Keeping them here decouples tracking from any future theme migration.

> Cleans up 3 broken scripts from the v4 `theme.liquid`:
> - Bing enhanced conversions had `contoso@example.com` placeholder → now uses `{{ customer.email }}`
> - Bing purchase event had `REPLACE_WITH_PRODUCT_ID` → now uses real order vars
> - Google Customer Reviews opt-in had hardcoded 2023 order/email → now uses `{{ order.name }}` / `{{ order.email }}`

---

## Paste this entire block into the Additional Scripts field

```html
{% if first_time_accessed %}
<!-- ============================================== -->
<!-- Microsoft Bing UET — Purchase Conversion Event -->
<!-- ============================================== -->
<script>
  window.uetq = window.uetq || [];

  {% if customer %}
  // Enhanced conversions: identify the customer
  window.uetq.push('set', { 'pid': {
    'em': '{{ customer.email | default: order.email }}',
    'ph': '{{ customer.default_address.phone | default: "" }}'
  }});
  {% else %}
  window.uetq.push('set', { 'pid': {
    'em': '{{ order.email | default: "" }}'
  }});
  {% endif %}

  // Fire purchase event with real order data
  window.uetq.push('event', 'PRODUCT_PURCHASE', {
    "ecomm_prodid": [{% for line in order.line_items %}"{{ line.product_id }}"{% unless forloop.last %},{% endunless %}{% endfor %}],
    "ecomm_pagetype": "PURCHASE",
    "revenue_value": {{ order.total_price | money_without_currency | remove: ',' }},
    "currency": "{{ shop.currency }}",
    "transaction_id": "{{ order.order_number }}"
  });
</script>

<!-- ============================================== -->
<!-- Google Customer Reviews — Opt-In Survey -->
<!-- Merchant ID: 122065428 -->
<!-- ============================================== -->
<script src="https://apis.google.com/js/platform.js?onload=renderOptIn" async defer></script>
<script>
  window.___gcfg = { lang: '{{ request.locale.iso_code | default: "en" }}' };

  window.renderOptIn = function() {
    window.gapi.load('surveyoptin', function() {
      window.gapi.surveyoptin.render({
        "merchant_id": 122065428,
        "order_id": "{{ order.name }}",
        "email": "{{ order.email }}",
        "delivery_country": "{{ order.shipping_address.country_code | default: 'US' }}",
        "estimated_delivery_date": "{{ 'now' | date: '%s' | plus: 604800 | date: '%Y-%m-%d' }}",
        "products": [
          {% for line in order.line_items %}
          { "gtin": "{{ line.sku | default: line.variant_id }}" }{% unless forloop.last %},{% endunless %}
          {% endfor %}
        ]
      });
    });
  };
</script>
{% endif %}
```

---

## What each block does

| Block | Purpose | Fires when |
|---|---|---|
| `{% if first_time_accessed %}` | Ensures scripts only run once per order (not on refresh) | Shopify native |
| `uetq.push('set', 'pid')` | Bing Ads enhanced conversions — hashes customer email/phone for match-rate | Thank-you page |
| `uetq.push('event', 'PRODUCT_PURCHASE')` | Bing purchase conversion — real product IDs, revenue, order number | Thank-you page |
| `gapi.surveyoptin.render` | Google Customer Reviews — email customer 7 days later asking for a review | Thank-you page |

## Verify after pasting

1. Place a $1 test order (or refund afterward)
2. On the thank-you page: **DevTools → Network → filter `bat.js`** → should see a request firing with `ti=187151969`
3. **DevTools → Network → filter `platform.js`** → Google survey opt-in should load
4. In Bing Ads → **Conversion tracking → UET tag 187151969** → the purchase event should show up within 24h

## If it breaks

- `{{ order.line_items }}` is only available on the Shopify-hosted order status page — not theme product pages
- If you see `undefined` in Liquid output, the script was put in the wrong place (theme vs checkout). Must be in **Settings → Checkout → Order status page**.
- Google Customer Reviews requires Merchant Center ID `122065428` to still be linked — verify in Google Merchant Center if reviews stop flowing.
