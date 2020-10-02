import unittest
import primer_parcial

class TestPrimerParcial(unittest.TestCase):
    #casos de prueba
    def TestEquilatero(self):
        self.assertEqual(tipoTriangulo(3, 3, 3))
        self.assertEqual(tipoTriangulo(5, 5, 5))

    def TestNoTriangulo(self):
        self.assertEqual(tipoTriangulo(0, 0, 0))
        self.assertEqual(tipoTriangulo(0, 5, 7))
        self.assertEqual(tipoTriangulo(1, 2, 3)) 
    

    def TestIsoceles(self):
        self.assertEqual(tipoTriangulo(10, 7, 7))
        self.assertEqual(tipoTriangulo(4, 5, 4))
    

    def TestEscaleno(self):
        self.assertEqual(tipoTriangulo(8, 6, 5))

if __name__ == '__main__':
    unittest.main()
       
    