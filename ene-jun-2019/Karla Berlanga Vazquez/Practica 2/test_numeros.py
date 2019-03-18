import unittest
import numeros

class TestNumeros(unittest.TestCase):
    def test_clasificacion(self):
        test_cases=(
        ("51 -12 -3 0 2", "2 número(s) positivo(s) \n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
        ("0 1 2 3 4", "4 número(s) positivo(s) \n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
        ("-1 -2 -3", "0 número(s) positivo(s) \n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)"),
        ("0", "0 número(s) positivo(s) \n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)")
        )

        for case, expected in test_cases:
            actual = numeros.clasificacion(case)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
