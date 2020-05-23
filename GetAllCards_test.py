import unittest
from APIRequest import getAllCards
import APIRequest
class GetAllCards_test(unittest.TestCase):

    # Test para asegurar que nos regresa todas las cartas de la base de datos
    def setUp(self):
        print("Preparando el contexto...")
        self.opcion = 2
        self.cards = 7016
        
    def test_file(self):
        entrada = self.opcion
        salida_esperada = self.cards
        salida_real = getAllCards()
            
        self.assertEqual(salida_esperada,salida_real)
        
    def tearDown(self):
        print("Destruyendo el contexto...")
        del(self.opcion)
        del(self.cards)

    
    




if __name__ == "__main__":
    unittest.main()