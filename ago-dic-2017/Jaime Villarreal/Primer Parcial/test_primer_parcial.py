import unittest
from primer_parcial import tri_from_file

class TestPrimerParcial(unittest.TestCase):

    def setUp(self):
        with open('equi1.txt', 'w') as equi1:
            equi1.write('3 3 3')
        with open('equi2.txt', 'w') as equi2:
            equi2.write('5 5 5')
        with open('notri1.txt', 'w') as notri1:
            notri1.write('0 0 0')
        with open('notri2.txt', 'w') as notri2:
            notri2.write('0 5 7')
        with open('notri3.txt', 'w') as notri3:
            notri3.write('1 2 3')
        with open('iso1.txt', 'w') as iso1:
            iso1.write('10 7 7')
        with open('iso2.txt', 'w') as iso2:
            iso2.write('4 5 4')
        with open('esca1.txt', 'w') as esca1:
            esca1.write('4 5 4')


    def testEquilatero(self):
        self.assertEqual(tri_from_file('equi1.txt'), 'Equilátero.')
        self.assertEqual(tri_from_file('equi2.txt'), 'Equilátero.')


    def testNoTri(self):
        self.assertEqual(tri_from_file('notri1.txt'), 'No triángulo.')
        self.assertEqual(tri_from_file('notri2.txt'), 'No triángulo.')
        self.assertEqual(tri_from_file('notri3.txt'), 'No triángulo.')


    def testIsoceles(self):
        self.assertEqual(tri_from_file('iso1.txt'), 'Isóceles.')
        self.assertEqual(tri_from_file('iso2.txt'), 'Isóceles.')


    def testEscaleno(self):
        self.assertEqual(tri_from_file('esca1.txt'), 'Escaleno.')



if __name__ == '__main__':
    unittest.main()
