import unittest
from  unittest import mock
from practica4 import calc_prom

test_cases = [
            {
                'name': 'Case 1 ok',
                'input': '10\n20\n30',
                'expected_output': 60,
                'expected_raise': False,
            },
            {
                'name': 'Case 2 ok',
                'input': '10\n20\n30\n10',
                'expected_output': 70,
                'expected_raise': False,
            },
             {
                'name': 'Case 3 ok',
                'input': '10',
                'expected_output': 10,
                'expected_raise': False,
            },
             {
                'name': 'Case 4 ok',
                'input': '',
                'expected_output': 0,
                'expected_raise': False,
            },
             {
                'name': 'Case 5 error',
                'input': 'refe',
                'expected_output': 0,
                'expected_raise': True,
            },
    ]
class TestPractica4(unittest.TestCase):
    def test_archivito(self):
        for test in test_cases:
            if test["expected_raise"]:
                self.assertRaises(Exception, calc_prom, test["input"])
            else:
                mock_open = mock.mock_open(read_data=test['input'])
                with mock.patch('builtins.open', mock_open):
                    result = calc_prom()
                self.assertEqual(test['expected_output'], result)

if __name__ == '__main__':
    unittest.main()