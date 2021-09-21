import unittest
from ListaDeJuanita import ListaDeJuanita


class PruebasDeJuanita(unittest.TestCase):

    def Caso1(self):
        prueba = ListaDeJuanita([71, -24, -9, 0, 4])
        self.assertEqual(
            prueba, '2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)')

    def Caso2(self):
        prueba = ListaDeJuanita([1, 1, 2, 3, 4])
        self.assertEqual(
            prueba, '4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)')

    def Caso3(self):
        prueba = ListaDeJuanita([-3, -8, -9,-12])
        self.assertEqual(
            prueba, '0 número(s) positivo(s)\n4 número(s) negativo(s)\n2 número(s) par(es)\n2 número(s) impar(es)')

    def Caso4(self):
        prueba = ListaDeJuanita([0])
        self.assertEqual(prueba, '0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)')

if __name__ == '__main__':
    unittest.main()
