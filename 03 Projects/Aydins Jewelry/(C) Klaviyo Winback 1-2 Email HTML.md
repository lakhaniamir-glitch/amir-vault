# (C) Klaviyo Customer Winback — W1 / W2 (paste-ready)

> **What this is:** Two paste-ready Customer Winback emails. Style-matched to the homepage v3 design and the AC / Welcome / Thank You / Browse shell. Bebas Neue headlines, Cormorant Garamond italic subtitles, Poppins body, ink + cream + brass-gold palette.
>
> **Source of truth for every claim:** [[(C) Aydins Policies — Source of Truth]]. No fabricated warranties, no "handcrafted" / "made by hand" language. Marketing copy uses approved short labels only: "Free Engraving," "Free U.S. Shipping," "Lifetime Warranty," "30-Day Returns."
>
> **Strategic choice baked in: no discount.** Winback is a re-engagement play, not a price play. These customers already bought once — they know the quality. Discounts here cannibalize buyers who would re-engage anyway. The play is: show them what's new from the shop, invite them to reply. Aydin sign-off keeps it human.

---

## ⚠️ Pause the flow FIRST

The Winback flow ID is **`QVt7Vu`** and it's currently live, firing on dormant customers. You **cannot** paste edits while the flow is live — you risk shipping a half-edited email mid-update to a real customer.

**Before pasting any HTML below:**

1. Klaviyo → **Flows** → open **Customer Winback** (`QVt7Vu`)
2. Top-right corner → toggle flow status from **Live** → **Draft**
3. Confirm the canvas shows a "Draft" badge

When both emails are pasted, tested, and saved → toggle status back to **Live**.

---

## How to use it in Klaviyo

1. Pause flow `QVt7Vu` (see above)
2. Click the email block on the canvas → **Edit Email**
3. **Update Subject + Preview** at the top of the editor
4. In the body editor, **delete every existing row/block** until the canvas is empty
5. Drag in a new **HTML** block (under "Content" → "HTML")
6. Paste the matching HTML below into that block
7. Save → Preview on desktop + mobile → exit
8. Repeat for W2
9. Re-activate the flow (toggle back to Live)

---

## Push order

| # | Email | Message ID | Status before edits | Send delay |
|---|---|---|---|---|
| 1 | Winback 1 — It's been a while | `WiJLsV` | LIVE — generic copy | Trigger: dormant 90+ days |
| 2 | Winback 2 — Last note | `QQPRA6` | LIVE — generic copy | 7 days after W1, if no engagement |

---

## Why no product grid

Earlier versions of this email used a dynamic product feed (`feeds.SHOP_POPULAR_ALL_CATEGORIES`). It didn't reliably render in Klaviyo's preview, which means there was no way to know what dormant customers actually saw without sending live tests. Replaced with a single hero shot + strong "Shop The Catalog" CTA. Cleaner, faster to load, renders identically in preview and production, no feed maintenance.

If you want a product grid back later, the cleanest path is Klaviyo's drag-and-drop **Product Block** component instead of the HTML feed loop. Tell me when you're ready and I'll rebuild it that way.

---

## Style locked (matches homepage v3 + AC + Welcome + Thank You + Browse)

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

## W1 — Message ID `WiJLsV`

**Subject:**
```
It's been a while
```

**Preview text:**
```
A few new pieces from the shop you haven't seen yet.
```

**Body HTML (paste into a single HTML block):**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
    .ay-product-cell { display:block !important; width:100% !important; padding:0 0 20px 0 !important; }
    .ay-product-img { width:100% !important; height:auto !important; max-width:100% !important; }
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
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Welcome Back</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">It's been<br>a while.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">A few new pieces, in case you want a look.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">Good to see you back, {{ person.first_name|default:'friend' }}. Since you last looked, we've engraved and shipped a lot of new pieces. New metals, new finishes, new custom work.</p>
            <p style="margin:0;">Take a look when you're ready.</p>
          </td>
        </tr>

        <!-- HERO IMAGE -->
        <tr>
          <td style="padding:24px 0 0 0;background:#F2EDE4;">
            <img src="https://cdn.shopify.com/s/files/1/1857/8135/files/Why_Aydins_Jewelry.png?v=1777352028" width="600" alt="Aydins workshop" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 24px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="https://shopaydins.com/collections/all" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">Shop The Catalog &rarr;</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- SIGN-OFF -->
        <tr>
          <td class="ay-pad" style="padding:0 40px 40px 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">Looking for something specific? Reply to this email. A lot of what we engrave is custom and never hits the storefront.</p>
            <p style="margin:18px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:18px;font-style:italic;color:#1A1A1A;">&mdash; Amir</p>
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

## W2 — Message ID `QQPRA6`

**Subject:**
```
We've missed you. Here's what's new.
```

**Preview text:**
```
A handful of new pieces picked for you.
```

**Body HTML (paste into a single HTML block):**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
    .ay-product-cell { display:block !important; width:100% !important; padding:0 0 20px 0 !important; }
    .ay-product-img { width:100% !important; height:auto !important; max-width:100% !important; }
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
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Still Here For You</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">We've<br>missed you.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">A handful of pieces, picked from the shop.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">Since you've been gone, the shop has been busy. New pieces, new metals, new custom engraving work.</p>
            <p style="margin:0;">If nothing here is right, just reply. We make a lot of custom pieces that never hit the storefront.</p>
          </td>
        </tr>

        <!-- HERO IMAGE -->
        <tr>
          <td style="padding:24px 0 0 0;background:#F2EDE4;">
            <img src="https://cdn.shopify.com/s/files/1/1857/8135/files/Why_Aydins_Jewelry.png?v=1777352028" width="600" alt="Aydins workshop" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 24px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="https://shopaydins.com/collections/all" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">View The Catalog &rarr;</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- SIGN-OFF -->
        <tr>
          <td class="ay-pad" style="padding:0 40px 40px 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">Anything we can help with, {{ person.first_name|default:'friend' }}? Sizing, a custom piece, a question on a past order. Just reply.</p>
            <p style="margin:18px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:18px;font-style:italic;color:#1A1A1A;">&mdash; Amir</p>
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

## After you paste both, sanity check

For W1 and W2, confirm:

- [ ] Subject + Preview updated at the top of the editor
- [ ] Old email blocks deleted, only the new HTML block remains
- [ ] Desktop preview shows the hero workshop image full-width under the body copy
- [ ] Mobile preview shows the hero image scaled to full width with no overflow
- [ ] First-name personalization renders (load a test profile in preview to confirm)
- [ ] "— Amir" sign-off renders correctly in Cormorant italic
- [ ] CTA button click-through lands on `/collections/all`
- [ ] `{% unsubscribe %}` renders as a working link, not raw text
- [ ] Footer reads "A small jewelry shop. Free engraving on every order."

## ⚠️ Final step — re-activate the flow

After both emails are pasted, saved, and tested:

1. Klaviyo → **Flows** → **Customer Winback** (`QVt7Vu`)
2. Top-right corner → toggle status from **Draft** → **Live**
3. Confirm the canvas shows "Live" badge again

Until you do this, **the Winback flow will not send anything to dormant customers**. The emails sit ready but the trigger is paused.

## What this email set does that the existing one doesn't

- Treats Winback as re-engagement, not discount-driven
- "— Aydin" personal sign-off in Cormorant italic (human, not corporate)
- First-name personalization on the helper line
- Soft reply CTA that opens the door to custom work (your highest-margin channel)
- Same shell as AC + Welcome + Thank You + Browse, so brand reads continuous
- No fabricated claims, no "handcrafted," no "made by hand"

## When this is done

Reply "Winback done" and I'll move to **Order Confirmation** (`RRHrAp`). Reminder for that one: you'll need to decide whether to turn off Shopify's native order confirmation email first, or your customers will receive two receipts (Shopify's + Klaviyo's). I'll walk you through that decision when we get there.
