import SegundaParte
import unittest
from unittest.mock import patch

from SegundaParte.SegundaParte import *
class SegundaParteTest(unittest.TestCase):

    @patch('SegundaParte.Escritor.escribir')
    def test_implementacion(self, mock_implementacion):
        mock_implementacion.return_value = '15'

        imp = Implementacion()

        res = imp.escribir()

        self.assertEqual(imp.escribir, res)

if __name__ == '__main__':
    unittest.main()
