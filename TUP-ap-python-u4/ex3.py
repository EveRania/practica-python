# 3) Continua con el ejercicio anterior y modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje “Se han encontrado {} vehículos con {} ruedas:” únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.


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
        return f"{type(self).__name__} (color = {self.color}, ruedas = {self.ruedas}, tipo = {self.tipo}, velocidad = {self.velocidad}, cilindrada = {self.cilindrada})"


# Programa principal : crear objetos y agregarlos a una lista
vehiculos = [
    Coche("rojo", 4, 120, 1600),
    Camioneta("blanca", 4, 100, 2000, 1500),
    Bicicleta("azul", 2, "urbana"),
    Motocicleta("negra", 2, "deportiva", 180, 600),
]


def catalogar(vehiculos, ruedas=None):
    encontrados = []

    for v in vehiculos:
        if ruedas is None or v.ruedas == ruedas:
            encontrados.append(v)

    if ruedas is not None:
        print(f"Se han encontrado {len(encontrados)} vehículos con {ruedas} ruedas: \n")

    for v in encontrados:
        print(f"Clase: {type(v).__name__}")
        print(v)
        print()


catalogar(vehiculos, 4)
catalogar(vehiculos, 0)
catalogar(vehiculos, 2)
