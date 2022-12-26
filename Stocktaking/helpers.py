import json, csv
from products import Product
from products import ProductEncoder

data_list = []
product_list = []


def receive_data(file_path):
    try:
        with open(file_path, encoding='utf-8-sig') as f:
            content = csv.DictReader(f)
            for row in content:
                # print(row)
                data_list.append(row)
            return data_list
    except FileNotFoundError:
        return f'File {file_path} was not found.'

   # # try:
    ##     with open(file_path, encoding='utf-8-sig') as f:
   # #         content = f.read().split('\n')
   # #         product_list = []
    ##         for row in content:
    ##             data = row.split(',')
    ##             product = Product(data[0], data[1], data[2], data[3])
    ##             product_list.append(product)
    ##         return product_list
    ## except FileNotFoundError:
    ##     return f'File path "{file_path}" was not found.'


def return_to_json(product_data):
    json_str = json.dumps(Product(product_data), cls=ProductEncoder)
    return json_str
# funkcja formatujaca liste produktow w jsona

def get_data(file_path):
    try:
        with open(file_path, encoding='utf-8-sig') as f:
            content = f.read().split('\n')
            pr_index = []
            name = []
            amount = []
            price = []
            for row in content:
                data = row.split(',')
                pr_index.append(data[0])
                name.append(data[1])
                amount.append(data[2])
                price.append(data[3])
                # product = Product(data[0], data[1], data[2], data[3])
                # product = Product()
                # product_list.append(Product(data[0], data[1], data[2], data[3]))

            return pr_index, name, amount, price
    except FileNotFoundError:
        return f'File path "{file_path}" was not found.'

def create_object(pr_index, name, amount, price):
    for x in range(len(pr_index)):
        productx = Product(pr_index[x], name[x], amount[x], price[x])
        product_list.append(productx)
    return product_list