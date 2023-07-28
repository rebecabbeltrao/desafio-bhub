
from flask import Flask, request, jsonify

from api.service.customer import create_customer, delete_customer_by_id, edit_customer_by_id, get_customer_by_id, get_customers
from api.errors.errors import invalidIdMessage
from api.utils.utils import IsNotValid

app = Flask(__name__)

@app.route('/customer', methods=['GET'])
def controller_get_customers():
    customers = get_customers()
    resp = {"result": 200,
            "data": customers}
    return jsonify(resp)

@app.route('/customer/<id>', methods=['GET'])
def controller_get_customer_by_id(id):
    if IsNotValid(id):
        resp = {"result": 400,
                "data": {"message": invalidIdMessage()}}
    else:
        customer = get_customer_by_id(id)
        resp = {"result": 200,
                "data": customer}
    return jsonify(resp)

@app.route('/customer', methods=['POST'])
def controller_create_customer():
    new_customer = request.get_json()
    customer = create_customer(new_customer)
    resp = {"result": 200,
            "data":  {"message": ''}}
    return jsonify(resp)

@app.route('/customer/<id>', methods=['DELETE'])
def controller_delete_customer_by_id(id):
    if IsNotValid(id):
        resp = {"result": 400,
                "data": {"message": invalidIdMessage()}}
    else:
        customer = delete_customer_by_id(id)
        resp = {"result": 200,
                "data": {"message": ''}}
    return jsonify(resp)

@app.route('/customer/<id>', methods=['PUT'])
def controller_edit_customer_by_id(id):
    edited_customer = request.get_json()
    if IsNotValid(id):
        resp = {"result": 400,
                "data": {"message": invalidIdMessage()}}
    else:
        customer = edit_customer_by_id(id, edited_customer)
        resp = {"result": 200,
                "data": customer}
    return resp

app.run(port=5000, host='localhost', debug=True)
