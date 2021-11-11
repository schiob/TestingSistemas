import unittest
from unittest.mock import patch
from Parcial2Pt2 import InsertarTexto


class TestPromedio(unittest.TestCase):
    @patch('Parcial2Pt2.InsertarTexto.enImagen')
    def test_con_datos(self,mock_imagen):
        mock_imagen.return_value='usamos python para esto :)'

        imagen= InsertarTexto.enImagen()
        self.assertEqual(InsertarTexto.enImagen(),imagen)


if __name__ == '__main__':
    unittest.main()