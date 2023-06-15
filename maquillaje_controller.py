from Maquillajedb import get_db
from Clase_maquillajes import Maquillaje


def insert_maquillaje(codigo, nombre, precio, stock, marca, color, acabado):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO maquillajes (codigo, nombre, precio, stock, marca, color, acabado) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?)"
    cursor.execute(statement, [codigo, nombre, precio, stock, marca, color, acabado])
    db.commit()
    return True

def update_maquillaje(codigo, nombre, precio, stock, marca, color, acabado):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE maquillajes SET nombre = ?, precio = ?, stock = ?, marca = ?, color= ?, acabado = ? \
    WHERE codigo = ?"
    cursor.execute(statement, [nombre, precio, stock, marca, color, acabado, codigo])
    db.commit()
    return True


def delete_maquillaje(codigo):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM maquillajes WHERE codigo = ?"
    cursor.execute(statement, [codigo])
    db.commit()
    return True


def get_by_codigo(codigo):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT codigo, nombre, precio, stock, marca, color, acabado FROM maquillajes \
    WHERE codigo = ?"
    cursor.execute(statement, [codigo])
    single_maquillaje = cursor.fetchone()
    codigo = single_maquillaje[0]
    nombre = single_maquillaje[1]
    precio = single_maquillaje[2]
    stock = single_maquillaje[3]
    marca = single_maquillaje[4]
    color = single_maquillaje[5]
    acabado = single_maquillaje[6]
    maquillaje = Maquillaje(codigo, nombre, precio, stock, marca, color, acabado)
    return maquillaje.serialize_details()


def get_maquillajes():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT codigo, nombre, precio, stock, marca, color, acabado FROM maquillajes"
    cursor.execute(query)
    maquillaje_list = cursor.fetchall()
    list_of_maquillaje = []
    for maquillaje in maquillaje_list:
        codigo = maquillaje[0]
        nombre = maquillaje[1]
        precio = maquillaje[2]
        stock = maquillaje[3]
        marca = maquillaje[4]
        color = maquillaje[5]
        acabado = maquillaje[6]
        maquillaje_to_add = Maquillaje(codigo, nombre, precio, stock, marca, color, acabado)
        list_of_maquillaje.append(maquillaje_to_add)
    return list_of_maquillaje




