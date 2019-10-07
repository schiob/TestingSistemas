import unittest
from triangulo import TipoTriangulo

class TesTriangulo(unittest.TestCase):

    def test_Equilatero(self):
        hi = TipoTriangulo(3, 3, 3)
        self.assertEqual(hi, "equilatero")

    def test_Isoceles(self):
        hi = TipoTriangulo(10, 10, 5)
        self.assertEqual(hi, "isoceles")

    def test_Escaleno(self):
        hi = TipoTriangulo(90, 2, 9)
        self.assertEqual(hi, "escaleno")

    def test_NoEsTriangulo(self):
        hi =TipoTriangulo(1, 2, 3)
        self.assertEqual(hi, "No es triangulo")


if __name__== '__main__':
    unittest.main()
