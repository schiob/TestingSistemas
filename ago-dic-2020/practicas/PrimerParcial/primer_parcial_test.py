import unittest
import os
import primer_parcial

class TestTriangulo(unittest.TestCase):
    def setUp(self):
        pass

    def test_Equi(self):
        esperado = Equilatero
        actual = Equilatero
        self.assertEqual(actual, esperado)


if __name__ == "__main__":
    unittest.main()