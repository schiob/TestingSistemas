import unittest
import triangulo

class TestTriangulo(unittest.TestCase):
    def test_clasificacion(self):
        test_cases=(
        ("1 2 3", "Los lados no forman un triángulo"),
        ("4 0 1", "Los lados no forman un triángulo"),
        ("-1 5 10", "Los lados no forman un triángulo"),
        ("5 5 5", "Triangulo Equilátero"),
        ("4 4 5", "Triangulo Isósceles"),
        ("12 16 8", "Triangulo Escaleno"),
        ("hola", "Entrada de datos inválida")
        )


        for case, expected in test_cases:
            actual = triangulo.clasificacion(case)
            self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()
