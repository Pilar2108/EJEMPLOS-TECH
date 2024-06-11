class cuenta: 
    
    def __init__(self, titular, saldo = 0):
       self.titular = titular
       self.saldo = saldo 
       
    def realizar_retiros(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("El retiro fue exitoso. Saldo restante: ", self.saldo)
        else:
            print("Fondos insuficientes")

class Banco:
    
    def __init__(self,  agregar_cuenta, eliminar_cuenta, mostrar_cuentas):
        self.agregar_cuenta = agregar_cuenta
        self.elimar_cuenta = eliminar_cuenta
        self.mostrar_cuentas = mostrar_cuentas
        
      
class ListaCuentas:
    
    def __init__(self):
        self.cuentas = []
