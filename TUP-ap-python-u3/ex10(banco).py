# 10) En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.


class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if monto <= self.cantidad:
            self.cantidad -= monto
        else:
            print("f{self.nombre} no tiene saldo suficiente.")

    def mostrar_total(self):
        print(f"{self.nombre} tiene $ {self.cantidad}")


class Banco:
    # init,
    def __init__(self):
        # 3 objetos de la clase cliente
        self.cliente1 = Cliente("German", 0)
        self.cliente2 = Cliente("Damian", 0)
        self.cliente3 = Cliente("Wanda", 0)

    # métodos: operar, deposito total
    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(4000)
        self.cliente3.depositar(1500)
        self.cliente1.extraer(300)

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad

        print(f"Total depositado en el banco: ${total}")


# Programa principal

banco = Banco()
banco.operar()
banco.cliente1.mostrar_total()
banco.cliente2.mostrar_total()
banco.cliente3.mostrar_total()
banco.deposito_total()
