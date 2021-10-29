import unittest
from unittest.mock import patch
from uber import *

class SiguienteUsuarioTest(unittest.TestCase):
    @patch('uber.Uber.siguiente_usuario')
    def test_principal_siguiente_usuario(self, mock_siguiente_usuario):
        mock_siguiente_usuario.return_value = 'ChioCode'
        print(str(mock_siguiente_usuario))

        principal = Uber()

        principal.viajes_disponibles()

        respuesta = principal.siguiente_usuario()
        print(respuesta)

        self.assertEqual(principal.principal(),
            f'Usuario: {respuesta} ID del viaje: 4\nUsuario: {respuesta} ID del viaje: 2\nUsuario: {respuesta} ID del viaje: 1\nUsuario: {respuesta} ID del viaje: 3'
        )

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