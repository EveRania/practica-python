# 2) Agregarle a la clase anterior un constructor que reciba nombre y edad.


class Persona:
    def __init__(self, nombre, edad):
        self.set_nombre(nombre)
        self.set_edad(edad)

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(
        self,
    ):
        print(f"{self.nombre} tiene {self.edad} años ")


persona1 = Persona("Juan", 34)
persona2 = Persona("Laura", 20)
persona1.print_persona()
persona2.print_persona()
