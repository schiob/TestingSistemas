import unittest
import Triangulos

class TestTriangulo(unittest.TestCase):
    def test_tipo(self):
        test_casos=[(1,2,3,"No es un Triangulo"),
                    (4,4,4,"Es un Triangulo Equilatero"),
                    (4,4,5,"Es un Triangulo Isoceles"),
                    (4,3,6,"Es un Triangulo Escaleno"),
                    (-1,0,9,"No es un Triangulo"),
                    (0,0,0,"No es un Triangulo"),
                    (-8,-10,-7,"No es un Triangulo")]

        for a,b,c,esperado in test_casos:
            actual = Triangulos.tipo_triangulo(a,b,c)
            self.assertEqual(esperado,actual)

if __name__ == "__main__":
    unittest.main()