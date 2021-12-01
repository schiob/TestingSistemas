import builtins
import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch
from calcular_promedio import *


class PromedioTest(TestCase):
    @patch('__main__.open', create=True)
    def test_archivito(self, mock_open):
        mock_open.return_value = 15
        salida_esperada = 3
        self.assertEqual(calc_prom(), salida_esperada)


if __name__ == '__main__':
    unittest.main()
