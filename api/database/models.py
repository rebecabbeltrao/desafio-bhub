from flask_mongoengine import MongoEngine

db = MongoEngine()

class BankAccount(db.EmbeddedDocument):
    branch = db.StringField(required=True)
    account = db.StringField(required=True)
    bank = db.StringField(required=True)

class Customer(db.Document):
    company_name = db.StringField(required=True)
    phone = db.StringField(required=True)
    address = db.StringField(required=True)
    invoicing = db.FloatField(required=True)
    bank_data = db.EmbeddedDocumentListField(
        document_type=BankAccount,
        required=True
    )
    register_date = db.StringField(required=True)
    last_update = db.StringField(required=False )
