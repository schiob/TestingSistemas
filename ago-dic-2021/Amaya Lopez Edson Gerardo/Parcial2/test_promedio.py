from unittest import TestCase, mock
from unittest.mock import patch,mock_open
from promedio import promedio

class TestPromedio(TestCase):
    def test_con_datos(self):
        read_data ='Jose_Lopez matematicas 80.00\nJose_Lopez testing 80.00\nJose_Lopez quimica 80.00'
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada= 80.00
        with mock.patch("builtins.open", mock_open):
            result = promedio()
        self.assertEqual(salida_esperada, result)

    def test_con_datos2(self):
        read_data ='Jose_Lopez quimica 70.00\nJose_Lopez quimica 85.00\nJose_Lopez quimica 90.00'
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada= 70.00
        with mock.patch("builtins.open", mock_open):
            result = promedio()
            print(result)
        self.assertEqual(salida_esperada, result)

    def test_sin_datos(self):
        read_data = ''
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada= 'el alumno no tiene calificaciones'
        with mock.patch("builtins.open", mock_open):
            result = promedio()
        self.assertEqual(salida_esperada, result)