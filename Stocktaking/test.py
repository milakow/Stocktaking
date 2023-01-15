import csv
import json
from object_classes import Product, StockProducts
import helpers

product_list = []
obj_list = []

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
        product_x = Product(pr_index[x], name[x], amount[x], price[x])
        product_list.append(product_x)
        # stock = StockProducts(product_list)
    return product_list  # zwraca mi liste obiektow

def create_obj_list(product_list):

    lista = []
    for product in obj_list.prod_list:
        lista.append(product.name)

# def load_data(path_of_file):  # niech pokazuje tylko status 201 (ok)
#     response_data = {
#         'success': True,
#         'data': []  # prpduct list z create object ma zwrocic
#     }
#     # filepath = request.json
#     # path_of_file = filepath["filepath"]
#     try:  # wykorzystac "try"-  jak sie uda stworzyc obiekt to niech zwroic status- 201, jak nie np 400
#         pr_index, name, amount, price = get_data(path_of_file)
#         prod_lis = create_object(pr_index, name, amount, price)
#         global obj_list
#         obj_list = StockProducts(prod_lis)
#         return obj_list
#     #     if prod_lis is not None:
#     #         if response_data["success"]:
#     #             response_data["data"] = obj_list.get_products_as_dicts()
#     #         return response_data
#     except ValueError:  # ale to nie jest value error w moim programie przeciez
#          response_data["success"] = False
#     #     response_data["data"] = f"Data could not been loaded."

def main():
    file_path = r"C:\Users\Kamila\PycharmProjects\Stocktaking\Stocktaking\list_of_products.csv"
    pr_index, name, amount, price = get_data(file_path)
    # prod_list = create_object(pr_index, name, amount, price)

    #GET_PRODUCT
    response_data = {
            'success': True,
            'data': helpers.stock_object.get_products_as_dicts()
        }
    index = 1
    list_of_products = []
    response_dict = {}
    product_id_list = []
    print(helpers.data_loader(file_path))
    for element in helpers.stock_object.prod_list:
        pass
        # print(type(element))
    #     list_of_products.append(element.change_to_dict())
    # for product in list_of_products:
    #     if str(index) == product["pr_index"]:
    #         # return list_of_products[index - 1]
    #         response_dict = list_of_products[index - 1]
    #     product_id_list.append(product["pr_index"])
    # if str(index) not in product_id_list:
    #     response_dict = f"Product with id {index} not found in product list."
    # response_data["data"] = response_dict

"""
def get_product(index: int):
    response_data = {
        'success': True,
        'data': helpers.stock_object.get_products_as_dicts()
    }

    list_of_products = []
    response_dict = {}
    product_id_list = []
    for element in obj_list.prod_list:
        list_of_products.append(element.change_to_dict())
    for product in list_of_products:
        if str(index) == product["pr_index"]:
            # return list_of_products[index - 1]
            response_dict = list_of_products[index - 1]
        product_id_list.append(product["pr_index"])
    if str(index) not in product_id_list:
        response_dict = f"Product with id {index} not found in product list."
    response_data["data"] = response_dict
"""

if __name__ == '__main__':
    main()
