import unittest
from uber import *

class UsuarioTest(unittest.TestCase):
    def test_siguiente_usuario(self):
        usuario = siguiente_usuario()
        self.assertEqual(usuario, 'Susana')
        usuario = siguiente_usuario()
        self.assertEqual(usuario, 'Luis')
        usuario = siguiente_usuario()
        self.assertEqual(usuario, 'Pepe')
        usuario = siguiente_usuario()
        self.assertEqual(usuario, 'Tom')
        usuario = siguiente_usuario()
        self.assertEqual(usuario, 'Andres')

class ConductorTest(unittest.TestCase):
    def test_extraer_conductores(self):
        conductor = extraer_conductores()
        self.assertEqual(conductor, ['Juan', '3', 'Jesus', '2', 'Mariam', '3', 'Antonio', '1'])

class TarifaTest(unittest.TestCase):
    def test_calculo_de_las_tarifas(self):
        tarifa = calcular_tarifa()
        self.assertEqual(tarifa, [50, 40, 50, 30])

class TestViajes(unittest.TestCase):
    def test_viajes_disponibles(self):
        viajes = viajes_disponibles()
        self.assertEqual(viajes, {1: 50, 2: 40, 3: 50, 4: 30})




if __name__ == '__main__':
    unittest.main()