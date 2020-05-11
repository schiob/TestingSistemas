
class Ingrediente:
    def __init__(self, nombre, UdM, KalXUnidad):
        self.nombre = nombre
        self.UdM = UdM
        self.KalXUnidad = KalXUnidad

class Platillo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = list()
    
    def addIngrediente(self, ingrediente, cantidad):
        for i, ing in enumerate(self.ingredientes):
            if ing["ingrediente"].nombre == ingrediente.nombre:
                self.ingredientes[i]["cantidad"] += cantidad
                return
        
        self.ingredientes.append({"ingrediente": ingrediente, "cantidad": cantidad})
