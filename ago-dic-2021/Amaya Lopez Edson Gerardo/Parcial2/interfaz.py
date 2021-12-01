from abc import abstractmethod
from abc import ABCMeta
class Escritor(metaclass=ABCMeta):
    @abstractmethod
    def escribir(self,parametro:str)->int:
        pass
