class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

class Empresa:
    def __init__(self):
        self.empleados = []
        
    def agregar_empleados(self, empleado):
        self.empleados.append(empleado)
        
        
    def calcular_salario_total(self):
      return sum(empleado.salario for empleado in self.empleados)
  
    def mostrar_inf_empleados(self):
       for empleado in self.empleados:
        print(f"nombre {empleado.nombre}, puesto {empleado.puesto}, salario {empleado.salario}") 

empresa = Empresa()

empresa.agregar_empleados(Empleado ("Juan", "Desarrollador", 3000))
empresa.agregar_empleados(Empleado ("Maria", "Diseñadora", 2500))

print("salario total de la empresa: ", empresa.calcular_salario_total())
empresa.mostrar_inf_empleados()
