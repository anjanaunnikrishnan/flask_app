from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv  # Loaded .env file

load_dotenv()

app = Flask(__name__)

# Connecting to MongoDB Atlas using MONGO_URI from .env or GitHub Secrets
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.shop_db
products_collection = db.products

# Route for Homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route for Products Page
@app.route('/products')
def products():
    products = products_collection.find()  # Fetching products from MongoDB
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
