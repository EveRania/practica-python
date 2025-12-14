# 2) Continua con el ejercicio anterior y realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.

# clase Vehiculo
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"{type(self).__name__}(color={self.color}, ruedas = {self.ruedas})"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return (
            f"{type(self).__name__}(color = {self.color}, ruedas = {self.ruedas}, "
            f"velocidad = {self.velocidad}, cilindrada = {self.cilindrada})"
        )


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"{type(self).__name__}(color = {self.color}, ruedas = {self.ruedas}, velocidad = {self.velocidad}, cilindrada = {self.cilindrada}, carga = {self.carga})"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{type(self).__name__}(color = {self.color}, ruedas = {self.ruedas}, tipo = {self.tipo})"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{type(self).__name__} (color = {self.color}, ruedas = self.ruedas, tipo = self.tipo, velocidad = self.velocidad, cilindrada = self.cilindrada)"


# Programa principal : crear objetos y agregarlos a una lista
vehiculos = [
    Coche("rojo", 4, 120, 1600),
    Camioneta("blanca", 4, 100, 2000, 1500),
    Bicicleta("azul", 2, "urbana"),
    Motocicleta("negra", 2, "deportiva", 180, 600),
]


# Mostrar vehiculos y el nombre de su clase

def catalogar (): 

    for v in vehiculos:
        print("Clase:", type(v).__name__)
        print(v)
        print()


catalogar()