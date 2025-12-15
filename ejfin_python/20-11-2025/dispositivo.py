class Dispositivo:
    # * Todos los dispositivos comparten: marca, modelo, precio y estado (inicialmente "apagado")
    # * Cada dispositivo debe poder encenderse y mostrar su información específica
    def __init__(self, marca, modelo, precio, estado="apagado"):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.estado = estado

    def encender(self):
        self.estado = "encendido"
        

    def mostrar_info(self):
        print("Info del dispositivo: ")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        print(f"Estado: {self.estado}")

    def instalar_app(self, app):
        pass


