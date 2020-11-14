from io import StringIO
from os import readlink
from unittest import TestCase
from unittest.mock import mock_open, patch, Mock
from parcial import *


# @patch("builtins.open")
# def test_open(self, MockOpen):
#     mockk = MockOpen
#     mockk.return_value = ["juan_johnny quimica 89.00\n juan_johnny matematicas 85.34\n juan_alberto fisica 95.50\n juan_alberto español 90.00"]
#     esperado = ["juan_johnny quimica 89.00\n juan_johnny matematicas 85.34\n juan_alberto fisica 95.50\n juan_alberto español 90.00"]
#     real = open_file("archivo.txt")
#     self.assertEqual(esperado, real)


# # @patch("builtins.open", new_callable=mock_file, read_data="data")
# # def test_openfileee(mock_file):
# #     assert open("archivo.txt").read() == "data"
# #     mock_file.assert_called_with("archivo.txt")

# def test_otro(self):
#     with mock_open.patch('parcial.open_file.open') as mocked_open:
#         mocked_open.return_value = StringIO('foo')
#         esperado = 'foo'
#         real = open_file("archivo.txt")
#         self.assertEqual(esperado, real)

# def test_open_file1(self):
#     pass

# @mock.patch("parcial.open", return_value = 5, autospec=True)
# def test_mock(self, MockLoco):
#     data
#     operacioncita = MockLoco
#     operacioncita.return_value = 99
#     esperado = 99
#     real = calcula_promedio(data)
#     self.assertEqual(esperado, real)

#     def test_multiplicacion(self, MockMulti):
#         operacioncita = MockMulti
#         operacioncita.return_value = 99
#         #response = sumaloca.suma
#         esperado = 99
#         a = Operaciones()
#         real = a.multiplicacion("gatos", "perros")
#         self.assertEqual(esperado, real)

def test_open_file_9999():
    esperado = ['johnny_nazco quimica 75.00', 'johnny_nazco matematicas 75.34', 'luisillo_pillo fisica 95.50', 'luisillo_pillo espaÃ±ol 90.00']
    real = open_file("otroarchivo.txt")
    assert(esperado, real)