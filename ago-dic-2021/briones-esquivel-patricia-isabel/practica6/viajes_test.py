import unittest
from viajes import *

class Mock_usuario ():
    def __init__(self, return_value): 
        self.return_value = return_value

    def leer_u(self) -> list: 
        usuarios = self.return_value.split('\n')
        return usuarios

class Mock_conductor ():
    def __init__(self, return_value): 
        self.return_value = return_value

    def leer_c(self) -> list: 
        conductores = self.return_value.split('\n')
        return conductores


class TestViajes(unittest.TestCase):
    def test_extraer_usuarios(self):
        mi_mock = Mock_usuario("Andres 10\nTom 4\nPepe 3\nSusana 2\nLuis 2")         
        self.assertEqual(extraer_usuarios(mi_mock), [[10, 'Andres'], [4, 'Tom'], [3, 'Pepe'], [2, 'Susana'], [2, 'Luis']])
        
    def test_extraer_conductores(self):
        mi_mock = Mock_conductor("Juan 3\nJesus 2\nMaria 3\nPedro 1")         
        self.assertEqual(extraer_conductores(mi_mock), [['Juan', 3], ['Jesus', 2], ['Maria', 3], ['Pedro', 1]])
        
    def test_calcular_tarifa(self):
        mi_mock = Mock_conductor("Juan 3\nJesus 2\nMaria 3\nPedro 1")
        self.assertEqual(calcular_tarifa(extraer_conductores(mi_mock), 'Maria'),50)

    def test_viajes_disponibles(self):
        mi_mock = Mock_conductor("Juan 3\nJesus 2\nMaria 3\nPedro 1")
        self.assertEqual(viajes_disponibles(extraer_conductores(mi_mock)),[[1, 50], [2, 40], [3, 50], [4, 30]])

    def test_siguiente_usuario(self):
        mi_mock = Mock_usuario("Andres 10\nTom 4\nPepe 3\nSusana 2\nLuis 2")         
        self.assertEqual(siguiente_usuario(extraer_usuarios(mi_mock)),['Luis', 'Susana', 'Pepe', 'Tom', 'Andres'])

    def test_funcion_principal(self):
        mi_mock = Mock_usuario("Andres 10\nTom 4\nPepe 3\nSusana 2\nLuis 2")         
        mi_mock1 = Mock_conductor("Juan 3\nJesus 2\nMaria 3\nPedro 1")
        self.assertEqual(main(siguiente_usuario(extraer_usuarios(mi_mock)),viajes_disponibles(extraer_conductores(mi_mock1))),['Luis - viaje 4', 'Susana - viaje 2', 'Pepe - viaje 1', 'Tom - viaje 3'])


if __name__ == "__main__":
    unittest.main()




