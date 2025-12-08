# 8- Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.


class Calculadora:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número entero: "))
        self.num2 = int(input("Ingrese el segundo número entero: "))

    def suma(self):
        print(f"La suma de {self.num1} + {self.num2} es {self.num1 + self.num2} ")

    def resta(self):
        print(f"La resta de {self.num1} - {self.num2} es {self.num1 - self.num2} ")

    def multiplicacion(self):
        print(
            f"La multiplicación de {self.num1} * {self.num2} es {self.num1 * self.num2} "
        )

    def division(self):
        print(f"La división de {self.num1} / {self.num2} es {self.num1 / self.num2} ")



cuenta1 = Calculadora()
cuenta1.suma()
cuenta1.resta()
cuenta1.multiplicacion()
cuenta1.division()
