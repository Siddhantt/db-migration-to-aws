from flask import Flask, render_template
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mongo-to-mysql.cdcwsug8qi9r.ap-south-1.rds.amazonaws.com")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "yourStrongPassword123")  # replace with your actual password
DB_NAME = os.getenv("DB_NAME", "shop")

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def index():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
        conn.close()
        return render_template("index.html", products=products)
    except Exception as e:
        return f"<h2>Database Error:</h2> {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8008)
