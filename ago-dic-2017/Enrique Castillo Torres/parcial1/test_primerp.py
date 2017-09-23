import unittest
from primer_parcial import tri

class TestTriangulo(unittest.TestCase):
    def setUp(self):
        with open('esca1.txt', 'w') as f:
            f.write('8 6 5')

    def test_equilatero(self):
        self.assertEqual(tri('equi1.txt'), 'Equilatero')
        self.assertEqual(tri('equi2.txt'), 'Equilatero')

    def test_no_tri(self):
        self.assertEqual(tri("notri1.txt"), "No es triangulo")
        self.assertEqual(tri("notri2.txt"), "No es triangulo")
        self.assertEqual(tri("notri3.txt"), "No es triangulo")

    def test_iscoceles(self):
        self.assertEqual(tri("iso1.txt"), "Isosceles")
        self.assertEqual(tri("iso2.txt"), "Isosceles")

    def test_escaleno(self):
        self.assertEqual(tri("esca1.txt"), "Escaleno")

if __name__ == '__main__':
    unittest.main()
