# # Actividad Práctica - Python Unidad 1
# # 1) Escribe un programa muestre por pantalla “Hello World”.

print("Hello World")


# # 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.

print(3 + 5)


# # 3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”

nombre_usuario = input("Ingrese su nombre ")
print(f" Hola {nombre_usuario}")


# # 4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.

num1 = int(input("Ingrese un número "))
num2 = int(input("Ingrese otro número "))
print(num1 + num2)


# # 5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.

num1 = int(input("Ingrese un número "))
num2 = int(input("Ingrese otro número "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}")


# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.

num1 = int(input("Ingrese un número "))
num2 = int(input("Ingrese otro número "))
num3 = int(input("Ingrese otro número "))

if num1 > num2 and num1 > num3:
    print(f"{num1} es mayor que {num2} y {num3}")
elif num1 < num2 and num3 < num2:
    print(f"{num2} es mayor que {num1} y {num3}")
else:
    print(f"{num3} es mayor que {num1} y {num2}")


# 7) Escribe un programa que pida un número y diga si es divisible por 2

num1 = int(input("Ingrese un número "))
modulo = num1 % 2
if modulo == 0:
    print(f"El numero {num1} es divisible por 2")
else:
    print(f"El numero {num1} no es divisible por 2")


# 8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)

num1 = int(input("Ingrese un número "))
mod2 = num1 % 2
mod3 = num1 % 3
mod5 = num1 % 5
mod7 = num1 % 7

if mod2 == 0 or mod3 == 0 or mod5 == 0 or mod7 == 0:
    print(f"El numero {num1} es divisible por 2, 3, 5 o 7")
else:
    print(f"El numero {num1} no es divisible por 2, 3, 5 o 7")


# 9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)

num1 = int(input("Ingrese un número "))
mod2 = num1 % 2
mod3 = num1 % 3
mod5 = num1 % 5
mod7 = num1 % 7

if mod2 == 0:
    print(f"El numero {num1} es divisible por 2")
if mod3 == 0:
    print(f"El numero {num1} es divisible por 3")
if mod5 == 0:
    print(f"El numero {num1} es divisible por 5")
if mod7 == 0:
    print(f"El numero {num1} es divisible por 7")


# 10) Escribir un programa que escriba en pantalla los divisores de un número dado

num1 = int(input("Ingrese un número "))
print(f"El número {num1} es divisible por: ")
for i in range(1, num1 + 1):
    if num1 % i == 0:
        print(f"{i}")


# 11) Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)

num1 = int(input("Ingrese un número "))
primo = True

if num1 <= 1:
    print(f"{num1} no es número primo porque es 1 o un numero menor")
else:
    for i in range(2, num1):
        if num1 % i == 0:
            primo = False
            break
if primo:
    print(f"{num1} es un número primo.")
else:
    print(f"{num1} no es un número primo.")


# 12) Pide una nota (número). Muestra la calificación según la nota:
#  0-3: Muy deficiente
#  3-5: Insuficiente
#  5-6: Suficiente
#  6-7: Bien
#  7-9: Notable
#  9-10: Sobresaliente

nota = float(input("Ingrese su nota (Debe ser un numero entre 0 y 10) "))

if nota < 3:
    print("Muy deficiente")
elif nota >= 3 and nota < 5:
    print("Insuficiente")
elif nota >= 5 and nota < 6:
    print("Suficiente")
elif nota >= 6 and nota < 7:
    print("Bien")
elif nota >= 7 and nota < 9:
    print("Notable")
else:
    print("Sobresaliente")


# 13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# ……….

for i in range(31):
    print(i * f"{i}")


# 14) Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 6):
# 666666
# 55555
# 4444
# 333
# 22
# 1

num = int(input("Ingrese un número "))

for i in range(num, 0, -1):
    print(i * f"{i}")


# 15) Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo:
# 1
# 2
# 3
# 4 (Múltiplo de 4)
# 5
# ------------------------------------------------------------
# 6
# 7
# 8 (Múltiplo de 4)
# 9 (Múltiplo de 9)
# 10

for i in range(1, 501):
    if i % 4 == 0:
        print(f"{i} (múltiplo de 4)")
    elif i % 9 == 0:
        print(f"{i} (múltiplo de 9)")
    elif i % 5 == 0:
        print(f"{i}")
        print(30 * "-")
    else:
        print(f"{i}")
