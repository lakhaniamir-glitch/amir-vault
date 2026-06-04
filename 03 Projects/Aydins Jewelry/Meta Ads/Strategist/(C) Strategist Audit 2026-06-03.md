# Beta Meta Strategist Audit, Aydins

Date: 2026-06-03
Mode: read-only Marketing API audit. No writes, no budget changes, no campaign or ad set changes.
Raw API export: `/home/openclaw/.openclaw/command-center/work/meta/meta-strategist-api-data-2026-06-03.json`
Account: `act_23304577` / Aydins / USD / America/Los_Angeles

## Executive read

- Account is not broken, but it is under-structured for a professional scale path.
- Current live spend is concentrated in one active sales campaign, broad US mobile-first purchase optimization, with one historical winner and two new UGC ads just activated.
- API returned 0 custom audiences and 0 saved audiences. That is the biggest strategic gap. Prospecting, retargeting, and purchaser exclusions are not set up as a controlled system.
- The active winner has proven creative-market fit, but the account lacks a formal testing lane, retargeting lane, and exclusion hygiene.
- Last 30-day topline from Amir: $1,067 spend, 12 purchases, $3,069 revenue, 2.87 ROAS, $89 CPA, 1.55% CTR. Use this as the attributed source of truth. API action arrays include overlapping event types and should not be naively summed.

## 1. Account structure

- Campaigns pulled: 129
- Ad sets pulled: 297
- Ads pulled: 860
- Active campaign count: 1
- Active ad set count: 2

### Campaign inventory

| ID | Name | Status | Effective | Objective | Budget | Bid strategy | Start | Stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52566193429730 | Catalog Sales | PAUSED | PAUSED | OUTCOME_SALES | $25.00/day | LOWEST_COST_WITHOUT_CAP | 2025-12-14T12:05:14-0800 |  |
| 52518283129530 | 2/AY/9.8/New Gemini Images/ - 50 - | PAUSED | PAUSED | OUTCOME_SALES | $20.00/day | LOWEST_COST_WITHOUT_CAP | 2025-09-08T22:05:43-0700 |  |
| 6929192369326 | 1/AY/6.3/Couples engraved/ - 30 | ACTIVE | ACTIVE | OUTCOME_SALES | $50.00/day | LOWEST_COST_WITHOUT_CAP | 2025-06-03T11:26:34-0700 |  |
| 6716392056726 | 51/FB/1.10/Fingerprint/Review | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-10-01T03:03:31-0700 |  |
| 6716013430326 | 50/FB/30.9/Fingerprint/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-30T00:00:00-0700 |  |
| 6713494839326 | 2/AY/6.3/Fingerprint/ | PAUSED | PAUSED | OUTCOME_SALES | $30.00/day | LOWEST_COST_WITHOUT_CAP | 2024-09-19T00:36:47-0700 |  |
| 6713108940926 | 48/FB/18.9/Tweet Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-18T00:00:00-0700 |  |
| 6712801874326 | 47/FB/17.9/4 square/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-16T19:34:17-0700 |  |
| 6712564925726 | 46/FB/16.9/4 square/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-16T00:00:00-0700 |  |
| 6711953264526 | 45/FB/13.9/Tweet Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-13T00:44:49-0700 |  |
| 6711537370926 | 44/FB/12.9/GG search/4 Img | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-12T00:00:00-0700 |  |
| 6710493990926 | 43/FB/9.9/Phone Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-09T00:00:00-0700 |  |
| 6709594126326 | 42/FB/5.9/Catalog/Dynamic | PAUSED | PAUSED | OUTCOME_SALES | $40.00/day | LOWEST_COST_WITHOUT_CAP | 2024-09-05T00:00:00-0700 |  |
| 6709586206326 | 41/FB/5.9/All/Catalog | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-05T00:00:00-0700 |  |
| 6709582567326 | 40/FB/5.9/4 Square/Plain Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-05T00:00:00-0700 |  |
| 6709579510526 | 39/FB/5.9/Tweet Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-05T00:00:00-0700 |  |
| 6708491015726 | 35/FB/1.9/Tweet Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-09-01T00:00:00-0700 |  |
| 6707957580526 | 38 - Adv all - 30/8 Campaign | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-30T00:00:00-0700 |  |
| 6707711947526 | 37/FB/29.8/Catalog/Target | PAUSED | PAUSED | OUTCOME_SALES | $40.00/day | LOWEST_COST_WITHOUT_CAP | 2024-08-29T01:11:54-0700 |  |
| 6707711101526 | 38/FB/29.8/Catalog/Broad | PAUSED | PAUSED | OUTCOME_SALES | $40.00/day | LOWEST_COST_WITHOUT_CAP | 2024-08-29T01:10:00-0700 |  |
| 6707707683926 | 37/FB/29.8/Catalog/ | PAUSED | PAUSED | OUTCOME_SALES | $40.00/day | LOWEST_COST_WITHOUT_CAP | 2024-08-29T01:05:03-0700 |  |
| 6707392748526 | 27a/FB/29.07/4 Square/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-28T00:25:57-0700 |  |
| 6706532736126 | 36/FB/25.8/4 Square/Color Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-24T17:33:05-0700 |  |
| 6705945951926 | 35/FB/22.8/Tweet Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-22T04:48:00-0700 |  |
| 6705945209326 | 35/FB/22.8/Tweet Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-22T04:41:28-0700 |  |
| 6705894616926 | 35/FB/22.8/Tweet Review/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-22T00:36:32-0700 |  |
| 6704283030526 | 34/FB/16.8/Unique Inlay/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-16T00:00:00-0700 |  |
| 6703721628126 | 33/FB/14.8/The best ring/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-14T00:00:00-0700 |  |
| 6703153941926 | 32/FB/12.8/Image/Collection | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-12T22:34:03-0700 |  |
| 6701471640126 | 31/FB/5.8/The best ring(b)/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-05T01:36:43-0700 |  |
| 6701469839726 | 30/FB/5.8/The best ring(a)/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-05T01:30:21-0700 |  |
| 6700890714726 | 29/FB/2.8/4 Square/Color Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-08-02T00:00:00-0700 |  |
| 6700082951326 | 28/FB/30.7/Single Image/Minimal Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-30T00:00:00-0700 |  |
| 6699846021926 | 27/FB/29.07/4 Square/Color Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-29T00:00:00-0700 |  |
| 6699845659126 | 26/FB/29.07/Single Image/Minimal Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-29T00:00:00-0700 |  |
| 6699745724326 | 25/FB/28.7/Single Image/Minimal Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-28T00:00:00-0700 |  |
| 6698723325726 | 24/FB/23.7/4 square/Minimal Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-23T00:00:00-0700 |  |
| 6698438338726 | 23/FB/22.7/Review/Minimal Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-22T00:00:00-0700 |  |
| 6697942622726 | 22/FB/19.7/Carousel/Wood background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-19T00:00:00-0700 |  |
| 6697938798526 | 21/FB/19/7//Adv+ - Copy | PAUSED | PAUSED | OUTCOME_SALES | $20.00/day | LOWEST_COST_WITHOUT_CAP | 2024-07-19T00:00:00-0700 |  |
| 6697938151126 | 20/FB/19/7//Adv+ | PAUSED | PAUSED | OUTCOME_SALES | $20.00/day | LOWEST_COST_WITHOUT_CAP | 2024-07-19T00:00:00-0700 |  |
| 6697489469326 | 19/FB/17.7/4 Square/Color Background | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-17T00:00:00-0700 |  |
| 6697240050126 | 18/FB/16.7/Craft your own ring/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-16T00:00:00-0700 |  |
| 6696537989926 | 17/FB/12.7/Web Review/Split | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-12T00:00:00-0700 |  |
| 6696536355926 | 16/FB/12.7/Web Review/Center | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-12T00:00:00-0700 |  |
| 6696234352326 | 15/FB/11.7/Review/1 product | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-11T00:00:00-0700 |  |
| 6696233598526 | 14/FB/11.7/Review/4 square | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-11T00:00:00-0700 |  |
| 6694374362726 | 13/FB/3.7/GIF/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-03T00:47:52-0700 |  |
| 6694367563326 | 12/FB/3.7/Transition Hook/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-07-03T00:42:06-0700 |  |
| 6693257059526 | 11/FB/28.6/Testimonial/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-28T00:50:57-0700 |  |
| 6693256225126 | 10/FB/28.6/Scratch/PAS | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-28T00:40:34-0700 |  |
| 6693011279326 | 9/FB/27.6/If your ring looks like this/PAS | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-27T02:08:15-0700 |  |
| 6691003192926 | 8/FB/16.06/Type 4 Img Best Sellers/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-16T01:04:07-0700 |  |
| 6690964440926 | 7/FB/16.6/Compare/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-16T00:00:00-0700 |  |
| 6690955896126 | 6/FB/15.6/Test Static/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-15T07:02:44-0700 |  |
| 6689495894326 | 05/FB/Testimonial/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-09T00:00:00-0700 |  |
| 6689174156926 | 04/FB/Quote/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-07T00:18:09-0700 |  |
| 6689170018126 | 03/FB/3 Benefits/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-06-07T00:05:27-0700 |  |
| 6687498995526 | 02/FB/All/ | PAUSED | PAUSED | OUTCOME_SALES |  | None | 2024-05-31T00:26:33-0700 |  |
| 6687264653326 | 01/FB/All/Catalog | PAUSED | PAUSED | OUTCOME_SALES | $50.00/day | LOWEST_COST_WITHOUT_CAP | 2024-05-30T03:17:33-0700 |  |
| 6685989934726 | New Traffic - 5-23-2024 | PAUSED | PAUSED | OUTCOME_TRAFFIC | $30.00/day | LOWEST_COST_WITHOUT_CAP | 2024-05-23T12:51:18-0700 |  |
| 6674656844926 | Advantage+ shopping campaign 05/09/2024 Campaign | PAUSED | PAUSED | OUTCOME_SALES | $50.00/day | LOWEST_COST_WITHOUT_CAP | 2024-05-09T12:38:08-0700 |  |
| 6335251474726 | Sponsored Message [RECART] | PAUSED | PAUSED | MESSAGES |  | None | 2022-07-01T22:55:56-0700 | 2022-07-05T16:59:59-0700 |
| 6291242048326 | **LP - Prospecting - Catalog Sales | PAUSED | PAUSED | PRODUCT_CATALOG_SALES | $39.99/day | LOWEST_COST_WITHOUT_CAP | 2021-06-25T13:45:45-0700 |  |
| 6284237254726 | **LP - Static Remarketing - Conv | PAUSED | PAUSED | CONVERSIONS | $26.66/day | LOWEST_COST_WITHOUT_CAP | 2021-04-27T12:30:39-0700 |  |
| 6284229718126 | **LP - Mid-Funnel - Conv | PAUSED | PAUSED | CONVERSIONS | $3.33/day | LOWEST_COST_WITHOUT_CAP | 2021-04-27T10:51:36-0700 |  |
| 6284226881926 | **LP - Prospecting - Conv | PAUSED | PAUSED | CONVERSIONS | $31.66/day | LOWEST_COST_WITHOUT_CAP | 2021-04-27T10:18:25-0700 |  |
| 6280361148926 | **LP - Draft | PAUSED | PAUSED | LINK_CLICKS | $1.00/day | LOWEST_COST_WITHOUT_CAP | 2021-03-25T18:38:14-0700 |  |
| 6273746427926 | TOF - Prospecting - ABO | PAUSED | PAUSED | CONVERSIONS |  | None | 2021-02-02T11:45:25-0800 |  |
| 6265217615326 | NG - New Ad Creatives - 12/13/20 | PAUSED | PAUSED | CONVERSIONS |  | None | 2020-12-13T08:30:10-0800 |  |
| 6263717814726 | NG CBO Test 9% and 10% Purchase LLA | PAUSED | PAUSED | CONVERSIONS | $50.00/day | LOWEST_COST_WITHOUT_CAP | 2020-12-04T08:42:10-0800 |  |
| 6262544556126 | NG - Black Friday Ads | PAUSED | PAUSED | CONVERSIONS |  | None | 2020-11-27T10:29:52-0800 |  |
| 6260662944126 | NG - Black Friday Conversion Campaign | PAUSED | PAUSED | CONVERSIONS |  | None | 2020-11-17T07:49:48-0800 |  |
| 6256059416126 | NG - New Conversion Campaign | PAUSED | PAUSED | CONVERSIONS |  | None | 2020-10-16T11:09:53-0700 |  |
| 6255744092926 | NG - DPA Catalog Ads | PAUSED | PAUSED | PRODUCT_CATALOG_SALES |  | None | 2020-10-14T11:52:33-0700 |  |
| 6179684478126 | Laser Engraving - 20 Miles - Grapevine | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2019-11-25T22:36:48-0800 |  |
| 6179681869326 | Traffic - Fingerprint Dog Tag | PAUSED | PAUSED | LINK_CLICKS | $20.00/day | LOWEST_COST_WITHOUT_CAP | 2019-11-25T22:03:37-0800 |  |
| 6176833360526 | Conversions | PAUSED | PAUSED | CONVERSIONS | $20.00/day | LOWEST_COST_WITHOUT_CAP | 2019-11-14T11:21:41-0800 |  |
| 6152985315326 | [06/02/2019] Promoting http://Shopaydins.com/ | PAUSED | PAUSED | CONVERSIONS |  | None | 2019-06-02T12:42:35-0700 |  |
| 6151838367926 | Messages | PAUSED | PAUSED | MESSAGES |  | None | 2019-05-24T18:58:54-0700 |  |
| 6151411019326 | Aydins - Retarget | PAUSED | PAUSED | PRODUCT_CATALOG_SALES |  | None | 2019-05-21T17:40:45-0700 |  |
| 6151236161126 | Website - Traffic | PAUSED | PAUSED | LINK_CLICKS | $50.00/day | LOWEST_COST_WITHOUT_CAP | 2019-05-20T12:23:24-0700 |  |
| 6150567429926 | Website - Conversions | PAUSED | PAUSED | CONVERSIONS | $20.00/day | LOWEST_COST_WITHOUT_CAP | 2019-05-14T22:27:55-0700 |  |
| 6148614928526 | COV - Purchase Lookalike | PAUSED | PAUSED | CONVERSIONS |  | None | 2019-04-28T20:26:21-0700 |  |
| 6146932382926 | AL--Website--CS--May | PAUSED | PAUSED | PRODUCT_CATALOG_SALES | $30.00/day | LOWEST_COST_WITHOUT_CAP | 2019-04-13T07:15:41-0700 |  |
| 6146281331726 | PGC--TOF--Conversions--Purchase 2% | PAUSED | PAUSED | PRODUCT_CATALOG_SALES |  | None | 2019-04-08T16:41:27-0700 |  |
| 6145556732326 | PGC--TOF--LLA 2% Purchase Conversion | PAUSED | PAUSED | CONVERSIONS |  | None | 2019-04-02T16:20:00-0700 |  |
| 6145556549326 | PGC--TOF--Initiate Checkout | PAUSED | PAUSED | PRODUCT_CATALOG_SALES |  | None | 1969-12-31T15:59:59-0800 |  |
| 6144392014926 | Personalized 3D Bar Necklace | PAUSED | PAUSED | CONVERSIONS | $50.00/day | LOWEST_COST_WITHOUT_CAP | 2019-03-23T19:07:21-0700 |  |
| 6144144621126 | Post: "💎💍💎GIVE AWAY💎💍💎 " | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2019-03-21T12:56:49-0700 | 2019-03-31T12:56:49-0700 |
| 6143362688126 | 3D Bar Necklace Funnel | PAUSED | PAUSED | LINK_CLICKS |  | None | 2019-03-15T06:15:33-0700 | 2019-03-21T23:59:33-0700 |
| 6141959815126 | Aydins--Traffic DPA | PAUSED | PAUSED | LINK_CLICKS | $40.00/day | LOWEST_COST_WITHOUT_CAP | 2019-03-01T06:44:11-0800 |  |
| 6135787158326 | PGC-DPA--MOF | PAUSED | PAUSED | PRODUCT_CATALOG_SALES | $30.00/day | LOWEST_COST_WITHOUT_CAP | 2019-01-10T10:10:30-0800 |  |
| 6134933457526 | PGC--MOF--Catalog Ads | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2019-01-03T14:10:52-0800 |  |
| 6132955196526 | Conversion Campaign 2 | PAUSED | PAUSED | CONVERSIONS |  | None | 1969-12-31T15:59:59-0800 |  |
| 6132955194526 | Conversion Campaign | PAUSED | PAUSED | CONVERSIONS |  | None | 1969-12-31T15:59:59-0800 |  |
| 6131945981926 | PGC--Conversions--TOF--Video | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-12-06T08:36:19-0800 |  |
| 6130173226526 | PGC--MOF--Traffic--November | PAUSED | PAUSED | LINK_CLICKS |  | None | 2018-11-15T17:11:48-0800 |  |
| 6130135022526 | PGC--TOF--Conversions--November | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-11-15T08:03:12-0800 |  |
| 6126921318926 | PGC--PPE--LLA | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2018-10-08T11:38:16-0700 |  |
| 6124468554126 | PGC--BOF | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-09-10T14:39:10-0700 |  |
| 6123688702126 | PGC--BOF--RHC AddToCart | PAUSED | PAUSED | LINK_CLICKS |  | None | 2018-09-01T08:36:23-0700 |  |
| 6123514683526 | Video views | PAUSED | PAUSED | VIDEO_VIEWS |  | None | 2018-08-30T08:03:11-0700 |  |
| 6122401541926 | PGC--MOF--Conversions | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-08-16T14:01:04-0700 |  |
| 6121900240126 | PGC--Broad Audience--Conversions | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-08-10T14:00:08-0700 |  |
| 6121416373326 | Retargeting Wooden Ring | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-08-05T10:42:10-0700 |  |
| 6121415342126 | PGC: TOF--Conversions | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-08-05T10:20:44-0700 |  |
| 6121353619126 | PGC: TOF-LLA--PPE | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2018-08-04T11:21:10-0700 | 2018-09-25T00:00:00-0700 |
| 6121349584526 | PGC: TOF-Broad Targeting--PPE | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2018-08-04T10:02:12-0700 | 2018-09-25T00:00:00-0700 |
| 6121349071526 | PGC: TOF--Broad Targeting-Conversions | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-08-04T09:58:23-0700 |  |
| 6115227683926 | Post: "Aydins Jewelry Real Wood Tungsten Rings.       👉🏻..." | PAUSED | PAUSED | VIDEO_VIEWS |  | None | 2018-05-24T21:52:27-0700 | 2018-05-31T21:52:22-0700 |
| 6115100082526 | Post: "Over 500 styles to choose the perfect wedding..." | PAUSED | PAUSED | VIDEO_VIEWS |  | None | 2018-05-23T12:12:20-0700 | 2018-06-05T12:12:20-0700 |
| 6106067518326 | [02/06/2018] Promoting http://etsy.me/2ErvdZq | PAUSED | PAUSED | CONVERSIONS |  | None | 2018-02-06T17:57:53-0800 | 2018-02-16T17:57:53-0800 |
| 6082582978126 | Split Test - Fashion Watch Express | PAUSED | PAUSED | LINK_CLICKS |  | None | 2017-03-16T13:05:56-0700 | 2017-03-30T13:05:56-0700 |
| 6074521522726 | Post: "Give a gift your loved ones will cherish...." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-12-21T12:42:43-0800 | 2016-12-24T12:42:42-0800 |
| 6074328202926 | Post: "Stop giving boring gifts. Personalize it with a..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-12-19T08:40:14-0800 | 2016-12-23T08:40:14-0800 |
| 6073546611326 | Post: "Personalized Name Necklaces - Order a custom made..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-12-11T09:49:39-0800 | 2016-12-16T09:49:39-0800 |
| 6072647374526 | Post: "Personalized Name Rings - Order a custom made..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-12-03T15:45:20-0800 | 2016-12-07T15:45:19-0800 |
| 6072631842926 | Post: "Need ideas for Christmas Gifts, order a custom..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-12-03T09:51:41-0800 | 2016-12-05T09:51:40-0800 |
| 6072546415126 | Post: "Personalized Men's Wedding Band" | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-12-02T14:33:05-0800 | 2016-12-06T09:58:23-0800 |
| 6063343746326 | Post: "Personalized Couples Tungsten Ring" | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-09-03T12:25:13-0700 | 2016-09-06T06:04:19-0700 |
| 6057681299926 | Post: "Personalized Your YETI cup Today!!! at Aydins..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-07-18T12:36:08-0700 | 2016-07-19T13:25:00-0700 |
| 6053562429726 | Post: "Personalized Your Father's Day Gift Today!!! at..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-06-17T11:07:47-0700 | 2016-06-20T07:38:06-0700 |
| 6048444876326 | Post: "Personalized Tungsten Ring Engraving Order Yours..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-04-27T10:40:13-0700 | 2016-05-02T06:33:42-0700 |
| 6048382585926 | Post: "Personalized Sterling Silver Bar Necklace Only..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-04-26T15:25:05-0700 | 2016-04-29T15:25:05-0700 |
| 6048121213926 | Post: "Personalized Flat Top Rings.. Bring your own..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-04-23T18:05:32-0700 | 2016-04-26T18:05:32-0700 |
| 6046705751126 | Post: "Personalized Name Tags.. Bring your own design..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-04-09T14:30:09-0700 | 2016-04-11T14:30:09-0700 |
| 6046076933926 | Post: "Personalized photo frame.. Bring your own design..." | PAUSED | PAUSED | POST_ENGAGEMENT |  | None | 2016-04-03T14:00:27-0700 | 2016-04-05T07:08:48-0700 |
| 6010948795326 | My Ads | PAUSED | PAUSED | NONE |  | None | 2008-09-20T19:57:44-0700 |  |

### Active and spend-bearing ad sets

| ID | Name | Campaign | Status | Effective | Opt event | Billing | Bid | Budget | Targeting summary | 30d spend | 30d freq | 30d CTR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52566196699530 | 1/Cut/12.14/Radiate | 6929192369326 | ACTIVE | ACTIVE | PURCHASE | IMPRESSIONS | campaign default |  | geo US; age 18-65; auto_audience None; not explicit in name | 4.46 | 1.706349 | 2.790698 |
| 52566193429930 | New Sales Ad Set | 52566193429730 | ACTIVE | CAMPAIGN_PAUSED | PURCHASE | IMPRESSIONS | campaign default |  | geo US; age 18-65; auto_audience 0; not explicit in name | 501.32 | 9.125831 | 2.044851 |
| 52566187275330 | 1/Cut/12.14/Legend - Copy | 6929192369326 | PAUSED | PAUSED | PURCHASE | IMPRESSIONS | campaign default |  | geo US; age 18-65; auto_audience None; not explicit in name | 34.07 | 2.711111 | 5.819672 |
| 6957175130726 | 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | 6929192369326 | PAUSED | PAUSED | PURCHASE | IMPRESSIONS | campaign default |  | geo US; age 18-65; auto_audience 1; manual mobile naming | 672.56 | 2.5331 | 1.127783 |
| 6929192369126 | 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | 6929192369326 | ACTIVE | ACTIVE | PURCHASE | IMPRESSIONS | campaign default |  | geo US; age 18-65; auto_audience 1; manual mobile naming | 350.17 | 2.094701 | 2.343928 |

### Ad inventory, active and 30-day spend-bearing

| ID | Name | Ad set | Status | Effective | Creative ID | 30d spend | 14d spend | 7d spend | 30d CTR | 30d freq | Purchase ROAS field |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52670541457530 | UGC v4 ASHER carbon fiber couples | 6929192369126 | ACTIVE | PENDING_REVIEW | 1205667488289123 | 0 | 0 | 0 |  |  |  |
| 52670541452730 | UGC v2 DEVITO coffee cup | 6929192369126 | ACTIVE | PENDING_REVIEW | 980632814586363 | 0 | 0 | 0 |  |  |  |
| 52658116819130 | Forever Rings Enter the Chat | 52566187275330 | ACTIVE | ADSET_PAUSED | 2775088679515941 | 0.21 | 0 | 0 | 0 | 1.142857 |  |
| 52658116818930 | Not Your Dad's Gold Band | 52566187275330 | ACTIVE | ADSET_PAUSED | 2550368768761209 | 33.86 | 1.66 | 0 | 5.858086 | 2.705357 |  |
| 52566196790330 | Built For Real Life | 52566196699530 | ACTIVE | ACTIVE | 800713472623553 | 1.29 | 0.98 | 0.86 | 0 | 1.405797 |  |
| 52566196771130 | Gold Looks Without Gold Cost | 52566196699530 | ACTIVE | ACTIVE | 922808770667572 | 3.17 | 3.17 | 0.16 | 5.084746 | 1.761194 |  |
| 6950313392326 | 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US/Single image/3 | 6929192369126 | ACTIVE | ACTIVE | 721157503750715 | 350.17 | 132.17 | 43.7 | 2.343928 | 2.094701 | [{'action_type': 'omni_purchase', 'value': '4.88854'}] |
| 6957175131126 | 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US/Single image/1 | 6957175130726 | ACTIVE | ADSET_PAUSED | 1075550524511498 | 33.59 | 2.35 | 0 | 0.823045 | 1.571642 | [{'action_type': 'omni_purchase', 'value': '4.025007'}] |
| 6957190217726 | 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US/Single image/4 | 6957175130726 | ACTIVE | ADSET_PAUSED | 1911308339705624 | 526.64 | 112.88 | 0 | 0.974698 | 2.376623 | [{'action_type': 'omni_purchase', 'value': '1.957827'}] |
| 6957175130526 | 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US/Single image/2 | 6957175130726 | ACTIVE | ADSET_PAUSED | 4071579113084089 | 5.43 | 2.14 | 0 | 0.601202 | 1.253769 |  |
| 6957175130926 | 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US/Single image/3 | 6957175130726 | ACTIVE | ADSET_PAUSED | 1976749899765059 | 106.9 | 1.03 | 0 | 2.221668 | 1.857209 |  |
| 52566193429530 | Shopify Dynamic Facebook Ads Product Set - Sales | 52566193429930 | ACTIVE | CAMPAIGN_PAUSED | 1181630036882136 | 501.32 | 97.05 | 0 | 2.044851 | 9.125831 | [{'action_type': 'omni_purchase', 'value': '1.900822'}] |
| 52566187275530 | Forever Rings Enter the Chat | 52566187275330 | ACTIVE | ADSET_PAUSED | 1390649136029161 | 0.21 | 0 | 0 | 0 | 1.142857 |  |
| 52566187275730 | Not Your Dad's Gold Band | 52566187275330 | ACTIVE | ADSET_PAUSED | 875858204786541 | 33.86 | 1.66 | 0 | 5.858086 | 2.705357 |  |
| 52566185141930 | Forever Rings Enter the Chat | 52566183452130 | PAUSED | PAUSED | 1288678446398827 | 0.21 | 0 | 0 | 0 | 1.142857 |  |
| 52566185151330 | Not Your Dad's Gold Band | 52566183452130 | PAUSED | PAUSED | 835420719116903 | 33.86 | 1.66 | 0 | 5.858086 | 2.705357 |  |
| 52518283130130 | 2/AY/9.8/New Gemini Images/ - 50 - /*/All mobile devices/1 BS/US/Carousel/2 | 52518283129130 | ACTIVE | ADSET_PAUSED | 1482697346359543 | 0 | 0 | 0 |  |  |  |
| 52518283132130 | 2/AY/9.8/New Gemini Images/ - 50 - /*/All mobile devices/1 BS/US/Carousel/1 | 52518283129130 | ACTIVE | ADSET_PAUSED | 1282101450083974 | 0 | 0 | 0 |  |  |  |
| 6716392056926 | 51/FB/1.10/Fingerprint/Review/*/All mobile devices/1/US/Single image/1 | 6716392057326 | ACTIVE | ADSET_PAUSED | 6716398994126 | 0 | 0 | 0 |  |  |  |
| 6716398746526 | 51/FB/1.10/Fingerprint/Review/*/All mobile devices/1/US/Single image/2 | 6716392057326 | ACTIVE | ADSET_PAUSED | 6716398999526 | 0 | 0 | 0 |  |  |  |
| 6716013473326 | 50/FB/30.9/Fingerprint//*/All mobile devices/2/US/Single image/2 | 6716013473526 | ACTIVE | ADSET_PAUSED | 6713497286726 | 0 | 0 | 0 |  |  |  |
| 6712801874926 | 47/FB/17.9/4 square//*/All mobile devices/1/US/Single image/3 | 6712801875326 | ACTIVE | ADSET_PAUSED | 6712565306526 | 0 | 0 | 0 |  |  |  |
| 6712801874526 | 47/FB/17.9/4 square//*/All mobile devices/1/US/Single image/* | 6712801875326 | ACTIVE | ADSET_PAUSED | 6712565309126 | 0 | 0 | 0 |  |  |  |
| 6712801875526 | 47/FB/17.9/4 square//*/All mobile devices/1/US/Single image/* | 6712801875326 | ACTIVE | ADSET_PAUSED | 6712565311726 | 0 | 0 | 0 |  |  |  |
| 6711954519726 | 45/FB/13.9/Tweet Review//*/All mobile devices/1/US/Single image/4 | 6711953264726 | ACTIVE | ADSET_PAUSED | 6711954963326 | 0 | 0 | 0 |  |  |  |
| 6711953265326 | 45/FB/13.9/Tweet Review//*/All mobile devices/1/US/Single image/3 | 6711953264726 | ACTIVE | ADSET_PAUSED | 6711954968526 | 0 | 0 | 0 |  |  |  |
| 6711953264926 | 45/FB/13.9/Tweet Review//*/All mobile devices/1/US/Single image/1 | 6711953264726 | ACTIVE | ADSET_PAUSED | 6711955000326 | 0 | 0 | 0 |  |  |  |
| 6711953265126 | 45/FB/13.9/Tweet Review//*/All mobile devices/1/US/Single image/2 | 6711953264726 | ACTIVE | ADSET_PAUSED | 6711954965926 | 0 | 0 | 0 |  |  |  |
| 6711538030926 | 44/FB/12.9/GG search/4 Img/*/All mobile devices/1/US/Single image/3 | 6711537371126 | ACTIVE | ADSET_PAUSED | 6711538365326 | 0 | 0 | 0 |  |  |  |
| 6711538030726 | 44/FB/12.9/GG search/4 Img/*/All mobile devices/1/US/Single image/2 | 6711537371126 | ACTIVE | ADSET_PAUSED | 6711538362726 | 0 | 0 | 0 |  |  |  |
| 6711537370526 | 44/FB/12.9/GG search/4 Img/*/All mobile devices/1/US/Single image/1 | 6711537371126 | ACTIVE | ADSET_PAUSED | 6711538370526 | 0 | 0 | 0 |  |  |  |
| 6710494386726 | 43/FB/9.9/Phone Review//*/All mobile devices/2/US/Single image/3 | 6710494386326 | ACTIVE | ADSET_PAUSED | 6710494438326 | 0 | 0 | 0 |  |  |  |
| 6710494386526 | 43/FB/9.9/Phone Review//*/All mobile devices/2/US/Single image/* | 6710494386326 | ACTIVE | ADSET_PAUSED | 6710494425126 | 0 | 0 | 0 |  |  |  |
| 6710494386126 | 43/FB/9.9/Phone Review//*/All mobile devices/2/US/Single image/1 | 6710494386326 | ACTIVE | ADSET_PAUSED | 6710494426126 | 0 | 0 | 0 |  |  |  |
| 6709594270926 | 42/FB/5.9/Catalog/Dynamic/*/All mobile devices/2/US/ACO/1 | 6709594270726 | ACTIVE | ADSET_PAUSED | 6707710483926 | 0 | 0 | 0 |  |  |  |
| 6709585430126 | 40/FB/5.9/4 Square/Plain Background/*/All mobile devices/2/US/Single image/* | 6709585429926 | ACTIVE | ADSET_PAUSED | 6697495362326 | 0 | 0 | 0 |  |  |  |
| 6709585430326 | 40/FB/5.9/4 Square/Plain Background/*/All mobile devices/2/US/Single image/2 | 6709585429926 | ACTIVE | ADSET_PAUSED | 6697495359726 | 0 | 0 | 0 |  |  |  |
| 6709579510326 | 39/FB/5.9/Tweet Review//*/All mobile devices/2/US/Single image/1 | 6709579510926 | ACTIVE | ADSET_PAUSED | 6708491321126 | 0 | 0 | 0 |  |  |  |
| 6707711101926 | 38/FB/29.8/Catalog/Broad/*/All mobile devices/3/US/ACO/1 | 6707711102726 | ACTIVE | ADSET_PAUSED | 6707711667326 | 0 | 0 | 0 |  |  |  |
| 6707711101726 | 38/FB/29.8/Catalog/Broad/*/All mobile devices/1/US/ACO/1 | 6707711101326 | ACTIVE | ADSET_PAUSED | 6707711662526 | 0 | 0 | 0 |  |  |  |
| 6707711102326 | 38/FB/29.8/Catalog/Broad/*/All mobile devices/4/US/ACO/1 | 6707711102926 | ACTIVE | ADSET_PAUSED | 6707711662326 | 0 | 0 | 0 |  |  |  |
| 6707392749126 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/03 | 6707392749326 | ACTIVE | ADSET_PAUSED | 6697495397526 | 0 | 0 | 0 |  |  |  |
| 6707392749726 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/01 | 6707392749326 | ACTIVE | ADSET_PAUSED | 6697495360926 | 0 | 0 | 0 |  |  |  |
| 6707392749926 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/04 | 6707392749326 | ACTIVE | ADSET_PAUSED | 6697495361726 | 0 | 0 | 0 |  |  |  |
| 6707392749526 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/02 | 6707392749326 | ACTIVE | ADSET_PAUSED | 6697495359326 | 0 | 0 | 0 |  |  |  |
| 6706532736526 | 36/FB/25.8/4 Square/Color Background/*/All mobile devices/2/US/Single image/2 | 6706532734926 | ACTIVE | ADSET_PAUSED | 6697495359726 | 0 | 0 | 0 |  |  |  |
| 6706532736326 | 36/FB/25.8/4 Square/Color Background/*/All mobile devices/2/US/Single image/1 | 6706532734926 | ACTIVE | ADSET_PAUSED | 6697495362326 | 0 | 0 | 0 |  |  |  |
| 6705945952926 | 35/FB/22.8/Tweet Review//*/All mobile devices/2/US/Single image/2 | 6705945951726 | ACTIVE | ADSET_PAUSED | 6705946359726 | 0 | 0 | 0 |  |  |  |
| 6705945953126 | 35/FB/22.8/Tweet Review//*/All mobile devices/2/US/Single image/3 | 6705945951726 | ACTIVE | ADSET_PAUSED | 6705946363726 | 0 | 0 | 0 |  |  |  |
| 6705945953326 | 35/FB/22.8/Tweet Review//*/All mobile devices/2/US/Single image/1 | 6705945951726 | ACTIVE | ADSET_PAUSED | 6705946359326 | 0 | 0 | 0 |  |  |  |
| 6704285030526 | 34/FB/16.8/Unique Inlay//*/All mobile devices/2/US/Single image/1 | 6704285030326 | ACTIVE | ADSET_PAUSED | 6704285159326 | 0 | 0 | 0 |  |  |  |
| 6704285031126 | 34/FB/16.8/Unique Inlay//*/All mobile devices/1/US/Single image/1 | 6704285030326 | ACTIVE | ADSET_PAUSED | 6704285166326 | 0 | 0 | 0 |  |  |  |
| 6704285030726 | 34/FB/16.8/Unique Inlay//*/All mobile devices/2/US/Single image/* | 6704285030326 | ACTIVE | ADSET_PAUSED | 6704285168526 | 0 | 0 | 0 |  |  |  |
| 6704285030926 | 34/FB/16.8/Unique Inlay//*/All mobile devices/2/US/Single image/4 | 6704285030326 | ACTIVE | ADSET_PAUSED | 6704285156926 | 0 | 0 | 0 |  |  |  |
| 6703722934926 | 33/FB/14.8/The best ring//*/All mobile devices/1/US/Single image/4 | 6703721629126 | ACTIVE | ADSET_PAUSED | 6703723534926 | 0 | 0 | 0 |  |  |  |
| 6703722935326 | 33/FB/14.8/The best ring//*/All mobile devices/1/US/Single image/3 | 6703721629126 | ACTIVE | ADSET_PAUSED | 6703723525926 | 0 | 0 | 0 |  |  |  |
| 6703722935126 | 33/FB/14.8/The best ring//*/All mobile devices/1/US/Single image/2 | 6703721629126 | ACTIVE | ADSET_PAUSED | 6703723520326 | 0 | 0 | 0 |  |  |  |
| 6703721628526 | 33/FB/14.8/The best ring//*/All mobile devices/1/US/Single image/1 | 6703721629126 | ACTIVE | ADSET_PAUSED | 6703723535326 | 0 | 0 | 0 |  |  |  |
| 6703155589526 | 32/FB/12.8/Image/Collection/*/All mobile devices/2/US/Single image/2 | 6703155589126 | ACTIVE | ADSET_PAUSED | 6703436688926 | 0 | 0 | 0 |  |  |  |
| 6703155589326 | 32/FB/12.8/Image/Collection/*/All mobile devices/2/US/Single image/* | 6703155589126 | ACTIVE | ADSET_PAUSED | 6703436694726 | 0 | 0 | 0 |  |  |  |
| 6701471640526 | 31/FB/5.8/The best ring(b)//*/All mobile devices/1/US/Single image/2 | 6701471639326 | ACTIVE | ADSET_PAUSED | 6701472530726 | 0 | 0 | 0 |  |  |  |
| 6701471640326 | 31/FB/5.8/The best ring(b)//*/All mobile devices/1/US/Single image/1 | 6701471639326 | ACTIVE | ADSET_PAUSED | 6701472523526 | 0 | 0 | 0 |  |  |  |
| 6701471314126 | 30/FB/5.8/The best ring(a)//*/All mobile devices/2/US/Single image/1 | 6701471314326 | ACTIVE | ADSET_PAUSED | 6701471492726 | 0 | 0 | 0 |  |  |  |
| 6701471313926 | 30/FB/5.8/The best ring(a)//*/All mobile devices/2/US/Single image/2 | 6701471314326 | ACTIVE | ADSET_PAUSED | 6701471492126 | 0 | 0 | 0 |  |  |  |
| 6700891392526 | 29/FB/2.8/4 Square/Color Background/*/All mobile devices/2/US/Single image/4 | 6700891392726 | ACTIVE | ADSET_PAUSED | 6697495359726 | 0 | 0 | 0 |  |  |  |
| 6700891393126 | 29/FB/2.8/4 Square/Color Background/*/All mobile devices/2/US/Single image/2 | 6700891392726 | ACTIVE | ADSET_PAUSED | 6697495362326 | 0 | 0 | 0 |  |  |  |
| 6700891393326 | 29/FB/2.8/4 Square/Color Background/*/All mobile devices/2/US/Single image/3 | 6700891392726 | ACTIVE | ADSET_PAUSED | 6697495395126 | 0 | 0 | 0 |  |  |  |
| 6700891392926 | 29/FB/2.8/4 Square/Color Background/*/All mobile devices/2/US/Single image/1 | 6700891392726 | ACTIVE | ADSET_PAUSED | 6697495360326 | 0 | 0 | 0 |  |  |  |
| 6700082952126 | 28/FB/30.7/Single Image/Minimal Background/*/All mobile devices/1/US/Single image/1 | 6700082951126 | ACTIVE | ADSET_PAUSED | 6700085307926 | 0 | 0 | 0 |  |  |  |
| 6700082952326 | 28/FB/30.7/Single Image/Minimal Background/*/All mobile devices/1/US/Single image/2 | 6700082951126 | ACTIVE | ADSET_PAUSED | 6700085309526 | 0 | 0 | 0 |  |  |  |
| 6700082952526 | 28/FB/30.7/Single Image/Minimal Background/*/All mobile devices/1/US/Single image/3 | 6700082951126 | ACTIVE | ADSET_PAUSED | 6700085307526 | 0 | 0 | 0 |  |  |  |
| 6699846022526 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/02 | 6699846023726 | ACTIVE | ADSET_PAUSED | 6697495359326 | 0 | 0 | 0 |  |  |  |
| 6699846022726 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/03 | 6699846023726 | ACTIVE | ADSET_PAUSED | 6697495397526 | 0 | 0 | 0 |  |  |  |
| 6699846022126 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/04 | 6699846023726 | ACTIVE | ADSET_PAUSED | 6697495361726 | 0 | 0 | 0 |  |  |  |
| 6699846022326 | 27/FB/29.07/4 Square/Color Background /*/All mobile devices/01/US/Single image/01 | 6699846023726 | ACTIVE | ADSET_PAUSED | 6697495360926 | 0 | 0 | 0 |  |  |  |
| 6699745725326 | 25/FB/28.7/Single Image/Minimal Background /*/All mobile devices/1/US/Single image/2 | 6699745724126 | ACTIVE | ADSET_PAUSED | 6699746368126 | 0 | 0 | 0 |  |  |  |
| 6699745725526 | 25/FB/28.7/Single Image/Minimal Background /*/All mobile devices/1/US/Single image/3 | 6699745724126 | ACTIVE | ADSET_PAUSED | 6699746368726 | 0 | 0 | 0 |  |  |  |
| 6699745725126 | 25/FB/28.7/Single Image/Minimal Background /*/All mobile devices/1/US/Single image/1 | 6699745724126 | ACTIVE | ADSET_PAUSED | 6699746367326 | 0 | 0 | 0 |  |  |  |
| 6698723846126 | 24/FB/23.7/4 square/Minimal Background/*/All mobile devices/2/US/Single image/3 | 6698723845726 | ACTIVE | ADSET_PAUSED | 6698723871126 | 0 | 0 | 0 |  |  |  |
| 6698723845926 | 24/FB/23.7/4 square/Minimal Background/*/All mobile devices/2/US/Single image/2 | 6698723845726 | ACTIVE | ADSET_PAUSED | 6698723871726 | 0 | 0 | 0 |  |  |  |
| 6698723845526 | 24/FB/23.7/4 square/Minimal Background/*/All mobile devices/2/US/Single image/1 | 6698723845726 | ACTIVE | ADSET_PAUSED | 6698723870526 | 0 | 0 | 0 |  |  |  |
| 6698438338926 | 23/FB/22.7/Review/Minimal Background/*/All mobile devices/1/US/Single image/3 | 6698438340526 | ACTIVE | ADSET_PAUSED | 6698440867326 | 0 | 0 | 0 |  |  |  |
| 6698438339326 | 23/FB/22.7/Review/Minimal Background/*/All mobile devices/1/US/Single image/2 | 6698438340526 | ACTIVE | ADSET_PAUSED | 6698440864726 | 0 | 0 | 0 |  |  |  |
| 6698438339126 | 23/FB/22.7/Review/Minimal Background/*/All mobile devices/1/US/Single image/1 | 6698438340526 | ACTIVE | ADSET_PAUSED | 6698440864126 | 0 | 0 | 0 |  |  |  |
| 6697942622926 | 22/FB/19.7/Carousel/Wood background/*/All mobile devices/1/US/Carousel/1 | 6697942624326 | ACTIVE | ADSET_PAUSED | 6697946345326 | 0 | 0 | 0 |  |  |  |
| 6697946241526 | 22/FB/19.7/Carousel/Wood background/*/All mobile devices/1/US/Carousel/2 | 6697942624326 | ACTIVE | ADSET_PAUSED | 6697946343526 | 0 | 0 | 0 |  |  |  |
| 6697495216126 | 19/FB/17.7/4 Square/Color Background/*/All mobile devices/2/US/Single image/1 | 6697495216526 | ACTIVE | ADSET_PAUSED | 6697495359726 | 0 | 0 | 0 |  |  |  |
| 6697495216726 | 19/FB/17.7/4 Square/Color Background/*/All mobile devices/2/US/Single image/3 | 6697495216526 | ACTIVE | ADSET_PAUSED | 6697495362326 | 0 | 0 | 0 |  |  |  |
| 6697495216326 | 19/FB/17.7/4 Square/Color Background/*/All mobile devices/2/US/Single image/2 | 6697495216526 | ACTIVE | ADSET_PAUSED | 6697495395126 | 0 | 0 | 0 |  |  |  |
| 6697495216926 | 19/FB/17.7/4 Square/Color Background/*/All mobile devices/2/US/Single image/4 | 6697495216526 | ACTIVE | ADSET_PAUSED | 6697495360326 | 0 | 0 | 0 |  |  |  |
| 6697240378926 | 18/FB/16.7/Craft your own ring//*/All mobile devices/2/US/Single image/2 | 6697240379526 | ACTIVE | ADSET_PAUSED | 6697240404526 | 0 | 0 | 0 |  |  |  |
| 6697240379126 | 18/FB/16.7/Craft your own ring//*/All mobile devices/2/US/Single image/3 | 6697240379526 | ACTIVE | ADSET_PAUSED | 6697240405926 | 0 | 0 | 0 |  |  |  |
| 6697240379326 | 18/FB/16.7/Craft your own ring//*/All mobile devices/2/US/Single image/1 | 6697240379526 | ACTIVE | ADSET_PAUSED | 6697240405126 | 0 | 0 | 0 |  |  |  |
| 6696536838726 | 16/FB/12.7/Web Review/Center/*/All mobile devices/2/US/Single image/1 | 6696536838926 | ACTIVE | ADSET_PAUSED | 6696536859926 | 0 | 0 | 0 |  |  |  |
| 6696538888326 | 17/FB/12.7/Web Review/Split/*/All mobile devices/1/US/Single image/* | 6696538887726 | ACTIVE | ADSET_PAUSED | 6696538949326 | 0 | 0 | 0 |  |  |  |
| 6696537990126 | 17/FB/12.7/Web Review/Split/*/All mobile devices/2/US/Single image/* | 6696537989326 | ACTIVE | ADSET_PAUSED | 6696538950326 | 0 | 0 | 0 |  |  |  |
| 6696538888126 | 17/FB/12.7/Web Review/Split/*/All mobile devices/1/US/Single image/2 | 6696538887726 | ACTIVE | ADSET_PAUSED | 6696538948526 | 0 | 0 | 0 |  |  |  |
| 6696537988726 | 17/FB/12.7/Web Review/Split/*/All mobile devices/2/US/Single image/3 | 6696537989326 | ACTIVE | ADSET_PAUSED | 6696538949526 | 0 | 0 | 0 |  |  |  |
| 6696537989726 | 17/FB/12.7/Web Review/Split/*/All mobile devices/2/US/Single image/1 | 6696537989326 | ACTIVE | ADSET_PAUSED | 6696538950926 | 0 | 0 | 0 |  |  |  |
| 6696538887926 | 17/FB/12.7/Web Review/Split/*/All mobile devices/1/US/Single image/3 | 6696538887726 | ACTIVE | ADSET_PAUSED | 6696538951526 | 0 | 0 | 0 |  |  |  |
| 6696536838526 | 16/FB/12.7/Web Review/Center/*/All mobile devices/2/US/Single image/2 | 6696536838926 | ACTIVE | ADSET_PAUSED | 6696536858726 | 0 | 0 | 0 |  |  |  |
| 6696536839126 | 16/FB/12.7/Web Review/Center/*/All mobile devices/2/US/Single image/3 | 6696536838926 | ACTIVE | ADSET_PAUSED | 6696536877726 | 0 | 0 | 0 |  |  |  |
| 6696235653926 | 15/FB/11.7/Review/1 product/*/All mobile devices/2/US/Single image/1 | 6696235653726 | ACTIVE | ADSET_PAUSED | 6696235979726 | 0 | 0 | 0 |  |  |  |
| 6696235653526 | 15/FB/11.7/Review/1 product/*/All mobile devices/2/US/Single image/2 | 6696235653726 | ACTIVE | ADSET_PAUSED | 6696236027726 | 0 | 0 | 0 |  |  |  |
| 6694374363126 | 13/FB/3.7/GIF//*/All mobile devices/1/US/Single video/1 | 6694374362926 | ACTIVE | ADSET_PAUSED | 6694374924526 | 0 | 0 | 0 |  |  |  |
| 6694367562926 | 12/FB/3.7/Transition Hook//*/All mobile devices/1/US/Single video/1 | 6694367563126 | ACTIVE | ADSET_PAUSED | 6694374163926 | 0 | 0 | 0 |  |  |  |
| 6693257059726 | 11/FB/28.6/Testimonial//*/All mobile devices/1/US/Single video/1 | 6693257059926 | ACTIVE | ADSET_PAUSED | 6693257499326 | 0 | 0 | 0 |  |  |  |
| 6693256599726 | 10/FB/28.6/Scratch/PAS /*/All mobile devices/1/US/Single video/1 | 6693256599526 | ACTIVE | ADSET_PAUSED | 6693256929526 | 0 | 0 | 0 |  |  |  |
| 6691010290526 | 8/FB/16.06/Type 4 Img Best Sellers//*/All mobile devices/01/US/Single image/4 Type Img Best Seller AD 03 | 6691003193526 | ACTIVE | ADSET_PAUSED | 6691010296526 | 0 | 0 | 0 |  |  |  |
| 6691010302726 | 8/FB/16.06/Type 4 Img Best Sellers//*/All mobile devices/01/US/Single image/4 Type Img Best Seller AD 04 | 6691003193526 | ACTIVE | ADSET_PAUSED | 6691010344126 | 0 | 0 | 0 |  |  |  |
| 6691007226726 | 8/FB/16.06/Type 4 Img Best Sellers//*/All mobile devices/01/US/Single image/4 Type Img Best Seller AD 02 | 6691003193526 | ACTIVE | ADSET_PAUSED | 6691007257726 | 0 | 0 | 0 |  |  |  |
| 6691003193326 | 8/FB/16.06/Type 4 Img Best Sellers//*/All mobile devices/01/US/Single image/4 Type Img Best Seller AD 01 | 6691003193526 | ACTIVE | ADSET_PAUSED | 6691007222326 | 0 | 0 | 0 |  |  |  |
| 6690965028526 | 7/FB/16.6/Compare//*/All mobile devices/2/US/Single image/1 | 6690965028726 | ACTIVE | ADSET_PAUSED | 6690965139526 | 0 | 0 | 0 |  |  |  |
| 6690955896726 | 6/FB/15.6/Test Static//*/All mobile devices/1/US/Single image/1 | 6690955898326 | ACTIVE | ADSET_PAUSED | 6690958969726 | 0 | 0 | 0 |  |  |  |
| 6690957039926 | 6/FB/15.6/Test Static//*/All mobile devices/1/US/Single image/1B | 6690955898326 | ACTIVE | ADSET_PAUSED | 6690958954726 | 0 | 0 | 0 |  |  |  |
| 6690957377126 | 6/FB/15.6/Test Static//*/All mobile devices/1/US/ACO/2B | 6690955898326 | ACTIVE | ADSET_PAUSED | 6690958950326 | 0 | 0 | 0 |  |  |  |
| 6690955897326 | 6/FB/15.6/Test Static//*/All mobile devices/1/US/ACO/2 | 6690955898326 | ACTIVE | ADSET_PAUSED | 6690958974926 | 0 | 0 | 0 |  |  |  |
| 6689496789326 | 05/FB/Testimonial//09.06/*/All mobile devices/02/US/Single video/Ad 1 | 6689496789526 | ACTIVE | ADSET_PAUSED | 6689496783526 | 0 | 0 | 0 |  |  |  |
| 6689174157926 | 04/FB/Quote//7.6/*/All mobile devices/2/US/Single image/3 | 6689174157326 | ACTIVE | ADSET_PAUSED | 6689175736926 | 0 | 0 | 0 |  |  |  |
| 6689174159126 | 04/FB/Quote//7.6/*/All mobile devices/2/US/Single image/2 | 6689174157326 | ACTIVE | ADSET_PAUSED | 6689175756926 | 0 | 0 | 0 |  |  |  |
| 6689174158926 | 04/FB/Quote//7.6/*/All mobile devices/2/US/Single image/4 | 6689174157326 | ACTIVE | ADSET_PAUSED | 6689175708526 | 0 | 0 | 0 |  |  |  |
| 6689173680326 | 03/FB/3 Benefits//7.6/*/All mobile devices/2/US/Single image/2 | 6689173680526 | ACTIVE | ADSET_PAUSED | 6689173866926 | 0 | 0 | 0 |  |  |  |
| 6689173680726 | 03/FB/3 Benefits//7.6/*/All mobile devices/2/US/Single image/4 | 6689173680526 | ACTIVE | ADSET_PAUSED | 6689173846326 | 0 | 0 | 0 |  |  |  |
| 6689173680926 | 03/FB/3 Benefits//7.6/*/All mobile devices/2/US/Single image/3 | 6689173680526 | ACTIVE | ADSET_PAUSED | 6689173843526 | 0 | 0 | 0 |  |  |  |
| 6687267645926 | 01/FB/All/Catalog/30.05/Weddings (weddings)+Wedding ring (weddings)+Ring (jewellery)+Engagement (weddings)/All mobile devices/02/US/ACO/01 | 6687267645726 | ACTIVE | ADSET_PAUSED | 6687267830926 | 0 | 0 | 0 |  |  |  |
| 6687264655126 | 01/FB/All/Catalog/30.05/*/All mobile devices/01/US/ACO/01 | 6687264653926 | ACTIVE | ADSET_PAUSED | 6687267831526 | 0 | 0 | 0 |  |  |  |
| 6291242357326 | **LP - Prospecting - CS - Jewelry Interest - DPA - V1 | 6291242357526 | ACTIVE | ADSET_PAUSED | 6649083918326 | 0 | 0 | 0 |  |  |  |
| 6291242357126 | **LP - Prospecting - CS - Jewelry Interest - DPA - V2 | 6291242357526 | ACTIVE | ADSET_PAUSED | 6649083797526 | 0 | 0 | 0 |  |  |  |
| 6311403356126 | **LP - Static Remarketing - Conv - 3 Day - DPA - V2 | 6311403355526 | ACTIVE | ADSET_PAUSED | 6284237323326 | 0 | 0 | 0 |  |  |  |
| 6285117941726 | **LP - Static Remarketing - Conv - 7 Day - DPA - V2 | 6285117941926 | ACTIVE | ADSET_PAUSED | 6284237323326 | 0 | 0 | 0 |  |  |  |
| 6285119484926 | **LP - Mid-Funnel - Conv - IG/FB Ad/Post Engagers - 60 Day - Video - V1 | 6285119484326 | ACTIVE | ADSET_PAUSED | 6285120285726 | 0 | 0 | 0 |  |  |  |
| 6285119484726 | **LP - Mid-Funnel - Conv - IG/FB Ad/Post Engagers - 60 Day - Video - V2 | 6285119484326 | ACTIVE | ADSET_PAUSED | 6285119327926 | 0 | 0 | 0 |  |  |  |
| 6285119484126 | **LP - Mid-Funnel - Conv - IG/FB Ad/Post Engagers - 60 Day - DPA - V1 | 6285119484326 | ACTIVE | ADSET_PAUSED | 6284230128126 | 0 | 0 | 0 |  |  |  |
| 6285119484526 | **LP - Mid-Funnel - Conv - IG/FB Ad/Post Engagers - 60 Day - DPA - V2 | 6285119484326 | ACTIVE | ADSET_PAUSED | 6284230128326 | 0 | 0 | 0 |  |  |  |
| 6260667016726 | Fingerprint Rings - Copy | 6260666488526 | ACTIVE | ADSET_PAUSED | 6260667240126 | 0 | 0 | 0 |  |  |  |
| 6260666488926 | Fingerprint Rings | 6260666488526 | ACTIVE | ADSET_PAUSED | 6260667239326 | 0 | 0 | 0 |  |  |  |
| 6262546620326 | Wood inlay | 6262546619926 | ACTIVE | ADSET_PAUSED | 6262546915326 | 0 | 0 | 0 |  |  |  |
| 6262546620926 | Chairman | 6262546619926 | ACTIVE | ADSET_PAUSED | 6262546904326 | 0 | 0 | 0 |  |  |  |
| 6262546620526 | Color Collection | 6262546619926 | ACTIVE | ADSET_PAUSED | 6262546883726 | 0 | 0 | 0 |  |  |  |
| 6262546620726 | Grooved collection | 6262546619926 | ACTIVE | ADSET_PAUSED | 6262546902926 | 0 | 0 | 0 |  |  |  |
| 6262546619726 | Timeless | 6262546619926 | ACTIVE | ADSET_PAUSED | 6262546914526 | 0 | 0 | 0 |  |  |  |
| 6262546620126 | Inlay | 6262546619926 | ACTIVE | ADSET_PAUSED | 6262546884526 | 0 | 0 | 0 |  |  |  |
| 6255744768326 | Store collection Fingerprint Rings - Catalog sales | 6255744768526 | ACTIVE | ADSET_PAUSED | 6255890613926 | 0 | 0 | 0 |  |  |  |
| 6179684481126 | Default name - Messages | 6179684480926 | ACTIVE | ADSET_PAUSED | 6179687516726 | 0 | 0 | 0 |  |  |  |
| 6152985318926 | Promoting Website: http://Shopaydins.com/ | 6152985317926 | ACTIVE | ADSET_PAUSED | 6152985371726 | 0 | 0 | 0 |  |  |  |
| 6151838368926 | Default name - Messages | 6151838368326 | ACTIVE | ADSET_PAUSED | 6151838379326 | 0 | 0 | 0 |  |  |  |
| 6152214337126 | Default name - Messages | 6152214336926 | ACTIVE | ADSET_PAUSED | 6152214574526 | 0 | 0 | 0 |  |  |  |
| 6151236161926 | Front Banner Video | 6151236161526 | ACTIVE | ADSET_PAUSED | 6151249437126 | 0 | 0 | 0 |  |  |  |
| 6144748324526 | 3D Bar Necklace Conversion - Image - Copy 2 | 6144396009126 | ACTIVE | ADSET_PAUSED | 6144755366926 | 0 | 0 | 0 |  |  |  |
| 6144746626526 | 3D Bar Necklace Conversion - Image | 6144473303526 | ACTIVE | ADSET_PAUSED | 6144755366526 | 0 | 0 | 0 |  |  |  |
| 6144748338526 | 3D Bar Necklace Conversion - Image - Copy 3 | 6144392015326 | ACTIVE | ADSET_PAUSED | 6144755361126 | 0 | 0 | 0 |  |  |  |
| 6144748324126 | 3D Bar Necklace Conversion - Image - Copy | 6144396009326 | ACTIVE | ADSET_PAUSED | 6144755360926 | 0 | 0 | 0 |  |  |  |
| 6144473303326 | 3D Bar Necklace Conversion - Video | 6144473303526 | ACTIVE | ADSET_PAUSED | 6144474510926 | 0 | 0 | 0 |  |  |  |
| 6144396009726 | 3D Bar Necklace Conversion | 6144396009326 | ACTIVE | ADSET_PAUSED | 6144396873726 | 0 | 0 | 0 |  |  |  |
| 6144396099926 | 3D Bar Necklace Conversion | 6144396099726 | ACTIVE | ADSET_PAUSED | 6144396889326 | 0 | 0 | 0 |  |  |  |
| 6144392015726 | 3D Bar Necklace Conversion | 6144392015326 | ACTIVE | ADSET_PAUSED | 6144396872526 | 0 | 0 | 0 |  |  |  |
| 6144396009526 | 3D Bar Necklace Conversion | 6144396009126 | ACTIVE | ADSET_PAUSED | 6144396884326 | 0 | 0 | 0 |  |  |  |
| 6143362689526 | Personalized 3D Bar Necklace | 6143362688726 | ACTIVE | ADSET_PAUSED | 6143362700726 | 0 | 0 | 0 |  |  |  |

Full historical ad inventory is in the raw API export because 860 ads are not useful as a strategy table.

## 2. Audience inventory

- Saved audiences returned by API: 0
- Custom audiences returned by API: 0
- Website visitor, add-to-cart, initiate-checkout, purchaser, page engager, video-viewer, and lookalike audiences were not found via the ad account audience endpoints.
- Active prospecting currently appears broad US, age 18 to 65, purchase optimized, with automated audience expansion enabled on the winning ad set.
- Critical implication: purchaser exclusions and warm retargeting cannot be confirmed. Treat them as missing until built or proven elsewhere in Business Manager.

## 3. Placement and bid analysis

- Current campaign bid strategy: lowest cost without cap at campaign level.
- Active ad sets optimize for offsite conversions, promoted event PURCHASE, billing by impressions.
- Active winning ad set name indicates all mobile devices and US. Targeting object confirms US, broad age, purchase event.
- Publisher platform breakdown shows mobile-heavy delivery. Some network inventory shows very high CTR with no purchase value, which should be watched as low-quality traffic.

### 30-day publisher platform breakdown, spend-bearing rows

| Ad set | Platform | Spend | Impr | CTR | CPM | Freq | ROAS field | CPA field |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | facebook | 575.51 | 56146 | 0.92 | 10.25 | 2.42 | 5.25 | 31.97 |
| New Sales Ad Set | facebook | 368.82 | 14847 | 1.81 | 24.84 | 9.04 | 5.19 | 40.98 |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | facebook | 225.69 | 21482 | 0.91 | 10.51 | 2.03 | 22.75 | 18.81 |
| New Sales Ad Set | instagram | 117.99 | 4050 | 1.9 | 29.13 | 5.04 | 8.01 | 19.67 |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | instagram | 74.98 | 4090 | 1.2 | 18.33 | 2.63 | 6.4 | 24.99 |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | audience_network | 70.49 | 1517 | 26.24 | 46.47 | 6.62 | 0.0 | None |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | instagram | 53.24 | 3239 | 0.74 | 16.44 | 1.59 | 0.0 | None |
| 1/Cut/12.14/Legend - Copy | facebook | 22.61 | 911 | 2.41 | 24.82 | 2.29 | 0.0 | None |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | audience_network | 21.28 | 557 | 21.54 | 38.2 | 5.16 | 0.0 | None |
| New Sales Ad Set | audience_network | 13.84 | 285 | 15.79 | 48.57 | 2.91 | 0.0 | None |
| 1/Cut/12.14/Legend - Copy | audience_network | 7.49 | 227 | 21.15 | 33.0 | 5.97 | 0.0 | None |
| 1/Cut/12.14/Legend - Copy | instagram | 3.92 | 80 | 1.25 | 49.0 | 1.95 | 0.0 | None |
| 1/Cut/12.14/Radiate | facebook | 3.39 | 156 | 1.28 | 21.73 | 1.7 | 0.0 | None |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | threads | 0.74 | 125 | 0.0 | 5.92 | 1.11 | 0.0 | None |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | threads | 0.73 | 118 | 0.0 | 6.19 | 1.04 | 0.0 | None |
| New Sales Ad Set | threads | 0.66 | 37 | 2.7 | 17.84 | 1.23 | 0.0 | None |
| 1/Cut/12.14/Radiate | audience_network | 0.61 | 21 | 19.05 | 29.05 | 1.75 | 0.0 | None |
| 1/Cut/12.14/Radiate | instagram | 0.46 | 38 | 0.0 | 12.11 | 1.46 | 0.0 | None |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | unknown | 0.06 | 5 | 20.0 | 12.0 | 1.25 | 0.0 | None |
| 1/Cut/12.14/Legend - Copy | unknown | 0.05 | 2 | 0.0 | 25.0 | 1.0 | 0.0 | None |

### 30-day device breakdown, spend-bearing rows

| Ad set | Device | Spend | Impr | CTR | CPM | Freq | ROAS field | CPA field |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | iphone | 502.59 | 45733 | 0.87 | 10.99 | 2.38 | 6.09 | 27.92 |
| New Sales Ad Set | android_smartphone | 329.15 | 12548 | 2.41 | 26.23 | 9.45 | 4.17 | 54.86 |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | iphone | 210.05 | 17492 | 0.81 | 12.01 | 1.89 | 24.45 | 17.5 |
| New Sales Ad Set | iphone | 155.42 | 6184 | 1.33 | 25.13 | 8.76 | 9.57 | 17.27 |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | android_smartphone | 153.02 | 13568 | 1.86 | 11.28 | 2.72 | 2.86 | 51.01 |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | android_smartphone | 127.35 | 8128 | 5.17 | 15.67 | 2.47 | 0.0 | None |
| 1/Cut/12.14/Legend - Copy | iphone | 17.74 | 699 | 3.15 | 25.38 | 2.34 | 0.0 | None |
| 1/Cut/12.14/Legend - Copy | android_smartphone | 11.58 | 390 | 10.51 | 29.69 | 2.62 | 0.0 | None |
| New Sales Ad Set | desktop | 9.35 | 228 | 0.0 | 41.02 | 2.78 | 0.0 | None |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | android_tablet | 8.65 | 380 | 12.11 | 22.77 | 8.44 | 0.0 | None |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | desktop | 8.02 | 1009 | 0.4 | 7.95 | 2.5 | 0.0 | None |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | ipad | 6.58 | 451 | 3.33 | 14.59 | 2.41 | 0.0 | None |
| New Sales Ad Set | ipad | 3.6 | 154 | 0.65 | 23.38 | 6.7 | 0.0 | None |
| 1/Cut/12.14/Legend - Copy | desktop | 2.65 | 7 | 0.0 | 378.57 | 1.75 | 0.0 | None |
| New Sales Ad Set | android_tablet | 2.61 | 76 | 5.26 | 34.35 | 4.0 | 0.0 | None |
| 1/Cut/12.14/Radiate | android_smartphone | 2.52 | 73 | 8.22 | 34.52 | 1.49 | 0.0 | None |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | ipad | 2.45 | 203 | 2.46 | 12.07 | 1.56 | 0.0 | None |
| 1/AY/6.29/Gym Images/ - 30/*/All mobile devices/2/US | android_tablet | 2.18 | 129 | 13.95 | 16.9 | 3.69 | 0.0 | None |
| 1/Cut/12.14/Radiate | iphone | 1.79 | 125 | 0.0 | 14.32 | 1.79 | 0.0 | None |
| 1/AY/6.3/Couples engraved/ - 30/*/All mobile devices/1/US | desktop | 1.64 | 152 | 3.95 | 10.79 | 1.3 | 0.0 | None |

## 4. Pixel and event optimization

- Pixel ID: 1151493648281503.
- Active ad sets optimize for Purchase, which is correct for the current sales campaign because purchase volume exists and Aydins has a clear conversion objective.
- 7-day raw pixel event volume, not ad-attributed: Purchase 75, AddToCart 526, InitiateCheckout 304, ViewContent 137,970, AddPaymentInfo 69. These counts indicate the pixel is firing and has enough upper-funnel signal.
- Because of the billing blackout from 2026-05-25 to 2026-06-02, recent 7-day ad-attributed purchase signal is temporarily weak. Do not judge the new UGC ads until delivery stabilizes.

## 5. Exclusions audit

- Past purchaser exclusions from prospecting: not confirmed. API audience inventory returned 0 custom audiences.
- Recent engager exclusions from cold campaigns: not confirmed.
- Duplicate audience overlap: likely low right now because only one core ad set is active, but historical parallel ad sets in the same campaign could cause overlap if reactivated without exclusions.
- Critical recommendation: build purchaser 365d, purchaser 60d exclusion, website visitor 30d, ATC 30d, IC 30d, page engager 30d, IG engager 30d, video viewer 75% 30d before scaling.

## 6. Schedule and frequency

- Active prospecting target: keep frequency under 3.5.
- Winning ad set 30-day frequency from API breakdown varies by placement, but core mobile rows are mostly under the danger zone. Historical catalog-style retargeting showed frequency near or above 9, which is saturated.
- Time-of-day delivery was pulled by advertiser time zone, but purchase-level volume is too thin after blackout to make daypart rules. Do not daypart yet.
- Day-of-week breakdown request failed because `days_1` is not a supported breakdown in this API version.

## Audit conclusion

Aydins has a live winner and a working purchase-optimized sales campaign. The pro-level gap is not creative execution anymore. It is account architecture: missing audience inventory, missing exclusions, no dedicated retargeting lane, and no formal testing/scaling governance. Build those before increasing budget aggressively.
