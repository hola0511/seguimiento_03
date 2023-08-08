class CuentaBancaria:
    def __init__(self, numero_cuenta: int, balance: float, propietario: str):
        self.numero_cuenta: int = numero_cuenta
        self.propietarios: str = propietario
        self.balance: float = balance
