from object_classes import Product,  StockProducts
# from stocktaking import obj_list
import os

stock_object = StockProducts()

def data_loader(file_path):
    try:
        with open(file_path, encoding='utf-8-sig') as f:
            content = f.read().split('\n')
            if os.path.getsize(file_path) > 0:
                for row in content:
                    product_data = row.split(",")
                    product = Product(int(product_data[0]), product_data[1], int(product_data[2]), int(product_data[3]))
                    # obj_list.append(product)
                    # if len(stock_object.prod_list) == 0:
                    #     stock_object.prod_list.append(product)
                    # elif len(stock_object.prod_list) > 0:
                    #     for item in stock_object.prod_list:
                    #         if item.__dict__["pr_index"] == product.pr_index:
                    #             return f"Product already exists."
                    #             break
                    #         else:
                    stock_object.prod_list.append(product)
            else:
                raise IOError(f"Your file is empty.")
    except FileNotFoundError:
        return f'File path "{file_path}" was not found.'


def save_data(filename):
    with open('saved_data', 'w') as f:
        f.write(filename)

