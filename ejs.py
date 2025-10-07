

# Ejercicio 6: Diccionarios
# Enunciado: Escribe un programa que pida al usuario ingresar el nombre y edad de varias personas, los guarde en un diccionario y luego permita buscar la edad de una persona específica por su nombre.

personas = {}

while True:
    nombre = input("Ingrese el nombre o 'salir' para terminar ")
    if nombre.lower() == "salir":
        break
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    personas[nombre] = edad 
 
persona = input("Ingrese el nombre de la persona que deseas buscar ")
print(f"{persona} tiene {personas[persona]} años ")


