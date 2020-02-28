from abc import abstractclassmethod, ABC
import requests

class Pokymon():
    def __init__(self,name):
        self.name = name

class Bibliopokymon(ABC):
    @abstractclassmethod
    def Search(id):
        pass

def getPokymon(id, bibliotec):
    Pockymon = bibliotec.Search(id)

    return Pockymon.name

class pokeapi(Bibliopokymon):
    def __init__(self, url_base):
        self.url = url_base

def Search(self, id):
    res = requests.get("{}/{}".format(self.url,id))
    json = res.json()
    return Pokymon(json['name'])

if __name__ == '__main__':
    biblio = pokeapi("https://pokeapi.co/api/v2/pokemon")
    