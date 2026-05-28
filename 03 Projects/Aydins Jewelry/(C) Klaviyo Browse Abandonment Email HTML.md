# (C) Klaviyo Browse Abandonment Email HTML (paste-ready)

> **What this is:** A single paste-ready Browse Abandonment email. Style-matched to the homepage v3 design and the AC / Welcome / Thank You shell. Bebas Neue headlines, Cormorant Garamond italic subtitles, Poppins body, ink + cream + brass-gold palette.
>
> **Source of truth for every claim:** [[(C) Aydins Policies — Source of Truth]]. No fabricated warranties, no "handcrafted" / "made by hand" language. Marketing copy uses approved short labels only: "Free Engraving," "Free U.S. Shipping," "Lifetime Warranty," "30-Day Returns."
>
> **Strategic choice baked in: no discount.** Browse Abandonment is earlier-funnel than Abandoned Cart. These subscribers viewed a product but didn't add to cart. Dropping a discount here trains people to leave the site to trigger one and cannibalizes margin from buyers who would have come back on their own. The AC series owns the discount play. This email is a soft re-introduction to the piece, plus social proof, plus the trust pillars.

---

## How to use it in Klaviyo

1. Klaviyo → **Flows** → open **"Browse Abandonment"** (flow contains message `T6q2n5`)
2. Click the email block on the canvas → **Edit Email**
3. **Update Subject + Preview** at the top of the editor
4. In the body editor, **delete every existing row/block** until the canvas is empty
5. Drag in a new **HTML** block (under "Content" → "HTML")
6. Paste the HTML below into that block
7. Save → Preview on desktop + mobile → exit

---

## Push status

| # | Email | Message ID | Status before edits | Trigger |
|---|---|---|---|---|
| 1 | Browse Abandonment | `T6q2n5` | LIVE — generic copy | Viewed Product, no Started Checkout within 4 hours |

---

## Viewed Product variable map

Klaviyo's Shopify integration fires the **Viewed Product** event with a few standard fields. The exact variable path depends on which integration version you're on. The HTML below uses the most common path. If a field renders blank in preview, swap to the alternate path:

| Field | Primary path (used in HTML below) | Alternate path |
|---|---|---|
| Product title | `{{ event.Name }}` | `{{ event.ProductName }}` or `{{ event.extra.product.title }}` |
| Product image | `{{ event.ImageURL }}` | `{{ event.ImageUrl }}` or `{{ event.extra.product.image_url }}` |
| Product URL | `{{ event.URL }}` | `{{ event.extra.product.url }}` |
| Product price | `{{ event.Price }}` (already includes `$`, do not prepend) | `{{ event.extra.product.price }}` |

> ⚠️ **Price gotcha:** The Shopify-Klaviyo integration returns `event.Price` as a **pre-formatted string with the `$` already in it** (e.g. `$169.00`). Do NOT hardcode a `$` before the variable in HTML or you'll get `$$169.00`. The HTML below has this fix baked in.

**How to verify which path your flow uses:**
1. Klaviyo → Analytics → Metrics → "Viewed Product"
2. Click any recent event → view the JSON payload
3. Find the field names that are populated and swap the HTML if needed

---

## Style locked (matches homepage v3 + AC + Welcome + Thank You)

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

## Browse Abandonment — Message ID `T6q2n5`

**Subject:**
```
Still looking at this one?
```

**Preview text:**
```
Free engraving, free U.S. shipping. Here whenever you're ready.
```

**Body HTML (paste into a single HTML block):**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
    .ay-prod-img { width:100% !important; height:auto !important; max-width:100% !important; }
    .ay-prod-pad { padding:20px !important; }
    .ay-prod-name { font-size:20px !important; letter-spacing:0.5px !important; }
    .ay-quote { font-size:15px !important; line-height:1.5 !important; }
  }
</style>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Free Engraving &middot; Free U.S. Shipping &middot; Lifetime Warranty &middot; 30-Day Returns</p>
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
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Still On Your Mind?</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Still looking<br>at this one?</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">No rush. We saved the photo.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 16px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">You were looking at one of our pieces a little while ago. Figured we'd send the photo back, in case you want to pick up where you left off.</p>
            <p style="margin:0;">No discount, no countdown. The ring is here when you're ready.</p>
          </td>
        </tr>

        <!-- VIEWED PRODUCT CARD -->
        <tr>
          <td class="ay-pad" style="padding:16px 40px 8px 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 14px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#999090;text-transform:uppercase;font-weight:700;">The Piece You Were Looking At</p>
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;">
              <tr>
                <td style="padding:0;">
                  <a href="{{ event.URL|default:'https://shopaydins.com' }}" style="text-decoration:none;display:block;">
                    <img src="{{ event.ImageURL }}" width="600" alt="{{ event.Name|default:'Aydins ring' }}" class="ay-prod-img" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
                  </a>
                </td>
              </tr>
              <tr>
                <td class="ay-prod-pad" style="padding:28px 28px;" align="left">
                  <p class="ay-prod-name" style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:24px;letter-spacing:1px;color:#1A1A1A;font-weight:400;line-height:1.1;text-transform:uppercase;">
                    <a href="{{ event.URL|default:'https://shopaydins.com' }}" style="color:#1A1A1A;text-decoration:none;">{{ event.Name|default:'One of our pieces' }}</a>
                  </p>
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:15px;color:#1A1A1A;font-weight:600;letter-spacing:0.3px;">{{ event.Price|default:'' }}</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 24px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ event.URL|default:'https://shopaydins.com' }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">View The Ring &rarr;</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- SOCIAL PROOF -->
        <tr>
          <td class="ay-pad" style="padding:8px 40px 32px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid #D4CDC0;border-bottom:1px solid #D4CDC0;">
              <tr>
                <td style="padding:28px 0;" align="left">
                  <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:14px;letter-spacing:2px;color:#B08D57;font-weight:700;">&#9733; &#9733; &#9733; &#9733; &#9733;</p>
                  <p class="ay-quote" style="margin:0 0 12px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:18px;line-height:1.55;color:#1A1A1A;font-style:italic;font-weight:400;">"Exactly what I hoped for. The quality was incredible, and the service was top-notch. Arrived fast and beautifully packaged."</p>
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:2px;color:#999090;text-transform:uppercase;font-weight:600;">Marcus G. &middot; Verified Buyer</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- HELPER LINE -->
        <tr>
          <td class="ay-pad" style="padding:0 40px 40px 40px;background:#F2EDE4;" align="left">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Questions on sizing, materials, or a custom version of this ring? Reply to this email. A real person reads every one.</p>
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
            <p style="margin:0 0 20px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:14px;font-style:italic;color:rgba(255,255,255,0.4);">A small jewelry shop. Free engraving on every order.</p>
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

## After you paste, sanity check

- [ ] Subject and Preview updated at the top of the editor
- [ ] Old email blocks deleted, only the HTML block remains
- [ ] Desktop preview shows the product image (not a broken-image icon)
- [ ] Mobile preview shows the product image scaled to full width
- [ ] Product name, price, and link all populate (load a real Viewed Product profile in Preview to verify)
- [ ] CTA button click-through lands on the actual product page (not the homepage)
- [ ] `{% unsubscribe %}` renders as a working link (not raw text)
- [ ] Footer reads "A small jewelry shop. Free engraving on every order."

## If variables come up blank in preview

The HTML uses `{{ event.ProductName }}`, `{{ event.ImageUrl }}`, `{{ event.URL }}`, `{{ event.Price }}`. If any of those render blank for a real Viewed Product event:

1. Open Klaviyo → Analytics → Metrics → "Viewed Product" → click any recent event
2. Find the actual field names in the JSON payload (look for `product.title`, `product.image_url`, etc.)
3. Find-and-replace in the HTML block. Common swap: `event.ProductName` → `event.extra.product.title`

## What this email does that the existing one doesn't

- Stops generic "abandoned-cart-style" copy and treats Browse as its own funnel stage
- No discount — preserves margin and doesn't train browsers to expect a code
- Concrete social proof (real 5-star review) instead of a wall of feature bullets
- One CTA, not three — eyes go to "View The Ring"
- Same shell as AC + Welcome + Thank You, so the brand feels continuous
- Footer signature aligned with Welcome + Thank You ("A small jewelry shop")

## When this is done

Reply "Browse done" and we move to **Customer Winback 1 + 2** (`WiJLsV`, `QQPRA6`). Reminder: the Winback flow (`QVt7Vu`) must be **paused first** before editing the email templates so a half-edited flow doesn't fire on dormant customers mid-update.
