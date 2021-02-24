from abc import ABC

class Entrada(ABC):
    def pedir_entrada(self) -> str:
        pass

class EntradaTerminal(Entrada):
    def pedir_entrada(self) -> str:
        return input("dame la entrada: ")
    
class EntradaArchivo(Entrada):
    def __init__(self, file_name: str):
        self.file_name = file_name

    def pedir_entrada(self) -> str:
        with open(self.file_name, "r") as f:
            return f.read()

def sumar_algo(n: int, mi_entrada: Entrada):
    val = int(mi_entrada.pedir_entrada())

    return n + val

if __name__ == "__main__":
    mi_entradita_terminal = EntradaTerminal()
    print(sumar_algo(42, mi_entradita_terminal))