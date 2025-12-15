from dispositivo import Dispositivo
# Smartphone:

# * Capacidad de almacenamiento en GB
# * Capacidad de instalar aplicaciones
# * Información debe incluir cantidad de apps instaladas


class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, precio, almacenamiento):
        super().__init__(marca, modelo, precio)
        self.almacenamiento = almacenamiento
        self.apps = []

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de almacenamiento: {self.almacenamiento} GB")
        print(f"Aplicaciones instaladas: {len(self.apps)}")

    def instalar_app(self, app):
       
        self.apps.append(app)
        print(f"Aplicación {app} instalada")


