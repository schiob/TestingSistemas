import unittest
from practica2 import sumar_dos_numeros

class TestSumar (unittest.TestCase):
    def test_suma (self):
        test_cases = [
            (5,7,12),
            (-4,1,-3),
            (6,-1,5),
            (-5,-5,-10),
            (0.5,0.5,1),
            (1/4,1/4,2/4),
            ("q",5,"error"),
            (7,"w","error"),
            ("r","r","error"),
            ]

        for tc in test_cases:
            resultado = sumar_dos_numeros (tc[0],tc[1])
            self.assertEqual(resultado,tc[2])

if __name__ == '__main__':
    unittest.main()  