from practica4_Main import obtenerPromedios,abrirArchivo,personas
import unittest
from unittest.mock import patch, MagicMock
from unittest import mock

class testMockPractica4(unittest.TestCase):
 pruebaMock={"test1":[personas('juanito','hotmail.com',90.0),personas('pedro','gmail.com',24.0),personas('julio','hotmail.com',90.0),personas('panchito','hotmail.com',90.0),personas('juannito','gmail.com',24.0),personas('andres','gmail.com',24.0)]}
 @patch('practica4_Main.abrirArchivo',return_value=pruebaMock['test1'])
 def test_pruebaMock(self,mock_get):
     resultado_esperado={'hotmail.com':90.0,'gmail.com':24.0}
     resultado_actual=obtenerPromedios("mock")
     assert resultado_esperado==resultado_actual
     

if __name__ == "__main__":
    unittest.main()