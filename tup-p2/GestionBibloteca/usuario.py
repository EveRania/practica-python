class Usurio:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__prestamos = []

    def get_nombre_completo(self):
        return f"{self.__apellido}-{self.__nombre}"
        
    def get_prestamos(self):
        return self.__prestamos
    
    def agregar_prestamo(self, publicacion):
        publicacion.prestar_copia()
        self.__prestamos.append(publicacion)

    def remover_prestamo(self, publicacion):
        if publicacion not in self.__prestamos:
            raise ValueError("El préstamo no está en la lista de préstamos del usuario.")
        publicacion.devolver_copia()
        self.__prestamos.remove(publicacion)

    def get_cant_publicaciones_genero(self, genero):
        return len([p for p in self.__prestamos if p.get_genero() == genero])