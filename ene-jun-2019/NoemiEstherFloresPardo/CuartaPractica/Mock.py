import unittest
import Request
from unittest.mock import patch
import requests

class MockTest(unittest.TestCase):

    @patch('requests.post')
    def test_mock(self, mock_post):
        test_cases = (("no", 200, """{ "INPUT":"no", "OUTPUT":"NO" }""","NO"),
                      ("azul", 200, """{ "INPUT":"azul", "OUTPUT":"AZUL" }""", "AZUL"),
                      ("asd", 404, '404 page not found', "error"))

        for entrada, stat, mock_text, esperado in test_cases:
            mock_post.return_value.status_code = stat
            mock_post.return_value.text = mock_text
            salida_real = Request.getOutput(entrada)
            self.assertEqual(salida_real, esperado)

if __name__ == "__main__":
    unittest.main()