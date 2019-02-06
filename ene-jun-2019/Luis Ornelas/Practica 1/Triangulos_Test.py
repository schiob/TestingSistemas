import unittest
import Triangulos
class TestTriangulo(unittest.TestCase):
    def test_area(self):
        test_case = [(1,2,3,"No es un Triangulo"),
                     (3,3,3,"Triangulo Equilatero"),
                     (4,4,5,"Triangulo Isosceles"),
                     (4,3,6,"Triangulo Escaleno"),
                     (-1,8,3,"No es un Triangulo"),
                     (0,0,0,"No es un Triangulo")]
        for a,b,c,esperado in test_case:
            actual = Triangulos.Tipo(a,b,c)
            self.assertEqual(esperado,actual)
if __name__ == '__main__':
    unittest.main()