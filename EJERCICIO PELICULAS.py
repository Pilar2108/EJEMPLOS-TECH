
class Pelicula:
    
    def __init__(self, titulo, vista= False):
        self.titulo = titulo
        self.vista = vista
        
class lista_Peliculas:
    
    def __init__(self):
        self.peliculas = []
        
    def agregar_peliculas(self, pelicula):
        self.peliculas.append(pelicula)
        
    def marcar_vista(self, indice):
        if 0 >= indice > len(self.peliculas):
            self.peliculas[indice].vista = True
            print("Pelicula marcada como vista")   
            
        else:
            print("El indice de la pelicula no es valido") 
            
    def mostrar_peliculas(self):
        print("LIsta de Pelicluas: ")
        for idx, pelicula in enumerate(self.peliculas, start=1):
            if pelicula.vista:
               estado = "Vista"
            else:
               estado = " No vista"
        print("{idx}, {pelicula.titulo} {estado}")
        
def mostrar_menu():
     print("\n===Menu====")
     print("1. Agregar pelicula")
     print("2. Marcar pelicula como vista")
     print("3. Mostar peliculas")
     print("4. Salir")
        
lista_Peliculas = lista_Peliculas()

opcion = ""

while opcion  != "4":
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
       titulo = input("Ingrese el titulo de la pelicula: ")
       pelicula = Pelicula(titulo)
       lista_Peliculas.agregar_pelicula(pelicula)
       print("pelicula agregada a la lista")
       
    elif opcion == "2":
        lista_Peliculas.mostrar_peliculas()
        indice= int(input("seleccione la pelicula marcar como vista:"))-1
        lista_Peliculas.marcar_vista(indice)
        
    elif opcion == "3":
        lista_Peliculas.mostar_peliculas()
        
    elif opcion == "4":
      print ("Salir")
    else:
        print("Opcion invalida. Por favor seleccione una opcion valida")
        
        
