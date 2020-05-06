import unittest
from APIRequest import getCard, Yugih, BiblioYugih

class YugiMock(BiblioYugih): #La clase Mock va a implementar la interface de la App

    def cardata(self, efecto):  #Manipulamos la info manualmente sin necesidad de la API

        self.card = Yugih("")
    
    def Search(self,nombre):    #Buscamos la info en la clase del Mock y no en la función Original
        return self.card


class TestRequest(unittest.TestCase):

    def test_card(self):
        card_test = (
            
            

        )