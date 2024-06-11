class Estudiante:
    def __init__(self, id, nombre, edad, grado):
        self.id = id
        self.nombre =nombre
        self.edad = edad
        self.grado = grado
class Curso:
    
  def __init__(self, nombre, profesor):
       self.nombre =nombre
       self.profesor = profesor
       self.estudiantes= []
       self.next.id= 1
       
  def agregar_estudiante(self, estudiante):
      estudiante.id = self.next.id
      self.estudiante.id += 1
      self.estudiantes.append(estudiante)
      
def eliminar_estudiantes(sel, estudiante_id):
    for estudiante in self.estudiantes:
        if estudiante.id == estudiante_id:
          self.estudiantes.remove(estudiante)
          print("Estudiante eliminado del curso")
          return
    print("No se encontro estudiante con ese ID")
    
def mostar_estudiantes(self):
        print("Estudiantes en el curso de", self.nombre)
        for estudiante in self.estudiantes:
            print("ID:", estudiante.id, "| Nombre:" , estudiante.nombre)
            
def mostrar_menu():
   print("1. Agregar estudiante al curso")
   print("2. Eliminar estudiante del curso por ID")
   print("3. Mostarr estudiante al curso")
   print("4. Salir")


curso1 = Curso("Matematicas Especiales", "Jairo Guzman")
opcion = ""
while opcion != "4":
  print("\n ===Mwenu===")
  mostrar_menu()
  opcion = input("Selecciona una opcion")

if opcion == "1":
  nombre = input("Ingrese el nombre del estudiante: ")
  nombre = input("Ingrese el nombre del estudiante: ")
  edad = input("Ingrese la edad del estudiante: ")  
  estudiante = Estudiante(None, nombre, edad, grado)
  curso1.agregar_estudiante(estudiante)
  print("Estudiante agregado al curso")

elif opcion == "2":
      estudiante_id = int(input("Ingrese el ID del estudiante a eliminar: "))
      curso1.eliminar_estudiantes(estudiante_id)
        
elif opcion == "3":
       curso1.mostrar_estudiantes() 
         
elif opcion == "4":
    print("Saliendo del programa....")
        
else:
    print("Opcion invalida. Por favor, selecciones una opcion valida")

 
 
 
 
 
 
 
 
 


# class Estudiante:
#     def __init__(self, id, nombre, edad, grado):
#         self.id = id
#         self.nombre = nombre
#         self.edad = edad
#         self.grado = grado
# class Curso:
    
#     def __init__(self, nombre, profesor):
#         self.nombre = nombre
#         self.profesor = profesor
#         self.estudiantes = []
#         self.next_id = 1
        
#     def agregar_estudiante(self, estudiante):
#         estudiante.id = self.next_id
#         self.next_id += 1
#         self.estudiantes.append(estudiante)
        
#     def eliminar_estudiantes(self, estudiante_id):
#         for estudiante in self.estudiantes:    
#             if estudiante.id == estudiante_id:
#                 self.estudiantes.remove(estudiante)
#                 print("Estudiante eliminado del curso")
#                 return
#         print("No se encontro ningun estudiante con ese ID")
        
#     def mostrar_estudiantes(self):
#         print("Estudiantes en el curso de ", self.nombre) 
#         for estudiante in self.estudiantes:
#             print("ID:", estudiante.id, "| Nombre: ", estudiante.nombre)
# def mostrar_menu():
#     print("1. Agregar estudiante al curso")
#     print("2. Eliminar estudiante del curso por ID")
#     print("3. Mostrar estudiantes del curso")
#     print("4. Salir")
    
    
    
# curso1 = Curso("Matematicas Especiales", "Jairo Guzman") 
# opcion = ""
# while opcion != "4":
#     print("\n===Menu===")
#     mostrar_menu()
#     opcion = input("Seleccione una opcion: ")
    
#     if opcion == "1":
#       nombre = input("Ingrese el nombre del estudiante: ")
#       edad = input("Ingrese la edad del estudiante: ") 
#       grado = input("Ingrese el grado del estudiante: ")
#       estudiante = Estudiante(None, nombre, edad, grado) 
#       curso1.agregar_estudiante(estudiante)
#       print("Estuante agregado al curso")
    
#     elif opcion == "2":
#         estudiante_id = int(input("Ingrese el ID del estudiante a eliminar: "))
#         curso1.eliminar_estudiantes(estudiante_id)
        
#     elif opcion == "3":
#         curso1.mostrar_estudiantes() 
        
#     elif opcion == "4":
#         print("Saliendo del programa....")
        
#     else:
#         print("Opcion invalida. Por favor, selecciones una opcion valida")






        
