import unittest
from unittest.mock import patch
from saludo import saludo
from unittest.mock import MagicMock



class TestSaludo(unittest.TestCase):
    @patch("builtins.input")
    def test_saludo(self, mock_input):
        test_cases = (
            {
                "entrada": "Erick",
                "user_input": [[123], [456]],
                "salida_esperada": "hola Erick Perez",
            },
        )

        for cp in test_cases:
            def func():
                return cp["user_input"]
            mock_input.return_value = MagicMock()
            mock_input.return_value.values = MagicMock()
            mock_input.return_value.values.tolist = func

            salida_real = saludo(cp["entrada"])
            self.assertEqual(salida_real, cp["salida_esperada"])

if __name__ == "__main__":
    unittest.main()