import unittest
from practica3a import juanitaList


class testJuanita(unittest.TestCase):

    def test1(self):
        prueba = juanitaList([51, -12, -3, 0, 2])
        self.assertEqual(
            prueba, '2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)')

    def test2(self):
        prueba = juanitaList([0, 1, 2, 3, 4])
        self.assertEqual(
            prueba, '4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)')

    def test3(self):
        prueba = juanitaList([-1, -2, -3])
        self.assertEqual(
            prueba, '0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)')

    def test4(self):
        prueba = juanitaList([0])
        self.assertEqual(prueba, '0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)')

if __name__ == '__main__':
    unittest.main()
