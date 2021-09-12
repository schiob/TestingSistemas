import unittest
from sumar import calculo

class TestSumar(unittest.TestCase):

    def sumar_positivos(self):
        calculo_real = calculo(10, 10)
        self.assertEqual(calculo_real, 20)

    def sumar_multiplicados(self):
        calculo_real = calculo(10*10, 50)
        self.assertEqual(calculo_real, 150)
    
    def sumar_divididos(self):
        calculo_real = calculo(10/5, 3)
        self.assertEqual(calculo_real, 5)
    
    def sumar_negativos(self):
        calculo_real = calculo(-50, -20)
        self.assertEqual(calculo_real, -70)

if __name__ == '__main__':
    unittest.main()
