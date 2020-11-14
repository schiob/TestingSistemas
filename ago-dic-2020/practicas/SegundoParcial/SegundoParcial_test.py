import unittest
import os
from unittest.mock import MagicMock
from SegundoParcial import promedio

class TestPromedio(unittest.TestCase):
    def testMostrar(self):
        entrada = []

    def setUp(self):
        archivo = open("calificaciones_test.txt", "w")
        archivo.write("Jose_Lopez quimica 89.00""\nJose_Lopez matematicas 85.34""\nMaria_Martinez fisica 95.50""\nMaria_Martinez español 90.00")

    def testReader(self):
        entrada = ['Jose_Lopez quimica 89.00\n', 'Jose_Lopez matematicas 85.34\n', 'Maria_Martinez fisica 95.50\n',
                   'Maria_Martinez espanol 90.00\n']
        salida_esperada = {'Jose_Lopez': 87.17, 'Maria_Martinez': 92.75}

        fileMock = MagicMock()
        fileMock.reader.return_value = entrada

        real = promedio(fileMock)
        self.assertEqual(salida_esperada, real)

    def test_integration(self):
        salida_esperada = [("Jose_Lopez quimica", 89.00),
                           ("Jose_Lopez matematicas", 85.34),
                           ("Maria_Martinez fisica", 95.50),
                           ("Maria_Martinez español", 90.00)]

        real = promedio()
        self.assertEqual(salida_esperada, real)

    def tearDown(self):
        os.remove("calificaciones_test.txt")

if __name__ == '__main__':
    unittest.main()