import unittest
import sys
import os
# Adding the parent directory to sys.path for app import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import db  # Importing db from app.py

class MongoDBTestCase(unittest.TestCase):
    def setUp(self):
        self.db = db  #  MongoDB instance

    def test_mongodb_ping(self):
        # Pinging MongoDB to verify the connection
        result = self.db.command('ping')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
