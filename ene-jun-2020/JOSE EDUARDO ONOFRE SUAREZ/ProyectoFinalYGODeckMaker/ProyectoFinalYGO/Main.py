import requests
from abc import ABC, abstractclassmethod
import DBCreate

class ApiYugiCard():

    def __init__(self, url_base):
        self._url = url_base
    

    def RequestYGOAPICard():
        res = requests.get("{}".format(self.url))#Request a la Api
        results = res.json()

        count = 0

        for i in range(0,len(results)):
    
            Bdeck = Card.Card(results[i]['id'],results[i]['name'],results[i]['type'],results[i]['desc'],results[i]['card_prices'][0]['ebay_price'])
        
            count+= 1
            print(Bdeck)
        



if __name__ == "__main__":

    Api = ApiYugiCard("https://db.ygoprodeck.com/api/v6/cardinfo.php")


