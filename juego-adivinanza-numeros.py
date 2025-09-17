## Actividad juego adivinanza numeros: crear un juego en el que hay que adivinar un numero del 1 al 100 por consola
import random

def juego_adivinanza():
    # Generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    # Primeras líneas del juego
    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar un número entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # Solitar un número del 1 al 100
        adivinanza = input("Introduzca un  número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Pasa de string a int
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza} ")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos"
                )
        else:
            print("Por favor introduzca un número válido entre el 1 al 100")


juego_adivinanza()
