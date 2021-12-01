from abc import *

class Escritor(metaclass=ABCMeta):
    @abstractclassmethod
    def escritor(self, datos: str):
        return datos