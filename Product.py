class Product:
    def __init__(self, title, in_stock):
        self.title = title
        self.in_stock = in_stock


    def __eq__(self, other):
        title_match = False
        stock_match = False

        if isinstance(other, Product):
            if self.title == other.title:
                title_match = True
            if self.in_stock == other.in_stock:
                stock_match = True

            return title_match, stock_match
