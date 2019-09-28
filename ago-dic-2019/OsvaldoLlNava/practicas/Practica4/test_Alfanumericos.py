import unittest
from unittest.mock import patch
import Alfanumericos
"""
def Quitar_especiales(direccion):
    archivo = open(direccion, "r")
    texto = archivo.read()
    archivo.close()
    cadena=''

    for i in range(0,len(texto)):
        if texto[i].isalnum() or texto[i]=='\n' or texto[i]==' ':
            cadena = cadena + texto[i]

    cadena = cadena.lower()

    return cadena
    """

def Func():
    return 'prueba'

class test(unittest.TestCase):

    def test_vacio(self):
        ruta='vacio.txt'
        self.assertEqual(Alfanumericos.Quitar_especiales(ruta),'')

    def test_sinquitar(self):
        ruta='sinquitar.txt'
        self.assertEqual(Alfanumericos.Quitar_especiales(ruta),'fuego123 y arroz')

    def test_quitar(self):
        ruta='quitar.txt'
        self.assertEqual(Alfanumericos.Quitar_especiales(ruta),'fuego123 y arroz')

   # @patch('builtins.open')
   # def test_leer(self, mock_open):
    #    mock_open.return_value.read = Func
   #     res = Alfanumericos.Quitar_especiales('test.txt')
   #     self.assertEqual(res,'prueba')
   #     mock_open.assert_called_with('test.txt','r')

    @patch('builtins.open')
    def test_leer(self, mock_open):
        mock_open.return_value.read.return_value = 'textito'
        res = Alfanumericos.Quitar_especiales('test.txt')
        self.assertEqual(res,'textito')
    


if __name__ == '__main__':
    unittest.main()