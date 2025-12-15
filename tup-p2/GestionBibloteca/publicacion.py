from genero import Genero

class Publicacion():
    def __init__(self, titulo, año_publicacion, genero: Genero, copias=1):
        self.__titulo = titulo
        self.__año_publicacion = año_publicacion
        self.__genero = genero
        self.__copias = copias

    def get_titulo(self):
        return self.__titulo
    
    def get_año_publicacion(self):
        return self.__año_publicacion
    
    def get_genero(self):
        return self.__genero
    
    def get_copias(self):
        return self.__copias

    def prestar_copia(self):
        if not self.__copias > 0:
            raise ValueError("No hay copias disponibles para prestar.")
        self.__copias -= 1

    def devolver_copia(self):
        self.__copias += 1