from promedio import calc_prom
from os import read
import unittest
from unittest import mock
from unittest.case import TestCase
from unittest.mock import patch, mock_open


class calc_prom_test(unittest.TestCase):

    def test_calc_prom(self):
        cases = [
            {
                "name": "Prom1",
                "input": "Maria_Martinez fisica 95.50\nMaria_Martinez español 90.00",
                "expected_output": "Maria_Martinez 92.75",
                "expected_raise": True,
            },
            {
                "name": "Prom2",
                "input": "Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34",
                "expected_output": "Jose_Lopez 87.17",
                "expected_raise": True,  
            },
            {   
                "name": "Prom_Negativo",
                "input": "Juanito_Banana Matematicas -95.00\nJuanito_Banana Historia 50.63",
                "expected_output": "Juanito_Banana -44.37",
                "expected_raise": True,
            },
            {
                "name": "Prom_Erroneo",
                "input": "Juanito_Banana Matematicas 75.00\nJuanito_Banana Historia 50.63",
                "expected_output": "Juanito_Banana 50",
                "expected_raise": False,
            }
            
        ]

        for test_case in cases:
            if test_case["expected_raise"]:
                self.assertRaises(Exception, calc_prom)
            else:
                read_data = test_case["input"]
                mock_open = mock.mock_open(read_data=read_data)
                with mock.patch('builtins.open', mock_open):
                    res = calc_prom()
                self.assertEqual(res, test_case["expected_output"])


if __name__ == '__main__':
    unittest.main()