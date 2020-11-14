from unittest import mock
import unittest
from unittest.mock import patch,MagicMock
from segundoparcialapp import leer_prom_alumno


class test_Mock_segundo_parcial(unittest.TestCase):
    def test_Uno(self):
        resultadoEsperado={'pepito': 61.995000000000005, 'maria': 83.66499999999999}
        read_data='pepito mate 34.65\nmaria espanol 78.99\npepito quimica 89.34\nmaria mate 88.34'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=leer_prom_alumno('filename')
        self.assertEqual(resultadoEsperado,result)

    def test_Dos(self):
        resultadoEsperado={'juanito': -62.325, 'pedrito': -83.485}
        read_data='juanito mate -56.77\npedrito espanol -99.99\njuanito quimica -67.88\npedrito mate -66.98'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=leer_prom_alumno('filename')
        self.assertEqual(resultadoEsperado,result)

    def test_Tres(self):
        resultadoEsperado={'juanito': 0, 'pedrito': 0}
        read_data='juanito mate 0\npedrito espanol 0\njuanito quimica 0\npedrito mate 0'
        mock_open=mock.mock_open(read_data=read_data)
        with mock.patch('builtins.open',mock_open):
            result=leer_prom_alumno('filename')
        self.assertEqual(resultadoEsperado,result)


if __name__ == "__main__":
    unittest.main()