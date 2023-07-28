import datetime
from flask import Flask, request, jsonify
from api.database.models import Customer

from api.utils.utils import user_exists
# import api.database.models as models

app = Flask(__name__)

dic = [{
        'id': '1',
        'razao_social': '123456',
        'telefone': '123456',
        'endereco': 'avenida das avenidas',
        'data_cadastro': '12/12/12',
        'faturamento': '1222,22',
        'dados_bancarios': {
                'agencia': '12',
                'conta': '1111',
                'banco': 'br'
        },
 
    },
    {
        "id" : "2",
        "razao_social" : "22222",
        "telefone" : "23323232",
        "endereco" : "avenida das avenidas 2",
        "data_cadastro" : "13/13/13",
        "faturamento" : "13333,22",
        "dados_bancarios" : {
            "agencia" : "123",
            "conta" : "11112",
            "banco" : "br2"
    }
    }
]

def get_customers():
    # return objects from db
    customers = Customer.objects()
    return customers

def get_customer_by_id(id):
    # return object from db if the matching id
    customers = Customer.objects().get(id=id)
    return customers
    #  use equals id funtion

def create_customer(new_customer):
    if user_exists(id):
        print('user exists')
    #     exception 
    else:
        setCreationDate(new_customer)
        setGeneration(new_customer)
        saved_customer = Customer(**new_customer).save() 
        # check if user_exists(id)
        # set data cadastro 
        # save data on db
    return saved_customer

def edit_customer_by_id(id, new_customer):
    if user_exists(id):
        setGeneration(new_customer)
        edited_customer = Customer.objects(id=id).update(new_customer)
    else:
        print('')
        # execption/error
    return edited_customer

def setCreationDate(object):
    now = datetime.now()
    object["data_cadastro"] = now.isoformat()

def setGeneration(object):
    generation += 1
    object["generation"] = generation

def delete_customer_by_id(id):
    if user_exists(id):
        deleted_custumer = Customer.objects(id=id).delete()
    else:
        print('')
    return ' ', 200
   
def user_exists(id):
  if len(get_customer_by_id(id)) > 0 :
      return True
  return False