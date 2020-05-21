import pprint
import requests
import Card
import DBCreate


r = requests.get('https://db.ygoprodeck.com/api/v6/cardinfo.php')

results = r.json()


count = 0
Db = DBCreate.dataBase()
#Db.CreateDatabase()
#Db.CardTable()

#for i in range(0,len(results)):
    
#    Bdeck = Card.Card(results[i]['id'],results[i]['name'],results[i]['type'],results[i]['desc'],results[i]['card_prices'][0]['ebay_price'])
#    count+= 1
#    Db.insertarC(Bdeck)
    #print(Bdeck)

#print('xDXDXDDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXDXD')
#print(count)

if __name__ == "__main__":
    
    Db.Visualizar()