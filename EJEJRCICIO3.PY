class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
       
    def presentarse(self):
        print(f"hola, me llamo {self.nombre} y tengo {self.edad} años")
    
persona =Persona('Pilar', 47)
persona.presentarse()
                  
class Profesor(Persona):

     def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre,edad)
        self.especialidad = especialidad
             
     def ensenar(self):
      print(f"El Profesor {self.nombre} esta enseñando {self.especialidad}")
    
profesor= Profesor("Pilar", 47, "Ingenieria")
profesor.presentarse()
profesor.ensenar()
     
    
     
