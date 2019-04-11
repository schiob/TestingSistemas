import unittest
import os
import SegundoParcial
from unittest.mock import MagicMock
from SegundoParcial import Alumnos

class TestAlumnos(unittest.TestCase):
    def testMostrar(self):
        entrada = [("Jose_Lopez","quimica", 99.08),
                    ("Jose_Lopez","matematicas", 95.37),
                    ("Maria_Martinez","fisica", 85.60),
                    ("Maria_Martinez","español", 80.20)]

        salida_esperada = [("Jose_Lopez", 99.08),
                           ("Jose_Lopez", 95.37),
                           ("Maria_Martinez", 85.60),
                           ("Maria_Martinez", 80.20)]

        Mock = MagicMock()
        Mock.mostrar.return_value = entrada

        real = Alumnos(Mock)
        self.assertEqual(salida_esperada, real)

    def setUp(self):
        archivo = open("alumnos_test", "w")
        archivo.write("Jose_Lopez quimica 99.08""\nJose_Lopez matematicas 95.37""\nMarta_Martinez fisica 85.60""\nMarta_Martinez español 80.20")

    def tearDown(self):
        os.remove("alumnos_test.txt")

    def test_integration(self):

        salida_esperada = [("Jose_Lopez", 99.08),
                           ("Jose_Lopez", 95.37),
                           ("Maria_Martinez", 85.60),
                           ("Maria_Martinez", 80.20)]

        real = Alumnos(Mock)
        self.assertEqual(salida_esperada, real)

if __name__ == '__main__':
    unittest.main()