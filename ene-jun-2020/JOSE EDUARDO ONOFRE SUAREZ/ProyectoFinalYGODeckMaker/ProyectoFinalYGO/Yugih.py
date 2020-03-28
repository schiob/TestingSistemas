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
    
    
   
def getDeck(name, bibliotec):
    baraja = bibliotec.Search(id)
        
    return baraja.name



class BiblioYugih(ABC):#Clase abstracta para que esta sea la interface 
    @abstractclassmethod
    def Search(id):
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






