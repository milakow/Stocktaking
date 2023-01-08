import csv
import json
from products import StockEncoder, Product, StockProducts
import json

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

def load_data(path_of_file):  # niech pokazuje tylko status 201 (ok)
    response_data = {
        'success': True,
        'data': []  # prpduct list z create object ma zwrocic
    }
    # filepath = request.json
    # path_of_file = filepath["filepath"]
    try:  # wykorzystac "try"-  jak sie uda stworzyc obiekt to niech zwroic status- 201, jak nie np 400
        pr_index, name, amount, price = get_data(path_of_file)
        prod_lis = create_object(pr_index, name, amount, price)
        global obj_list
        obj_list = StockProducts(prod_lis)
        return obj_list
    #     if prod_lis is not None:
    #         if response_data["success"]:
    #             response_data["data"] = obj_list.get_products_as_dicts()
    #         return response_data
    except ValueError:  # ale to nie jest value error w moim programie przeciez
         response_data["success"] = False
    #     response_data["data"] = f"Data could not been loaded."

def main():
    file_path = r"C:\Users\Kamila\PycharmProjects\Stocktaking\Stocktaking\list_of_products.csv"
    pr_index, name, amount, price = get_data(file_path)
    prod_list = create_object(pr_index, name, amount, price)
    # print(StockProducts(prod_list).prod_list)
    obj_list = load_data(file_path)
    lista = []
    pr_id = []
    index = 2

    # GET SINGLE PRODUCT
    # for elements in obj_list.prod_list:
    #     lista.append(elements.__dict__)
    #
    # for prod in lista:
    #     # print(pr_id)
    #     if str(index) == prod["pr_index"]:
    #         item = lista[index - 1]
    #         print(item)
    #
    #     pr_id.append(prod["pr_index"])
    # if str(index) not in pr_id:
    #     print('uups')

    # DELETE PRODUCT
    # for elements in obj_list.prod_list:
    #     lista.append(elements.__dict__)
    #
    # for prod in lista:
    #     # print(pr_id)
    #     if str(index) == prod["pr_index"]:
    #         lista.remove(lista[index-1])
    # print(lista)

    # ADD NEW PRODUCT
    new_prod_id = "5"
    new_prod_name = "moccha"
    new_prod_amount = "2"
    new_prod_price = "10"
    key_list = ["pr_index", "name", "amount", "price"]
    slownik = {}
    slownik["pr_index"] = new_prod_id
    slownik["name"] = new_prod_name
    slownik["amount"] = new_prod_amount
    slownik["price"] = new_prod_price
    addLista = []
    for elements in obj_list.prod_list:
        addLista.append(elements.__dict__)
    new_prod_list = create_object(new_prod_id, new_prod_name, new_prod_amount, new_prod_price)
    addLista.append(slownik)
    # print(addLista)

    add_Obj_list = StockProducts(addLista)
    # addLista.append(add_Obj_list)
    print(add_Obj_list.prod_list)


    # GET VALUE
    # value = 1
    # for elements in obj_list.prod_list:
    #     value = int(elements.count_value())
    # print(value)






if __name__ == '__main__':
    main()
