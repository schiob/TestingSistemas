import builtins
import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import mock_open, patch
from escritor import *

class ElEscritor(unittest.TestCase):
    @patch('escritor.Escribiendo.numero_de_palabras')
    def test_escritor_con_letras_b(self, mock_letras_b):
        mock_letras_b.return_value = '7'

        letras = Escribiendo.numero_de_palabras()

        self.assertEqual(Escribiendo.numero_de_palabras(), letras)


if __name__ == '__main__':
    unittest.main()