class Cliente:
    
   def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
       
class Tienda:
    
   def __init__(self):
        self.clientes = []
        
   def agregar_clientes(self, cliente):
       self.clientes.append(cliente)
       
   def incrementar_puntos(self, nombre_cliente, puntos):
       for cliente in self.clientes:
           if cliente.nombre == nombre_cliente:
               cliente.puntos += puntos
               break
   def mostrar_info_clientes(self):
        for cliente in self.clientes:
            print(f"Nombre: {cliente.nombre}, Puntos {cliente.puntos}")
        
tienda = Tienda()
tienda.agregar_cliente(Cliente"Juan"))
tienda.agregar_cliente(Cliente("Maria")) 
tienda.agregar_cliente(Cliente("Laura")) 
tienda.incrementar_puntos("Juan, 100")
tienda.incrementar_puntos("Laura, 200")
tienda.mostrar_info_clientes()


           

        

      