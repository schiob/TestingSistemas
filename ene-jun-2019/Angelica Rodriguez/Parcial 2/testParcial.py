import unittest
import os
from unittest.mock import MagicMock
from parcialDos import showAlumnos, Alumno, Archivo

class TestAlumnos(unittest.TestCase):
    def setUp(self):
        self.archivo = Archivo("datosAlumnos.txt")
        self.archivo.guardarAlumno(Alumno("Jose_Lopez quimica 89.00"))
        #self.archivo.guardarAlumno(Alumno("Jose_Lopez", "matematicas", 85.34))

    def tearDown(self):
        os.remove("datosAlumnos.txt")

    def testShowAll(self):
        entrada = "Jose_Lopez quimica 89.00\nJose_Lopez quimica 89.00"
        salida_esperada = "Jose_Lopez quimica 89.00\nJose_Lopez quimica 89.00"

        dbMock = MagicMock()
        dbMock.getSalida.return_value = entrada

        real = showAlumnos(dbMock)
        self.assertEqual(salida_esperada, real)

    #def test_integration(self):
    #    salida_esperada = "Jose_Lopez quimica 89.00\nJose_Lopez quimica 89.00"
    #    real = showAlumnos(self.archivo)
    #    self.assertEqual(salida_esperada, real)

if __name__ == "__main__":
    unittest.main()
