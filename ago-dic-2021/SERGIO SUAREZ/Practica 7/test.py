import unittest
from unittest import mock
from unittest.mock import patch
from viajes import *

class ViajesTest1(unittest.TestCase):
    @patch('viajes.Viajes.extraer_conductores')
    def test_1(self, mock_extraer_conductores):
        mock_extraer_conductores.return_value =  {'Juan', '3', 'Jesus', '2', 'Mariam', '3', 'Toño', '1'}
        prueba = Viajes()
        self.assertEqual(prueba.principal(), {'Juan': 3, 'Jesus': 2, 'Maria': 3, 'Toño': 1})

    @patch('viajes.Viajes.extraer_conductores')
    def test_2(self, mock_extraer_conductores):
        mock_extraer_conductores.return_value =  {'Juan', '5', 'Jesus', '1'}
        prueba = Viajes()
        self.assertEqual(prueba.principal(), {'Juan': 5, 'Jesus': 1})