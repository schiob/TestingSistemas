from abc import ABC,abstractmethod
class Tweeti():
    def __init__(self,user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile,Ranking,Categoria,Victorias,Derrotas):
        self.user_id = user_id
        self.handle = handle
        self.lugar = lugar
        self.verificado = verificado
        self.followers = followers
        self.numtweets = numtweets
        self.friends = friends
        self.description = description
        self.lenguaje = lenguaje
        self.profile = profile
        self.Ranking = None
        self.Categoria = None
        self.Victorias = 0
        self.Derrotas = 0



class Abstracttweet(ABC):
    @abstractmethod
    def getUsuario(self,handle):
        pass
class Abstractbase(ABC):
    @abstractmethod
    def insert_db(self,Tweet):
        pass
    @abstractmethod
    def deleteUsuario(self,handle):
        pass
    @abstractmethod
    def updateUsuario():
        pass
    @abstractmethod
    def selectUsuario():
        pass
