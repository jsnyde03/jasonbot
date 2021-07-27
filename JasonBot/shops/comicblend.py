from bs4 import BeautifulSoup


def find_products(response):
    soup = BeautifulSoup(response.text, "html.parser")
    productsNode = soup.select("ul li.product.type-product")
    products = []
    for productNode in productsNode:
        products.insert(0, {
            "title": productNode.select("h2.woocommerce-loop-product__title")[0].string.strip(),
            "price": "".join(productNode.select("span.amount")[0].strings),
            "image": productNode.select("img")[0]["src"],
            "url": productNode.select("a")[0]["href"]
        })
    print(products)
    return products
