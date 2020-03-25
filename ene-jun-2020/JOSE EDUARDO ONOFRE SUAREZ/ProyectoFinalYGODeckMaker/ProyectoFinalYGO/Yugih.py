import requests
import pprint
from abc import ABC,abstractclassmethod


#class Deck:
#   def __init__(self,name,main,extra,side,price):
#
 #       self.Name = name
  #      self.Main = main
   #     self.Extra = extra
    #    self.Side = side
     #   self.Price = price
    
    

class SearchInDeck(ABC):
    @abstractclassmethod
    def Search(id):
        pass

   
def getDeck(name, bibliotec):
    baraja = bibliotec.Search(id)
        
    return baraja.name



class Card:
    def __init__(self, id, name, types, desc, atk, defs,level, race, attribute, price):

        self.Id = id
        self.Name = name
        self.Type = types
        self.Desc = desc
        self.Atk = atk
        self.Def = defs
        self.Level = level
        self.Race = race
        self.Attribute = attribute
        self.Price = price

class BiblioYugih(ABC):#Clase abstracta para que esta sea la interface 
    @abstractclassmethod
    def Search(id):
        pass

def getCard(id, bibliotec):# Metodo para obtener el nombre o algo en especifico 
    yugih = bibliotec.Search(id)

    return yugih.name


def ShowMyDecks():
        pass


class Deck(object):
    def __init__(self, main_deck):
        self.main_deck = main_deck

    def add_normal_cards(self, card_to_add, all_cards):
        "Agrega monstruos, hechizos y trampas al deck"
        "La función len() devuelve la longitud de una cadena de caracteres o el número de elementos de una lista."
        
        if len(self.main_deck) > 60:
            return "Tienes mas cartas de las permitidas en tu Deck (60)."
        else:
            contador_cartas = 0
            # Verifica cuántas copias de una carta hay en tu mazo. Puedes tener máximo 3 de la misma tarjeta. Tarjetas limitadas,
            # se agregaran.
            for card in self.main_deck:
                if card == card_to_add:
                    contador_cartas += 1
            if contador_cartas == 3:
                return "Tienes muchas copias de esa carta en tu deck (3)"
            else:
                if card_to_add not in all_cards:
                    return "Esa carta aún no se ha agregado al juego  (" + card_to_add + ")."
                else:
                    self.main_deck.append(card_to_add)

def BuildExtraDeck(self, card_to_add, all_cards):
        "Agrega monstruos, hechizos y trampas al deck"
        
        if len(self.main_deck) > 15:
            return "Tienes mas cartas de lo permitido en tu extra deck (15)."
        else:
            contador_carta = 0
            # Verifica cuántas copias de una carta hay en tu mazo. Puedes tener máximo 3 de la misma tarjeta. Tarjetas limitadas,
            # se agregaran.
            for card in self.main_deck:
                if card == card_to_add:
                    contador_carta += 1
            if contador_carta == 3:
                return "Tienes muchas copias de esa carta en tu deck (3)."
            else:
                if card_to_add not in all_cards:
                    return "Esa carta aún no se ha agregado al juego (" + card_to_add + ")."
                else:
                    self.main_deck.append(card_to_add)

def BuildSideDeck():
        pass

def countCards():
        contador=0

def DeckValue():
        pass
    


class ApiYugihCard(BiblioYugih):#Funcion de la clase que recibe como parametro la URL, para buscar una carta
    def __init__(self, url_base):
        self.url = url_base

def RequestYGOAPICard():
    res = requests.get("{}/{}".format(self.url, id))#Request a la Api
    json = res.json()
    return Card(json['name'],json['atk'])



class ApiYugihDeck(SearchInDeck):#Funcion de la clase que recibe como parametro la URL, para buscar un deck
    def __init__(self, url_base):
        self.url = url_base

def RequestYGOAPIDeck():
    res = requests.get("{}/{}".format(self.url, id))#Request a la Api
    json = res.json()
    return Deck(json['name'],json['main'])



if __name__ == "__main__":
    biblio = ApiYugihCard("https://db.ygoprodeck.com/api/v6/cardinfo.php")
    print(getcard("34541863", biblio))
    biblio2 = ApiYugihDeck("https://db.ygoprodeck.com/api/v6/cardinfo.php")
    print(getDeck("12340",biblio2))






