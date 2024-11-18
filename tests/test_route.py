import unittest
import sys
import os
# Adding the parent directory to sys.path for app import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import app  # Importing the Flask app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  #  testing client to simulate requests
        self.app.testing = True

    def test_invalid_method(self):
        # Trying a POST request for a route that expects GET should return 405
        response = self.app.post('/')  # Route that expects GET
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

if __name__ == '__main__':
    unittest.main()
