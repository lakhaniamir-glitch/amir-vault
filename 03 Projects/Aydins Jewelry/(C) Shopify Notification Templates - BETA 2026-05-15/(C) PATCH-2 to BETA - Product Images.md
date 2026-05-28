# Patch 2: Product Images on Line Items

> **Handoff date:** 2026-05-16
> **From:** Claudian (vault-side Claude)
> **To:** BETA (OpenClaw orchestrator)
> **Re:** V2 rebuild approved on compliance. One gap to close before Phase 2.

---

## Issue

Neither V2 template renders the product image alongside each line item. For a wedding-band brand, the customer needs to see the ring they ordered. Right now they get a title and a line of meta text. Not enough.

This is also a missing global rule for Phase 2 — every transactional template that displays line items must show product images.

---

## Fix on existing V2 templates

### `aydins-order-confirmation-shopify.html`

Inside the `{% for line in subtotal_line_items %}` loop (currently around line 70-84), wrap the line-item content in a two-column table: image on the left, text on the right. Use Shopify's `img_url` filter on the line item.

**Pattern to apply** (per line item):

```liquid
{% for line in subtotal_line_items %}
  <table class="item" role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="border-top:1px solid #ded6c9;padding:14px 0;">
    <tr>
      <td width="80" valign="top" style="padding:14px 14px 14px 0;">
        {% if line.image %}
          <img src="{{ line | img_url: 'compact' }}" alt="{{ line.title | escape }}" width="72" height="72" style="display:block;border:1px solid #ded6c9;background:#fffaf2;">
        {% endif %}
      </td>
      <td valign="top" style="padding:14px 0;">
        <p class="item-title" style="font-size:14px;color:#2b2723;margin:0 0 4px;">{{ line.title }} × {{ line.quantity }}</p>
        {% if line.variant_title != blank and line.variant_title != 'Default Title' %}<p class="item-meta" style="font-size:12px;color:#746b61;margin:0;">{{ line.variant_title }}</p>{% endif %}
        {% if line.selling_plan_allocation %}<p class="item-meta" style="font-size:12px;color:#746b61;margin:0;">{{ line.selling_plan_allocation.selling_plan.name }}</p>{% endif %}
        {% if line.properties %}
          {% for property in line.properties %}
            {% assign first_character = property.first | slice: 0 %}
            {% unless property.last == blank or first_character == '_' %}
              <p class="item-meta" style="font-size:12px;color:#746b61;margin:0;">{{ property.first }}: {{ property.last }}</p>
            {% endunless %}
          {% endfor %}
        {% endif %}
      </td>
    </tr>
  </table>
{% endfor %}
```

Note: Convert the `<div class="item">` block to a `<table>` so the image-and-text layout holds in Outlook. Keep the existing `.item` border-top behavior on the table.

### `aydins-shipping-confirmation-shopify.html`

Same pattern inside the `{% for line in fulfillment.fulfillment_line_items %}` loop (currently around line 90-103). Adjust the variable reference because fulfillment line items wrap the line item one level deeper:

```liquid
{% for line in fulfillment.fulfillment_line_items %}
  <table class="item" role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="border-top:1px solid #ded6c9;padding:14px 0;">
    <tr>
      <td width="80" valign="top" style="padding:14px 14px 14px 0;">
        {% if line.line_item.image %}
          <img src="{{ line.line_item | img_url: 'compact' }}" alt="{{ line.line_item.title | escape }}" width="72" height="72" style="display:block;border:1px solid #ded6c9;background:#fffaf2;">
        {% endif %}
      </td>
      <td valign="top" style="padding:14px 0;">
        <p class="item-title" style="font-size:14px;color:#2b2723;margin:0 0 4px;">{{ line.line_item.title }} × {{ line.quantity }}</p>
        {% if line.line_item.variant_title != blank and line.line_item.variant_title != 'Default Title' %}<p class="item-meta" style="font-size:12px;color:#746b61;margin:0;">{{ line.line_item.variant_title }}</p>{% endif %}
        {% if line.line_item.properties %}
          {% for property in line.line_item.properties %}
            {% assign first_character = property.first | slice: 0 %}
            {% unless property.last == blank or first_character == '_' %}
              <p class="item-meta" style="font-size:12px;color:#746b61;margin:0;">{{ property.first }}: {{ property.last }}</p>
            {% endunless %}
          {% endfor %}
        {% endif %}
      </td>
    </tr>
  </table>
{% endfor %}
```

Drop the `.item:first-of-type { border-top:0; }` rule from the CSS (the new pattern uses table rows, not adjacent div siblings, so the rule is moot).

---

## New global rule for Phase 2 (and beyond)

**Every transactional template that displays line items must render the product image alongside each item.** Applies to:

- ✅ Order confirmation (patch above)
- ✅ Shipping confirmation (patch above)
- 🔜 Out-for-delivery
- 🔜 Shipping update (carrier change, address change, delays)
- 🔜 Order edited
- 🔜 Order cancelled
- 🔜 Order refund

**Image spec (locked):**
- Source: `line | img_url: 'compact'` (for line item context) or `line.line_item | img_url: 'compact'` (for fulfillment context). `'compact'` is Shopify's 160x160 thumbnail size — right balance between sharpness and email weight.
- Render at 72×72px in the email
- 1px hairline border `#ded6c9` and `background:#fffaf2` (handles transparent PNGs)
- Wrap in `{% if line.image %}` guard so missing images don't break the layout
- Alt text = product title (escaped)
- Two-column table per line item: 80px image cell on left, content on right

Account-management templates (customer welcome, customer activation, password reset) do not have line items, so this rule does not apply to them.

---

## Delivery

- Patch both V2 templates on the server: `/home/openclaw/.openclaw/agents/beta/shopify/notification-templates/`
- Confirm with timestamps + md5sum diff vs the V2 hashes Amir has on file
- Then proceed with Phase 2 templates using the image rule as a hard requirement

---

## V3 compliance scan (run after patch)

Verify each before reporting back:
- `{% if line.image %}` guard present in every line-item loop
- `img_url: 'compact'` filter used (not raw `line.image` which is just a hash)
- Two-column table layout (Outlook safe)
- No regressions on the prior rules: no bare "lifetime warranty", no em dashes, brass `#B08D57` on tagline, no mailing address, footer embedded inline

Hand back to Amir for final sign-off on V3, then unlock Phase 2.
