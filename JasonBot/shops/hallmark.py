from bs4 import BeautifulSoup

def find_products(response):
    soup = BeautifulSoup(response.text, "html.parser")
    productsNode = soup.select("ul.browse-container")
    products = []
    for productNode in productsNode:
        products.insert(0, {
            "title": productNode.find_all("h2", "title")[0].string,
            "price": "".join(productNode.find_all("span", "price-original")[0].strings),
            "image": productNode.find_all("img")[0]["data-lzy-src"],
            "url": "https://www.hallmark.com" + productNode.find_all("a")[0]["href"]
        })
    return products