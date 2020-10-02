import unittest
from primer_parcial import tri_from_file

class Test_Tri_From_File(unittest.TestCase):
    def setUp(self):
        #Equilatero
        self.equi1 = "equi1.csv"
        self.equi2 = "equi2.csv"

        #No triangulo
        self.notri1 = "notri1.csv"
        self.notri2 = "notri2.csv"

        #Isoceles
        self.iso1 = "iso1.csv"
        self.iso2 = "iso2.csv"

        #Escaleno
        self.esca1 = "esca1.csv"
        self.esca2 = "esca2.csv"

    def test_equilatero(self):
        salida_esperada1 = tri_from_file(self.equi1)
        salida_real1 = "Equilátero"
        self.assertEqual(salida_real1, salida_esperada1)

        salida_esperada2 = tri_from_file(self.equi2)
        salida_real2 = "Equilátero"
        self.assertEqual(salida_real2, salida_esperada2)
    
    def test_no_tri(self):
        salida_esperada1 = tri_from_file(self.notri1)
        salida_real1 = "No triángulo"
        self.assertEqual(salida_real1, salida_esperada1)

        salida_esperada2 = tri_from_file(self.notri2)
        salida_real2 = "No triángulo"
        self.assertEqual(salida_real2, salida_esperada2)
    
    def test_isoceles(self):
        salida_esperada1 = tri_from_file(self.iso1)
        salida_real1 = "Isóceles"
        self.assertEqual(salida_real1, salida_esperada1)

        salida_esperada2 = tri_from_file(self.iso2)
        salida_real2 = "Isóceles"
        self.assertEqual(salida_real2, salida_esperada2)

    def test_escaleno(self):
        salida_esperada1 = tri_from_file(self.esca1)
        salida_real1 = "Escaleno"
        self.assertEqual(salida_real1, salida_esperada1)

        salida_esperada2 = tri_from_file(self.esca2)
        salida_real2 = "Escaleno"
        self.assertEqual(salida_real2, salida_esperada2)

    def tearDown(self):
        #Equilatero
        del(self.equi1)
        del(self.equi2)

        #No triangulo
        del(self.notri1)
        del(self.notri2)

        #Isoceles
        del(self.iso1)
        del(self.iso2)

        #Escaleno
        del(self.esca1)
        del(self.esca2)

if __name__ == '__main__':
    unittest.main()