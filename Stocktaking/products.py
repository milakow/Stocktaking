import json
class Product:
    def __init__(self, pr_index, name, amount, price):
        self.pr_index = pr_index
        self.name = name
        self.amount = amount
        self.price = price

    def count_value(self):
        return self.price * self.amount

class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        return [obj.pr_index, obj.name, obj.amount, obj.price]
