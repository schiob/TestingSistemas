#Test para la Práctica 3
#Casos de pruebas
#<1, 1> <3, 6> <4, 10> <56, 1596> <400, 80200>
import unittest
import Practica3Triangular

class Test (unittest.TestCase):
    def test_triangular(self):
        res=Practica3Triangular.Ctriangular(1)
        self.assertEqual(res, 1)
    def test_triangular1(self):
        res=Practica3Triangular.Ctriangular(3)
        self.assertEqual(res, 6)
    def test_triangular2(self):
        res=Practica3Triangular.Ctriangular(4)
        self.assertEqual(res, 10)
    def test_triangular3(self):
        res=Practica3Triangular.Ctriangular(56)
        self.assertEqual(res, 1596)
    def test_triangular4(self):
        res=Practica3Triangular.Ctriangular(400)
        self.assertEqual(res, 80200)

if __name__ == '__main__':
    unittest.main()
