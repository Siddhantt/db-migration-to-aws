from flask import Flask, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to local MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["shop"]
    products_collection = db["products"]
except Exception as e:
    print("Error connecting to MongoDB:", e)
    exit(1)

@app.route("/")
def home():
    return redirect("/products")

@app.route("/products")
def products():
    try:
        items = list(products_collection.find({}, {"_id": 0}))
        return render_template("products.html", products=items)
    except Exception as e:
        return f"<h3>Error fetching products: {e}</h3>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

