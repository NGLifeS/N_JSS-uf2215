from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "sakila_es"
        )

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM actor LIMIT 10")
        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template("index.html", datos = datos)
    
    except mysql.connector.Error as e:
        return f"Error de base de datos: {e}"

if __name__ == "__main__":
    app.run(debug=True, port=8000)