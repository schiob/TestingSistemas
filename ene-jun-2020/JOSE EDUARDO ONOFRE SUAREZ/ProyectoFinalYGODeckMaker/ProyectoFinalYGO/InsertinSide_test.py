import unittest
from MainDeck import CardinDeck
from SideDeck import SideDeck,SideDeckInterface
import SideDeck


class sideMock(SideDeckInterface):

    def setcard(self,id,name,types,desc,price,quantity):
        self.carta = CardinDeck(id,name,types,desc,price,quantity)

    def savecardtoSide(self,Card):
        return carta
    
    def insertarSide(self):
        pass    



class insertTest(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto...")
        self.side = CardinDeck(

                    56481,
                    "Lava Golem",
                    "Fiend",
                    "Descripcion de Lava Golem",
                    4.43,
                    2
                )
        return self.side


    def test_inTables(self):
        test_cases = [

            {
                "nombre" : "Insertar una carta en Tabla",
                "datos" : {

                    "Id" : 56481,
                    "Name" : "Lava Golem",
                    "Type" : "Fiend",
                    "Desc" : "Descripcion de Lava Golem",
                    "Price" : 4.43,
                    "Quantity" : 2


                },
                "salida_esperada" : self.side

            },

        ]

        for tc in test_cases:
            card_mock = sideMock()
            card_mock.setcard(

                tc["datos"]["Id"],
                tc["datos"]["Name"],
                tc["datos"]["Type"],
                tc["datos"]["Desc"],
                tc["datos"]["Price"],
                tc["datos"]["Quantity"]

            )
            obj = SideDeck.SideDeck("YugiohDB.db")
            actual = obj.savecardtoSide(card_mock.carta)
            self.assertEqual(actual,tc["salida_esperada"])

        def tearDown(self):
            print("Destruyendo el contexto...")
            del(self.side)

if __name__ == "__main__":
    unittest.main()