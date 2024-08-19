import json

class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("El monto del depósito debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("El monto del retiro no es válido o excede el saldo disponible.")

    def consultar_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Cuenta: {self.numero_cuenta}, Titular: {self.titular}, Saldo: {self.saldo}"
    
class CuentaBancariaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0.0, sobregiro_permitido=0.0):
        super().__init__(numero_cuenta, titular, saldo)
        self.sobregiro_permitido = sobregiro_permitido

    def retirar(self, monto):
        if monto <= self.saldo + self.sobregiro_permitido:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("El monto del retiro excede el saldo y el sobregiro permitido.")

    def __str__(self):
        return f"Cuenta Corriente: {self.numero_cuenta}, Titular: {self.titular}, Saldo: {self.saldo}, Sobregiro Permitido: {self.sobregiro_permitido}"
    
class CuentaBancariaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0.0, tasa_interes=0.01):
        super().__init__(numero_cuenta, titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa_interes
        print(f"Interés aplicado. Nuevo saldo: {self.saldo}")

    def __str__(self):
        return f"Cuenta de Ahorro: {self.numero_cuenta}, Titular: {self.titular}, Saldo: {self.saldo}, Tasa de Interés: {self.tasa_interes}"
    
class Banco:
    def __init__(self):
        self.cuentas = []

    def crear_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"Cuenta creada: {cuenta}")

    def leer_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        raise ValueError("Cuenta no encontrada")


    def actualizar_cuenta(self, numero_cuenta, titular=None, saldo=None):
        cuenta = self.leer_cuenta(numero_cuenta)
        if cuenta:
            if titular is not None:
                cuenta.titular = titular
            if saldo is not None:
                cuenta.saldo = saldo
            print(f"Cuenta actualizada: {cuenta}")
        else:
            print("Cuenta no encontrada.")

    def eliminar_cuenta(self, numero_cuenta):
        cuenta = self.leer_cuenta(numero_cuenta)
        if cuenta:
            self.cuentas.remove(cuenta)
            print(f"Cuenta eliminada: {cuenta}")
        else:
            print("Cuenta no encontrada.")

    def listar_cuentas(self):
        for cuenta in self.cuentas:
            print(cuenta)