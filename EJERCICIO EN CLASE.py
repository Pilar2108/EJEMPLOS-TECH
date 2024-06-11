class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre =nombre
        self.edad = edad
        self.grado = grado
        
class Curso :
    def __init__(self,nombre, profesor):
        self.nombre =nombre
        self.profesor = profesor
        self.estudiantes= []
        
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)
        
    def mostrar_estudiante(self):
        for estudiante in self.estudiantes:
            print(f"Nombre estudiante {estudiante.nombre}")
            
estudiante1 = Estudiante("Juan", 15, "Noveno")
estudiante2 = Estudiante("Maria", 14, "Octavo")
    
curso1 = Curso("Matematicas Especiales","Julio Gonzalez")
curso1.agregar_estudiante(estudiante1)
curso1.agregar_estudiante(estudiante2)
curso1.mostrar_estudiante()
curso1.eliminar_estudiante(estudiante2)
curso1.mostrar_estudiante()