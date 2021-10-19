
import unittest
from uber import (siguiente_usuario,
    calcular_tarifa,
    extrar_conductores,
    viajes_disponibles,
    principal
)
class test_usuario(unittest.TestCase):
    def test_usuario_siguiente(self):
        user = siguiente_usuario()
        self.assertEqual(user,'Susana')

        user = siguiente_usuario()
        self.assertEqual(user,'Luis')

        user = siguiente_usuario()
        self.assertEqual(user,'Pepe')

class test_conductor(unittest.TestCase):
    def test_extraer_conductor(self):
        conductores = extrar_conductores()
        self.assertEqual(conductores,{'Juan': 3, 'Jesus': 2, 'Maria': 3, 'Toño': 1})

class test_tarifa(unittest.TestCase):
    def test_calculo_tarifa(self):
        tarifa = calcular_tarifa("Juan")
        self.assertEqual(tarifa,50)

class test_viajes(unittest.TestCase):
    def test_lista_viajes_disponibles(self):
        lista = viajes_disponibles()
        self.assertEqual(lista,{1: 50, 2: 40, 3: 50, 4: 30})



if __name__ == "__main__":
    unittest.main()