from abc import ABC, abstractclassmethod
import requests

class Pokemon():#Constructor de la clase
    def __init__(self,name,weight):
        self.Name = name
        self.Weight = weight
    
    

class BiblioPoke(ABC):#Clase abstracta para que esta sea la interface 
    @abstractclassmethod
    def Search(id):
        pass

def getPoke(id, bibliotec):# Metodo para obtener el nombre o algo en especifico 
    poke = bibliotec.Search(id)

    return poke.Name              


class ApiPoke(BiblioPoke):#Funcion de la clase que recibe como parametro la URL
    def __init__(self, url_base):
        self.url = url_base

    def Search(self, id):#Metodo para buscar el objeto por medio el ID
        res = requests.get("{}/{}".format(self.url, id))#Request a la Api
        json = res.json()
        return Pokemon(json['name'],json['weight'])

if __name__ == "__main__":
    biblio = ApiPoke("https://pokeapi.co/api/v2/pokemon")
    print(getPoke("25", biblio))