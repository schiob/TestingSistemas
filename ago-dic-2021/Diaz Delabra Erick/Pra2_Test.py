import unittest
from unittest.main import main
from Pra2 import suma

class test(unittest.TestCase):
    def Postitivos(self):
        self.assertEqual(suma(5,5), 10)
    
    def NegativoYPositivo(self):
        self.assertEqual(suma(-1,10), 9)

    def PositivoYNegativo(self):
        self.assertEqual(suma(5, -1), 4)

    def Negativos(self):
        self.assertEqual(suma(-5,-5), -10)

if __name__ == '__main__':
    unittest.main()