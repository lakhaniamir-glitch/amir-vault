# Kalles v5 — Aydins Design Deploy

> **Created:** 2026-05-06
> **Theme:** `kalles-v5-4-0-official` (ID `159068061933`) — unpublished
> **Status:** Files generated and saved here. Manual deploy required (token scope ceiling).

---

## What's in this folder

| File | What it is |
|---|---|
| `aydins-design.css` | The Aydins design layer. Forces Kalles' generated CSS variables to the Aydins palette + adds bespoke utilities (eyebrow, brass, numerals, etc.). Self-contained. |
| `(C) settings_data.aydins.json` | Patched theme settings — Aydins color scheme, Poppins + Cormorant fonts, square 2px radius, button shape, heading sizes. Drop-in replacement for the v5 theme's `config/settings_data.json`. |
| `(C) settings_data.original-backup-2026-05-06.json` | Backup of what was on the v5 theme before any of this — restore from this if anything goes wrong. |

---

## Why this is manual

The Shopify Admin token I'm using (`shpat_...`) has scope `write_theme_code` listed but the REST Admin Asset API requires `write_themes` to PUT any asset, including JSON config files. So I couldn't push these directly.

**Two ways to fix that for next time:**

1. **Grant `write_themes` to the custom app** — Shopify admin → Apps → Develop apps → [the app this token belongs to] → Configuration → Admin API access scopes → enable `write_themes`. Reinstall, get a new token.
2. **Or just keep deploying manually** — for one-off design changes, this is fine.

---

## Deploy in 3 minutes (manual)

### Step 1 — Add the CSS file

1. Shopify admin → **Online Store → Themes**
2. Find `kalles-v5-4-0-official` (the unpublished v5 theme — NOT the live v4)
3. Click `…` → **Edit code**
4. In the left sidebar, scroll to **Assets** → click **Add a new asset**
5. Choose file → upload `aydins-design.css` from this folder
6. Save

### Step 2 — Link the CSS in `theme.liquid`

1. In the same Edit code view, open **Layout → theme.liquid**
2. Find the line that pulls in Kalles' CSS — search for `css-variables` or `theme.scss.css` or `{% render 'css-variables' %}`. There will be a block of `{% render %}` calls and `<link>` tags inside `<head>`.
3. **After** the last Kalles CSS include but **before** `</head>`, paste this single line:

   ```liquid
   {{ 'aydins-design.css' | asset_url | stylesheet_tag }}
   ```

4. Save.

### Step 3 — Replace `settings_data.json` (if you want the theme-editor pickers updated too)

This step is optional if Step 1 is done. Step 1 already forces every Kalles variable to Aydins values via CSS. Step 3 is what makes the **Customize → Theme settings** pickers also reflect those values, so you can toggle them later without editing CSS.

1. In the same Edit code view, open **Config → settings_data.json**
2. **Replace the entire file contents** with the contents of `(C) settings_data.aydins.json` from this folder.
3. Save.
4. Open **Customize** on the v5 theme to verify the color scheme + fonts + radius now show Aydins values.

> **Rollback:** if Step 3 breaks something, paste `(C) settings_data.original-backup-2026-05-06.json` back into `settings_data.json` and save.

### Step 4 — Preview

1. In Themes, find `kalles-v5-4-0-official` → click **Preview**
2. Walk a PDP, the Size Chart page, the Cart, the homepage
3. Check: backgrounds Bone, text Ink, buttons Ink with Bone text, no red sale prices, brass only on accent moments

---

## What the CSS does (one-line summary per block)

- **Aydins palette tokens** — `--aj-ink`, `--aj-bone`, etc. for use anywhere
- **Override Kalles vars** — every `--color-*`, `--hdt-btn-*`, `--radius-*`, `--font-*` Kalles emits, redefined to Aydins values
- **Display rule** — Cormorant on H1 + H0 only, Poppins everywhere else
- **`.aj-eyebrow`** — the brass-underlined micro-label
- **Button voice** — uppercase, +0.12em tracking, no gradients
- **`.aj-numeral`** — large brass display numerals
- **`.aj-card` / `.aj-reassure`** — Aydins surface containers
- **`.aj-table`** — size charts, spec tables
- **`.aj-tabs`** — region tabs, filter tabs
- **`.aj-section`** — opt-in section spacing scale
- **Banned tells** — kills shadows on cards, red sale prices, gradient hovers, generic announcement bar styling

---

## Source of truth

- Design system: [[.claude/DESIGN.md]]
- Aydins design rules: 4 colors max, 2 fonts max, no red, no gradients, no drop shadows, eyebrow above every section H2

If anything in `aydins-design.css` ever conflicts with [[.claude/DESIGN.md]], DESIGN.md wins. Update the CSS to match, not the rule.
