import unittest
from holi import foo

class TestAB(unittest.TestCase):
    def test_suma(self):
        test_cases = (
            {
                "entrada_a": 5, 
                "entrada_b": 24, 
                "salida_esperada": 29,
                "error": False,
            },
            {
                "entrada_a": -2, 
                "entrada_b": 24, 
                "salida_esperada": 22,
                "error": False,
            },
            {
                "entrada_a": -6, 
                "entrada_b": -2, 
                "salida_esperada": -8,
                "error": False,
            },
            {
                "entrada_a": "cosas", 
                "entrada_b": "malas", 
                "salida_esperada": "",
                "error": True,
            },
        )

        for tc in test_cases:
            if tc["error"]:
                with self.assertRaises(Exception):
                    foo(tc["entrada_a"], tc["entrada_b"])
            else:
                salida_real = foo(tc["entrada_a"], tc["entrada_b"])
                self.assertEqual(salida_real, tc["salida_esperada"])

if __name__ == '__main__':
    unittest.main()