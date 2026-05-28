# Aydins Klaviyo Abandoned Cart Emails – Metadata

Generated: 2026-05-14 01:04 UTC  
Flow: TrNjjf (Abandoned Cart Reminder)  
Spec: KLAVIYO-EMAIL-STANDARD.md v1.0  
Voice: V5 editorial, masculine, family‑run  

---

## Email 1 – sent 1 hour after abandon

**Subject A:** You left something in your cart  
**Subject B:** Still thinking it over?  
**Preview text:** Your ring is saved. Free engraving included.  
**From name:** Aydins Jewelry  
**Reply‑to:** sales@shopaydins.com  

**Open items:**  
- `[HERO_IMAGE_URL]` placeholder – replace with actual landing‑page hero image URL (likely from `/pages/lifetime‑sizing‑lifetime‑warranty` or `[[(C) Ring Care Guide — Shopify Page Content]]`)  
- Product image fallback – merge tag `{{ item.product.images[0]|default:'' }}` will show alt text if image missing  

---

## Email 2 – sent 24 hours after abandon

**Subject A:** About your cart: a few things to know  
**Subject B:** Sizing, engraving, returns: answered  
**Preview text:** What happens if it doesn't fit? Read this before you decide.  
**From name:** Aydins Jewelry  
**Reply‑to:** sales@shopaydins.com  

**Open items:**  
- `[HERO_IMAGE_URL]` placeholder – replace with actual landing‑page hero image URL  
- Product image fallback – merge tag `{{ item.product.images[0]|default:'' }}` will show alt text if image missing  

---

## Email 3 – sent 48–72 hours after abandon

**Subject A:** Last note about your cart  
**Subject B:** One more thing before we let it go  
**Preview text:** Free engraving is still on the table. So is your ring.  
**From name:** Aydins Jewelry  
**Reply‑to:** sales@shopaydins.com  

**Open items:**  
- `[HERO_IMAGE_URL]` placeholder – replace with actual landing‑page hero image URL  
- Discount code `WELCOME20` (20% off, 48‑hour expiry) – verify exists in Shopify before deploying Email 3. If only `WELCOME10` exists, repurpose to 20% and rename, or create `WELCOME20` fresh and disable `WELCOME10`. Do not run both.  
- Product image fallback – merge tag `{{ item.product.images[0]|default:'' }}` will show alt text if image missing  

---

## Deploy checklist (from Klaviyo spec Section 12)

For each email, before activating:

- [ ] Subject line declarative, no exclamation, ≤50 chars
- [ ] Preview text complements subject, ≤90 chars
- [ ] Reply‑to set to `sales@shopaydins.com` (in Klaviyo UI)
- [ ] From name set to `Aydins Jewelry` (in Klaviyo UI)
- [ ] No banned phrases (Section 4)
- [ ] Only approved trust pillars (Section 5)
- [ ] Voice matches V5 anchors (editorial, masculine, family‑run)
- [ ] Pricing quoted only in research context (abandoned cart = research mode) ✓
- [ ] All merge tags have fallbacks (`{{ first_name|default:'there' }}`, etc.)
- [ ] Phone number listed: `1‑800‑214‑7345`
- [ ] Portal linked: `aydins.thunderreturns.com`
- [ ] `{% unsubscribe %}` in footer
- [ ] Hero image replaced with landing‑page imagery
- [ ] CTA button uses brass `#B08D57`, table‑cell layout
- [ ] Preview sent to yourself + 1 other (iOS Mail, Gmail web, Outlook)
- [ ] Mobile rendering tested
- [ ] All linked URLs tested (no 404)
- [ ] Discount code exists in Shopify (Email 3 only)
- [ ] Suppression rules set if cross‑channel needed (Recart SMS within 24h)

---

## Design fidelity

- **V5 design system:** Cormorant Garamond (serif headers) / Poppins (body)  
- **Palette:** brass `#B08D57`, cream `#F2EBDC`, bone `#FAF8F4`, ink `#1A1A1A`, hairline `#E5E2DB`  
- **Layout:** Mobile‑first, 600px max width, centered, table‑based for Outlook  
- **CTA button:** Solid `#B08D57`, white text, 14px vertical / 32px horizontal padding, 2px border‑radius, rendered as table cell  
- **Hero headline:** Cormorant Garamond italic for `<em>` words with color `#B08D57`  
- **Signature:** Italic, smaller font, ink color  
- **Footer:** 12px Poppins, compact, with sales@shopaydins.com / 1‑800‑214‑7345 / aydins.thunderreturns.com / unsubscribe