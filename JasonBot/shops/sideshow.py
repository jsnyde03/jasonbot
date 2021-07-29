import time
import os

from bs4 import BeautifulSoup
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge


def find_products(response):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless')
    edge_options.add_argument('gpu-disabled')
    browser = Edge(executable_path='\home\jasonbot\JasonBot\shops\edgedriver_win64\msedgedriver.exe', options=edge_options)
    url = "https://www.sideshow.com/search?keywords=hot+toys#/sort:ss_days_since_release:asc/filter:ss_availability:Pre-Release/filter:ss_availability:Available$2520Now"
    browser.get(url)
    time.sleep(5)
    response = browser.page_source
    soup = BeautifulSoup(response, 'html.parser')
    products = []
    productsNode = soup.select("div.c-ProductList.row.ss-targeted")
    for productNode in productsNode:
        for i in range(len(productNode.find_all("h2", "c-ProductListItem__title"))):
            
            products.insert(0, {
                "title": productNode.find_all("h2", "c-ProductListItem__title")[i].string.strip(),
                "price": productNode.find_all("span", "c-ProductListItem__price-full")[i].string.strip(),
                "image": "https:" +productNode.find_all("img", "c-ProductListItem__image")[i]["src"],
                "url": "https://www.sideshow.com" +productNode.find_all("a", "c-ProductListItem__image-link")[i]["href"]
            }) 
    return products
            
       # i = 0
       # if i < range(len(productNode)):
            #products.insert(0, {
             #   "title":  productNode.find_all("h2", "c-ProductListItem__title")[i].string,
             #   "price": "".join(productNode.select("span.c-ProductListItem__price-full")[i].string.split()),                
              #  "image": "https:" +productNode.select("img.c-ProductListItem__image--portrait.image--loaded")[i]["src"],
              #  "url": "https://www.sideshow.com" +productNode.select("a.c-ProductListItem__image-link")[i]["href"]
            #})
    #print(products)
    #return products

   
   
