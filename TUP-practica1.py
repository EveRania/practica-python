# 1.Hola Mundo: Escribe un programa en Python que imprima en pantalla el mensaje "Hola Mundo". Luego modifica el mensaje para que diga "Bienvenidos a la programación en Python".
print("Hola mundo")
print("Bienvenidos a la programación en Python")


# 2.Salida por pantalla: Escribe un programa que muestre tu nombre, tu edad y tu ciudad en líneas separadas usando la función print.

print("Mi nombre es Evelyn")
print("Mi edad es 30 años")
print("Vivo en Rosario, Santa Fé")


# 3.Lectura por teclado: Escribe un programa que solicite al usuario su nombre, edad y ciudad. Luego, muestra un mensaje de saludo personalizado utilizando esos datos.

nombre = input("Ingrese su nombre ")
edad = input("Ingrese su edad ")
ciudad = input("Ingrese la ciudad en la que vive ")
nombre = nombre.capitalize()
ciudad = ciudad.capitalize()

print(f"Hola, soy {nombre}, tengo {edad} años y vivo en {ciudad}")

# 4.Tipo de datos: Crea un programa que le pida al usuario ingresar dos números enteros y un número flotante. Luego muestra la suma de los dos enteros y el producto del entero con el flotante.

int1 = input("Ingrese un número entero ")
int2 = input("Ingrese otro número entero ")
decimal = input("Ingrese un número decimal ")

suma_enteros = int(int1) + int(int2)
producto = suma_enteros * float(decimal)

print(
    f"La suma de {int1} + {int2} es igual a {suma_enteros}. La multiplicación de esta suma con el número decimal es igual a {producto}  "
)


# 5. Tipo de operadores: Aritméticos: Diseña un programa que tome dos números enteros del usuario y muestre:La suma, la resta, la multiplicación, la división (ten en cuenta que uno puede ser 0, verifica esto antes de dividir)y el módulo (resto de la división).


num1 = input("Ingrese un número entero ")
num2 = input("Ingrese otro número entero ")
num1 = int(num1)
num2 = int(num2)

suma = num1 + num2
print(f"La suma de los numeros {num1} y {num2} es {suma}")
resta = num1 - num2
print(f"La resta de los numeros {num1} y {num2} es {resta}")
multiplicacion = num1 * num2
print(f"La multiplicación de los numeros {num1} y {num2} es {multiplicacion}")

if num1 and num2 != 0:
    division = num1 / num2
    print(f"La división de los numeros {num1} y {num2} es {division}")
    modulo = num1 % num2
    print(f"El resto de la división de los numeros {num1} y {num2} es {modulo}")
else:
    print("No es posible dividir ni calcular el resto por 0 ")


# 6. Variables: escribe un programa en el que declares una variable para almacenar tu nombre, otra para tu edad y otra para la calificación de tu última prueba. Luego muestra un mensaje que diga: "Mi nombre es X, tengo X años y mi última calificación fue X."

nombre = "Evelyn"
edad = 30
calificacion = 8.70

print(
    f"Mi nombre es {nombre}, tengo {edad} años y mi última calificación fue {calificacion}"
)
