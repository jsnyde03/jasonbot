import hashlib
import sqlite3
import asyncio
import logging
import importlib
from discord.colour import Colour
from discord.embeds import Embed
import requests
from bs4 import BeautifulSoup
import config, shops_monitor, proxies

class NonShopifyMonitor(shops_monitor.ShopsMonitor):

    def __init__(self):
        super().__init__("nonshopify")

    def get_product_hash(self, shop, product):
        digest = "".join([
            shop["name"],
            product["url"],
            product["price"],
            product["image"]
        ])
        return hashlib.sha256(digest.encode('utf-8')).hexdigest()[0:10]

    def gen_new_embeds(self, shop, product):
        if(shop["name"]) == "lego":
            product_hash = self.get_product_hash(shop, product)
            if self.product_exists(product_hash):
                return []
                
            embed = Embed(title=product["title"], url=product["url"], color=Colour(0x245100))
            embed.set_image(url=product["image"])
            embed.add_field(name="Price", value=product["price"], inline=False)
            embed.add_field(name="Availability", value=product["availability"], inline=False)
            embed.add_field(name="VIP", value=product["vip"], inline=False)
            embed.set_author(name=shop["long_name"], url=shop["url"], icon_url=shop["logo"])
        else:
            product_hash = self.get_product_hash(shop, product)
            if self.product_exists(product_hash):
                return []
                
            embed = Embed(title=product["title"], url=product["url"], color=Colour(0x245100))
            embed.set_thumbnail(url=product["image"])
            embed.add_field(name="Price", value=product["price"], inline=False)
            embed.set_author(name=shop["long_name"], url=shop["url"], icon_url=shop["logo"])

        return [{
            "embed": embed,
            "product_hash": product_hash,
            "channels_id": shop["channels_id"],
            "shop_name": shop["name"]
        }]

    def get_shop_new_products(self, shop):
        logging.info("Checking {}...".format(shop["name"]))

        shop_module = importlib.import_module('JasonBot.shops.{}'.format(shop["name"]))
        if shop.get("custom_request") == True:
            shop_products = shop_module.find_products(shop)
        else:
            headers = {'User-Agent': config.USER_AGENT}
            response = requests.get(shop["url"], headers=headers) 
            shop_products = shop_module.find_products(response)
        products = []
        for product in shop_products:
            products = products + self.gen_new_embeds(shop, product)
            if len(products) > config.MAX_NEW_PRODUCTS:
                break

        logging.info("New products: {}".format(len(products)))
        return products