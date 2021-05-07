import unittest
from unittest import mock, TestCase
from unittest.mock import *
from segundo_examen import *


class Test(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="Holi")
    def test__leer_archivo(self, mock_file):
        self.assertEqual(leer_archivo('archivo.txt'), "Holi")
    
    @patch('requests.post')
    def test_mock(self, mockpst):
        cases = (   ("marte",   200, """{"INPUT":"marte", "OUTPUT":"MARTE"}""", "MARTE"),
                    ("jupiter", 200, """{"INPUT":"jupiter", "OUTPUT":"JUPITER"}""", "JUPITER"),
                    ("saturno", 404, "404 page not found", "****ERROR****") )
        for inp, st, mocktxt, esp in cases:
            mockpst.return_value.status_code = st
            mockpst.return_value.text = mocktxt
            outpt = upper(inp)
            self.assertSequenceEqual(outpt, esp)
    
    def test_convertir(self):
        convertir = MagicMock()
        convertir.return_value = "JULIO\nCESAR"
        self.assertEqual(convertir("julio\ncesar"), "JULIO\nCESAR")



if __name__ == '__main__':
    unittest.main()