class cuentaBancaria:
    def __init__(self, saldoInicial = 0): #__init__ constructor de la clase, inicializa el saldo de la cuenta.
        self.saldo = saldoInicial
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo
    
    def retirar(self, cantidad):
       if self.saldo >= cantidad:
           self.saldo -= cantidad
           return self.saldo
       else:
           print("Saldo insuficiente")
           return self.saldo
    def consultar_saldo(self):
        return self.saldo
    
mi_cuenta = cuentaBancaria(1000)

mi_cuenta.depositar(500)

mi_cuenta.retirar(200)

saldo_actual = mi_cuenta.consultar_saldo()

print(f"El saldo actual es: {saldo_actual}")


