# Controladores de flujo

# 1.Condicionales: sentencia if:
# Crea un programa que solicite la edad de una persona e indique si es mayor de edad (18 años o más) o no.
# Variante: Modifica el programa para que además indique si es un adolescente (entre 13 y 17 años).

edad = int(input("Ingrese su edad "))

if edad >= 18 :
    print("Usted es mayor de edad")
elif edad >=13 and edad <= 17 :
    print("Usted es adolescente")
else :
    print("Usted es menor de edad")


# 2. Condicionales anidadas: Escribe un programa que le pida al usuario ingresar su nota en una prueba (un número entre 0 y 10). El programa debe mostrar: "Insuficiente" si la nota es menor que 4; "Regular" si la nota es mayor o igual a 4 pero menor que 6; "Bueno" si la nota es mayor o igual a 6 pero menor que 8; "Muy Bueno" si la nota es mayor o igual a 8 pero menor que 10; "Excelente" si la nota es igual a 10.

nota = float(input("Ingrese su nota (Debe ser un numero entre 0 y 10) "))

if nota < 4:
    print("Insuficiente")
elif nota >= 4 and nota < 6:
    print("Regular")
elif nota >= 6 and nota < 8:
    print("Bueno")
elif nota >= 8 and nota < 10:
    print("Muy bueno")
else :
    print("Excelente")


# 3. Estructuras iterativas: while:
# Escribe un programa que solicite al usuario un número entero positivo e imprima todos los números desde 1 hasta ese número.
# Variante: Haz que el programa también sume todos los números impresos y muestre el total al final.

num = int(input("Ingrese un número entero positivo "))
n = 1
suma = 0
while n <= num:
    print(n)
    suma += n
    n += 1

print(suma)

#4. Estructuras iterativas: for: Escribe un programa que imprima la tabla de multiplicar del número que el usuario elija. Usa la sentencia for.

num = int(input("Ingrese el numero a multiplicar "))

for n in range(11):
    resultado = num * n
    print(f"{num} * {n} = {resultado}")
    n+= 1


# 5.Iteración controlada con while y input: Crea un programa que solicite al usuario una contraseña (puedes definir una tú). El programa debe pedir la contraseña hasta que el usuario la escriba correctamente.

psw = "12345678"

ingresada = input ("Ingrese su contraseña ")

while ingresada != psw :

    ingresada = input ("Por favor ingrese su contraseña correctamente ")

print("Contraseña ingresada correctamente")