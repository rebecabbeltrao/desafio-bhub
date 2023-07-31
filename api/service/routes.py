
from datetime import datetime
from flask import Blueprint, jsonify, request
from api.database.models import Customer
from api.errors.exceptions import handleExceptions
from api.service.messages import healthCheckMessage
from http import HTTPStatus


app_bp = Blueprint('api', __name__, url_prefix='/api/v1')

@app_bp.route('/health', methods=['GET'])
def health_check_get():
    return jsonify({"message": healthCheckMessage()}), HTTPStatus.OK

customer_bp = Blueprint('customers', __name__, url_prefix='/api/v1')

@customer_bp.route('/customers', methods=['GET'])
def getCustomers():
    try:
        customers = Customer.objects()
    except Exception as e:
        return handleExceptions(e, HTTPStatus.BAD_REQUEST)
    return jsonify(customers), HTTPStatus.OK

@customer_bp.route('/customer/<id>', methods=['GET'])
def getCustomerById(id):
    try:
        print(id)
        customer = Customer.objects().get(id=id)
    except Exception as e:
        return handleExceptions(e, HTTPStatus.BAD_REQUEST)
    return jsonify(customer), HTTPStatus.OK

@customer_bp.route('/customer', methods=['POST'])
def saveCustomer():
    try:
        getCustomerById(id)
    except Exception as e:
        return handleExceptions(e, HTTPStatus.BAD_REQUEST)
    
    new_customer = request.get_json()
    setRegisterDate(new_customer)
    setLastUpdate(new_customer)
    saved_customer = Customer(**new_customer).save() 
    return jsonify(saved_customer), HTTPStatus.OK

@customer_bp.route('/customer/<id>', methods=['PUT'])
def editCustomerById(id):
    try:
        getCustomerById(id)
    except Exception as e:
        return handleExceptions(e, HTTPStatus.BAD_REQUEST)
    
    new_customer = request.get_json()
    setLastUpdate(new_customer)
    edited_customer = Customer.objects(id=id).update(**new_customer)
    return jsonify(edited_customer), HTTPStatus.OK

def setRegisterDate(object):
    now = datetime.now()
    object["register_date"] = now.isoformat()

def setLastUpdate(object):
    now = datetime.now()
    object['last_update'] = now.isoformat()

@customer_bp.route('/customer/<id>', methods=['DELETE'])
def deleteCustomerById(id):
    try:
        getCustomerById(id)
    except Exception as e:
        return handleExceptions(e)
    Customer.objects(id=id).delete()
    return '', HTTPStatus.OK

