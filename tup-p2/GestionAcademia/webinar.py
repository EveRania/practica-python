from datetime import date

class Webinar():

    def __init__(self, nombre, mes_inicio, anio_inicio):
        self.__nombre = nombre
        self.__mes_inicio = mes_inicio
        self.__anio_inicio = anio_inicio
        self.__estudiantes = []
        self.__estudiantes_finales = []

    def get_nombre(self):
        return self.__nombre
    
    def get_mes_inicio(self):
        return self.__mes_inicio
    
    def get_anio_inicio(self):
        return self.__anio_inicio
    
    def get_estudiantes(self):
        return self.__estudiantes
    
    def get_cantidad_estudiantes(self):
        return len(self.__estudiantes)
    
    def agregar_estudiante(self, estudiante):
        mes_actual = date.today().month
        anio_actual = date.today().year
        if (self.__anio_inicio < anio_actual) or (self.__anio_inicio == anio_actual and self.__mes_inicio < mes_actual):
            raise Exception("La fecha de inicio ya ha pasado.")
        self.__estudiantes.append(estudiante)

    def agregar_estudiante_final(self, estudiante):
        if estudiante not in self.__estudiantes:
            raise Exception("El estudiante no está en la lista de estudiantes.")
        self.__estudiantes_finales.append(estudiante)