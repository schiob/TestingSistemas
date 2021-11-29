import unittest
from unittest import mock
from unittest.mock import patch
from practica_uber2 import *

class UberTest(unittest.TestCase):
    @patch('practica_uber2.uber.viajes_disponibles')
    def test_siguiente_usuario(self, mock_viajes_disponibles):
        mock_viajes_disponibles.return_value = {1: 20, 2: 50, 3: 25, 4: 11}

        prueba = uber()
        self.assertEqual(prueba.principal(),
        ['Usuario: Susana, ID del viaje: 4', 'Usuario: Luis, ID del viaje: 1', 'Usuario: Pepe, ID del viaje: 3', 'Usuario: Tom, ID del viaje: 2'])
    
    @patch('practica_uber2.uber.calcular_tarifa')
    def test_calcular_tarifa(self, mock_calcular_tarifa):
        mock_calcular_tarifa.return_value = [15, 25, 30, 55]

        prueba = uber()
        self.assertEqual(prueba.principal(),
        ['Usuario: Susana, ID del viaje: 1', 'Usuario: Luis, ID del viaje: 2', 'Usuario: Pepe, ID del viaje: 3', 'Usuario: Tom, ID del viaje: 4'])