# (C) Klaviyo Thank You — T1 / T2 (paste-ready)

> **What this is:** Two complete, paste-ready post-purchase thank-you emails. Style-matched to [[(C) Klaviyo AC1-AC2-AC3 Email HTML]] and [[(C) Klaviyo Welcome 1-4 Email HTML]] so the brand reads continuous from popup → welcome → checkout → confirmation.
>
> **Source of truth for every claim:** [[(C) Aydins Policies — Source of Truth]]. No fabricated warranties, no "handcrafted / made by hand / forged" language. Marketing copy uses approved short labels only — "Free Engraving," "Free U.S. Shipping," "Lifetime Warranty," "30-Day Returns" — without fee qualifiers (those live on the policy pages).
>
> **All Klaviyo render fixes baked in from the start:**
> - `{% unsubscribe %}` stands alone in the footer (no `<a href="">` wrap)
> - First-name personalization with safe fallback: `{{ person.first_name|default:'there' }}`
> - Order number with safe fallback: `{{ event.extra.order_number|default:'' }}`
> - Track-order CTA points to Shopify's order status page: `{{ event.extra.order_status_url|default:'https://shopaydins.com/account' }}`
> - Banned phrases scrubbed: no "handcrafted," "cut," "forged," "made by hand," "crafting"
> - **Irving / "since 2011" framing removed** (per request 2026-05-11). Brand anchor for these emails is now: "small family-run shop" + "free engraving on every ring."

---

## How to use it in Klaviyo

1. Klaviyo → **Flows** → open the **"Customer Thank You"** flow (flow ID: `Tu8u9F`)
2. For each email below: click the email block on the canvas → **Edit Email**
3. **Update Subject + Preview** at the top of the editor (paste from the values below)
4. In the body editor, **delete every existing row/block** until the canvas is empty
5. Drag in a new **HTML** block (under "Content" → "HTML")
6. Paste the matching email HTML below into that block
7. Save → Preview on desktop + mobile → exit

Repeat for T1 → T2.

---

## Push order

| # | Email | Message ID | Trigger | Send delay |
|---|---|---|---|---|
| 1 | Thank You 1 — First-time customer | `TQrkhz` | Placed Order, customer order count = 1 | Immediately after order |
| 2 | Thank You 2 — Repeat customer | `UZQbbr` | Placed Order, customer order count > 1 | Immediately after order |

> ℹ️ **Flow split:** This flow conditionally splits between first-time and repeat customers. The two emails are intentionally different in tone — T1 introduces the workshop and what to expect; T2 thanks them for coming back. Don't merge the two messages.

---

## T1 — Message ID `TQrkhz` (first-time customer)

**Subject:**
```
Your order is in good hands, {{ person.first_name|default:'there' }}.
```

**Preview text:**
```
Here's what happens next. Plus a note from the shop.
```

**Body HTML (paste into a single HTML block):**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:40px !important; line-height:0.95 !important; }
    .ay-step-num { font-size:30px !important; }
    .ay-step-pad { padding:18px 18px !important; }
  }
</style>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Order Received &middot; Free Engraving &middot; Free U.S. Shipping &middot; Lifetime Warranty</p>
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
            <img src="https://cdn.shopify.com/s/files/1/1857/8135/files/Why_Aydins_Jewelry.png?v=1777352028" width="600" alt="Aydins wedding band, shop close-up" style="display:block;width:100%;max-width:600px;height:auto;border:0;">
          </td>
        </tr>

        <!-- EYEBROW + HEADLINE -->
        <tr>
          <td class="ay-pad" style="padding:48px 40px 0 40px;background:#F2EDE4;" align="left">
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Order Confirmed</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Thank you<br>for your order.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">Your piece is in good hands, {{ person.first_name|default:'there' }}.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 16px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">We're a small family-run jewelry shop, and your order just landed on the bench.</p>
            <p style="margin:0;">Here's what the next few days look like.</p>
          </td>
        </tr>

        <!-- STEPS -->
        <tr>
          <td class="ay-pad" style="padding:8px 40px 16px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;">
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;border-bottom:1px solid #D4CDC0;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">01</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Order Received</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">Your order moves into production at the shop.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;border-bottom:1px solid #D4CDC0;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">02</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Personalization</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">If your order includes engraving, we set up the proof and run it on the laser. Double-checked before it goes on the ring.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;border-bottom:1px solid #D4CDC0;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">03</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Inspection &amp; Pack</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">The piece is inspected, polished, and packaged in our gift box.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">04</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Shipped</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">Tracking lands in your inbox once it ships. Usually 1 to 3 business days from order.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:8px 40px 48px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ event.extra.order_status_url|default:'https://shopaydins.com/account' }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">View Order Status &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Engraving questions or anything custom? Reply to this email or write <a href="mailto:sales@shopaydins.com" style="color:#666060;text-decoration:underline;">sales@shopaydins.com</a>. A real person reads every one.</p>
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

## T2 — Message ID `UZQbbr` (repeat customer)

**Subject:**
```
Thank you for coming back, {{ person.first_name|default:'there' }}.
```

**Preview text:**
```
Returning customers are the reason we still do this.
```

**Body HTML (paste into a single HTML block):**

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');
  @media only screen and (max-width:480px) {
    .ay-pad { padding-left:20px !important; padding-right:20px !important; }
    .ay-headline { font-size:38px !important; line-height:0.95 !important; }
    .ay-step-num { font-size:30px !important; }
    .ay-step-pad { padding:18px 18px !important; }
  }
</style>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F2EDE4;font-family:'Poppins',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;margin:0;padding:0;">
  <tr>
    <td align="center" style="padding:0;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#FFFFFF;">

        <!-- TOP BAR -->
        <tr>
          <td style="background:#1A1A1A;padding:11px 20px;text-align:center;">
            <p style="margin:0;font-family:'Poppins',sans-serif;font-size:10px;letter-spacing:2px;color:#B08D57;text-transform:uppercase;font-weight:600;">Welcome Back &middot; Free Engraving &middot; Free U.S. Shipping &middot; Lifetime Warranty</p>
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
            <p style="margin:0 0 18px 0;display:inline-block;font-family:'Poppins',sans-serif;font-size:11px;letter-spacing:3px;color:#B08D57;text-transform:uppercase;font-weight:700;padding-left:14px;border-left:3px solid #B08D57;">Welcome Back</p>
            <h1 class="ay-headline" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:54px;line-height:0.95;color:#1A1A1A;font-weight:400;letter-spacing:1.5px;text-transform:uppercase;">Thank you<br>for coming back.</h1>
            <p style="margin:14px 0 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-style:italic;color:#355E3B;">Good to see you again, {{ person.first_name|default:'there' }}.</p>
          </td>
        </tr>

        <!-- BODY COPY -->
        <tr>
          <td class="ay-pad" style="padding:32px 40px 16px 40px;background:#F2EDE4;font-family:'Poppins',sans-serif;font-size:14px;line-height:1.85;color:#666060;" align="left">
            <p style="margin:0 0 16px 0;">We saw your order come through and wanted to say thanks. Repeat customers are the reason we still do this.</p>
            <p style="margin:0;">You know the drill, but here's the timeline anyway.</p>
          </td>
        </tr>

        <!-- STEPS -->
        <tr>
          <td class="ay-pad" style="padding:8px 40px 16px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #D4CDC0;">
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;border-bottom:1px solid #D4CDC0;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">01</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Order Received</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">Your order moves into production at the shop.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;border-bottom:1px solid #D4CDC0;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">02</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Personalization</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">If your order includes engraving, we set up the proof and run it on the laser. Double-checked before it goes on the ring.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;border-bottom:1px solid #D4CDC0;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">03</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Inspection &amp; Pack</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">The piece is inspected, polished, and packaged in our gift box.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
              <tr>
                <td class="ay-step-pad" style="padding:22px 24px;" valign="top">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                    <td width="56" valign="top" style="width:56px;">
                      <p class="ay-step-num" style="margin:0;font-family:'Bebas Neue','Impact','Arial Black',sans-serif;font-size:36px;color:#B08D57;line-height:1;letter-spacing:1px;">04</p>
                    </td>
                    <td valign="top">
                      <p style="margin:0 0 4px 0;font-family:'Poppins',sans-serif;font-size:12px;letter-spacing:2px;color:#1A1A1A;text-transform:uppercase;font-weight:700;">Shipped</p>
                      <p style="margin:0;font-family:'Poppins',sans-serif;font-size:13px;line-height:1.7;color:#666060;">Tracking lands in your inbox once it ships. Usually 1 to 3 business days from order.</p>
                    </td>
                  </tr></table>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- CTA -->
        <tr>
          <td class="ay-pad" style="padding:8px 40px 48px 40px;background:#F2EDE4;" align="left">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="background:#1A1A1A;padding:17px 38px;">
                  <a href="{{ event.extra.order_status_url|default:'https://shopaydins.com/account' }}" style="font-family:'Poppins',-apple-system,sans-serif;font-size:12px;letter-spacing:2px;color:#F2EDE4;text-decoration:none;text-transform:uppercase;font-weight:700;">View Order Status &rarr;</a>
                </td>
              </tr>
            </table>
            <p style="margin:14px 0 0 0;font-family:'Poppins',sans-serif;font-size:11px;color:#999090;line-height:1.6;">Anything we can help with? Sizing, gift ideas, custom work, just reply here or write <a href="mailto:sales@shopaydins.com" style="color:#666060;text-decoration:underline;">sales@shopaydins.com</a>. We answer everything.</p>
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

## Self-check before saving each email

For T1 and T2, verify:

- [ ] Subject + Preview pasted from this doc (don't leave the old "ranjy" copy)
- [ ] HTML block is the ONLY block on the canvas (delete all stock rows first)
- [ ] First-name personalization renders with fallback (preview as a test profile WITHOUT a first name — should read "there")
- [ ] Order status CTA points to `{{ event.extra.order_status_url|default:'https://shopaydins.com/account' }}` — verify by clicking through in the desktop preview
- [ ] No "handcrafted," "made by hand," "forged," "crafting" anywhere in the body
- [ ] No fabricated warranty language ("lifetime warranty included" without disclosure, "free lifetime sizing," "30-day free returns")
- [ ] No emoji
- [ ] `{% unsubscribe %}` renders as a clickable link in the test send (not raw `{% unsubscribe %}` text)
- [ ] Mobile preview: headline doesn't run off-canvas, step numbers don't collide with text, CTA is tappable

---

## What you're shipping when this is done

A two-email post-purchase flow that:
- Tells first-time buyers what to expect from the Irving shop — no inflated claims, no fabricated guarantees
- Thanks repeat customers in their own tone (they don't need re-introduction; they need acknowledgement)
- Routes them to their order status page with a working CTA
- Holds the visual brand across the whole journey (popup → welcome → abandoned cart → thank you)

---

## Next up

Push it, send tests on both branches (first-time + repeat), then we move to **Browse Abandonment (`T6q2n5`)** — single email, viewed-item card, same shell.
