import unittest
from unittest.main import main
from Problema import numerosxd

class testNumeros(unittest.TestCase):
    def test_1(self):
        entrada = numerosxd([51, -12, -3, 0, 2])
        esperado = '2 positivos, 2 negativos, 3 pares, 2 impares'
        self.assertEqual(entrada, esperado)
        
    def test_2(self):
        entrada = numerosxd([0, 1, 2, 3, 4])
        esperado = '4 positivos, 0 negativos, 3 pares, 2 impares'
        self.assertEqual(entrada, esperado)

    def test_3(self):
        entrada = numerosxd([-1, -2, -3])
        esperado = '0 positivos, 3 negativos, 1 pares, 2 impares'
        self.assertEqual(entrada, esperado)

    def test_4(self):
        entrada = numerosxd([0])
        esperado = '0 positivos, 0 negativos, 1 pares, 0 impares'
        self.assertEqual(entrada, esperado)

if __name__ == '__main__':
    unittest.main()
    