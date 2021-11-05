import unittest
from unittest.mock import patch

from app import (calcular_tarifa, extraer_conductores, funcion_principal,
                 siguiente_usuario, viajes_disponibles)


class TestApp(unittest.TestCase):
    @patch('app.siguiente_usuario')
    def test_funcion_principal_1(self, mock_siguiente_usuario):
        mock_siguiente_usuario.return_value = [['Andres', '10'], ['Tom', '4'], ['Pepe', '3'], ['Susana', '2']]
        self.assertEqual(funcion_principal(), ['Andres - viaje 1', 'Tom - viaje 2', 'Pepe - viaje 3', 'Susana - viaje 4'])

    @patch('app.viajes_disponibles')
    def test_funcion_principal_2(self, mock_viajes_disponibles, ):
        mock_viajes_disponibles.return_value = [[1, 50], [2, 40], [3, 50], [4, 30]]
        self.assertEqual(funcion_principal(), ['Andres - viaje 1', 'Tom - viaje 2', 'Pepe - viaje 3', 'Susana - viaje 4'])

    @patch('app.extraer_conductores')
    def test_viajes_disponibles_1(self, mock_extraer_conductores):
        mock_extraer_conductores.return_value = [['Juan', '3'], ['Jesus', '2'], ['Maria', '3'], ['Toño', '1']]
        self.assertEqual(viajes_disponibles(), [[1, 50], [2, 40], [3, 50], [4, 30]])
    
    @patch('app.calcular_tarifa')
    def test_viajes_disponibles_2(self, mock_calcular_tarifa):
        mock_calcular_tarifa.return_value = 120
        self.assertEqual(viajes_disponibles(), [[1, 120], [2, 120], [3, 120], [4, 120]])

    @patch('mocks.File.Read')
    def test_siguiente_usuario(self, mock_file_read):
        mock_file_read.return_value = 'Tom 4\nSusana 2\nAndres 10\nPepe 3\nLuis 2'
        self.assertEqual(siguiente_usuario(), [['Andres', '10'], ['Tom', '4'], ['Pepe', '3'], ['Susana', '2']])

    @patch('mocks.File.Read')
    def test_extraer_conductores(self, mock_file_read):
        mock_file_read.return_value = 'Juan 3\nJesus 2\nMaria 3\nToño 1'
        self.assertEqual(extraer_conductores(), [['Juan', '3'], ['Jesus', '2'], ['Maria', '3'], ['Toño', '1']])

    def test_calcular_tarifa(self):
        self.assertEqual(calcular_tarifa(10), 120)
   
if __name__ == '__main__':
    unittest.main()
