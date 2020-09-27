from random import choice
from internet import MessageCreator

class MiRandomGenerator(MessageCreator):
    def CreateMessage(self, persona: str) -> str:
        abc = "abcdefghijklmnñopqrstuvwxyz"

        txt = persona
        for _ in range(30):
            txt += choice(abc)
        
        return txt