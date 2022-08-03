import yfinance as yf

tickers = ["AAN","AAOI","AAON","AAT","AAWW","AAXN","ABCB","ABEO","ABG","ABM","ABTX","AC","ACA","ACAD","ACBI","ACCO","ACER",
"ACHN","ACIA","ACIW","ACLS","ACNB","ACOR","ACRE","ACRS","ACRX","ACTG","ADC","ADES","ADMA","ADMS","ADNT","ADRO","ADSW","ADTN",
"ADUS","ADVM","AEGN","AEIS","AEL","AEO","AERI","AFI","AFIN","AFMD","AGE","AGEN","AGLE","AGM","AGS","AGX","AGYS","AHH","AHT",
"AI","AIMC","AIMT","AIN","AIR","AIRG","AIT","AJRD","AJX","AKBA","AKCA","AKR","AKRO","AKRX","AKS","AKTS","ALBO","ALCO","ALDR",
"ALDX","ALE","ALEC","ALEX","ALG","ALGT","ALLK","ALLO","ALOT","ALRM","ALTM","ALTR","ALX","AMAG","AMAL","AMBA","AMBC","AMC",
"AMED","AMEH","AMK","AMKR","AMN","AMNB","AMOT","AMPH","AMRC","AMRS","AMRX","AMSC","AMSF","AMSWA","AMTB","AMWD","ANAB","ANDE",
"ANF","ANGO","ANH","ANIK","ANIP","AOBC","AOSL","APAM","APEI","APLS","APOG","APPF","APPN","APPS","APTS","APYX","AQUA","ARA",
"ARAY","ARCB","ARCH","ARDX","ARES","ARGO","ARI","ARL","ARLO","ARNA","AROC","AROW","ARQL","ARR","ARTNA","ARVN","ARWR","ASC",
"ASGN","ASIX","ASMB","ASNA","ASPS","ASRT","ASTE","AT","ATEC","ATEN","ATEX","ATGE","ATHX","ATI","ATKR","ATLO","ATNI","ATNX",
"ATRA","ATRC","ATRI","ATRO","ATRS","ATSG","AUB","AVA","AVAV","AVCO","AVD","AVDR","AVID","AVNS","AVRO","AVX","AVXL","AVYA",
"AWR","AX","AXAS","AXDX","AXE","AXGN","AXL","AXLA","AXNX","AXSM","AXTI","AYR","AZZ","B","BANC","BAND","BANF","BANR","BATRA",
"BATRK","BBBY","BBCP","BBIO","BBSI","BBX","BCBP","BCC","BCEI","BCEL","BCML","BCO","BCOR","BCOV","BCPC","BCRX","BDC","BDGE",
"BDSI","BE","BEAT","BECN","BELFB","BFC","BFIN","BFS","BFST","BGG","BGS","BGSF","BH","BHB","BHE","BHLB","BHR","BHVN","BIG",
"BIOS","BJ","BJRI","BKD","BKE","BKH","BL","BLBD","BLD","BLDR","BLFS","BLKB","BLMN","BLX","BMCH","BMI","BMRC","BMTC","BNED",
"BNFT","BOCH","BOLD","BOMN","BOOM","BOOT","BOX","BPFH","BPMC","BPRN","BRC","BREW","BRG","BRID","BRKL","BRKS","BRT","BRY",
"BSET","BSGM","BSIG","BSRR","BSTC","BSVN","BTAI","BTU","BUSE","BV","BWB","BWFG","BXC","BXG","BXMT","BXS","BY","BYD","BYSI","BZH",
"CAC","CADE","CAI","CAKE","CAL","CALA","CALM","CALX","CAMP","CAR","CARA","CARB","CARE","CARG","CARO","CARS","CASA","CASH","CASI",
"CASS","CATC","CATM","CATO","CATS","CATY","CBAN","CBAY","CBB","CBL","CBLK","CBM","CBMG","CBNK","CBPX","CBRL","CBTX","CBU","CBZ",
"CCB","CCBG","CCF","CCMP","CCNE","CCO","CCOI","CCRN","CCS","CCXI","CDE","CDLX","CDMO","CDNA","CDR","CDXC","CDXS","CDZI","CECE",
"CECO","CEIX","CELC","CELH","CENT","CENTA","CENX","CERC","CERS","CETV","CEVA","CFB","CFFI","CFFN","CFMS","CHAP","CHCO","CHCT",
"CHDN","CHEF","CHGG","CHMA","CHMG","CHMI","CHRA","CHRS","CHS","CHUY","CIA","CIO","CIR","CISN","CIVB","CIX","CJ","CKH","CKPT",
"CLAR","CLBK","CLCT","CLDR","CLDT","CLF","CLFD","CLI","CLNC","CLNE","CLPR","CLVS","CLW","CLXT","CMBM","CMC","CMCO","CMCT",
"CMLS","CMO","CMP","CMPR","CMRE","CMRX","CMTL","CNBKA","CNCE","CNDT","CNMD","CNNE","CNO","CNOB","CNR","CNS","CNSL","CNST",
"CNTY","CNX","CNXN","CODA","COHU","COKE","COLB","COLL","CONN","COOP","CORE","CORR","CORT","COWN","CPE","CPF","CPK","CPLG",
"CPRX","CPS","CPSI","CRAI","CRBP","CRC","CRCM","CRD.A","CRK","CRMD","CRMT","CRNX","CROX","CRS","CRTX","CRUS","CRVL","CRY",
"CRZO","CSFL","CSGS","CSII","CSLT","CSOD","CSTE","CSTL","CSTR","CSV","CSWI","CTB","CTBI","CTMX","CTO","CTRA","CTRC","CTRE",
"CTRN","CTS","CTSO","CTT","CTWS","CUB","CUBI","CUE","CULP","CURO","CUTR","CVA","CVBF","CVCO","CVCY","CVGI","CVGW","CVI",
"CVIA","CVLT","CVLY","CVM","CVRS","CVTI","CWCO","CWEN","CWEN.A","CWH","CWK","CWST","CWT","CXW","CYCN","CYH","CYRX","CYTK",
"CZNC","DAKT","DAN","DAR","DBD","DBI","DCO","DCOM","DCPH","DDD","DDS","DEA","DECK","DENN","DERM","DF","DFIN","DGICA","DGII",
"DHIL","DHT","DHX","DIN","DIOD","DJCO","DK","DLA","DLTH","DLX","DMRC","DNBF","DNLI","DNOW","DNR","DO","DOC","DOMO","DOOR","DORM",
"DOVA","DPLO","DRH","DRNA","DRQ","DS","DSKE","DSPG","DSSI","DTIL","DVAX","DX","DXPE","DY","DZSI","EAT","EB","EBF","EBIX","EBS",
"EBSB","EBTC","ECHO","ECOL","ECOM","ECOR","ECPG","EDIT","EE","EEX","EFC","EFSC","EGAN","EGBN","EGHT","EGLE","EGOV","EGP","EGRX",
"EHTH","EIDX","EIG","EIGI","EIGR","ELF","ELOX","ELVT","ELY","EME","EML","ENDP","ENFC","ENOB","ENPH","ENS","ENSG","ENTA","ENV",
"ENVA","ENZ","EOLS","EPAY","EPC","EPM","EPRT","EPZM","EQBK","ERA","ERI","ERII","EROS","ESCA","ESE","ESGR","ESNT","ESPR","ESQ",
"ESSA","ESTE","ESXB","ETH","ETM","EVBG","EVBN","EVC","EVER","EVFM","EVH","EVI","EVLO","EVOP","EVRI","EVTC","EXLS","EXPI","EXPO",
"EXPR","EXTN","EXTR","EYE","EYPT","EZPW","FARM","FARO","FATE","FBC","FBIZ","FBK","FBM","FBMS","FBNC","FBP","FC","FCAP","FCBC",
"FCBP","FCCY","FCF","FCFS","FCN","FCPT","FDBC","FDEF","FDP","FELE","FET","FF","FFBC","FFG","FFIC","FFIN","FFNW","FFWM","FG",
"FGBI","FGEN","FI","FIBK","FII","FISI","FIT","FIVN","FIX","FIXX","FIZZ","FLDM","FLIC","FLMN","FLNT","FLOW","FLWS","FLXN","FLXS",
"FMAO","FMBH","FMBI","FMNB","FN","FNCB","FNHC","FNKO","FNLC","FNWB","FOCS","FOE","FOLD","FOR","FORM","FORR","FOSL","FOXF","FPI",
"FPRX","FR","FRAC","FRAF","FRBA","FRBK","FRGI","FRME","FRPH","FRPT","FRTA","FSB","FSBW","FSCT","FSP","FSS","FSTR","FTK","FTR",
"FTSI","FTSV","FUL","FULC","FULT","FVCB","FWRD","GABC","GAIA","GALT","GATX","GBCI","GBL","GBLI","GBT","GBX","GCAP","GCBC","GCI",
"GCO","GCP","GDEN","GDOT","GDP","GEF","GEF.B","GEN","GENC","GEO","GEOS","GERN","GES","GFF","GFN","GHDX","GHL","GHM","GIII","GKOS",
"GLDD","GLNG","GLOG","GLRE","GLT","GLUU","GLYC","GME","GMED","GMRE","GMS","GNC","GNE","GNK","GNL","GNLN","GNMK","GNRC","GNTY","GNW",
"GOGO","GOLF","GOOD","GORO","GOSS","GPI","GPMT","GPOR","GPRE","GPRO","GPX","GRBK","GRC","GRIF","GRPN","GRTS","GSBC","GSHD","GSIT",
"GTHX","GTLS","GTN","GTS","GTT","GTY","GTYH","GVA","GWB","GWGH","GWRS","HA","HABT","HAE","HAFC","HALL","HALO","HARP","HASI","HAYN",
"HBB","HBCP","HBMD","HBNC","HCAT","HCC","HCCI","HCI","HCKT","HCSG","HEES","HELE","HFFG","HFWA","HI","HIBB","HIFS","HIIQ","HL","HLI",
"HLIO","HLIT","HLNE","HLX","HMHC","HMN","HMST","HMSY","HMTV","HNGR","HNI","HNRG","HOFT","HOMB","HOME","HONE","HOOK","HOPE","HPR","HQY",
"HR","HRI","HRTG","HRTX","HSC","HSII","HSKA","HSTM","HT","HTBI","HTBK","HTH","HTLD","HTLF","HTZ","HUBG","HUD","HURC","HURN","HVT","HWBK",
"HWC","HWKN","HY","HZO","I","IBCP","IBKC","IBOC","IBP","IBTX","ICD","ICFI","ICHR","ICPT","IDCC","IDEX","IDT","IESC","IHC","III","IIIN",
"IIIV","IIN","IIPR","IIVI","ILPT","IMAX","IMGN","IMKTA","IMMR","IMMU","IMXI","INBK","INDB","INFN","INGN","INN","INO","INOV","INS","INSE","INSG",
"INSM","INSP","INST","INSW","INT","INTL","INVA","INWK","IOSP","IOTS","IOVA","IPAR","IPHI","IPHS","IPI","IRBT","IRDM","IRET","IRMD","IRT","IRTC",
"IRWD","ISBC","ISCA","ISRL","ISTR","ITCI","ITGR","ITI","ITIC","ITRI","IVC","IVR","JACK","JAG","JAX","JBSS","JBT","JCAP","JCOM","JCP","JELD","JILL",
"JJSF","JNCE","JOE","JOUT","JRVR","JYNT","KAI","KALA","KALU","KALV","KAMN","KBAL","KBH","KBR","KDMN","KE","KELYA","KEM","KFRC","KFY","KIDS","KIN",
"KLDO","KLXE","KMT","KN","KNL","KNSA","KNSL","KOD","KOP","KPTI","KRA","KREF","KRG","KRNY","KRO","KRTX","KRUS","KRYS","KTB","KTOS","KURA","KVHI","KW",
"KWR","KZR","LAD","LADR","LANC","LAND","LASR","LAUR","LAWS","LBAI","LBC","LBRT","LC","LCI","LCII","LCNB","LCTX","LCUT","LDL","LE","LEAF","LEE","LEGH",
"LEVL","LFVN","LGIH","LGND","LHCG","LILA","LILAK","LIND","LITE","LIVN","LIVX","LJPC","LKFN","LKSD","LL","LLNW","LMAT","LMNR","LMNX","LNDC","LNN","LNTH",
"LOB","LOCO","LOGC","LORL","LOVE","LPG","LPI","LPSN","LPX","LQDA","LQDT","LRN","LSCC","LTC","LTHM","LTRPA","LTS","LTXB","LVGO","LXFR","LXP","LXRX","LXU",
"LZB","MANT","MATW","MATX","MAXR","MBI","MBII","MBIN","MBIO","MBUU","MBWM","MC","MCB","MCBC","MCFT","MCHX","MCRB","MCRI","MCRN","MCS","MDC","MDCA","MDCO",
"MDGL","MDP","MDR","MDRX","MEC","MED","MEDP","MEET","MEI","MEIP","MESA","METC","MFIN","MFNC","MFSF","MG","MGEE","MGLN","MGNX","MGPI","MGRC","MGTA","MGTX",
"MGY","MHO","MIK","MINI","MIRM","MITK","MITT","MJCO","MLAB","MLHR","MLI","MLND","MLP","MLR","MLVF","MMAC","MMI","MMS","MMSI","MNK","MNKD","MNLO","MNOV",
"MNR","MNRL","MNRO","MNSB","MNTA","MOBL","MOD","MODN","MOFG","MOG.A","MORF","MOV","MPAA","MPB","MPX","MR","MRC","MRCY","MRKR","MRLN","MRNS","MRSN","MRTN",
"MRTX","MSA","MSBI","MSEX","MSGN","MSON","MSTR","MTDR","MTEM","MTH","MTOR","MTRN","MTRX","MTSC","MTSI","MTW","MTX","MTZ","MUSA","MVBF","MWA","MXL","MYE",
"MYGN","MYOK","MYRG","NANO","NAT","NATH","NATR","NAV","NBEV","NBHC","NBN","NBR","NBTB","NC","NCBS","NCI","NCMI","NCSM","NDLS","NE","NEO","NEOG","NERV",
"NESR","NEWM","NEXT","NFBK","NG","NGHC","NGM","NGS","NGVC","NGVT","NHC","NHI","NINE","NJR","NKSH","NL","NMIH","NMRK","NNBR","NNI","NODK","NOG","NOVA",
"NOVT","NP","NPK","NPO","NPTN","NR","NRC","NRCG","NRIM","NSA","NSIT","NSP","NSSC","NSTG","NTB","NTCT","NTGN","NTGR","NTLA","NTRA","NTUS","NUVA","NVAX",
"NVCR","NVEC","NVEE","NVRO","NVTA","NWBI","NWE","NWFL","NWLI","NWN","NWPX","NX","NXGN","NXRT","NXTC","NYMT","NYNY","OAS","OBNK","OCFC","OCN","OCUL",
"OCX","ODC","ODP","ODT","OEC","OFG","OFIX","OFLX","OGS","OII","OIS","OLBK","OLP","OMCL","OMER","OMI","OMN","ONB","ONCE","ONDK","OOMA","OPB","OPBK","OPI",
"OPK","OPRX","OPTN","OPY","ORA","ORBC","ORC","ORGO","ORIT","ORRF","OSBC","OSG","OSIS","OSMT","OSPN","OSTK","OSUR","OSW","OTTR","OVBC","OVLY","OXM","PACB",
"PACD","PAHC","PAR","PARR","PATK","PAYS","PBFS","PBH","PBI","PBIP","PBPB","PBYI","PCB","PCH","PCRX","PCSB","PCYO","PDCE","PDCO","PDFS","PDLB","PDLI","PDM",
"PEB","PEBK","PEBO","PEGI","PEI","PENN","PETQ","PETS","PFBC","PFBI","PFGC","PFIS","PFNX","PFS","PFSI","PGC","PGNX","PGTI","PHAS","PHR","PHUN","PHX","PI",
"PICO","PIRS","PJC","PJT","PKBK","PKD","PKE","PKOH","PLAB","PLAY","PLCE","PLMR","PLOW","PLPC","PLSE","PLT","PLUG","PLUS","PLXS","PMBC","PMT","PNM","PNRG",
"PNTG","POL","POR","POWI","POWL","PPBI","PQG","PRA","PRAA","PRFT","PRGS","PRGX","PRIM","PRK","PRLB","PRMW","PRNB","PRO","PROS","PROV","PRPL","PRSC","PRSP",
"PRTA","PRTH","PRTK","PRTY","PRVL","PSB","PSDO","PSMT","PSN","PSNL","PTCT","PTE","PTGX","PTLA","PTN","PTSI","PTVCB","PUB","PUMP","PVAC","PVBC","PWOD","PYX",
"PZN","PZZA","QADA","QCRH","QDEL","QEP","QLYS","QNST","QTRX","QTS","QTWO","QUAD","QUOT","RAD","RAMP","RARE","RARX","RAVN","RBB","RBBN","RBCAA","RBNC","RC",
"RCII","RCKT","RCKY","RCM","RCUS","RDFN","RDI","RDN","RDNT","RDUS","REAL","RECN","REGI","REI","REPH","REPL","RES","RESI","RETA","REV","REVG","REX","REXR",
"RFL","RGCO","RGEN","RGNX","RGR","RGS","RH","RHP","RICK","RIGL","RILY","RLGT","RLGY","RLH","RLI","RLJ","RM","RMAX","RMBI","RMBS","RMNI","RMR","RMTI","RNET",
"RNST","ROAD","ROAN","ROCK","ROG","ROIC","ROLL","ROSE","RPD","RPT","RRBI","RRD","RRGB","RRR","RRTS","RST","RTEC","RTIX","RTRX","RTW","RUBI","RUBY","RUN",
"RUSHA","RUSHB","RUTH","RVI","RVNC","RVSB","RWT","RXN","RYAM","RYI","RYTM","SAFE","SAFM","SAFT","SAH","SAIA","SAIC","SAIL","SALT","SAM","SAMG","SANM","SASR",
"SAVE","SB","SBBP","SBBX","SBCF","SBH","SBOW","SBRA","SBSI","SBT","SCHL","SCHN","SCL","SCOR","SCS","SCSC","SCU","SCVL","SCWX","SD","SDRL","SEAS","SEM",
"SEMG","SENEA","SENS","SF","SFBS","SFE","SFIX","SFL","SFNC","SFST","SGA","SGC","SGH","SGMO","SGMS","SGRY","SHAK","SHBI","SHEN","SHO","SHOO","SHSP","SIBN",
"SIC","SIEB","SIEN","SIG","SIGA","SIGI","SILK","SITE","SJI","SJW","SKT","SKY","SKYW","SLAB","SLCA","SLCT","SLDB","SLP","SM","SMBC","SMBK","SMHI","SMMF","SMP",
"SMPL","SMTC","SNBR","SNCR","SND","SNDX","SNH","SNR","SOI","SOLY","SONA","SONM","SONO","SP","SPAR","SPFI","SPKE","SPNE","SPOK","SPPI","SPRO","SPSC","SPTN",
"SPWH","SPWR","SPXC","SR","SRCE","SRCI","SRDX","SRG","SRI","SRNE","SRRK","SRT","SSB","SSD","SSP","SSTI","SSTK","SSYS","STAA","STAG","STAR","STBA","STC","STFC",
"STIM","STML","STMP","STNG","STOK","STRA","STRL","STRO","STRS","STXB","SUM","SUPN","SVMK","SVRA","SWAV","SWM","SWN","SWX","SXC","SXI","SXT","SYBT","SYBX",
"SYKE","SYNA","SYNH","SYNL","SYRS","SYX","TACO","TALO","TAST","TBBK","TBI","TBIO","TBK","TBNK","TBPH","TCBK","TCDA","TCFC","TCI","TCMD","TCRR","TCS","TCX",
"TDOC","TDW","TECD","TELL","TEN","TENB","TERP","TESS","TEUM","TEX","TG","TGH","TGI","TGNA","TGTX","TH","THC","THFF","THOR","THR","THRM","TILE","TIPT","TISI",
"TITN","TIVO","TK","TLRA","TLRD","TLYS","TMDX","TMHC","TMP","TMST","TNAV","TNC","TNDM","TNET","TNK","TOCA","TORC","TOWN","TPB","TPC","TPCO","TPH","TPIC","TPRE",
"TPTX","TR","TRC","TREC","TREX","TRHC","TRMK","TRNO","TRNS","TROX","TRS","TRST","TRTN","TRTX","TRUE","TRUP","TRWH","TRXC","TSBK","TSC","TSE","TTEC","TTEK","TTGT",
"TTI","TTMI","TTS","TUP","TUSK","TVTY","TWI","TWIN","TWNK","TWST","TXMD","TXRH","TYME","TYPE","TZOO","UBA","UBFO","UBNK","UBSI","UBX","UCBI","UCFC","UCTT","UE",
"UEC","UEIC","UFCS","UFI","UFPI","UFPT","UHT","UIHC","UIS","ULH","UMBF","UMH","UNB","UNF","UNFI","UNIT","UNT","UNTY","UPLD","UPWK","URGN","USCR","USLM","USNA",
"USPH","USWS","USX","UTL","UTMD","UUUU","UVE","UVSP","UVV","VAC","VALU","VAPO","VBIV","VBTX","VC","VCEL","VCRA","VCYT","VEC","VECO","VG","VGR","VHC","VHI","VIAV",
"VICR","VIVO","VKTX","VLGEA","VLY","VNCE","VNDA","VPG","VRA","VRAY","VRCA","VREX","VRNS","VRNT","VRRM","VRS","VRTS","VRTU","VRTV","VSEC","VSH","VSLR","VSTO","VVI",
"VYGR","WAAS","WABC","WAFD","WAIR","WASH","WATT","WBT","WD","WDFC","WDR","WERN","WETF","WEYS","WGO","WHD","WHG","WIFI","WINA","WING","WIRE","WK","WLDN","WLFC",
"WLH","WLL","WMC","WMGI","WMK","WMS","WNC","WNEB","WOR","WOW","WPG","WRE","WRLD","WRTC","WSBC","WSBF","WSC","WSFS","WSR","WTBA","WTI","WTRE","WTRH","WTS","WTTR",
"WVE","WW","WWW","XAN","XBIT","XELA","XENT","XERS","XFOR","XHR","XLRN","XNCR","XOG","XON","XPER","XXII","YCBD","YELP","YETI","YEXT","YGYI","YMAB","YORW","YRCW",
"ZAGG","ZEUS","ZGNX","ZIOP","ZIXI","ZUMZ","ZUO","ZYNE","ZYXI"]

test = ["AAPL" ,"MSFT"]

data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = tickers,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1y",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'column',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

data2 = data.unstack(level=-1) 
data2 = data2.reset_index()
data2 = data2.pivot(index = ["level_1","Date"], columns = ["level_0"], values = 0) 
data2 = data2.reset_index()
data2 = data2.rename(columns = {"level_1": "Ticker"}) 

import sqlite3 as sq
table_name = "stock_database" # table and file name

conn = sq.connect('{}.sqlite'.format(table_name)) # creates file
data2.to_sql(table_name, conn, if_exists='replace', index=False) # writes to file
conn.close() 

