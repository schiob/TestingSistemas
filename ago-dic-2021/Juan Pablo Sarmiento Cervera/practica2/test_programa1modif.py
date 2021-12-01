import unittest
from unittest.case import TestCase
from practica1modif import suma

class test_suma(unittest.TestCase):
    def test_suma(self):
        Test_Case = [
            (1,3,4),
            (7,9,15),
            ("a",7,"error"),
            (5,"b","Error"),
            #(5.2,7.8,13.0)

        ]

        for tc in Test_Case:
            resultado = suma(tc[0], tc[1])
            self.assertEqual(resultado, tc[2])

if __name__ == "__main__":
    unittest.main()