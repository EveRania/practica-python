# 11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.

cadena = input("Ingrese una cadena: ")
ancho = 80

espacios = (ancho - len(cadena)) // 2

print(" " * espacios + cadena + " " * espacios)
