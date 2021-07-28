import os

DATA_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", ".data")
BOT_TOKEN = ''
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
        "channels_id": [861375048715993088],
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



