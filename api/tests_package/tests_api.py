import unittest
from flask import Flask
from http import HTTPStatus
from ..app import app_bp
from api.errors.exceptions import healthCheckMessage 

class HealthCheckGetTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.app.register_blueprint(app_bp)

    def test_health_check_get(self):
        with self.app.test_client() as client:
            response = client.get('/health')

            self.assertEqual(response.status_code, HTTPStatus.OK)

            expected_message = {"message": healthCheckMessage()}
            self.assertEqual(response.json, expected_message)

if __name__ == '__main__':
    unittest.main()
