# 3. Parámetros por Defecto
# Enunciado: Escribe una función llamada saludar que reciba el nombre de una persona y un saludo opcional con un valor por defecto de "Hola". Si el saludo no se especifica, la función debe usar el valor por defecto. Luego, crea un programa que llame a la función varias veces, algunas veces con un saludo personalizado y otras veces sin especificar el saludo.

def saludar (nombre, saludo="Hola") :
    print(f"{saludo} {nombre}")


saludar("Eve")
saludar("Flor", "Qué tal")
saludar("Duko y Taco")
saludar("Agustín", "Buen día")