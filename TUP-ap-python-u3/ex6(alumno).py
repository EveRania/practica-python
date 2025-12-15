# 6- Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´


class Alumno:
    # atributos: nombre, nota.
    # metodos inicializar atributos, imprimirlos, motrar mensaje con nota y si aprobado o no.

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self): 
        return f"La nota de {self.nombre} es {self.nota}"
    
    def aprobado(self) :
        if self.nota >= 6 :
            print("Esta aprobado")
            return True
        else : 
            print("NO esta aprobado")
            return False
    
alumno1 = Alumno("Juan", 6)
alumno2 = Alumno("Carlos", 10)
alumno3 = Alumno("Matias", 3)
print(alumno1)
alumno1.aprobado()
print(alumno2)
alumno2.aprobado()
print(alumno3)
alumno3.aprobado()