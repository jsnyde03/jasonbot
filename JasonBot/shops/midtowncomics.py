from bs4 import BeautifulSoup


def find_products(response):
    soup = BeautifulSoup(response.text, "html.parser")
    productsNode = soup.select("div.product-card.row.list-style")
    products = []
    for productNode in productsNode:
        products.insert(0, {
            "title": productNode.select("h3")[0].string.strip(),
            "price": productNode.select("div.price2 p")[0].string.strip(),
            "image": productNode.select("img")[0]["src"],
            "url": productNode.select("div.product-title a")[0]["href"]
        })
    return products
