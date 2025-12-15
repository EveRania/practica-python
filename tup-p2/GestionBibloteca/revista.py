from publicacion import Publicacion

class Revista(Publicacion):
    def __init__(self, titulo, año_publicacion, mes_publicacion, genero):
        super().__init__(titulo, año_publicacion, genero)
        self.__mes_publicacion = mes_publicacion

    def get_mes_publicacion(self):
        return self.__mes_publicacion
    