import unittest
import programa_numeros

class TestNumeros(unittest.TestCase):
    def test_num(self):
        test_cases_nums = [("51 -12 -3 0 2", "2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
                           ("0 1 2 3 4", "4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
                           ("-1 -2 -3", "0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)"),
                           ("0", "0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)")]

        for inp in test_cases_nums:
            expected = inp[1]
            actual = programa_numeros.clasificacion_numeros(inp[0])
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
