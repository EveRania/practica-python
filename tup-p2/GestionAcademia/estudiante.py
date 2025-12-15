class Estudiante():
    def __init__(self, nombre, apellido, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_correo(self):
        return self.__correo