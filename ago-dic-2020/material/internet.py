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