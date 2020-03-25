import requests
import pprint
from abc import ABC,abstractclassmethod


class Deck:
    
    def __init__(self,name,main,extra,side,price):

        self.Name = name
        self.Main = main
        self.Extra = extra
        self.Side = side
        self.Price = price
    
    

class SearchInDeck(ABC):
    @abstractclassmethod
    def SearchCardDeckById(id):
        pass

    @abstractclassmethod
    def SearchCardDeckByName(name):
        pass



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

class SearchCard(ABC):
    @abstractclassmethod
    def SearchCardById(id):
        pass
    

    @abstractclassmethod
    def SearchCardByName(name):
        pass

    #def SearchCardById(id):
    #    pass

    #def SearchCardByName(name):
    #    pass


    def ShowMyDecks():
        pass

    def BuildMainDeck():
        pass

    def BuildExtraDeck():
        pass

    def BuildSideDeck():
        pass

    def countCards():
        pass

    def DeckValue():
        pass
    

def RequestYGOAPI():

    result = request.get("https://db.ygoprodeck.com/api/v6/cardinfo.php")

    result = json()

    return result


if __name__ == "__main__":
    pass

