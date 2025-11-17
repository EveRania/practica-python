# 12) Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de Octubre de 2017”. Escribir también un programa para verificar su comportamiento.


def fecha_extendida(dia, mes, año):
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    if año < 100:
        if año > 30:
            año += 1900
        else:
            año += 2000

    print(f"{dia} de {meses[mes - 1]} de {año}")


fecha_extendida(2, 5, 94)
fecha_extendida(8, 11, 90)
fecha_extendida(9, 12, 25)
