import unittest
from primer_parcial import tri_from_file

class TestParcial(unittest.TestCase):

    def test_TestEquilatero(self):
        self.assertEqual(tri_from_file("equi1.txt"),"Equilátero")
        self.assertEqual(tri_from_file("equi2.txt"),"Equilátero")

    def test_TestNoTri(self):
        self.assertEqual(tri_from_file("notri1.txt"),"No triángulo")
        self.assertEqual(tri_from_file("notri2.txt"),"No triángulo")
        self.assertEqual(tri_from_file("notri3.txt"),"No triángulo")

    def test_TestIsoceles(self):
        self.assertEqual(tri_from_file("iso1.txt"),"Isóceles")
        self.assertEqual(tri_from_file("iso2.txt"),"Isóceles")

    def test_TestEscaleno(self):
        self.assertEqual(tri_from_file("esca1.txt"),"Escaleno")

if __name__ == '__main__':
    unittest.main()