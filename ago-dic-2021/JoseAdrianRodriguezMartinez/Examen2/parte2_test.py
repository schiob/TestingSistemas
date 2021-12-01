
import unittest
from unittest.mock import patch
from parte2 import *

class Parte2(unittest.TestCase):

    @patch('parte2.escritor.escribir')
    def test_imp(self, mock):
        mock.return_value = '10 1'

        uso = implementacion()

        resultado = uso.escribir()

        self.assertEqual(uso.escribir, resultado)

if __name__ == '__main__':
    unittest.main()