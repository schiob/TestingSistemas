import unittest
import triangulo

class TestTriangulo(unittest.TestCase):

    def testTipoTriangulo(self):
        test_cases=[(1,2,3,"No es un Triángulo"),
                    (5,2,2,"Isosceles"),
                    (7,7,7,"Equilatero")]

        for (a,b,c),expected in test_cases:
            actual = triangulo.tipo(5,5,5)
            self.assertEquals(expected,actual)
if __name__ == '__main__':
    unittest.main()