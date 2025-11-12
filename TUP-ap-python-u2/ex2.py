# 2) Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.

def fecha_valida(dia,mes, año):
    # dia entre 1 y 31
    # mes entre 1 y 12
    # año hast 4 digitos
    if dia >= 1 and dia <= 31:
        if mes >=1 and mes <= 12 :
            if año >=1 and año <= 9999:
                print(f"Fecha válida: {dia}/{mes}/{año}")
                return True

    print(f"Fecha inválida: {dia}/{mes}/{año}")
    return False 
        # print(f"Fecha inválida: {dia}/{mes}/{año}")


#todo valido
fecha_valida(1,1,1994)
# dia y mes valido
fecha_valida(2,5,20012)
# dia y año valido
fecha_valida(3,16,2005)
# mes y año valido
fecha_valida(35,2,2020)
#solo dia valido
fecha_valida(10,20,33335)
#solo mes valido
fecha_valida(40,6,10006)
#solo año valido
fecha_valida(60,18,90)
# todo invalido
fecha_valida(40,19,60006)

fecha_valida(2,5,2005)