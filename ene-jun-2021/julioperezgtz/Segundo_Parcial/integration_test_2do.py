import unittest
from unittest import mock, TestCase
from unittest.mock import *
from segundo_examen import *


class Test_integration(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="holi")
    def test_mock_solo_open_archivo(self, mock_file):  #solo mock de archivo y los demas reales
        self.assertEqual(convertir('archivo.txt'), "HOLI")
    
    @mock.patch("segundo_examen.upper")
    def test_get_text(self, mock_response): #solo mock de api y los demas reales 
        mock_response.return_value = "MAYUSCULAS"
        response = convertir('archivo.txt')
        self.assertEqual(response, "MAYUSCULAS")
    
    def test_completo(self):
        self.assertEqual(convertir('archivo.txt'), 'HOLA')


if __name__ == '__main__':
    unittest.main()