import os
import unittest
from unittest.mock import MagicMock
import prom
from prom import *


class PromTest(unittest.TestCase):
    def testMostrar(self):
        entrada = []

    def setUp(self):
        archivo = open("calificaciones_Test.txt", "r")
        archivo.write("Jose_Lopez quimica 89.00""\nJose_Lopez matematicas 85.34""\nMaria_Martinez fisica 95.50""\nMaria_Martinez español 90.00")

    def tearDown(self):
        os.remove("informacion_test.txt")

    def test_integration(self):
        salida_esperada = [("Jose_Lopez quimica", 89.00),
                           ("Jose_Lopez matematicas", 85.34),
                           ("Maria_Martinez fisica", 95.50),
                           ("Maria_Martinez español", 90.00)]

        real = promedio()
        self.assertEqual(salida_esperada, real)


if __name__ == '__main__':
    unittest.main()