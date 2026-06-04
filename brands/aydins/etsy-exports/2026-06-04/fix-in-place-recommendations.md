# Fix-in-Place Recommendations
**Date:** 2026-06-04
**Total listings flagged for review:** 986

## Structural Issues (from CSV analysis)

### 1. No Video — 909 listings
Etsy 2026 algorithm ranks video-enabled listings higher. This is the single biggest SEO drag.

### 2. Tag Cannibalization
Top tags overlap across 788%+ of listings:
| Tag | Listings Using It | % of Catalog |
|---|---|---|
| wedding ring | 788 | 78% |
| promise ring | 688 | 69% |
| engagement ring | 642 | 64% |
| personalized ring | 632 | 63% |
| comfort fit ring | 599 | 60% |
| wedding band for men | 592 | 59% |
| mens wedding band | 462 | 46% |
| unique ring | 427 | 43% |
| engraved ring | 416 | 41% |
| mens jewelry | 409 | 41% |

### 3. SKU Duplicates — 305 clusters
Same base SKU appears in multiple listings — either true duplicates or listing templating errors.
| Base SKU | Listings | Sections |
|---|---|---|
| JDTR709 | 4512044948, 522912537 | Black Wedding Bands |
| AYTR022 | 4512045822, 528037261 | Black Wedding Bands |
| AYTR435 | 1205810812, 4512044566 | Black Wedding Bands |
| AYTR363 | 4512043812, 1219759609 | Tungsten Rings |
| JDTR061 | 817764707, 4512044721 | Fingerprint Rings |
| JDTR739 | 526238869, 4512045450 | Wood Inlay Wedding Bands |
| JDTR865 | 830756083, 4512044152 | Tungsten Rings |
| AYTR109 | 1219753461, 4512043105 | Green Wedding Bands |
| JDTR738 | 4512046064, 514629168 | Tungsten Rings |
| JDTR813 | 512437020, 4512045826 | Black Wedding Bands |
| AYTR092 | 817720997, 4512042169 | Wood Inlay Wedding Bands |
| AYTR203 | 4512045162, 1085033765 | Wood Inlay Wedding Bands |
| AYTR183 | 1071090688, 4512044818 | Wood Inlay Wedding Bands |
| AYTR119 | 1205805390, 4512045168 | Black Wedding Bands |
| AYTR011 | 674790993, 539297138, 4512043501, 4512008217 | , Tungsten Rings, Black Wedding Bands |
| AYSSTAGP | 4512034186, 509712178, 4512043578, 499499119 | Fingerprint Dog Tags |
| JDTR380 | 512444810, 4512043417 | Black Wedding Bands |
| JDTR217 | 4512033184, 532801793 | Tungsten Rings |
| JDTR733 | 509099536, 4512044678 | Black Wedding Bands |
| AYTR034 | 640726968, 4512043721 | Wood Inlay Wedding Bands |
| AYTR172 | 4512044808, 1085032359 | Wood Inlay Wedding Bands |
| AYTR309 | 4512044262, 1205805282 | Titanium Wedding Bands |
| TR729 | 522910507, 4512057448 | Rose Gold Wedding Bands |
| AYTR068 | 817678243, 4512055715 | Wood Inlay Wedding Bands |
| AYTR510 | 4512057354, 532667558 | Tungsten Rings |
| AYTR009 | 4512042393, 674792355, 4512057674, 4512020055, 660953700, 539296130 | Tungsten Rings, , Fingerprint Rings |
| AYTR037 | 895892476, 4512009132, 4512057672, 803432898 | Wood Inlay Wedding Bands, Black Wedding Bands |
| AYTR064 | 817713747, 4512056693 | Wood Inlay Wedding Bands |
| JDTR1141 | 1822237177, 4512056511 | Black Wedding Bands |
| AYTR038 | 4512053733, 895890230, 4512044030, 803772710 | Wood Inlay Wedding Bands |
| JDTR822 | 4512056151, 683797309 | Black Wedding Bands |
| AYTR079 | 4512055969, 803811772 | Wood Inlay Wedding Bands |
| AYTR015 | 4512057576, 602673677 | Black Wedding Bands |
| JDTR124 | 4512057440, 532813855 | Black Wedding Bands |
| AYTR094 | 4512056507, 817722015 | Wood Inlay Wedding Bands |
| JDTR715 | 512431720, 4512056515 | Black Wedding Bands |
| AYTR273 | 1085041785, 1219760135, 4512054273, 4512057886 | Black Wedding Bands |
| AYTR135 | 4512056742, 1205809466 | Purple Wedding Bands |
| JDTR081 | 532818005, 4512055347, 519002454, 4512054103 | Tungsten Rings |
| AYTR040 | 4512054541, 817676389, 4512054899, 895897698 | Wood Inlay Wedding Bands |
| AYTR018 | 1074430158, 4512055489 | Black Wedding Bands |
| AYTR058 | 817677761, 4512057160 | Wood Inlay Wedding Bands |
| JDTR839 | 4512056494, 816889242 | Tungsten Rings |
| JDTR754 | 522897325, 4512055033 | Black Wedding Bands |
| JDTR880 | 662897430, 4512055477 | Black Wedding Bands |
| JDTR713 | 4512055713, 526242435 | Black Wedding Bands |
| AYTR216 | 1071097564, 4512056496 | Wood Inlay Wedding Bands |
| AYTR026 | 4512056968, 648781881 | Black Wedding Bands |
| AYTR052 | 4512055349, 817708623 | Wood Inlay Wedding Bands |
| AYTR176 | 1074212822, 4512056734 | Wood Inlay Wedding Bands |
| JDTR692 | 509472214, 4512055583 | Blue Wedding Bands |
| AYTR059 | 4512056610, 803810154 | Wood Inlay Wedding Bands |
| TR710 | 4512055123, 509101184 | Black Wedding Bands |
| JDTR1127 | 4512057158, 1822238987 | Black Wedding Bands |
| AYTR093 | 4512056402, 817721363 | Wood Inlay Wedding Bands |
| AYTR053 | 4512054547, 817709229 | Wood Inlay Wedding Bands |
| TR210 | 519007892, 4512054099 | Tungsten Rings |
| AYTR007 | 4512054281, 553095337 | Black Wedding Bands |
| AYTR084 | 817719867, 4512054097 | Wood Inlay Wedding Bands |
| AYTR049 | 817691631, 4512055900 | Wood Inlay Wedding Bands |
| JDTR744 | 523291361, 4512054901 | Blue Wedding Bands |
| AYTR070 | 4512054439, 803819532 | Wood Inlay Wedding Bands |
| AYTR001 | 4512056242, 514222670 | Black Wedding Bands |
| AYTR030 | 634954472, 4512056114 | Black Wedding Bands |
| AYTR065 | 803437224, 4512056406 | Wood Inlay Wedding Bands |
| AYTR125 | 1205794076, 4512056112 | Black Wedding Bands |
| AYTR032 | 648784295, 634955052, 4512044309, 4512055778 | Black Wedding Bands |
| JDTR1133 | 1822239365, 4512055960 | Black Wedding Bands |
| JDTR1150 | 1822237303, 4512055964 | Black Wedding Bands |
| AYTR388 | 1219759759, 4512055710 | Black Wedding Bands |
| AYTR081 | 817717875, 4512056238 | Wood Inlay Wedding Bands |
| AYTR207 | 4512054105, 1071082688 | Wood Inlay Wedding Bands |
| JDTR933 | 4512056118, 1077633064 | Black Wedding Bands |
| AYTR321 | 1205804872, 4512056330 | Titanium Wedding Bands |
| AYTR083 | 817719373, 4512053885 | Wood Inlay Wedding Bands |
| JDTR1151 | 1808040116, 4512056124 | Wood Inlay Wedding Bands |
| AYTR091 | 4512056408, 817720389 | Wood Inlay Wedding Bands |
| AYTR075 | 803442190, 4512054543 | Wood Inlay Wedding Bands |
| AYTR006 | 4512046168, 539293582, 4512006781, 660954458 | Fingerprint Rings, Black Wedding Bands |
| AYTR078 | 817679601, 4512053879 | Wood Inlay Wedding Bands |
| AYTR413 | 1219752759, 4512053603 | Blue Wedding Bands |
| JDTR804 | 661071949, 4512044853 | Black Wedding Bands |
| AYTR016 | 514631128, 4512055444 | Tungsten Rings |
| AYTR005 | 539295594, 674764297, 4512017757, 4512046160 | Fingerprint Rings, Black Wedding Bands |
| JDTR594 | 4512046170, 647406724 | Tungsten Rings, Black Wedding Bands |
| JDTR1161 | 4315637099, 4512055442 | Blue Wedding Bands |
| JDTR600 | 661243221, 4512053881 | Tungsten Rings |
| AYTR088 | 4512044601, 803797922 | Wood Inlay Wedding Bands |
| AYTR191 | 4512053599, 1071103086 | Wood Inlay Wedding Bands |
| AYTR124 | 4512046540, 1205805442 | Orange Wedding Bands, Black Wedding Bands |
| AYTR640 | 1205802792, 4512044729 | Green Wedding Bands, Black Wedding Bands |
| AYTR129 | 4512046338, 1219743137 | Black Wedding Bands |
| JDTR1144 | 4512045318, 1808040228 | Black Wedding Bands |
| JDTR793 | 4512045594, 661079605 | Black Wedding Bands |
| JDTR941 | 4315662363, 4512042391, 4512044311, 1077240530 | Black Wedding Bands |
| AYTR039 | 817666425, 4512043843 | Wood Inlay Wedding Bands |
| AYTR182 | 1085044235, 4512045922 | Wood Inlay Wedding Bands |
| AYTR256 | 4512043607, 1219744809 | Black Wedding Bands |
| AYTR134 | 4512043605, 1205803360 | Orange Wedding Bands |
| AYTR076 | 817664513, 4512045592 | Wood Inlay Wedding Bands |
| JDTR934 | 1077625394, 4512043723 | Black Wedding Bands |
| AYTR659 | 1219760109, 4512044201 | Black Wedding Bands |
| AYTR086 | 817665283, 4512044081 | Wood Inlay Wedding Bands |
| JDTR704 | 4512045720, 509474002 | Black Wedding Bands |
| JDTR603 | 661078775, 4512044307 | Black Wedding Bands |
| JDTR1137 | 4512043845, 1822237645 |  |
| JDTR748 | 4512042979, 522899269 | Black Wedding Bands |
| JDTR788 | 4512042761, 512438248 | Black Wedding Bands |
| JDTR1142 | 1808040348, 4512043315 | Blue Wedding Bands |
| JDTR331 | 661519637, 4512043421 | Black Wedding Bands |
| AYTR514 | 1205809654, 4512043113 | Tungsten Rings |
| JDTR085 | 4512043415, 647238976 | Black Wedding Bands |
| AYTR265 | 4512044956, 1219752199 | Black Wedding Bands |
| AYTR515 | 1219743529, 4512042873 | Tungsten Rings |
| AYTR143 | 4512044268, 1205805478 | Green Wedding Bands |
| JDTR837 | 4512044264, 830782267 | Tungsten Rings |
| AYTR055 | 817653539, 4512043101 | Wood Inlay Wedding Bands |
| AYTR591 | 4512043109, 1205809810 | Black Wedding Bands |
| JDTR608 | 661244157, 4512044674 | Black Wedding Bands |
| JDTR015 | 803871736, 4512044474 | , Fingerprint Rings |
| JDTR740 | 4512044258, 526237977 | Tungsten Rings |
| AYTR987 | 1733308737, 4512043808 | , Wood Inlay Wedding Bands |
| AYTR051 | 4512042503, 817707937 | Wood Inlay Wedding Bands |
| AYTR145 | 1219744527, 4512042177 | Tungsten Rings |
| JDTR172 | 519010084, 4512043912 | Tungsten Rings, Precious Stone Bands |
| JDTR727 | 4512044034, 509472954 | Tungsten Rings, Blue Wedding Bands |
| JDTR726 | 4512044038, 510652228 | Blue Wedding Bands |
| JDTR599 | 4512043910, 647241320 | Tungsten Rings, Rose Gold Wedding Bands |
| JDTR743 | 661072565, 4512032847 | Tungsten Rings, Rose Gold Wedding Bands |
| JDTR1163 | 4315607855, 4512042163 | Precious Stone Bands |
| JDTR696 | 524466601, 4512043918 | Tungsten Rings |
| AYTR069 | 4512042023, 803810924 | Wood Inlay Wedding Bands |
| AYTR082 | 4512032859, 803836306 | Wood Inlay Wedding Bands |
| AYTR412 | 1219759455, 4512034338 | Orange Wedding Bands, Blue Wedding Bands |
| AYTR387 | 4512043576, 1205804210 | Orange Wedding Bands, Black Wedding Bands |
| AYTR377 | 1205809612, 4512043678 | Orange Wedding Bands, Black Wedding Bands |
| JDTR683 | 4512033408, 669958022 | Tungsten Rings |
| JDTR775 | 1842100856, 4512033748 | , Black Wedding Bands |
| AYTR641 | 1219752847, 4512033902 | Orange Wedding Bands, Black Wedding Bands |
| JDTR792 | 803888310, 4512033752 | Fingerprint Rings |
| JDTR332 | 4512032145, 817771559 | Fingerprint Rings |
| JDTR324 | 4512032431, 532808333 | Blue Wedding Bands, Carbon Fiber Bands |
| AYTR263 | 1205803770, 4512033412 | Tungsten Rings, Purple Wedding Bands |
| AYTR331 | 1205809314, 4512032143 | Tungsten Rings, Purple Wedding Bands |
| JDTR045 | 519005070, 4512031769 | Tungsten Rings |
| TR675 | 4512032001, 512436046 | Black Wedding Bands |
| AYTR013 | 4512033634, 522893837 | Wood Inlay Wedding Bands |
| JDTR1028 | 4512032425, 1842100744 | , Black Wedding Bands |
| AYTR029 | 634953928, 4512031639 | Black Wedding Bands |
| JDTR1086 | 1822237743, 4512034026 | , Black Wedding Bands |
| AYTR260 | 1219744839, 4512033400 | Orange Wedding Bands, Tungsten Rings |
| JDTR354 | 509106182, 4512033532 | Tungsten Rings |
| JDTR752 | 4512032632, 523292385 | Wood Inlay Wedding Bands, Blue Wedding Bands |
| AYTR012 | 4512029927, 660954126, 539296482, 4512032636 | Tungsten Rings, Fingerprint Rings |
| JDTR205 | 4512033090, 518984776 | Tungsten Rings, Carbon Fiber Bands |
| JDTR902 | 676748103, 4512031369 | , Black Wedding Bands |
| JDTR697 | 4512033194, 510639990 | Black Wedding Bands |
| JDTR869 | 4512030915, 885311147 | Black Wedding Bands |
| AYTR061 | 817711565, 4512030691 | Wood Inlay Wedding Bands |
| AYTR367 | 1219753255, 4512031535 | Orange Wedding Bands, Tungsten Rings |
| JDTR700 | 526244355, 4512032156 | Tungsten Rings, Black Wedding Bands |
| AYTR539 | 1205810566, 4512030841 | Orange Wedding Bands, Black Wedding Bands |
| AYTR150 | 1219752479, 4512031365 | Tungsten Rings, Purple Wedding Bands |
| JDTR734 | 4512032286, 522902423 | Blue Wedding Bands, Black Wedding Bands |
| AYTR110 | 1205795278, 4512032294 | Titanium Wedding Bands |
| AYTR080 | 817705011, 4512032630 | Wood Inlay Wedding Bands |
| JDTR367 | 526255301, 4512030591 | Blue Wedding Bands, Unique Inlay Bands |
| JDTR810 | 4512031539, 661241993 | Tungsten Rings, Gold Wedding Bands |
| JDTR703 | 509105132, 4512031259 | Tungsten Rings, Gold Wedding Bands |
| AYTR246 | 1351010165, 4512031529 | Wood Inlay Wedding Bands |
| AYTR041 | 803800326, 4512032746 | Wood Inlay Wedding Bands |
| JDTR836 | 4512030697, 830800425 | Tungsten Rings |
| AYTR297 | 1205805302, 4512031033 | Titanium Wedding Bands |
| JDTR731 | 4512032502, 526240319 | Gold Wedding Bands |
| AYTR615 | 1205795136, 4512031377 | Orange Wedding Bands, Black Wedding Bands |
| AYTR505 | 4512031379, 1219743177 | Orange Wedding Bands, Green Wedding Bands |
| AYTR108 | 4512032296, 1219744055 | Titanium Wedding Bands, Blue Wedding Bands |
| AYTR144 | 4512030463, 1219754359 | Tungsten Rings, Orange Wedding Bands |
| JDTR701 | 4512030459, 661079893 | Black Wedding Bands |
| AYTR660 | 4512030333, 1205803224 | Black Wedding Bands, Purple Wedding Bands |
| AYTR436 | 1219759809, 4512030211 | Black Wedding Bands, Purple Wedding Bands |
| JDTR334 | 526256379, 4512031906 | Tungsten Rings, Rose Gold Wedding Bands |
| JDTR204 | 4512031354, 532801415 | Blue Wedding Bands, Carbon Fiber Bands |
| AYTR506 | 4512030331, 1205809884 | Green Wedding Bands, Purple Wedding Bands |
| AYTR031 | 4512031502, 634954696 | Black Wedding Bands |
| AYTR357 | 4512032066, 1219758691 | Tungsten Rings, Orange Wedding Bands |
| AYTR010 | 553099247, 4512022078, 4512031362, 674792981 | Tungsten Rings, , Green Wedding Bands, Fingerprint Rings |
| JDTR749 | 661079285, 4512030219 | Black Wedding Bands |
| JDTR674 | 4512030061, 512436422 | Unique Inlay Bands, Black Wedding Bands |
| JDTR622 | 661073527, 4512031356 | Black Wedding Bands |
| AYTR353 | 4512032158, 1219752389 | Tungsten Rings, Purple Wedding Bands |
| JDTR151 | 518990008, 4512029721 | Tungsten Rings |
| JDTR745 | 524467763, 4512030067 | Black Wedding Bands |
| AYTR111 | 4512030457, 1219743503 | Titanium Wedding Bands |
| AYTR002 | 528029467, 4512030327 | Black Wedding Bands |
| JDTR020 | 4512029719, 803878882 | , Fingerprint Rings |
| AYSSTAG | 541041099, 528048177, 4512021740, 4512018041 | Fingerprint Dog Tags |
| JDTR177 | 4512022086, 518997310 | Tungsten Rings |
| AYTR120 | 1219745003, 4512020715 | Black Wedding Bands, Purple Wedding Bands |
| AYTR087 | 803792844, 4512021752 | Wood Inlay Wedding Bands |
| JDTR185 | 532814209, 4512020607, 4512019495, 532810197 | Tungsten Rings, Gold Wedding Bands |
| AYTR330 | 1205795922, 4512021968 | Orange Wedding Bands, Tungsten Rings |
| AYTR043 | 803825222, 4512020489 | Wood Inlay Wedding Bands |
| AYTR386 | 1219743957, 4512021528 | Green Wedding Bands, Black Wedding Bands |
| AYTR024 | 646450961, 646449939, 4512008502, 4512021964 | Wood Inlay Wedding Bands |
| JDTR838 | 816884694, 4512019921 | Tungsten Rings |
| AYTR434 | 4512021382, 1205793822 | Green Wedding Bands, Black Wedding Bands |
| AYTR614 | 4512020287, 1205802548 | Green Wedding Bands, Black Wedding Bands |
| JDTR665 | 526251287, 4512022076 | Black Wedding Bands |
| AYTR085 | 817327103, 4512021524 | Wood Inlay Wedding Bands |
| AYTR074 | 4512019281, 803835048 | Wood Inlay Wedding Bands |
| AYTR566 | 1205803900, 4512019487 | Orange Wedding Bands, Black Wedding Bands |
| AYTR045 | 803434560, 4512021132 | Wood Inlay Wedding Bands |
| JDTR778 | 4512021012, 524454669 | Black Wedding Bands |
| AYTR027 | 4512019725, 634952800 | Black Wedding Bands |
| JDTR115 | 4512019283, 647335116 | Black Wedding Bands |
| AYTR373 | 4512021244, 1219753587 | Black Wedding Bands, Purple Wedding Bands |
| JDTR100 | 803881478, 4512020342 | Fingerprint Rings |
| JDTR625 | 4512019055, 661524043 | Tungsten Rings, Rose Gold Wedding Bands |
| AYTR063 | 817712827, 4512020538 | Wood Inlay Wedding Bands |
| AYTR042 | 4512019717, 803816290 | Wood Inlay Wedding Bands |
| AYTR050 | 803818144, 4512019721 | Wood Inlay Wedding Bands |
| JDTR791 | 817767195, 4512020882 | Fingerprint Rings |
| AYTR071 | 4512019287, 803833060 | Wood Inlay Wedding Bands |
| AYTR048 | 803794772, 4512019483 | Wood Inlay Wedding Bands |
| AYTR028 | 4512019289, 634953648 | Black Wedding Bands |
| JDTR800 | 4512020888, 694856924 | , Fingerprint Rings |
| AYTR513 | 1205804840, 4512019916 | Green Wedding Bands |
| AYTR355 | 4512018845, 1219743355 | Green Wedding Bands |
| AYTR329 | 4512018711, 1205802920 | Green Wedding Bands |
| JDTR158 | 518986696, 4512018705 | Blue Wedding Bands, Carbon Fiber Bands |
| AYTR066 | 4512018497, 817662471 | Wood Inlay Wedding Bands |
| JDTR823 | 4512019914, 676764639 | Black Wedding Bands |
| AYTR375 | 4512018847, 1205810588 | Green Wedding Bands, Black Wedding Bands |
| AYTR148 | 1219760167, 4512020036 | Green Wedding Bands |
| AYTR365 | 1205795712, 4512019922 | Green Wedding Bands |
| JDTR862 | 830752869, 4512018407 | Tungsten Rings |
| JDTR801 | 4512019666, 662910772 | Tungsten Rings |
| AYTR565 | 4512018951, 1219753003 | Green Wedding Bands, Black Wedding Bands |
| AYTR638 | 4512019590, 1219758255 | Black Wedding Bands, Purple Wedding Bands |
| JDTR708 | 512432994, 4512020256 | Black Wedding Bands |
| AYTR118 | 4512019158, 1219753647 | Green Wedding Bands, Black Wedding Bands |
| AYTR538 | 1219744425, 4512010306 | Green Wedding Bands, Black Wedding Bands |
| AYTR095 | 836243894, 4512010298 | Tungsten Rings, Black Wedding Bands |
| AYTR133 | 1219753421, 4512010418 | Green Wedding Bands |
| JDTR969 | 1091171223, 4512019324 | Rose Gold Wedding Bands |
| AYTR411 | 1219759497, 4512010000 | Blue Wedding Bands, Green Wedding Bands |
| AYTR540 | 1205805140, 4512010164 | Black Wedding Bands, Purple Wedding Bands |
| AYTR047 | 4512008753, 803784778 | Wood Inlay Wedding Bands |
| AYTR563 | 1219752225, 4512009155 | Black Wedding Bands, Purple Wedding Bands |
| AYTR054 | 803828892, 4512009147 | Wood Inlay Wedding Bands |
| JDTR746 | 522899815, 4512010414 | Rose Gold Wedding Bands, Black Wedding Bands |
| AYTR077 | 4512010296, 817674113 | Wood Inlay Wedding Bands |
| AYTR123 | 4512010308, 1205804024 | Green Wedding Bands, Black Wedding Bands |
| JDTR1011 | 4315672219, 4512008749 | , Black Wedding Bands |
| AYTR437 | 4512008759, 1205803392 | Red Wedding Bands, Black Wedding Bands |
| AYTR014 | 4512008003, 528039519 | Black Wedding Bands |
| JDTR699 | 4512008125, 647689242 | Black Wedding Bands |
| AYTR261 | 4512009692, 1073324052 | Black Wedding Bands |
| AYTR227 | 4512007891, 1071099906 | Wood Inlay Wedding Bands |
| AYTR115 | 4512008299, 909822489 | Black Wedding Bands |
| AYTR008 | 539294916, 4512008535 | Orange Wedding Bands, Black Wedding Bands |
| AYTR057 | 803786078, 4512008295 | Wood Inlay Wedding Bands |
| AYTR073 | 817715617, 4512009554 | Wood Inlay Wedding Bands |
| AYTR056 | 817660461, 4512009810 | Wood Inlay Wedding Bands |
| AYTR637 | 4512009348, 1219743881 | Red Wedding Bands, Black Wedding Bands |
| AYTR541 | 1205805216, 4512009924 | Red Wedding Bands, Black Wedding Bands |
| AYTR389 | 1205793748, 4512009236 | Red Wedding Bands, Black Wedding Bands |
| AYTR588 | 4512007885, 1219753603 | Black Wedding Bands, Purple Wedding Bands |
| JDTR867 | 830757627, 4512009234 | Tungsten Rings |
| JDTR366 | 512445894, 4512008219 | Tungsten Rings, Unique Inlay Bands |
| JDTR206 | 4512008533, 532812337 | Tungsten Rings, Rose Gold Wedding Bands |
| AYTR262 | 4512009808, 1219744609 | Black Wedding Bands, Purple Wedding Bands |
| JDTR595 | 647406472, 4512008221 | Tungsten Rings |
| AYTR062 | 4512008433, 803830342 | Wood Inlay Wedding Bands |
| AYTR504 | 1205810038, 4512007893 | Green Wedding Bands |
| JDTR849 | 4512007429, 816878130 | Tungsten Rings |
| AYTR072 | 4512009008, 817716549 | Wood Inlay Wedding Bands |
| JDTR841 | 816899866, 4512007657 | Tungsten Rings |
| AYTR128 | 4512007531, 1205803974 | Green Wedding Bands, Black Wedding Bands |
| AYTR089 | 4512008504, 817694807 | Wood Inlay Wedding Bands |
| AYTR616 | 1219758977, 4512008604 | Black Wedding Bands, Purple Wedding Bands |
| AYTR130 | 1219757849, 4512007223 | Black Wedding Bands, Purple Wedding Bands |
| JDTR809 | 4512008688, 512434714 | Wood Inlay Wedding Bands |
| AYTR612 | 4512008790, 1219743029 | Red Wedding Bands, Black Wedding Bands |
| AYTR242 | 4512007431, 1085035169 | Wood Inlay Wedding Bands |
| AYTR046 | 803773576, 4512007341 | Wood Inlay Wedding Bands |
| AYTR035 | 4512008508, 640727372 | Wood Inlay Wedding Bands |
| AYTR658 | 4512008606, 1205804618 | Green Wedding Bands, Black Wedding Bands |
| JDTR787 | 4512007653, 532676064 | Tungsten Rings, Rose Gold Wedding Bands |
| AYTR590 | 1205804378, 4512008424 | Green Wedding Bands, Black Wedding Bands |
| JDTR853 | 4512008890, 830768771 | Tungsten Rings |
| AYTR312 | 514632860, 4512007655 | Tungsten Rings |
| JDTR751 | 4512007964, 522897925 | Rose Gold Wedding Bands |
| AYTR096 | 843459196, 4512007854 | Wood Inlay Wedding Bands |
| AYTR036 | 4512006919, 654560271 | Wood Inlay Wedding Bands |
| AYTR259 | 1219744927, 4512007035 | Orange Wedding Bands, Black Wedding Bands |
| JDTR722 | 4512008336, 647691302 | Unique Inlay Bands, Black Wedding Bands |
| AYTR067 | 4512008090, 803791040 | Wood Inlay Wedding Bands |
| AYTR060 | 4512006681, 817700609 | Wood Inlay Wedding Bands |
| JDTR812 | 4512007860, 526239437 | Tungsten Rings, Rose Gold Wedding Bands |
| AYTR285 | 4512008418, 1205805248 | Titanium Wedding Bands, Blue Wedding Bands |
| AYTR149 | 1219760197, 4512008086 | Orange Wedding Bands, Tungsten Rings |
| JDTR840 | 4512008332, 830801879 | Tungsten Rings |
| AYTR587 | 4512006583, 1219743321 | Red Wedding Bands, Black Wedding Bands |

### 4. Products Mentioned in Dashboard (Views/Orders Context)

**High-View Zero-Revenue Kill Candidates (from Amir dashboard, May 2026):**

| Listing | Issue | Action |
|---|---|---|
| Fingerprint His & Her Tungsten (200 views, 0 orders) | High views, zero conversion | KILL or complete revamp |
| Personalized Fingerprint Ring Promise (263 views, 29 favs, 0 orders) | High favorites, no sales — pricing or photo issue | FIX-IN-PLACE: check pricing vs competitors |
| Black Diamond Tungsten 9 Channel (110 views, 8 favs, 0 orders) | Low conversion | FIX-IN-PLACE: price + photo audit |
| Silver Rose Gold Brushed Off Set (123 views, 13 favs, 0 orders) | Strong interest, no sales | FIX-IN-PLACE: pricing issue most likely |

## Missing Data (Not in CSV)
These metrics require Etsy Shop Manager dashboard and were NOT in the CSV export:
- 30-day visits per listing
- 90-day orders per listing
- Favorites count
- Revenue per listing
- Search ranking position

Amir should export this data separately from Etsy Shop Manager > Listings manager > Export stats.