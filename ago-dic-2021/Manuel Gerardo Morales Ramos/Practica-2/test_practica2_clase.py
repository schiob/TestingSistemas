import unittest
from practica2 import sum

class TestPractica2Clase(unittest.TestCase):
     def test_sum(self):
        test_cases = [
            {
                "name": "Two positive integers",
                "input": [4, 6],
                "expected_output": 10,
                "expected_raise": False,
            },
             {
                "name": "Two negative integers",
                "input": [-4, -6],
                "expected_output": -10,
                "expected_raise": False,
            },
             {
                "name": "Both zeros",
                "input": [0, 0],
                "expected_output": 0,
                "expected_raise": False,
            },
             {
                "name": "First number negative",
                "input": [-1, 1],
                "expected_output": 0,
                "expected_raise": False,
            },
             {
                "name": "Second number negative",
                "input": [1, -1],
                "expected_output": 0,
                "expected_raise": False,
            },
             {
                "name": "Both floats numbers",
                "input": [0.1, 0.2],
                "expected_output": 0.3,
                "expected_raise": False,
            },
           
        ]

        for tc in test_cases:
            if tc["expected_raise"]:
                self.assertRaises(Exception, sum, tc["input"][0], tc["input"][1])
            else:
                result = round(sum(tc["input"][0], tc["input"][1]), 2)
                self.assertEqual(result, tc["expected_output"], msg="Falla en el test {}, entrada {}, salida esperada {}, salida real {}".format(tc["name"], tc["input"], tc["expected_output"], result)) 

if __name__ == '__main__':
    unittest.main()