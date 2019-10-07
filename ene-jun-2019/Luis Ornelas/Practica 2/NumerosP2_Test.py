import unittest
import NumerosP2
class TestNumeros(unittest.TestCase):
    def test_numeros(self):
        test_case = [((51, -12, -3, 0, 2),"2 Numero(s) Positivo(s)\n2 Numero(s) Negativo(s)\n3 Numero(s) Par(es)\n2 Numero(s) Impar(es)"),
                     ((0, 1, 2, 3, 4),"4 Numero(s) Positivo(s)\n0 Numero(s) Negativo(s)\n3 Numero(s) Par(es)\n2 Numero(s) Impar(es)"),
                     ((-1, -2, -3),"0 Numero(s) Positivo(s)\n3 Numero(s) Negativo(s)\n1 Numero(s) Par(es)\n2 Numero(s) Impar(es)"),
                     ((0,),"0 Numero(s) Positivo(s)\n0 Numero(s) Negativo(s)\n1 Numero(s) Par(es)\n0 Numero(s) Impar(es)")]
        for numeros,esperado in test_case:
            actual = NumerosP2.Calcular(numeros)
            self.assertEqual(esperado, actual)

if __name__ == '__main__':
        unittest.main()