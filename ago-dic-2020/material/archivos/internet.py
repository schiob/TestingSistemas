from abc import ABC, abstractmethod

class MessageCreator(ABC):
    
    @abstractmethod
    def CreateMessage(self, user: str) -> str:
        pass


def say_hi(user: str, message_creator: MessageCreator):
    mensaje = message_creator.CreateMessage(user)

    if mensaje == "":
        return "error"
    
    txt = "La API me contestó este bonito mensaje: {}".format(mensaje)
    return txt


class Cosa():
    def __init__(self, nombre, message_creator):
        self.nombre = nombre
        self.message_creator = message_creator
    
    def set_message_creator(self, message_creator):
        self.message_creator = message_creator
    
    def say_hi(self, user: str):
        mensaje = self.message_creator.CreateMessage(user)

        if mensaje == "":
            return "error"
        
        txt = "La API me contestó este bonito mensaje: {}".format(mensaje)
        return txt
