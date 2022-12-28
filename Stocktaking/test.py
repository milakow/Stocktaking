import csv
import json
from products import ProductEncoder, Product
import json

# **************************************
# data_list = []
# ##program pakuje mi dane w listę słowników i z niej formatuje dane do formatu json,aby moc je wyswietlic (dziala)
# def receive_data(file_path):
#     try:
#         with open(file_path, encoding='utf-8-sig') as f:
#             content = csv.DictReader(f)
#             for row in content:
#                 data_list.append(row)
#             return data_list
#     except FileNotFoundError:
#         return f'File {file_path} was not found.'
#
# def return_to_json():
#     file_path = r"C:\Users\Kamila\PycharmProjects\Stocktaking\Stocktaking\list_of_products.csv"
#     data_list = receive_data(file_path)
#     data_json = json.dumps(data_list, cls=ProductEncoder)
#     print(data_json)

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
    product_list = {}
    for x in range(len(pr_index)):
        productx = Product(pr_index[x], name[x], amount[x], price[x])
        product_list[x+1] = productx
    return product_list


def delete_product():
    with open("saved_data", 'w+') as f:
        content = f.read()
    #
    # response_data = {
    #     'success': True,
    #     'data': content
    # }
    print(type(content))
    for prod_list in content:
        for prod_data in prod_list:
            if prod_data[0] == index:
                content.replace(prod_data, "")
            # return type(content)


def main():
    data_list = []
    file_path = r"C:\Users\Kamila\PycharmProjects\Stocktaking\Stocktaking\list_of_products.csv"
    pr_index, name, amount, price = get_data(file_path)
    # print(create_object(pr_index, name, amount, price))
    # data_json = json.dumps(data_list, cls=ProductEncoder)
    delete_product()


if __name__ == '__main__':
    main()
