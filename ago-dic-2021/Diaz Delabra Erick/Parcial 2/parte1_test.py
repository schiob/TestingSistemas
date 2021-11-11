import unittest
from unittest import TestCase
from unittest.mock import mock_open, patch
from parte1 import *
from unittest import mock

class test_parte1(unittest.TestCase):
    def test1_normal(self): 
        nuevoMock = ""
        nuevoMock = """Erick_Days Programacion 90.00
Erick_Days Quimica 96.00
Susan_Flowers Quimica 100.00
Susan_Flowers Redes 70.00""" #datos nuevos

        archivo = mock_open(read_data=nuevoMock) # creamos archivo con los datos nuevos
        esperado = ['Erick_Days 93.0', 'Susan_Flowers 85.0'] #salida esperada

        with patch('builtins.open', archivo): 
            mockenviar = calcular_promedio() #valores que mmandaremos ya con nuestro mock
            
        self.assertEqual(mockenviar, esperado)

    def test2_ERROR_en_PROMEDIO(self): 
        nuevoMock = ""
        nuevoMock = """Erick_Days Programacion 92.00 
Erick_Days Quimica 70.32
Susan_Flowers Quimica 78.00
Susan_Flowers Redes 71.22""" #datos nuevos

        archivo = mock_open(read_data=nuevoMock) # creamos archivo con los datos nuevos
        esperado = ['Erick_Days 67.0', 'Susan_Flowers 60.0'] #salida esperada
        with patch('builtins.open', archivo): 
            mockenviar = calcular_promedio() #valores que mmandaremos ya con nuestro mock
        self.assertEqual(mockenviar, esperado)

    def test3_decimales(self): 
        nuevoMock = ""
        nuevoMock = """Erick_Days Programacion 50.5
Erick_Days Quimica 96.78
Susan_Flowers Quimica 56.16
Susan_Flowers Redes 89.14""" #datos nuevos

        archivo = mock_open(read_data=nuevoMock) # creamos archivo con los datos nuevos
        esperado = ['Erick_Days 73.64', 'Susan_Flowers 72.65'] #salida esperada
        with patch('builtins.open', archivo): 
            mockenviar = calcular_promedio() #valores que mmandaremos ya con nuestro mock
        self.assertEqual(mockenviar, esperado)

    def test4_PERFECTO(self): 
        nuevoMock = ""
        nuevoMock = """Erick_Days Programacion 100.00 
Erick_Days Quimica 100.00
Susan_Flowers Quimica 100.00
Susan_Flowers Redes 100.00""" #datos nuevos

        archivo = mock_open(read_data=nuevoMock) # creamos archivo con los datos nuevos
        esperado = ['Erick_Days 100.0', 'Susan_Flowers 100.0'] #salida esperada
        with patch('builtins.open', archivo): 
            mockenviar = calcular_promedio() #valores que mmandaremos ya con nuestro mock
        self.assertEqual(mockenviar, esperado)

if __name__ == '__main__':
    unittest.main() 