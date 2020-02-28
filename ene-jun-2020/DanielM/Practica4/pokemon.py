from abc import ABC, abstractclassmethod
import requests


class Pokemon:
    def __init__(self, name):
        self.naME = name


class Pokedex(ABC):
    @abstractclassmethod
    def search(id):
        pass


def get_pokemon(id, bibliotec):
    p = bibliotec.search(id)

    return p.naME


class Pokmn(Pokedex):
    def __init__(self, url_base):
        self.url = url_base

    def search(self, id):
        response = requests.get('{}/{}'.format(self.url, id))
        json = response.json()
        return Pokemon(json['name'])


if __name__ == "__main__":
    id = input('Hola, soy tu Pokedex! :v \nTeclea el ID del pokémon que deseas buscar:  ')
    pokemon = Pokmn('https://pokeapi.co/api/v2/pokemon')
    print('\nEl pokémon que pertenece a este ID es: ', get_pokemon(id, pokemon))
