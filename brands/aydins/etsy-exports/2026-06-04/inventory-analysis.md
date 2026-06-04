# Inventory Analysis — Aydins Jewelry Etsy
**Date:** 2026-06-04
**Method:** CSV export structural analysis + Shopify Top 50 cross-ref

## Summary
| Metric | Value |
|---|---|
| Unique listings | 1004 |
| With codename prefix | 39 |
| With variant SKUs | 707 |
| With video | 95 |
| Avg photos per listing | 7.0 |
| Shopify top 50 | 50 |
| Etsy-Shopify matches | 18 |
| New Shopify not on Etsy | 42 |
| SKU duplicate clusters | 305 |

## Critical Gaps Identified
| Issue | Impact |
|---|---|
| No video: 91% of listings | Etsy 2026 algorithm penalizes listings without video. This is the #1 ranking drag. |
| Tag cannibalization: 'wedding ring' on 788/1004 listings | Listings compete against each other for same search terms |
| Tag cannibalization: 'mens wedding band' on 462/1004 listings | Same keyword over-allocated across hundreds of listings |
| SKU duplicates: 305 clusters | Each JDTR/TR base SKU appears in multiple listings — product confusion |

## Section Distribution
| Section | Listings |
|---|---|
| Black Wedding Bands            |  254 ##############################################################################################################################################################################################################################################################
| Wood Inlay Wedding Bands       |  206 ##############################################################################################################################################################################################################
| Tungsten Rings                 |  163 ###################################################################################################################################################################
| (none)                         |   55 #######################################################
| Blue Wedding Bands             |   43 ###########################################
| Precious Stone Bands           |   43 ###########################################
| Green Wedding Bands            |   41 #########################################
| Unique Inlay Bands             |   37 #####################################
| Dinosaur Bone                  |   23 #######################
| Fingerprint Rings              |   20 ####################
| Orange Wedding Bands           |   19 ###################
| Purple Wedding Bands           |   18 ##################
| Rose Gold Wedding Bands        |   17 #################
| Titanium Wedding Bands         |   12 ############
| Camouflage Wedding Bands       |   12 ############
| Damascus Steel                 |   11 ###########
| Fingerprint Dog Tags           |   10 ##########
| Gold Wedding Bands             |    6 ######
| Red Wedding Bands              |    6 ######
| Signet Rings                   |    4 ####
| Carbon Fiber Bands             |    4 ####

## Etsy-Shopify Cross-Matches
| Listing ID | Etsy Title | Match Type | Shopify Product |
|---|---|---|---|
| 1219745003 | CLEMATIS | Tungsten Ring Purple Inside, Mens Weddi | codename:CLEMATIS | CLEMATIS | Purple Ring, Black Tungsten R |
| 1822237743 | 8mm Black Tungsten Ring with Purple Opal Inlay | M | sku:jdtr1086 | LUSTERS | Black Tungsten Purple Tiger Co |
| 1842100744 | Black Tungsten Ring with White CZ Diamonds - Bevel | sku:jdtr1028 | NEMESIS | Black Tungsten CZ Eternity Wed |
| 4512017757 | Men's Tungsten Carbide Wedding Band, Black Tungste | sku:aytr005 | FERRARI | Red Ring, Black Tungsten Ring, |
| 4512020342 | Fingerprint Jewelry | His and Her Fingerprint, Cou | sku:jdtr100 | Fingerprint Ring | Mens Wedding Band, Co |
| 4512020715 | Men's Tungsten Carbide Wedding Band, Black Tungste | sku:aytr120 | CLEMATIS | Purple Ring, Black Tungsten R |
| 4512030691 | Men's Damascus Steel Wedding Band, Silver Damascus | sku:aytr061 | RIDGES | Damascus Steel Olive Wood Inlay |
| 4512032425 | Men's Tungsten Carbide Wedding Band, Black Tungste | sku:jdtr1028 | NEMESIS | Black Tungsten CZ Eternity Wed |
| 4512034026 | Men's Tungsten Carbide Wedding Band, Black Tungste | sku:jdtr1086 | LUSTERS | Black Tungsten Purple Tiger Co |
| 4512044474 | Men's Tungsten Carbide Wedding Band, Available in  | sku:jdtr015 | Fingerprint Ring | Mens Wedding Band, Co |
| 4512045594 | Men's Tungsten Carbide Wedding Band, Black Tungste | sku:jdtr793 | AEROBITS | Red Tungsten Hammered Ring |
| 4512046160 | Fingerprint Jewelry | His & Her Fingerprint, Coupl | sku:aytr005 | FERRARI | Red Ring, Black Tungsten Ring, |
| 539295594 | Black Tungsten Ring with Red Interior - Domed Wedd | sku:aytr005 | FERRARI | Red Ring, Black Tungsten Ring, |
| 661079605 | Black Tungsten Ring | Mens Wedding Band, Hammered  | sku:jdtr793 | AEROBITS | Red Tungsten Hammered Ring |
| 674764297 | Fingerprint Jewelry | His & Her Fingerprint, Coupl | sku:aytr005 | FERRARI | Red Ring, Black Tungsten Ring, |
| 803871736 | Fingerprint Jewelry | His and Her Fingerprint, Cou | sku:jdtr015 | Fingerprint Ring | Mens Wedding Band, Co |
| 803881478 | Fingerprint Jewelry | His and Her Fingerprint, Cou | sku:jdtr100 | Fingerprint Ring | Mens Wedding Band, Co |
| 817711565 | Damascus Steel Wood Rings | Olive Wood Wedding Ban | sku:aytr061 | RIDGES | Damascus Steel Olive Wood Inlay |

## SKU-Based Duplicate Clusters
| Base SKU | Listings |
|---|---|
| JDTR709 | `4512044948`, `522912537` |
| AYTR022 | `4512045822`, `528037261` |
| AYTR435 | `1205810812`, `4512044566` |
| AYTR363 | `4512043812`, `1219759609` |
| JDTR061 | `817764707`, `4512044721` |
| JDTR739 | `526238869`, `4512045450` |
| JDTR865 | `830756083`, `4512044152` |
| AYTR109 | `1219753461`, `4512043105` |
| JDTR738 | `4512046064`, `514629168` |
| JDTR813 | `512437020`, `4512045826` |
| AYTR092 | `817720997`, `4512042169` |
| AYTR203 | `4512045162`, `1085033765` |
| AYTR183 | `1071090688`, `4512044818` |
| AYTR119 | `1205805390`, `4512045168` |
| AYTR011 | `674790993`, `539297138`, `4512043501`, `4512008217` |
| AYSSTAGP | `4512034186`, `509712178`, `4512043578`, `499499119` |
| JDTR380 | `512444810`, `4512043417` |
| JDTR217 | `4512033184`, `532801793` |
| JDTR733 | `509099536`, `4512044678` |
| AYTR034 | `640726968`, `4512043721` |
| AYTR172 | `4512044808`, `1085032359` |
| AYTR309 | `4512044262`, `1205805282` |
| TR729 | `522910507`, `4512057448` |
| AYTR068 | `817678243`, `4512055715` |
| AYTR510 | `4512057354`, `532667558` |
| AYTR009 | `4512042393`, `674792355`, `4512057674`, `4512020055`, `660953700`, `539296130` |
| AYTR037 | `895892476`, `4512009132`, `4512057672`, `803432898` |
| AYTR064 | `817713747`, `4512056693` |
| JDTR1141 | `1822237177`, `4512056511` |
| AYTR038 | `4512053733`, `895890230`, `4512044030`, `803772710` |
| JDTR822 | `4512056151`, `683797309` |
| AYTR079 | `4512055969`, `803811772` |
| AYTR015 | `4512057576`, `602673677` |
| JDTR124 | `4512057440`, `532813855` |
| AYTR094 | `4512056507`, `817722015` |
| JDTR715 | `512431720`, `4512056515` |
| AYTR273 | `1085041785`, `1219760135`, `4512054273`, `4512057886` |
| AYTR135 | `4512056742`, `1205809466` |
| JDTR081 | `532818005`, `4512055347`, `519002454`, `4512054103` |
| AYTR040 | `4512054541`, `817676389`, `4512054899`, `895897698` |
| AYTR018 | `1074430158`, `4512055489` |
| AYTR058 | `817677761`, `4512057160` |
| JDTR839 | `4512056494`, `816889242` |
| JDTR754 | `522897325`, `4512055033` |
| JDTR880 | `662897430`, `4512055477` |
| JDTR713 | `4512055713`, `526242435` |
| AYTR216 | `1071097564`, `4512056496` |
| AYTR026 | `4512056968`, `648781881` |
| AYTR052 | `4512055349`, `817708623` |
| AYTR176 | `1074212822`, `4512056734` |
| JDTR692 | `509472214`, `4512055583` |
| AYTR059 | `4512056610`, `803810154` |
| TR710 | `4512055123`, `509101184` |
| JDTR1127 | `4512057158`, `1822238987` |
| AYTR093 | `4512056402`, `817721363` |
| AYTR053 | `4512054547`, `817709229` |
| TR210 | `519007892`, `4512054099` |
| AYTR007 | `4512054281`, `553095337` |
| AYTR084 | `817719867`, `4512054097` |
| AYTR049 | `817691631`, `4512055900` |
| JDTR744 | `523291361`, `4512054901` |
| AYTR070 | `4512054439`, `803819532` |
| AYTR001 | `4512056242`, `514222670` |
| AYTR030 | `634954472`, `4512056114` |
| AYTR065 | `803437224`, `4512056406` |
| AYTR125 | `1205794076`, `4512056112` |
| AYTR032 | `648784295`, `634955052`, `4512044309`, `4512055778` |
| JDTR1133 | `1822239365`, `4512055960` |
| JDTR1150 | `1822237303`, `4512055964` |
| AYTR388 | `1219759759`, `4512055710` |
| AYTR081 | `817717875`, `4512056238` |
| AYTR207 | `4512054105`, `1071082688` |
| JDTR933 | `4512056118`, `1077633064` |
| AYTR321 | `1205804872`, `4512056330` |
| AYTR083 | `817719373`, `4512053885` |
| JDTR1151 | `1808040116`, `4512056124` |
| AYTR091 | `4512056408`, `817720389` |
| AYTR075 | `803442190`, `4512054543` |
| AYTR006 | `4512046168`, `539293582`, `4512006781`, `660954458` |
| AYTR078 | `817679601`, `4512053879` |
| AYTR413 | `1219752759`, `4512053603` |
| JDTR804 | `661071949`, `4512044853` |
| AYTR016 | `514631128`, `4512055444` |
| AYTR005 | `539295594`, `674764297`, `4512017757`, `4512046160` |
| JDTR594 | `4512046170`, `647406724` |
| JDTR1161 | `4315637099`, `4512055442` |
| JDTR600 | `661243221`, `4512053881` |
| AYTR088 | `4512044601`, `803797922` |
| AYTR191 | `4512053599`, `1071103086` |
| AYTR124 | `4512046540`, `1205805442` |
| AYTR640 | `1205802792`, `4512044729` |
| AYTR129 | `4512046338`, `1219743137` |
| JDTR1144 | `4512045318`, `1808040228` |
| JDTR793 | `4512045594`, `661079605` |
| JDTR941 | `4315662363`, `4512042391`, `4512044311`, `1077240530` |
| AYTR039 | `817666425`, `4512043843` |
| AYTR182 | `1085044235`, `4512045922` |
| AYTR256 | `4512043607`, `1219744809` |
| AYTR134 | `4512043605`, `1205803360` |
| AYTR076 | `817664513`, `4512045592` |
| JDTR934 | `1077625394`, `4512043723` |
| AYTR659 | `1219760109`, `4512044201` |
| AYTR086 | `817665283`, `4512044081` |
| JDTR704 | `4512045720`, `509474002` |
| JDTR603 | `661078775`, `4512044307` |
| JDTR1137 | `4512043845`, `1822237645` |
| JDTR748 | `4512042979`, `522899269` |
| JDTR788 | `4512042761`, `512438248` |
| JDTR1142 | `1808040348`, `4512043315` |
| JDTR331 | `661519637`, `4512043421` |
| AYTR514 | `1205809654`, `4512043113` |
| JDTR085 | `4512043415`, `647238976` |
| AYTR265 | `4512044956`, `1219752199` |
| AYTR515 | `1219743529`, `4512042873` |
| AYTR143 | `4512044268`, `1205805478` |
| JDTR837 | `4512044264`, `830782267` |
| AYTR055 | `817653539`, `4512043101` |
| AYTR591 | `4512043109`, `1205809810` |
| JDTR608 | `661244157`, `4512044674` |
| JDTR015 | `803871736`, `4512044474` |
| JDTR740 | `4512044258`, `526237977` |
| AYTR987 | `1733308737`, `4512043808` |
| AYTR051 | `4512042503`, `817707937` |
| AYTR145 | `1219744527`, `4512042177` |
| JDTR172 | `519010084`, `4512043912` |
| JDTR727 | `4512044034`, `509472954` |
| JDTR726 | `4512044038`, `510652228` |
| JDTR599 | `4512043910`, `647241320` |
| JDTR743 | `661072565`, `4512032847` |
| JDTR1163 | `4315607855`, `4512042163` |
| JDTR696 | `524466601`, `4512043918` |
| AYTR069 | `4512042023`, `803810924` |
| AYTR082 | `4512032859`, `803836306` |
| AYTR412 | `1219759455`, `4512034338` |
| AYTR387 | `4512043576`, `1205804210` |
| AYTR377 | `1205809612`, `4512043678` |
| JDTR683 | `4512033408`, `669958022` |
| JDTR775 | `1842100856`, `4512033748` |
| AYTR641 | `1219752847`, `4512033902` |
| JDTR792 | `803888310`, `4512033752` |
| JDTR332 | `4512032145`, `817771559` |
| JDTR324 | `4512032431`, `532808333` |
| AYTR263 | `1205803770`, `4512033412` |
| AYTR331 | `1205809314`, `4512032143` |
| JDTR045 | `519005070`, `4512031769` |
| TR675 | `4512032001`, `512436046` |
| AYTR013 | `4512033634`, `522893837` |
| JDTR1028 | `4512032425`, `1842100744` |
| AYTR029 | `634953928`, `4512031639` |
| JDTR1086 | `1822237743`, `4512034026` |
| AYTR260 | `1219744839`, `4512033400` |
| JDTR354 | `509106182`, `4512033532` |
| JDTR752 | `4512032632`, `523292385` |
| AYTR012 | `4512029927`, `660954126`, `539296482`, `4512032636` |
| JDTR205 | `4512033090`, `518984776` |
| JDTR902 | `676748103`, `4512031369` |
| JDTR697 | `4512033194`, `510639990` |
| JDTR869 | `4512030915`, `885311147` |
| AYTR061 | `817711565`, `4512030691` |
| AYTR367 | `1219753255`, `4512031535` |
| JDTR700 | `526244355`, `4512032156` |
| AYTR539 | `1205810566`, `4512030841` |
| AYTR150 | `1219752479`, `4512031365` |
| JDTR734 | `4512032286`, `522902423` |
| AYTR110 | `1205795278`, `4512032294` |
| AYTR080 | `817705011`, `4512032630` |
| JDTR367 | `526255301`, `4512030591` |
| JDTR810 | `4512031539`, `661241993` |
| JDTR703 | `509105132`, `4512031259` |
| AYTR246 | `1351010165`, `4512031529` |
| AYTR041 | `803800326`, `4512032746` |
| JDTR836 | `4512030697`, `830800425` |
| AYTR297 | `1205805302`, `4512031033` |
| JDTR731 | `4512032502`, `526240319` |
| AYTR615 | `1205795136`, `4512031377` |
| AYTR505 | `4512031379`, `1219743177` |
| AYTR108 | `4512032296`, `1219744055` |
| AYTR144 | `4512030463`, `1219754359` |
| JDTR701 | `4512030459`, `661079893` |
| AYTR660 | `4512030333`, `1205803224` |
| AYTR436 | `1219759809`, `4512030211` |
| JDTR334 | `526256379`, `4512031906` |
| JDTR204 | `4512031354`, `532801415` |
| AYTR506 | `4512030331`, `1205809884` |
| AYTR031 | `4512031502`, `634954696` |
| AYTR357 | `4512032066`, `1219758691` |
| AYTR010 | `553099247`, `4512022078`, `4512031362`, `674792981` |
| JDTR749 | `661079285`, `4512030219` |
| JDTR674 | `4512030061`, `512436422` |
| JDTR622 | `661073527`, `4512031356` |
| AYTR353 | `4512032158`, `1219752389` |
| JDTR151 | `518990008`, `4512029721` |
| JDTR745 | `524467763`, `4512030067` |
| AYTR111 | `4512030457`, `1219743503` |
| AYTR002 | `528029467`, `4512030327` |
| JDTR020 | `4512029719`, `803878882` |
| AYSSTAG | `541041099`, `528048177`, `4512021740`, `4512018041` |
| JDTR177 | `4512022086`, `518997310` |
| AYTR120 | `1219745003`, `4512020715` |
| AYTR087 | `803792844`, `4512021752` |
| JDTR185 | `532814209`, `4512020607`, `4512019495`, `532810197` |
| AYTR330 | `1205795922`, `4512021968` |
| AYTR043 | `803825222`, `4512020489` |
| AYTR386 | `1219743957`, `4512021528` |
| AYTR024 | `646450961`, `646449939`, `4512008502`, `4512021964` |
| JDTR838 | `816884694`, `4512019921` |
| AYTR434 | `4512021382`, `1205793822` |
| AYTR614 | `4512020287`, `1205802548` |
| JDTR665 | `526251287`, `4512022076` |
| AYTR085 | `817327103`, `4512021524` |
| AYTR074 | `4512019281`, `803835048` |
| AYTR566 | `1205803900`, `4512019487` |
| AYTR045 | `803434560`, `4512021132` |
| JDTR778 | `4512021012`, `524454669` |
| AYTR027 | `4512019725`, `634952800` |
| JDTR115 | `4512019283`, `647335116` |
| AYTR373 | `4512021244`, `1219753587` |
| JDTR100 | `803881478`, `4512020342` |
| JDTR625 | `4512019055`, `661524043` |
| AYTR063 | `817712827`, `4512020538` |
| AYTR042 | `4512019717`, `803816290` |
| AYTR050 | `803818144`, `4512019721` |
| JDTR791 | `817767195`, `4512020882` |
| AYTR071 | `4512019287`, `803833060` |
| AYTR048 | `803794772`, `4512019483` |
| AYTR028 | `4512019289`, `634953648` |
| JDTR800 | `4512020888`, `694856924` |
| AYTR513 | `1205804840`, `4512019916` |
| AYTR355 | `4512018845`, `1219743355` |
| AYTR329 | `4512018711`, `1205802920` |
| JDTR158 | `518986696`, `4512018705` |
| AYTR066 | `4512018497`, `817662471` |
| JDTR823 | `4512019914`, `676764639` |
| AYTR375 | `4512018847`, `1205810588` |
| AYTR148 | `1219760167`, `4512020036` |
| AYTR365 | `1205795712`, `4512019922` |
| JDTR862 | `830752869`, `4512018407` |
| JDTR801 | `4512019666`, `662910772` |
| AYTR565 | `4512018951`, `1219753003` |
| AYTR638 | `4512019590`, `1219758255` |
| JDTR708 | `512432994`, `4512020256` |
| AYTR118 | `4512019158`, `1219753647` |
| AYTR538 | `1219744425`, `4512010306` |
| AYTR095 | `836243894`, `4512010298` |
| AYTR133 | `1219753421`, `4512010418` |
| JDTR969 | `1091171223`, `4512019324` |
| AYTR411 | `1219759497`, `4512010000` |
| AYTR540 | `1205805140`, `4512010164` |
| AYTR047 | `4512008753`, `803784778` |
| AYTR563 | `1219752225`, `4512009155` |
| AYTR054 | `803828892`, `4512009147` |
| JDTR746 | `522899815`, `4512010414` |
| AYTR077 | `4512010296`, `817674113` |
| AYTR123 | `4512010308`, `1205804024` |
| JDTR1011 | `4315672219`, `4512008749` |
| AYTR437 | `4512008759`, `1205803392` |
| AYTR014 | `4512008003`, `528039519` |
| JDTR699 | `4512008125`, `647689242` |
| AYTR261 | `4512009692`, `1073324052` |
| AYTR227 | `4512007891`, `1071099906` |
| AYTR115 | `4512008299`, `909822489` |
| AYTR008 | `539294916`, `4512008535` |
| AYTR057 | `803786078`, `4512008295` |
| AYTR073 | `817715617`, `4512009554` |
| AYTR056 | `817660461`, `4512009810` |
| AYTR637 | `4512009348`, `1219743881` |
| AYTR541 | `1205805216`, `4512009924` |
| AYTR389 | `1205793748`, `4512009236` |
| AYTR588 | `4512007885`, `1219753603` |
| JDTR867 | `830757627`, `4512009234` |
| JDTR366 | `512445894`, `4512008219` |
| JDTR206 | `4512008533`, `532812337` |
| AYTR262 | `4512009808`, `1219744609` |
| JDTR595 | `647406472`, `4512008221` |
| AYTR062 | `4512008433`, `803830342` |
| AYTR504 | `1205810038`, `4512007893` |
| JDTR849 | `4512007429`, `816878130` |
| AYTR072 | `4512009008`, `817716549` |
| JDTR841 | `816899866`, `4512007657` |
| AYTR128 | `4512007531`, `1205803974` |
| AYTR089 | `4512008504`, `817694807` |
| AYTR616 | `1219758977`, `4512008604` |
| AYTR130 | `1219757849`, `4512007223` |
| JDTR809 | `4512008688`, `512434714` |
| AYTR612 | `4512008790`, `1219743029` |
| AYTR242 | `4512007431`, `1085035169` |
| AYTR046 | `803773576`, `4512007341` |
| AYTR035 | `4512008508`, `640727372` |
| AYTR658 | `4512008606`, `1205804618` |
| JDTR787 | `4512007653`, `532676064` |
| AYTR590 | `1205804378`, `4512008424` |
| JDTR853 | `4512008890`, `830768771` |
| AYTR312 | `514632860`, `4512007655` |
| JDTR751 | `4512007964`, `522897925` |
| AYTR096 | `843459196`, `4512007854` |
| AYTR036 | `4512006919`, `654560271` |
| AYTR259 | `1219744927`, `4512007035` |
| JDTR722 | `4512008336`, `647691302` |
| AYTR067 | `4512008090`, `803791040` |
| AYTR060 | `4512006681`, `817700609` |
| JDTR812 | `4512007860`, `526239437` |
| AYTR285 | `4512008418`, `1205805248` |
| AYTR149 | `1219760197`, `4512008086` |
| JDTR840 | `4512008332`, `830801879` |
| AYTR587 | `4512006583`, `1219743321` |

## New Shopify Products Not on Etsy
| Product Title | Handle | 90d Sales | 90d Revenue | Material | Images |
|---|---|---|---|---|---|
| AURION | Gold Tungsten Beveled Ring | aurion-gold-tungsten-ring-gold | 17 | $2879.12 | Gold | 8 |
| AURIC | Gold Tungsten Ring | auric-silver-tungsten-ring-whi | 10 | $1690.00 | Gold | 8 |
| ELYSIAN | Black Titanium Wedding Band - Brushed &  | elysian-black-titanium-ring-wi | 7 | $1119.93 | Titanium | 5 |
| KNIGHT | Black Titanium Steel Chain Black Diamond  | nurgle-black-diamond-titanium- | 7 | $6244.00 | Titanium | 5 |
| IRONLANCE | Brushed Black Tungsten 8 Laser-Engrave | ironlance-black-tungsten-ring- | 6 | $1014.00 | Tungsten | 5 |
| EMPEROR | Black Ring, Blue Tungsten Ring, Brushed, | emperor-black-tungsten-ring-bl | 6 | $876.00 | Tungsten | 4 |
| VESUVIUS | Black Ceramic Lava Rock Wedding Ring, B | alexander-black-gray-lava-rock | 6 | $1383.44 | Ceramic | 3 |
| VALOR | Silver Tungsten Ring, Silver Inlay & Black | valor-silver-tungsten-ring-sil | 5 | $2595.00 | Silver | 4 |
| Brushed Stainless Steel Fingerprint Dog Tag Neckla | stainless-steel-fingerprint-do | 5 | $235.00 | Gold | 4 |
| JAKUB | Black Ring, Black Tungsten Ring, Gold Groo | jakub-black-tungsten-ring-gold | 4 | $584.00 | Gold | 2 |
| SMOKEYLADE | Gun Metal Tungsten Ring, Brushed, Dom | smokeylade-black-gun-metal-tun | 4 | $676.00 | Tungsten | 3 |
| REVOLVE | Black Tungsten Fidget Spinner Wedding Ri | revolve-black-tungsten-brushed | 4 | $879.96 | Tungsten | 5 |
| PHANTOM | Black Titanium Fidget Spinner Wedding Ri | phantom-black-titanium-brushed | 3 | $627.00 | Titanium | 3 |
| RIDWAN | Black Ring, Black Tungsten Ring, Green Gr | ridwan-black-tungsten-ring-gre | 3 | $438.00 | Tungsten | 2 |
| GLOWHIGH | Blue Tungsten Brushed Domed Wedding Rin | glowhigh-domed-blue-tungsten-c | 3 | $507.00 | Tungsten | 2 |
| NYMERIA | Titanium Ring Blue Sapphire | nymeria-tension-set-blue-sapph | 3 | $1152.00 | Silver | 1 |
| BRANDMARK | Custom Logo Laser Engraved Signet Ring | custom-logo-laser-engraved-sig | 3 | $140.01 | Gold | 6 |
| CRIMSEN | Red Tungsten Domed Ring | crimsen-red-tungsten-ring-brus | 3 | $507.00 | Tungsten | 4 |
| SPARTANITE | Black Ring, Black Tungsten Ring, Oran | spartanite-black-ring-black-br | 2 | $297.46 | Tungsten | 2 |
| LEPORIS | Black Tungsten Ring, Diamond Stimulant C | leporis-black-tungsten-ring-ro | 2 | $338.00 | Tungsten | 3 |
| MAESTRO | Silver Tungsten Ring, Gold Groove, Bevel | maestro-mens-silver-brushed-tu | 2 | $338.00 | Silver | 4 |
| ADDERSFIELD | Gold Ring, Gold Tungsten Ring, Brush | addersfield-gold-tungsten-ring | 2 | $292.00 | Gold | 6 |
| BRAVE | Blue Tungsten Ring, Blue Tungsten Ring, Br | brave-blue-tungsten-ring-blue- | 2 | $292.00 | Tungsten | 4 |
| COSMIC | Black Tungsten Ring, Crushed Alexandrite, | cosmic-black-tungsten-ring-cru | 2 | $598.00 | Tungsten | 6 |
| GUNNAR | Yellow Gold Tungsten Rosewood & Crushed T | gunnar-yellow-gold-tungsten-ri | 2 | $338.00 | Gold | 9 |
| CAIRNS | Rose Gold Ring, Black Tungsten Ring, Purp | cairns-rose-gold-tungsten-ring | 2 | $292.00 | Gold | 4 |
| GEELONG | Green Ring, Black Tungsten Ring, Purple  | geelong-green-aluminum-ring-pu | 2 | $292.00 | Tungsten | 4 |
| BLACKJACK | Black Ring, Black Tungsten Ring, Brush | blackjack-tungsten-ring-black- | 2 | $292.00 | Tungsten | 4 |
| RUGGED | Black Tungsten Hammered Ring | rugged-black-tungsten-ring-gun | 2 | $338.00 | Tungsten | 4 |
| YORKSHIRE | Black Ceramic Ring Brushed Finish | yorkshire-brushed-finish-black | 2 | $334.04 | Ceramic | 3 |
| GALAXY | Silver Titanium Ring, Blue Green Opal Inl | galaxy-titanium-polished-bevel | 2 | $338.00 | Opal | 5 |
| BALDUR | Domed Tungsten Rune Wedding Band | baldur-domed-tungsten-rune-wed | 2 | $798.00 | Tungsten | 7 |
| RAPTOR | Black Ring, Black Tungsten Ring, Blue Off | raptor-black-tungsten-ring-blu | 2 | $294.48 | Tungsten | 4 |
| ALABASTER | Silver Ring, White Ceramic Ring, Domed | alabaster-silver-ring-white-ce | 2 | $292.00 | Ceramic | 4 |
| DOMINUS | Silver Tungsten Ring, Shiny Domed | dominus-domed-tungsten-carbide | 2 | $383.14 | Silver | 2 |
| REVOLUTION | Silver Tungsten Fidget Spinner Weddin | revolution-tungsten-carbide-sp | 2 | $418.00 | Silver | 2 |
| BRIDGEPORT | Purple Ring, Black Tungsten Ring, Gre | bridgeport-purple-aluminum-rin | 2 | $292.00 | Tungsten | 4 |
| Signet Ring - Custom Signet Ring - Fingerprint Rin | signet-ring-custom-signet-ring | 2 | $93.34 | Gold | 4 |
| PEACHLAND | Black Tungsten Ring Green Celtic Drago | peachland-black-tungsten-ring- | 2 | $345.30 | Tungsten | 2 |
| KNOX | Gold Tungsten Ring with Black Hammered Cent | knox-gold-tungsten-ring-black- | 1 | $146.00 | Tungsten | 2 |
| HARTMAN | Tungsten Blue Yellow Wood Inlay Ring | hartman-white-tungsten-blue-ye | 1 | $149.08 | Wood | 5 |
| SEQUOIA | IRON Wood, Black Tungsten Ring, Shiny, D | sequoia-iron-wood-black-shiny- | 1 | $148.23 | Wood | 4 |