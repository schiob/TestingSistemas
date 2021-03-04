import unittest
from foaas import saludar
from unittest.mock import patch, MagicMock

class TestFoaas(unittest.TestCase):
    @patch("requests.get")
    def test_saludo(self, mock_get):
        mi_response_magico = MagicMock()
        mi_response_magico.text = "This is Fucking Awesome. - Chio"

        mock_get.return_value = mi_response_magico
        actual = saludar("Chio")

        self.assertEqual(actual, "This is Fucking Awesome. - Chio")


if __name__ == "__main__":
    unittest.main()