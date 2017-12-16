import unittest
from primer_parcial import tipo_triangulo

class Test_Triangulos(unittest.TestCase):

    def setUp(self):
        equi1 = open('equi1.txt','w')
        equi1.write('3 3 3')
        equi1.close()

        equi2 = open('equi2.txt','w')
        equi2.write('5 5 5')
        equi2.close()

        notri1 = open('notri1.txt','w')
        notri1.write('0 0 0')
        notri1.close()

        notri2 = open('notri2.txt','w')
        notri2.write('0 5 7')
        notri2.close()

        notri3 = open('notri3.txt','w')
        notri3.write('1 2 3')
        notri3.close()

        iso1 = open('iso1.txt','w')
        iso1.write('10 7 7')
        iso1.close()

        iso2 = open('iso2.txt','w')
        iso2.write('4 5 4')
        iso2.close()

        esca = open('esca.txt','w')
        esca.write('8 6 5')
        esca.close()

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
