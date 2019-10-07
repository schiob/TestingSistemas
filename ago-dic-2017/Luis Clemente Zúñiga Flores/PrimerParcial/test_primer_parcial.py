import os
import unittest
import tempfile

from primer_parcial import Tri_from_file

class test_primer_parcial(unittest.TestCase):
    
    def setUp(self):
     
        self.equi1 = open('equi1.txt','w')
        self.equi1.write('3 3 3')
        self.equi1.close()        
        
        
        self.equi2 = open('equi2.txt','w')
        self.equi2.write('5 5 5')
        self.equi2.close()
        
        self.notri1 = open('notri1.txt','w')
        self.notri1.write('0 0 0')
        self.notri1.close()

        self.notri2 = open('notri2.txt','w')
        self.notri2.write('0 5 7')
        self.notri2.close()        
        
        self.notri3 = open('notri3.txt','w')
        self.notri3.write('1 2 3')
        self.notri3.close()
        
        
        self.iso1 = open('iso1.txt','w')
        self.iso1.write('10 7 7')
        self.iso1.close()
        
        self.iso2 = open('iso2.txt','w')
        self.iso2.write('4 5 4')
        self.iso2.close()
        
        self.esca1 = open('esca1.txt','w')
        self.esca1.write('8 6 5')
        self.esca1.close()
    
        
    def testEquilatero(self):       
        self.assertEqual(Tri_from_file(self.equi1.name),'Equilátero')
        self.assertEqual(Tri_from_file(self.equi2.name),'Equilátero')

    def testNoTri(self):
        self.assertEqual(Tri_from_file(self.notri1.name),'No triángulo')
        self.assertEqual(Tri_from_file(self.notri2.name),'No triángulo')
        self.assertEqual(Tri_from_file(self.notri3.name),'No triángulo')
    

    def testIsoceles(self):
        self.assertEqual(Tri_from_file(self.iso1.name),'Isósceles')
        self.assertEqual(Tri_from_file(self.iso2.name),'Isósceles')

    def testEscaleno(self):
        self.assertEqual(Tri_from_file(self.esca1.name),'Escaleno')
        

if __name__ == '__main__':
    unittest.main()

        
         
