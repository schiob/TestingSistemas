import unittest
from unittest.mock import patch
import request

class TestRequest(unittest.TestCase):
    @patch("requests.post")
    def test_request(self, post_mock):
        tc = (
            # entrada, mock.code, mock.text, esperada
            ("holi", 404, '404 page not found', {}, "error, mensaje: 404 page not found"),
            ("holi", 200, """{ "INPUT":"holi","OUTPUT":"HOLI" }""", {"INPUT":"holi","OUTPUT":"HOLI"}, "HOLI"),
            ("que onda clase", 200, """{ "INPUT":"que onda clase","OUTPUT":"QUE ONDA CLASE" }""", {"INPUT":"que onda clase","OUTPUT":"QUE ONDA CLASE"}, "QUE ONDA CLASE"),
            ("HOLI", 200, """{ "INPUT":"HOLI","OUTPUT":"HOLI" }""", {"INPUT":"HOLI","OUTPUT":"HOLI"}, "HOLI")
        )

        for entrada, code, mock_text, mock_dic, esperada in tc:
            post_mock.return_value.status_code = code
            post_mock.return_value.text = mock_text
            post_mock.return_value.json = lambda : mock_dic

            salida_real = request.ToUpper(entrada)
            self.assertEqual(salida_real, esperada)

if __name__ == "__main__":
    unittest.main()