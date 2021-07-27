from bs4 import BeautifulSoup

def find_products(response):
    soup = BeautifulSoup(response.text, "html.parser")
    productsNode = soup.select("div.list-grid")
    products=[]
    for productNode in productsNode:
        products.insert(0, {
            "title": productNode.find_all("div", "grid-title")[0].string.strip(),
            "price": "${}".format(productNode.find_all("span", "sqs-money-native")[0].string.strip()),
            "image": productNode.find_all("img", "grid-item-image")[0]["data-src"], 
            "url": "https://thecomiccornerstore.com{}".format(productNode.find_all("a","grid-item-link")[0]["href"])
        })
    return products