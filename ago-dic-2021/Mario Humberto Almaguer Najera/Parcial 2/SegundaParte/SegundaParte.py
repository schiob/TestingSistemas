from abc import ABC, abstractmethod

class Escritor(ABC):
    
    @abstractmethod
    def escribir(texto : str) -> str:
        return texto

class Implementacion(Escritor):

    def escribir(texto: str):
        texto = input('Inserta dos numeros separados por un espacio')
        arr = texto.split(' ')
        return str(int(arr[0]) + int(arr[1]))


class Cliente():
    imp = Implementacion()
    print(imp.escribir())

if __name__ == '__main__':
    c = Cliente()

