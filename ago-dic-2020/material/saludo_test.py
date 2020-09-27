import unittest
from unittest.mock import patch
from saludo import saludo

class TestSaludo(unittest.TestCase):
    @patch("builtins.input")
    def test_saludo(self, mock_input):
        test_cases = (
            {
                "entrada": "Erick",
                "user_input": "Perez",
                "salida_esperada": "hola Erick Perez",
            },
        )

        for cp in test_cases:
            mock_input.return_value = cp["user_input"]
            salida_real = saludo(cp["entrada"])
            self.assertEqual(salida_real, cp["salida_esperada"])

if __name__ == "__main__":
    unittest.main()