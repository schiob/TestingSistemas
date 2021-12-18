import unittest
from unittest import mock
from unittest.mock import patch, mock_open
from funcion import calc_prom


class test_practica(unittest.TestCase):

    def test_practica(self):
        read_data = "100\n100"
        mock_open = mock.mock_open(read_data=read_data)
        salida_esperada = 100
        with mock.patch('builtins.open', mock_open):
            result = calc_prom()
        self.assertEqual(salida_esperada, result)

    def test_practica(self):
        test_cases = [
            {
                "name": "Puros cienes",
                "input": "100\n100\n100",
                "expected_output": 100,
                "expected_raise": False,

            },
            {
                "name": "Por poco y no la hace",
                "input": "65\n58\n100",
                "expected_output": 74.33,
                "expected_raise": False,
            },
            {
                "name": "El archivo esta vacio",
                "input": "",
                "expected_output": "Porfavor ingresa datos",
                "expected_raise": False
            }
        ]

        for tc in test_cases:
            if tc["expected_raise"]:
                self.assertRaises(Exception, calc_prom)
            else:
                read_data = tc["input"]
                mock_open = mock.mock_open(read_data=read_data)
                with mock.patch('builtins.open', mock_open):
                    resultado = calc_prom()
                self.assertEqual(resultado, tc["expected_output"], msg="Falla en el test {}, entrada {}, salida esperada {}, salida real {}".format(
                    tc["name"], tc["input"], tc["expected_output"], resultado))


if __name__ == "__main__":
    unittest.main()