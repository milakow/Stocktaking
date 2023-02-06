import pytest
import json
from Stocktaking.object_classes import Product, StockProducts
from Stocktaking.stocktaking import app
from flask import request
app.testing = True


def test_get_all_products(create_stock):
    response = app.test_client().get('/products_all')
    # print(response.data)
    res = json.loads(response.data.decode('utf-8'))
    assert res["success"] == True
    assert res["data"] == [{'amount': 2, 'name': 'water', 'pr_index': 1, 'price': 3}, {'amount': 5, 'name': 'juice', 'pr_index': 2, 'price': 6}]

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

# def test_add_product(new_product_dict):
def test_add_product(client):
    # response = app.test_client().post('/product_new', data=new_product_dict)  #response is object type
    new_product_dict = {"amount": 6, "name": "tea", "pr_index": 3, "price": 5}
    # response = app.test_client().post('/product_new', data=json.dumps(new_product_dict))  #response is object type
    response = client.post("/product_new", data={
            "amount": 6,
            "name": "tea",
            "pr_index": 3,
            "price": 5
        })
    res = json.loads(response.data.decode('utf-8')) #res to klasa str
    # print(res)
    assert res["success"] == True
    assert res["data"] == {"amount": 6, "name": "tea", "pr_index": 3, "price": 5}

def test_update_product(create_stock):
    updated_product_data = {"pr_index": 3, "name": "fanta", "amount": 1555, "price": 10}
    response = app.test_client().put(f"/products/{3}", data=json.dumps(updated_product_data))
    print(response.data)
    res = json.loads(response.data.decode('utf-8'))
    assert res['data'] == updated_product_data


