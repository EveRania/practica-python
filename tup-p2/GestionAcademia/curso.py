from webinar import Webinar
from datetime import date
class Curso(Webinar):

    def __init__(self, nombre, mes_inicio, anio_inicio, cupo_maximo=30):
        super().__init__(nombre, mes_inicio, anio_inicio)
        self.__cupo_maximo = cupo_maximo

    def get_cupo_maximo(self):
        return self.__cupo_maximo
    
    def agregar_estudiante(self, estudiante):
        if self.get_cantidad_estudiantes() >= self.__cupo_maximo:
            raise Exception("No se puede agregar más estudiantes, el cupo máximo es 30.")
        super().agregar_estudiante(estudiante)