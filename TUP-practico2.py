## Practico 2: (clases 3 y 4)
# Ejercicio 1: Cadenas de caracteres y slicing
# Escribe un programa que reciba una frase y, utilizando slicing, obtenga las primeras 5 letras, las últimas 5, y la frase invertida.

frase = input("Ingrese una frase ")
print(frase[:5])
print(frase[-5:])
print(frase[::-1])

# Ejercicio 2: Métodos de cadenas
# Enunciado: Escribe un programa que pida al usuario ingresar una frase y realice las siguientes operaciones utilizando métodos de cadenas:
# 1. Convertir la frase a mayúsculas.
# 2. Contar cuántas veces aparece la letra 'a'.
# 3. Reemplazar las vocales por el símbolo '*'.

frase = input("Ingrese una frase: ")

print("En mayúsculas:", frase.upper())
print("Cantidad de 'a': ", frase.count("a"))
print(
    "Vocales reemplazadas: ",
    frase.replace("e", "*")
    .replace("a", "*")
    .replace("i", "*")
    .replace("o", "*")
    .replace("u", "*"),
)

# Ejercicio 3: f-strings
# Enunciado: Crea un programa que pida al usuario su nombre, edad y ciudad, y luego muestre un mensaje formateado usando f-strings del tipo:
# •
# "Hola, [nombre]. Tienes [edad] años y vives en [ciudad]."
# Concepto: Las f-strings (f"...") permiten insertar variables directamente en una cadena de texto de forma más sencilla y legible.
# Ejercicio 4: Métodos de listas
# Enunciado: Escribe un programa que pida al usuario una lista de números (separados por comas) y luego:
# 1.
# Muestre la lista original.
# 2.
# Ordene la lista de menor a mayor.
# 3.
# Elimine el último número de la lista.
# 4.
# Añada un nuevo número al inicio de la lista.
# Concepto: Los métodos de listas como .sort(), .append(), y .pop() son útiles para modificar listas de manera eficiente.
# Ejercicio 5: Tuplas
# Enunciado: Crea una tupla con los días de la semana. Luego, pide al usuario un número del 1 al 7 y muestra el día correspondiente.
# Concepto: Las tuplas son tipos de datos compuestos inmutables, es decir, no se pueden modificar una vez creadas.
# Ejercicio 6: Diccionarios
# Enunciado: Escribe un programa que pida al usuario ingresar el nombre y edad de varias personas, los guarde en un diccionario y luego permita buscar la edad de una persona específica por su nombre.
# Concepto: Los diccionarios son estructuras de datos que almacenan pares clave-valor, donde la clave es única.
# Ejercicio 7: Conjuntos
# Enunciado: Escribe un programa que pida dos listas de números al usuario y luego muestre:
# 1.
# Los elementos que están en ambas listas.
# 2.
# Los elementos que están en la primera lista pero no en la segunda.
# Concepto: Los conjuntos permiten realizar operaciones como intersección y diferencia para identificar elementos comunes o únicos entre colecciones de datos.
# 1. Funciones: Llamada y Retorno de Valores
# Enunciado: Escribe una función llamada suma que reciba dos números como parámetros, los sume y retorne el resultado. Luego, crea un programa que solicite dos números al usuario, llame a la función suma y muestre el resultado en pantalla.
# 2. Parámetros Mutables e Inmutables
# Enunciado: Crea una función llamada modificar_lista que reciba una lista como parámetro, agregue un nuevo valor a la lista, y luego imprima la lista dentro de la función. Luego, fuera de la función, imprime la lista nuevamente para verificar si ha sido modificada.
# 3. Parámetros por Defecto
# Enunciado: Escribe una función llamada saludar que reciba el nombre de una persona y un saludo opcional con un valor por defecto de "Hola". Si el saludo no se especifica, la función debe usar el valor por defecto. Luego, crea un programa que llame a la función varias veces, algunas veces con un saludo personalizado y otras veces sin especificar el saludo.
# 4. Docstring
# Enunciado: Crea una función llamada multiplicar que reciba dos números y retorne su producto. Asegúrate de agregar un docstring que explique lo que hace la función y los parámetros que recibe.
# 5. Funciones Lambda/Anónima
# Enunciado: Escribe una función lambda que reciba un número y devuelva su cuadrado. Luego, usa la función map para aplicar esta función lambda a una lista de números del 1 al 5.
# 6. Funciones con Argumentos de Referencia y Valor
# Enunciado: Escribe una función llamada duplicar_valor que reciba una variable y la duplique.
# luego, crea otra función llamada duplicar_lista que reciba una lista y duplique cada uno de sus elementos. Muestra el efecto de pasar valores por referencia y por valor.
