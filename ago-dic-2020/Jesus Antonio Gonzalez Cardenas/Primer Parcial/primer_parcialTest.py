import unittest
from primer_parcial import Tri_from_file

class PrimerParcialTest(unittest.TestCase):
    
    def testEquilatero(self):
        filepath1 = 'equi1.txt'
        Answer = Tri_from_file(filepath1)
        self.assertEqual(Answer,'Equilátero')
        
        filepath2 = 'equi2.txt'
        Answer2 = Tri_from_file(filepath2)
        self.assertEqual(Answer2,'Equilátero')

    def testNoTri(self):
        filepath = 'notri1.txt'
        Answer = Tri_from_file(filepath)
        self.assertEqual(Answer,'No triángulo')
        
        filepath = 'notri2.txt'
        Answer2 = Tri_from_file(filepath)
        self.assertEqual(Answer2,'No triángulo')
        
        filepath = 'notri3.txt'
        Answer3 = Tri_from_file(filepath)
        self.assertEqual(Answer3,'No triángulo')

    def testIsoceles(self):
        filepath1 = 'iso1.txt'
        Answer = Tri_from_file(filepath1)
        self.assertEqual(Answer,'Isóceles')
        
        filepath2 = 'iso2.txt'
        Answer2 = Tri_from_file(filepath2)
        self.assertEqual(Answer2,'Isóceles')
       
       
    def testEscaleno(self):
        filepath = 'esca1.txt'
        Answer = Tri_from_file(filepath)
        self.assertEqual(Answer,'Escaleno')

if __name__ == '__main__':
    unittest.main()
