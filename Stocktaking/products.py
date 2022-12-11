class Product:
    def __init__(self, pr_index, name, amount, price):
        self.pr_index = pr_index
        self.name = name
        self.amount = amount
        self.price = price

    def count_value(self):
        return self.price * self.amount
