  
import unittest
from primer_parcial import triangulo

class TestTriangulo(unittest.TestCase):
    def setUp(self):
        with open('equilatero1.txt', 'w') as equilatero1:
            equilatero1.write('3 3 3')
        with open('equilatero2.txt', 'w') as equilatero2:
            equilatero2.write('5 5 5')
        with open('notriangulo1.txt', 'w') as notriangulo1:
            notriangulo1.write('0 0 0')
        with open('notriangulo2.txt', 'w') as notriangulo2:
            notriangulo2.write('0 5 7')
        with open('notriangulo3.txt', 'w') as notriangulo3:
            notriangulo3.write('1 2 3')
        with open('isosceles1.txt', 'w') as isosceles1:
            isosceles1.write('10 7 7')
        with open('isosceles2.txt', 'w') as isosceles2:
            isosceles2.write('4 5 4')
        with open('escaleno1.txt', 'w') as escaleno1:
            escaleno1.write('4 5 3')

    def test_equilatero(self):
        self.assertEqual(triangulo('equilatero1.txt'), 'Equilatero')
        self.assertEqual(triangulo('equilatero2.txt'), 'Equilatero')

    def test_no_tri(self):
        self.assertEqual(triangulo("notriangulo1.txt"), "No es triangulo")
        self.assertEqual(triangulo("notriangulo2.txt"), "No es triangulo")
        self.assertEqual(triangulo("notriangulo3.txt"), "No es triangulo")

    def test_iscoceles(self):
        self.assertEqual(triangulo("isosceles1.txt"), "Isosceles")
        self.assertEqual(triangulo("isosceles2.txt"), "Isosceles")

    def test_escaleno(self):
        self.assertEqual(triangulo("escaleno1.txt"), "Escaleno")

if __name__ == '__main__':
    unittest.main()