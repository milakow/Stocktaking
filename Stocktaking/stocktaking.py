from flask import Flask, make_response, jsonify
from products import Products

app = Flask(__name__)

def receive_data(filename):
    try:
        with open(f'{filename}.csv', encoding='utf-8-sig') as fopen:
            content = fopen.read()
            return content
    except FileNotFoundError:
        print(f'File {filename} was not found.')

@app.route('/posts')
def prepare_data(content):
    response_data = {
        'success': True,
        'data': POSTS

    }
    return jsonify(response_data)
    # stocktaking_data = receive_data(filename).replace('\n', ';').split(';')
    # print(stocktaking_data)


@app.route('/')
def welcome():
    return 'Welcome to the Stocktaking application. What would you like to do next?'


@app.route('/all_products')
def get_all_product():
    return {'products': 'product data'}


@app.route('/id')
def get_specific_product():
    return {'id product': 'product data'}


if __name__ == '__main__':
    prepare_data('list-of-products')
    # app.run(debug=True)
