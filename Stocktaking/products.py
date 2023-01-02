import json
class Product:
    def __init__(self, pr_index, name, amount, price):
        self.pr_index = pr_index
        self.name = name
        self.amount = amount
        self.price = price

    def count_value(self):
        return self.price * self.amount

    # return self (Product object) as a dictionary of attributes
    # def to_dict(self):
    #     # prod_as_dict = {
    #     #     'index': self.pr_index,
    #     #     'name': self.name,
    #     #     'amount': self.amount,
    #     #     'price': self.price
    #     # }
    #     return self.__dict__
class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return [obj.pr_index, obj.name, obj.amount, obj.price]

class StockProducts:
    def __init__(self, prod_list):
        self.prod_list = prod_list

    # returns list of products where Product is a dictionary of its attributes
    def get_products_as_dicts(self) -> json:
        list_of_product_dicts = []
        for product in self.prod_list:
            list_of_product_dicts.append(product.__dict__)  # __dict__ returns attributes as a dictionary
        return list_of_product_dicts

class StockEncoder(json.JSONEncoder):
    def default(self, obj):
        return [obj.prod_list]
