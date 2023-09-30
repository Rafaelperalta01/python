class CuentaBancaria:

    print("Bienvenido, ingrese un numero para realizar una operacion")
    print("1: Consultar saldo")
    print("2: Depositar")
    print("3: Extraer")
    print("0: Salir")
saldo = 0

while True:
    numero = int(input("Ingresa un número: "))
    if (numero == 1):
        print("Su saldo actual es de: " , saldo)
    if (numero == 2):
        deposito = int(input("Ingrese cantidad a depositar "))
        saldo += deposito
    if(numero == 3):
        extraer = int(input("Ingrese cantidad a extrar "))
        if (saldo >= extraer):
            saldo -= extraer
        else:
            print("Saldo insuficiente")
    if numero == 0:
        print("¿Esta seguro que desea salir?")
        comprobar = int(input("Presione 0 para salir, digite cualquier numero para continuar "))
        if(comprobar == 0):
         break




