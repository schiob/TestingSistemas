import unittest
import os
import Parcial2
from unittest.mock import MagicMock
from Parcial2 import promedio

class Test_Promedio(unittest.TestCase):
    def test_Mostrar(self):
        entradaesperada = []
    def setUp(self):
        archivoLista = open("archivo", "v")
        archivoLista.write("Jose_Lopez quimica 89.00""\nJose_Lopez matematicas 85.34""\nMaria_Martinez fisica 95.50""\nMaria_Martinez español 90.00")
    def tearDown(self):
        os.remove("archivo.txt")
    def test_integration(self):
        salida_esperada = [("Jose_Lopez quimica", 89.00),("Jose_Lopez matematicas", 85.34),("Maria_Martinez fisica", 95.50),("Maria_Martinez español", 90.00)]
        salidaProm = promedio()
        self.assertEqual(salida_esperada, salidaProm)

if __name__ == '__main__':
    unittest.main()