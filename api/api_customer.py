
from flask import Flask, request, jsonify

from api.errors.errors import InvalidID, ContentNotFound
from api.utils.utils import Equals

app = Flask(__name__)

dic = [{
        'id': '1',
        'razao_social': '123456',
        'telefone': '123456',
        'endereco': 'avenida das avenidas',
        'data_cadastro': '12/12/12',
        'faturamento': '1222,22',
        'dados_bancarios': '2930-98232',
        'agencia': '12',
        'conta': '1111',
        'banco': 'br',
    },
    {
        'id': '2',
        'razao_social': '1234567',
        'telefone': '1234567',
        'endereco': 'avenida das avenidas 2',
        'data_cadastro': '12/12/12',
        'faturamento': '1222,22',
        'dados_bancarios': '2930-98232',
        'agencia': '12',
        'conta': '1111',
        'banco': 'br',
    },
    {
        'id': '3',
        'razao_social': '12345678',
        'telefone': '12345678',
        'endereco': 'avenida das avenidas 3',
        'data_cadastro': '12/12/12',
        'faturamento': '1222,22',
        'dados_bancarios': '2930-98232',
        'agencia': '12',
        'conta': '1111',
        'banco': 'br',
    },
]

@app.route('/customer', methods=['GET'])
def get_customers():
    return jsonify(dic)

@app.route('/customer/<id>', methods=['GET'])
def get_customer_by_id(id):
    if IsNotValid(id):
        raise InvalidID()
    try: 
        # TODO: add real get endpoint separated
        for i in dic:
            print(i)
            if Equals(i.get('id'), id):
                return jsonify(i)
    except:
        raise ContentNotFound()
    # TODO: change return to something that says No Content found!
    return jsonify(dic)
    
#idvalidation       
def IsNotValid(id):
   if len(id) == 0:
     return True
   return False
     
@app.route('/customer', methods=['POST'])
def create_customer():
    new_customer = request.get_json()
    dic.append(new_customer)
    return jsonify(dic)

@app.route('/customer/<id>', methods=['PUT'])
def edit_customer_by_id(id):
    edited_customer = request.get_json()
    for i, customer in enumerate(dic):
        # if equals(customer.get('id'), id):
        #     # separate update
        #     dic[i].update(edited_customer)
            return jsonify(dic[i])
      
@app.route('/customer/<id>', methods=['DELETE'])
def delete_customer_by_id(id):
    for i, customer in enumerate(dic):
        # if equals(customer.get('id'), id):
        #     #separate delete
        #     del dic[i]
            return jsonify(dic)

app.run(port=5000, host='localhost', debug=True)





