import requests
import json
from bs4 import BeautifulSoup

def find_products(response):
    soup = BeautifulSoup(response.text, "html.parser")
    productsNode = soup.select("div.panel-body.p-a-sm")
    products = []
    for productNode in productsNode:
        products.insert(0, {
            "title": productNode.select("h5 a")[0].string.strip(),
            "price": productNode.select("h4 strong")[0].string.strip(),
            "image": productNode.find_all("img")[0]["src"],
            "url": "https://www.archonia.com" + productNode.select("h5 a")[0]["href"]
        })
    return products
