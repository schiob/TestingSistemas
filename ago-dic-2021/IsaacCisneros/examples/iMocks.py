from abc import ABC, abstractmethod


# --------------Interfaz-----------------

class Entrada(ABC):

    @abstractmethod
    def Leer(Self) -> str:
        pass


# --------------Implementación----------

class Terminal(Entrada):
    def Leer(self) -> str:
        return input()

# --------------Implementción 2----------

class FIle(Entrada):
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
    
    def Leer(self) -> str:
        f= open(self.nombre_archivo,"r")
        body = f.read()
        f.close()
        return body


# -------------Unidad------------------

def isPositive(entrada: Entrada) -> bool:
    n= int()
    if n < 0:
        return False
    return True

if __name__ == "__main__":
    mi_term = Terminal()
    mi_file = File("archivito.txt")
    print(isPositive(mi_file))
