import json
class Product:
    def __init__(self, pr_index: int, name: str, amount: int, price: int):
        self.pr_index = pr_index
        self.name = name
        self.amount = amount
        self.price = price

    def count_value(self):
        return self.price * self.amount

    # return self (Product object) as a dictionary of attributes
    def change_to_dict(self):
        prod_as_dict = {
            'pr_index': self.pr_index,
            'name': self.name,
            'amount': self.amount,
            'price': self.price
        }
        return prod_as_dict

class StockProducts:
    def __init__(self):
        self.prod_list = []

    # returns list of products where Product is a dictionary of its attributes
    def get_products_as_dicts(self) -> json:
        list_of_product_dicts = []
        for product in self.prod_list:
            # json_prod = json.dumps(product.__dict__, indent=4).replace("\n", "")
            json_prod = product.__dict__
            list_of_product_dicts.append(json_prod)
        return list_of_product_dicts

    def find_product_by_index(self, index: int):
        for product in self.prod_list:
            if index == product.pr_index:
                return product
#
# class StockEncoder(json.JSONEncoder):
#     def default(self, obj):
#         return [obj.prod_list]
