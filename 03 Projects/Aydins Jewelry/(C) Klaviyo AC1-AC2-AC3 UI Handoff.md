# (C) Klaviyo AC1 / AC2 / AC3 — UI Handoff

> **Why this doc exists:** Klaviyo's API doesn't allow PATCH on flow-message subject/preview, and the AC templates are SYSTEM_DRAGGABLE (drag-and-drop) which the API also doesn't allow direct HTML edits on. So these 3 fixes have to be done in the Klaviyo UI by hand. This doc gives you the exact paste-ready copy and a click-by-click path.
>
> **Total time: ~15 min for all 3.** Stops the false-claim leak going to live customers right now.
>
> **Source of truth for every claim below:** [[(C) Aydins Policies — Source of Truth]]

---

## How to navigate to each email

1. Klaviyo → **Flows** (left nav)
2. Open flow **"Abandoned Cart"** (ID: `TrNjjf`)
3. For each email below: click the email block on the canvas → **"Edit Email"** in the right panel

You'll edit each email in this order: AC1 → AC2 → AC3.

---

## The Locked Trust Block (use this exactly, in all 3 emails)

This is the one paragraph that goes into all 3 emails. Don't paraphrase. Don't break it up. Don't add a Lifetime Warranty bullet outside of this paragraph.

> Free engraving. Free U.S. shipping. Free exchange in the first 30 days. Lifetime Warranty against breaks and defects — free for 6 months, then $34.50, then $54.50 flat. Lifetime Sizing if your finger ever changes — for a small flat fee, no time limit. We've been doing this since 2011, out of our Dallas-area workshop.

**Paste-ready text-block version (drop into a Klaviyo Text block, no styling needed):**

```
Free engraving. Free U.S. shipping. Free exchange in the first 30 days. Lifetime Warranty against breaks and defects — free for 6 months, then $34.50, then $54.50 flat. Lifetime Sizing if your finger ever changes — for a small flat fee, no time limit. We've been doing this since 2011, out of our Dallas-area workshop.
```

---

# AC1 — Message ID `SQdgLg`

### 1. Subject line (top of editor, "Subject" field)

**Replace:**
> Need a gentle nudge? Enjoy 20 % off today

**With:**
```
Still thinking it over? Here's 20% off — code EMK20
```

### 2. Preview text ("Preview text" field, just under subject)

**Replace:**
> Use code EMK20 before midnight to secure your handcrafted piece.

**With:**
```
Free engraving, free U.S. shipping, free exchange in the first 30 days. Code expires at midnight.
```

### 3. Body — the FAQ section

Find the FAQ block in the body. It currently says:

> **What's your return & exchange policy?**
> Every piece comes with 30-day free returns & exchanges. If it isn't perfect, send it back and we'll resize, remake, or refund.

**Delete that Q&A entirely.** Replace it with:

> **What's your return & exchange policy?**
> Free exchange in the first 30 days on unengraved rings ($34.50 surcharge on engraved). 30-day returns are accepted with a $25 restocking fee — engraved rings can be exchanged but not returned. Lifetime Sizing for the original purchaser if your finger ever changes — small flat fee, no time limit.

**Paste-ready (mono-style for clean copy):**

```
What's your return & exchange policy?

Free exchange in the first 30 days on unengraved rings ($34.50 surcharge on engraved). 30-day returns are accepted with a $25 restocking fee — engraved rings can be exchanged but not returned. Lifetime Sizing for the original purchaser if your finger ever changes — small flat fee, no time limit.
```

### 4. Body — sizing link (if present)

Anywhere the email says **"findmyringsize.com"** or links to that external URL, change it to:

```
https://shopaydins.com/pages/find-your-ring-size
```

Display text can stay as: "Find Your Ring Size →"

---

# AC2 — Message ID `UCDagK`

### 1. Subject line

**Replace:**
> Your handcrafted jewelry is nearly ready ✨

**With:**
```
Your handcrafted ring is nearly ready
```

(Removing the sparkle emoji — Aydins design system has no emoji.)

### 2. Preview text — **THIS IS THE WORST LEAK, FIX FIRST**

**Replace (this is shipping a fabricated claim to every customer right now):**
> Finish your order today—free engraving & lifetime warranty included.

**With:**
```
A few minutes to finish, and we'll start cutting it in the workshop.
```

### 3. Body — the 3-line feature bullets

Find the block that says:

> Free laser engraving on every item
> Lifetime fit guarantee & warranty
> 2-day U.S. shipping on most orders

**Delete that whole 3-line block.** Replace it with the **Locked Trust Block** above (one paragraph, not bullets).

If the original was a bullet/icon block, switch it to a plain Text block before pasting — the Trust Block needs to read as one continuous paragraph, not as 3 separate bullets.

---

# AC3 — Message ID `UJLFPZ`

### 1. Subject line

**Replace:**
> Final reminder: we're holding your jewelry a little longer

**With:**
```
Last call — your piece is still set aside
```

### 2. Preview text

**Replace:**
> We'll release it back to the workshop at midnight—let us finish it for you.

**With:**
```
Since 2011, every Aydins ring has been made by hand. Yours is ready when you are.
```

### 3. Body — the emoji feature checklist

Find the block at the bottom that says (with emojis):

> ✅ Lifetime Warranty & Fit
> ✒️ Free Laser Engraving
> 🚚 Free 2-Day Shipping

**Delete that whole 3-line block.** Replace it with the **Locked Trust Block** above (one paragraph, no emoji).

---

## Self-check before you hit "Save"

For each of the 3 emails, confirm:

- [ ] No "lifetime warranty included" without the fee disclosure (free 6mo, $34.50, $54.50)
- [ ] No "lifetime fit guarantee"
- [ ] No "30-day free returns" (returns are NOT free — $25 restocking)
- [ ] No "we'll resize, remake, or refund" naked (Lifetime Sizing has a flat fee)
- [ ] No "2-day shipping" (carrier service-level not verified — use "Free U.S. shipping" only)
- [ ] No emoji
- [ ] No "guaranteed" attached to fit/sizing/warranty
- [ ] Sizing link points to `shopaydins.com/pages/find-your-ring-size` (not findmyringsize.com)
- [ ] Locked Trust Block is exact, not paraphrased

## What you're shipping when this is done

A 3-email abandoned-cart series that:
- Stops sending false "lifetime warranty included" / "30-day free returns" claims
- Tells the truth in a way that's actually more impressive than the lie
- Leaves the visual design intact (we didn't touch the drag-and-drop layout)
- Is consistent with what the website will say once the page-rewrites land

---

## When you're done

Reply "AC1/2/3 done" and I'll move on to:
- Welcome 1–4 UI handoff doc (same format)
- Thank You 1–2
- Browse Abandonment
- Customer Winback 1–2 (this one needs the flow paused first — I'll handle that)
- Order Confirmation + Shipping Confirmation activation

In parallel, I'm now working on the `.claude/page-rewrites/` folder — 19 files, will produce a delta audit, then rewrite all flagged sections so you can publish to shopaydins.com.
