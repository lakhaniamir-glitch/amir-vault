# Patch A: Retrofit Product Images on the 7 Existing Templates

> **Handoff date:** 2026-05-16
> **From:** Claudian (vault-side Claude)
> **To:** BETA (OpenClaw orchestrator)
> **Re:** Naming collision. Patch-3 was misread as Phase 3. Re-issuing under a non-numeric label. This is NOT a new phase. This is a retrofit on 7 files you already built.

---

## Read this first

I previously issued two image-related handoffs:

- **Patch-2** (2026-05-16 00:21 UTC) — add product images on order confirmation + shipping confirmation
- **Patch-3** (2026-05-16 00:23 UTC) — consolidated: apply images to all 7 templates with line items

Then at 00:25 UTC you built the 3 account-management templates (customer welcome, customer activation, password reset) and reported "V3 / Phase 3 done." Those 3 are compliant and good to ship. But you skipped both Patch-2 and Patch-3. The 7 templates with line items still have zero product images.

That's because "Patch-3" collided with "Phase 3" in the roadmap numbering. **My fault for the naming.** Re-issuing as **Patch A** so there's no number to confuse with a phase.

---

## What Patch A does

**Apply the product-image rule to these 7 templates only.** This is a retrofit on existing files, not a new build phase. Account-management templates (Phase 3) are skipped — no line items, no images needed.

| File | Current state | Action |
|---|---|---|
| `aydins-order-confirmation-shopify.html` | no images | add Pattern A |
| `aydins-shipping-confirmation-shopify.html` | no images | add Pattern B |
| `aydins-out-for-delivery-shopify.html` | no images | add Pattern B |
| `aydins-shipping-update-shopify.html` | no images | add Pattern B |
| `aydins-order-edited-shopify.html` | no images | add Pattern A (or B if loop uses fulfillment context) |
| `aydins-order-cancelled-shopify.html` | no images | add Pattern A (or B if loop uses fulfillment context) |
| `aydins-order-refund-shopify.html` | no images | add Pattern C |

---

## Image spec (locked, applies to all 7 templates)

| Property | Value |
|---|---|
| Source filter | `img_url: 'compact'` (Shopify 160×160 thumbnail) |
| Render size | 72×72 px (`width="72" height="72"`) |
| Border | `1px solid #ded6c9` |
| Background | `#fffaf2` (handles transparent PNGs gracefully) |
| Guard | `{% if <image_var> %}` so missing images don't break the row |
| Alt text | Product title, escaped |
| Layout | `<table>` with 80-px image cell on the left, content cell on the right. NOT a div. |

---

## Canonical patterns (copy these into the right loop)

### Pattern A — direct line items
Use when the loop is `{% for line in subtotal_line_items %}` or `{% for line in line_items %}`.

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

### Pattern B — fulfillment-wrapped line items
Use when the loop is `{% for line in fulfillment.fulfillment_line_items %}`. Variable references are one level deeper (`line.line_item.*`).

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

### Pattern C — refund line items
Use when the loop is `{% for line in refund_line_items %}` (order refund template).

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

## CSS cleanup

When converting `<div class="item">` blocks to tables, drop these now-moot rules from the `<style>` block on each template:

- `.item { border-top:1px solid #ded6c9; padding:14px 0; }` → border is now inline on the table
- `.item:first-of-type { border-top:0; }` → moot (table rows, not adjacent siblings)

If you want the first row to skip the border-top, gate it inside the loop with `{% if forloop.first %}` and inline `border-top:0` on that first table.

---

## Verification protocol (do this BEFORE reporting back)

Run this on the server, get clean output, then report:

```bash
cd /home/openclaw/.openclaw/agents/beta/shopify/notification-templates/

# 1. Image refs per file (every line-item template should be > 0)
for f in aydins-order-confirmation-shopify.html aydins-shipping-confirmation-shopify.html aydins-out-for-delivery-shopify.html aydins-shipping-update-shopify.html aydins-order-edited-shopify.html aydins-order-cancelled-shopify.html aydins-order-refund-shopify.html; do
  count=$(grep -c 'img_url' $f)
  echo "$f: $count img_url refs"
done

# 2. Image guards present (every <img> wrapped in {% if ... .image %})
for f in aydins-order-confirmation-shopify.html aydins-shipping-confirmation-shopify.html aydins-out-for-delivery-shopify.html aydins-shipping-update-shopify.html aydins-order-edited-shopify.html aydins-order-cancelled-shopify.html aydins-order-refund-shopify.html; do
  echo "=== $f ==="
  grep -A1 '{% if.*\.image' $f | head -4
done

# 3. New timestamps + new hashes
ls -la *.html
md5sum *.html

# 4. Existing rule regression check
for f in *.html; do
  em=$(grep -c '—' $f)
  bare=$(grep -ci 'lifetime warranty' $f | xargs -I {} sh -c "echo {}")
  aydins_lw=$(grep -ci 'Aydins Lifetime Warranty' $f)
  brass=$(grep -c '#B08D57' $f)
  old_gold=$(grep -c '#9a7a45' $f)
  mailing=$(grep -ci 'flower mound\|long prairie\|PMB' $f)
  echo "$f: em=$em aydins_lw=$aydins_lw brass=$brass old_gold=$old_gold mailing=$mailing"
done
```

**Pass criteria for V3:**

| Check | Expected on 7 templates |
|---|---|
| `img_url` refs per template | ≥ 1 (Pattern A) or ≥ 1 (Pattern B/C) |
| `{% if ... .image %}` guards | one per `<img>` |
| New timestamp on all 7 | newer than 2026-05-16 00:25 UTC |
| Em dashes | 0 |
| "Aydins Lifetime Warranty" present, no bare phrase | yes |
| `#B08D57` present, `#9a7a45` absent | yes / yes |
| Mailing address / Flower Mound / PMB | 0 |

Report back with the full output of those scans (not just "passed"). Amir verifies independently after.

---

## Out of scope for Patch A

- Phase 3 account-management templates (customer welcome, customer activation, password reset) — no line items, no images needed. Leave as-is.
- Off-palette neutrals (`#f7f3ec`, `#fffaf2`, `#f2ede4`, `#ded6c9`, `#1f1b18`) — flagged as polish, not blockers. Separate pass.
- Footer reference file (`aydins-footer-shopify-new-design.html`) — design reference only, no images.

Patch A is one focused job: add product images to the 7 line-item templates. Don't expand scope.
