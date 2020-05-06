from abc import ABC, abstractclassmethod
import requests

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


class ApiYugih(BiblioYugih):#Funcion de la clase que recibe como parametro la URL
    def __init__(self, url_base):
        self.url = url_base

    def Search(self, name):#Metodo para buscar el objeto por medio del nombre
        res = requests.get("{}name={}".format(self.url, name))#Request a la Api     res = https://db.ygoprodeck.com/api/v2/cardinfo.php?name=Dark%20Magician
        json = res.json()
        dato = json['data'][0]['desc']
        return Yugih(dato)


#if __name__ == "__main__":

def start():
    nom = input("Escriba el nombre de la carta que desea obtener su efecto o descripción: ")
    biblio = ApiYugih("https://db.ygoprodeck.com/api/v7/cardinfo.php?")
    print(getCard(nom, biblio))
