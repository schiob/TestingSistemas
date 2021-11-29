from typing import Text
import unittest
import builtins
from unittest import result, TestCase, mock
from unittest.mock import patch, mock_open
from practia_6 import calcular_tarifa
from practia_6 import viajes_disponibles
from practia_6 import siguiente_usuario
from practia_6 import extraer_conductores
from practia_6 import Principal
from textwrap import dedent


class test_principal(unittest.TestCase):
    @mock.patch("practia_6.viajes_disponibles",return_value=[[1, 50], [2, 40], [3, 50], [4, 30]])
    @mock.patch("practia_6.siguiente_usuario",return_value="alo")
    def test_uno (self,mock_A, mock_b):
        mock_A.called
        mock_b.prompt.called
        self.assertEqual(Principal(),[['alo', 'viaje 1'],['alo', 'viaje 2'],['alo', 'viaje 3'],['alo', 'viaje 4']])

class test_principal_21(unittest.TestCase):
    @mock.patch("practia_6.viajes_disponibles",return_value=[[1, 50], [2, 40], [3, 50], [4, 30]])
    def test_principal_viajes_dis (self,mock_A):
        mock_A.called
        self.assertEqual(Principal(),[['Susana', 'viaje 1'],['Luis', 'viaje 2'],['Pepe', 'viaje 3'],['Tom', 'viaje 4']])
        rescribir()
    @mock.patch("practia_6.extraer_conductores")
    def test_ex_co_con (self, mock_response):
        mock_response.return_value = list([['Juan', 3], ['Jesus', 2], ['Maria', 3], ['Toño', 1]])
        self.assertEqual(viajes_disponibles(),[[1, 50], [2, 40], [3, 50], [4, 30]])

class test_principal_22(unittest.TestCase):
    @mock.patch("practia_6.viajes_disponibles",return_value=[[1, 50], [2, 40], [3, 50], [4, 30]])
    def test_principal_viajes_dis (self,mock_A):
        mock_A.called
        self.assertEqual(Principal(),[['Susana', 'viaje 1'],['Luis', 'viaje 2'],['Pepe', 'viaje 3'],['Tom', 'viaje 4']])
        rescribir()
    
    def test_ex_co_sin  (self):
        self.assertEqual(viajes_disponibles(),[[1, 50], [2, 40], [3, 50], [4, 30]])
   
    DATA = dedent("""
       Juan 3
Jesus 2
Maria 3
Toño 1
        """).strip()
    @patch("builtins.open", mock_open(read_data=DATA))
    def test_conductores (self):
        with open("conductores", "r") as f:
           result=f.read()
        open.assert_called_once_with("conductores", "r")
        self.assertEqual(extraer_conductores(),[['Juan', 3], ['Jesus', 2], ['Maria', 3], ['Toño', 1]])
    
    def test_tarifa (self):
        lista= [[1,30],[2,40],[3,50],[4,60],[5,70,],[6,80],[7,90],[8,100]]
        for i in range(0,len(lista),1):
            resultado=calcular_tarifa(int(lista[i][0]))
            self.assertEqual(resultado,lista[i][1])


    
    
        
class test_principal_3(unittest.TestCase):
    @mock.patch("practia_6.siguiente_usuario",return_value="alo")
    def test_uno (self,mock_A):
        mock_A.called
        self.assertEqual(Principal(),[['alo', 'viaje 1'],['alo', 'viaje 2'],['alo', 'viaje 3'],['alo', 'viaje 4']])
    
    DATA = dedent("""
        Tom 4
Susana 2
Andres 10
Pepe 3
Luis 2
        """).strip()
    @patch("builtins.open", mock_open(read_data=DATA))
    def test_uno (self):
        with open("usuarios", "r") as f:
           result=f.read()
        open.assert_called_once_with("usuarios", "r")
        self.assertEqual(siguiente_usuario(),'Susana')

def rescribir():
    file_text= open ("usuario.txt", "a")
    file_text.write("\nPepe 3\nSusana 2\nLuis 2\nTom 4")


if __name__ =='__main__':
 unittest.main()
 rescribir()
 