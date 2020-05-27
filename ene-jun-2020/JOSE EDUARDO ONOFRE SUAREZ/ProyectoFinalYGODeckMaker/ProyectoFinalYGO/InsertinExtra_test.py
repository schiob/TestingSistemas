import unittest
from MainDeck import CardinDeck
from ExtraDeck import ExtraDeckInterface, ExtraDeck
import ExtraDeck


class extraMock(ExtraDeckInterface):

    def setcard(self,id,name,types,desc,price,quantity):
        self.carta = CardinDeck(id,name,types,desc,price,quantity)

    def savecardtoMain(self,Card):
        return carta



class insertTest(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto...")
        self.extra = CardinDeck(

                    9876,
                    "Borreload Dragon",
                    "Dragon",
                    "Descripcion de Borreload Dragon",
                    32.43,
                    3
                )
        return self.extra


    def inTables_test(self):
        test_cases = [

            {
                "nombre" : "Insertar una carta en Tabla",
                "datos" : {

                    "Id" : 1234,
                    "Name" : "Borreload Dragon",
                    "Type" : "Dragon",
                    "Desc" : "Descripcion de Borreload Dragon",
                    "Price" : 32.43,
                    "Quantity" : 3


                },
                "salida_esperada" : self.extra

            },

        ]

        for tc in test_cases:
            card_mock = extraMock()
            card_mock.setcard(

                tc["datos"]["Id"],
                tc["datos"]["Name"],
                tc["datos"]["Type"],
                tc["datos"]["Desc"],
                tc["datos"]["Price"],
                tc["datos"]["Quantity"]

            )
            obj = ExtraDeck("YugiohDB.db")
            actual = obj.savecardtoExtra(card_mock.carta)
            self.assertEqual(actual,tc["salida_esperada"])

        def tearDown(self):
            print("Destruyendo el contexto...")
            del(self.extra)

if __name__ == "__main__":
    unittest.main()

        