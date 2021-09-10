import unittest
from practica2 import sumar_dos_numeros

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        test_cases = [
            # Posición 1 y 2 entradas. Posición 3 salida esperada.
            (5,7,12),
            (-1,5,4),
            (-5,-6,-11),
            (4,-8,-4),
            (1/4,2/4,3/4),
            (2,2.5,4.5),
            ("p",5,"error"),
            (9,"c", "error"),
            ("w","t","error"),
        ]

        for tc in test_cases:
            resultado = sumar_dos_numeros(tc[0],tc[1])
            self.assertEqual(resultado,tc[2])

if __name__ == '__main__':
    unittest.main()
   


   