# 9) Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función.


def lista_ordenada(lista):
    lista_ordenada = lista.copy()
    lista_ordenada.sort()

    if lista_ordenada == lista:
        print("La lista se encuentra ordenada en forma ascendente")
        return True
    else:
        print("La lista no se encuentra ordenada en forma ascendente")
        return False



# programa para verificar comportamiento
# Lista ordenada asc
lista_ordenada(lista=[1, 2, 3, 4, 5])
lista_ordenada(lista=["a", "b", "c", "d", "e", "f"])

# Lista ordenada des
lista_ordenada(lista=[5, 4, 3, 2, 1])
lista_ordenada(lista=["f", "e", "d", "c", "b", "a"])

# Lista desordenada
lista_ordenada(lista=[20, 3, 4, 7, 6])
lista_ordenada(lista=["g", "l", "m", "p", "a", "b", "c"])
