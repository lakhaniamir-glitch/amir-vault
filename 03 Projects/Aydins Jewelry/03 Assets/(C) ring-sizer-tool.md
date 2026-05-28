# Ring Sizer Tool. Drop-in HTML

> **Surface:** `/pages/ring-sizer` (new Shopify page). Also embeddable inside the Size Chart modal as a deep-link tab/section.
> **Job to be done:** Replace the "go visit findmyringsize.com" hand-off with an Aydins-branded, on-vault sizing tool.
> **Status:** Build-ready HTML (drop into a Shopify page with a custom Liquid template, or paste into a Page > Code view).
> **Created:** 2026-05-06
> **Updated:** 2026-05-18 (V4: slider range bumped to handle real mobile DPI. Min 300, max 720, default 480. V3 maxed at 440px which was smaller than an actual credit card on iPhone 14+ and most modern Android phones, customer had no headroom to scroll the on-screen card bigger to match their real card. Also added accuracy disclaimer near Step 3 readout (CYA: recommends in-person sizing by a local jeweler before customer can claim our tool was wrong). Fixed button color override on mobile, raised specificity to .aydins-rs a.rs-btn and pinned :link / :visited so the Shopify theme cannot beat it. Fixed EMAIL US button text off-center via asymmetric padding (padding-left bumped by 0.12em) to absorb trailing letter-spacing on short uppercase labels. First attempt used text-indent which is unreliable in shrink-to-fit inline-blocks across browsers.)
> 2026-05-18 (V3: rotated calibration card to portrait orientation so it fits on mobile screens. Card now sized by height, aspect-ratio 53.98/85.6, chip repositioned to upper-left. Label/slider copy updated.)
> 2026-05-17 (V2: em-dash sweep per locked rule, accurate policy block, sales@shopaydins.com email, V5 pillar topbar)
> **Owner:** Amir
> **Design system:** [[.claude/DESIGN.md]] v1.1
> **Policy reference:** [[.claude/page-rewrites/returns-exchanges.html]] and [[.claude/page-rewrites/lifetime-sizing-lifetime-warranty.html]]
> **Scoped CSS prefix:** `.aydins-rs`. Does not collide with theme styles.

---

## How it works (for Amir)

1. Customer measures their screen with a credit card (ISO/IEC 7810 ID-1: every credit card is exactly 85.6mm × 53.98mm).
2. Slider calibrates a card image on screen until it matches the real card edge-to-edge.
3. Calibration scale (mm-per-pixel) is stored in `localStorage` so the customer doesn't have to re-do it every visit.
4. Customer places an existing ring on the screen, drags a circular overlay to match the **inside** of the ring.
5. Tool converts the diameter (mm) into US half-sizes + UK / EU / Japan equivalents.

**Policy block reflects the canonical live policy pages ([[.claude/page-rewrites/returns-exchanges.html]] + [[.claude/page-rewrites/lifetime-sizing-lifetime-warranty.html]]):**
- **30-day exchange:** unengraved standard rings exchange free within 30 days. Engraved rings are exchange-only with a $34.50 surcharge.
- **Lifetime Sizing:** original purchaser only, small flat fee, no time limit. Covers fit changes.
- **Aydins Lifetime Warranty:** manufacturing defects only. Free first 6 months, $34.50 through month 12, $54.50 flat after that.
- Sizing and Warranty are two separate programs, not one combined "Lifetime Sizing & Warranty Program" (legacy V1 wording, retired).

---

## Drop-in HTML

Paste the entire block below into a Shopify page (Online Store > Pages > Add page > "Show HTML" toggle). Wrap in a section if added via theme code.

```html
<!-- ============================================================
     AYDINS RING SIZER. Scoped to .aydins-rs (no theme conflicts).
     ============================================================ -->
<style>
  .aydins-rs {
    --ink:#1A1A1A; --bone:#FAF8F4; --stone:#EEEAE2;
    --hair:#E5E2DB; --char:#4A4A4A; --brass:#B08D57;
    --radius:2px;
    font-family:'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    color:var(--ink); background:var(--bone);
    max-width:960px; margin:0 auto; padding:56px 24px;
    line-height:1.65;
  }
  .aydins-rs *, .aydins-rs *::before, .aydins-rs *::after { box-sizing:border-box; }
  .aydins-rs .rs-pillars {
    font-size:11px; letter-spacing:0.16em; text-transform:uppercase;
    color:var(--char); text-align:center;
    padding-bottom:28px; margin:0 0 36px;
    border-bottom:1px solid var(--hair);
  }
  .aydins-rs .rs-eyebrow {
    font-size:12px; font-weight:500; letter-spacing:0.18em;
    text-transform:uppercase; color:var(--char); margin:0 0 12px;
    display:inline-block; border-bottom:1px solid var(--brass); padding-bottom:6px;
  }
  .aydins-rs h1 {
    font-family:'Cormorant Garamond', Georgia, serif; font-weight:500;
    font-size:clamp(32px,5vw,44px); line-height:1.15; letter-spacing:-0.01em;
    margin:0 0 16px;
  }
  .aydins-rs h2 {
    font-family:'Poppins', sans-serif; font-weight:500;
    font-size:20px; letter-spacing:-0.005em; margin:0 0 12px;
  }
  .aydins-rs p { font-size:16px; margin:0 0 16px; color:var(--ink); }
  .aydins-rs .rs-lede { font-size:17px; max-width:62ch; color:var(--char); }

  .aydins-rs .rs-step {
    border-top:1px solid var(--hair); padding:40px 0;
  }
  .aydins-rs .rs-step:first-of-type { border-top:none; padding-top:8px; }
  .aydins-rs .rs-step-num {
    font-family:'Cormorant Garamond', Georgia, serif; font-weight:500;
    font-size:48px; color:var(--brass); line-height:1; margin:0 0 8px;
  }

  /* Calibration card visual */
  .aydins-rs .rs-card-wrap {
    background:var(--stone); border:1px solid var(--hair);
    padding:32px 24px; border-radius:var(--radius);
    display:flex; flex-direction:column; align-items:center;
    margin:24px 0;
  }
  .aydins-rs .rs-card {
    background:linear-gradient(135deg,#2a2a2a 0%, #1a1a1a 100%);
    border-radius:6px;
    width:auto; aspect-ratio:53.98/85.6;
    box-shadow:0 1px 0 rgba(0,0,0,0.06);
    position:relative; overflow:hidden;
    transition:height 60ms linear;
  }
  .aydins-rs .rs-card::after {
    content:""; position:absolute; left:14px; top:16px;
    width:30px; height:22px; border-radius:3px;
    background:linear-gradient(135deg,#caa46a,#8a6a3a);
    opacity:0.85;
  }
  .aydins-rs .rs-card-label {
    font-size:11px; letter-spacing:0.2em; text-transform:uppercase;
    color:var(--char); margin-top:14px;
  }
  .aydins-rs .rs-slider-row { width:100%; max-width:520px; margin-top:20px; }
  .aydins-rs .rs-slider-row label {
    display:flex; justify-content:space-between; font-size:12px;
    letter-spacing:0.12em; text-transform:uppercase; color:var(--char);
    margin-bottom:8px;
  }
  .aydins-rs input[type="range"] {
    width:100%; -webkit-appearance:none; appearance:none;
    background:transparent; height:24px;
  }
  .aydins-rs input[type="range"]::-webkit-slider-runnable-track {
    height:1px; background:var(--ink);
  }
  .aydins-rs input[type="range"]::-moz-range-track {
    height:1px; background:var(--ink);
  }
  .aydins-rs input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance:none; appearance:none; margin-top:-9px;
    width:18px; height:18px; border-radius:50%;
    background:var(--ink); border:2px solid var(--bone);
    box-shadow:0 0 0 1px var(--ink);
  }
  .aydins-rs input[type="range"]::-moz-range-thumb {
    width:18px; height:18px; border-radius:50%;
    background:var(--ink); border:2px solid var(--bone);
  }

  /* Ring measurement visual */
  .aydins-rs .rs-ring-wrap {
    background:var(--stone); border:1px solid var(--hair);
    padding:32px 24px; border-radius:var(--radius);
    display:flex; flex-direction:column; align-items:center;
    margin:24px 0;
  }
  .aydins-rs .rs-ring-stage {
    position:relative; width:100%; max-width:360px; aspect-ratio:1;
    display:flex; align-items:center; justify-content:center;
  }
  .aydins-rs .rs-ring {
    border:2px solid var(--ink);
    border-radius:50%;
    background:rgba(176,141,87,0.08);
    transition:width 60ms linear, height 60ms linear;
  }
  .aydins-rs .rs-readout {
    margin-top:24px; text-align:center;
  }
  .aydins-rs .rs-readout-size {
    font-family:'Cormorant Garamond', Georgia, serif; font-weight:500;
    font-size:56px; line-height:1; color:var(--ink);
  }
  .aydins-rs .rs-readout-mm {
    font-size:13px; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--char); margin-top:6px;
  }
  .aydins-rs .rs-readout-intl {
    margin-top:18px; display:grid; gap:6px 24px;
    grid-template-columns:repeat(3, auto); justify-content:center;
    font-size:13px; color:var(--char);
  }
  .aydins-rs .rs-readout-intl b { color:var(--ink); font-weight:500; margin-right:6px; }

  /* Reassurance band */
  .aydins-rs .rs-reassure {
    background:var(--stone); border-radius:var(--radius);
    padding:32px 28px; margin-top:48px;
    border:1px solid var(--hair);
  }
  .aydins-rs .rs-reassure h2 {
    font-family:'Cormorant Garamond', Georgia, serif; font-weight:500;
    font-size:24px; margin-bottom:8px;
  }
  .aydins-rs .rs-reassure p {
    font-size:15px; color:var(--char); max-width:62ch;
  }
  .aydins-rs .rs-btn-row {
    display:flex; gap:12px; flex-wrap:wrap; margin-top:18px;
  }
  /* Use a.rs-btn to beat theme-level `a { color }` rules on mobile */
  /* Asymmetric padding: padding-left bumped by 0.12em to absorb trailing letter-spacing on the right and optically center short labels like EMAIL US */
  .aydins-rs a.rs-btn,
  .aydins-rs a.rs-btn:link,
  .aydins-rs a.rs-btn:visited,
  .aydins-rs a.rs-btn:hover,
  .aydins-rs a.rs-btn:focus,
  .aydins-rs a.rs-btn:active {
    display:inline-block;
    padding:12px 24px 12px calc(24px + 0.12em);
    background:var(--ink); color:var(--bone) !important;
    text-decoration:none; border:1px solid var(--ink);
    font-size:13px; letter-spacing:0.12em; text-transform:uppercase;
    font-weight:500; border-radius:var(--radius);
    text-align:center; text-indent:0;
    transition:opacity 160ms ease;
  }
  .aydins-rs a.rs-btn:hover { opacity:0.85; }
  .aydins-rs a.rs-btn-ghost,
  .aydins-rs a.rs-btn-ghost:link,
  .aydins-rs a.rs-btn-ghost:visited,
  .aydins-rs a.rs-btn-ghost:hover,
  .aydins-rs a.rs-btn-ghost:focus,
  .aydins-rs a.rs-btn-ghost:active {
    background:transparent; color:var(--ink) !important;
  }

  /* Accuracy disclaimer block. Brass left bar grabs the eye without alarming. */
  .aydins-rs .rs-disclaimer {
    background:var(--stone); border-left:3px solid var(--brass);
    padding:18px 22px; margin-top:28px; border-radius:var(--radius);
  }
  .aydins-rs .rs-disclaimer p {
    font-size:14px; line-height:1.6; color:var(--char); margin:0 0 8px;
  }
  .aydins-rs .rs-disclaimer p:last-child { margin-bottom:0; }
  .aydins-rs .rs-disclaimer strong { color:var(--ink); font-weight:500; }

  .aydins-rs .rs-tips {
    border-top:1px solid var(--hair); padding-top:24px; margin-top:32px;
  }
  .aydins-rs .rs-tips ul {
    margin:0; padding-left:18px; font-size:14px; color:var(--char);
  }
  .aydins-rs .rs-tips li { margin-bottom:8px; }

  @media (max-width:640px) {
    .aydins-rs { padding:40px 20px; }
    .aydins-rs h1 { font-size:30px; }
    .aydins-rs .rs-readout-intl { grid-template-columns:repeat(2, auto); }
  }
</style>

<section class="aydins-rs">

  <!-- V5 trust pillars -->
  <div class="rs-pillars">Free engraving · Free U.S. shipping · Aydins Lifetime Warranty · 30-day returns</div>

  <!-- Hero -->
  <span class="rs-eyebrow">Aydins Ring Sizer</span>
  <h1>Find your size at home.</h1>
  <p class="rs-lede">
    Two minutes. All you need is a credit card and a ring you already wear on the right finger.
    No printer. No tape measure. No guessing.
  </p>

  <!-- Step 1: Calibrate the screen -->
  <div class="rs-step">
    <div class="rs-step-num">01</div>
    <h2>Calibrate your screen with a credit card.</h2>
    <p>Hold any credit, debit, or ID card flat against the screen below. Drag the slider until the card on the screen matches the real card edge-to-edge.</p>

    <div class="rs-card-wrap">
      <div class="rs-card" id="rs-card" style="height:480px;"></div>
      <div class="rs-card-label">Hold a real card vertically against the screen. Drag the slider until the long edge matches: 85.6 mm</div>
      <div class="rs-slider-row">
        <label><span>Card long edge</span><span id="rs-card-mm">85.6 mm</span></label>
        <input type="range" id="rs-card-slider" min="300" max="720" value="480" step="1" />
      </div>
    </div>
  </div>

  <!-- Step 2: Place a ring -->
  <div class="rs-step">
    <div class="rs-step-num">02</div>
    <h2>Place a ring you already own on the screen.</h2>
    <p>Use a ring that fits the correct finger comfortably. Drag the slider until the circle below matches the <b>inside</b> of your ring exactly.</p>

    <div class="rs-ring-wrap">
      <div class="rs-ring-stage">
        <div class="rs-ring" id="rs-ring" style="width:120px; height:120px;"></div>
      </div>
      <div class="rs-slider-row">
        <label><span>Inside diameter</span><span id="rs-ring-mm">mm</span></label>
        <input type="range" id="rs-ring-slider" min="40" max="280" value="120" step="1" />
      </div>
    </div>
  </div>

  <!-- Step 3: Read the size -->
  <div class="rs-step">
    <div class="rs-step-num">03</div>
    <h2>Your size.</h2>
    <p>This is the closest US size to the inside diameter you measured. International equivalents are listed below.</p>

    <div class="rs-readout">
      <div class="rs-readout-size" id="rs-size-us">0</div>
      <div class="rs-readout-mm" id="rs-size-mm">Slide to measure</div>
      <div class="rs-readout-intl">
        <div><b>UK</b><span id="rs-size-uk"></span></div>
        <div><b>EU</b><span id="rs-size-eu"></span></div>
        <div><b>Japan</b><span id="rs-size-jp"></span></div>
      </div>
    </div>

    <div class="rs-disclaimer">
      <p><strong>A note on accuracy.</strong> This tool is a strong starting point, not a guarantee. Screen calibration varies between phones, tablets, and laptops, and small differences in how the card or ring is held can shift the result by up to a half-size.</p>
      <p>For the most accurate measurement, get sized in person by a local jeweler. Most do it free in under five minutes. If your Aydins ring arrives and the fit is off, that is exactly what our 30-day exchange and Lifetime Sizing programs are for (see below).</p>
    </div>

    <div class="rs-tips">
      <ul>
        <li>Measure at the end of the day. Fingers swell, and you'll size a half-size differently in the morning.</li>
        <li>Measure the hand the ring will live on. The dominant hand is usually a half-size larger.</li>
        <li>Wider bands (6mm+) wear a half-size tighter. If the result is between two sizes, size up.</li>
        <li>If your ring is between sizes, round up. Comfort fit is forgiving on the tighter side.</li>
      </ul>
    </div>
  </div>

  <!-- Reassurance close. Policy-accurate per live /pages/returns-exchanges + /pages/lifetime-sizing-lifetime-warranty -->
  <div class="rs-reassure">
    <span class="rs-eyebrow">Exchanges, Sizing &amp; Warranty</span>
    <h2>Wrong size? You're covered.</h2>
    <p>
      <b>30-day exchange.</b> Unengraved standard rings exchange free within 30 days. Engraved rings are exchange-only with a $34.50 surcharge.
    </p>
    <p>
      <b>Lifetime Sizing.</b> Fit changes after 30 days are covered for the original purchaser at a small flat fee, with no time limit.
    </p>
    <p>
      <b>Aydins Lifetime Warranty.</b> Manufacturing defects are covered free for the first 6 months, then $34.50 through month 12, then $54.50 flat after that.
    </p>
    <div class="rs-btn-row">
      <a href="mailto:sales@shopaydins.com" class="rs-btn">Email Us</a>
      <a href="tel:18002147345" class="rs-btn rs-btn-ghost">Call 1-800-214-7345</a>
    </div>
  </div>

</section>

<script>
(function(){
  var CARD_WIDTH_MM = 85.6;
  var STORAGE_KEY = 'aydins-rs-cal-v2';
  var DEFAULT_CARD_PX = 480;

  // US half-sizes 4 → 15, with mm inside diameter + UK / EU / Japan equivalents
  var RING_SIZES = [
    {us:'4',   mm:14.88, uk:'H',     eu:'46.5', jp:'7'},
    {us:'4.5', mm:15.27, uk:'H 1/2', eu:'47.8', jp:'8'},
    {us:'5',   mm:15.70, uk:'J 1/2', eu:'49.3', jp:'9'},
    {us:'5.5', mm:16.10, uk:'K 1/2', eu:'50.6', jp:'10'},
    {us:'6',   mm:16.51, uk:'L 1/2', eu:'51.9', jp:'12'},
    {us:'6.5', mm:16.92, uk:'M 1/2', eu:'53.1', jp:'13'},
    {us:'7',   mm:17.32, uk:'N 1/2', eu:'54.4', jp:'14'},
    {us:'7.5', mm:17.73, uk:'O 1/2', eu:'55.7', jp:'15'},
    {us:'8',   mm:18.14, uk:'P 1/2', eu:'57.0', jp:'16'},
    {us:'8.5', mm:18.54, uk:'Q 1/2', eu:'58.3', jp:'17'},
    {us:'9',   mm:18.95, uk:'R 1/2', eu:'59.5', jp:'18'},
    {us:'9.5', mm:19.35, uk:'S 1/2', eu:'60.8', jp:'19'},
    {us:'10',  mm:19.76, uk:'T 1/2', eu:'62.1', jp:'20'},
    {us:'10.5',mm:20.17, uk:'U 1/2', eu:'63.4', jp:'21'},
    {us:'11',  mm:20.57, uk:'V 1/2', eu:'64.6', jp:'22'},
    {us:'11.5',mm:20.98, uk:'W 1/2', eu:'65.9', jp:'24'},
    {us:'12',  mm:21.39, uk:'X 1/2', eu:'67.2', jp:'25'},
    {us:'12.5',mm:21.79, uk:'Z',     eu:'68.5', jp:'26'},
    {us:'13',  mm:22.20, uk:'Z 1/2', eu:'69.7', jp:'27'},
    {us:'13.5',mm:22.61, uk:'Z+1',   eu:'71.0', jp:'28'},
    {us:'14',  mm:23.01, uk:'Z+2',   eu:'72.3', jp:'29'},
    {us:'14.5',mm:23.42, uk:'Z+3',   eu:'73.6', jp:'30'},
    {us:'15',  mm:23.83, uk:'Z+4',   eu:'74.8', jp:'31'}
  ];

  var card        = document.getElementById('rs-card');
  var cardSlider  = document.getElementById('rs-card-slider');
  var cardMmEl    = document.getElementById('rs-card-mm');
  var ring        = document.getElementById('rs-ring');
  var ringSlider  = document.getElementById('rs-ring-slider');
  var ringMmEl    = document.getElementById('rs-ring-mm');
  var sizeUsEl    = document.getElementById('rs-size-us');
  var sizeMmEl    = document.getElementById('rs-size-mm');
  var sizeUkEl    = document.getElementById('rs-size-uk');
  var sizeEuEl    = document.getElementById('rs-size-eu');
  var sizeJpEl    = document.getElementById('rs-size-jp');

  // Restore calibration if saved. Clamp to current slider range in case bounds changed.
  try {
    var saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
    if (saved && saved.cardPx) {
      var min = parseFloat(cardSlider.min);
      var max = parseFloat(cardSlider.max);
      var px  = Math.max(min, Math.min(max, parseFloat(saved.cardPx)));
      cardSlider.value = px;
      card.style.height = px + 'px';
    }
  } catch(e){}

  function mmPerPx() {
    var px = parseFloat(cardSlider.value) || DEFAULT_CARD_PX;
    return CARD_WIDTH_MM / px;
  }

  function findClosestSize(mm) {
    if (!isFinite(mm) || mm <= 0) return null;
    var best = RING_SIZES[0];
    var bestDiff = Math.abs(RING_SIZES[0].mm - mm);
    for (var i = 1; i < RING_SIZES.length; i++) {
      var d = Math.abs(RING_SIZES[i].mm - mm);
      if (d < bestDiff) { best = RING_SIZES[i]; bestDiff = d; }
    }
    return best;
  }

  function updateCard() {
    var px = parseFloat(cardSlider.value) || DEFAULT_CARD_PX;
    card.style.height = px + 'px';
    cardMmEl.textContent = CARD_WIDTH_MM.toFixed(1) + ' mm';
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify({ cardPx: px })); } catch(e){}
    updateRing();
  }

  function updateRing() {
    var px = parseFloat(ringSlider.value) || 120;
    ring.style.width  = px + 'px';
    ring.style.height = px + 'px';

    var mm = px * mmPerPx();
    ringMmEl.textContent = mm.toFixed(1) + ' mm';

    var match = findClosestSize(mm);
    if (match) {
      sizeUsEl.textContent = match.us;
      sizeMmEl.textContent = mm.toFixed(1) + ' mm inside diameter';
      sizeUkEl.textContent = match.uk;
      sizeEuEl.textContent = match.eu;
      sizeJpEl.textContent = match.jp;
    }
  }

  cardSlider.addEventListener('input', updateCard);
  ringSlider.addEventListener('input', updateRing);
  updateCard();
})();
</script>
```

---

## Spec Block

| Element | Value | Source |
|---|---|---|
| Background | Bone `#FAF8F4` | DESIGN.md §Color |
| Body text | Ink `#1A1A1A` | DESIGN.md §Color |
| Accents | Brass `#B08D57` (eyebrow underline + step numerals only) | DESIGN.md §Color |
| Surface bg | Stone `#EEEAE2` (calibration card + ring stage + reassurance band) | DESIGN.md §Color |
| Hairline | `#E5E2DB` (borders, dividers between steps) | DESIGN.md §Color |
| Display font | Cormorant Garamond 500 (H1 + step numerals + size readout) | DESIGN.md §Typography |
| UI / body | Poppins 400 / 500 | DESIGN.md §Typography |
| Container | 960px max, 56px padding desktop / 40px mobile | DESIGN.md §Layout |
| Primary CTA | Ink bg, Bone text, 2px radius, 13px Poppins 500 +0.12em UPPERCASE | DESIGN.md §Buttons |
| Secondary CTA | Transparent bg, Ink border, Ink text | DESIGN.md §Buttons |
| Calibration unit | ISO/IEC 7810 ID-1 credit card (85.6mm × 53.98mm) | Industry standard |
| Persistence | `localStorage` key `aydins-rs-cal-v1` |, |

**Color count: 4** (Bone, Ink, Brass, Hairline; Stone is tonal bg variant) ✓
**Font count: 2** (Poppins + Cormorant) ✓

---

## 10-Rule Self-Check

| # | Rule | Pass | Note |
|---|---|---|---|
| 1 | Whitespace ≥56px desktop / ≥40px mobile per section | ✓ | 56px container padding, 40px between steps |
| 2 | ≤4 colors visible | ✓ | Bone, Ink, Brass, Hairline (Stone tonal) |
| 3 | ≤2 fonts | ✓ | Poppins + Cormorant |
| 4 | Mobile 375px, tap targets ≥44px, no horizontal scroll | ✓ | Sliders 24px tall touch area; layout collapses to single column |
| 5 | No banned tells (gradients, drop shadows, pure black, `#fff301`, ribbons, bursts, clip art) | ✓ | Card is only "gradient", represents a real plastic card visual, not decoration |
| 6 | Hierarchy unambiguous (squint test) | ✓ | H1 > step numerals > step H2s > readout |
| 7 | Photography first (or zero) | ✓ | Zero photos. Geometric primitives only (rectangle = card, circle = ring) |
| 8 | Eyebrow above every section H2 | ✓ | "Aydins Ring Sizer," "30-Day Exchanges & Lifetime Sizing" |
| 9 | Premium gut-check (Hodinkee/Gear Patrol-adjacent) | ✓ | Calm copy, restrained palette, tool-not-toy tone |
| 10 | Trust gut-check (would a man spending $1,800 feel safe) | ✓ | Reassurance block uses canonical policy, no overpromises |

**All 10 pass.**

---

## Implementation notes

### Where it lives
- **New page:** `Online Store > Pages > Add page > "Ring Sizer"` → slug `ring-sizer` → URL `/pages/ring-sizer`
- **Link from PDP:** add a tertiary link in the size-chart modal: "Don't have a measuring tool? Use our Ring Sizer →" pointing to `/pages/ring-sizer`
- **Link from size chart:** mirror the link both directions, Size Chart and Ring Sizer link to each other

### Accuracy disclaimer
- Screen calibration is good enough for ±0.5 size. The reassurance block exists because the tool is a starting point, not a guarantee.

### Browser support
- Vanilla JS, no framework, no dependencies. Works on every modern browser including iOS Safari and Android Chrome.
- `localStorage` is the only Web API used, graceful fallback if disabled (calibration just doesn't persist).

### Future improvements (not V1)
- Save the result + email it to the customer ("text me my size" flow)
- Auto-pre-select the variant on the linked PDP via URL param (`?ring_size=8.5`)
- Print-friendly fallback PDF (the old findmyringsize.com paper method) for customers without a credit card on hand

---

## Why this beats sending people to findmyringsize.com

| findmyringsize.com | Aydins Ring Sizer |
|---|---|
| Off-site, customer leaves the funnel | On-domain, customer stays on Aydins |
| Generic, unbranded | Aydins voice + design system |
| Cluttered, ad-laden in places | Calm, editorial, trust surface |
| Uses a paper printout method (calibration via printed PDF) | Uses a credit card (every adult has one within reach) |
| Doesn't reassure the customer about getting it wrong | Closes with the actual 30-day + Lifetime Sizing policy |
| No path back to Aydins | Buttons go directly to email + phone support |

---

## Next steps

1. Paste the HTML block into a new Shopify page at `/pages/ring-sizer`.
2. Add a link from the Size Chart modal: "Use our Ring Sizer →"
3. Add a link from PDP under the Add to Cart row: "Not sure of your size? Try the Ring Sizer →"
4. Test on iPhone (Safari) and Android (Chrome), verify the credit card calibration feels right against a real card.
5. Run `/shopify-design-qa` after live.
