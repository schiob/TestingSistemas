import unittest
from practica3 import numeros_lista

class TestNumeros(unittest.TestCase):
    def positivos(self):
        positivos = 0
        for i in numeros_lista(5,'1 2 3 4 5'):    
            if i > 0:
                positivos += 1
        self.assertEqual(positivos, 5)
    def negativos(self):
        negativos = 0
        for i in numeros_lista(5, '1 2 3 4 5'):
            if i < 0:
                negativos += 1
        self.assertEqual(negativos, 0)
    def pares(self):
        pares = 0
        for i in numeros_lista(5, '1 2 3 4 5'):
            if i % 2 == 0:
                pares += 1
        self.assertEqual(pares, 2)

    def impares(self):
        impares = 0
        for i in numeros_lista(5, '1 2 3 4 5'):
            if i %  2!= 0:
                impares += 1
        self.assertEqual(impares, 3)

if __name__ == '__main__':
    unittest.main()
