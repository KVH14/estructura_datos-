class CuentaBancaria:
    def __init__(self, titular: str, saldo: float, numerocuenta: str):
        self.titular = titular
        self.saldo = saldo
        self.numeroDeCuenta = numerocuenta

    def depositar(self, cantidad: float):
        self.saldo += cantidad
        print("")
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad: float):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

    def consultarSaldo(self):
        print(f"Saldo actual: {self.saldo}")


titular = input("Ingrese el nombre del titular: ")
print("")
saldo = float(input("Ingrese el saldo inicial: "))
print("")
numeroDeCuenta = input("Ingrese el número de cuenta: ")
print("")

cuenta = CuentaBancaria(titular, saldo, numeroDeCuenta)
cuenta.consultarSaldo()

deposito = float(input("Ingrese la cantidad a depositar: "))
print("")
cuenta.depositar(deposito)

retiro = float(input("Ingrese la cantidad a retirar: "))
print("")
cuenta.retirar(retiro)



   


