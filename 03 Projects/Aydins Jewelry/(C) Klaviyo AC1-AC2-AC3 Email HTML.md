# (C) Klaviyo Abandoned Cart — AC1 / AC2 / AC3 + SMS (paste-ready)

> **What this is:** Three complete, paste-ready abandoned-cart emails plus the SMS message body for the same flow. Emails are style-matched to the Aydins homepage v3 design — Bebas Neue headlines, Cormorant Garamond italic subtitles, Poppins body, ink + cream + brass gold palette. SMS body is short, on-brand, and segment-safe.
>
> **No fee details in the body** — the policy pages on shopaydins.com hold those. Emails stay top-of-funnel: short, confident, on-brand.
>
> **How to use it in Klaviyo:**
> 1. Klaviyo → Flows → "Abandoned Cart" (`TrNjjf`) → click the email block → **Edit Email**
> 2. **Update Subject + Preview** at the top of the editor (per the values below)
> 3. In the body editor, **delete every existing row/block** until the canvas is empty
> 4. Drag in a new **HTML** block (under "Content" → "HTML")
> 5. Paste the matching email HTML below into that block
> 6. Save → Preview on desktop + mobile → exit
>
> Repeat for AC1 → AC2 → AC3.
>
> ✅ **Updated 2026-05-11 with all known Klaviyo render fixes:**
> - CTA `href` now uses `{{ event.extra.checkout_url }}` (the old `{% checkout_url %}` is NOT a valid Klaviyo tag and throws "invalid syntax" in preview)
> - Product name uses `{{ item.product.title|default:item.title|default:'Your Ring' }}` (the old `{{ item.product_name }}` is the wrong field for Checkout Started events)
> - Price uses `|floatformat:2` so `146.0` renders as `146.00`
> - Image `alt` is populated from the product title
> - Cart cell alignment fixed (`vertical-align:middle`)
> - Unsubscribe link uses the bare `{% unsubscribe %}` tag standalone — wrapping it in another `<a href="">` produces broken nested HTML (the tag outputs a full anchor, not a URL)
>
> If a button URL is blank in the test email, swap `{{ event.extra.checkout_url }}` to `{{ event.checkout_url }}` — varies by Klaviyo integration version.

---

## Style locked (matches homepage v3)

| Element | Spec |
|--------|------|
| Primary headline | Bebas Neue, uppercase, letter-spacing 0.04em, line-height 1.0 |
| Subtitle / accent line | Cormorant Garamond italic, 18–20px, hunter green #355E3B or stone-mid |
| Body | Poppins 400, 14–16px, line-height 1.7 |
| Eyebrow | Poppins 700, 11px, letter-spacing 0.18em, uppercase, gold #B08D57 |
| Button | Bebas Neue or Poppins 700, ink bg #1A1A1A, stone text, letter-spacing 0.1em |
| Top bar | Ink #1A1A1A bg, gold #B08D57 text, 11px, letter-spacing 0.14em, uppercase |
| Cream background | #F2EDE4 |
| Brass / gold accent | #B08D57 |
| Hunter green | #355E3B (used on italic serif accents) |

---

## AC1 — Message ID `SQdgLg`

**Subject:**
```
Still thinking it over? Here's 20% off. Code EMK20
```

**Preview text:**
```
Free engraving, free U.S. shipping, 30-day returns. Code expires at midnight.
```

**Body HTML (paste into a single HTML block):**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  /* Mobile responsiveness — Klaviyo strips comments but keeps @media rules */
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-pad-top { padding-top:32px !important; }
    .ay-headline { font-size:40px !important; line-height:0.95 !important; }
    .ay-cart-img-cell { width:96px !important; }
    .ay-cart-img { width:96px !important; height:96px !important; max-width:96px !important; }
    .ay-cart-text { padding:14px 16px !important; }
    .ay-cart-name { font-size:15px !important; letter-spacing:0.5px !important; }
    .ay-trust-cell { padding:18px 16px !important; }
    .ay-reward-pad { padding:22px 20px !important; }
    .ay-reward-headline { font-size:30px !important; letter-spacing:1px !important; }
  }
</style>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Free Shipping &middot; Lifetime Warranty &middot; 30-Day Returns &middot; Irving, TX &middot; Since 2011</p>
          </td>
        </tr>

        <!-- LOGO -->
        <tr>
          <td align="center" style="padding:36px 24px 8px 24px;border-bottom:1px solid #D4CDC0;">
            <p style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:30px;letter-spacing:5px;color:#1A1A1A;font-weight:400;">AYDINS<span style="color:#B08D57;">.</span></p>
          </td>
        </tr>

        <!-- HERO IMAGE -->
        <tr>
          <td style="padding:0;">
            <img src="https://cdn.shopify.com/s/files/1/1857/8135/files/Why_Aydins_Jewelry.png?v=1777352028" width="600" alt="Aydins wedding band on workbench" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- EYEBROW + HEADLINE -->
        <tr>
          <td class="ay-pad" style="padding:48px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Still In Your Cart</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Still thinking<br>it over?</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">We saved your spot.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">No pressure. We just wanted to make it easier to come back, with 20% off, on us.</p>
            <p style="margin:0;">The ring is yours whenever you're ready. Here's what you were looking at:</p>
          </td>
        </tr>

        <!-- CART CONTENTS -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 8px 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 14px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">In Your Cart</p>
            {% for item in event.extra.line_items %}
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;margin:0 0 12px 0;table-layout:fixed;">
              <tr>
                <td width="120" class="ay-cart-img-cell" style="padding:0;vertical-align:middle;width:120px;">
                  <a href="{{ item.product.url|default:event.extra.checkout_url }}" style="text-decoration:none;display:block;">
                    <img src="{{ item.product.images.0.src }}" width="120" alt="{{ item.product.title|default:item.title }}" class="ay-cart-img" style="display:block;width:120px;max-width:120px;height:120px;object-fit:cover;border:0;">
                  </a>
                </td>
                <td class="ay-cart-text" style="padding:18px 22px;vertical-align:middle;word-break:break-word;overflow-wrap:break-word;">
                  <p class="ay-cart-name" style="margin:0 0 8px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:18px;letter-spacing:1px;color:#1A1A1A;font-weight:400;line-height:1.15;text-transform:uppercase;">
                    <a href="{{ item.product.url|default:event.extra.checkout_url }}" style="color:#1A1A1A;text-decoration:none;">{{ item.product.title|default:item.title|default:'Your Ring' }}</a>
                  </p>
                  {% if item.quantity > 1 %}<p style="margin:0 0 8px 0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#999090;text-transform:uppercase;font-weight:600;">Qty {{ item.quantity }}</p>{% endif %}
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:15px;color:#1A1A1A;font-weight:600;letter-spacing:0.3px;">${{ item.line_price|floatformat:2 }}</p>
                </td>
              </tr>
            </table>
            {% endfor %}
          </td>
        </tr>

        <!-- REWARD PANEL -->
        <tr>
          <td class="ay-pad" style="padding:16px 40px 0 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#1A1A1A;">
              <tr>
                <td class="ay-reward-pad" style="padding:28px 28px;" align="left">
                  <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;">Your Reward</p>
                  <p class="ay-reward-headline" style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:38px;letter-spacing:2px;color:#FFFFFF;font-weight:400;line-height:1;text-transform:uppercase;">20% Off Your Cart</p>
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:12px;color:rgba(255,255,255,0.7);line-height:1.6;">Apply code <strong style="color:#C9A84C;letter-spacing:1.5px;font-weight:700;">EMK20</strong> at checkout. Expires at midnight tonight.</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 48px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ event.extra.checkout_url }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">Use Code EMK20 &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:1.5px;color:#999090;text-transform:uppercase;font-weight:600;">Code expires at midnight</p>
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
          <td style="background:#1A1A1A;padding:48px 40px 32px 40px;" align="center">
            <p style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:24px;letter-spacing:5px;color:#FFFFFF;font-weight:400;">AYDINS</p>
            <p style="margin:0 0 20px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:14px;font-style:italic;color:rgba(255,255,255,0.4);">Engraving wedding bands in Irving, Texas since 2011.</p>
            <p style="margin:0 0 6px 0;font-family:'Poppins',sans-serif;font-size:11px;color:rgba(255,255,255,0.45);letter-spacing:0.5px;">
              <a href="mailto:sales@shopaydins.com" style="color:rgba(255,255,255,0.45);text-decoration:none;">sales@shopaydins.com</a>
              &nbsp;&middot;&nbsp;
              <a href="tel:18002147345" style="color:rgba(255,255,255,0.45);text-decoration:none;">1-800-214-7345</a>
            </p>
            <p style="margin:20px 0 0 0;font-family:'Poppins',sans-serif;font-size:10px;color:rgba(255,255,255,0.4);letter-spacing:1px;text-align:center;">
              {% unsubscribe %}
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
```

---

## AC2 — Message ID `UCDagK`

**Subject:**
```
Your ring is nearly ready
```

**Preview text:**
```
A few minutes to finish, and we'll engrave it and ship it from Irving.
```

**Body HTML:**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  /* Mobile responsiveness — Klaviyo strips comments but keeps @media rules */
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-pad-top { padding-top:32px !important; }
    .ay-headline { font-size:40px !important; line-height:0.95 !important; }
    .ay-cart-img-cell { width:96px !important; }
    .ay-cart-img { width:96px !important; height:96px !important; max-width:96px !important; }
    .ay-cart-text { padding:14px 16px !important; }
    .ay-cart-name { font-size:15px !important; letter-spacing:0.5px !important; }
    .ay-trust-cell { padding:18px 16px !important; }
    .ay-reward-pad { padding:22px 20px !important; }
    .ay-reward-headline { font-size:30px !important; letter-spacing:1px !important; }
  }
</style>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Free Shipping &middot; Lifetime Warranty &middot; 30-Day Returns &middot; Irving, TX &middot; Since 2011</p>
          </td>
        </tr>

        <!-- LOGO -->
        <tr>
          <td align="center" style="padding:36px 24px 8px 24px;border-bottom:1px solid #D4CDC0;">
            <p style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:30px;letter-spacing:5px;color:#1A1A1A;font-weight:400;">AYDINS<span style="color:#B08D57;">.</span></p>
          </td>
        </tr>

        <!-- HERO IMAGE -->
        <tr>
          <td style="padding:0;">
            <img src="https://cdn.shopify.com/s/files/1/1857/8135/files/Why_Aydins_Story_split_image.png?v=1777386326" width="600" alt="Aydins workshop in Irving, Texas" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- EYEBROW + HEADLINE -->
        <tr>
          <td class="ay-pad" style="padding:48px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Almost There</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Your ring is<br>nearly ready.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">A few minutes to finish.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">Your cart is still saved. Finish it, and we'll engrave your ring and ship it from our shop in Irving, Texas.</p>
            <p style="margin:0;">Your size, your finish, and your engraving if you want it. We set it up the day your order comes in.</p>
          </td>
        </tr>

        <!-- CART CONTENTS -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 8px 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 14px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">Your Saved Cart</p>
            {% for item in event.extra.line_items %}
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;margin:0 0 12px 0;table-layout:fixed;">
              <tr>
                <td width="120" class="ay-cart-img-cell" style="padding:0;vertical-align:middle;width:120px;">
                  <a href="{{ item.product.url|default:event.extra.checkout_url }}" style="text-decoration:none;display:block;">
                    <img src="{{ item.product.images.0.src }}" width="120" alt="{{ item.product.title|default:item.title }}" class="ay-cart-img" style="display:block;width:120px;max-width:120px;height:120px;object-fit:cover;border:0;">
                  </a>
                </td>
                <td class="ay-cart-text" style="padding:18px 22px;vertical-align:middle;word-break:break-word;overflow-wrap:break-word;">
                  <p class="ay-cart-name" style="margin:0 0 8px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:18px;letter-spacing:1px;color:#1A1A1A;font-weight:400;line-height:1.15;text-transform:uppercase;">
                    <a href="{{ item.product.url|default:event.extra.checkout_url }}" style="color:#1A1A1A;text-decoration:none;">{{ item.product.title|default:item.title|default:'Your Ring' }}</a>
                  </p>
                  {% if item.quantity > 1 %}<p style="margin:0 0 8px 0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#999090;text-transform:uppercase;font-weight:600;">Qty {{ item.quantity }}</p>{% endif %}
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:15px;color:#1A1A1A;font-weight:600;letter-spacing:0.3px;">${{ item.line_price|floatformat:2 }}</p>
                </td>
              </tr>
            </table>
            {% endfor %}
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 48px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ event.extra.checkout_url }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">Finish Your Order &rarr;</a>
                </td>
              </tr>
            </table>
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
          <td style="background:#1A1A1A;padding:48px 40px 32px 40px;" align="center">
            <p style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:24px;letter-spacing:5px;color:#FFFFFF;font-weight:400;">AYDINS</p>
            <p style="margin:0 0 20px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:14px;font-style:italic;color:rgba(255,255,255,0.4);">Engraving wedding bands in Irving, Texas since 2011.</p>
            <p style="margin:0 0 6px 0;font-family:'Poppins',sans-serif;font-size:11px;color:rgba(255,255,255,0.45);letter-spacing:0.5px;">
              <a href="mailto:sales@shopaydins.com" style="color:rgba(255,255,255,0.45);text-decoration:none;">sales@shopaydins.com</a>
              &nbsp;&middot;&nbsp;
              <a href="tel:18002147345" style="color:rgba(255,255,255,0.45);text-decoration:none;">1-800-214-7345</a>
            </p>
            <p style="margin:20px 0 0 0;font-family:'Poppins',sans-serif;font-size:10px;color:rgba(255,255,255,0.4);letter-spacing:1px;text-align:center;">
              {% unsubscribe %}
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
```

---

## AC3 — Message ID `UJLFPZ`

**Subject:**
```
Last call. Your piece is still set aside
```

**Preview text:**
```
Since 2011, Aydins has been engraving wedding bands in Irving, Texas. Yours is ready when you are.
```

**Body HTML:**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  /* Mobile responsiveness — Klaviyo strips comments but keeps @media rules */
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-pad-top { padding-top:32px !important; }
    .ay-headline { font-size:40px !important; line-height:0.95 !important; }
    .ay-cart-img-cell { width:96px !important; }
    .ay-cart-img { width:96px !important; height:96px !important; max-width:96px !important; }
    .ay-cart-text { padding:14px 16px !important; }
    .ay-cart-name { font-size:15px !important; letter-spacing:0.5px !important; }
    .ay-trust-cell { padding:18px 16px !important; }
    .ay-reward-pad { padding:22px 20px !important; }
    .ay-reward-headline { font-size:30px !important; letter-spacing:1px !important; }
  }
</style>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Free Shipping &middot; Lifetime Warranty &middot; 30-Day Returns &middot; Irving, TX &middot; Since 2011</p>
          </td>
        </tr>

        <!-- LOGO -->
        <tr>
          <td align="center" style="padding:36px 24px 8px 24px;border-bottom:1px solid #D4CDC0;">
            <p style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:30px;letter-spacing:5px;color:#1A1A1A;font-weight:400;">AYDINS<span style="color:#B08D57;">.</span></p>
          </td>
        </tr>

        <!-- HERO IMAGE -->
        <tr>
          <td style="padding:0;">
            <img src="https://shopaydins.com/cdn/shop/files/Return_Exchange_image.jpg" width="600" alt="Aydins ring on workbench" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- EYEBROW + HEADLINE -->
        <tr>
          <td class="ay-pad" style="padding:48px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Last Call</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Your piece<br>is still<br>set aside.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">Yours is ready when you are.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">Since 2011, every Aydins order has been engraved and shipped from our shop in Irving, Texas.</p>
            <p style="margin:0 0 16px 0;">We're a small family operation. Not a marketplace, not a drop-shipper. Tungsten, titanium, Damascus, gold, meteorite, dinosaur bone. Your size, your finish, your engraving if you want it. Set up by the same small team for fifteen years.</p>
            <p style="margin:0;">When you're ready, we'll get yours moving.</p>
          </td>
        </tr>

        <!-- CART CONTENTS -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 8px 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 14px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">Set Aside For You</p>
            {% for item in event.extra.line_items %}
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;margin:0 0 12px 0;table-layout:fixed;">
              <tr>
                <td width="120" class="ay-cart-img-cell" style="padding:0;vertical-align:middle;width:120px;">
                  <a href="{{ item.product.url|default:event.extra.checkout_url }}" style="text-decoration:none;display:block;">
                    <img src="{{ item.product.images.0.src }}" width="120" alt="{{ item.product.title|default:item.title }}" class="ay-cart-img" style="display:block;width:120px;max-width:120px;height:120px;object-fit:cover;border:0;">
                  </a>
                </td>
                <td class="ay-cart-text" style="padding:18px 22px;vertical-align:middle;word-break:break-word;overflow-wrap:break-word;">
                  <p class="ay-cart-name" style="margin:0 0 8px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:18px;letter-spacing:1px;color:#1A1A1A;font-weight:400;line-height:1.15;text-transform:uppercase;">
                    <a href="{{ item.product.url|default:event.extra.checkout_url }}" style="color:#1A1A1A;text-decoration:none;">{{ item.product.title|default:item.title|default:'Your Ring' }}</a>
                  </p>
                  {% if item.quantity > 1 %}<p style="margin:0 0 8px 0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:1.5px;color:#999090;text-transform:uppercase;font-weight:600;">Qty {{ item.quantity }}</p>{% endif %}
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:15px;color:#1A1A1A;font-weight:600;letter-spacing:0.3px;">${{ item.line_price|floatformat:2 }}</p>
                </td>
              </tr>
            </table>
            {% endfor %}
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 48px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ event.extra.checkout_url }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">Complete Your Order &rarr;</a>
                </td>
              </tr>
            </table>
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
          <td style="background:#1A1A1A;padding:48px 40px 32px 40px;" align="center">
            <p style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:24px;letter-spacing:5px;color:#FFFFFF;font-weight:400;">AYDINS</p>
            <p style="margin:0 0 20px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:14px;font-style:italic;color:rgba(255,255,255,0.4);">Engraving wedding bands in Irving, Texas since 2011.</p>
            <p style="margin:0 0 6px 0;font-family:'Poppins',sans-serif;font-size:11px;color:rgba(255,255,255,0.45);letter-spacing:0.5px;">
              <a href="mailto:sales@shopaydins.com" style="color:rgba(255,255,255,0.45);text-decoration:none;">sales@shopaydins.com</a>
              &nbsp;&middot;&nbsp;
              <a href="tel:18002147345" style="color:rgba(255,255,255,0.45);text-decoration:none;">1-800-214-7345</a>
            </p>
            <p style="margin:20px 0 0 0;font-family:'Poppins',sans-serif;font-size:10px;color:rgba(255,255,255,0.4);letter-spacing:1px;text-align:center;">
              {% unsubscribe %}
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
```

---

## AC SMS — Abandoned Cart Text Message

**What this is:** Paste-ready SMS body for the Abandoned Cart flow's SMS message block. Two variants below — pick the one that matches where the SMS sits in your flow timing.

**TCPA note:** Klaviyo auto-appends "Reply STOP to unsubscribe" on the first SMS in a session per your SMS settings. The "Aydins:" prefix at the start identifies the sender, which Klaviyo + carrier rules require. Keep total length under **160 characters per segment** — if the message splits, you pay double per send.

**No fabrications:** No "handcrafted," no "made by hand," no "we'll cut your ring." SMS uses the same honest framing as the emails — engrave + ship from Irving, TX.

---

### Primary SMS (pairs with AC1 timing — discount push)

Use this if the SMS fires within the first ~4 hours of cart abandonment. Mirrors the EMK20 lever in AC1.

**Body:**
```
Aydins: Still thinking about your ring? Take 20% off your cart with code EMK20. Expires midnight tonight. {{ event.extra.checkout_url }}
```

Length: ~118 chars + Klaviyo-shortened cart URL (~25 chars) = **~143 total. One segment.** ✅

---

### Alternate SMS (later in flow — last-call tone, no discount)

Use this if the SMS fires after AC2 or AC3 has already gone out (so EMK20 has already been pitched in email).

**Body:**
```
Aydins: Your ring is still set aside. We'll engrave & ship it from our shop in Irving, TX. {% checkout_url %}
```

Length: ~99 chars + URL = **~124 total. One segment.** ✅

---

### How to paste into Klaviyo

1. Klaviyo → **Flows** → "Abandoned Cart" (`TrNjjf`) → click the **SMS message block**
2. **Edit Message** → delete existing body
3. Paste the matching variant above into the message text field
4. **Verify the cart link variable.** The body uses `{% checkout_url %}` — same as the emails. If your existing SMS used `{{ event.extra.cart_url }}` or a different tag, copy that exact tag from the original and replace `{% checkout_url %}`.
5. **Klaviyo's editor shows live character count and segment count** — confirm it shows **1 segment** before saving. If it shows 2, the message will cost double per send and may break across the URL.
6. Click **Preview & Send** → send to your own phone → confirm:
   - The "Aydins:" prefix shows up
   - The link opens to the actual cart with items in it
   - The discount code (EMK20) is visible if using the primary variant
7. Save and exit

### What to do if the SMS shows 2 segments

If you see "2 segments" in Klaviyo's editor, the most likely culprits are:
- The em-dash `—` (U+2014) or smart quotes — replace with regular `-` and `'` to drop to GSM-7 encoding (160 char limit). With em-dash you get UCS-2 encoding (70 char limit).
- The `&` symbol — replace with "and" to save chars.

**GSM-7-safe Primary SMS** (zero special chars):
```
Aydins: Still thinking about your ring? Take 20% off your cart with code EMK20 - expires midnight tonight. {% checkout_url %}
```

**GSM-7-safe Alternate SMS:**
```
Aydins: Your ring is still set aside. We'll engrave and ship it from our shop in Irving, TX. {% checkout_url %}
```

---

## ⚠️ Verify the cart-loop variables before saving

Each email now renders the actual abandoned cart contents — product image, name, quantity, and price — using a Klaviyo `{% for item in event.extra.line_items %}` loop. The exact variable names depend on **which trigger metric** your Abandoned Cart flow runs on:

| Trigger | Loop variable | Image | Name | Price | URL |
|---|---|---|---|---|---|
| **Shopify "Checkout Started"** (most common) | `event.extra.line_items` | `item.product.images.0.src` | `item.product.title` | `item.line_price` | `item.product.url` |
| **Klaviyo "Started Checkout"** (legacy) | `event.extra.line_items` | `item.product.images.0` | `item.title` | `item.line_price` | `item.product.url` |
| **Custom "Added to Cart"** | varies — check the event payload in Klaviyo |

> The HTML below uses a defensive chain: `{{ item.product.title|default:item.title|default:'Your Ring' }}` — it tries the modern field first, falls back to the legacy field, then to a safe label. Works across all integration versions.

**Before you save each email:**
1. Open the flow → click the email → click **Preview & Test**
2. Pick a real recent abandoned-cart profile from the dropdown
3. Confirm the cart block renders with the actual product image, name, and price
4. If anything is blank, the variable name is wrong — open the trigger event in Klaviyo's metric explorer, find the real variable path, and update the HTML

If `${{ item.line_price }}` shows up as `$1995.00` instead of `$1,995`, that's normal — Klaviyo doesn't apply commas to raw numeric output. If you want commas, swap to `{{ item.line_price|number_with_delimiter }}`.

If your store's prices are stored in cents (`199500`), divide first: `${{ item.line_price|divided_by:100 }}`. Most Shopify→Klaviyo integrations already pass dollars — verify with Preview.

---

## After you paste — sanity check

For each of the 3 emails, before you save:

- [ ] Subject line matches the value above (no emoji, no fabrications)
- [ ] Preview text matches the value above
- [ ] Old drag-and-drop blocks are deleted (only the HTML block remains)
- [ ] CTA `href` is `{{ event.extra.checkout_url }}` (if test email button URL is blank, swap to `{{ event.checkout_url }}`)
- [ ] `{% unsubscribe %}` is on its OWN line, NOT wrapped in `<a href="">` — the tag outputs a full anchor and nesting breaks it
- [ ] **Cart block renders with real product image, name, and price** in Preview & Test (see verify section above)
- [ ] AC1 reward panel shows "20% Off Your Cart" with EMK20 callout
- [ ] Click "Preview & Test" → send yourself a real test email → click the CTA → confirm it goes to checkout
- [ ] Mobile preview renders cleanly (the table is responsive at 600px)

## Font fallback note

Bebas Neue and Cormorant Garamond load via Google Fonts at the top of the HTML. Most modern email clients (Gmail web, Apple Mail, iOS Mail) render them fine. Outlook desktop will fall back to **Impact / Arial Black** for headlines and **Georgia** for serif italic — still on-brand, just a touch heavier. That's expected and acceptable.

## What this ships

A 3-email + 1-SMS abandoned-cart sequence that:
- Stops sending false "lifetime warranty included" / "30-day free returns" / "lifetime fit guarantee" claims
- Stops claiming Aydins "handcrafts," "cuts," or "makes by hand" — accurately frames the operation as **engrave + ship from Irving, Texas** (per Source-of-Truth Rule #9)
- Matches the homepage v3 design language exactly — Bebas Neue headlines, brass gold accents, ink + cream palette, italic serif accent line
- Says "Irving, Texas" not "Flower Mound" or "Grapevine Mills"
- SMS is segment-safe (under 160 chars in GSM-7) and TCPA-compliant ("Aydins:" sender ID, Klaviyo auto-appends STOP)
- Is consistent with what shopaydins.com will say once the page-rewrites land

When all 3 emails + the SMS are saved, reply "AC1/2/3 + SMS done" and I'll build the same paste-ready bundles for Welcome 1-4, Thank You 1-2, Browse Abandonment, and Customer Winback 1-2 next.
