import csv
import json
from products import StockEncoder, Product, StockProducts
import json

product_list = []
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
    for x in range(len(pr_index)):
        product_x = Product(pr_index[x], name[x], amount[x], price[x])
        product_list.append(product_x)
        # stock = StockProducts(product_list)
    return product_list  # zwraca mi liste obiektow

def create_obj_list(product_list):
    obj_list = StockProducts(product_list)

    lista = []
    for product in obj_list.prod_list:
        lista.append(product.name)

def load_data(path_of_file):  # niech pokazuje tylko status 201 (ok)
    response_data = {
        # 'success': True,
        'data': []  # prpduct list z create object ma zwrocic
    }
    # filepath = request.json
    # path_of_file = filepath["filepath"]
    try:       # wykorzystac "try"-  jak sie uda stworzyc obiekt to niech zwroic status- 201, jak nie np 400
        pr_index, name, amount, price = get_data(path_of_file)
        prod_lis = create_object(pr_index, name, amount, price)
        # prod_obj = json.dumps(prod_list, cls=ProductEncoder, indent=4)
        obj_list = StockProducts(prod_lis)
        print(obj_list)
        js_obj_list = json.dumps(obj_list, cls=StockEncoder, indent=4)
        if prod_lis is not None:
            response_data['data'] = js_obj_list
            # response = jsonify(response_data)
            # response.status_code = 200
        # else:
        #     response_data['success'] = False
        #     response.status_code = 400
    except ValueError:  # ale to nie jest value error w moim programie przeciez
        # response = jsonify(response_data)
        response_data['success'] = False
        # response.status_code = 404
    return response_data


def main():
    data_list = []
    file_path = r"C:\Users\Kamila\PycharmProjects\Stocktaking\Stocktaking\list_of_products.csv"
    pr_index, name, amount, price = get_data(file_path)
    prod_list = create_object(pr_index, name, amount, price)
    print(StockProducts(prod_list).prod_list)

    # print(type(prod1))
    # list_prod_list = StockProducts(prod_list)
    # print(create_obj_list(prod_list))

# def delete_product():
#     with open("saved_data", 'w+') as f:
#         content = f.read()
#     #
#     # response_data = {
#     #     'success': True,
#     #     'data': content
#     # }
#     print(type(content))
#     for prod_list in content:
#         for prod_data in prod_list:
#             if prod_data[0] == index:
#                 content.replace(prod_data, "")
#             # return type(content)


if __name__ == '__main__':
    main()
