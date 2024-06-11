# class Persona:
#     def __init__(self, nombre, edad, sexo, nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.sexo = sexo
#         self.nacionalidad = nacionalidad
        
#     persona = Persona('Pilar','47','femenino', 'Colombiana')
    
    
class Auto:
    def __init__(self, marca, modelo, anio, color):
       self.marca = marca
       self.modelo = modelo
       self.anio= anio
       self.color = color
        
    def encendido(self):
        print(self.marca, self.modelo, self.anio, self.color +"el auto esta encendido")
                 
    def apagado(self):
        print(self.marca, self.modelo, self.anio, self.color +"el auto esta apagado")  
                
     mi_auto = Auto('CR30','PLUS','2024', 'Azul')
     
     
# class Auto:
#     def __init__(self, marca, modelo, anio, color):
#         self.marca = marca 
#         self.modelo = modelo
#         self.anio = anio
#         self.color = color
        
#     def estado(self):
#             print(f'Mi carro es un {carro.marca} {carro.modelo} del año {carro.anio} color {carro.color} y esta encendido')
            
        
# carro = Auto('Ford', 'Fiestas', 2018, 'gris' )
# carro.estado()


         
        
        