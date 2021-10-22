
import unittest
from promedio import *
from unittest import TestCase
from unittest import mock
from unittest.mock import patch



class test_promedio(TestCase):
    @patch('builtins.open', create=True)
    def test_archivito(self, mock_open):
         mock_open.return_value = 10
         salida_esperada = 2
         self.assertEqual(calc_prom(), salida_esperada)
    
    # def test_archivito1(self, mock_open):
    #     mock_open.return_value = 10
    #     salida_esperada = 1.6666667
    #     self.assertEqual(calc_prom(), salida_esperada)
    
    # def test_archivito2(self, mock_open):
    #     mock_open.return_value = 10
    #     salida_esperada = 10
    #     self.assertEqual(calc_prom(), salida_esperada)

if __name__ == '__main__':
    unittest.main()