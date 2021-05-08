import unittest
import Parcial_2
from unittest.mock import patch
from Parcial_2 import Funcion_2

class TestMock(unittest.TestCase):
   @patch('requests.post')
   def test(self, mockpost):
        TestCases = (("hola mundo", """{ "INPUT":"hola mundo","OUTPUT":"HOLA MUNDO" }"""),
                      ("adios mundo", """{ "INPUT":"adios mundo","OUTPUT":"ADIOS MUNDO" }"""),
                      ("error", '404 page not found')
                      )
        for entrada, mocktext  in TestCases:
            mockpost.return_value.text = mocktext
            salida = Parcial_2.Funcion_2(entrada)
            self.assertSequenceEqual(salida,mocktext)

if __name__ == '__main__':
    unittest.main()