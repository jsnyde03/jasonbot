from bs4 import BeautifulSoup

def find_products(response):
    soup = BeautifulSoup(response.text, "html.parser")
    productsNode = soup.select("li.xfolkentry.product")
    products = []
    for productNode in productsNode:
        products.insert(0, {
            "title": productNode.find_all("h2", "woocommerce-loop-product__title")[0].string,
            "price": "".join(productNode.find_all("span", "woocommerce-Price-amount")[0].strings),
            "image": productNode.find_all("img", "attachment-woocommerce_thumbnail")[0]["src"],
            "url": productNode.find_all("a")[0]["href"]
        })
    return products
