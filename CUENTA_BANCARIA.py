class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"Cliente: {self.nombre}, {self.apellido}n Balance de cuenta {self.numero_cuenta}: ${self.ba
    
    def depositar(self.monto_deposito):
     if self.balance += monto_deposito
     print("Deposito aceptado")
     
        
    def retirar(self.monto_retiro):
     self.balance >= monto_retiro
       self.blance -= monto_retiro
     print("Retiro realizado")
     
     else
     
     print("Fondos insuficientes")
     
          
     def crear:cliente()
     nombre_c1 = imput("ingrese su nombre:")
     apellido_c1 = imput("ingrese su apellio:")
     cuenta_c1 = imput("ingrese su cuenta:")
     nombre_c1 = imput("ingrese su nombre:")
     
     
     
     
     def inicio():
     mi_cliente = crear_cliente()
     print(mi_cliente)
     opcion = 0
     
     while opcion != 'S':
      print("Elije: Depositar (D), Retirar (R), Salir (S) ")
      opcion = imput()
      
      if opcion == "D":
        monto_dep = int(imput ("Monto a depositar"))
         mi_cleinte.depositar(monto_dep)
      elif opcion == "R":
       monto_ret == int(imput ("Monto a retirar"))
       mi_cliente.retirar(monto_ret)
       print(mi_cliente)
    
    print("Gracias por opera en nuestro Banco")