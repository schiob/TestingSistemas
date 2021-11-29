from typing import Text
import unittest
import builtins
from unittest import result, TestCase, mock
from unittest.mock import patch, mock_open
from parte_2 import escribir_a_pantalla

class test_excribri_patalla(unittest.TestCase):
    @mock.patch("parte_2.escribir",return_value="hola")
    @patch ("builtins.input")
    def test_uno (self,mock_A):
        muck_open.return_value=pruebas[i][0]
        mock_A.called
        self.assertEqual(escribir_a_pantalla(),"hola")
        
        "sin terminar"
if __name__ =='__main__':
 unittest.main()
