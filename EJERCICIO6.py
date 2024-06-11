class Producto:
   
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Venta:
   
   def __init__(self):
     self.productos_vendidos= []
    
def agregar_productos(self, productos):
    self.productos_vendidos.append(producto)   

def calcular_total_venta(self):
   return sum(producto.precio * producto.cantidad for producto in self.productos_vendidos)

# def calcular_total_venta2(self):
#     total= 0
#     for producto in self productos_vendidos:
#         total += precio * producto,cantidad 
#     return total
   
venta = Venta()
venta.agregar_productos(Producto("camisa", 20000, 2))
venta.agregar_productos(Producto("pantalon", 50000, 1))
print("total de venta", venta.calcular_total_venta())


    


