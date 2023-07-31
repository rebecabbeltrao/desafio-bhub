import unittest
# from app_run import app
# from api.app import app

# from api import app
from api.database.models import db
from dotenv import load_dotenv


load_dotenv(".env.test", override=True)

class CustomerTest(unittest.TestCase):
    def setUp(self):
        # self.db = db.get_db()
        # self.app = app.test_client()
        print("1")
        
    
    # def test_successful_update_customer(self):

    