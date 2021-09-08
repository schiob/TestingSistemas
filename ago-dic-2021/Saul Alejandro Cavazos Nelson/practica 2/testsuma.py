import unittest
from practica_uno import suma

class testSuma(unittest.TestCase):
     def test_suma_1_enteros(self):
         resultado=suma(2,2)
         self.assertEqual(resultado,4)
         self.assertTrue(resultado,4) 
             
     def test_suma_2_decimales(self):
         resultado=suma(.5,.5)
         self.assertEqual(resultado,1)
         self.assertTrue(resultado,1)

     def test_suma_3_mixtos(self):
         resultado=suma(-3,4)
         self.assertEqual(resultado,1)
         self.assertTrue(resultado,1)

     def test_suma_4_negativos(self):
         resultado=suma(-3,-4)
         self.assertEqual(resultado,-7)
         self.assertTrue(resultado,-7)
         
     def test_suma_5_decimales_mixtos(self):
         resultado=suma(-3,1.5)
         self.assertEqual(resultado,-1.5)
         self.assertTrue(resultado,-1.5)

     def test_suma_6_ceros(self):
         resultado=suma(0,0)
         self.assertEqual(resultado,0)
         self.assertTrue(resultado,0)


if __name__ =='__main__':
 unittest.main()
 
 


