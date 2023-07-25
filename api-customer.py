from flask import Flask, request, jsonify

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
    for i in dic:
        if i.get('id') == id:
            return jsonify(i)

@app.route('/customer', methods=['POST'])
def create_customer_by_id():
    new_customer = request.get_json()
    dic.append(new_customer)
    return jsonify(dic)

@app.route('/customer/<id>', methods=['PUT'])
def edit_customer_by_id(id):
    edited_customer = request.get_json()
    for i, customer in enumerate(dic):
        if customer.get('id') == id:
            dic[i].update(edited_customer)
            return jsonify(dic[i])
      
@app.route('/customer/<id>', methods=['DELETE'])
def delete_customer_by_id(id):
    for i, customer in enumerate(dic):
        if customer.get('id') == id:
            del dic[i]
            return jsonify(dic)


app.run(port=5000, host='localhost', debug=True)

# localhost/customer (GET)
# localhost/customer/id (GET)
# localhost/customer/id (POST)
# localhost/customer/id (DELETE)
# localhost/customer/id (PUT)
