import requests
from abc import ABC, abstractclassmethod

class pokemon():
    def __init__(self,name):
        self.name=name

class Natpokedex(ABC):
    @abstractclassmethod
    def Search(num):
        pass


def getPokemon(num, api):
    poke=api.Search(num)
    return poke.name

class RegPokedex(Natpokedex):
    def __init__(self,base_url):
        self.base_url=base_url
    
    def Search(self,num):
        res=requests.get(f"{self.base_url}/{num}")
        json = res.json()
        return pokemon(json['name'])

if __name__=="__main__":
    poke = RegPokedex("https://pokeapi.co/api/v2/pokemon/")
    print(getPokemon("390",poke))