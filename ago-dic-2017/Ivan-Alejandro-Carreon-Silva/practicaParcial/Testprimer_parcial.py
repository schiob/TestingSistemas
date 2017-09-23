import unittest
from primer_parcial import tipo_triangulo

class Test_Triangulos(unittest.TestCase):

    def setUp(self):
        equi1 = open('equi1.txt','w').write('3 3 3')
        equi2 = open('equi2.txt','w').write('5 5 5')
        notri1 = open('notri1.txt','w').write('0 0 0')
        notri2 = open('notri2.txt','w').write('0 5 7')
        notri3 = open('notri3.txt','w').write('1 2 3')
        iso1 = open('iso1.txt','w').write('10 7 7')
        iso2 = open('iso2.txt','w').write('4 5 4')
        escal = open('esca.txt','w').write('8 6 5')

    def testEquilatero(self):
        self.assertEqual(tipo_triangulo('equi1.txt'),'Equilatero' )
        self.assertEqual(tipo_triangulo('equi2.txt'),'Equilatero')

    def testNoTri(self):
        self.assertEqual(tipo_triangulo('notri1.txt'),'No triángulo')
        self.assertEqual(tipo_triangulo('notri2.txt'),'No triángulo')
        self.assertEqual(tipo_triangulo('notri3.txt'),'No triángulo')

    def testIsoceles(self):
        self.assertEqual(tipo_triangulo('iso1.txt'),'Isóceles' )
        self.assertEqual(tipo_triangulo('iso2.txt'),'Isóceles' )

    def testEscaleno(self):
        self.assertEqual(tipo_triangulo('esca.txt'),'Escaleno' )



if __name__ == '__main__':
    unittest.main()
