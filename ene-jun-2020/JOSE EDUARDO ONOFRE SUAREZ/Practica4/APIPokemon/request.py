import requests
from abc import ABC,abstractclassmethod
import pprint

class PoketMonsta():
    def __init__(self, name, types, weight):
        self.Name = name
        self.Types = types
        self.Weight = weight

class Pokedex(ABC): #Clase abstracta para funcionar como Interface
    @abstractclassmethod
    def Search(id):
        pass

def getPokimon(id, pokedx): #Metodo para obtener un dato en especifico/ El nombre
    pokimon = pokedx.Search(id)

    return pokimon.Name


class PokeApi(Pokedex):
    def __init__(self, url_base): #Funcion de la clase que recibe la URL de la API
        self.url = url_base # Set de la URL

    def Search(self, id): #Metodo para buscar en la API por medio del id
        res = requests.get("{}/{}".format(self.url, id)) #request a la API
        json = res.json() #Jason de regreso por la API
        return PoketMonsta(json['name'], json['types'], json['weight']) #El metodo nos regresa un objeto Tipo PoketMonsta con titulo,episodios y descripcion


if __name__ == "__main__":

    id = input("Escriba el id del Pokemon: ")
    pokemon = PokeApi("https://pokeapi.co/api/v2/pokemon")

    print(getPokimon(id,pokemon))