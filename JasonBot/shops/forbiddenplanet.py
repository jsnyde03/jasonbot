from bs4 import BeautifulSoup

def find_products(response):
    soup = BeautifulSoup(response.text, "html.parser")
    productsNode = soup.find_all("li", "product-list__list__item")
    products = []
    for productNode in productsNode:
        data = [item.strip() for item in productNode.find_all("p", "h4")[0].strings]
        image = "https://forbiddenplanet.com/static/catalog/default_product_image.a09eebf731fb.svg"
        images = productNode.find_all("img","img--r")
        if len(images) > 0:
            image = images[0]["src"]
        products.insert(0, {
            "title": data[0],
            "price": data[3] + data[4],
            "image": image,
            "url": "https://forbiddenplanet.com" + productNode.find_all("a", "one-whole")[0]["href"]
        })
    return products
    
