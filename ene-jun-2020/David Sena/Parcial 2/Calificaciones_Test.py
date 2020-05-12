import unittest
import os
import Calificaciones
from unittest.mock import MagicMock
from Calificaciones import *

class TestAlumnos(unittest.TestCase):
    def testMostrar(self):
        entrada = [("Jose_Lopez","quimica", 89.00),
                    ("Jose_Lopez","matematicas", 96.22),
                    ("Maria_Martinez","fisica", 95.50),
                    ("Maria_Martinez","español", 97.25)]

        expected_out = [("Jose_Lopez", 89.00),
                           ("Jose_Lopez", 96.22),
                           ("Maria_Martinez", 95.50),
                           ("Maria_Martinez", 97.25)]

        Mock = MagicMock()
        Mock.mostrar.return_value = entrada

        real = Promedio(Mock)
        self.assertEqual(expected_out, real)

    def setUp(self):
        archivo = open("Calificaciones_Test.txt", "w")
        archivo.write("Jose_Lopez quimica 89.00""\nJose_Lopez matematicas 96.22""\nMarta_Martinez fisica 95.50""\nMarta_Martinez español 97.25")

    def tearDown(self):
        os.remove("Calificaciones_Test.txt")

    def test_integration(self):

        expected_out = [("Jose_Lopez", 89.00),
                           ("Jose_Lopez", 96.22),
                           ("Maria_Martinez", 95.50),
                           ("Maria_Martinez", 97.25)]

        real = Promedio(Mock)
        self.assertEqual(expected_out, real)

if __name__ == '__main__':
    unittest.main()