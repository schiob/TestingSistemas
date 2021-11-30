import unittest, unittest.mock as mock
from practica4 import calc_prom

test_cases = [
            {
                'name': 'Case 1 ok',
                'input': '10\n20\n30',
                'expected_output': 20,
                'expected_raise': False,
            },
            {
                'name': 'Case 2 ok',
                'input': '10\n20\n30\n10',
                'expected_output': 17.5,
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
                'name': 'Case 5 ok',
                'input': '5\n6\n7\n8',
                'expected_output': 6.5,
                'expected_raise': False
            },
            {
                'name': 'Case 6 error',
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