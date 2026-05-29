# Theonar Etsy — VELA CSV Exports

## Drop your VELA exports here

This folder is watched. Any CSV you save here gets synced to the VPS within 10 minutes via Obsidian Git, and BETA Etsy can then read and audit it.

## Workflow

1. Open VELA (or use vela.codes)
2. Filter to your Theonar listings only
3. Export to CSV (Bulk Edit → Export)
4. Save the file here with the date in the name:
   `2026-05-28-vela-theonar-export.csv`
5. Tell BETA Etsy (via dashboard chat, Telegram with @beta-etsy, or directly in Obsidian):

   > @beta-etsy read vault/brands/theonar/etsy-exports/2026-05-28-vela-theonar-export.csv and audit every listing against the locked Theonar brand profile at vault/brands/theonar/profile.md. Flag the top 10 listings that need rewriting first based on view count, favorites, and sales signal in the CSV. Draft replacement titles and tags for those 10. Save the audit report to vault/brands/theonar/etsy-exports/audit-{date}.md.

6. BETA Etsy outputs the audit + drafts. You review on your laptop tomorrow.

## What BETA Etsy will look for

- **Voice violations** (softening words "lovely/beautiful/elegant", fluff openers, missing imperative voice)
- **Brand violations** (em dashes, third-party brand names, bare "lifetime warranty", manufacturing claims)
- **Title structure** — eBay/Etsy SEO best practices vs current
- **Tags** — relevance to titanium + Thor-energy keywords
- **Pricing signals** — outliers vs the rest of your catalog
- **Photo count** — listings under 5 photos flagged
- **Engraving conventions** — Inside vs Inside & Outside tag correctness

## File naming convention

`YYYY-MM-DD-vela-{brand}-export.csv`

Examples:
- `2026-05-28-vela-theonar-export.csv` (Theonar listings)
- `2026-05-28-vela-aydins-export.csv` (Aydins listings, if you ever audit those)

Keep older exports in this folder — useful for diffing what changed between audits.
