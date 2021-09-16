import unittest
from practica3 import numbers_summary

class TestPractica3(unittest.TestCase):
    def test_numbers(self):
        test_cases = [
            {
                "name": "Case 1 ok",
                "input": "51 -12 -3 0 2",
                "expected_output": "2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)",
                "expected_raise": False,
            },
             {
                "name": "Case 2 ok",
                "input": "0 1 2 3 4",
                "expected_output": "4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)",
                "expected_raise": False,
            },
             {
                "name": "Case 3 ok",
                "input": "-1 -2 -3",
                "expected_output": "0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)",
                "expected_raise": False,
            },
             {
                "name": "Case 4 ok",
                "input": "0",
                "expected_output": "0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)",
                "expected_raise": False,
            },
             {
                "name": "Case 5 error",
                "input": "aeiou",
                "expected_output": "0 número(s) positivo(s)\n0 número(s) negativo(s)\n0 número(s) par(es)\n0 número(s) impar(es)",
                "expected_raise": True,
            },
             {
                "name": "Case 6 error",
                "input": " ",
                "expected_output": "0 número(s) positivo(s)\n0 número(s) negativo(s)\n0 número(s) par(es)\n0 número(s) impar(es)",
                "expected_raise": True,
            },
        ]
        
        for tc in test_cases:
            if tc["expected_raise"]:
                self.assertRaises(Exception, numbers_summary, tc["input"])
            else:
                input = str(tc["input"]).split(" ")
                self.assertEqual(tc["expected_output"], numbers_summary(input))

if __name__ == '__main__':
    unittest.main()