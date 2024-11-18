import unittest
import sys
import os
# Adding the parent directory to sys.path for app import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import db  #  db from app.py

class MongoDBWriteTestCase(unittest.TestCase):
    def setUp(self):
        self.collection = db.products  # Access the products collection

    def test_insert_product(self):
        # Creating testing product to insert
        product = {'name': 'Test Product', 'tag': 'Heater', 'price': 99.99, 'image_path': 'test_product.jpg'}
        result = self.collection.insert_one(product)
        
        # Checking if the product was successfully inserted
        inserted_product = self.collection.find_one({'_id': result.inserted_id})
        self.assertEqual(inserted_product['name'], 'Test Product')
        self.assertEqual(inserted_product['price'], 99.99)

if __name__ == '__main__':
    unittest.main()
