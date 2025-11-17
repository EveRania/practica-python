# 14) Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.

def eliminar_claves(diccionario, claves): 
    eliminado = False

    for (clave) in claves :
        if clave in diccionario:
            del diccionario[clave]
            eliminado = True 

    return diccionario, eliminado
