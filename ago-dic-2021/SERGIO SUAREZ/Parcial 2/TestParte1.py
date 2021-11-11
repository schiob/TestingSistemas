from unittest import TestCase, mock
from unittest.mock import patch,mock_open
from parte1 import average

class TestPromedio(TestCase):
    def test(self):
        read_data ='Edgar_Padilla Programacion 80.00\nEdgar_Padilla Matematicas 90.00\nEdgar_Padilla Redes 70.00'
        mock_open = mock.mock_open(read_data=read_data)
        expected_output= 80.00
        with mock.patch("builtins.open", mock_open):
            result = average()
        self.assertEqual(expected_output, result)

    def test2(self):
        read_data ='Edgar_Padilla Programacion 100.00\nEdgar_Padilla Matematicas 65.00\nEdgar_Padilla Redes 85.00'
        mock_open = mock.mock_open(read_data=read_data)
        expected_output= 83.33
        with mock.patch("builtins.open", mock_open):
            result = average()
            print(result)
        self.assertEqual(expected_output, result)

    def test3(self):
        read_data = ''
        mock_open = mock.mock_open(read_data=read_data)
        expected_output= 'No hay registros'
        with mock.patch("builtins.open", mock_open):
            result = average()
        self.assertEqual(expected_output, result) 