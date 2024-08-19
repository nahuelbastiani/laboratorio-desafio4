from laboratorio_poo import (
  CuentaBancaria,
  CuentaBancariaAhorro,
  CuentaBancariaCorriente,
  Banco,
)

import time

def con_menu():
    # Crear una instancia del banco
    banco = Banco()

    while True:
        print("Ingrese una opcion")
        print("1 - Crear una cuenta corriente")
        print("2 - Crear una cuenta de ahorro")
        print("3 - Listar cuentas")

        opcion = input()

        if opcion== "":
            print("adiosito")
            time.sleep(3)
            print("chau")
            break

        if opcion == "1":
            print("Ingrese numero de cuenta:")
            nro_cuenta=input()
            print("Ingrese nombre y apellido del titular:")
            titular=input()
            print("Ingrese sobregiro permitido:")
            sobregiro_permitido=input()
            cc=  CuentaBancariaCorriente(numero_cuenta=nro_cuenta, titular=titular, sobregiro_permitido=int(sobregiro_permitido))
            banco.crear_cuenta(cc)

        if opcion == "2":
            print("Ingrese numero de cuenta:")
            nro_cuenta=input()
            print("Ingrese nombre y apellido del titular:")
            titular=input()
            print("Ingrese saldo inicial:")
            saldo_inicial=input()
            saldo_inicial_calculado=float(saldo_inicial)*0.01+float(saldo_inicial)
            cc= CuentaBancariaAhorro(numero_cuenta=nro_cuenta, titular=titular, saldo=saldo_inicial_calculado)


            banco.crear_cuenta(cc)
        elif opcion == "3":
            print("\nLista de cuentas bancarias:")
            banco.listar_cuentas()

def main():
    # Crear una instancia del banco
    banco = Banco()

    # Crear cuentas bancarias
    cuenta_corriente = CuentaBancariaCorriente(numero_cuenta="87654321", titular="Ana Gómez", sobregiro_permitido=500)
    cuenta_ahorro = CuentaBancariaAhorro(numero_cuenta="11223344", titular="Luis Rodríguez", tasa_interes=0.05)

    # Agregar cuentas al banco
    banco.crear_cuenta(cuenta_corriente)
    banco.crear_cuenta(cuenta_ahorro)

    # Leer y mostrar una cuenta bancaria
    cuenta = banco.leer_cuenta("87654321")
    if cuenta:
        print(f"Cuenta leída: {cuenta}")

    # Actualizar saldo de una cuenta
    banco.actualizar_cuenta("87654321", saldo=1500)

    # Listar todas las cuentas del banco
    print("\nLista de cuentas bancarias:")
    banco.listar_cuentas()

    # Aplicar interés a la cuenta de ahorro
    print("\nAplicando interés a la cuenta de ahorro:")
    cuenta_ahorro.aplicar_interes()
    
    # Listar cuentas después de aplicar interés
    banco.listar_cuentas()

    # Eliminar una cuenta bancaria
    print("\nEliminando cuenta de ahorro:")
    banco.eliminar_cuenta("11223344")

    # Listar cuentas después de eliminar una cuenta
    print("\nLista de cuentas bancarias después de eliminar una cuenta:")
    banco.listar_cuentas()

if __name__ == "__main__":
    #main()
    con_menu()