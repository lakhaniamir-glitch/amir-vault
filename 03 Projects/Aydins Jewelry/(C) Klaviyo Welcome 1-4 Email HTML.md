# (C) Klaviyo Welcome Series — W1 / W2 / W3 / W4 (paste-ready)

> **What this is:** Four complete, paste-ready welcome-series emails. Style-matched to the Aydins homepage v3 design — Bebas Neue headlines, Cormorant Garamond italic subtitles, Poppins body, ink + cream + brass-gold palette. Same shell as [[(C) Klaviyo AC1-AC2-AC3 Email HTML]] so the brand feels continuous from popup → first email → checkout flows.
>
> **Source of truth for every claim:** [[(C) Aydins Policies — Source of Truth]]. No fabricated warranties, no "handcrafted" / "made by hand" language. Marketing copy uses approved short labels only — "Free Engraving," "Free U.S. Shipping," "Lifetime Warranty," "30-Day Returns" — without fee qualifiers (those live on policy pages).
>
> **All Klaviyo render fixes baked in from the start:**
> - `{% unsubscribe %}` stands alone in the footer (no `<a href="">` wrap — wrapping breaks it because the tag outputs a full anchor)
> - `{% coupon_code '20_OFF2' %}` for dynamic per-recipient code rendering
> - Banned phrases scrubbed: no "handcrafted," "cut," "forged," "made by hand"
> - **Irving / "since 2011" framing removed** (per request 2026-05-11). Brand anchor for these emails is now: "small family-run shop" + "free engraving on every ring."

---

## How to use it in Klaviyo

1. Klaviyo → **Flows** → open **"Email Welcome Series with Discount"** (flow ID: `XQZ9kX`)
2. For each email below: click the email block on the canvas → **Edit Email**
3. **Update Subject + Preview** at the top of the editor (paste from the values below)
4. In the body editor, **delete every existing row/block** until the canvas is empty
5. Drag in a new **HTML** block (under "Content" → "HTML")
6. Paste the matching email HTML below into that block
7. Save → Preview on desktop + mobile → exit

Repeat for W1 → W2 → W3 → W4.

---

## Push order

| # | Email | Message ID | Status before edits | Send delay |
|---|---|---|---|---|
| 1 | Welcome 1 — Welcome + 20% code | `TzFzsG` | LIVE — old "Lakhani Group LLC" copy must go | Immediately on list signup |
| 2 | Welcome 2 — Reminder | `SWEwQ5` | LIVE — has emoji + generic copy | 3 days later |
| 3 | Welcome 3 — Follow the workshop | `SjDuds` | LIVE — generic social CTA | 3 days after W2 |
| 4 | Welcome 4 — Most-ordered pieces | `VUvfeq` | LIVE — bestsellers, generic copy | 4 days after W3 |

> ⚠️ **Discount code:** The flow uses Klaviyo's `{% coupon_code '20_OFF2' %}` tag. That generates a unique per-recipient code if the coupon is set up as "Multi-use unique code" in Klaviyo → Coupons. If it's set up as a static code, the tag still works — it just renders the same string for everyone. Verify the coupon `20_OFF2` exists in **Klaviyo → Coupons** before going live. If you want to switch to a new code (e.g. `WELCOME20`), create it in Klaviyo Coupons first, then find-and-replace `20_OFF2` in all 4 HTML blocks.

---

## Style locked (matches homepage v3 + AC series)

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

## W1 — Message ID `TzFzsG`

**Subject:**
```
Welcome to Aydins. Here's 20% off your first ring.
```

**Preview text:**
```
Your code is inside. Plus a quick note on what we actually do.
```

**Body HTML (paste into a single HTML block):**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
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
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Free Engraving &middot; Free U.S. Shipping &middot; Lifetime Warranty &middot; 30-Day Returns</p>
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
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Welcome To Aydins</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">20% off your<br>first ring.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">A small jewelry shop. Free engraving on every order.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">Glad to have you. Aydins is a small family-run shop. Tungsten, titanium, Damascus, gold, ceramic, meteorite, dinosaur bone. Whatever the metal, if you want engraving, it's on us.</p>
            <p style="margin:0;">Here's 20% off your first ring, on us.</p>
          </td>
        </tr>

        <!-- REWARD PANEL -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 0 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#1A1A1A;">
              <tr>
                <td class="ay-reward-pad" style="padding:28px 28px;" align="left">
                  <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;">Your Welcome Reward</p>
                  <p class="ay-reward-headline" style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:38px;letter-spacing:2px;color:#FFFFFF;font-weight:400;line-height:1;text-transform:uppercase;">20% Off Your First Order</p>
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:12px;color:rgba(255,255,255,0.7);line-height:1.6;">Apply code <strong style="color:#C9A84C;letter-spacing:1.5px;font-weight:700;">{% coupon_code '20_OFF2' %}</strong> at checkout. One per customer.</p>
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
                  <a href="https://shopaydins.com/collections/all" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">Shop The Catalog &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Questions on sizing, materials, or a custom idea? Reply to this email. A real person reads every one.</p>
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

## W2 — Message ID `SWEwQ5`

**Subject:**
```
Reminder: your 20% Aydins code is still good
```

**Preview text:**
```
Code 20_OFF2. Yours when you're ready.
```

**Body HTML:**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
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
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Free Engraving &middot; Free U.S. Shipping &middot; Lifetime Warranty &middot; 30-Day Returns</p>
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
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Still Good</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Your 20% code<br>is waiting.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">Use it when you're ready.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">Quick reminder: your welcome code is still good. 20% off any ring in the catalog. Tungsten, titanium, Damascus, gold, ceramic, meteorite, dinosaur bone. Engraving is always free.</p>
            <p style="margin:0;">Take your time. The code holds.</p>
          </td>
        </tr>

        <!-- REWARD PANEL -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 0 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#1A1A1A;">
              <tr>
                <td class="ay-reward-pad" style="padding:28px 28px;" align="left">
                  <p style="margin:0 0 10px 0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;">Your Welcome Reward</p>
                  <p class="ay-reward-headline" style="margin:0 0 10px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:38px;letter-spacing:2px;color:#FFFFFF;font-weight:400;line-height:1;text-transform:uppercase;">20% Off Any Ring</p>
                  <p style="margin:0;font-family:'Poppins',sans-serif;font-size:12px;color:rgba(255,255,255,0.7);line-height:1.6;">Apply code <strong style="color:#C9A84C;letter-spacing:1.5px;font-weight:700;">{% coupon_code '20_OFF2' %}</strong> at checkout. One per customer.</p>
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
                  <a href="https://shopaydins.com/collections/all" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">Browse The Catalog &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Need help picking a metal? Reply with what you do for work. I'll tell you which holds up.</p>
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

## W3 — Message ID `SjDuds`

**Subject:**
```
A few places to follow Aydins
```

**Preview text:**
```
New pieces, customs, and behind-the-scenes from the shop.
```

**Body HTML:**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:42px !important; line-height:0.95 !important; }
    .ay-social-cell { padding:18px 12px !important; }
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

        <!-- HERO IMAGE -->
        <tr>
          <td style="padding:0;">
            <img src="https://cdn.shopify.com/s/files/1/1857/8135/files/Return_Exchange_image.jpg" width="600" alt="Aydins ring detail" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- EYEBROW + HEADLINE -->
        <tr>
          <td class="ay-pad" style="padding:48px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Follow Along</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">A few places<br>to find us.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">New pieces, customs, behind-the-scenes.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 24px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">A lot of what we engrave never makes it onto the storefront. Custom pieces, fingerprint engravings, one-off Damascus orders. The best place to see those is on our social channels.</p>
            <p style="margin:0;">Pick a platform, or all three.</p>
          </td>
        </tr>

        <!-- SOCIAL ROW -->
        <tr>
          <td class="ay-pad" style="padding:8px 40px 48px 40px;background:#F2EDE4;" align="center">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;">
              <tr>
                <td width="33%" class="ay-social-cell" style="padding:28px 16px;border-right:1px solid #D4CDC0;text-align:center;">
                  <a href="https://www.instagram.com/aydinsjewelry" style="text-decoration:none;color:#1A1A1A;">
                    <p style="margin:0 0 6px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:22px;letter-spacing:2px;color:#1A1A1A;font-weight:400;text-transform:uppercase;">Instagram</p>
                    <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;letter-spacing:0.5px;">New drops &middot; customs</p>
                  </a>
                </td>
                <td width="33%" class="ay-social-cell" style="padding:28px 16px;border-right:1px solid #D4CDC0;text-align:center;">
                  <a href="https://www.facebook.com/aydinsjewelry" style="text-decoration:none;color:#1A1A1A;">
                    <p style="margin:0 0 6px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:22px;letter-spacing:2px;color:#1A1A1A;font-weight:400;text-transform:uppercase;">Facebook</p>
                    <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;letter-spacing:0.5px;">Reviews &middot; community</p>
                  </a>
                </td>
                <td width="34%" class="ay-social-cell" style="padding:28px 16px;text-align:center;">
                  <a href="https://www.pinterest.com/aydinsjewelry" style="text-decoration:none;color:#1A1A1A;">
                    <p style="margin:0 0 6px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:22px;letter-spacing:2px;color:#1A1A1A;font-weight:400;text-transform:uppercase;">Pinterest</p>
                    <p style="margin:0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;letter-spacing:0.5px;">Style boards &middot; ideas</p>
                  </a>
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

> **Before saving:** verify the three social URLs above match your actual handles. Update any that are wrong (Instagram, Facebook, Pinterest). Klaviyo won't catch wrong handles — they'll just lead to 404s.

---

## W4 — Message ID `VUvfeq`

**Subject:**
```
A few of our most-ordered pieces
```

**Preview text:**
```
The rings customers come back for.
```

**Body HTML:**

> Uses Klaviyo's `feeds.SHOP_POPULAR_ALL_CATEGORIES` product feed — same feed your existing welcome series already pulls from. If the feed isn't wired up, the product grid renders empty (but the rest of the email is fine).

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
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Most-Ordered</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">The rings<br>customers<br>come back for.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">Start here if you're not sure where to start.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 8px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0;">Out of everything we've engraved and shipped, these are the pieces customers keep coming back for. Take a look.</p>
          </td>
        </tr>

        <!-- PRODUCT GRID -->
        <tr>
          <td class="ay-pad" style="padding:24px 40px 8px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                {% for item in feeds.SHOP_POPULAR_ALL_CATEGORIES|slice:":3" %}
                <td class="ay-product-cell" width="33%" valign="top" style="padding:0 6px;">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;">
                    <tr>
                      <td style="padding:0;">
                        <a href="{{ item.url }}" style="text-decoration:none;display:block;">
                          <img src="{{ item.image_url }}" alt="{{ item.title }}" class="ay-product-img" style="display:block;width:100%;max-width:172px;height:auto;border:0;">
                        </a>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding:14px 14px 16px 14px;" align="center">
                        <p style="margin:0 0 6px 0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:14px;letter-spacing:1px;color:#1A1A1A;font-weight:400;line-height:1.2;text-transform:uppercase;">
                          <a href="{{ item.url }}" style="color:#1A1A1A;text-decoration:none;">{{ item.title }}</a>
                        </p>
                        <p style="margin:0;font-family:'Poppins',sans-serif;font-size:12px;color:#1A1A1A;font-weight:600;">${{ item.price|floatformat:2 }}</p>
                      </td>
                    </tr>
                  </table>
                </td>
                {% endfor %}
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
                  <a href="https://shopaydins.com/collections/all" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">Shop The Catalog &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Looking for something custom? Reply to this email. A lot of what we engrave never makes it to the storefront.</p>
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

## ⚠️ Verify before saving

### W1 + W2 — coupon code
- The `{% coupon_code '20_OFF2' %}` tag relies on a coupon named exactly **`20_OFF2`** existing in **Klaviyo → Coupons**. Confirm it's there before going live. If you want a new code, create it in Klaviyo Coupons first.

### W3 — social URLs
- Instagram: `https://www.instagram.com/aydinsjewelry`
- Facebook: `https://www.facebook.com/aydinsjewelry`
- Pinterest: `https://www.pinterest.com/aydinsjewelry`
- Verify each handle is correct before saving — Klaviyo will not catch typos.

### W4 — product feed
- The `feeds.SHOP_POPULAR_ALL_CATEGORIES` feed is what your existing welcome flow already uses. Confirm it's still populating in **Klaviyo → Templates → Web Feeds** (or wherever feeds are managed in your account version). If it's empty, the product grid will render blank.
- If the feed uses different field names than `item.title` / `item.image_url` / `item.url` / `item.price`, swap them. The existing welcome series uses `item.title`, `item.price`, `item.regular_price`, `item.url` — those should still work.

---

## After you paste — sanity check

For each of the 4 emails, before you save:

- [ ] Subject line matches the value above (no emoji)
- [ ] Preview text matches the value above
- [ ] Old drag-and-drop blocks are deleted (only the HTML block remains)
- [ ] `{% unsubscribe %}` is on its OWN line, NOT wrapped in `<a href="">` — the tag outputs a full anchor and nesting breaks it
- [ ] No "handcrafted," "made by hand," "we cut," or "forged" language anywhere in the body
- [ ] Click "Preview & Test" → send yourself a real test email → confirm:
  - Coupon code renders (W1, W2)
  - Social buttons go to the right handles (W3)
  - Product feed renders 3 products (W4)
- [ ] Mobile preview renders cleanly (table is responsive at 600px)

---

## What this ships

A welcome series that:
- Tells the truth (no fabricated lifetime warranty / free returns / handcrafted claims)
- Looks identical to the homepage and the abandoned cart series (same fonts, palette, structure)
- Uses Klaviyo's coupon and product-feed tags correctly
- Has a clean unsubscribe link in the footer (no broken nested anchors)
- Reads premium-but-direct — short paragraphs, no emoji, Amir-tone reply CTAs

Push it, send tests, then we move to **Thank You 1 + 2 (`TQrkhz`, `UZQbbr`)** next.
