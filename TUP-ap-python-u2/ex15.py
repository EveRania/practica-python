# 15) Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dados, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función utilizando rebanadas.


def eliminar_subcadena(cadena, posicion, cant):
    # tomaria la cadena original y slice desde principio hasta posicion y desde posicion+cant hasta final
    # concaternaria las cadenas resultantes
    return cadena[:posicion] + cadena[posicion + cant :]


# Programa para verificar comportamiento

text = input("Ingrese una cadena de caracteres: ")
inicio = int(input("Ingrese la posición desde donde quiere eliminar"))
cantidad_caracteres = int(input("Ingrese la cantidad de caracteres a eliminar"))

cadena_final = eliminar_subcadena(text, inicio, cantidad_caracteres)

print(f"La cadena original es{text} y la cadena resultante es {cadena_final}")
