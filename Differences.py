# takes a list of titles of last week's products (off the database) and
# takes a list of titles of this week's products (off the website) and
# returns a list of titles that have been added to the site
# (products now on the site that weren't there last week)
def new_additions(db_titles, scraped_titles):
    return_list = []
    for title in scraped_titles:
        # if a product that is on the website is not in the database,
        # it must be new, so add it to the return list
        if title not in db_titles:
            return_list.append(title)

    return return_list


# takes a list of titles of last week's products (off the database) and
# takes a list of titles of this week's products (off the website) and
# returns a list of titles that have been taken off the site
# (products that were on the site last week that are no longer there
def new_subtractions(db_titles, scraped_titles):
    return_list = []
    for title in db_titles:
        # if a product that is in the database is not on the website,
        # it must have been removed, so add it to the return list
        if title not in scraped_titles:
            return_list.append(title)

    return return_list


def new_out_stock(db_products, scraped_products):
    out_of_stock = []
    for product in scraped_products:
        if product.in_stock is False:
            out_of_stock.append(product.title)

    for product in db_products:
        if product.title in out_of_stock and product.in_stock is False:
            out_of_stock.remove(product.title)

    db_names = []
    for product in db_products:
        db_names.append(product.title)

    for name in out_of_stock:
        if name not in db_names:
            out_of_stock.remove(name)

    return out_of_stock


def new_in_stock(db_products, scraped_products):
    in_stock = []
    for product in scraped_products:
        if product.in_stock is True:
            in_stock.append(product.title)

    for product in db_products:
        if product.title in in_stock and product.in_stock is True:
            in_stock.remove(product.title)

    db_names = []
    for product in db_products:
        db_names.append(product.title)

    for name in in_stock:
        if name not in db_names:
            in_stock.remove(name)

    return in_stock
