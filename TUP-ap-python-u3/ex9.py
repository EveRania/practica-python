# 9) Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto, Editar contacto, Cerrar agenda.


class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        print("\n-- Añadir contacto--")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        nuevo = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo)
        print("Contacto agregado correctamente.\n")

    def listar_contactos(self):
        print("\n-- Lista de contactos --")
        if not self.contactos:
            print("No hay contactos cargados. \n")
        else:
            contador = 1
            for contacto in self.contactos:
                print(f"{contador}. {contacto}")
                contador += 1

    def buscar_contacto(self):
        print("\n -- Buscar contacto --")
        nombre = input("Ingrese el nombre a buscar: ")
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]

        if not encontrados:
            print("No se encontró ese contacto. \n")
        else:
            print("Contacto encontrado:")
            for c in encontrados:
                print(c)
            print()

    def editar_contacto(self):
        print("\n-- Editar contacto--")
        nombre = input("Ingrese el nombre del contacto a editar: ")
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                print(f"Editando: {c}")
                c.nombre = input("Nuevo nombre (enter para mantener): ") or c.nombre
                c.telefono = (
                    input("Nuevo teléfono (enter para mantener): ") or c.telefono
                )
                c.email = input("Nuevo email (enter para mantener): ") or c.email
                print("Contacto actualizado\n")
                return
        print("No se encontró ese contacto.\n")

    def menu(self):
        while True:
            print("----AGENDA----")
            print("1. Añadir contacto")
            print("2. Listar contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción inválida. \n")


# Programa principal
agenda = Agenda()
agenda.menu()
