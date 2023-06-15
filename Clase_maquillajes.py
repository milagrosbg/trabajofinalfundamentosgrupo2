class Maquillaje:

    def __init__(self, codigo, nombre, precio, stock, marca, color, acabado) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.color = color
        self.acabado = acabado


    def serialize(self):
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'name': self.precio,
            'stock': self.stock,
            'marca': self.marca
        }

    def serialize_details(self):
        return {
            'codigo': self.codigo,
            'nombre':self.nombre,
            'precio': self.precio,
            'stock': self.stock,
            'marca': self.marca,
            'color': self.color,
            'acabado': self.acabado
        }