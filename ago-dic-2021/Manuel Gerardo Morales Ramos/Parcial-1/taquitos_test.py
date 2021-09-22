import unittest
from taquitos import calculate_price

class TestTaquitos(unittest.TestCase):
     def test_taquitos(self):
          test_cases = [
            {
                "name": "Case 1 ok",
                "input": "cachete lengua cachete tripitas machito machito machito cachete lengua",
                "expected_output": 110,
                "expected_raise": False,
            },
              {
                "name": "Case 2 ok",
                "input": "cachete lengua cachete",
                "expected_output": 36,
                "expected_raise": False,
            },
              {
                "name": "Case 3 ok",
                "input": "cachete",
                "expected_output": 13,
                "expected_raise": False,
            },
              {
                "name": "Case 4 ok",
                "input": "cachete lengua cachete tripitas machito machito machito cachete lengua pastor machito",
                "expected_output": 139,
                "expected_raise": False,
            },
              {
                "name": "Case 5 fail",
                "input": " ",
                "expected_output": 110,
                "expected_raise": True,
            },
            {
                "name": "Case 6 fail",
                "input": 1,
                "expected_output": 110,
                "expected_raise": True,
            },
             {
                "name": "Case 7 fail",
                "input": "cachete lengua cachete tripitas machito machito machito cachete lengua pastor machito cachete lengua cachete tripitas machito machito machito cachete lengua pastor machito cachete lengua cachete tripitas machito machito machito cachete lengua pastor machito",
                "expected_output": 110,
                "expected_raise": True,
            },
              {
                "name": "Case 8 fail",
                "input": "asdasdas",
                "expected_output": 110,
                "expected_raise": True,
            },
          ]

          for tc in test_cases:
            if tc["expected_raise"]:
                self.assertRaises(Exception, calculate_price, tc["input"])
            else:
                input = str(tc["input"]).split(" ")
                self.assertEqual(tc["expected_output"], calculate_price(input))

if __name__ == '__main__':
    unittest.main()