import hashlib
import sqlite3
import asyncio
import logging
import importlib
import requests
from bs4 import BeautifulSoup
from discord import Embed, Colour
import config, discord_task, shops_monitor

class RestockMonitor(shops_monitor.ShopsMonitor):
    
    def __init__(self):
        super().__init__("restock")

    def instock_hash(self, url):
        return hashlib.sha256(url.encode('utf-8')).hexdigest()[0:9] + "1"
    
    def outofstock_hash(self, url):
        return hashlib.sha256(url.encode('utf-8')).hexdigest()[0:9] + "0"

    def backorder_hash(self, url):
        return hashlib.sha256(url.encode('utf-8')).hexdigest()[0:9] + "2"

    def shop_product_status(self, shop, url):
        headers = {'User-Agent': config.USER_AGENT}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        in_stock_element = soup.select(shop["selector"])
        if len(in_stock_element) > 0:
            availability_text = soup.select(shop["selector"])[0].string.strip()
            if availability_text == shop["in_stock_string"]:
                return "instock"
            elif availability_text == shop["backorder_string"]:
                return "backorder"
        return "outofstock"

    def db_product_status(self, url):
        if self.product_exists(self.instock_hash(url)):
            return "instock"
        if self.product_exists(self.outofstock_hash(url)):
            return "outofstock"
        if self.product_exists(self.backorder_hash(url)):
            return "backorder"
        return "unknown"

    def delete_product(self, url):
        cur = self.db.cursor()
        values = (self.instock_hash(url), self.outofstock_hash(url), self.backorder_hash(url))
        cur.execute('DELETE FROM products WHERE product_hash in (?,?,?)', values)
        self.db.commit()
    
    def gen_new_embeds(self, shop, url, soup, instock, backorder):
        if instock:
            title="IN STOCK ALERT: "
        elif backorder:
            title="BACKORDER ALERT: "
        else:
            title="OUT OF STOCK ALERT: "
        title += soup.select("title")[0].string

        embed = Embed(title=title, url=url, color=Colour(0x246100))
        metaImage = soup.select('meta[property="og:image"]')
        if len(metaImage) > 0:
            embed.set_image(url=metaImage[0]["content"])
        if instock:
            product_hash = self.instock_hash(url)
        elif backorder:
            product_hash = self.backorder_hash(url)
        else:
            product_hash = self.outofstock_hash(url)
        return [{
            "embed": embed,
            "product_hash": product_hash,
            "channels_id": shop["channels_id"],
            "shop_name": shop["name"]
        }]

    def get_shop_new_products(self, shop):
        logging.info("Checking restock {}...".format(shop["name"]))
        products = []
        for url in shop["urls"]:
            headers = {'User-Agent': config.USER_AGENT}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            old_status = self.db_product_status(url)
            new_status = self.shop_product_status(shop, url)
            if old_status != new_status:
                products = products + self.gen_new_embeds(shop, url, soup, new_status == "instock", new_status == "backorder")
                if old_status != "unknown":
                    self.delete_product(url)
        
        logging.info("New products: {}".format(len(products)))
        return products

