import unittest
import os
from unittest.mock import MagicMock
from ParcialDos import File, promedio

class TestFile(unittest.TestCase):

    def setUp(self):
        with open('C:/Users/Skynet-Gold/Desktop/mi_repo/TestingSistemas/ago-dic-2020/mariacastro/practicas/segundoParcial/calificaciones.txt', "w") as f:
            f.write("Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez espanol 90.00")
        self.file = File("calificacionespruebas.txt")

    def eliminar(self):
        os.remove("calificacionespruebas.txt")

    def testReader(self):
        entrada = ['Jose_Lopez quimica 89.00\n', 'Jose_Lopez matematicas 85.34\n', 'Maria_Martinez fisica 95.50\n', 'Maria_Martinez espanol 90.00\n']
        salida_esperada = {'Jose_Lopez': 87.17, 'Maria_Martinez': 92.75}

        fileMock = MagicMock()
        fileMock.reader.return_value = entrada

        real = promedio(fileMock)
        self.assertEqual(salida_esperada, real)

    def test_integration(self):
        salida_esperada = {'Jose_Lopez': 87.17, 'Maria_Martinez': 92.75}

        real = promedio(self.file)
        self.assertEqual(salida_esperada, real)

if __name__ == "__main__":
    unittest.main()