# 4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:resultado = 10/0

try : 
    resultado = 10/0
    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
    

