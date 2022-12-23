from flask import Flask, jsonify, request
# from products import Product
import helpers
import json

app = Flask(__name__)
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

@app.route('/', methods=['GET']) #dodac endpoint #dlaczego miałam tu 'post' patrz Kamila na zdj
def provide_file_path():
    response_data = {
        'success': True,
        'data': f'Mam wszystkie produkty'
    }
    s = helpers.receive_data()
    json_product = json.dumps(helpers.receive_data())
    products = helpers.receive_data()
    return s


@app.route('/products_all', methods=['GET'])
def get_products():
    response_data = {
        'success': True,
        'data': data_list
    }

    return jsonify(response_data)


@app.route('/product_new', methods=['POST'])
def add_product():
    response_data = {
        'success': True,
        'data': []
    }

    data = request.json
    if 'id' not in data or 'name' not in data or 'amount' not in data or 'price' not in data:
        response_data['success'] = False
        response_data['error'] = 'Please provide all required information!'
        response = jsonify(response_data)
        response.status_code = 400
    else:
        data_list.append(data)
        response_data['data'] = data_list
        response = jsonify(response_data)
        response.status_code = 201
    return response

# returns information about specific resource (product)

@app.route('/products/<int:index>')
def get_product(index: int):
    response_data = {
        'success': True,
        'data': data_list
    }
            # poprawic wywolanie indeksu, ktory nie istnieje!

    for dicts in data_list:
        number = int(dicts.get("id"))
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
    response_data = {
        'success': True,
        'data': data_list
    }
    # for dicts in data_list:
    #     if index == dicts["id"]:
    #         dicts.clear()
    #         # response_data["data"] = data_list
    # return jsonify(response_data)
    for dicts in data_list:
        number = int(dicts.get('id')) #
        print(number)
        if number == index:
            dicts.clear()
            print(data_list)
    # for obj in obj_list:
    #   if obj.get("id") is not None:
    #     return obj

    #obj_list.remove(obj)

# def main():
#     # filename = input('Enter the name of the file with data: ')
#     receive_data()


# csv file name to enter below
# list-of-products

if __name__ == '__main__':
    app.run(debug=True)
