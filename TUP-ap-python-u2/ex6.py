# 6) Crear una función lambda para comprobar si un número es par o impar. Desarrollar además un programa para verificar el comportamiento de la función.


es_par = lambda num: "par" if num % 2 == 0 else "impar"

numero = int(input("Ingrese un número: "))
print(f"El número {numero} es {es_par(numero)}")
