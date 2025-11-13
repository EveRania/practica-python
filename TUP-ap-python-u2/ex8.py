# 8) Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.


def borrar_duplicados (lista1, lista2): 
    for palabra in lista2 :
        while palabra in lista1:
            lista1.remove(palabra)
        
    print ("Lista resultante: ", lista1)

lista_og=["esta", "es", "la", "lista", "de", "palabras", "original"]
lista2=["esta", "es", "la", "segunda"]
print(lista_og)
print(lista2)

borrar_duplicados(lista_og, lista2)