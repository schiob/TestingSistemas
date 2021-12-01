from os import read
from unittest import TestCase, mock
from unittest.mock import patch, mock_open
from practica4 import calc_prom

class Test_practica4(TestCase):
    def test_archivo1(self):
        read_data = '5\n5\n5\n5'
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada = 5
        
        with mock.patch('builtins.open', mock_open):
            resultado = calc_prom()
        
        self.assertEqual(salida_esperada, resultado)

    def test_archivo_vacio(self):
        read_data = ''
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada = 'El archivo está vacío.'
        
        with mock.patch('builtins.open', mock_open):
            resultado = calc_prom()
        
        self.assertEqual(salida_esperada, resultado)

