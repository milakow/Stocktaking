import pytest
import json
import requests
from Stocktaking.object_classes import Product, StockProducts
from Stocktaking.stocktaking import app
from flask import request, jsonify

app.testing = True


def test_get_all_products(create_stock):
    response = app.test_client().get('/products_all')
    # print(response.data)
    res = json.loads(response.data.decode('utf-8'))
    assert res["success"] == True
    assert res["data"] == [{'amount': 2, 'name': 'water', 'pr_index': 1, 'price': 3},
                           {'amount': 5, 'name': 'juice', 'pr_index': 2, 'price': 6}]


def test_get_specific_product(create_stock):
    response = app.test_client().get('/products/1')
    res = json.loads(response.data.decode('utf-8'))
    assert res["success"] == True
    assert res["data"] == {'amount': 2, 'name': 'water', 'pr_index': 1, 'price': 3}


def test_get_non_existing_product(create_stock):
    response = app.test_client().get('/products/4')
    res = json.loads(response.data.decode('utf-8'))
    assert res["success"] == False
    assert res["message"] == f'Index 4 out of range.'


def test_add_product(new_product_dict):
    response = app.test_client().post("/product_new", json=new_product_dict)
    resp_str = response.get_data().decode("utf-8")
    res = json.loads(resp_str)
    assert res["data"] == {"amount": 6, "name": "tea", "pr_index": 3, "price": 5}

# def test_add_existing_product(new_product_dict):
#     response = app.test_client().post("/product_new", json={"amount": 6, "name": "tea", "pr_index": 1, "price": 5})
#     resp_str = response.get_data().decode("utf-8")
#     res = json.loads(resp_str)
#     assert res["message"] == f"Product with index 1 already exists."
#     assert res["success"] == False

def test_update_product(create_stock):
    updated_product_data = {"pr_index": 1, "name": "water", "amount": 10, "price": 3}
    response = app.test_client().put("/products/1", json=updated_product_data)
    resp_str = response.get_data().decode("utf-8")
    res = json.loads(resp_str)
    assert res["data"] == [{"pr_index": 1, "name": "water", "amount": 10, "price": 3}, {"pr_index": 2, "name": "juice", "amount": 5, "price": 6}]

def test_delete_product(create_stock):
    response = app.test_client().delete('/products/2')
    res = json.loads(response.data.decode('utf-8'))
    assert res["success"] == True
    assert res["message"] == f'Product 2 successfully deleted.'

def test_get_value_of_product(create_stock):
    response = app.test_client().get('/products/get_value/1')
    res = json.loads(response.data.decode('utf-8'))
    assert res["success"] == True
    assert res["message"] == f'The value of product no 1 equals 6 EUR.'

