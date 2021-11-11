import Differences
from HTMLScaper import create_product_list
from DatabaseConnector import *
from Differences import *




'''
matches = []
for item1 in database_product_list:
    for item2 in scraped_product_list:
        if item1.title == item2.title:
            matches.append((item1, item2))


matches[10][0].in_stock = False

new_out = []
new_in = []
for item in matches:
    if item[0].in_stock is True and item[1].in_stock is False:
        new_out.append(item[0].title)
    if item[0].in_stock is False and item[1].in_stock is True:
        new_in.append(item[0].title)

print(new_out)
print(new_in)
'''




database_product_list = create_product_list_from_db("ProductList")
scraped_product_list = create_product_list()

answer = Differences.new_in_stock(database_product_list, scraped_product_list)
print(answer)

