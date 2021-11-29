from typing import Text
import unittest
import builtins
from unittest import result, TestCase, mock
from unittest.mock import patch, mock_open
from practia_6 import calcular_tarifa
from practia_6 import viajes_disponibles
from practia_6 import siguiente_usuario
from practia_6 import extraer_conductores
from practia_6 import Principal
from textwrap import dedent

class test_calcular_tarifa(unittest.TestCase):
    def test_uno (self):
        lista= [[1,30],[2,40],[3,50],[4,60],[5,70,],[6,80],[7,90],[8,100]]
        for i in range(0,len(lista),1):
            resultado=calcular_tarifa(int(lista[i][0]))
            self.assertEqual(resultado,lista[i][1])

class test_siguiente_usuario(unittest.TestCase):
    DATA = dedent("""
        Tom 4
Susana 2
Andres 10
Pepe 3
Luis 2
        """).strip()
    @patch("builtins.open", mock_open(read_data=DATA))
    def test_uno (self):
        with open("usuarios", "r") as f:
           result=f.read()
        open.assert_called_once_with("usuarios", "r")
        self.assertEqual(siguiente_usuario(),'Susana')

class test_Extraer_conductores(unittest.TestCase):
    DATA = dedent("""
       Juan 3
Jesus 2
Maria 3
Toño 1
        """).strip()
    @patch("builtins.open", mock_open(read_data=DATA))
    def test_uno (self):
        with open("conductores", "r") as f:
           result=f.read()
        open.assert_called_once_with("conductores", "r")
        self.assertEqual(extraer_conductores(),[['Juan', 3], ['Jesus', 2], ['Maria', 3], ['Toño', 1]])

class test_viajes_disponibles(unittest.TestCase):
    DATA = dedent("""
       Juan 3
Jesus 2
Maria 3
Toño 1
        """).strip()
    @patch("builtins.open", mock_open(read_data=DATA))
    def test_uno (self):
        with open("conductores", "r") as f:
           result=f.read()
        open.assert_called_once_with("conductores", "r")
        self.assertEqual(viajes_disponibles(),[[1, 50], [2, 40], [3, 50], [4, 30]])

class test_principal(unittest.TestCase):
    DATA_conductores = dedent("""
       Juan 3
Jesus 2
Maria 3
Toño 1
        """).strip()
    @patch("builtins.open", mock_open(read_data=DATA_conductores))
    def test_uno (self):
        with open("conductores", "r") as f:
           result=f.read()
        open.assert_called_once_with("conductores", "r")
        self.assertEqual(Principal(),[['Toño', 'viaje 1'],['Toño', 'viaje 2'],['Toño', 'viaje 3'],['Toño', 'viaje 4']])


if __name__ =='__main__':
 unittest.main()