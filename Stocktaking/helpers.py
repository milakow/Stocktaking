from Stocktaking.object_classes import Product, StockProducts
import os

stock_object = StockProducts()

def data_loader(file_path):
    try:
        with open(file_path, encoding='utf-8-sig') as f:
            content = f.read().split('\n')
            if os.path.getsize(file_path) > 0 and len(stock_object.prod_list) == 0:
                for row in content:
                    product_data = row.split(",")
                    product = Product(int(product_data[0]), product_data[1], int(product_data[2]), int(product_data[3]))
                    stock_object.prod_list.append(product)
            else:
                raise IOError(f"Your file is empty or your data have already been loaded.")
    except FileNotFoundError:
        raise IOError(f'File path "{file_path}" was not found.')


def save_data(filename):
    with open('saved_data', 'w') as f:
        f.write(filename)

