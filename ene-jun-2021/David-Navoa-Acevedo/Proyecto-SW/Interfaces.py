from abc import ABC, abstractclassmethod

class Mostrar_detalles_del_mob(ABC):

    @abstractclassmethod
    def mostrarMob(self, mob: Mobs) -> :
        pass
class Modificaciones_de_mobs(ABC):
    @abstractclassmethod
    def guardarMob (self, mob: Mobs) -> bool:
        pass 
    @abstractclassmethod
    def cambiarRunas (self, mob: Mobs, runas_a_cambiar: runas) ->bool:
        pass 
    @abstractclassmethod
    def cambiarElemento (self, mob: Mobs, elemento: elemento) -> bool:
        pass 
    @abstractclassmethod
    def cambiarStats (self, mob: Mobs) -> bool:
        pass 
    @abstractclassmethod
    def modificarSkills (self, mob: Mobs) -> bool:
        pass 
    @abstractclassmethod
    def borrarMob (self, mob: Mobs) -> bool:
        pass 
    