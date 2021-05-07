import unittest
import requests
from practica4 import pedido
from unittest.mock import patch, MagicMock

class testRequests(unittest.TestCase):

    @patch('requests.post')
    def testRequest (self , mock_post):

        cosa_magica = MagicMock()
        
        casos = (
            ["jaja saludos equisdee", """{ "INPUT":"jaja saludos equisdee","OUTPUT":"JAJA SALUDOS EQUISDEE" }"""],
            ["Si jalo el test?", """{ "INPUT":"Si jalo el test?","OUTPUT":"SI JALO EL TEST?" }"""],
            ["456", """{ "INPUT":"456","OUTPUT":"456" }"""]
        )
        
        for x in casos:

            cosa_magica.text = pedido(1)
            mock_post.return_value = cosa_magica

            self.assertEquals(pedido(0), pedido(1))

if __name__ == "__main__":
    unittest.main()