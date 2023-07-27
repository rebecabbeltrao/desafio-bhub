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

def get_customers():
    return jsonify(dic)