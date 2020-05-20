import unittest
from APIRequest import getCard, Yugih, BiblioYugih

class YugiMock(BiblioYugih): #La clase Mock va a implementar la interface de la App

    def cardata(self, efecto):  #Manipulamos la info manualmente sin necesidad de la API
        self.card = Yugih(efecto)
    
    def Search(self,nombre):    #Buscamos la info en la clase del Mock y no en la función Original
        return self.card


class TestRequest(unittest.TestCase):

    def test_card(self):
        card_test = (

            {
                "entrada" : "Red-Eyes B. Dragon",
                "salida_esperada" : "A ferocious dragon with a deadly attack."
            },
            {
                "entrada" : "Dark Magician",
                "salida_esperada" : "The ultimate wizard in terms of attack and defense."
            },
            {
                "entrada" : "Blue-Eyes White Dragon",
                "salida_esperada" : "This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale."
            },
            {
                "entrada" : "Dark Ruler No More",
                "salida_esperada" : "Negate the effects of all face-up monsters your opponent currently controls, until the end of this turn, also, for the rest of this turn after this card resolves, your opponent takes no damage. Neither player can activate monster effects in response to this card's activation."
            }


        )
    
        for tc in card_test:
            card_mock = YugiMock()
            card_mock.cardata(tc['salida_esperada'])

            actual = getCard(tc['entrada'], card_mock)
            self.assertEqual(tc['salida_esperada'], actual)

if __name__ == "__main__":
    unittest.main()