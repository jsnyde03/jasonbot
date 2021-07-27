import hashlib
import sqlite3
import asyncio
import logging
import importlib
import re
import requests
from bs4 import BeautifulSoup
from discord import Embed, Colour
import config, discord_task, restock_monitor

def contains(title, keywords, operator="and"):
    clean_title = re.sub(' +', ' ', title).strip()
    if operator == "and":
        for keyword in keywords:
            if re.search(keyword, clean_title, re.IGNORECASE) is None:
                return False
        return True
    elif operator == "or":
        for keyword in keywords:
            if re.search(keyword, clean_title, re.IGNORECASE) is not None:
                return True
        return False
    raise Exception("invalid operator")


class ShopsMonitor:
    def __init__(self, monitor_name):
        logging.basicConfig(format=config.LOG_FORMAT.format(monitor_name), filename=config.LOG_FILE, level=logging.INFO)
        self.name = monitor_name
        self.db = self.connect_db()
    
    def connect_db(self):
        try:
            db = sqlite3.connect(config.DATABASE_FILES[self.name])
            db.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_hash CHARACTER(10) PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            return db
        except sqlite3.Error as e:
            logging.exception(e)

    def product_exists(self, product_hash):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM products WHERE product_hash=?', (product_hash[0:10],))
        row = cur.fetchone()
        if row is None:
            return False
        return True
    
    def insert_product(self, product_hash):
        cur = self.db.cursor()
        cur.execute('INSERT OR IGNORE INTO products (product_hash) VALUES (?)', (product_hash[0:10],))
        self.db.commit()
    
    def get_all_new_products(self):
        products = []
        for shop in config.SHOPS[self.name]:
            try:
                products = products + self.get_shop_new_products(shop)
            except Exception as e:
                logging.exception(e)
        return products

    async def publish_new_products(self, products, discord_client):
        for product in products:
            logging.info("publish {} new product: {}...".format(product["shop_name"], product["embed"].title[0:20]))
            for channel_id in product["channels_id"]:
                channel = discord_client.get_channel(channel_id if not config.TEST_MODE else config.TEST_CHANNEL_ID)
                if not config.DONT_PUBLISH:
                    await channel.send(embed=product["embed"])
                    await asyncio.sleep(0.2)
        for product in products:
            for keyword_filter in config.KEYWORD_FILTERS:
                if contains(product["embed"].title, keyword_filter["keywords"], operator=keyword_filter["operator"]):
                    channel = discord_client.get_channel(keyword_filter["channel_id"] if not config.TEST_MODE else config.TEST_CHANNEL_ID)
                    if not config.DONT_PUBLISH:
                        await channel.send(embed=product["embed"])
                        await asyncio.sleep(0.2)
            self.insert_product(product["product_hash"])


    def check(self):
        new_products = self.get_all_new_products()
        #print(new_products)

        if len(new_products) > 0:
            daemon = discord_task.DiscordTask(messages=new_products, monitor=self)
            daemon.run(config.BOT_TOKEN)
        else:
            logging.info("No new products.")