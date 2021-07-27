from bs4 import BeautifulSoup

def find_products(response):
   soup = BeautifulSoup(response.text, "html.parser")
   productsNode = soup.select("li.item.product.product-item.product-item-info")
   products = []
   for productNode in productsNode:
      products.insert(0, {
            "title": productNode.find_all("a", "product-item-link")[0].string.strip(),
            "price": productNode.find_all(attrs={"data-price-type": "finalPrice"})[0].string.strip(),
            "image": productNode.find_all("img", "product-image-photo")[0]["data-src"],
            "url": productNode.find_all("a", "product-item-link")[0]["href"]
        })
      return products
