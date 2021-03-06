import unittest
import SHOUTCLOUDV2
from unittest.mock import patch


class shoutcloudv2(unittest.TestCase):
    @patch('requests.post')
    def test_shout(self, mock_post):
        # entrada-codigo-mockJson-salida
        test_cases = (("hellow", 200, """{ "INPUT":"hellow","OUTPUT":"HELLOW" }""", "HELLOW"),
                      ("adios", 200, """{ "INPUT":"adios","OUTPUT":"ADIOS" }""", "ADIOS"),
                      ("Probando errores", 404, '404 page not found', "error, mensaje: 404 page not found")
                      )

        for entrada, code, mock_text, esperado in test_cases:
            mock_post.return_value.status_code = code
            mock_post.return_value.text = mock_text

            salida_real = SHOUTCLOUDV2.mayus(entrada)
            self.assertSequenceEqual(salida_real, esperado)


if __name__ == '__main__':
    unittest.main()
