class Dispositivo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo  = modelo
        self.precio = precio
        self.estado = "apagado" # estado inicial
    
    def encender(self):
        self.estado = "encendido"
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        print(f"Estado: {self.estado}")