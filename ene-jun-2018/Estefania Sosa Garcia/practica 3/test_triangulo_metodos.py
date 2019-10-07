import unittest
from triangulo_Metodos import compruebaRango
from triangulo_Metodos import imprime

class TestingMethodsTriangulo(unittest.TestCase):
    """"teste de la clase triangulo"""
    def test_compruebaFueraRango(self):
        p1 = compruebaRango(101,-101,0)
        self.assertEqual( p1 , 0)

    def test_compruebaRangoOK(self):    
        p2 = compruebaRango(80,80,80)
        self.assertEqual( p2 , 1 )
    
    def test_noTriangulo(self):
        t1 = imprime(-5,-5,-10)
        self.assertEqual( t1 , "no triangulo" )

    def  test_equilatero(self):
        t2 =imprime(50,50,50)
        self.assertEqual( t2 , "equilatero" )

    def  test_equilatero(self):
        t3 =imprime(11,11,9)
        self.assertEqual( t3 , "isoceles" )

    def  test_equilatero(self):
        t4 =imprime(5,4,3)
        self.assertEqual( t4 , "escaleno" )

if __name__ == '__main__':
            unittest.main()        
