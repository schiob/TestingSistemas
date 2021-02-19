import unittest
from Practica2test import trian_1

class Pruebararo(unittest.TestCase):

    def test_equi(self):
        self.assertEqual(trian_1(3,3,3), 'Equilatero')

    def test_Isos(self):
        self.assertEqual(trian_1(4,4,2), 'Isoceles')

    def test_esca(self):
        self.assertEqual(trian_1(1,2,3), 'Escaleno') 

    def test_not(self):
        ada='asd'
        self.assertEqual(trian_1(1, 2, -5), 'Lado negativo!!!!')  


if __name__ == "__main__":
    unittest.main()

