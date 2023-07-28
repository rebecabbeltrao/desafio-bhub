from api.database import db

class BankAccount(db.EmbeddedDocument):
    ag = db.StringField(required=True)
    conta = db.StringField(required=True)
    banco = db.StringField(required=True)

class Customer(db.Document):
    id = db.StringField(required=True, unique=True) 
    razao_social = db.StringField(required=True)
    telefone = db.StringField(required=True)
    endereco = db.StringField(required=True)
    faturamento = db.IntField(required=True)
    dados_bancarios = db.EmbeddedDocumentListField(
        document_type=BankAccount,
        required=True
    )
    data_cadastro = db.StringField(required=True)
    generation = db.IntField()
