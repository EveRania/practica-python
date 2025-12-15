from dispositivo import Dispositivo
# Tablet:


# * Tamaño de pantalla en pulgadas
# * Modo tablet especial
# * Información debe incluir tamaño de pantalla
class Tablet(Dispositivo):
    def __init__(self, marca, modelo, precio, tamaño_pantalla):
        super().__init__(marca, modelo, precio)
        self.tamaño_pantalla = tamaño_pantalla
        self.modo = "normal"

    def mostrar_info(self):
        
        super().mostrar_info()
        
        print(f"Tamaño de pantalla: {self.tamaño_pantalla} pulgadas")
        print(f"Modo tablet: {self.modo}")

    def modo_tablet(self):
        self.modo = "especial"
        print(f"Modo tablet: {self.modo} activado")

