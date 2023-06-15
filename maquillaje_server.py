from flask import Flask, jsonify, request
import maquillaje_controller
from Maquillajedb import create_tables
from exchange import get_xr


app = Flask(__name__)


@app.route('/maquillaje', methods=["GET"])
def get_maquillajes():
    maquillajes = maquillaje_controller.get_maquillajes()
    maquillaje_list=[]
    for maquillaje in maquillajes:
        elem = maquillaje.serialize_details()
        maquillaje_list.append(elem)
    return jsonify(maquillaje_list)

@app.route("/maquillaje/create", methods=["POST"])
def insert_maquillaje():
    maquillaje_details = request.get_json()
    codigo = maquillaje_details["codigo"]
    nombre = maquillaje_details["nombre"]
    precio = maquillaje_details["precio"]
    stock = maquillaje_details["stock"]
    marca = maquillaje_details["marca"]
    color = maquillaje_details["color"]
    acabado = maquillaje_details["acabado"]
    result = maquillaje_controller.insert_maquillaje(codigo, nombre, precio, stock, marca, color, acabado)
    return jsonify(result)


@app.route("/maquillaje/modify", methods=["PUT"])
def update_maquillaje():
    maquillaje_details = request.get_json()
    codigo = maquillaje_details["codigo"]
    nombre = maquillaje_details["nombre"]
    precio = maquillaje_details["precio"]
    stock = maquillaje_details["stock"]
    marca = maquillaje_details["marca"]
    color = maquillaje_details["color"]
    acabado = maquillaje_details["acabado"]
    result = maquillaje_controller.update_maquillaje(codigo, nombre, precio, stock, marca, color, acabado)
    return jsonify(result)


@app.route("/maquillaje/eliminate/<codigo>", methods=["DELETE"])
def delete_maquilaje(codigo):
    result = maquillaje_controller.delete_maquillaje(codigo)
    return jsonify(result)


@app.route("/maquillaje/<codigo>", methods=["GET"])
def get_maquillaje_by_codigo(codigo):
    maquillaje = maquillaje_controller.get_by_codigo(codigo)
    return jsonify(maquillaje)


@app.route("/maquillaje/usd/<codigo>", methods=["GET"])
def get_maquillaje_by_codigo_usd(codigo):
    maquillaje = maquillaje_controller.get_by_codigo(codigo)
    xr = get_xr()
    precio_usd = maquillaje['precio']/xr
    maquillaje['precio'] = round(precio_usd,2)
    return jsonify(maquillaje)



create_tables()

app.run()

if __name__ == '__main__':
    app.run()

