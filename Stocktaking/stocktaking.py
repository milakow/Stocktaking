from flask import Flask, jsonify, request
from products import Product, StockProducts, StockEncoder
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
    # response_data = {
    #     # 'success': True,
    #     'data': []  # prpduct list z create object ma zwrocic
    # }
    filepath = request.json
    path_of_file = filepath["filepath"]
    try:       # wykorzystac "try"-  jak sie uda stworzyc obiekt to niech zwroic status- 201, jak nie np 400
        pr_index, name, amount, price = helpers.get_data(path_of_file)
        prod_lis = helpers.create_object(pr_index, name, amount, price)
        # prod_obj = json.dumps(prod_list, cls=ProductEncoder, indent=4)
        global obj_list
        obj_list = StockProducts(prod_lis)
        # js_obj_list = json.dumps(obj_list, cls=StockEncoder, indent=4)
        if prod_lis is not None:
           # response_data['data'] = js_obj_list
            response = jsonify({"success": True,
                                'data': obj_list.get_products_as_dicts()})
            response.status_code = 200
            return response
        # else:
        #     response_data['success'] = False
        #     response.status_code = 400
    except ValueError:  # ale to nie jest value error w moim programie przeciez
        # response = jsonify(response_data)
        # response_data['success'] = False
        response = response = jsonify({"success": False,
                                       "data": "Data could not been loaded."})
        response.status_code = 404
        return response


# returns information about all products in app storage
@app.route('/products_all')
def get_products(obj_list):
    response_data = {
        'success': True,
        'data': [] # prpduct list z create object ma zwrocic
    }
    # obj_list = StockProducts(prod_list)
    response = jsonify(response_data)
    response_data['data'] = obj_list
    return response


# DOKONCZYC
# allows to add new product to the storage
@app.route('/product_new', methods=['POST'])
def add_product():
    with open("saved_data", 'r') as f:
        content = f.read()

    response_data = {
        'success': True,
        'data': content
    }
    data = request.json
    new_prod_id = data["pr_index"]
    new_prod_name = data["name"]
    new_prod_amount = data["amount"]
    new_prod_price = data["price"]

    # if 'id' not in data or 'name' not in data or 'amount' not in data or 'price' not in data:
    if new_prod_id not in content or new_prod_name not in content or new_prod_amount not in content or new_prod_price not in content:  # chyba niepotrzebnie to zrobilam
        response_data['success'] = False
        response_data['error'] = 'Please provide all required information!'
        response = jsonify(response_data)
        response.status_code = 400
    else:
        prod_list = helpers.create_object(new_prod_id, new_prod_name, new_prod_amount, new_prod_price)
        prod_obj = json.dumps(prod_list, cls=ProductEncoder, indent=4)
        response_data['data'] = prod_obj

        # data_list.append(data)
        # response_data['data'] = data_list
        response = jsonify(response_data)
        response.status_code = 201

    return response


# returns information about specific resource (product)
@app.route('/products/<int:index>')
def get_product(index: int):
    with open("saved_data", 'r') as f:
        content = f.read()

    response_data = {
        'success': True,
        'data': content
    }
    #  poprawic wywolanie indeksu, ktory nie istnieje!

    for obj in content:
        number = content["pr_index"]
        if number == index:
            index = number - 1
            item = data_list[index]
            response_data['data'] = item
            return jsonify(response_data)

    # item = ''
    # for user_id in data_list:
    #     if user_id['id'] == user_id:
    #         item = user_id
    """"" 
    space
    """
    # item = [dicts for dicts in data_list if dicts["id"] == index][0]
    #
    # response_data['data'] = item
    # return jsonify(response_data)


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


@app.route('/products/<int:index>', methods=['PUT'])  # DO DOKOŃCZENIA
def update_product(index: int):
    return jsonify({
        'success': True,
        'data': f'Product {index} has been updated.'
    })


@app.route('/products/<int:index>', methods=['DELETE'])  # DO DOKOŃCZENIA
def delete_product(index: int):
    with open("saved_data", 'r+') as f:
        content = f.read()
        content2 = content.replace(" ", "")

    response_data = {
        'success': True,
        'data': content
    }

    for prod_list in content:
        for prod_data in prod_list:
            if prod_data[0] == index:
                pass
            return content2

    # obj_list.remove(obj)


@app.route('/products/<int:index>/get_value', methods=['GET'])
def get_value(index: int):
    pass


# def main():
#     # filename = input('Enter the name of the file with data: ')
#     receive_data()


# csv file name to enter below
# list-of-products

if __name__ == '__main__':
    app.run(debug=True)
