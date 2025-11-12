# 4) Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
# **********
# **********
# **********
# **********
# **********

# **
# ****
# ******
# ********
# **********


def patron_10(filas):
    for x in range(filas):
        print("**********")


def patron_des(filas):
    for x in range(filas):
        print((2 * x) * "*")


patron_10(5)
patron_des(10)

