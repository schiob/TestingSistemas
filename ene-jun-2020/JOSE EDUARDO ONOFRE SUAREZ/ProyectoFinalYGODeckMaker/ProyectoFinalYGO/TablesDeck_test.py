import unittest
import MainDeck
import ExtraDeck
from ExtraDeck import tableExtraDeck
import SideDeck
from SideDeck import tableSideDeck
from MainDeck import MainDeckInterface
from MainDeck import tableMainDeck
from unittest.mock import patch,MagicMock

class TablesDeck_test(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto...")
        self.call = tableMainDeck()
        self.callE = tableExtraDeck()
        self.callS = tableSideDeck()
    

    def test_MainBD(self):

        test_cases = [

            {
                "nombre" : "Crear Tabla MainDeck en la BD",
                "entrada" : self.call,
                "salida_esperada" : 'Tabla MainDeck creada con exito' 
            },
            {
                "nombre" : "Crear Tabla ExtraDeck en la BD",
                "entrada" : self.callE,
                "salida_esperada" : 'Tabla ExtraDeck creada con exito' 
            },
            {
                "nombre" : "Crear Tabla SideDeck en la BD",
                "entrada" : self.callS,
                "salida_esperada" : 'Tabla SideDeck creada con exito' 
            },
            
            
        ]


        for tc in test_cases:
            self.assertEqual(tc['entrada'],tc['salida_esperada'])
            
    def tearDown(self):
        print("Destruyendo el contexto...")
        del(self.call)


if __name__ == "__main__":
    unittest.main()