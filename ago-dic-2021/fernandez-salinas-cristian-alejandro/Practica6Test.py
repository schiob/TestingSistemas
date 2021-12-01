import unittest
from unittest import mock
from unittest.mock import patch
from Practica6 import (siguiente_usuario,
    calcular_tarifa,
    extraer_conductores,
    viajes_disponibles,
    principal
)




class test_principal(unittest.TestCase):

    @patch('uber.siguiente_usuario')
    def test_funcion_principal_test1(self,mock_siguiente_usuario):

        mock_siguiente_usuario.return_value = 'Susana'
        self.assertEqual(principal(),{4: 'Susana', 2: 'Susana', 1: 'Susana', 3: 'Susana'} )

    @patch('uber.viajes_disponibles')
    def test_funcion_principal_test2(self,mock_viajes_disponibles):

        mock_viajes_disponibles.return_value = '30'
        print(str(mock_viajes_disponibles))

        self.assertEqual(viajes_disponibles(),{1: 50, 2: 40, 3: 50, 4: 30})


    @patch('uber.extraer_conductores')
    def test_viajes_disponibles(self,mock_extraer_conductores):

        mock_extraer_conductores.return_value = {'Juan' :  3}

        self.assertEqual(viajes_disponibles(),{1: 50, 2: 40, 3: 50, 4: 30})

    @patch('uber.calcular_tarifa')
    def test_viajes_disponibles_test2(self,mock_calcular_tarifa):

        mock_calcular_tarifa.return_value ='Juan'

        self.assertEqual(calcular_tarifa('Juan'),50)





if __name__ == "__main__":
    unittest.main() 