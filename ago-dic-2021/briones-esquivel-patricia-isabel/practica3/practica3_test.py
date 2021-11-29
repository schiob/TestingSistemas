import unittest
from practica3 import clasificar_num

class TestClasificar (unittest.TestCase):
    def test_clasificar (self):
        test_cases = [
            # --Primer elemento: entrada, 
            # --Segundo elemento: Salida esperada (Positivo, negativo, par, impar)
            ([51,-12,-3,0,2],[2,2,3,2]),
            ([0, 1, 2, 3, 4],[4,0,3,2]),
            ([-1, -2, -3],[0,3,1,2]),
            ([0],[0,0,1,0])
            ]

        for tc in test_cases:
            resultado = clasificar_num (tc[0])
            self.assertEqual(resultado,tc[1])
            
if __name__ == '__main__':
    unittest.main()  