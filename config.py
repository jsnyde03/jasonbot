import os

DATA_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", ".data")
BOT_TOKEN = 'ODYwMzI5MDI3Mjk4MjYzMDUx.YN5p2A.k61S0AcVqgVo1i77Fwx6dc2wexo'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
NO_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/600px-No_image_available.svg.png"

LOG_FILE = os.path.join(DATA_FOLDER, "jasonbot.log")
LOG_FORMAT = "%(asctime)s [{}] %(levelname)s %(message)s"

TEST_CHANNEL_ID = 859943911908704277
TEST_MODE = False
DONT_PUBLISH = False
MAX_NEW_PRODUCTS = 3 if TEST_MODE else 500

DATABASE_FILES = {
    "shopify": os.path.join(DATA_FOLDER, "shopify_monitor.db"),
    "nonshopify": os.path.join(DATA_FOLDER, "nonshopifymonitor.db"),
    "restock": os.path.join(DATA_FOLDER, "restock_monitor.db"),
}

PID_FILES = {
    "shopify":os.path.join(DATA_FOLDER, "shopify_monitor.pid"),
    "nonshopify": os.path.join(DATA_FOLDER, "nonshopify_monitor.pid"),
    "restock": os.path.join(DATA_FOLDER, "restock_monitor.pid"),
}

KEYWORD_FILTERS = [{
    "keywords": ["star", "wars"],
    "channel_id": 796350028557975582,
    "operator": "and"
},{
    "keywords": ["crain"],
    "channel_id": 863834789656002560,
    "operator": "or"
},{
    "keywords": ["frison"],
    "channel_id": 806663098361839616,
    "operator": "or"
},{
    "keywords": ["momoko"],
    "channel_id": 806663147225219092,
    "operator": "or"
},{
    "keywords": ["quah"],
    "channel_id": 806663283893469264,
    "operator": "or"
},{
    "keywords": ["Dell'Otto", "DellOtto", "Dell Otto"],
    "channel_id": 806663382035726387,
    "operator": "or"
},{
    "keywords": ["gallagher"],
    "channel_id": 806663535148924998,
    "operator": "or"
},{
    "keywords": ["inhyuk"],
    "channel_id": 806663620318461993,
    "operator": "or"
},{
    "keywords": ["kirkham"],
    "channel_id": 807669379444899900,
    "operator": "or"
},{
    "keywords": ["mayhew"],
    "channel_id": 807670353002233896,
    "operator": "or"
},{
    "keywords": ["tyndall"],
    "channel_id": 807671238155042916,
    "operator": "or"
},{
    "keywords": ["campbell"],
    "channel_id": 807672114630230057,
    "operator": "or"
},{
    "keywords": ["greg horn"],
    "channel_id": 807676253313302539,
    "operator": "or"
},{
    "keywords": ["jeehyung"],
    "channel_id": 807678029408763944,
    "operator": "or"
},{
    "keywords": ["gleason"],
    "channel_id": 800333886026416138,
    "operator": "or"
},{
    "keywords": ["frank cho"],
    "channel_id": 812670368749846560,
    "operator": "or"
},{
    "keywords": ["kael ngu"],
    "channel_id": 812670478275444746,
    "operator": "or"
},{
    "keywords": ["parrillo"],
    "channel_id": 812670595271098378,
    "operator": "or"
},{
    "keywords": ["stegman"],
    "channel_id": 812670758358351883,
    "operator": "or"
},{
    "keywords": ["besch"],
    "channel_id": 812670851114991617,
    "operator": "or"
},{
    "keywords": ["christopher"],
    "channel_id": 864324259069558784,
    "operator": "or"
},{
    "keywords": ["witter"],
    "channel_id": 864324314634911754,
    "operator": "or"
},{
    "keywords": ["hughes"],
    "channel_id": 869764526881525760,
    "operator": "or"
}]

SHOPS = {
    "shopify": [{
        "domain": "frankiescomics.com",
        "name": "frankiescomics",
        "long_name": "Frankie's Comics",
        "logo": "https://cdn.shopify.com/s/files/1/1045/2402/t/4/assets/logo.png?v=8845134509068189876",
        "currency": "$",
        "channels_id": [791705478907559947],
        "group_variants": False
    },{
        "domain": "www.7ate9comics.com",
        "name": "7ate9comics",
        "long_name": "7 Ate 9 Comics",
        "logo": "https://cdn.shopify.com/s/files/1/1496/3582/files/7ate9_logo_white_ANIMATED_1_3d1dae48-dc38-4b57-aa45-9bab96fb3004_250x@2x.gif?v=1563037952",
        "currency": "£",
        "channels_id": [793506348272189491],
        "group_variants": False
    },{
        "domain": "www.hive-comics.com",
        "name": "hive-comics",
        "long_name": "Hive Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0343/7051/9084/files/hive_comics_540x.jpg?v=1584596772",
        "currency": "$",
        "channels_id": [793509547230494772],
        "group_variants": False
    },{
        "domain": "www.comicbooksurplus.com",
        "name": "linebreakers",
        "long_name": "Linebreakers",
        "logo": "https://cdn.shopify.com/s/files/1/0031/1099/4029/files/LINEBREAKERS_LOGO_180x.png?v=1598064169",
        "currency": "$",
        "channels_id": [796083946965565450],
        "group_variants": False
    },{ 
        "domain": "sanctumsanctorumcomics.com",
        "name": "sanctumsanctorumcomics",
        "long_name": "Sanctum Sanctorum Comics",
        "logo": "https://cdn.shopify.com/s/files/1/1080/7600/files/Sanctum-Sanctorum-Eyeball-Logo-Condensed-Tranparent-Final_200x.png?v=1577305158",
        "currency": "$",
        "channels_id": [791706117687476234],
        "group_variants": False
    },{
        "domain": "www.stadiumcomics.com",
        "name": "stadiumcomics",
        "long_name": "Stadium Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0227/7137/t/3/assets/logo.png?v=13301969214669996486",
        "currency": "$",
        "channels_id": [796083654937411674],
        "group_variants": True
    },{
        "domain": "stateofcomics.com",
        "name": "stateofcomics",
        "long_name": "State Of Comics",
        "logo": "https://cdn.shopify.com/s/files/1/1796/6731/files/Web_Logo_120x@2x.jpg?v=1521392087",
        "currency": "$",
        "channels_id": [796083776438272050],
        "group_variants": False
    },{
        "domain": "izzyscomics.com",
        "name": "izzyscomics",
        "long_name": "Izzys Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0406/6990/5049/files/Izzy_Comics_Logo_Color_9bd49f31-aeb2-4808-89ef-cf9fb4949fe0_180x.png?v=1607288086",
        "currency": "$",
        "channels_id": [796084072270004235],
        "group_variants": False
    },{
        "domain": "bigtimecollectibles.com",
        "name": "bigtimecollectibles",
        "long_name": "Big Time Collectibles",
        "logo": "https://cdn.shopify.com/s/files/1/2659/3382/files/btc_540x.jpg?v=1601523600",
        "currency": "$",
        "channels_id": [791706502087442442],
        "group_variants": False
    },{
        "domain": "thecomicmint.com",
        "name": "thecomicmint",
        "long_name": "The Comic Mint",
        "logo": "https://cdn.shopify.com/s/files/1/1570/4597/files/tcm_logo_225x@2x.png?v=1517036809",
        "currency": "$",
        "channels_id": [791705605139595324],
        "group_variants": False
    },{
        "domain": "www.comicselitecomics.com",
        "name": "comicselitecomics",
        "long_name": "Comics Elite",
        "logo": "https://cdn.shopify.com/s/files/1/1164/9704/files/8039816743733_6caf0770-2d11-43d4-bd83-91d20403f4ad_100x@2x.png?v=1509950346",
        "currency": "$",
        "channels_id": [791706250249109504],
        "group_variants": False
    },
    {
        "domain": "goldenapplecomics.com",
        "name": "goldenapplecomics",
        "long_name": "Golden Apple Comics",
        "logo": "https://cdn.shopify.com/s/files/1/2059/7683/files/GABANNER-HEADER7_800x@2x.jpg?v=1584202158",
        "currency": "$",
        "channels_id": [791705723407040523],
        "group_variants": False
    },{
        "domain": "shop.reedpop.com",
        "name": "reedpop",
        "long_name": "ReedPop",
        "logo": "https://cdn.shopify.com/s/files/1/0411/2256/2201/files/Screenshot_2020-06-15_at_11.06.37_400x@2x.png?v=1592215615",
        "currency": "$",
        "channels_id": [793509898540941382],
        "group_variants": True
    },{
        "domain": "www.sadlemoncomics.com",
        "name": "sadlemoncomics",
        "long_name": "Sad Lemon Comics",
        "logo": "https://cdn.shopify.com/s/files/1/1496/3484/t/9/assets/logo.png?v=4042678280299833177",
        "currency": "£",
        "channels_id": [793505824718192651],
        "group_variants": False
    },{
        "domain": "scottscollectables-shop.co.uk",
        "name": "scottscollectables",
        "long_name": "Scott's Collectables",
        "logo": "https://cdn.shopify.com/s/files/1/2585/0012/files/Scott_s_Logo_900x.jpg?v=1511688665",
        "currency": "£",
        "channels_id": [793506085897633802],
        "group_variants": False
    },{
        "domain": "www.slabbedheroes.com",
        "name": "slabbedheroes",
        "long_name": "Slabbed Heroes",
        "logo": "https://cdn.shopify.com/s/files/1/1832/0941/files/SHLogo_AbsCarn_blk_500x.jpg?v=1571533976",
        "currency": "$",
        "channels_id": [793508621165002763],
        "group_variants": False
    },{
        "domain": "www.slabcitycomics.com",
        "name": "slabcitycomics",
        "long_name": "Slab City Comics",
        "logo": "https://cdn.shopify.com/s/files/1/1671/7183/files/logo_shop_3cd74690-b271-4fad-9747-3caf18326959_50x@2x.png?v=1567214864",
        "currency": "£",
        "channels_id": [793508496854351892],
        "group_variants": False
    },{
        "domain": "trinity-comics.com",
        "name": "trinity-comics",
        "long_name": "Trinity Comics",
        "logo": "https://cdn.shopify.com/s/files/1/1796/9501/files/trinity_horizontal_80e878db-ddae-4ed6-ab09-944f6116f846_200x@2x.jpg?v=1603140623",
        "currency": "$",
        "channels_id": [793510092355797033],
        "group_variants": False
    },{
        "domain": "unknowncomicbooks.com",
        "name": "unknowncomicbooks",
        "long_name": "Unknown Comic Books",
        "logo": "https://cdn.shopify.com/s/files/1/1556/9595/files/BOXLOGOUCBUNKNOWNONLY_f46a7dcd-ed73-4107-a661-dddee69ededc_240x@2x.png?v=1588701261",
        "currency": "$",
        "channels_id": [791706014557798460],
        "group_variants": False 
    },{
        "domain": "blackcapecomics.com",
        "name": "blackcapecomics",
        "long_name": "Black Cape Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0325/8499/0851/files/colored_logo10_1080x.png?v=1583519149",
        "currency": "$",
        "channels_id": [796083386635518002],
        "group_variants": False
    },{
        "domain": "www.blackflagcomics.com",
        "name": "blackflagcomics",
        "long_name": "Black Flag Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0299/4025/2807/files/Screen_Shot_2020-01-09_at_10.13.15_PM_540x.png?v=1578626040",
        "currency": "$",
        "channels_id": [796083544858296341],
        "group_variants": False
    },{
        "domain": "mutantbeavercomics.com",
        "name": "mutantbeavercomics",
        "long_name": "Mutant Beaver Comics",
        "logo": "https://cdn.shopify.com/s/files/1/2797/0812/files/MBC_25429_540x.jpg?v=1550177352",
        "currency": "C$",
        "channels_id": [796084222447321169],
        "group_variants": False
    },{
        "domain": "krscomics.com",
        "name": "krscomics",
        "long_name": "KRS Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0951/5836/files/93950674_295647041422195_583726724571725824_n_300x.png?v=1588113586",
        "currency": "$",
        "channels_id": [796789438373429248],
        "group_variants": False
    },{
        "domain": "impulsecreations.com",
        "name": "impulsecreations",
        "long_name": "Impulse Creations",
        "logo": "https://cdn.shopify.com/s/files/1/0015/6873/5334/files/New_Logo_Small_white_300_111_450x@2x.jpg?v=1587866980",
        "currency": "$",
        "channels_id": [796791862627008552],
        "group_variants": False
    },{
        "domain": "the616comics.com",
        "name": "the616comics",
        "long_name": "The 616 Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0275/9858/5921/files/616_Logo_v5_540x.PNG?v=1591892468",
        "currency": "$",
        "channels_id": [806593546588258375],
        "group_variants": False
    },{
        "domain": "tylerkirkhamart.com",
        "name": "tylerkirkhamart",
        "long_name": "Tyler Kirkham",
        "logo": "https://cdn.shopify.com/s/files/1/0017/9663/6731/files/tyler_kirkham_smear_logonobackground_540x.png?v=1523561265",
        "currency": "$",
        "channels_id": [807669379444899900],
        "group_variants": False
    },{
        "domain": "comickingdomofcanada.com",
        "name": "comickingdomofcanada",
        "long_name": "Comic Kingdom Of Canada",
        "logo": "https://cdn.shopify.com/s/files/1/0012/0392/9182/files/IMG_8396_100x@2x.JPG?v=1530160618",
        "currency": "C$",
        "channels_id": [806595168442515506],
        "group_variants": False
    },{
        "domain": "www.mikemayhewstudio.com",
        "name": "mikemayhewstudio",
        "long_name": "Mike Mayhew",
        "logo": "https://cdn.shopify.com/s/files/1/0159/2514/9796/files/Mayhew_HiResSig_3_495x@2x.png?v=1547926426",
        "currency": "$",
        "channels_id": [807670353002233896],
        "group_variants": False
    },{
        "domain": "jamietyndall.net",
        "name": "jamietyndall",
        "long_name": "Jamie Tyndall",
        "logo": "https://cdn.shopify.com/s/files/1/0987/7290/files/name_x40@2x.jpg?v=1572544953",
        "currency": "$",
        "channels_id": [807671238155042916],
        "group_variants": False
    },{
        "domain": "jscottcampbell.com",
        "name": "jscottcampbell",
        "long_name": "J. Scott Campbell",
        "logo": "https://cdn.shopify.com/s/files/1/0990/1714/files/Campbell-WebLogo-2018_779c32d6-955e-489f-95b1-d7977c55de05_600x.jpg?v=1539378941",
        "currency": "$",
        "channels_id": [807672114630230057],
        "group_variants": False 
    },{
        "domain": "greghornart.com",
        "name": "greghornart",
        "long_name": "Greg Horn",
        "logo": "https://cdn.shopify.com/s/files/1/1775/7943/files/Greg_Horn_Art.new_logos_18.ENLARGED_720x.jpg?v=1521726376",
        "currency": "$",
        "channels_id": [807676253313302539],
        "group_variants": False
    },{
        "domain": "jeehyung.com",
        "name": "jeehyung.com",
        "long_name": "JeeHyung Lee",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS89grl7nQvWHvcY3Hch2x5O6ir7s3RjbSBhg&usqp=CAU",
        "currency": "$",
        "channels_id": [807678029408763944],
        "group_variants": False
    },{
        "domain": "www.yellowsnowcomics.com",
        "name": "yellowsnowcomics",
        "long_name": "Yellow Snow Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0465/8669/1752/files/ysn_01_190x@2x.png?v=1602273425",
        "currency": "$",
        "channels_id": [807679431245430794],
        "group_variants": False
    },{
        "domain": "amorphousink.com",
        "name": "amorphousink",
        "long_name": "Amorphous Ink",
        "logo": "https://cdn.shopify.com/s/files/1/2099/2991/files/Amorphous_Ink_Logo_92922d9a-92ac-4203-b331-7af600e1bb2c_200x@2x.png?v=1517041103",
        "currency": "$",
        "channels_id": [812671048616771644],
        "group_variants": False
    },{
        "domain": "www.wantedcomix.com",
        "name": "wantedcomix",
        "long_name": "Wanted Comix",
        "logo": "https://cdn.shopify.com/s/files/1/0537/5564/2021/files/wanted-comix-white_140x@2x.png?v=1613156568",
        "currency": "$",
        "channels_id": [812753506326675566],
        "group_variants": False
    },{
        "domain": "www.comicblend.com",
        "name": "comicblend",
        "long_name": "Comicblend",
        "logo": "https://cdn.shopify.com/s/files/1/0556/5752/9535/files/comicblend-for-dark-bgs_9d7c1b49-ec6c-4b9d-82b9-ef5fa97a5997_300x300.png?v=1616634090",        
        "currency": "$",
        "channels_id": [806581132468158474],
        "group_variants": False
    },{
        "domain": "www.claytoncrain.com",
        "name": "claytoncrain",
        "long_name": "Clayton Crain",
        "logo": "https://cdn.shopify.com/s/files/1/0541/9371/7437/files/Clayton_Crain_red_sm_400x.png?v=1620770711",
        "currency": "$",
        "channels_id": [863834789656002560],
        "group_variants": False
    },{
        "domain": "www.nocturnalrabbit.com",
        "name": "nocturnalrabbit",
        "long_name": "Nocturnal Rabbit",
        "logo": "https://cdn.shopify.com/s/files/1/0286/6600/3542/files/NRC_White_Shopify_15bb8d92-dc65-4cfb-ac65-85d5c35edb4f_150x150.jpg?v=1590251417",
        "currency": "$",
        "channels_id": [863904023555080192],
        "group_variants": False
    },{
        "domain": "www.scoutcomics.com",
        "name": "scoutcomics",
        "long_name": "Scout Comics",
        "logo": "https://cdn.shopify.com/s/files/1/0265/2585/9919/files/Scout_HQ_Logo.png?v=1567879425",
        "currency": "$",
        "channels_id": [793509988927668334],
        "group_variants": True
    },{
        "domain": "kirbyscomicartshop.com",
        "name": "kirbysart",
        "long_name": "Kirby's Comic Art",
        "logo": "https://cdn.shopify.com/s/files/1/0050/9991/3280/files/1_c85496b3-0683-4768-868b-665806be2265_450x.png?v=1609238580",
        "currency": "£",
        "channels_id": [868488920764149760],
        "group_variants": False

    },{
        "domain": "mondoshop.com",
        "name": "mondoshop",
        "long_name": "Mondo",
        "logo": "https://www.mondo.com",
        "currency": "$",
        "channels_id": [868497459167518750],
        "group_variants": False
    }],
    "nonshopify": [{
        "url": "https://www.tfaw.com/catalogsearch/result/index/?prod_type=3&product_list_order=on_sale_date&q=star+wars&product_list_limit=128",
        "name": "tfaw",
        "long_name": "Things From Another World",
        "logo": "https://www.tfaw.com/static/version1623786354/frontend/TFAW/default/en_US/images/logo.png",
        "channels_id": [792924094290198549],
    },{
        "url": "https://www.tfaw.com/catalogsearch/result/index/?prod_type=3&product_list_order=on_sale_date&q=copy&product_list_limit=128",
        "name": "tfaw",
        "long_name": "Things From Another World",
        "logo": "https://www.tfaw.com/static/version1608056150/frontend/TFAW/default/en_US/images/logo.png",
        "channels_id": [792924094290198549]
    },{
         "url": "https://www.tfaw.com/catalogsearch/result/?q=tfaw+exclusive/",
        "name": "tfaw",
        "long_name": "Things From Another World",
        "logo": "https://www.tfaw.com/static/version1608056150/frontend/TFAW/default/en_US/images/logo.png",
        "channels_id": [792924094290198549]

    },{ 
        "url": "https://forbiddenplanet.com/catalog/comics-and-graphic-novels/comics/?sort=recently-added&page=1",
        "name": "forbiddenplanet",
        "long_name": "Forbidden Planet",
        "logo": "https://forbiddenplanet.com/static/images/rocket.da7a6f895f02.png",
        "channels_id": [793506266215481355]
    },{
        "url": "https://legacycomics.com/product-category/comics/?orderby=date",
        "name": "legacycomics",
        "long_name": "Legacy Comics And Cards",
        "logo": "https://legacycomics.com/wp-content/themes/legacy-prime/library/images/logo.png",
        "channels_id": [793509690998128640]
    },{
        "url": "https://www.midtowncomics.com/search?pp=100&pj=1&rel=1",
        "name": "midtowncomics",
        "long_name": "Midtown Comics",
        "logo": "https://www.midtowncomics.com/images/logos/midtown/midtown_logo.png",
        "channels_id": [796496537127092254]
    },{
        "url": "https://madcavestudios.com/comics/search/?filters=product_cat[200]",
        "name": "madcavestudios",
        "long_name": "Mad Cave Studios",
        "logo": "https://madcavestudios.com/wp-content/uploads/2018/03/madcave-logo-1.svg",
        "channels_id": [863834484615807027]
   },{
       "url": "https://www.thecomiccornerstore.com/store",
       "name": "thecornercomic",
       "long_name": "The Corner Comic",
       "logo": "https://images.squarespace-cdn.com/content/v1/6005c8dd6f0b7e66aaa739f9/1620605244611-65RZVCCHCQPGWDQ1SXWN/The+Comic+Corner+Logo.png?format=1500w",
       "channels_id": [863834368329383976]

   },{
       "url": "https://www.thecomiccornerstore.com/store/exclusives",
       "name": "thecornercomic",
       "long_name": "The Corner Comic",
       "logo": "https://images.squarespace-cdn.com/content/v1/6005c8dd6f0b7e66aaa739f9/1620605244611-65RZVCCHCQPGWDQ1SXWN/The+Comic+Corner+Logo.png?format=1500w",
       "channels_id": [863834368329383976]

   },{
       "url": "https://www.scorpioncomics.com/shop",
       "name": "scorpioncomics",
       "long_name": "Scorpion Comics",
       "logo": "https://images.squarespace-cdn.com/content/v1/5716ec2d859fd035924f1f3f/1555635919587-AUK7DTLO445PITJXL4RF/IMG_1255.PNG?format=original",
       "channels_id": [814267645608067092]
   },{
        "url": "https://www.archonia.com/en-us/search?qf%5B0%5D=3006&sort=inserted_timestamp_desc",
        "name": "archonia",
        "long_name": "Archonia.com",
        "logo": "https://cdn.archonia.com/shop/test-home/misc/archonia-no-cats-transparant_short6.png",
        "channels_id": [863793950837309490]
   },{
        "url": "https://www.hallmark.com/popminded/?prefn0=theme&prefv0=Events#products",
        "name": "hallmark",
        "long_name": "Hallmark PopMinded",
        "logo": "https://www.hallmark.com/on/demandware.static/-/Sites-HallmarkUS-Library/default/dw5c27acda/09-10-20-popminded-logo.svg",
        "channels_id": [867790088545107978]
   }],
    "restock": [{
        "name": "lego.com",
        "selector": 'p[data-test="product-overview-availability"] span',
        "in_stock_string": "Available now",
        "backorder_string": "Backorders accepted, will ship in 60 days",
        "outofstock_string": "Temporarily out of stock",
        "channels_id": [793510290209112064],
        "urls": [
            "https://www.lego.com/en-us/product/r2-d2-75308",
            "https://www.lego.com/en-us/product/typewriter-21327",
            "https://www.lego.com/en-us/product/world-map-31203",
            "https://www.lego.com/en-us/product/daily-bugle-76178",
            "https://www.lego.com/en-us/product/lego-star-wars-advent-calendar-2021-75307",
            "https://www.lego.com/en-us/product/republic-gunship-75309",
            "https://www.lego.com/en-us/product/volkswagen-t2-camper-van-10279",
            "https://www.lego.com/en-us/product/the-guardians-ship-76193",
            "https://www.lego.com/en-us/product/the-bad-batch-attack-shuttle-75314",
            "https://www.lego.com/en-us/product/boba-fett-s-starship-75312",
            "https://www.lego.com/en-us/product/gingerbread-house-10267",
            "https://www.lego.com/en-us/product/darth-vader-s-castle-75251",
            "https://www.lego.com/en-us/product/diagon-alley-75978",
            "https://www.lego.com/en-us/product/mos-eisley-cantina-75290"

        ]
    }],
}



