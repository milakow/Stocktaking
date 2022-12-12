from flask import Flask, jsonify, request
# from products import Product
import csv

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
@app.route('/')
def welcome():
    filename = input('Enter the name of the file with data: ')
    try:
        with open(f'{filename}.csv', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)
    except FileNotFoundError:
        return f'File {filename} was not found.'
    return 'Welcome to the Stocktaking application. What would you like to do next?'


@app.route('/products', methods=['GET', 'POST'])  # czy powinnam zmienić nazwę endpointa i funkcji poniżej?
def products():
    response_data = {
        'success': True,
        'data': []
    }

    if request.method == 'GET':
        response_data['data'] = data_list
        return jsonify(response_data)
    elif request.method == 'POST':
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
def get_product(index):
    response_data = {
        'success': True,
        'data': []
    }
            #poprawic wywolanie indeksu, ktory nie istnieje!

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

# @app.route('/delete_content')
#
# @app.route('/change_content')

# @app.route('/save')

# ??


# def main():
#     # filename = input('Enter the name of the file with data: ')
#     receive_data()


# csv file name to enter below
# list-of-products

if __name__ == '__main__':
    app.run(debug=True)
