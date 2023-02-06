from flask import Flask, jsonify, request
from Stocktaking.object_classes import Product
from Stocktaking import helpers

app = Flask(__name__)


@app.route('/data_loading', methods=['POST'])
def load_data():
    response_data = {
        "success": True,
        "data": []
    }
    filepath = request.json
    path_of_file = filepath["filepath"]
    try:
        helpers.data_loader(path_of_file)
        response_data["data"] = helpers.stock_object.get_products_as_dicts()
        response = jsonify(response_data)
        response.status_code = 200
        return response
    except IOError as e:
        response_data["success"] = False
        response_data["message"] = e.message
        response = jsonify(response_data)
        response.status_code = 400
        return response


# returns information about all products in app storage
@app.route('/products_all', methods=['GET'])
def get_products():
    response_data = {
        "success": True,
        "data": helpers.stock_object.get_products_as_dicts()
    }
    return jsonify(response_data)


# returns information about specific resource (product)
@app.route('/products/<int:index>', methods=['GET'])
def get_product(index: int):
    response_data = {
        'success': True,
        'data': []
    }
    for element in helpers.stock_object.prod_list:
        if element.pr_index == index:
            response_data["data"] = element.__dict__
            break
    if not response_data["data"]:
        response_data["message"] = f"Index {index} out of range."
        response_data["success"] = False

    return jsonify(response_data)


# allows to add new product to the storage
@app.route('/product_new', methods=['POST'])
def add_product():
    response_data = {
        'success': True,
        'data': []
    }
    new_data = request.json
    try:
        new_product = Product(new_data["pr_index"], new_data["name"], new_data["amount"], new_data["price"])
        product = helpers.stock_object.find_product_by_index(new_product.pr_index)
        if product is None:
            helpers.stock_object.prod_list.append(new_product)
            response_data["data"] = new_product.change_to_dict()
            response = jsonify(response_data)
        else:
            response_data["message"] = f"Product with index {int(new_product.pr_index)} already exists."
            response_data["success"] = False
            return jsonify(response_data)

    except KeyError as error:
        response_data["message"] = f'The entered data {error} is incorrect.'
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
    response_data = {
        'success': True,
        'data': []
    }
    updated_data = request.json
    updated_product = Product(updated_data["pr_index"], updated_data["name"], updated_data["amount"], updated_data["price"])

    for product in helpers.stock_object.prod_list:
        if index == product.pr_index:
            helpers.stock_object.prod_list.pop(index-1)
            helpers.stock_object.prod_list.insert(index-1, updated_product)
    response_data["data"] = helpers.stock_object.get_products_as_dicts()
    return jsonify(response_data)


# allows to delete product from the storage
@app.route('/products/<int:index>', methods=['DELETE'])
def delete_product(index: int):
    response_data = {
        'success': True,
        'data': []
    }
    product = helpers.stock_object.find_product_by_index(index)
    helpers.stock_object.prod_list.remove(product)
    response_data["message"] = f'Product {index} successfully deleted.'
    return jsonify(response_data)


# returns the value of the product
@app.route('/products/get_value/<int:index>', methods=['GET'])
def get_value(index: int):
    response_data = {
        'success': True,
        'data': []
    }

    product = helpers.stock_object.find_product_by_index(index)
    value = product.count_value()
    response_data["message"] = f"The value of product no {index} equals {value} EUR."
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
