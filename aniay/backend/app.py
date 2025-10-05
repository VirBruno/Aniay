# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # para permitir peticiones desde Django frontend

juguetes = [
    {"id": 1, "name": "Brillitos", "price": 150.00},
    {"id": 2, "name": "Tren de bloques", "price": 180.50},
]

proveedores = [
    {"id": 1, "nombre": "Proveedor A"},
    {"id": 2, "nombre": "Proveedor B"},
]

@app.route("/juguetes", methods=["GET"])
def get_juguetes():
    return jsonify(juguetes)

@app.route("/proveedores", methods=["GET"])
def get_proveedores():
    return jsonify(proveedores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
