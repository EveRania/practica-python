# 7) Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.


def calcular_cuadrados(n):
    cuadrados = []
    for i in range(1, n + 1):
        cuadrados.append(i**2)
    return cuadrados


limite = int(input("Ingrese el número límite: "))


lista_cuadrados = calcular_cuadrados(limite)
print(lista_cuadrados[-10:])
