from abc import ABC,abstractclassmethod
import requests

class Pokymon():
    def __init__(self,name):
        self.name = name

class Bibliopokymon(ABC):
    @abstractclassmethod
    def Search(id):
        pass

def getPokymon(id, Bibliotec):
    Pokymon = Bibliotec.Search(id)
    return Pokymon.name

class pokeapi(Bibliopokymon):
    def __init__(self, url_base):
        self.url = url_base

    def Search(self, id):
        res = requests.get(f"{self.url}/{id}")
        json = res.json()
        return Pokymon(json['name'])

if __name__ == '__main__':
    biblio = pokeapi("https://pokeapi.co/api/v2/pokemon/")
    print(getPokymon("390", biblio))
    