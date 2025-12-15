from smartphone import Smartphone
from tablet import Tablet


def main():
    # Crear diferentes dispositivos
    dispositivo1 = Smartphone("Samsung", "Galaxy S21", 800, 128)
    dispositivo2 = Tablet("Apple", "iPad Air", 600, 10.9)
    dispositivo3 = Smartphone("Xiaomi", "Redmi Note", 300, 64)

    # Lista para manejar todos los dispositivos
    inventario = [dispositivo1, dispositivo2, dispositivo3]

    # Completar operaciones requeridas:

    # 1. Mostrar información de cada dispositivo
    # Recorrer la lista 'inventario' y llamar al método mostrar_info() de cada dispositivo
    print("INFORMACIÓN INICIAL")
    for i in inventario:
        i.mostrar_info()
        print("-----------")

    # 2. Instalar aplicaciones en los smartphones
    # Usar el método instalar_app() en los objetos Smartphone
    # Instalar al menos 2 aplicaciones diferentes
    print("INSTALANDO APLICACIONES")
    for i in inventario:
        i.instalar_app("Whatsapp")
        i.instalar_app("Instagram")


    # 3. Cambiar estado de los dispositivos
    # Recorrer la lista y llamar al método encender() en cada dispositivo
    print("ENCENDIENDO DISPOSITIVOS")
    for i in inventario:
         i.encender()
    

    # 4. Mostrar información final después de los cambios
    # Volver a recorrer la lista y mostrar la información actualizada
    
    print("INFORMACIÓN FINAL")
    for i in inventario:
        i.mostrar_info()
        print("-----------")
    

if __name__ == "__main__":
    main()
