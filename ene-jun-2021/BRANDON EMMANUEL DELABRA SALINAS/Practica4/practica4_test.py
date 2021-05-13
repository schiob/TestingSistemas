import unittest
from unittest.mock import patch, MagicMock
from practica4 import Shouter


class TestShouter(unittest.TestCase):
    @patch("requests.post")
    def test_Shouter(self):
        entrada = "hola a todos"
        magick_response = MagicMock()
        magick_response.text = "HOLA A TODOS"

        actual = Shouter(entrada)
        self.assertEqual(actual, "HOLA A TODOS")


    def test_Shouter_mixed(self):
        entrada = "asdf1234AsdF"
        self.assertEqual(Shouter(entrada),"ASDF1234ASDF")


    def test_Shouter_numbers(self):
        entrada = "1234567"
        self.assertEqual(Shouter(entrada),"1234567")




if __name__ == '__main__':
    unittest.main()