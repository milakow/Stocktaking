#rozpoznaje static fixture
import pytest
from Stocktaking.object_classes import Product, StockProducts
from Stocktaking.helpers import stock_object
from Stocktaking.stocktaking import app

@pytest.fixture()
def application():
    # applic = app
    # applic.config.update({
    #     "TESTING": True,
    # })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(application):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture()
def create_stock():
    product_1 = Product(1, "water", 2, 3)
    product_2 = Product(2, "juice", 5, 6)
    stock = stock_object
    stock.prod_list.append(product_1)
    stock.prod_list.append(product_2)
    return stock

@pytest.fixture()
def new_product_dict():
    return {"amount": 6, "name": "tea", "pr_index": 3, "price": 5}
