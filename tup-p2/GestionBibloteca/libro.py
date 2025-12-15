from publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, titulo, año_publicacion, genero, copias, autor="Desconocido"):
        super().__init__(titulo, año_publicacion, genero, copias)
        self.__autor = autor

    def get_autor(self):
        return self.__autor
    
    