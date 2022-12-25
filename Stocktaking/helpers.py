import json
from products import Product
from products import ProductEncoder

def receive_data(file_path):
    try:
        with open(file_path, encoding='utf-8-sig') as f:
            content = f.read().split('\n')
            product_list = []
            for row in content:
                data = row.split(',')
                product = Product(data[0], data[1], data[2], data[3])
                product_list.append(product)
            return product_list
                # print(product.name)
                    # product_obj = Product(row)

    except FileNotFoundError:
        return f'File path "{file_path}" was not found.'

def return_to_json(product_data):
    json_str = json.dumps(Product(product_data), cls=ProductEncoder)
    return json_str
# funkcja formatujaca liste produktow w jsona

# if __name__ == "__main__":
#      s = receive_data()
#      for thing in s:
#          print(thing.name)