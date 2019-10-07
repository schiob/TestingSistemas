import unittest
from triangulo import tipo_triang

class TestTriang(unittest.TestCase):
    """Tests for 'triangulo.py'"""

    def test_equilatero(self):
        result = tipo_triang(3, 3, 3)
        self.assertEqual(result, 'Equilatero')

    def test_isosceles(self):
        result = tipo_triang(3, 3, 2)
        self.assertEqual(result, 'Isósceles')

    def test_escaleno(self):
        result = tipo_triang(2, 3, 4)
        self.assertEqual(result, 'Escaleno')

    def test_false(self):
        result = tipo_triang(0, 0, 0)
        self.assertEqual(result, 'No es triangulo')
        result = tipo_triang(-10, -10, -10)
        self.assertEqual(result, 'No es triangulo')
        result = tipo_triang(1, 2, 3)
        self.assertEqual(result, 'No es triangulo')
        result = tipo_triang(50, 70, -85)
        self.assertEqual(result, 'No es triangulo')

if __name__ == '__main__':
    unittest.main()
