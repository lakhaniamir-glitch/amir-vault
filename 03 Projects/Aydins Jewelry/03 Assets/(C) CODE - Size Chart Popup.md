---
template: Aydins Size Chart Popup (PDP modal + /pages/size-chart standalone)
paste-into: Shopify Admin → Online Store → Pages → "Size Chart" → Show HTML (`<>`)
source-spec: (C) size-chart-redesign-spec.md
related: (C) ring-sizer-tool.md, (C) ring-size-guide-page.md
version: V4 (built 2026-05-18, mobile button collision patch)
patch-notes: |
  V4 changes:
  - Fixed mobile rendering bug where the primary CTA button rendered as a solid black box with invisible text on Shopify Kalles theme.
  - Root cause: class names `.btn`, `.btn-primary`, `.btn-secondary` collided with Kalles theme's own button classes, which apply !important overrides that hid the button label.
  - Fix: renamed to `.aydins-btn`, `.aydins-btn-primary`, `.aydins-btn-secondary`, `.aydins-btn-row` so nothing in the theme can touch them.
  - Hardened with `a.aydins-btn` element+class selector + `!important` + hardcoded hex colors (no CSS custom property indirection) for maximum specificity against any future theme update.

  V3 changes:
  - Added half sizes to all four conversion tables (US 4.5 through 14.5, plus matching UK letter, EU/Swiss circumference, Japan JIS). Customers select half sizes constantly; chart now shows them.
  - Half-size math: +0.4064 mm inside-diameter per half-step (ISO 8653 standard).
  - Added a prominent CTA in the hero linking to the interactive ring sizer at /pages/find-your-ring-size.
  - Added a second CTA button at the end of the How to Measure section so customers who prefer a guided tool can jump to it from there too.

  V2 corrections (carried forward from prior build):
  1. US Diameter (in) and Circumference (in) values fixed to ISO 8653 standard (0.0320 in/size increment, not the 0.0245 V1 used). V1 would have given customers rings 1.5 to 3 sizes too big when measuring with string.
  2. EU table header relabeled: V1 said "Germany" but the values were actually inside diameter in mm. Now correctly shows EU (Germany/France) circumference and Switzerland.
  3. "Asia" tab renamed to "Japan" (China and Japan use different systems, combining was misleading).
  4. All em dashes scrubbed (locked rule 2026-05-15).
  5. "Free resizing in the first year" removed (banned phrase, fabricated policy).
  6. Reassurance block rewritten to match live /pages/returns-exchanges + /pages/lifetime-sizing-lifetime-warranty source-of-truth.
  7. "Lifetime Warranty" -> "Aydins Lifetime Warranty" (branded form).
  8. SVG `viewbox` -> `viewBox` (proper camelCase).
  9. Out-of-palette blue hover `#0A5A92` replaced with charcoal `#333333`.
  10. UK/Japan letter/number values aligned with ring-sizer-tool.md so the two surfaces agree.
---

# Paste-Ready Code: Size Chart Popup

**How to use:** Copy everything inside the code block below. In Shopify, replace the entire HTML body of the Size Chart page, then Save. Test the popup on a PDP on mobile + desktop before going live.

```html
<div class="aydins-sc">
  <style>
    /* Aydins Jewelry. Size Chart, scoped to .aydins-sc */
    .aydins-sc { --ink:#1A1A1A; --bone:#FAF8F4; --stone:#EEEAE2; --hairline:#E5E2DB; --charcoal:#333333; --brass:#B08D57; --white:#FFFFFF;
      background: var(--bone); color: var(--ink); font-family: Poppins, system-ui, -apple-system, "Segoe UI", sans-serif;
      max-width: 720px; margin: 0 auto; padding: 40px 20px; line-height: 1.65; -webkit-font-smoothing: antialiased; }
    .aydins-sc * { box-sizing: border-box; }
    .aydins-sc h1, .aydins-sc h2, .aydins-sc h3, .aydins-sc p { margin: 0; }
    .aydins-sc .eyebrow { font-size: 12px; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase; color: var(--charcoal); margin-bottom: 16px; }
    .aydins-sc .eyebrow::after { content: ""; display: block; width: 32px; height: 2px; background: var(--brass); margin-top: 10px; }
    .aydins-sc .eyebrow.no-rule::after { display: none; }
    .aydins-sc .h1 { font-family: "Cormorant Garamond", Georgia, serif; font-weight: 500; font-size: 32px; line-height: 1.05; letter-spacing: -0.01em; margin-bottom: 16px; }
    .aydins-sc .h2 { font-size: 24px; font-weight: 600; line-height: 1.2; letter-spacing: -0.005em; margin-bottom: 12px; }
    .aydins-sc .h3 { font-size: 18px; font-weight: 600; line-height: 1.3; margin-bottom: 12px; }
    .aydins-sc .lead { font-size: 16px; line-height: 1.65; margin-bottom: 24px; }
    .aydins-sc a.aydins-btn { display: inline-block !important; padding: 14px 24px !important; font-size: 14px !important; font-weight: 500 !important; letter-spacing: 0.12em !important; text-transform: uppercase !important; text-decoration: none !important; border-radius: 2px !important; border: 1px solid #1A1A1A !important; line-height: 1.2 !important; transition: background 150ms linear, color 150ms linear; cursor: pointer; box-shadow: none !important; }
    .aydins-sc a.aydins-btn-primary { background: #1A1A1A !important; color: #FAF8F4 !important; border-color: #1A1A1A !important; }
    .aydins-sc a.aydins-btn-primary:hover { background: #333333 !important; border-color: #333333 !important; color: #FAF8F4 !important; }
    .aydins-sc a.aydins-btn-secondary { background: transparent !important; color: #1A1A1A !important; border-color: #1A1A1A !important; }
    .aydins-sc a.aydins-btn-secondary:hover { background: #1A1A1A !important; color: #FAF8F4 !important; }
    .aydins-sc .aydins-btn-row { display: flex; gap: 12px; flex-wrap: wrap; }
    .aydins-sc .ghost-link { display: inline-block; margin-top: 16px; font-size: 14px; font-weight: 500; color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--ink); padding-bottom: 1px; }
    .aydins-sc .ghost-link:hover { border-bottom-width: 2px; }
    .aydins-sc section { padding: 40px 0; border-top: 1px solid var(--hairline); }
    .aydins-sc section:first-of-type { border-top: 0; padding-top: 0; }
    .aydins-sc .cards { display: grid; grid-template-columns: 1fr; gap: 16px; margin-top: 24px; }
    .aydins-sc .card { border: 1px solid var(--hairline); border-radius: 2px; padding: 24px; background: var(--white); }
    .aydins-sc .card .num { font-size: 12px; font-weight: 500; letter-spacing: 0.18em; color: var(--brass); margin-bottom: 12px; }
    .aydins-sc .card .ct { font-size: 18px; font-weight: 600; margin-bottom: 8px; line-height: 1.3; }
    .aydins-sc .card .cd { font-size: 14px; color: var(--charcoal); margin-bottom: 16px; line-height: 1.5; }
    .aydins-sc .method { padding: 24px 0; }
    .aydins-sc .method + .method { border-top: 1px solid var(--hairline); margin-top: 24px; padding-top: 32px; }
    .aydins-sc .steps { display: grid; grid-template-columns: 1fr; gap: 24px; margin-top: 16px; }
    .aydins-sc .step { text-align: left; }
    .aydins-sc .step-svg { width: 100%; max-width: 200px; height: 120px; background: var(--white); border: 1px solid var(--hairline); border-radius: 2px; display: block; margin-bottom: 12px; }
    .aydins-sc .step-num { font-size: 12px; font-weight: 500; letter-spacing: 0.18em; color: var(--brass); margin-bottom: 6px; }
    .aydins-sc .step-text { font-size: 14px; color: var(--ink); line-height: 1.5; }
    .aydins-sc .notes { margin-top: 32px; padding-top: 24px; border-top: 1px solid var(--hairline); }
    .aydins-sc .notes p { font-size: 14px; font-weight: 500; margin-bottom: 12px; color: var(--charcoal); letter-spacing: 0.05em; text-transform: uppercase; }
    .aydins-sc .notes ul { margin: 0; padding-left: 20px; font-size: 15px; line-height: 1.7; }
    .aydins-sc .notes li { margin-bottom: 6px; }
    .aydins-sc .tabs { display: flex; gap: 24px; border-bottom: 1px solid var(--hairline); margin: 16px 0 0; flex-wrap: wrap; }
    .aydins-sc .tab { background: none; border: 0; padding: 12px 0; font-family: inherit; font-size: 14px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; color: var(--charcoal); cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -1px; }
    .aydins-sc .tab.active { color: var(--ink); border-bottom-color: var(--ink); }
    .aydins-sc .tab-panel { display: none; margin-top: 24px; }
    .aydins-sc .tab-panel.active { display: block; }
    .aydins-sc table { width: 100%; border-collapse: collapse; }
    .aydins-sc thead th { font-size: 12px; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase; color: var(--charcoal); text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--ink); }
    .aydins-sc tbody td { padding: 10px 12px; font-size: 14px; color: var(--ink); border-bottom: 1px solid var(--hairline); }
    .aydins-sc tbody tr:nth-child(even) td { background: var(--stone); }
    .aydins-sc .reassure { background: var(--stone); padding: 32px 24px; border-radius: 2px; }
    .aydins-sc .reassure .h2 { margin-bottom: 12px; }
    .aydins-sc .reassure p { font-size: 15px; margin: 0 0 14px; max-width: 560px; }
    .aydins-sc .reassure p:last-of-type { margin-bottom: 22px; }
    .aydins-sc .reassure .aydins-btn-row { justify-content: flex-start; }
    @media (min-width: 720px) {
      .aydins-sc { padding: 80px 40px; }
      .aydins-sc .h1 { font-size: 40px; }
      .aydins-sc .h2 { font-size: 28px; }
      .aydins-sc section { padding: 56px 0; }
      .aydins-sc .cards { grid-template-columns: repeat(3, 1fr); gap: 24px; }
      .aydins-sc .steps { grid-template-columns: repeat(3, 1fr); gap: 32px; }
      .aydins-sc a.aydins-btn { padding: 16px 32px !important; }
    }
    @media (prefers-reduced-motion: reduce) {
      .aydins-sc a.aydins-btn { transition: none !important; }
    }
  </style>

  <!-- A. Hero -->
  <section>
    <div class="eyebrow">Ring Sizing</div>
    <h1 class="h1">Find your ring size.</h1>
    <p class="lead">Not sure? Use a ring you already own, or measure with a string. If the size is off, you are covered: 30-day exchange on unengraved rings, and Lifetime Sizing for the original purchaser after that.</p>
    <div class="aydins-btn-row">
      <a href="https://shopaydins.com/pages/find-your-ring-size" class="aydins-btn aydins-btn-primary">Find Your Size at Home</a>
      <a href="#measure" class="aydins-btn aydins-btn-secondary">See How to Measure</a>
    </div>
    <a href="#conversion" class="ghost-link">Already know your size? Use the chart below →</a>
  </section>

  <!-- B. Three ways -->
  <section>
    <div class="eyebrow no-rule">Three Ways to Find Your Size</div>
    <h2 class="h2">Pick the path that fits.</h2>
    <div class="cards">
      <div class="card">
        <div class="num">01</div>
        <div class="ct">Use a Ring You Own</div>
        <div class="cd">Most accurate. Measure the inside diameter of a ring that already fits.</div>
        <a href="#method-a" class="ghost-link">Show method →</a>
      </div>
      <div class="card">
        <div class="num">02</div>
        <div class="ct">Measure at Home</div>
        <div class="cd">String and a ruler. Takes about two minutes.</div>
        <a href="#method-b" class="ghost-link">Show me how →</a>
      </div>
      <div class="card">
        <div class="num">03</div>
        <div class="ct">Convert a Size</div>
        <div class="cd">If you already know your UK, EU, or Japan size.</div>
        <a href="#conversion" class="ghost-link">See chart →</a>
      </div>
    </div>
  </section>

  <!-- C. How to measure (two methods) -->
  <section id="measure">
    <div class="eyebrow no-rule">How to Measure</div>
    <h2 class="h2">Two methods, both accurate.</h2>

    <!-- Method A: ring you already own -->
    <div class="method" id="method-a">
      <h3 class="h3">Method A: Use a ring you already own</h3>
      <div class="steps">
        <div class="step">
          <svg class="step-svg" viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="0" y="0" width="200" height="120" fill="#FFFFFF"></rect>
            <ellipse cx="100" cy="60" rx="42" ry="24" stroke="#1A1A1A" stroke-width="1.5" fill="none"></ellipse>
            <ellipse cx="100" cy="60" rx="32" ry="16" stroke="#1A1A1A" stroke-width="1" fill="none" stroke-dasharray="3 3"></ellipse>
            <text x="84" y="106" font-family="Poppins" font-size="9" fill="#333">your ring</text>
          </svg>
          <div class="step-num">01</div>
          <div class="step-text">Find a ring that already fits the correct finger comfortably.</div>
        </div>
        <div class="step">
          <svg class="step-svg" viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="0" y="0" width="200" height="120" fill="#FFFFFF"></rect>
            <rect x="30" y="20" width="140" height="80" stroke="#1A1A1A" stroke-width="1" fill="none"></rect>
            <ellipse cx="100" cy="60" rx="22" ry="12" stroke="#1A1A1A" stroke-width="1.5" fill="none" stroke-dasharray="3 3"></ellipse>
            <text x="80" y="14" font-family="Poppins" font-size="9" fill="#333">paper</text>
          </svg>
          <div class="step-num">02</div>
          <div class="step-text">Place the ring on paper and trace the inside circle.</div>
        </div>
        <div class="step">
          <svg class="step-svg" viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="0" y="0" width="200" height="120" fill="#FFFFFF"></rect>
            <rect x="20" y="55" width="160" height="20" stroke="#1A1A1A" stroke-width="1.5" fill="none"></rect>
            <line x1="40" y1="55" x2="40" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="60" y1="55" x2="60" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="80" y1="55" x2="80" y2="68" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="100" y1="55" x2="100" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="120" y1="55" x2="120" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="140" y1="55" x2="140" y2="68" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="160" y1="55" x2="160" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="70" y1="80" x2="130" y2="80" stroke="#B08D57" stroke-width="2" stroke-linecap="round"></line>
            <text x="78" y="98" font-family="Poppins" font-size="9" fill="#1A1A1A">diameter</text>
          </svg>
          <div class="step-num">03</div>
          <div class="step-text">Measure the inside diameter across the widest point. Match it to the chart below.</div>
        </div>
      </div>
    </div>

    <!-- Method B: string and ruler -->
    <div class="method" id="method-b">
      <h3 class="h3">Method B: String and a ruler</h3>
      <div class="steps">
        <div class="step">
          <svg class="step-svg" viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="0" y="0" width="200" height="120" fill="#FFFFFF"></rect>
            <path d="M60 30 Q40 60 60 90 Q80 100 100 90 Q120 80 100 60 Q90 50 80 55 Q70 60 75 70" stroke="#1A1A1A" stroke-width="1.5" fill="none" stroke-linecap="round"></path>
            <circle cx="80" cy="65" r="22" stroke="#1A1A1A" stroke-width="1.5" fill="none" stroke-dasharray="3 3"></circle>
            <line x1="120" y1="40" x2="180" y2="60" stroke="#1A1A1A" stroke-width="1.5" stroke-linecap="round"></line>
            <text x="125" y="35" font-family="Poppins" font-size="9" fill="#333">string</text>
          </svg>
          <div class="step-num">01</div>
          <div class="step-text">Wrap a string snug at the base of the finger.</div>
        </div>
        <div class="step">
          <svg class="step-svg" viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="0" y="0" width="200" height="120" fill="#FFFFFF"></rect>
            <line x1="30" y1="60" x2="170" y2="60" stroke="#1A1A1A" stroke-width="1.5" stroke-linecap="round"></line>
            <line x1="105" y1="48" x2="105" y2="72" stroke="#B08D57" stroke-width="2" stroke-linecap="round"></line>
            <text x="95" y="42" font-family="Poppins" font-size="9" fill="#1A1A1A">mark</text>
          </svg>
          <div class="step-num">02</div>
          <div class="step-text">Mark the spot where the string overlaps.</div>
        </div>
        <div class="step">
          <svg class="step-svg" viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="0" y="0" width="200" height="120" fill="#FFFFFF"></rect>
            <rect x="20" y="55" width="160" height="20" stroke="#1A1A1A" stroke-width="1.5" fill="none"></rect>
            <line x1="40" y1="55" x2="40" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="60" y1="55" x2="60" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="80" y1="55" x2="80" y2="68" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="100" y1="55" x2="100" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="120" y1="55" x2="120" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="140" y1="55" x2="140" y2="68" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="160" y1="55" x2="160" y2="65" stroke="#1A1A1A" stroke-width="1"></line>
            <line x1="40" y1="80" x2="140" y2="80" stroke="#B08D57" stroke-width="2" stroke-linecap="round"></line>
            <text x="78" y="98" font-family="Poppins" font-size="9" fill="#1A1A1A">measure</text>
          </svg>
          <div class="step-num">03</div>
          <div class="step-text">Measure the marked length. Match the circumference to the chart.</div>
        </div>
      </div>
    </div>

    <div class="notes">
      <p>A few notes from the workshop</p>
      <ul>
        <li>Measure at the end of the day. Fingers are larger by then.</li>
        <li>Measure the hand the ring will live on. The dominant hand is usually a half-size larger.</li>
        <li>A wider band (6mm+) wears a half-size tighter. If between two sizes, size up.</li>
      </ul>
    </div>

    <div style="margin-top:32px;padding-top:24px;border-top:1px solid var(--hairline);text-align:center;">
      <p style="font-size:14px;color:var(--charcoal);margin:0 0 14px;">Prefer a guided tool? Use the interactive ring sizer.</p>
      <a href="https://shopaydins.com/pages/find-your-ring-size" class="aydins-btn aydins-btn-primary">Use the Interactive Ring Sizer</a>
    </div>
  </section>

  <!-- D. International conversion. Data: ISO 8653 standard, 0.8128mm per US size, base US 0 = 11.63mm diameter. -->
  <section id="conversion">
    <div class="eyebrow no-rule">International Conversion</div>
    <h2 class="h2">Find your size by region.</h2>
    <div class="tabs" role="tablist">
      <button class="tab active" data-tab="us" role="tab">US</button>
      <button class="tab" data-tab="uk" role="tab">UK</button>
      <button class="tab" data-tab="eu" role="tab">EU</button>
      <button class="tab" data-tab="japan" role="tab">Japan</button>
    </div>

    <div class="tab-panel active" data-panel="us">
      <table>
        <thead><tr>
<th>US Size</th>
<th>Diameter (in)</th>
<th>Circumference (in)</th>
<th>Diameter (mm)</th>
</tr></thead>
        <tbody>
          <tr><td>4</td><td>0.586</td><td>1.84</td><td>14.88</td></tr>
          <tr><td>4½</td><td>0.602</td><td>1.89</td><td>15.29</td></tr>
          <tr><td>5</td><td>0.618</td><td>1.94</td><td>15.70</td></tr>
          <tr><td>5½</td><td>0.634</td><td>1.99</td><td>16.10</td></tr>
          <tr><td>6</td><td>0.650</td><td>2.04</td><td>16.51</td></tr>
          <tr><td>6½</td><td>0.666</td><td>2.09</td><td>16.92</td></tr>
          <tr><td>7</td><td>0.682</td><td>2.14</td><td>17.32</td></tr>
          <tr><td>7½</td><td>0.698</td><td>2.19</td><td>17.73</td></tr>
          <tr><td>8</td><td>0.714</td><td>2.24</td><td>18.14</td></tr>
          <tr><td>8½</td><td>0.730</td><td>2.29</td><td>18.54</td></tr>
          <tr><td>9</td><td>0.746</td><td>2.34</td><td>18.95</td></tr>
          <tr><td>9½</td><td>0.762</td><td>2.39</td><td>19.36</td></tr>
          <tr><td>10</td><td>0.778</td><td>2.44</td><td>19.76</td></tr>
          <tr><td>10½</td><td>0.794</td><td>2.49</td><td>20.17</td></tr>
          <tr><td>11</td><td>0.810</td><td>2.54</td><td>20.57</td></tr>
          <tr><td>11½</td><td>0.826</td><td>2.59</td><td>20.98</td></tr>
          <tr><td>12</td><td>0.842</td><td>2.65</td><td>21.39</td></tr>
          <tr><td>12½</td><td>0.858</td><td>2.70</td><td>21.79</td></tr>
          <tr><td>13</td><td>0.874</td><td>2.75</td><td>22.20</td></tr>
          <tr><td>13½</td><td>0.890</td><td>2.80</td><td>22.61</td></tr>
          <tr><td>14</td><td>0.906</td><td>2.85</td><td>23.01</td></tr>
          <tr><td>14½</td><td>0.922</td><td>2.90</td><td>23.42</td></tr>
          <tr><td>15</td><td>0.938</td><td>2.95</td><td>23.83</td></tr>
        </tbody>
      </table>
    </div>

    <div class="tab-panel" data-panel="uk">
      <table>
        <thead><tr>
<th>US</th>
<th>UK / Australia / NZ</th>
<th>Diameter (mm)</th>
</tr></thead>
        <tbody>
          <tr><td>4</td><td>H</td><td>14.88</td></tr>
          <tr><td>4½</td><td>I</td><td>15.29</td></tr>
          <tr><td>5</td><td>J ½</td><td>15.70</td></tr>
          <tr><td>5½</td><td>K</td><td>16.10</td></tr>
          <tr><td>6</td><td>L ½</td><td>16.51</td></tr>
          <tr><td>6½</td><td>M</td><td>16.92</td></tr>
          <tr><td>7</td><td>N ½</td><td>17.32</td></tr>
          <tr><td>7½</td><td>O</td><td>17.73</td></tr>
          <tr><td>8</td><td>P ½</td><td>18.14</td></tr>
          <tr><td>8½</td><td>Q</td><td>18.54</td></tr>
          <tr><td>9</td><td>R ½</td><td>18.95</td></tr>
          <tr><td>9½</td><td>S</td><td>19.36</td></tr>
          <tr><td>10</td><td>T ½</td><td>19.76</td></tr>
          <tr><td>10½</td><td>U</td><td>20.17</td></tr>
          <tr><td>11</td><td>V ½</td><td>20.57</td></tr>
          <tr><td>11½</td><td>W</td><td>20.98</td></tr>
          <tr><td>12</td><td>X ½</td><td>21.39</td></tr>
          <tr><td>12½</td><td>Y</td><td>21.79</td></tr>
          <tr><td>13</td><td>Z ½</td><td>22.20</td></tr>
          <tr><td>13½</td><td>Z + 1</td><td>22.61</td></tr>
          <tr><td>14</td><td>Z + 2</td><td>23.01</td></tr>
          <tr><td>14½</td><td>Z + 3</td><td>23.42</td></tr>
          <tr><td>15</td><td>Z + 4</td><td>23.83</td></tr>
        </tbody>
      </table>
    </div>

    <div class="tab-panel" data-panel="eu">
      <table>
        <thead><tr>
<th>US</th>
<th>Germany / France</th>
<th>Switzerland</th>
<th>Diameter (mm)</th>
</tr></thead>
        <tbody>
          <tr><td>4</td><td>46.5</td><td>6.5</td><td>14.88</td></tr>
          <tr><td>4½</td><td>48.0</td><td>8.0</td><td>15.29</td></tr>
          <tr><td>5</td><td>49.3</td><td>9.3</td><td>15.70</td></tr>
          <tr><td>5½</td><td>50.6</td><td>10.6</td><td>16.10</td></tr>
          <tr><td>6</td><td>51.9</td><td>11.9</td><td>16.51</td></tr>
          <tr><td>6½</td><td>53.1</td><td>13.1</td><td>16.92</td></tr>
          <tr><td>7</td><td>54.4</td><td>14.4</td><td>17.32</td></tr>
          <tr><td>7½</td><td>55.7</td><td>15.7</td><td>17.73</td></tr>
          <tr><td>8</td><td>57.0</td><td>17.0</td><td>18.14</td></tr>
          <tr><td>8½</td><td>58.2</td><td>18.2</td><td>18.54</td></tr>
          <tr><td>9</td><td>59.5</td><td>19.5</td><td>18.95</td></tr>
          <tr><td>9½</td><td>60.8</td><td>20.8</td><td>19.36</td></tr>
          <tr><td>10</td><td>62.1</td><td>22.1</td><td>19.76</td></tr>
          <tr><td>10½</td><td>63.4</td><td>23.4</td><td>20.17</td></tr>
          <tr><td>11</td><td>64.6</td><td>24.6</td><td>20.57</td></tr>
          <tr><td>11½</td><td>65.9</td><td>25.9</td><td>20.98</td></tr>
          <tr><td>12</td><td>67.2</td><td>27.2</td><td>21.39</td></tr>
          <tr><td>12½</td><td>68.5</td><td>28.5</td><td>21.79</td></tr>
          <tr><td>13</td><td>69.7</td><td>29.7</td><td>22.20</td></tr>
          <tr><td>13½</td><td>71.0</td><td>31.0</td><td>22.61</td></tr>
          <tr><td>14</td><td>72.3</td><td>32.3</td><td>23.01</td></tr>
          <tr><td>14½</td><td>73.6</td><td>33.6</td><td>23.42</td></tr>
          <tr><td>15</td><td>74.8</td><td>34.8</td><td>23.83</td></tr>
        </tbody>
      </table>
      <p style="font-size:13px;color:#4A4A4A;margin-top:14px;">Germany and France use ring circumference in millimeters. Switzerland uses circumference minus 40.</p>
    </div>

    <div class="tab-panel" data-panel="japan">
      <table>
        <thead><tr>
<th>US</th>
<th>Japan</th>
<th>Diameter (mm)</th>
</tr></thead>
        <tbody>
          <tr><td>4</td><td>7</td><td>14.88</td></tr>
          <tr><td>4½</td><td>8</td><td>15.29</td></tr>
          <tr><td>5</td><td>9</td><td>15.70</td></tr>
          <tr><td>5½</td><td>10</td><td>16.10</td></tr>
          <tr><td>6</td><td>12</td><td>16.51</td></tr>
          <tr><td>6½</td><td>13</td><td>16.92</td></tr>
          <tr><td>7</td><td>14</td><td>17.32</td></tr>
          <tr><td>7½</td><td>15</td><td>17.73</td></tr>
          <tr><td>8</td><td>16</td><td>18.14</td></tr>
          <tr><td>8½</td><td>17</td><td>18.54</td></tr>
          <tr><td>9</td><td>18</td><td>18.95</td></tr>
          <tr><td>9½</td><td>19</td><td>19.36</td></tr>
          <tr><td>10</td><td>20</td><td>19.76</td></tr>
          <tr><td>10½</td><td>21</td><td>20.17</td></tr>
          <tr><td>11</td><td>22</td><td>20.57</td></tr>
          <tr><td>11½</td><td>23</td><td>20.98</td></tr>
          <tr><td>12</td><td>25</td><td>21.39</td></tr>
          <tr><td>12½</td><td>26</td><td>21.79</td></tr>
          <tr><td>13</td><td>27</td><td>22.20</td></tr>
          <tr><td>13½</td><td>28</td><td>22.61</td></tr>
          <tr><td>14</td><td>29</td><td>23.01</td></tr>
          <tr><td>14½</td><td>30</td><td>23.42</td></tr>
          <tr><td>15</td><td>31</td><td>23.83</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- E. Reassurance close. Policy matches live /pages/returns-exchanges + /pages/lifetime-sizing-lifetime-warranty -->
  <section>
    <div class="reassure">
      <div class="eyebrow no-rule">Exchanges, Sizing &amp; Warranty</div>
      <h2 class="h2">If your size is off, you are covered.</h2>
      <p><strong>30-day exchange.</strong> Unengraved standard rings exchange free within 30 days. Engraved rings are exchange-only with a $34.50 surcharge.</p>
      <p><strong>Lifetime Sizing.</strong> Fit changes after 30 days are covered for the original purchaser at a small flat fee, with no time limit.</p>
      <p><strong>Aydins Lifetime Warranty.</strong> Manufacturing defects are covered free for the first 6 months, then $34.50 through month 12, then $54.50 flat after that.</p>
      <div class="aydins-btn-row">
        <a href="mailto:sales@shopaydins.com" class="aydins-btn aydins-btn-secondary">Email Us</a>
        <a href="tel:18002147345" class="aydins-btn aydins-btn-secondary">Call 1-800-214-7345</a>
      </div>
    </div>
  </section>

  <script>
    (function(){
      var root = document.querySelector('.aydins-sc');
      if (!root) return;
      var tabs = root.querySelectorAll('.tab');
      var panels = root.querySelectorAll('.tab-panel');
      tabs.forEach(function(tab){
        tab.addEventListener('click', function(){
          var target = tab.getAttribute('data-tab');
          tabs.forEach(function(t){ t.classList.remove('active'); });
          panels.forEach(function(p){ p.classList.remove('active'); });
          tab.classList.add('active');
          var panel = root.querySelector('.tab-panel[data-panel="'+target+'"]');
          if (panel) panel.classList.add('active');
        });
      });
    })();
  </script>
</div>
```

---

## Data verification

Standard used: **ISO 8653 / North American ring sizing**. Each US size adds **0.8128 mm (1/32 in) of inside diameter**. Spot-check the math:

| US | Calc: 11.63 + size × 0.8128 mm | Chart value (mm) | Match |
|----|--------------------------------|------------------|-------|
| 4  | 14.88                          | 14.88            | ✓     |
| 7  | 17.32                          | 17.32            | ✓     |
| 10 | 19.76                          | 19.76            | ✓     |
| 13 | 22.20                          | 22.20            | ✓     |
| 15 | 23.83                          | 23.83            | ✓     |

Inches and circumference values derived from these mm values: `inches = mm / 25.4` and `circumference = π × diameter`. The mm column in every regional tab is identical because diameter does not change between regions — only the regional label does.

This data is also consistent with the [[(C) ring-sizer-tool.md]] mm table, so the two surfaces agree.
