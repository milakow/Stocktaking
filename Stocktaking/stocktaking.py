from flask import Flask, jsonify, request
from products import Product, StockProducts, StockEncoder, ProductEncoder
import helpers

# global obj_list
obj_list = []

app = Flask(__name__)

def validate_json(product_list):
    schema = {

    }


#  pr_index,name,amount,price

@app.route('/data_loading', methods=['POST'])
def load_data():
    response_data = {
        "success": True,
        "data": []
    }
    filepath = request.json
    path_of_file = filepath["filepath"]
    global obj_list
    try:
        pr_index, name, amount, price = helpers.get_data(path_of_file)
        product_list = helpers.create_object(pr_index, name, amount, price)
        # global obj_list
        obj_list = StockProducts(product_list)
        if product_list is not None:
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
    return jsonify(response_data)


# returns information about specific resource (product)
@app.route('/products/<int:index>')
def get_product(index: int):
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
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
    list_of_products = []
    for element in obj_list.prod_list:
        list_of_products.append(element.change_to_dict())
    try:
        new_prod_dict = {"pr_index": new_data["pr_index"],
                         "name": new_data["name"],
                         "amount": new_data["amount"],
                         "price": new_data["price"]}

        list_of_products.append(new_prod_dict)
        resp_list = StockProducts(list_of_products)
        response_data["data"] = resp_list.prod_list
        response = jsonify(response_data)
    except KeyError as error:
        response_data["data"] = f'The entered data {error} is incorrect.'
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


# allows to change product data
@app.route('/products/<int:index>', methods=['PUT'])
def update_product(index: int):
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }
    updated_data = request.json
    updated_prod_dict = {"pr_index": updated_data["pr_index"],
                         "name": updated_data["name"],
                         "amount": updated_data["amount"],
                         "price": updated_data["price"]}
    list_of_products = []
    for elements in obj_list.prod_list:
        list_of_products.append(elements.change_to_dict())
    for product in list_of_products:
        if str(index) == product["pr_index"]:
            list_of_products.pop(index-1)
            list_of_products.insert(index-1, updated_prod_dict)
    response_data["data"] = list_of_products

    return jsonify(response_data)


# allows to delete product from the storage
@app.route('/products/<int:index>', methods=['DELETE'])
def delete_product(index: int):
    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }

    list_of_products = []
    for element in obj_list.prod_list:
        list_of_products.append(element.change_to_dict())
    for product in list_of_products:
        if str(index) == product["pr_index"]:
            list_of_products.remove(list_of_products[index - 1])
    response_data["data"] = list_of_products

    return jsonify(response_data)


# returns value of the product
@app.route('/products/get_value/<int:index>', methods=['GET'])
def get_value(index: int):  # try to change code to use func in Product class

    global obj_list
    response_data = {
        'success': True,
        'data': obj_list.get_products_as_dicts()
    }
    list_of_products = []
    value = 1
    for element in obj_list.prod_list:
        list_of_products.append(element.change_to_dict())
    for prod in list_of_products:
        if str(index) == prod["pr_index"]:
            value = (int(prod["price"]) * (int(prod["amount"])))

    response_data["data"] = f"Value of product no {index} is {value} EUR."

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
