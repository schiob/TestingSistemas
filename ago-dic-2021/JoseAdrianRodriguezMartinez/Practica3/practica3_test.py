import unittest
from practica3 import *

class Practica3_test(unittest.TestCase):
    def test_1(self):
        entrada = [51, -12, -3, 0, 2]
        #el orden en la lista es positivo, negativo, par e impar
        salida_real=[]
        salida_esperada = [2, 2, 3, 2]
        
        salida_real.append(positivos(entrada))
        salida_real.append(negativos(entrada))
        salida_real.append(pares(entrada))
        salida_real.append(impares(entrada))
       
        self.assertEqual(salida_real, salida_esperada)

    def test_dos(self):
        entrada = [0, 1, 2, 3, 4]
        salida_real = []
        salida_esperada = [4, 0, 3, 2]
      
        salida_real.append(positivos(entrada))
        salida_real.append(negativos(entrada))
        salida_real.append(pares(entrada))
        salida_real.append(impares(entrada))

        self.assertEqual(salida_real, salida_esperada)

    def test_tres(self):
        entrada = [-1, -2, -3]
        salida_real = []
        salida_esperada = [0, 3, 1, 2]
        
        salida_real.append(positivos(entrada))
        salida_real.append(negativos(entrada))
        salida_real.append(pares(entrada))
        salida_real.append(impares(entrada))
        
        self.assertEqual(salida_real, salida_esperada)

    def test_cuatro(self):
        entrada = [0]
        salida_real = []
        salida_esperada = [0, 0, 1, 0]

        salida_real.append(positivos(entrada))
        salida_real.append(negativos(entrada))
        salida_real.append(pares(entrada))
        salida_real.append(impares(entrada))
        self.assertEqual(salida_real, salida_esperada)

if __name__ == '__main__':
    unittest.main()
    