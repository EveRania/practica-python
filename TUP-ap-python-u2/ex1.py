## Actividad Práctica - Python Unidad 2
# 1) Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.

def mayor_de_tres(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1  # num1 es mayor que num2 y 3
        elif num1 == num3:
            return -1  # num 1 y 3 iguales
        else:
            return num3  # num3 es mayor que 1 y 2

    elif num2 == num1:
        if num1 > num3:
            return -1  # num 1 y 2 iguales
        elif num3 > num1:
            return num3  # num3 es el mayor
        else:
            return -1  # todos iguales

    else:  # num2 es mayor a num1
        if num2 > num3:
            return num2  # b es el mayor
        elif num2 == num3:
            return -1  # 2 y 3 son iguales
        else:
            return num3  # num 3 es el  mayor


num1 = input("Ingrese el primer numero a comparar: ")
num2 = input("Ingrese el segundo numero a comparar: ")
num3 = input("Ingrese el tercer numero a comparar: ")

mayor = mayor_de_tres(num1, num2, num3)
if mayor == -1:
    print("No existe un mayor estricto.")
else:
    print(f"El mayor estricto es: {mayor}.")

