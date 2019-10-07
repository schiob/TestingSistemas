import unittest
import requests
import requestApi
import builtins
from unittest.mock import patch

class RequestTest(unittest.TestCase):
    """docstring for RequestTest."""
    @patch('requests.post')
    #@patch('builtins.print')
    def test_request(self, mock_post):
        test_cases = (
        #entrada, code, salida_real, solo_salida
        ("hola mundo", 400, "ERROR 400", {} ,"error :("),
        ("adios", 200, """{ "INPUT":"adios", "OUTPUT":"ADIOS" }""" ,{ "INPUT":"adios", "OUTPUT":"ADIOS" },"ADIOS")
        )
        for entrada, code, mock_text, mock_dic ,esperado in test_cases:
            #Se envia el codigo para cada prueba
            mock_post.return_value.status_code = code
            mock_post.return_value.text = mock_text
            mock_post.return_value.json = lambda : mock_dic
            salidaReal = requestApi.makePost(entrada)
            self.assertEqual(salidaReal, esperado)






if __name__ == '__main__':
    unittest.main()
