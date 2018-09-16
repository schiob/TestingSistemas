import unittest
from primer_parcial import main

class TriTestCase(unittest.TestCase):
        
    def TestEquilatero(self):
        self.assertEqual(main("equi1.txt" " 3 3 3"), "Equilatero")
        self.assertEqual(main("equi2.txt" " 5 5 5"), "Equilatero")

    def TestNotriangulo(self):
        self.assertEqual(main("notri1.txt" "0 0 0"),"No triangulo")
        self.assertEqual(main("notri2.txt" "0 5 7"),"No triangulo")
        self.assertEqual(main("notri2.txt" "1 2 3"),"No triangulo")

    def TestIsoceles(self):
        self.assertEqual(main("iso1.txt" "10 7 7"),"Isoceles")
        self.assertEqual(main("iso2.txt" "10 7 7"),"Isoceles")
        
    def TestEscaleno(self):
        self.assertEqual(main("esca1.txt" "8 6 5"),"Escaleno")
  
if __name__ == '__main__':
    unittest.main()
