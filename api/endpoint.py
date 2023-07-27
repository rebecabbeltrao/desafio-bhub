
# from flask import Flask, request, jsonify

# from api.errors.errors import InvalidID, ContentNotFound
# from api.utils.utils import Equals

# app = Flask(__name__)

# dic = [{
#         'id': '1',
#         'razao_social': '123456',
#         'telefone': '123456',
#         'endereco': 'avenida das avenidas',
#         'data_cadastro': '12/12/12',
#         'faturamento': '1222,22',
#         'dados_bancarios': '2930-98232',
#         'agencia': '12',
#         'conta': '1111',
#         'banco': 'br',
#     },
#     {
#         'id': '2',
#         'razao_social': '1234567',
#         'telefone': '1234567',
#         'endereco': 'avenida das avenidas 2',
#         'data_cadastro': '12/12/12',
#         'faturamento': '1222,22',
#         'dados_bancarios': '2930-98232',
#         'agencia': '12',
#         'conta': '1111',
#         'banco': 'br',
#     },
#     {
#         'id': '3',
#         'razao_social': '12345678',
#         'telefone': '12345678',
#         'endereco': 'avenida das avenidas 3',
#         'data_cadastro': '12/12/12',
#         'faturamento': '1222,22',
#         'dados_bancarios': '2930-98232',
#         'agencia': '12',
#         'conta': '1111',
#         'banco': 'br',
#     },
# ]

# def get_customers():
#     return jsonify(dic)

# def get_customer_by_id(id):
#     for i in dic:
#         print(i)
#         if Equals(i.get('id'), id):
#             return jsonify(i)
#         # add else if not found 
#     return jsonify(dic)

# def create_customer(new_customer):
#     dic.append(new_customer)
#     return jsonify(dic)

# def edit_customer_by_id(id):
#     edited_customer = request.get_json()
#     for i, customer in enumerate(dic):
#         if Equals(customer.get('id'), id):
#             # TODO: when update is finished separate it to another function
#             dic[i].update(edited_customer)
#             return jsonify(dic[i])
#         # add else if not found 
      
# def delete_customer_by_id(id):
#     for i, customer in enumerate(dic):
#         if Equals(customer.get('id'), id):
#             #TODO: separate delete
#             del dic[i]
#             return jsonify(dic)
#         # add else if not found 






