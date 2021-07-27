import hashlib
import sqlite3
import asyncio
import logging
import requests
from bs4 import BeautifulSoup
from discord import Embed, Colour, embeds
import config, shops_monitor

class ShopifyMonitor(shops_monitor.ShopsMonitor):

    def __init__(self, proxies={}):
        self.proxies = proxies
        super().__init__("shopify")

    def search_image(self, variant_id, images):
        if images is None or len(images) == 0:
            return config.NO_IMAGE_URL
        if len(images) == 1:
            return images[0]["src"]
        for image in images:
            if variant_id in image["variant_ids"]:
                return image["src"]
        for image in images:
            if len(image["variant_ids"]) == 0:
                return image["src"]
        return images[0]["src"]
    
    def get_product_hash(self, shop, variant, image):
        digest = "".join([
            shop["domain"],
            str(variant["id"]),
            str(variant["price"]),
            image
        ])
        return hashlib.sha256(digest.encode('utf-8')).hexdigest()[0:10]

    def get_product_quantity(self, shop, handle):
        quantities = {}
        headers = {'User-Agent': config.USER_AGENT}
        url = "https://{}/products/{}.json".format(shop["domain"], handle)
        if "http" in self.proxies:
           logging.info("PROXY: {}".format(self.proxies["http"]))
        response = requests.get(url, headers=headers, proxies = self.proxies)
        product = response.json()["product"]
        for variant in product["variants"]:
            quantities[variant["id"]] = variant.get("inventory_quantity", "unknown")
        return quantities
    
    def get_variants_price(self, shop, variants):
        prices = [variant["price"] for variant in variants]
        min_price = min(prices)
        max_price = max(prices)
        price = "{}{}".format(shop["currency"], min_price)
        if min_price < max_price:
            price = "From {} to {}{}".format(price, shop["currency"], max_price)
        return price
    
    def gen_variant_embed(self, shop, product, variant, image, quantity):
        title = "{} - {}".format(product["title"], variant["title"])
        price = "{}{}".format(shop["currency"], variant["price"])
        product_url = "https://{}/products/{}?variant={}".format(shop["domain"], product["handle"], variant["id"])
        shop_url = "https://{}/collections/all?sort_bye=created-descending".format(shop["domain"])
        atc_url = "https://{}/cart/add?id={}&quantity=1".format(shop["domain"], variant["id"])

        embed = Embed(title=title, url=product_url, color=Colour(0x246100))
        embed.set_thumbnail(url=image)
        embed.add_field(name="Price", value=price, inline=False)
        embed.add_field(name="Available quantity", value=quantity, inline=False)
        embed.add_field(name="Add to cart", value=atc_url, inline=False)
        embed.set_author(name=shop["long_name"], url=shop_url, icon_url=shop["logo"])
        return embed
    
    def gen_group_embed(self, shop, product, image):
        title = product["title"]
        price = self.get_variants_price(shop, product["variants"])
        product_url = "https://{}/products/{}".format(shop["domain"], product["handle"])
        shop_url = "https://{}/collections.all?sort_by=created-descending".format(shop["domain"])

        embed = Embed(title=title, url=product_url, color=Colour(0x246100))
        embed.set_thumbnail(url=image)
        embed.add_field(name="Price", value=price, inline=False)
        embed.add_field(name="Variants", value="--------------", inline=False)
        for variant in product["variants"]:
            name = "{} - ({}{})".format(variant["title"], shop["currency"], variant["price"])
            value = "https://{}/cart/add?id={}&quantity=1".format(shop["domain"], variant["id"])
            embed.add_field(name=name, value=value, inline=False)
        return embed

    def gen_new_embeds_grouped(self, shop, product):
        variant = product["variants"][0]
        image = self.search_image(variant["id"], product["images"])
        product_hash = self.get_product_hash(shop, variant, image)
        if self.product_exists(product_hash):
            return []
        return [{
            "embed": self.gen_group_embed(shop, product, image),
            "product_hash": product_hash,
            "channels_id": shop["channels_id"],
            "shop_name": shop["name"]
        }]

    def gen_new_embeds(self, shop, product):
        products = []
        quantities = None
        for variant in product["variants"]:
            image = self.search_image(variant["id"], product["images"])
            product_hash = self.get_product_hash(shop, variant, image)
            if not self.product_exists(product_hash):
                if quantities is None:
                    quantities= self.get_product_quantity(shop, product["handle"])
                quantity = quantities.get(variant["id"], "unknown")
                products.append({
                    "embed": self.gen_variant_embed(shop, product, variant, image, quantity),
                    "product_hash": product_hash,
                    "channels_id": shop["channels_id"],
                    "shop_name": shop["name"]
                })
        return products
    
    def get_shop_new_products(self, shop):
        logging.info("Checking {}... ".format(shop["domain"]))

        headers = {'User-Agent': config.USER_AGENT}
        url = "https://{}/products.json?limit=250".format(shop["domain"])
        if "http" in self.proxies:
           logging.info("PROXY: {}".format(self.proxies["http"]))
        response = requests.get(url, headers=headers, proxies=self.proxies)

        try:
            shop_products = response.json()["products"]
        except:
            logging.info(response.text)
            raise

        products = []
        for product in shop_products:
            if shop["group_variants"] and len(product["variants"]) > 1:
                products = products + self.gen_new_embeds_grouped(shop, product)
            else:
                products = products + self.gen_new_embeds(shop, product)


            if len(products) >= config.MAX_NEW_PRODUCTS:
                break
        
        logging.info("New Products: {}".format(len(products)))
        return products