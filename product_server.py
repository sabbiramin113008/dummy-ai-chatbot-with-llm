# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 29 Sep 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""

from flask import Flask, jsonify

app = Flask(__name__)

# Dummy product data
products = {
    '1': {"id": 1, "name": "Product A"},
    '2': {"id": 2, "name": "Product B"},
    '3': {"id": 3, "name": "Product C"}
}


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products/<int:id>', methods=['GET'])
def get_products_by_id(id):
    if str(id) in products:
        return jsonify(products[str(id)])
    return jsonify(None)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
