# endpointy
from products import Product

def receive_data():
    file_path = r"C:\Users\Kamila\PycharmProjects\Stocktaking\Stocktaking\list_of_products.csv"
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

def return_to_json(product_list):
    pass
# funkcja formatujaca liste produktow w jsona

# if __name__ == "__main__":
#      s = receive_data()
#      for thing in s:
#          print(thing.name)