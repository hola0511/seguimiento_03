class CuentaBancaria:
    def __init__(self, numero_cuenta: int, propietario: str, balance: float):
        self.numero_cuenta: int = numero_cuenta
        self.propietario: str = propietario
        self.balance: float = balance

    def depositar(self, dinero: int):
        self.balance = dinero + self.balance
        return self.balance

    def retirar(self, dinero: int):
        self.balance = self.balance - dinero
        return self.balance

    def cuota_manejo(self):
        cuota_manejo = 0.02 ** self.balance
        print(cuota_manejo)

    def detalles_cuenta(self):
        print(self.numero_cuenta)
        print(self.propietario)
        print(self.balance)


e1 = CuentaBancaria(1, "carlos", 15000)

print(e1.balance)
print(e1.propietario)
print(e1.numero_cuenta)

e1.depositar(15000)
print(e1.balance)

e1.retirar(10000)
print(e1.balance)

e1.cuota_manejo

e1.detalles_cuenta()
