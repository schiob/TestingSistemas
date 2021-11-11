import unittest
from unittest.mock import patch
from implementacion import Escribir


class TestPromedio(unittest.TestCase):
    @patch('implementacion.Escribir.escribir_cantidad_vocales')
    def test_con_datos(self,mock_vocal):
        mock_vocal.return_value='2'

        vocal= Escribir.escribir_cantidad_vocales()
        self.assertEqual(Escribir.escribir_cantidad_vocales(),vocal)


if __name__ == '__main__':
    unittest.main()
