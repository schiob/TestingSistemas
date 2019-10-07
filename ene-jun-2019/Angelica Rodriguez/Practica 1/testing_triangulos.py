import unittest
import programa_triangulos

class TestLados(unittest.TestCase):
    def test_lados(self):
        test_cases = [(0,0,0,"No triángulo"),
                      (-3,-3,-3,"No triángulo"),
                      (1,2,9,"No triángulo"),
                      (3,3,3,"Equilátero"),
                      (3,2,2,"Isósceles"),
                      (2,3,4,"Escaleno"),
                      (3.2,9,"","Entrada incorrecta")]

        for inp in test_cases:
            expected = inp[3]
            actual = programa_triangulos.ladosTriangulo(inp[0], inp[1], inp[2])
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
