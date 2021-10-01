from unittest import TestCase, mock
from unittest.mock import patch,mock_open
from promedio import calc_prom



class TestPromedio(TestCase):



    def test_con_datos(self):
        read_data ='20\n20\n20'
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada= 20
        with mock.patch("builtins.open", mock_open):
            result = calc_prom()
        self.assertEqual(salida_esperada, result)


    def test_sin_datos(self):
        read_data = ''
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada= 'no existen datos en el archivo'
        with mock.patch("builtins.open", mock_open):
            result = calc_prom()
        self.assertEqual(salida_esperada, result)


    def test_datos_con_letras(self):
        read_data = '2\n4\n4'
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada= 3.3333333333333335
        with mock.patch("builtins.open", mock_open):
            result = calc_prom()
        self.assertEqual(salida_esperada, result)


