import json, csv
from products import Product,  StockProducts

data_list = []

# def receive_data():
# filename: str = input('Enter the name of the file with data: ')
# try:
#     with open(f'{filename}.csv', encoding='utf-8-sig') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             data_list.append(row)
# except FileNotFoundError:
#     print(f'File {filename} was not found.')

def receive_data(file_path):
    try:
        with open(file_path, encoding='utf-8-sig') as f:
            content = csv.DictReader(f)
            for row in content:
                data_list.append(row)
            return data_list
    except FileNotFoundError:
        return f'File {file_path} was not found.'

# def return_to_json(product_data):
#     json_str = json.dumps(Product(product_data), cls=ProductEncoder)
#     return json_str

def get_data(file_path):
    try:
        with open(file_path, encoding='utf-8-sig') as f:
            content = f.read().split('\n')
            pr_index = []
            name = []
            amount = []
            price = []
            for row in content:
                data = row.split(",")
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
    product_list = []
    for x in range(len(pr_index)):
        product_x = Product(pr_index[x], name[x], amount[x], price[x])
        product_list.append(product_x)
        # stock = StockProducts(product_list)
    return product_list

def save_data(filename):
    with open('saved_data', 'w') as f:
        f.write(filename)

