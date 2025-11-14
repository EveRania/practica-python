# 10) Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.


def capicua(cadena):
    i = 0
    f = len(cadena) - 1

    while i < f:
        if cadena[i] != cadena[f]:
            print(f"La cadena {cadena} no es capicúa")
            return False

        i += 1
        f -= 1
    print(f"La cadena {cadena} es capicúa")
    return True


capicua("espacio")
capicua("12321")
capicua("estudiante")
capicua("neuquen")
capicua("radar")
capicua("python")
