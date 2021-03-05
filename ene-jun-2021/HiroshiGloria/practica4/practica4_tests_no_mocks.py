import unittest
from practica4 import Shouter

class TestShouter(unittest.TestCase):
    def test_Shouter_With_Only_Text_DownCased(self):
        cadena = "hola a todos"
        self.assertEqual(Shouter(cadena),"HOLA A TODOS")

    def test_Shouter_With_Only_Text_Some_DownCased(self):
        cadena = "hOlA a todOs"
        self.assertEqual(Shouter(cadena),"HOLA A TODOS")

    def test_Shouter_With_Only_Numbers(self):
        cadena = "1234567"
        self.assertEqual(Shouter(cadena),"1234567")

    def test_Shouter_With_Mixed_Input(self):
        cadena = "asdf1234AsdF"
        self.assertEqual(Shouter(cadena),"ASDF1234ASDF")


if __name__ == '__main__':
    unittest.main()