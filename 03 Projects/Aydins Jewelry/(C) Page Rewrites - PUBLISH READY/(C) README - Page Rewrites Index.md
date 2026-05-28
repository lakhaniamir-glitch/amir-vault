---
folder: (C) Page Rewrites - PUBLISH READY
purpose: Single-source HTML files for every Aydins Jewelry static page. Paste-ready for Shopify.
last-updated: 2026-05-17
source-of-truth: This folder. Edit the HTML here, then paste into Shopify. No mirror sync required.
---

# Page Rewrites Index

Paste-ready HTML for every Aydins Jewelry static page. This folder IS the source of truth. Open the `.html` file, select all, copy, paste into Shopify.

## How to use this folder (3 steps)

1. Open the `.html` file in Obsidian (or VS Code, any editor).
2. Select all, copy the full file contents.
3. In Shopify Admin -> Online Store -> Pages -> [matching page] -> click the `<>` (Show HTML) button -> Select all -> Paste -> Save.
4. Preview the page on the live site before walking away.

Edit the HTML directly in this folder. No copy-paste mirror dance, no second location to keep in sync.

## File map

| File | Shopify handle | URL on site | What it is |
|------|----------------|-------------|------------|
| `shipping.html` | `shipping` | `/pages/shipping` | Shipping policy, transit times, free-shipping threshold. |
| `returns-exchanges.html` | `returns-exchanges` | `/pages/returns-exchanges` | 30-day return + exchange policy. Source of truth for "30-day exchange" language across the site. |
| `lifetime-sizing-lifetime-warranty.html` | `lifetime-sizing-lifetime-warranty` | `/pages/lifetime-sizing-lifetime-warranty` | Lifetime Sizing program + Aydins Lifetime Warranty. Source of truth for fee schedule (free first 6mo, $34.50 mo 7-12, $54.50 after). |
| `aydins-protection-plan-terms-conditions.html` | `aydins-protection-plan-terms-conditions` | `/pages/aydins-protection-plan-terms-conditions` | Paid protection plan T&Cs (upsell at checkout). |
| `free-laser-engraving.html` | `free-laser-engraving` | `/pages/free-laser-engraving` | Free engraving program overview. |
| `price-match-guarantee.html` | `price-match-guarantee` | `/pages/price-match-guarantee` | Price-match policy. |
| `faqs.html` | `faqs` | `/pages/faqs` | Frequently asked questions. |
| `about-aydins.html` | `about-aydins` | `/pages/about-aydins` | About / brand story page. |
| `why-aydins-jewelry.html` | `why-aydins-jewelry` | `/pages/why-aydins-jewelry` | Trust pillars / why-buy-from-us page. |

## Related pages (different folders)

These also paste into Shopify pages but live elsewhere because they have richer companion docs:

| Surface | File location |
|---------|---------------|
| Size Chart popup (PDP modal) | [[03 Projects/Aydins Jewelry/03 Assets/(C) CODE - Size Chart Popup.md]] |
| Interactive Ring Sizer | [[03 Projects/Aydins Jewelry/03 Assets/(C) ring-sizer-tool.md]] |
| Sizing Guide page | [[03 Projects/Aydins Jewelry/03 Assets/(C) ring-size-guide-page.md]] |

## Notification templates (different folder)

Email notification HTML lives in:
`(C) Shopify Notification Templates - BETA 2026-05-15/`

Not pages, but same paste-ready format. Stays separate because Shopify edits these in a different admin section (Settings -> Notifications -> Customer notifications).

## Editing rules

- **No em dashes.** Locked rule, 2026-05-15. Use periods, commas, colons, semicolons, parens.
- **No fabricated policy.** Never write "free lifetime resizing," "lifetime warranty" (use "Aydins Lifetime Warranty"), or "30-day free returns" as customer-facing claims. Match the live source-of-truth files.
- **Aydins email:** `sales@shopaydins.com`
- **Aydins phone:** `1-800-214-7345`
- **Pillar topbar (where used):** "Free engraving . Free U.S. shipping . Aydins Lifetime Warranty . 30-day returns"

## Mirror sync

The `.claude/page-rewrites/` folder contains the same HTML files plus build scripts, SEO meta docs, schema JSON, and raw-fetch archives. If you edit a file here, copy it to `.claude/page-rewrites/` to keep the mirror in sync. If you edit there, copy it back here.

Future improvement: a single sync script that mirrors both directions. Not built yet.
