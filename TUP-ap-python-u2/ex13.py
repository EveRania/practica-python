# 13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.


def frase_ordenada_unicas(frase):
    palabras = frase.split()

    unicas = set(palabras)
    ordenadas= list(unicas)

    ordenadas.sort(key=len)
    

    print("Palabras ordenadas por longitud: ")
    for p in ordenadas:
        print(p)


frase= input("Ingrese una frase: ")

frase_ordenada_unicas(frase)
