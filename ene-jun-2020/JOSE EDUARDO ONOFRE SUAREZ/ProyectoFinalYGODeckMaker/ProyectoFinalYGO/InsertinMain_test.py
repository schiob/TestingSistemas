import unittest
from MainDeck import MainDeckInterface, CardinDeck
import MainDeck
from MainDeck import MainDeck
import sqlite3

class mainMock(MainDeckInterface):

    def setcard(self,id,name,types,desc,price,quantity):
        self.carta = CardinDeck(id,name,types,desc,price,quantity)

    def savecardtoMain(self,Card):
        return self.carta



class insertTest(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto...")
        self.main = CardinDeck(

                    1234,
                    "The Winged Dragon of RA",
                    "Winged Beast",
                    "Descripcion de Dragon of RA",
                    5.50,
                    1
                )


    def inTables_test(self):
        test_cases = [

            {
                "nombre" : "Insertar una carta en Tabla",
                "datos" : {

                    "Id" : 1234,
                    "Name" : "The Winged Dragon of RA",
                    "Type" : "Winged Beast",
                    "Desc" : "Descripcion de Dragon of RA",
                    "Price" : 5.50,
                    "Quantity" : 1


                },
                "salida_esperada" : self.main

            },

        ]

        for tc in test_cases:
            card_mock = mainMock()
            card_mock.setcard(

                tc["datos"]["Id"],
                tc["datos"]["Name"],
                tc["datos"]["Type"],
                tc["datos"]["Desc"],
                tc["datos"]["Price"],
                tc["datos"]["Quantity"]

            )
            obj = MainDeck("YugiohDB.db")
            actual = obj.savecardtoMain(card_mock.carta)
            self.assertEqual(actual,tc["salida_esperada"])
            
        def tearDown(self):
            print("Destruyendo el contexto...")
            del(self.main)

if __name__ == "__main__":
    unittest.main()

        