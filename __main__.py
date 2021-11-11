from HTMLScaper import create_product_list
from DatabaseConnector import *
from Differences import *
from EmailNotification import send_email


def main():
    # pull all of last week's products from the database and create a list
    # of product objects
    database_product_list = create_product_list_from_db("ProductList")
    # web scrape website and create a list of this week's products
    scraped_product_list = create_product_list()

    db_title_list = []
    sc_title_list = []
    # create a list of the titles of the products in the database
    for product in database_product_list:
        db_title_list.append(product.title)
    # create a list of the titles of the products on the website
    for product in scraped_product_list:
        sc_title_list.append(product.title)

    # list of new prods: prods on the website that weren't there last week
    adds = new_additions(db_title_list, sc_title_list)
    # list of prods that were removed from the site
    subs = new_subtractions(db_title_list, sc_title_list)
    new_in = new_in_stock(database_product_list, scraped_product_list)
    new_out = new_out_stock(database_product_list, scraped_product_list)

    # Maybe do truncating
    # now, we no longer need to know last week's products, so we clear the
    # database of last week's info and rewrite the db with this week's info
    clear_database('ProductList')
    create_db('ProductList', scraped_product_list)

    # send the email with the updates
    send_email(['emails'], adds, subs, new_in, new_out)


if __name__ == "__main__":
    main()


