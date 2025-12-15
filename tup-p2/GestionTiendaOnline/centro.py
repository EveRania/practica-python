class centro():
    def __init__(self, codigo, direccion):
        self.__codigo = codigo
        self.__direccion = direccion
        self.__productos = []

    def get_codigo(self):
        return self.__codigo

    def get_direccion(self):
        return self.__direccion

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def remover_producto(self, producto):
        if producto not in self.__productos:
            raise ValueError("El producto no está en la lista de productos del centro")
        self.__productos.remove(producto)

    def get_productos(self):
        return self.__productos
    
    def get_valor_total(self):
        return sum(producto.get_monto_total() for producto in self.__productos)
    
    def get_valor_total_categoria(self, categoria):
        return sum(producto.get_monto_total() for producto in self.__productos if producto.get_categoria() == categoria)    
    
    def get_valor_total_producto(self, producto):
        if producto not in self.__productos:
            raise ValueError("El producto no está en la lista de productos del centro")
        return producto.get_monto_total()
