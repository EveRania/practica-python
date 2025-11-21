# 1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.


class Persona:
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self, ):
        print(f"{self.nombre} tiene {self.edad} años ")


persona1 = Persona()
persona1.set_nombre  ("Juan")
persona1.set_edad (34)

persona2 = Persona()
persona2.set_nombre ("Laura")
persona2.set_edad  (20)

persona1.print_persona()
persona2.print_persona()