import unittest
from unittest import mock
from unittest.mock import patch
from uber import *

class UberTest(unittest.TestCase):
    @patch('uber.Uber.viajes_disponibles')
    def test_siguiente_usuario(self, mock_viajes_disponibles):
        mock_viajes_disponibles.return_value = {1: 20, 2: 50, 3: 25, 4: 11}

        prueba = Uber()
        self.assertEqual(prueba.principal(),
        ['Usuario: Susana, ID del viaje: 4', 'Usuario: Luis, ID del viaje: 1', 'Usuario: Pepe, ID del viaje: 3', 'Usuario: Tom, ID del viaje: 2'])

    @patch('uber.Uber.extraer_conductores')
    def test_calcular_tarifa_extraer_conductores(self, mock_extraer_conductores):
        mock_extraer_conductores.return_value =  ['Juan', '5', 'Jesus', '8', 'Mariam', '2', 'Antonio', '3']

        prueba = Uber()
        self.assertEqual(prueba.principal(),
        ['Usuario: Susana, ID del viaje: 3', 'Usuario: Luis, ID del viaje: 4', 'Usuario: Pepe, ID del viaje: 1', 'Usuario: Tom, ID del viaje: 2'])

    @patch('uber.Uber.calcular_tarifa')
    def test_calcular_tarifa(self, mock_calcular_tarifa):
        mock_calcular_tarifa.return_value = [15, 25, 30, 55]

        prueba = Uber()
        self.assertEqual(prueba.principal(),
        ['Usuario: Susana, ID del viaje: 1', 'Usuario: Luis, ID del viaje: 2', 'Usuario: Pepe, ID del viaje: 3', 'Usuario: Tom, ID del viaje: 4'])







### OTRO TIPO DE PRUEBAS

    # @patch('uber.Uber.siguiente_usuario')
    # def test_principal_siguiente_usuario(self, mock_siguiente_usuario):
    #     mock_siguiente_usuario.return_value = 'ChioCode'
    #     print(str(mock_siguiente_usuario))

    #     pr = Uber()

    #     pr.viajes_disponibles()

    #     respuesta = pr.siguiente_usuario()
    #     print(respuesta)

    #     self.assertEqual(pr.principal(),
    #         f'Usuario: {respuesta} ID del viaje: 4\nUsuario: {respuesta} ID del viaje: 2\nUsuario: {respuesta} ID del viaje: 1\nUsuario: {respuesta} ID del viaje: 3'
    #     )

    # @patch('uber.Uber.viajes_disponibles')
    # def test_siguiente_viaje__viajes_disponibles(self, mock_viajes_disponibles):
    #     mock_viajes_disponibles.return_value = {1: 25, 2: 35, 3: 65, 4: 39}

    #     principal = Uber()

    #     respuesta = principal.viajes_disponibles()

    #     principal.viajes = respuesta
    #     # print(respuesta)

    #     self.assertEqual(principal.viajes_disponibles()[1], 25)
    #     self.assertEqual(principal.viajes_disponibles()[2], 35)
    #     self.assertEqual(principal.viajes_disponibles()[3], 65)
    #     self.assertEqual(principal.viajes_disponibles()[4], 39)

    # @patch('uber.Uber.calcular_tarifa')
    # def test_viajes_disponibles_calcular_tarifa(self, mock_calcular_tarifa):
    #     mock_calcular_tarifa.return_value = [50, 50, 50, 50]

    #     principal = Uber()

    #     resultado = principal.calcular_tarifa()

    #     self.assertEqual(principal.viajes_disponibles(), {1: resultado[0], 2: resultado[1], 3: resultado[2], 4: resultado[3]})

if __name__ == '__main__':
    unittest.main()