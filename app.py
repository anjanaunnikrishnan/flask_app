from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Connecting to MongoDB Atlas
PASSWORD = os.getenv("PASSWORD")# Password protected using env file
client = MongoClient("mongodb+srv://ANJANA:"+PASSWORD+"@ecommerce.xvlyp.mongodb.net/?retryWrites=true&w=majority&appName=Ecommerce")
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

