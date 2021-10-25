import unittest
from viajes import *

class test1_usuario(unittest.TestCase):
    def test_siguiente_usuario(self):
        user = siguiente_usuario()
        self.assertEqual(user,'Susan')
        user = siguiente_usuario()
        self.assertEqual(user,'Luis')
        user = siguiente_usuario()
        self.assertEqual(user,'Pepe')

class test2_extraer_conductores(unittest.TestCase):
    def test_extraer_conductor(self):
        conductores = extraer_conductores()
        self.assertEqual(conductores,{'Juan': 3, 'Jesus': 2, 'Maria': 3, 'Toño': 1})

class test3_calc_tarifa(unittest.TestCase):
    def test_calc_tarifa(self):
        tarifa = calc_tarifa()
        self.assertEqual(tarifa)

class test4_viajes_disponibles(unittest.TestCase):
    def test_viajes_disp(self):
        lista = viajes_disp()
        self.assertEqual(lista,{1: 50, 2: 40, 3: 50, 4: 30})

if __name__ == '__main__':
    unittest.main() 