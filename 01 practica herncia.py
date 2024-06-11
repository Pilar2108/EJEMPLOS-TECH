# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad= edad

# class Alumno(Persona):
#     pass

# lupe= Alumno('lupita', 20)
# print(lupe.edad)


class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Alumno(Persona):
    pass

lupe = Alumno('Lupita', 20)
print(lupe.edad)