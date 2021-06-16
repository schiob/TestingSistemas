import unittest
from unittest.mock import *
from regalo_mas_caro import *

class tests(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='''controlRemoto 450.00
hamburguesa 90.00
Switch 6999.99
tarjetaRegalo 500.00
PixelCelular 15000.00
''')
    def test_modulo_1(self, mock_file):
        self.assertEqual(funcion_principal(mock_file),"Switch")
    
    @patch('builtins.open', new_callable=mock_open, read_data='''controlRemoto 450.00
hamburguesa 90.00
Switch 199.99
tarjetaRegalo 500.00
PixelCelular 15000.00
''')
    def test_modulo_1_numero_2(self, mock_file):
        self.assertEqual(funcion_principal(mock_file),"tarjetaRegalo")

    @patch('builtins.open', new_callable=mock_open, read_data='''''')
    def test_modulo_1_numero_3(self, mock_file):
        self.assertEqual(funcion_principal(mock_file),"El tamaño del archivo no esta dentro de los requerimentos")

if __name__ == '__name__':
    unittest.main()