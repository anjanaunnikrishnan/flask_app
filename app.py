from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connecting to MongoDB Atlas
client = MongoClient("mongodb+srv://ANJANA:nHkkTo0QenZybfS6@ecommerce.xvlyp.mongodb.net/?retryWrites=true&w=majority&appName=Ecommerce")
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

