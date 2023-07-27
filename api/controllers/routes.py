
from flask import Flask, request, jsonify

from api.api_customer import APIException, IsNotValid, create_customer, delete_customer_by_id, edit_customer_by_id, get_customer_by_id, get_customers
from api.errors.errors import InvalidID, invalidIdMessage, successMessage, userExistsMessage
from api.utils.utils import user_already_exists

app2 = Flask(__name__)

@app2.route('/customer/<id>', methods=['DELETE'])
def controller_delete_customer_by_id(id):
    if IsNotValid(id):
        resp = {"result": 400,
                "data": {"message": invalidIdMessage()}}
    else:
        delete_customer_by_id(id)
        resp = {"result": 200,
                "data": {"message": successMessage()}}
    return jsonify(**resp)


@app2.route('/customer/<id>', methods=['PUT'])
def controller_edit_customer_by_id(id):
    if IsNotValid(id):
        resp = {"result": 400,
                "data": {"message": invalidIdMessage()}}
    else:
        edit_customer_by_id(id)
        resp = {"result": 200,
                "data": {"message": successMessage()}}
    return jsonify(**resp)
    

@app2.route('/customer', methods=['POST'])
def controller_create_customer():
    new_customer = request.get_json()
    # TODO: check if user exists
    if user_already_exists():
        resp = {"result": 400,
                "data": {"message": userExistsMessage()}}
    else: 
        create_customer(new_customer)
        resp = {"result": 200,
                "data": {"message": successMessage()}}
    return jsonify(**resp)
   
@app2.route('/customer/<id>', methods=['GET'])
def controller_get_customer_by_id(id):
    if IsNotValid(id):
        resp = {"result": 400,
                "data": {"message": invalidIdMessage()}}
    else:
        get_customer_by_id(id)
        resp = {"result": 200,
                "data": {"message": successMessage()}}
    return jsonify(**resp)


@app2.route('/customer', methods=['GET'])
def controller_get_customers():
    get_customers()
    resp = {"result": 200,
            "data": {"message": successMessage()}}
    return jsonify(**resp)

