from os import read
import unittest
from unittest import mock
from unittest.case import TestCase
from unittest.mock import patch, mock_open
from Parcial2Pt1 import leerArch

class promedios_test(unittest.TestCase):

    def test_promedios(self):
        casos = [
            {
                "name": "Prueba 2 datos del ejemplo",
                "input": "Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez español 90.00",
                "expected_output": "Jose_Lopez 87.17\nMaria_Martinez 92.75",
                "expected_raise": False,            
            },
            {
                "name": "Prueba 3 sin datos",
                "input": "",
                "expected_output": "No hay datos",
                "expected_raise": False,            
            },
            {
                "name": "Prueba 4 datos negativos",
                "input": "yomerongo espanol -100\nyomerongo mate -85",
                "expected_output": "yomerongo 92.5",
                "expected_raise": False,            
            }
            
        ]

        for tc in casos:
            if tc["expected_raise"]:
                self.assertRaises(Exception, leerArch)
            else:
                read_data = tc["input"]
                mock_open = mock.mock_open(read_data=read_data)
                with mock.patch('builtins.open', mock_open):
                    res = leerArch()
                self.assertEqual(res, tc["expected_output"])


if __name__ == '__main__':
    unittest.main()