# Klaviyo Current Flow Audit
Pulled: 2026-05-08 09:12:47

## Flow 1: Welcome Series — LIVE
- ID: XQZ9kX
- Klaviyo Name: Email Welcome Series with Discount
- Status: live (archived: False)
- Created: 2025-05-27T13:54:21+00:00 / Updated: 2025-05-27T13:55:16+00:00
- Trigger:
Trigger Type: Added to List

### Action 1: Email — Subject: "Enjoy your special discount now."
- Message ID: TzFzsG
- Template ID: X5U68g
- Template Name: 2025-05-27 09:55 Welcome email (coupon)
- Preview: "Exclusive Offer Awaits You!"
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BOARD, BUTTON, COLLECTIONS, CONTACT, CRAFTED, EXCITED, EXCLUSIVELY, HAVE, HOME, JOINING, THANK
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] THANK YOU FOR JOINING Lakhani Group LLC! WE'RE EXCITED TO HAVE YOU ON BOARD! ## Claim Your Exclusive 20% Off Today! Welcome to Aydins Jewelry! Discover our stunning collection of men's wedding bands and custom rings designed to elevate your style. As a warm welcome, we invite you to enjoy a fantastic 20% off with your coupon code. Simply enter {% coupon_code '20_OFF2' %} at checkout to enjoy this exclusive benefit. Embrace the luxury that knows no bounds. Get 20% off with code {% coupon_code '20_OFF2' %} [BUTTON: "Shop Now" -> http://shopaydins.com] EXCLUSIVELY CRAFTED FOR YOU... {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ Price }} {{ Compare_at }} [BUTTON: "Shop now" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ Price }} {{ Compare_at }} [BUTTON: "Shop now" -> {{ item.url }}] {% ...
```

### Action 2: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 259200}
- Action ID: 82125756
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 259200}`

### Action 3: BOOLEAN_BRANCH
- Action ID: 82125757
- Raw attrs: `{"action_type": "BOOLEAN_BRANCH", "status": "live", "created": "2025-05-27T13:55:16+00:00", "updated": "2025-05-27T13:55:17+00:00", "settings": {"is_joined": true}, "tracking_options": null, "send_options": null, "badge_options": null, "render_options": null}`

### Action 4: Email — Subject: "Unlock your special deal today!"
- Message ID: SWEwQ5
- Template ID: RBZbfr
- Template Name: 2025-05-27 09:55 Coupon reminder email
- Preview: "Your Exclusive Welcome Offer"
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## Experience a Warm Welcome Like Never Before! Hi {{ first_name | default:"Friend" }}, unlock your exclusive welcome offer. Enjoy 20% off with your unique code: {% coupon_code '20_OFF2' %}. Whether it's free shipping or a discount, elevate your style with us. Act now and embrace sophistication with ease. {% coupon_code '20_OFF2' %} [BUTTON: "Shop Now" -> http://shopaydins.com] 🌟Discover Our Exciting Range of Products!👇🌟 {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ Price }} {{ Compare_at }} [BUTTON: "Shop now" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ Price }} {{ Compare_at }} [BUTTON: "Shop now" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:2 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:2%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> ...
```

### Action 5: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 259200}
- Action ID: 82125759
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 259200}`

### Action 6: Email — Subject: "Stay updated with our latest designs."
- Message ID: SjDuds
- Template ID: QYY8CN
- Template Name: 2025-05-27 09:55 Social media email
- Preview: "Join Us on Social Media"
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME
- **Body extracted:**

```
[IMG: Logo]
[BUTTON: "HOME" -> https://shopaydins.com/]
[BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections]
[BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins]
## Follow Us on Social Media!
Hey first_name | default:"Friend", it’s time to elevate your style! Dive into our social media channels for exclusive access to stunning men’s wedding bands and custom rings. Don’t miss out on exciting new arrivals and behind-the-scenes insights into our exquisite craftsmanship. Join our global community and discover your perfect piece today!
[IMG: facebook]
[IMG: twitter]
[IMG: instagram]
[IMG: pinterest]
{% unsubscribe %}.
{{ organization.name }} {{ organization.full_address }}
```

### Action 7: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 345600}
- Action ID: 82125761
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 345600}`

### Action 8: Email — Subject: "Explore top picks catered for you."
- Message ID: VUvfeq
- Template ID: XxEC47
- Template Name: 2025-05-27 09:55 Best sellers email
- Preview: "Discover Our Bestsellers"
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME
- **Body extracted:**

```
[IMG: Logo]
[BUTTON: "HOME" -> https://shopaydins.com/]
[BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections]
[BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins]
## Discover Our Must-Have Selections!
Elevate your style with our distinguished selection of men's wedding bands and custom rings. Enjoy the craftsmanship and design that has captured the attention of our global community. Discover what makes these pieces truly remarkable for yourself today.
[BUTTON: "Shop Now" -> http://shopaydins.com]
## Men's Wedding Bands
Discover the elegance of our classic yet modern bands, perfect for every occasion. Meticulously crafted, they are a testament to timeless love that will enhance your most cherished moments.
## Custom Rings
Discover your personal elegance with our bespoke rings. Crafted just for you, each piece is an exquisite masterpiece that sets you apart. Don't miss out on owning something truly unique!
## Discover Your New Favorites!
Discover our stunning selection of rings tailored for every style. Find your ideal match today!
[BUTTON: "Shop Now" -> http://shopaydins.com]
[IMG: facebook]
[IMG: twitter]
[IMG: instagram]
[IMG: pinterest]
{% unsubscribe %}.
{{ organization.name }} {{ organization.full_address }}
```


---

## Flow 2: Abandoned Cart — LIVE
- ID: TrNjjf
- Klaviyo Name: Abandoned Cart Reminder (Email)
- Status: live (archived: False)
- Created: 2025-05-27T12:25:58+00:00 / Updated: 2025-05-27T12:34:08+00:00
- Trigger:
Trigger Type: Metric

### Action 1: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 1800}
- Action ID: 82119928
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 1800}`

### Action 2: Email — Subject: "Need a gentle nudge? Enjoy 20 % off today"
- Message ID: SQdgLg
- Template ID: Sdce9D
- Template Name: 2025-05-27 08:34 Email #1
- Preview: "Use code EMK20 before midnight to secure your handcrafted piece."
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: ALSO, BUTTON, COLLECTIONS, CONTACT, EMK20, HOME, HUDSON, LIKE, MIGHT, ORBIT, THESE
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## A Little Thank-You: 20 % Off We know great keepsakes take thought. To make it easy, here’s a 20% off code: EMK20—good until 11:59 PM tonight. [BUTTON: "Return to cart" -> {{ event.extra.checkout_url|default:organization.url }}] {% if event.extra.line_items %} {% for item in event.extra.line_items %} [IMG: {{ item.product.title }}] ## [BUTTON: "{{ item.product.title }}" -> {{ organization.url|trim_slash }}/products/{{ item.product.handle }}] Quantity: {{ item.quantity|floatformat:0 }} — Total: {% currency_format item.line_price|floatformat:2 %} {% endfor %} {% else %} {% endif %} How do I find my ring size? Check our [BUTTON: "international ring-size chart" -> https://shopaydins.com/pages/size-chart] for quick conversions. Want the exact size right now? Open [BUTTON: "findmyringsize.com" -> https://findmyringsize.com] on your phone and follow the on-screen guide. What’s your return & exchange policy? Every piece comes with 30-day free returns & exchanges. If it isn’t perfect, send it back and we’ll resize, remake, or refund. Is engraving really free? Absolutely. Laser text engraving is included with every purchase. Want fingerprints, handwriting, or a logo? Upload your artwork before adding to cart and we’ll handle the rest. Real customers, real stories—tag #AydinsJewelry on Instagram to be featured. YOU ...
```

### Action 3: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 72000}
- Action ID: 82119930
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 72000}`

### Action 4: Email — Subject: "Your handcrafted jewelry is nearly ready ✨"
- Message ID: UCDagK
- Template ID: XAtSF6
- Template Name: 2025-05-27 08:34 Email #2
- Preview: "Finish your order today—free engraving & lifetime warranty included."
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME, HUDSON, ORBIT
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## Thanks for choosing a piece from our family workshop. Free laser engraving on every item Lifetime fit guarantee & warranty 2-day U.S. shipping on most orders [BUTTON: "Resume Checkout" -> {{ event.extra.checkout_url|default:organization.url }}] {% if event.extra.line_items %} {% for item in event.extra.line_items %} [IMG: {{ item.product.title }}] ## [BUTTON: "{{ item.product.title }}" -> {{ organization.url|trim_slash }}/products/{{ item.product.handle }}] Quantity: {{ item.quantity|floatformat:0 }} — Total: {% currency_format item.line_price|floatformat:2 %} {% endfor %} {% else %} {% endif %} ★★★★★ “The engraving came out perfect—couldn’t be happier with the craftsmanship and fit.” — Michael R., Dallas TX Discover More Amazing Products Right Here! Don’t Miss Out!👇 [IMG: Image of Pearl Essence - Women's Beaded Bracelet] [BUTTON: "Pearl Essence - Women's Beaded Bracelet" -> https://aydinsjewelry.myshopify.com/products/pearl-essence-womens-beaded-bracelet] $85.00 [BUTTON: "Shop now" -> https://aydinsjewelry.myshopify.com/products/pearl-essence-womens-beaded-bracelet] [IMG: Image of ORBIT | Custom Engraved Women's Signet Ring - Gold & Silver] ORBIT | Custom Engraved Women's Signet Ring - Gold & Silver (https://aydinsjewelry.myshopify.com/products/orbit-custom-logo-womens-laser-engraved-signet-ring-gold-silver) $57.00 [BUTTON: "Shop now" -> https://aydinsjewelry.myshopify.com/products/orbit-custom-logo-womens-laser-engraved-signet-ring-gold-silver] [IMG: Image of HUDSON | Silver Damascus Steel Ring, Carbon Fiber Inlay] HUDSON | Silver Damascus Steel Ring, Carbon Fiber Inlay (https://aydinsjewelry.myshopify.com/products/hudson-silver-damascus-steel-ring-carbon-fiber-inlay) $299.00 [BUTTON: "Shop ...
```

### Action 5: SMS
- Action ID: 82295814
- Raw attrs: `{"action_type": "SEND_SMS", "status": "live", "created": "2025-05-29T19:55:22+00:00", "updated": "2025-05-30T04:33:03+00:00", "settings": {}, "tracking_options": {"add_utm": false, "utm_params": []}, "send_options": {"use_smart_sending": true, "is_transactional": false, "quiet_hours_enabled": true}, "badge_options": null, "render_options": {"shorten_links": true, "add_org_prefix": true, "add_info_link": true, "add_opt_out_language": true}}`

### Action 6: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 300}
- Action ID: 82296510
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 300}`

### Action 7: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 172800}
- Action ID: 82313810
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 172800}`

### Action 8: Email — Subject: "Final reminder: we’re holding your jewelry a little longer"
- Message ID: UJLFPZ
- Template ID: Wxczku
- Template Name: 2025-05-27 08:34 Email #1
- Preview: "We’ll release it back to the workshop at midnight—let us finish it for you."
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: ALSO, BUTTON, COLLECTIONS, CONTACT, EMK20, HOME, HUDSON, LIKE, MIGHT, ORBIT, THESE
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## Last Call to Reserve Your Piece Since 2011 our small team has turned raw metal into lifelong symbols of love. Your chosen jewelry is set aside, but space in the workshop is limited. [BUTTON: "Complete My Order" -> {{ event.extra.checkout_url|default:organization.url }}] {% if event.extra.line_items %} {% for item in event.extra.line_items %} [IMG: {{ item.product.title }}] ## [BUTTON: "{{ item.product.title }}" -> {{ organization.url|trim_slash }}/products/{{ item.product.handle }}] Quantity: {{ item.quantity|floatformat:0 }} — Total: {% currency_format item.line_price|floatformat:2 %} {% endfor %} {% else %} {% endif %} ✅ Lifetime Warranty & Fit ✒️ Free Laser Engraving 🚚 Free 2-Day Shipping YOU MIGHT ALSO LIKE........THESE 👇 {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ Price }} {{ Compare_at }} [BUTTON: "Shop now" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ Price }} {{ Compare_at }} ...
```

### Action 9: BOOLEAN_BRANCH
- Action ID: 82910349
- Raw attrs: `{"action_type": "BOOLEAN_BRANCH", "status": "live", "created": "2025-06-10T17:51:10+00:00", "updated": "2025-06-10T17:53:16+00:00", "settings": {"is_joined": false}, "tracking_options": null, "send_options": null, "badge_options": null, "render_options": null}`

### Action 10: BOOLEAN_BRANCH
- Action ID: 82910463
- Raw attrs: `{"action_type": "BOOLEAN_BRANCH", "status": "live", "created": "2025-06-10T17:53:33+00:00", "updated": "2025-06-10T17:54:34+00:00", "settings": {"is_joined": false}, "tracking_options": null, "send_options": null, "badge_options": null, "render_options": null}`


---

## Flow 3: Customer Winback — LIVE
- ID: QVt7Vu
- Klaviyo Name: Customer Winback - Standard
- Status: live (archived: False)
- Created: 2025-05-27T15:14:36+00:00 / Updated: 2025-05-27T15:14:39+00:00
- Trigger:
Trigger Type: Metric

### Action 1: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 864000}
- Action ID: 82132791
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 864000}`

### Action 2: Email — Subject: "It's been a while..."
- Message ID: WiJLsV
- Template ID: Y7aDXq
- Template Name: [automation] [Trimmed] Shopify \ Win Back \ First Email
- Preview: ""
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## Discover the Hottest Trends You Can't Miss! From time to time, we like to let you know which products are trending. We combined your interests with what's popular now to create recommendations just for you. {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:2 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:2%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:3 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:3%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:4 %} {% with ...
```

### Action 3: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 2160000}
- Action ID: 82132796
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 2160000}`

### Action 4: Email — Subject: "We've missed you."
- Message ID: QQPRA6
- Template ID: SDfK6z
- Template Name: [automation] [Trimmed] Shopify \ Win Back \ First Email
- Preview: ""
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## Since you've been gone, a lot has changed. We're sending you this email to get you caught up. We spent some time and found these items just for you - let us know what you think! {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:2 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:2%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:3 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:3%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:4 %} {% ...
```


---

## Flow 4: Customer Thank You — LIVE
- ID: S3ZsM6
- Klaviyo Name: Customer Thank You
- Status: live (archived: False)
- Created: 2025-05-27T14:49:04+00:00 / Updated: 2025-05-27T14:49:07+00:00
- Trigger:
Trigger Type: Metric

### Action 1: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 86400}
- Action ID: 82130145
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 86400}`

### Action 2: BOOLEAN_BRANCH
- Action ID: 82130146
- Raw attrs: `{"action_type": "BOOLEAN_BRANCH", "status": "live", "created": "2025-05-27T14:49:04+00:00", "updated": "2025-05-27T14:49:07+00:00", "settings": {"is_joined": false}, "tracking_options": null, "send_options": null, "badge_options": null, "render_options": null}`

### Action 3: Email — Subject: "Thank you for choosing Aydins — your order is in expert hands"
- Message ID: TQrkhz
- Template ID: VCRdN4
- Template Name: [automation] [Trimmed] Base Template
- Preview: "We’ve started crafting your custom piece. Here’s what happens next."
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] Hey {{ person.first_name }}, What happens next: • We begin crafting your order by hand • Engraving is completed with precision laser tools • It’s inspected and packaged at our Dallas workshop • Tracking info will be emailed once it ships (usually within 1–3 business days) In the meantime: If you need help with sizing, engraving notes, or have any questions at all, just reply to this email or reach out at sales@shopaydins.com. We’re always here to help. Thank you again for being part of the Aydins family. We can’t wait for you to see your piece in person. — The Aydins Jewelry Team 🌟Discover What You’ll Adore Next!🌟👇 {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:0%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ Price }} {{ Compare_at }} [BUTTON: "Shop now" -> {{ item.url }}] {% endwith %} {% endwith %} {% endif %} {% if feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1 %} {% with item=feeds.SHOP_POPULAR_ALL_CATEGORIES|index:1%} {% with Title=item.title|safe Price=item.price|default:"" Compare_at=item.regular_price|default:"" %} [IMG: Image of {{ Title }}] [BUTTON: "{{ Title }}" -> {{ item.url }}] {{ ...
```

### Action 4: Email — Subject: "We appreciate your loyalty — order confirmed!"
- Message ID: UZQbbr
- Template ID: WNg4FU
- Template Name: Shopify Repeat Thank You
- Preview: "Repeat customers like you are the heart of Aydins — thank you again."
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME, HUDSON, ORBIT
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] Thank you for your order, {{ person.first_name|default:'' }}. Thank you for placing another order with Aydins Jewelry — it means the world to us. As a returning customer, your continued trust and support inspire our craft every day. Here’s what happens next: • We begin crafting your piece by hand • Engraving is completed with precision laser tools • It’s inspected and packaged at our Dallas workshop • Tracking info will be emailed once it ships (usually within 1–3 business days) Need anything else? Whether it’s a sizing question, a gift recommendation, or something custom — just reply to this email or reach us at sales@shopaydins.com. We’re truly grateful to have you as part of the Aydins family. We can’t wait for you to receive your next handcrafted piece. — The Aydins Jewelry Team Discover More Amazing Picks!👇 [IMG: Image of Pearl Essence - Women's Beaded Bracelet] [BUTTON: "Pearl Essence - Women's Beaded Bracelet" -> https://aydinsjewelry.myshopify.com/products/pearl-essence-womens-beaded-bracelet] $85.00 [BUTTON: "Shop now" -> https://aydinsjewelry.myshopify.com/products/pearl-essence-womens-beaded-bracelet] [IMG: Image of ORBIT | Custom Engraved Women's Signet Ring - Gold & Silver] ORBIT | Custom Engraved Women's Signet Ring - Gold & ...
```


---

## Flow 5: Browse Abandonment — LIVE
- ID: UiUnac
- Klaviyo Name: Browse Abandonment
- Status: live (archived: False)
- Created: 2025-05-27T15:05:49+00:00 / Updated: 2025-06-10T02:28:49+00:00
- Trigger:
Trigger Type: Metric

### Action 1: Time Delay — {"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 7200}
- Action ID: 82859838
- Raw settings: `{"days_of_week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "delay_seconds": 7200}`

### Action 2: Email — Subject: "Your piece caught our eye too ✨"
- Message ID: T6q2n5
- Template ID: V2MqsD
- Template Name: 2025-06-09 22:38 Abandoned Cart Flows Email 1
- Preview: "Every Aydins design is crafted with meaning — and yours is waiting."
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME, HUDSON, ORBIT, ORDERS
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## Don’t Let Your Items Slip Away! We noticed you were checking out one of our custom designs. Whether it was a tungsten ring, fingerprint pendant, or dog tag — we just wanted to say: great choice. {% if event.extra.line_items %} {% for item in event.extra.line_items %} [BUTTON: "{{ item.product.title }}" -> {{ organization.url|trim_slash }}/products/{{ item.product.handle }}] Quantity: {{ item.quantity|floatformat:0 }} — Total: {% currency_format item.line_price|floatformat:2 %} {% endfor %} {% else %} {% endif %} ★★★★★ "Exactly what I hoped for" "I ordered a custom tungsten ring with engraving for my fiancé — the quality was incredible and the service was top-notch. Arrived fast and beautifully packaged." – Marcus G. | Verified Buyer [BUTTON: "View My Item" -> {{ event.extra.checkout_url}}] FREE SHIPPING ON ALL ORDERS* ## Most loved categories [IMG: Image of Pearl Essence - Women's Beaded Bracelet] [BUTTON: "Pearl Essence - Women's Beaded Bracelet" -> https://aydinsjewelry.myshopify.com/products/pearl-essence-womens-beaded-bracelet] $85.00 [BUTTON: "Shop now" -> https://aydinsjewelry.myshopify.com/products/pearl-essence-womens-beaded-bracelet] [IMG: Image of ORBIT | Custom Engraved Women's Signet Ring - Gold & Silver] ORBIT | Custom Engraved Women's Signet Ring - Gold & Silver (https://aydinsjewelry.myshopify.com/products/orbit-custom-logo-womens-laser-engraved-signet-ring-gold-silver) $57.00 [BUTTON: "Shop now" -> https://aydinsjewelry.myshopify.com/products/orbit-custom-logo-womens-laser-engraved-signet-ring-gold-silver] ...
```


---

## Flow 6: Order Confirmation — DRAFT
- ID: W5AfdY
- Klaviyo Name: Order Confirmation - Standard
- Status: draft (archived: False)
- Created: 2025-05-27T16:03:56+00:00 / Updated: 2025-05-27T16:03:59+00:00
- Trigger:
Trigger Type: Metric

### Action 1: Email — Subject: "Thank you for your order!"
- Message ID: RRHrAp
- Template ID: TE9j6S
- Template Name: Shopify Order Confirmation (Transactional)
- Preview: ""
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, DISCOUNT, HOME, ORDER, SHOPAYDINS, TRACK, YOUR
- **Body extracted:**

```
[IMG: Logo] [BUTTON: "HOME" -> https://shopaydins.com/] [BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections] [BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins] ## Thank you for your purchase! This email is to confirm your order with Aydin's Jewelry. You can follow the status of your order by clicking the button below👇 [BUTTON: "TRACK YOUR ORDER>" -> https://shopaydins.com//tools/track?email={{ email|url_encode }}&order={{ event.extra.order_number }}] Your order number is {{ event.extra.order_number }}. ## Order Details: {% if event.extra.line_items %} {% for item in event.extra.line_items %} [IMG: {{ item.product.title }}] ## {{ item.product.title }} Quantity: {{ item.quantity }} Total: {{ item.price }} {% endfor %} {% else %} {% endif %} Discount-{{ event.discount_amount }} Subtotal{{ event.subtotal }} Shipping ({{ event.shipping_method }}){{ event.shipping_amount }} Tax{{ event.tax_amount }} Total{{ event.total_price }} Payment Method Payment Method{{ event.payment_method }} Shipping Address {{ event.shipping_address.first_name }} {{ event.shipping_address.last_name }} {{ event.shipping_address.address1 }} {{ event.shipping_address.city }}, {{ event.shipping_address.province }} {{ event.shipping_address.zip }} Tel: {{ event.shipping_address.phone }} Customer {{ event.customer.first_name }} {{ event.customer.last_name }} {{ event.customer.address1 }} {{ event.customer.city }}, {{ event.customer.province }} {{ event.customer.zip }} Tel: {{ event.customer.phone }} {{ event.customer.email }} Order Notes {{ event.note }} Please do not hesitate to give us a call on 1-800-214-7345 or send an email to [BUTTON: "sales@shopaydins.com" -> mailto:sales@shopaydins.com] if you have ...
```


---

## Flow 7: Shipping Confirmation — DRAFT
- ID: WcmfHm
- Klaviyo Name: Full Shipping Confirmation - Standard
- Status: draft (archived: False)
- Created: 2025-05-27T16:08:24+00:00 / Updated: 2025-05-27T16:08:26+00:00
- Trigger:
Trigger Type: Metric

### Action 1: Email — Subject: "Your {{ organization.name }} order has shipped!"
- Message ID: RYus5L
- Template ID: TLUjAf
- Template Name: None
- Preview: ""
- From: hello@aydinsjewelry.com (Aydins Jewelry)
- Smart Sending: None
- Discount/Codes detected: BUTTON, COLLECTIONS, CONTACT, HOME
- **Body extracted:**

```
[IMG: Logo]
[BUTTON: "HOME" -> https://shopaydins.com/]
[BUTTON: "COLLECTIONS" -> https://shopaydins.com/collections]
[BUTTON: "CONTACT" -> https://shopaydins.com/pages/contact-aydins]
Hi {{ event.extra.customer.default_address.first_name }},
We've got some good news! All of the items from order {{ event.extra.order_number }} have now been shipped:
{% if event.extra.line_items %}
{% for item in event.extra.line_items %}
## [BUTTON: "{{ item.name }}" -> {{ organization.url|trim_slash }}/products/{{ item.product.handle }}]
Quantity: {{ item.quantity|floatformat:0 }} — Total: ${{ item.price|floatformat:2 }}
{% endfor %}
{% else %}
{% endif %}
They are being shipped {% if event.extra.fulfillments.0.tracking_company %}via {{ event.extra.fulfillments.0.tracking_company }} {% endif %}to the following address:
{{ event.extra.shipping_address.first_name }} {{ event.extra.shipping_address.last_name }}
{{ event.extra.shipping_address.address1 }}
{{ event.extra.shipping_address.city }}, {{ event.extra.shipping_address.province_code }} {{ event.extra.shipping_address.zip }}
The tracking number for these items is {{ event.extra.fulfillments.0.tracking_number }}. Use the link below to see the status of your shipment.
[BUTTON: "Track Your Package" -> {{ event.extra.fulfillments.0.tracking_url }}]
Please allow some time for the status of the shipment to correctly display at the above address.
You will receive a confirmation email when more items from your order have been shipped.
Thanks again for ordering from {{ event.extra.fulfillments.0.line_items.0.vendor }}!
— The Team
[IMG: facebook]
[IMG: twitter]
[IMG: instagram]
[IMG: pinterest]
```


---

## Run Summary
- Total flows requested: 7
- Failed flows: 0
- Total emails pulled: 14
- Runtime: 24.6s