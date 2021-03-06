import unittest
import Numeros_Triangulares

class TestNT(unittest.TestCase):

    def test_nt(self):
        #Numero Entrada, Resultado Esperado
        test_casos = [(1, 1),
                      (3, 6),
                      (4, 10),
                      (6, 21),
                      (64, 2080)]

        for entrada, esperado in test_casos:
            actual = Numeros_Triangulares.n_triangular(entrada)
            self.assertEqual(esperado, actual)


if __name__ == '__main__':
    unittest.main()
