# Tidio Chatbot Revamp. Build Guide for Aydins Jewelry

**Status:** Build Spec, Ready to Execute
**Author:** Claude
**Date:** 2026-05-18
**Estimated build time:** 60 to 90 minutes
**Skill level assumed:** Complete beginner to Tidio

---

## How to Read This Guide

Build top to bottom. Do not skip ahead. Each section depends on the one before it.

When you see **bold text in quotes** like "Click here", that is the exact button or label you will see inside Tidio.

When you see a code block like this:
```
Copy-paste this text
```
That is text you literally copy and paste into Tidio.

When you see hex codes like `#B08D57`, that is a color code. Tidio has a color picker where you paste these in.

If you get stuck, stop and ask. Do not guess.

---

## What We Are Building (Plain English)

A small set of automated chats inside Tidio that:

1. Greet people in a smart way (only when they are actually thinking about buying, not the moment they land)
2. Catch people before they leave a product page (with a discount)
3. Save abandoned carts
4. Answer the most common jewelry questions (sizing, materials, shipping)
5. Route returns directly to Thunder Returns
6. Hand off to a human when the AI is out of its depth

We are throwing out everything you built 2 years ago. Clean slate.

---

## Glossary (Tidio Terms You Will See)

- **Flow:** An automated conversation. You build one for each scenario (welcome, exit intent, cart recovery, etc.).
- **Trigger:** The condition that makes a Flow start. (Example: "visitor on product page for 45 seconds")
- **Lyro:** Tidio's built-in AI agent. It answers questions in plain language using your store info.
- **Widget:** The chat bubble in the bottom-right corner of your site.
- **Operator:** A human agent (you). Tidio uses this word for any human team member.
- **Channel:** Where messages come from (live chat, email, Instagram, WhatsApp, etc.).
- **Knowledge source:** A document or webpage you give Lyro so it knows your policies and products.
- **Escalate:** Hand the chat off from Lyro/bot to a human.

---

# PART 1: Brand Colors and Visual Setup

You have V5 brand colors already locked (decision dated 2026-05-15, see [[(C) Recart Popup Revamp — V5 Final Design]]). We are using the same palette inside Tidio so the chat widget matches your site, your popups, and your emails.

## The Aydins V5 Color Palette

| Name | Hex Code | Use it for |
|---|---|---|
| **Brass** | `#B08D57` | Primary accent. Chat bubble, header, buttons, send button |
| **Brass Dark** | `#8F7244` | Hover state (when someone hovers over the chat button) |
| **Ink** | `#1A1A1A` | All text. Logo. Icons |
| **Bone** | `#FAF8F4` | Background of the chat window |
| **Cream** | `#F2EBDC` | Light accent if you need a secondary background |
| **Muted Gray** | `#6b6b6b` | Tiny text like timestamps |
| **White** | `#FFFFFF` | Text that sits on top of brass |

**The rule:** Yellow is out of the brand entirely. If Tidio offers a default yellow or gold preset, do not use it. Always paste in `#B08D57` for brass.

## Where to Paste Each Color in Tidio

Open Tidio. Go to **Settings** in the bottom-left corner. Then click **Channels**. Then click **Live Chat**. Then click the **Appearance** tab.

The Appearance page is split into two sections: **General** (colors and logo) and **Content** (text, welcome panel, conversation starters). We will do General here, then Content in the next part.

### General → Colors

You will see exactly 3 color fields. Paste these:

| Tidio Field          | What to Paste | Hex Code  | Notes                                                                |
| -------------------- | ------------- | --------- | -------------------------------------------------------------------- |
| **Background color** | Bone          | `#FAF8F4` | Already set correctly in your account.                               |
| **Text color**       | Ink           | `#1A1A1A` | Black is close enough. If a custom hex field exists, use `#1A1A1A`.  |
| **Action color**     | Brass         | `#B08D57` | **CURRENTLY SET TO BLUE. CHANGE THIS.** This colors every button, link, conversation starter accent, and the send arrow. Single most important color to fix. |

### General → Brand logo

Tidio shows: "Custom branding is available on the Plus plan. Contact us to enable this feature."

**Translation:** You cannot replace the "Powered by Tidio" footer or upload a custom widget logo at this tier. **Skip this section entirely.** We will swap your logo using the Welcome Image field in the Content section instead (next part of the guide). That field is available on every plan.

## Appearance → Content (The Welcome Panel)

Still on the **Appearance** page. Scroll down to the **Content** section. You will see 4 tabs: **Home**, **Chat**, **Pre-chat survey**, **Minimized**. We are going to fix all 4.

### Tab 1: Home (The First Thing Visitors See)

This is the panel that opens when someone clicks the chat bubble. Currently yours shows a generic "Hi there 👋" and weak conversation starters.

**Welcome image:**
- Select **"Your logo"** (you already have this selected).
- Click **Upload logo** and replace the current logo (the one with the yellow triangle) with the ink wordmark from your vault: `08 Brand Assets/Logo - Claw 2026-05-15/aydins-wordmark-transparent.png`
- If Tidio rejects the PNG, try the SVG version in the same folder.
- **Critical:** Yellow is out of the brand (locked 2026-05-15). Your current logo violates that. Swap it now.

**Header field:** Replace `Hi there 👋` with:

```
Need a hand?
```

Why: Emoji breaks the persona ("no emojis unless the customer uses them first"). "Need a hand?" is direct, on-brand, and assumes the visitor has a real question (which they do, otherwise they would not click).

**Message field:** Replace `The Aydins Jewelry team is ready to answer any questions you might have.` with:

```
Sizing, materials, gift help, order updates. Real answers, fast.
```

Why: Lists the specific things people actually ask about. Sets expectations. "Real answers, fast" promises something the chat will deliver.

**Conversation starters (the clickable suggested questions):**

Turn OFF all 5 current starters. Replace with these 4 (toggle ON, type each one):

```
What ring size am I?
```
```
Is this real gold or silver?
```
```
Where is my order?
```
```
Help me pick a gift
```

Order matters. Sizing is question #1 in jewelry, put it first. Gift help is seasonal gold (especially Nov-Dec, Valentine's, Mother's Day). "Where is my order" deflects support volume to Lyro. "Is this real gold" addresses the trust question every first-time buyer has but few will ask out loud.

**Why these 4 and not more:** Decision fatigue. 5+ options = nobody picks. 4 max.

**Online status:** Keep `We typically reply in a few minutes` (your current one is fine).

**Offline status:** Replace `Got a Question?` with:

```
We're closed. Leave your email and we'll reply within 24 hrs.
```

### Tab 2: Chat

This is the in-chat experience after the visitor starts typing. Most of this is controlled by your Flows and Lyro. Default settings are fine. Skip unless you spot something off-brand.

### Tab 3: Pre-chat survey

A short form Tidio shows before connecting a visitor to a live agent (asks for name + email).

**Recommendation: Turn this ON.** Reasoning:
- Captures the visitor's email even if the conversation goes nowhere = lead capture
- Gives you context before you reply
- Reduces "ghost chats" where someone messages and disappears

**Fields to require:**
- Name (required)
- Email (required)
- "What can we help with?" (optional, single line)

**Survey intro text:**
```
Real quick. Drop your name and email so we can follow up if we get disconnected.
```

### Tab 4: Minimized

This is the chat bubble itself (the floating brass circle in the bottom-right corner).

**Settings:**
- Position: bottom right
- Size: medium (default)
- Show notification badge: ON (the small red dot that signals "new message")
- Greeting bubble preview: OFF (we do not want a tooltip popping up uninvited, Flows handle invitations)

## Operator Avatar

For your human agent profile (the one that shows when you reply personally):

1. Go to **Settings** → **My Account** → **Profile**.
2. Upload a real photo of yourself or use the Aydins logo claw mark.
3. Set display name to your first name only ("Amir") not "Customer Support". Personal feels real, corporate feels like a bot.

## Typography

Tidio uses its own system fonts inside the chat window. You cannot change them to Cormorant or Poppins. That is fine. Keep your brand fonts for the website, let Tidio use its defaults inside the widget.

---

# PART 2: Widget Configuration (When the Chat Bubble Appears)

Still inside **Settings** → **Channels** → **Live Chat**.

## Visibility (Where the Chat Shows Up)

Go to the **Visibility** or **Display settings** tab.

**HIDE the widget on these pages:**
- `/checkout`
- `/checkouts/*` (Shopify uses this URL for checkout steps)
- `/cart`
- `/account/login`
- `/account/register`

**Why:** Chat on checkout pulls people out of buying. Chat on cart fights with our Cart Recovery flow. Hide it everywhere it could hurt conversion.

**SHOW the widget on:**
- Homepage
- All product pages (`/products/*`)
- All collection pages (`/collections/*`)
- Blog posts
- Policy pages

## Auto-Open Settings

Find the toggle that says something like **"Open widget automatically"** or **"Auto-invite"**.

**Turn this OFF.**

Our Flows will decide when to invite people to chat. We do not want the widget popping open on its own.

## Operating Hours

Go to **Settings** → **Operating hours**.

Set the hours when you are actually available to respond. Example:
- Monday-Friday: 9am to 6pm EST
- Saturday: 10am to 4pm EST
- Sunday: Closed

**Outside operating hours:** Tidio will show "We're offline" message. Set the offline message to:

```
We're closed right now. Our AI assistant can help with sizing, returns, and order status 24/7. For anything else, drop your email and we'll reply within 24 hours.
```

---

# PART 3: Lyro AI Setup (Do This BEFORE Building Flows)

**Why first:** Several of our Flows hand the conversation off to Lyro. If Lyro is not set up, those Flows break.

## Step 1: Activate Lyro

Go to **Automation** in the left sidebar. Click **Lyro AI**. Turn it on.

(Note: Lyro is a paid add-on. Free tier gets 50 AI conversations to test, then it costs around $32.50/mo for 50 conversations. Decide if this is in budget before activating. If not, skip Lyro entirely and use rule-based Flows only. The Flows below will still work, you just lose the smart Q&A on order status and free-form questions.)

## Step 2: Feed Lyro Your Knowledge

In Lyro settings, find **"Knowledge sources"** or **"Train Lyro"**.

Add these URLs from your Shopify store (if a page does not exist, create it first):

1. Shipping policy page
2. Return and exchange policy page (must mention Thunder Returns)
3. Ring sizing guide
4. Materials guide (what is solid gold vs plated, sterling silver, etc.)
5. Jewelry care guide (use [[(C) Ring Care Guide — Shopify Page Content]])
6. FAQ page
7. About / Our Story page

**Cross-reference your source of truth:** Open [[(C) Aydins Policies — Source of Truth]] and make sure your shipping, returns, and sizing policies on the live site match what is in that doc. If they do not match, fix the live site first, then point Lyro at it. Otherwise Lyro will give wrong answers.

## Step 3: Lyro Persona Prompt

In Lyro settings, find **"AI personality"** or **"Custom instructions"**. Paste this:

```
You are the jewelry expert for Aydins Jewelry, a family-run jewelry store since 2011. Be warm, direct, and helpful. Keep answers to 2-3 sentences max.

Never invent prices. Never promise discounts. Never confirm specific stock levels.
Never claim a piece is "the most popular" or "best seller" unless told.

Speak like a knowledgeable friend at a jewelry counter, not a corporate bot.
Do not use emojis unless the customer uses them first.
Do not use the dash character. Use periods, commas, or parentheses instead.

If the customer asks about ring sizing, walk them through measuring or recommend our free 60-day resize.
If the customer asks about a specific past order, ask for their order number and email.
If you do not know an answer with high confidence, hand off to a human.
```

## Step 4: Hard Routing Rules (When Lyro Must Hand Off)

In Lyro settings, find **"Escalation rules"** or **"Hand off to human when"**.

Set Lyro to escalate to a human for any of these:

- Custom orders or custom design requests
- Questions about whether a specific piece is real gold, real diamond, or solid silver
- Price negotiation or "best price" requests
- Lost, missing, or damaged orders
- Complaints, refund disputes, or angry tone
- Any specific past order question after 1 failed lookup attempt
- Anything Lyro cannot answer with confidence

---

# PART 4: The 6 Flows

Build these in the order listed. Each one has:

- **Name** (what to call it inside Tidio)
- **Trigger** (when it fires)
- **Messages and buttons** (exact text to paste)

To create a flow: **Automation** → **Flows** → **+ New flow** → **Start from scratch**.

---

## Flow 1: Smart Welcome on Product Pages

**Name:** PDP Welcome 45s

**Trigger:**
- Visitor is on a page where URL contains `/products/`
- Time on page: 45 seconds
- Visitor has not interacted with chat in this session

**How to set this trigger in Tidio:**
1. Click **"+ Add trigger"**
2. Pick **"Time on site"** or **"Visited page"**
3. Set URL contains: `/products/`
4. Set time: 45 seconds
5. Add condition: **"Has not started a chat in this session"**

**Bot message 1:**
```
Hey, noticed you've been looking at this piece. Anything I can help with?
```

**Add 4 buttons under the message:**

**Button 1: "Ring sizing"**
→ When clicked, jump to **Flow 4: Ring Sizing Helper** (we will build this next).

**Button 2: "Is this real gold/silver?"**
→ Bot reply:
```
Yes. Every piece is solid metal as described on the product page, no plating. Want me to confirm the exact karat for this specific item?
```
→ Add 1 button below: **"Talk to a human"** → routes to operator.

**Button 3: "Shipping and returns"**
→ Bot reply:
```
Free US shipping on orders $75+. Easy 60-day returns and free resizing on rings. Want the full policy?
```
→ Add 1 button: **"Yes, send the link"** → bot sends URL of your shipping/returns page.

**Button 4: "Just browsing"**
→ Bot reply:
```
All good. I'm here if you need me.
```
→ End flow.

**Save and turn ON.**

---

## Flow 2: Exit Intent Discount on Product Pages

**Name:** PDP Exit 10% Save

**Trigger:**
- Exit intent detected (mouse moves toward closing the tab)
- URL contains `/products/`
- Visitor has been on the site 30+ seconds
- Fires maximum 1 time per visitor (set this so it does not nag)

**How to set in Tidio:**
1. Trigger type: **"Exit intent"**
2. URL contains: `/products/`
3. Frequency: **Once per visitor**

**Bot message:**
```
Wait. Before you go, here's 10% off this piece. Code STAY10 at checkout. Good for 24 hours.
```

**Buttons:**
- **"Copy code"** → bot replies: `Code copied. STAY10. Hope to see you back.`
- **"Not interested"** → end flow.

**IMPORTANT CHECK BEFORE TURNING THIS ON:**
You already have Recart popups doing email capture with a discount (see [[(C) Recart Popup Revamp — V5 Spec]]). Running this Tidio exit popup AND a Recart popup on the same page = two popups firing on top of each other = zero conversions and an angry visitor.

**Decision rule:**
- If Recart is the active exit popup on product pages → leave this Tidio Flow 2 OFF.
- If Recart only fires on homepage/collections and product pages are open → turn this ON.

Confirm which is true by visiting a product page in incognito and triggering exit intent yourself.

---

## Flow 3: Cart Recovery

**Name:** Cart Idle 60s

**Trigger:**
- Visitor is on `/cart` for 60+ seconds
- Has 1+ items in cart
- Has not clicked the checkout button

**Wait:** Earlier we hid the widget on `/cart`. For this Flow to work, the widget must show up on cart. Adjust the **Visibility** rule in Part 2 to allow `/cart` but still block `/checkout` and `/checkouts/*`. (Checkout is where conversion lives, do not interrupt that. Cart is where people stall, that is where we want to help.)

**Bot message:**
```
You've got something good in your cart. Any question before checkout, or want a hand?
```

**Buttons:**

**Button 1: "Sizing question"**
→ Jump to Flow 4 (Ring Sizing).

**Button 2: "Shipping speed?"**
→ Bot reply:
```
Standard ships in 1-3 business days. Need it faster? Express options at checkout.
```

**Button 3: "10% off if I order now?"**
→ Bot reply:
```
Use code STAY10 at checkout. Good for the next 10 minutes.
```

**Button 4: "I'm good"**
→ End flow.

---

## Flow 4: Ring Sizing Helper

**Name:** Ring Sizing Guide

**Trigger (two ways to start this flow):**
1. Visitor clicks a "Ring sizing" button from another flow
2. Visitor types keywords: `size`, `sizing`, `fit`, `what size`, `ring size`

**How to add keyword triggers:**
- Trigger type: **"Visitor sends message"**
- Message contains: any of the keywords above (Tidio lets you list multiple).

**Bot message:**
```
Sizing is the #1 thing people ask. Where are you at?
```

**Buttons:**

**Button 1: "I know my size"**
→ Bot reply:
```
Perfect, you're set. Add to cart and you're done.
```
→ End flow.

**Button 2: "I need to measure"**
→ Bot reply:
```
Easiest way: wrap a string around the base of your finger, mark where it overlaps, measure that length in mm. Most common sizes are 6-7 for women, 9-10 for men. Full guide here:
```
→ Send link to your sizing guide page.

**Button 3: "It's a surprise gift"**
→ Bot reply:
```
Smart move. Two options: (1) Pick most common (size 6 for women, size 10 for men). (2) We offer free resizing within 60 days, so you're covered either way. Want me to flag your order as a gift?
```
→ Buttons below:
- **"Yes, flag it"** → routes to operator with note: "Customer requested gift flag on upcoming order"
- **"Got it, thanks"** → end flow

**Button 4: "Talk to a human"**
→ Routes to operator.

---

## Flow 5: Order Status Lookup

**Name:** Order Status Lookup

**Trigger:**
- Visitor types keywords: `where's my order`, `tracking`, `shipping update`, `when will it arrive`, `order status`, `track`

**Bot logic:**

This flow leans heavily on Lyro. If you activated Lyro in Part 3, route this flow to Lyro and let it ask for the order number and email, then pull from Shopify.

**If you did NOT activate Lyro**, build this manually:

**Bot message:**
```
Happy to look that up. What's your order number and the email you used?
```

After visitor replies, route directly to operator (you). Tidio will save the conversation in your inbox.

**Fallback after 2 failed lookups (Lyro version):**
```
Let me get a human on this. One sec.
```
→ Route to operator.

---

## Flow 6: Returns and Exchanges (Route to Thunder Returns)

**Name:** Returns Routing

**Trigger:**
- Visitor types keywords: `return`, `exchange`, `doesn't fit`, `wrong size`, `refund`, `resize`, `send back`

**Bot message:**
```
No stress. We make this easy. What do you need?
```

**Buttons:**

**Button 1: "Return for refund"**
→ Bot reply:
```
Start here, takes 60 seconds:
```
→ Send link to Thunder Returns portal URL.

**Button 2: "Exchange for different size"**
→ Bot reply:
```
Free resize within 60 days. Start here:
```
→ Send link to Thunder Returns portal URL.

**Button 3: "Something arrived damaged"**
→ Route to operator immediately.

**Button 4: "Just have a question"**
→ Route to operator.

**Cross-reference:** This is your owned tool, see [[03 Projects/Thunder Returns/CLAUDE.md]]. Every return touchpoint should funnel into Thunder Returns. That is the whole point of dogfooding your own product.

---

# PART 5: What NOT to Build (Skip the Temptation)

If you find yourself tempted to add any of these, stop. They sound smart and they do not work.

- **Quiz funnels.** Tidio's flow builder is not good enough. You will spend 4 hours building a "find your perfect piece" quiz and get 2% conversion. Do quizzes in Doofinder (see [[(C) Doofinder Quiz Maker — Build Plan]]), not Tidio.
- **Birthday or anniversary capture.** Save that for Klaviyo email flows, not chat.
- **Newsletter signup inside chat.** You already have email popups in Recart. Do not double up.
- **Auto-greeting on the homepage.** Kills bounce rate. Looks desperate.
- **Live chat at 2am with no fallback.** If you are not online, use offline mode. Do not pretend.

---

# PART 6: Build Order Checklist

Print this or copy it into your todo app. Check items off as you go.

- [ ] Part 1: Set all colors and upload logo (15 min)
- [ ] Part 2: Configure widget visibility and operating hours (10 min)
- [ ] Part 3: Lyro setup (knowledge sources + persona + escalation) (20 min)
- [ ] Flow 4: Ring Sizing (build this first, easiest, test by typing "size") (10 min)
- [ ] Flow 6: Returns (test by typing "return") (5 min)
- [ ] Flow 5: Order Status (test with a real order number) (5 min)
- [ ] Flow 1: PDP Welcome (test by sitting on a product page 45s in incognito) (10 min)
- [ ] Flow 3: Cart Recovery (test with item in cart) (5 min)
- [ ] Flow 2: Exit Intent (build LAST, only if Recart is not already running on product pages) (5 min)
- [ ] Turn each flow ON one at a time, test it, then move to the next

**Total:** 60-90 minutes if nothing breaks.

---

# PART 7: After Launch. What to Watch in Week 1

Open Tidio's **Analytics** tab daily for the first week. Look at:

1. **Conversations started by flow.** Which flows are firing the most? Which are silent?
2. **Goal completion** (if you set up goals). Are people clicking through to checkout after chatting?
3. **Most-asked questions.** Tidio logs all messages. Skim the inbox for patterns. Anything asked 3+ times that Lyro could not answer = add it to Lyro's knowledge base.
4. **Drop-off points.** If everyone clicks "Ring sizing" then exits, your sizing flow needs better copy.

**Adjust weekly.** Do not "set and forget." Chatbots are not a campaign, they are an ongoing tune-up.

---

# PART 8: Things You Will Probably Get Wrong (Pre-Mortem)

Heading these off before they happen:

**Problem:** "The chat popup is firing on every page, not just products."
**Cause:** You did not set the URL filter on the Flow 1 trigger.
**Fix:** Edit the trigger, add `URL contains /products/`.

**Problem:** "Lyro is giving wrong shipping info."
**Cause:** Your live shipping page does not match your source of truth.
**Fix:** Update the live page to match [[(C) Aydins Policies — Source of Truth]], then re-train Lyro.

**Problem:** "Two popups are firing on top of each other."
**Cause:** Tidio Flow 2 and Recart exit popup are both active on product pages.
**Fix:** Turn off one of them. Pick whichever has the better offer (Recart's 20% off probably beats Tidio's 10%, so let Recart win on product pages).

**Problem:** "Chat button color does not match my site."
**Cause:** You used Tidio's default color instead of pasting `#B08D57`.
**Fix:** Go back to Part 1. Paste the brass hex code.

**Problem:** "Bot reply uses em dashes."
**Cause:** Lyro's default training. Your persona prompt says no dashes but the model sometimes ignores.
**Fix:** Re-emphasize in persona prompt: "Never use the em dash or en dash character." If still happening, send Tidio support a complaint.

---

# Next Action

1. Open Tidio.
2. Open this guide on a second screen or print it.
3. Start at Part 1, step by step.
4. When you finish, send me a screenshot of your live Tidio dashboard and I will audit it.

Do not try to "improve" the copy as you build. Build it exactly as written, launch it, watch the data for 2 weeks, then we tune.
