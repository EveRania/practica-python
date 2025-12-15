# 3- Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.


class Persona:
    def __init__(self, nombre, edad):
        self.set_nombre(nombre)
        self.set_edad(edad)
        # self.es_mayor_de_edad(nombre, edad)

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad
    
    def es_mayor_de_edad (self) : 
        if self.edad < 18 : 
            print(f"{self.nombre} tiene {self.edad} años, por lo tanto es menor de edad")
            return False
        else : 
            print(f"{self.nombre} tiene {self.edad} años, por lo tanto es mayor de edad")
            return True

    def print_persona(
        self,
    ):
        print(f"{self.nombre} tiene {self.edad} años ")


persona1 = Persona("Juan", 34)
persona2 = Persona("Laura", 20)
persona3 = Persona("Emma", 6)

persona1.print_persona()
persona2.print_persona()
persona3.print_persona()

persona1.es_mayor_de_edad()
persona2.es_mayor_de_edad()
persona3.es_mayor_de_edad()

