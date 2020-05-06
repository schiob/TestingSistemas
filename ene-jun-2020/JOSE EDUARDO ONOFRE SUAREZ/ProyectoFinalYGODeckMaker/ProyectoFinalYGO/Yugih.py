import requests
import pprint
import DataBaseYGO
import BDYGOInterface
from abc import ABC,abstractclassmethod
    



class BiblioYugih(ABC):#Clase abstracta para que esta sea la interface 
    @abstractclassmethod
    def Search(name):
        pass



class ApiYugihCard(BiblioYugih):#Funcion de la clase que recibe como parametro la URL, para buscar una carta
    def __init__(self, url_base):
        self.url = url_base

def RequestYGOAPICard():
    res = requests.get("{}/{}".format(self.url, id))#Request a la Api
    json = res.json()

    count = 0

    for i in range(0,len(results)):
    
        #Bdeck = Card(results[i]['id'],results[i]['name'],results[i]['type'],results[i]['desc'],results[i]['atk'],results[i]['def'],results[i]['level'],results[i]['race'],results[i]['attribute'])
        Bdeck = Card.Card(results[i]['id'],results[i]['name'],results[i]['type'],results[i]['desc'],results[i]['card_prices'][0]['ebay_price'])
        #print(results[i]['name'])
        count+= 1
        print(Bdeck)


    #return Card(json['name'],json['atk'])


class ApiYugihDeck():#Funcion de la clase que recibe como parametro la URL, para buscar un deck
    def __init__(self, url_base):
        self.url = url_base

def RequestYGOAPIDeck():
    res = requests.get("{}/{}".format(self.url, id))#Request a la Api
    json = res.json()
    
    return Deck(json['name'],json['main'])



if __name__ == "__main__":
    
    biblio = ApiYugihCard("https://db.ygoprodeck.com/api/v6/cardinfo.php")







