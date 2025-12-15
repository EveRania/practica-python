from categoria import Categoria

class Producto():
    def __init__(self, nombre, precio, categoria:Categoria, stock_minimo, stock = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria
        self.__stock = stock
        self.__stock_minimo = stock_minimo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_categoria(self):
        return self.__categoria

    def get_stock(self):
        return self.__stock

    def get_stock_minimo(self):
        return self.__stock_minimo

    def agregar_stock(self, cantidad):
        self.__stock += cantidad

    def reducir_stock(self, cantidad):
        if cantidad > self.__stock:
            raise ValueError("No hay suficiente stock para reducir")
        elif self.__stock < self.__stock_minimo and cantidad > 1:
            raise ValueError("Solo se puede reducir 1 unidad si el stock es menor que el mínimo")
        self.__stock -= cantidad

    def get_monto_total(self):
        return self.__precio * self.__stock