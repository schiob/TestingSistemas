import unittest
import Request
from unittest.mock import patch
from Request import pag

class TestMock(unittest.TestCase):
   @patch('requests.post')
   def test(self, mockpost):
        TestCases = (("hola mundo", """{ "INPUT":"hola mundo","OUTPUT":"HOLA MUNDO" }"""),
                      ("adios mundo", """{ "INPUT":"adios mundo","OUTPUT":"ADIOS MUNDO" }"""),
                      ("error", '404 page not found')
                      )
        for entrada, mocktext  in TestCases:
            mockpost.return_value.text = mocktext
            salida = Request.pag(entrada)
            self.assertSequenceEqual(salida,mocktext)

if __name__ == '__main__':
    unittest.main()