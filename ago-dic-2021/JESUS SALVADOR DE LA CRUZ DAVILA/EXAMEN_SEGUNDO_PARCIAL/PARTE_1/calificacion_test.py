import builtins
import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import mock_open, patch
from calificacion import *


class CalificacionesTest(unittest.TestCase):
    def test_calificacion(self):
        datos = 'Jesus_davila geografia 70.00\nJesus_davila quimica 70.00\nJesus_davila fisica 70.00'
        mock_calificaciones = mock.mock_open(read_data=datos)
        salida = 70.00
        with mock.patch('builtins.open', mock_calificaciones):
            prueba = Alumnos()
            self.assertEqual(prueba.alumno(), salida)

    def test_no_tiene_datos(self):
        datos = 'Jesus_davila geografia 0.00\nJesus_davila quimica 0.00\nJesus_davila fisica 0.00'
        mock_calificaciones = mock.mock_open(read_data=datos)
        salida = 0.0
        with mock.patch('builtins.open', mock_calificaciones):
            prueba = Alumnos()
            self.assertEqual(prueba.alumno(), salida)

    def test_calificaciones_diferentes(self):
        datos = 'Jesus_davila geografia 70.00\nJesus_davila quimica 80.00\nJesus_davila fisica 90.00'
        mock_calificaciones = mock.mock_open(read_data=datos)
        salida = 70.00
        with mock.patch('builtins.open', mock_calificaciones):
            prueba = Alumnos()
            self.assertEqual(prueba.alumno(), salida)


if __name__ == '__main__':
    unittest.main()
