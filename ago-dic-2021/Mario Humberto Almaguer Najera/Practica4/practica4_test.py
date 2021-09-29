import unittest
from unittest import mock
from unittest.mock import patch, mock_open
from practica4 import calc_prom


class test_practica(unittest.TestCase):

    # @patch("builtins.open", new_callable=mock_open, read_data="90")
    # def test_archivo_encontrado(self, mock_file):
    #     assert open("archivito.txt").read() == "90"
    #     mock_file.assert_called_with("archivito.txt")

    # @patch("builtins.open")
    # def test_segundo(self, open_mock):
    #     open_mock = mock.mock_open(read_data="90")
    #     salida_esperada = open("archivito.txt").read()
    #     self.assertEqual(calc_prom(), salida_esperada)

    # @patch("builtins.open", create=True)
    # def test_tercero(self, mock_open):
    #     mock_open.return_value = "10\n10\n10"
    #     salida_esperada = 10
    #     self.assertEqual(calc_prom(), salida_esperada)

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
                "name": "'El Genio: 100, 100, 100'",
                "input": "100\n100\n100",
                "expected_output": 100,
                "expected_raise": False,

            },
            {
                "name": "'De panzazo: 65, 80, 70'",
                "input": "65\n80\n70",
                "expected_output": 71.67,
                "expected_raise": False,
            },
            {
                "name": "'Dado de baja'",
                "input": "",
                "expected_output": "No hay datos",
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
    print("Hola\npruebas")
