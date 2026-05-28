# Patch 3: Product Images Across All 7 Templates

> **Handoff date:** 2026-05-16
> **From:** Claudian (vault-side Claude)
> **To:** BETA (OpenClaw orchestrator)
> **Re:** Patch-2 was issued at 00:21 UTC. Phase 2 was already built at 00:19 UTC, so the image rule never landed. Consolidating into Patch-3. Apply the image rule to all 7 templates, run one V3 scan, then report back.

---

## Why this exists

Patch-2 (2026-05-16 00:21 UTC) introduced the product-image rule for every transactional template that displays line items. Two minutes earlier, Phase 2 went out without it. Evidence:

- Server timestamps on the 5 Phase 2 files: 2026-05-16 00:19 UTC (before Patch-2 was uploaded)
- `grep -c "img_url|line.image|line.line_item.image"` across all 7 templates returns 0
- V2 hashes for order conf, shipping conf, and footer are unchanged since 2026-05-16 00:10 UTC

This isn't a blame thing. It's a sequencing thing. Fixing it in one consolidated pass.

---

## The rule (locked, applies forever to all transactional templates with line items)

Every template that loops through line items must render the product image alongside each item. Two-column table layout: image on the left, content on the right. Outlook safe.

**Image spec (locked):**

| Property | Value |
|---|---|
| Source filter | `img_url: 'compact'` (Shopify 160×160 thumbnail, right tradeoff of sharpness vs email weight) |
| Render size | 72×72 px (`width="72" height="72"`) |
| Border | `1px solid #ded6c9` |
| Background | `#fffaf2` (handles transparent PNGs gracefully) |
| Guard | `{% if <image_var> %}` so missing images don't break the row |
| Alt text | Product title, escaped |
| Layout | `<table>` with 80-px image cell on the left, content cell on the right. NOT a div. |

---

## Templates and the exact Liquid variable per template

Use this table to pick the right variable for each loop. The variable depends on whether the loop is over line items directly or over fulfillment-wrapped line items.

| Template | Loop variable (existing) | Image guard | Image src filter | Title path |
|---|---|---|---|---|
| `aydins-order-confirmation-shopify.html` | `subtotal_line_items` | `{% if line.image %}` | `{{ line \| img_url: 'compact' }}` | `{{ line.title }}` |
| `aydins-shipping-confirmation-shopify.html` | `fulfillment.fulfillment_line_items` | `{% if line.line_item.image %}` | `{{ line.line_item \| img_url: 'compact' }}` | `{{ line.line_item.title }}` |
| `aydins-out-for-delivery-shopify.html` | `fulfillment.fulfillment_line_items` (likely) | `{% if line.line_item.image %}` | `{{ line.line_item \| img_url: 'compact' }}` | `{{ line.line_item.title }}` |
| `aydins-shipping-update-shopify.html` | `fulfillment.fulfillment_line_items` (likely) | `{% if line.line_item.image %}` | `{{ line.line_item \| img_url: 'compact' }}` | `{{ line.line_item.title }}` |
| `aydins-order-edited-shopify.html` | check the existing loop — likely `subtotal_line_items` or `line_items` | match it (`line.image` for direct, `line.line_item.image` for wrapped) | match it | match it |
| `aydins-order-cancelled-shopify.html` | likely `subtotal_line_items` or `line_items` | match it | match it | match it |
| `aydins-order-refund-shopify.html` | `refund_line_items` (Shopify wraps these) | `{% if line.line_item.image %}` | `{{ line.line_item \| img_url: 'compact' }}` | `{{ line.line_item.title }}` |

If a Phase 2 template uses a loop variable not listed here, read the existing Liquid, follow the same pattern (direct → `line.image`, wrapped → `line.line_item.image`), and document the variable choice in the V3 report.

---

## Canonical patterns (copy these)

### Pattern A: direct line items (order conf, order edited, order cancelled)

```liquid
{% for line in subtotal_line_items %}
  <table class="item" role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="border-top:1px solid #ded6c9;">
    <tr>
      <td width="80" valign="top" style="padding:14px 14px 14px 0;">
        {% if line.image %}
          <img src="{{ line | img_url: 'compact' }}" alt="{{ line.title | escape }}" width="72" height="72" style="display:block;border:1px solid #ded6c9;background:#fffaf2;">
        {% endif %}
      </td>
      <td valign="top" style="padding:14px 0;">
        <p style="font-size:14px;color:#2b2723;margin:0 0 4px;">{{ line.title }} × {{ line.quantity }}</p>
        {% if line.variant_title != blank and line.variant_title != 'Default Title' %}<p style="font-size:12px;color:#746b61;margin:0;">{{ line.variant_title }}</p>{% endif %}
        {% if line.selling_plan_allocation %}<p style="font-size:12px;color:#746b61;margin:0;">{{ line.selling_plan_allocation.selling_plan.name }}</p>{% endif %}
        {% if line.properties %}
          {% for property in line.properties %}
            {% assign first_character = property.first | slice: 0 %}
            {% unless property.last == blank or first_character == '_' %}
              <p style="font-size:12px;color:#746b61;margin:0;">{{ property.first }}: {{ property.last }}</p>
            {% endunless %}
          {% endfor %}
        {% endif %}
      </td>
    </tr>
  </table>
{% endfor %}
```

### Pattern B: fulfillment-wrapped line items (shipping conf, out-for-delivery, shipping update)

```liquid
{% for line in fulfillment.fulfillment_line_items %}
  <table class="item" role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="border-top:1px solid #ded6c9;">
    <tr>
      <td width="80" valign="top" style="padding:14px 14px 14px 0;">
        {% if line.line_item.image %}
          <img src="{{ line.line_item | img_url: 'compact' }}" alt="{{ line.line_item.title | escape }}" width="72" height="72" style="display:block;border:1px solid #ded6c9;background:#fffaf2;">
        {% endif %}
      </td>
      <td valign="top" style="padding:14px 0;">
        <p style="font-size:14px;color:#2b2723;margin:0 0 4px;">{{ line.line_item.title }} × {{ line.quantity }}</p>
        {% if line.line_item.variant_title != blank and line.line_item.variant_title != 'Default Title' %}<p style="font-size:12px;color:#746b61;margin:0;">{{ line.line_item.variant_title }}</p>{% endif %}
        {% if line.line_item.properties %}
          {% for property in line.line_item.properties %}
            {% assign first_character = property.first | slice: 0 %}
            {% unless property.last == blank or first_character == '_' %}
              <p style="font-size:12px;color:#746b61;margin:0;">{{ property.first }}: {{ property.last }}</p>
            {% endunless %}
          {% endfor %}
        {% endif %}
      </td>
    </tr>
  </table>
{% endfor %}
```

### Pattern C: refund line items (order refund)

```liquid
{% for line in refund_line_items %}
  <table class="item" role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="border-top:1px solid #ded6c9;">
    <tr>
      <td width="80" valign="top" style="padding:14px 14px 14px 0;">
        {% if line.line_item.image %}
          <img src="{{ line.line_item | img_url: 'compact' }}" alt="{{ line.line_item.title | escape }}" width="72" height="72" style="display:block;border:1px solid #ded6c9;background:#fffaf2;">
        {% endif %}
      </td>
      <td valign="top" style="padding:14px 0;">
        <p style="font-size:14px;color:#2b2723;margin:0 0 4px;">{{ line.line_item.title }} × {{ line.quantity }}</p>
        {% if line.line_item.variant_title != blank and line.line_item.variant_title != 'Default Title' %}<p style="font-size:12px;color:#746b61;margin:0;">{{ line.line_item.variant_title }}</p>{% endif %}
        <p style="font-size:12px;color:#746b61;margin:0;">Refund: {{ line.subtotal | money }}</p>
      </td>
    </tr>
  </table>
{% endfor %}
```

---

## Cleanup

When converting `<div class="item">` blocks to tables, drop these now-moot CSS rules from the `<style>` block on each template:

- `.item { border-top:1px solid #ded6c9; padding:14px 0; }` → border is now inline on the table
- `.item:first-of-type { border-top:0; }` → moot (table rows, not adjacent siblings)

If you want the first row to skip the border-top, gate it inside the loop with `{% if forloop.first %}` and inline `border-top:0` on that table.

---

## Delivery and verification

1. Patch all 7 templates on the server: `/home/openclaw/.openclaw/agents/beta/shopify/notification-templates/`
2. New timestamps on all 7
3. Report new md5sum for each (so Amir can verify diff)
4. Run V3 compliance scan covering **everything**, not just the new rule:

### V3 scan checklist

| Check | All 7 templates |
|---|---|
| Product image rendered with `img_url: 'compact'` | required where line items exist |
| `{% if ... .image %}` guard wraps every `<img>` tag | required |
| 72×72 render size, `#ded6c9` 1px border, `#fffaf2` background | required |
| Alt text uses escaped product title | required |
| Two-column table layout (not div) per line item | required |
| No bare "lifetime warranty" — only "Aydins Lifetime Warranty" | required |
| No em dashes (`—`) anywhere | required |
| Tagline color `#B08D57` (not `#9a7a45`) | required |
| Footer embedded inline (no external include) | required |
| No mailing address / Flower Mound in footer | required |
| Irving, Texas in body / brand voice context | required |

Report back with timestamps, new md5sums, and a per-template pass/fail on every row of that checklist. Then Amir signs off on V3 and the set goes live.

---

## Open items / notes

- Account-management templates (customer welcome, customer activation, password reset) are still in Phase 3, not built yet, and do not have line items. The image rule does not apply to them.
- If `img_url: 'compact'` returns broken images in Shopify's preview for any template, fall back to `'small'` (100×100). Document the choice in the V3 report.
- If any Phase 2 template uses a loop variable not covered by patterns A/B/C, document the actual variable choice and the pattern you applied.
