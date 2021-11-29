from abc import abstractmethod
from abc import ABCMeta
class Escritor(metaclass=ABCMeta):
    @abstractmethod
    def Escribir(self,parametro:str)->int:
        pass

class Escribir(Escritor):
    def cantidad_letras(parametro:str):
        alfabeto=0
        for letra in parametro:
            if letra.lower() in"abcdefghijklmnopqrstuvwxyz":
                alfabeto +=1
        return str(alfabeto)

if __name__ == '__main__':
    dato = input('Escribe lo que quieras contare sus letras mas rapido que Rayo Mcqueen:')
    print(Escribir.cantidad_letras(dato))