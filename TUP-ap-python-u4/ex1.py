# 1) Crea la clase Vehiculo, extiende la clase y realiza la siguiente implementación:
#  Vehículo(color ruedas) : coche (velocidad-km/h)(cilindrada(cc)): camioneta (carga(kg)), bicicleta(tipo urbana/deportiva): motocicleta (velocidad (km/h). cilindrada (cc))
# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.Nota: Puedes utilizar el atributo especial de clase name para recuperar el nombre de la clase de un objeto: type(objeto).__name__

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
for v in vehiculos:
    print(v)
    print("Clase:", type(v).__name__)
    print()
