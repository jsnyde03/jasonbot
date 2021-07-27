from bs4 import BeautifulSoup

def find_products(response):
    soup = BeauitfulSoup(response.text, "html.parser")
    print(soup)