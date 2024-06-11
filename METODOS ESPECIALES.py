class CD:
    
    def __init__(self, autor, tirulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        
    def  __str__(self):
        return f"Albun : {self.titulo, }, de {self.autor}"
    
    def __len__(self):
        return self.canciones
    
mi_cd = CD("Pink Floyd", "The wall", 24)
print(str(mi_cd))
print(len(mi_cd))
