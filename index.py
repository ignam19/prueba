class Auto():
    def __init__(self, puertas, color, modelo):
        self.puertas = puertas
        self.color = color
        self.modelo = modelo
        self.marcha = False 
        
    def arrancar(self):
        if self.marcha == False:
            self.marcha = True
            
            
    def detener(self):
        if self.marcha == True:
            self.marcha == False
            
            
    def estado(self):
        if self.marcha == True:
            print("El auto esta en marcha")
        else:
            print("El auto esta parado")    
        
auto1 = Auto(4, "Rojo", "Hilux")
auto1.estado()
            
        
        
        
    