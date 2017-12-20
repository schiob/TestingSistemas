import unittest
from primer_parcial import RegresaString
class primerP(unittest.TestCase):
    def setUp(self):
        notri1= open('notri1.txt','w')
        notri1.write("0 0 0")
        notri1.close()

        notri2= open('notri2.txt','w')
        notri2.write("0 5 7")
        notri2.close()

        notri3= open('notri3.txt','w')
        notri3.write("1 2 3")
        notri3.close()

        equi1= open('equi1.txt','w')
        equi1.write("3 3 3")
        equi1.close()

        equi2= open('equi2.txt','w')
        equi2.write("5 5 5")
        equi2.close()

        iso1= open('iso1.txt','w')
        iso1.write("10 7 7")
        iso1.close()

        iso2= open('iso2.txt','w')
        iso2.write("4 5 4")
        iso2.close()

        esca1= open('esca1.txt','w')
        esca1.write("8 6 5")
        esca1.close()

       

    def test_equilatero(self):
                
        self.assertEqual(RegresaString("equi1.txt"),'equilatero')
        self.assertEqual(RegresaString("equi2.txt"),'equilatero')
        
    def test_NOtriangulo(self):
                
        self.assertEqual(RegresaString("notri1.txt"),'no triangulo')
        self.assertEqual(RegresaString("notri2.txt"),'no triangulo')
        self.assertEqual(RegresaString("notri3.txt"),'no triangulo')
        
        
    def test_isoceles(self):
                
        self.assertEqual(RegresaString("iso1.txt"),'isoceles')
        self.assertEqual(RegresaString("iso2.txt"),'isoceles')
        
    def test_escaleno(self):
               
        self.assertEqual(RegresaString("esca1.txt"),'escaleno')
        
        
if __name__ == '__main__':
    unittest.main()


    
         
 
