# 7- Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es {mayor}")

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print(
                f"El triangulo de lados: {self.lado1}, {self.lado2} y {self.lado3} es equilatero, todos sus lados son iguales"
            )
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:

            print(
                f"El triangulo de lados: {self.lado1}, {self.lado2} y {self.lado3} es escaleno, todos sus lados son desiguales"
            )

        else:
            print(
                f"El triangulo de lados: {self.lado1}, {self.lado2} y {self.lado3} es isosceles, tiene dos lados iguales"
            )


forma1 = Triangulo(12, 6, 9)
forma1.lado_mayor()
forma1.tipo_triangulo()

forma2 = Triangulo(4, 5, 6)
forma2.lado_mayor()
forma2.tipo_triangulo()

forma3 = Triangulo(3, 5, 3)
forma3.lado_mayor()
forma3.tipo_triangulo()

forma4 = Triangulo(9, 9, 9)
forma4.lado_mayor()
forma4.tipo_triangulo()
