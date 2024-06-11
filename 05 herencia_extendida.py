class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer (self):
        print("Este animal ha nacido")
    
    def hablar (self):
        FileExistsError
        print("Este animal genera algun sonido")
        
    class Pajaro(Animal):
        
        def __init__(self, edad, color, altura_vuelo):
             super().__init__(edad,color)
             self.altuta_vuelo = altura_vuelo
             
     def hablar (self):
        print("pio")     
        
     def volar (self, metros):
        print(f"El pajaro vuela {metros} metros") 
    
piolin= Pajaro(2, 'amarillo', 20) 

     
piolin.hablar()     
piolin.volar()  

             

