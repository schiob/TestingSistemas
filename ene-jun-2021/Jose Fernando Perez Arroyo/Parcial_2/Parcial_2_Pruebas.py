import unittest
import requests

import builtins
from unittest.mock import patch
from Parcial_2 import *

class RequestTest(unittest.TestCase):
    
    @patch('requests.post')
    def test_request(self, mock_post):
        test_cases = (
        ("El archivito no estaba pero mientras ve este bonito perrito:", 200,
        """{ "INPUT":"adios", "OUTPUT":"ADIOS" }""" ,
        { "INPUT":"El archivito no estaba pero mientras ve este bonito perrito:", 
        "OUTPUT":"El archivito no estaba pero mientras ve este bonito perrito:" },
        "El archivito no estaba pero mientras ve este bonito perrito:")
        )
        for entrada, code, mock_text, mock_dic ,esperado in test_cases:
            #Se envia el codigo para cada prueba
            mock_post.return_value.status_code = code
            mock_post.return_value.text = mock_text
            mock_post.return_value.json = lambda : mock_dic
            salidaReal = requestApi.makePost(entrada)
            self.assertEqual(salidaReal, esperado)

    def test_unico(self):
        datop1="algo x"
        p1=check(datop1)
        self.assertEqual(p1, "El archivito no estaba pero mientras ve este bonito perrito:no se que onda con el perro jajaj")
    def test_get(self):
        datosg= "hola a todos"
        p2=get_url(datosg)
        self.assertEqual(p2, "HOLA A TODOS") 
    def com(self):
        name="doge.txt"
        p3=compilado(name)
        self.assertEqual(p3, "EL ARCHIVITO NO ESTABA PERO MIENTRAS VE ESTE BONITO PERRITO:")
if __name__ == "__main__":
    unittest.main()