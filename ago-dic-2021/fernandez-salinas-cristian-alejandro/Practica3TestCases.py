import unittest
from Practica3 import contarNumeros

class contarNumerosTest(unittest.TestCase):
    
    def test1(self):
        n = 5
        numeros = "51 -12 -3 0 2"
        resEsperado = "2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"
        self.assertEqual(contarNumeros(n,numeros),resEsperado)

    def test2(self):
        n = 5
        numeros = "0 1 2 3 4"
        resEsperado = "4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"
        self.assertEqual(contarNumeros(n,numeros),resEsperado)

    def test3(self):
        n = 3
        numeros = "-1 -2 -3"
        resEsperado = "0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)"
        self.assertEqual(contarNumeros(n,numeros),resEsperado)

    def test4(self):
        n = 1
        numeros = "0"
        resEsperado = "0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)"
        self.assertEqual(contarNumeros(n,numeros),resEsperado)

if __name__ == '__main__':
    unittest.main()

        