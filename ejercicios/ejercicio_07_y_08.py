class CuentaBancaria:
    def __init__(self, numero_cuenta: int, propietario: str, balance: float):
        self.numero_cuenta: int = numero_cuenta
        self.propietario: str = propietario
        self.balance: float = balance

    def depositar(self, dinero: int, balance: float):
        self.balance = dinero + self.balance
        return self.balance


e1 = CuentaBancaria(1, "carlos", 15000)

print(e1.balance)
print(e1.propietario)
print(e1.numero_cuenta)

e1.depositar(15000, e1.balance)
print(e1.balance)

