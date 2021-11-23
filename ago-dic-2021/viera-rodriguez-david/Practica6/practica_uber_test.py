import unittest
from practica_uber import *

class test_user(unittest.TestCase):
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

class test_driver(unittest.TestCase):
    def test_extraer_conductores(self):
        conductor = extraer_conductores()
        self.assertEqual(conductor, ['Juan', '3', 'Jesus', '2', 'Mariam', '3', 'Antonio', '1'])

class test_tarifa(unittest.TestCase):
    def test_calculo_de_las_tarifas(self):
        tarifa = calcular_tarifa()
        self.assertEqual(tarifa, [30, 20, 10, 60])

class test_tarifa(unittest.TestCase):
    def test_viajes_disponibles(self):
        viajes = viajes_disponibles()
        self.assertEqual(viajes, {1: 30, 2: 200, 3: 10, 4: 60})




if __name__ == '__main__':
    unittest.main()