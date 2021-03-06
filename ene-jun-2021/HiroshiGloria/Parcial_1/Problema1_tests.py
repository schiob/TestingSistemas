import unittest
from Problema1 import Triangulares as tri

class TestProblema1(unittest.TestCase):
    def test_Numero1(self):
        numero = 1
        res = tri(numero)
        self.assertEqual(res,1)

    def test_Numero3(self):
        numero = 3
        res = tri(numero)
        self.assertEqual(res,6)

    def test_Numero4(self):
        numero = 4
        res = tri(numero)
        self.assertEqual(res,10)

    def test_Numero56(self):
        numero = 56
        res = tri(numero)
        self.assertEqual(res,1596)

    def test_NumeroNegativo(self):
        numero = -1000
        res = tri(numero)
        self.assertEqual(res,"Número inválido.")

if __name__ == '__main__':
    unittest.main()