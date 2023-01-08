from flask import Flask, jsonify, request

# from products import StockProducts
from products import Product, StockProducts, StockEncoder, ProductEncoder
import helpers
import json

data_list = []
obj_list = []

app = Flask(__name__)

def validate_json(product_list):
    schema = {

    }


#  pr_index,name,amount,price

@app.route('/data_loading', methods=['POST'])
def load_data():  # niech pokazuje tylko status 201 (ok)
    response_data = {
        "success": True,
        "data": []
    }
    filepath = request.json
    path_of_file = filepath["filepath"]
    try:
        pr_index, name, amount, price = helpers.get_data(path_of_file)
        prod_lis = helpers.create_object(pr_index, name, amount, price)
        global obj_list
        obj_list = StockProducts(prod_lis)
        if prod_lis is not None:
            if response_data["success"]:
                response_data["data"] = obj_list.get_products_as_dicts()
            response = jsonify(response_data)
            response.status_code = 200
            return response
    except ValueError:
        response_data["success"] = False
        response_data["data"] = f"Data could not been loaded."
        response = jsonify(response_data)
        response.status_code = 404
        return response


# returns information about all products in app storage
@app.route('/products_all')
def get_products():
    global obj_list
    response_data = {
        "success": True,
        "data": obj_list.get_products_as_dicts()
    }
    # global obj_list
    # response_data["data"] = obj_list.get_products_as_dicts()
    response = jsonify(response_data)
    return response


# returns information about specific resource (product)
@app.route('/products/<int:index>')
def get_product(index: int):
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }

    lista = []
    resp = {}
    pr_id = []
    for elements in obj_list.prod_list:
        lista.append(elements.__dict__)
    for prod in lista:
        if str(index) == prod["pr_index"]:
            # return lista[index - 1]
            resp = lista[index - 1]
        pr_id.append(prod["pr_index"])
    if str(index) not in pr_id:
        resp = f"Product with id {index} not found in product list."
    response_data["data"] = resp
    return jsonify(response_data)

# allows to add new product to the storage
@app.route('/product_new', methods=['POST'])
def add_product():
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }
    new_data = request.json
    lista = []
    for elements in obj_list.prod_list:
        lista.append(elements.change_to_dict())

    new_prod_dict = {}
    try:
        new_prod_dict["pr_index"] = new_data["pr_index"]
        new_prod_dict["name"] = new_data["name"]
        new_prod_dict["amount"] = new_data["amount"]
        new_prod_dict["price"] = new_data["price"]

        lista.append(new_prod_dict)
        resp_list = StockProducts(lista)
        response_data["data"] = resp_list.prod_list
        response = jsonify(response_data)
    except KeyError as error:
        response_data["data"] = f'The entered data {error} is inccorect'
        response_data["success"] = False
        response = jsonify(response_data)
        response.status_code = 400
    return response


@app.errorhandler(404)
def not_found(error):
    response_data = {
        'success': False,
        'data': [],
        'error': 'Not found'
    }
    response = jsonify(response_data)
    response.status_code = 404
    return response

# TO BE CONTINUED
@app.route('/products/<int:index>', methods=['PUT'])  # DO DOKOŃCZENIA
def update_product(index: int):
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }
    updated_data = request.json




# allows to delete product from the storage
@app.route('/products/<int:index>', methods=['DELETE'])
def delete_product(index: int):
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }

    lista = []
    for elements in obj_list.prod_list:
        lista.append(elements.__dict__)
    for prod in lista:
        if str(index) == prod["pr_index"]:
            lista.remove(lista[index - 1])
    response_data["data"] = lista
    return jsonify(response_data)


# returns value of the product
@app.route('/products/get_value/<int:index>', methods=['GET'])
def get_value(index: int):                                      # try to change code to use func in Product class
    pass
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }
    lista = []
    value = 1
    for elements in obj_list.prod_list:
        lista.append(elements.__dict__)
    for prod in lista:
        if str(index) == prod["pr_index"]:
            value = (int(prod["price"]) * (int(prod["amount"])))

    response_data["data"] = f"Value of product no {index} is {value} EUR."
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
