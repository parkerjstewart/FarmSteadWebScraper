import requests
from bs4 import BeautifulSoup
from Product import Product


# scrapes the Double Star Farms website and returns a list of
# bs4.element.Tag, which contain html info about each listed product
def get_product_tags():
    url = "https://fs27.formsite.com/doublestarfarms/fd8esnpkyu/index.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # results contains an array of bs4.element.Tag
    results = soup.find_all("label", class_="question right_question")
    return results


# takes a bs4.element.Tag and returns the title of the product
def get_product_title(product):
    title = str(product.contents[0])
    # whoever designed the website decided to formal titles in two
    # different ways, so this if statement covers an odd scenario
    # idk why they couldn't just classify it as the title in html
    if "span style" in title:
        title = title[1:]
        title = title[title.find('>') + 1: title.find('<')]
    return title.strip()


# takes a bs4.element.Tag and returns whether it's true or not
# returns true if item is in stock. false if out of stock
def get_in_stock(product_tag):
    if "out of stock" in str(product_tag).lower() or "sold out" in str(product_tag).lower():
        return False
    return True


def create_product_list():
    return_list = []
    for item in get_product_tags():
        return_list.append(Product(get_product_title(item), get_in_stock(item)))
    return return_list



