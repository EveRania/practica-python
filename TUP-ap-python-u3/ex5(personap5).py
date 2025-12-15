# 5- Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.


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

    def es_mayor_de_edad(self):
        if self.edad < 18:
            print(
                f"{self.nombre} tiene {self.edad} años, por lo tanto es menor de edad"
            )
            return False
        else:
            print(
                f"{self.nombre} tiene {self.edad} años, por lo tanto es mayor de edad"
            )
            return True

    def es_mayor_que(self, otra_persona):
        if self.edad > otra_persona.edad:
            print(f"{self.nombre} es mayor que {otra_persona.nombre}")
            return True
        else:
            print(f"{otra_persona.nombre} es mayor que {self.nombre}")
            return False

    def get_mayor(persona1, persona2):
        if persona1.edad > persona2.edad:
            return persona1
        else:
            return persona2

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

persona1.es_mayor_que(persona2)
persona3.es_mayor_que(persona1)
persona2.es_mayor_que(persona3)

mayor = Persona.get_mayor(persona1, persona2)
print(f"La persona mayor es: {mayor.nombre} ({mayor.edad}años)")
mayor2 = Persona.get_mayor(persona1, persona3)
print(f"La persona mayor es: {mayor.nombre} ({mayor.edad}años)")
mayor3 = Persona.get_mayor(persona2, persona3)
print(f"La persona mayor es: {mayor.nombre} ({mayor.edad}años)")
