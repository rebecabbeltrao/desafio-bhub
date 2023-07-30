
from datetime import datetime
from flask import Blueprint, jsonify, request
from api.database.models import Customer
from api.errors.errors import handleExceptions

app_bp = Blueprint('customers', __name__)

@app_bp.route('/customer', methods=['GET'])
def getCustomers():
    try:
        customers = Customer.objects()
    except Exception as e:
        return handleExceptions(e)
    return jsonify(customers), 200


@app_bp.route('/customer/<id>', methods=['GET'])
def getCustomerById(id):
    try:
        print(id)
        customer = Customer.objects().get(id=id)
    except Exception as e:
        return handleExceptions(e)
    return jsonify(customer), 200

@app_bp.route('/customer', methods=['POST'])
def saveCustomer():
    try:
        getCustomerById(id)
    except Exception as e:
        return handleExceptions(e)
    
    new_customer = request.get_json()
    setCreationDate(new_customer)
    setLastUpdate(new_customer)
    saved_customer = Customer(**new_customer).save() 
    return jsonify(saved_customer), 200

@app_bp.route('/customer/<id>', methods=['PUT'])
def editCustomerById(id):
    try:
        getCustomerById(id)
    except Exception as e:
        return handleExceptions(e)
    
    new_customer = request.get_json()
    setLastUpdate(new_customer)
    edited_customer = Customer.objects(id=id).update(**new_customer)
    return jsonify(edited_customer), 200

def setCreationDate(object):
    now = datetime.now()
    object["data_cadastro"] = now.isoformat()

def setLastUpdate(object):
    now = datetime.now()
    object['last_update'] = now.isoformat()

@app_bp.route('/customer/<id>', methods=['DELETE'])
def deleteCustomerById(id):
    try:
        getCustomerById(id)
    except Exception as e:
        return handleExceptions(e)
    Customer.objects(id=id).delete()
    return '', 200
