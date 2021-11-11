import mysql.connector
from Product import Product


# this func. takes an existing database's name and a list of product
# objects and puts the product's info in the database
# this is used after the database is cleared in order to put the web's
# current products in the database for next week
def create_db(db_name, product_list):
    db = mysql.connector.connect(host='serverhost',
                                 user='username',
                                 passwd='password',
                                 database=db_name)
    mycursor = db.cursor()
    mycursor.execute("CREATE TABLE Product (title VARCHAR(100), in_stock"
                     " TINYINT, "
                     "productID int PRIMARY KEY AUTO_INCREMENT)")
    for item in product_list:
        if item.in_stock:
            num = 1
        else:
            num = 0
        mycursor.execute("INSERT INTO Product (title, in_stock) VALUES (%s, %s)", (item.title, num))
        db.commit()


# this func. connects to the database and pulls the title and whether or
# not the product is in stock in order to create a list of product obj.,
# which it returns
def create_product_list_from_db(db_name):
    return_list = []
    db = mysql.connector.connect(host='serverhost',
                                 user='master',
                                 passwd='password',
                                 database=db_name)
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Product")
    for item in mycursor:
        if item[1] == 1:
            in_stock = True
        else:
            in_stock = False
        return_list.append(Product(item[0].strip(), in_stock))

    return return_list


# truncate table or delete from table instead of deleting the table
# probably truncate
# clears out the database
# should only be used after the list of products has been pulled and
# the script is ready to override last week's product list with
# this week's product list
def clear_database(db_name):
    db = mysql.connector.connect(host='serverhost',
                                 user='username',
                                 passwd='password',
                                 database=db_name)
    mycursor = db.cursor()
    mycursor.execute("DROP TABLE Product")












