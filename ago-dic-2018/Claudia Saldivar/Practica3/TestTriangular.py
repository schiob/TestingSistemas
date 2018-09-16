import unittest
import Triangular

class TestTriangular(unittest.TestCase):
    def Test_Triangular(self):
        res = tringular.numero_triangular(1)
        self.assertEqual(resultado, 1)

        res = tringular.numero_triangular(3)
        self.assertEqual(resultado, 6)

        res = tringular.numero_triangular(4)
        self.assertEqual(resultado, 10)

        res = tringular.numero_triangular(56)
        self.assertEqual(resultado, 1596)

        res = tringular.numero_triangular(400)
        self.assertEqual(resultado, 80200)

if __name__ == '__main__':
    unittest.main()
