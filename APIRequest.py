from abc import ABC, abstractclassmethod
import requests
from DBCreate import dataBase
import DBCreate

class Yugih():#Constructor de la clase
    def __init__(self,desc):

        self.Desc = desc


class BiblioYugih(ABC):#Clase abstracta para que esta sea la interface 
    @abstractclassmethod
    def Search(name):
        pass



def getCard(name, biblio):# Metodo para obtener el nombre o algo en especifico 
    yugih = biblio.Search(name)

    return yugih.Desc

def getAllCards(): # Metodo para obtener todas las cartas desde la BD
    
    AllCards = DBCreate.dataBase()
    AllCards.CreateDatabase()
    elementos = AllCards.Visualizar()
    print("ACTUALMENTE EXISTEN {} CARTAS EN LA BASE DE DATOS".format(elementos))
    return elementos

class ApiYugih(BiblioYugih):#Funcion de la clase que recibe como parametro la URL
    def __init__(self, url_base):
        self.url = url_base

    def Search(self, name):#Metodo para buscar el objeto por medio del nombre
        res = requests.get("{}name={}".format(self.url, name))#Request a la Api     res = https://db.ygoprodeck.com/api/v2/cardinfo.php?name=Dark%20Magician
        json = res.json()
        dato = json['data'][0]['desc']
        return Yugih(dato)
    
    def SaveCardstoBD(self, url_base):

        for i in range(0,len(results)):
    
            Bdeck = Card.Card(results[i]['id'],results[i]['name'],results[i]['type'],results[i]['desc'],results[i]['card_prices'][0]['ebay_price'])
            count+= 1
            Db.insertarC(Bdeck)
            print(Bdeck)




#if __name__ == "__main__":

def start(): ##Funcion que se manda a llamar desde el Index para ejecutar la busqueda del efecto de una carta
    nom = input("Escriba el nombre de la carta que desea obtener su efecto o descripción: ")
    biblio = ApiYugih("https://db.ygoprodeck.com/api/v7/cardinfo.php?")
    print(getCard(nom, biblio))
