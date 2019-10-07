import unittest
import Triangulo

class TrianguloTest(unittest.TestCase):
    def test_Triangulo(self):
        res=Triangulo.tri(1)
        self.assertEqual(res, 1)

        res=Triangulo.tri(3)
        self.assertEqual(res, 6)

        res=Triangulo.tri(4)
        self.assertEqual(res, 10)

        res=Triangulo.tri(56)
        self.assertEqual(res, 1596)

        res=Triangulo.tri(400)
        self.assertEqual(res, 80200)

if __name__ == '__main__':
    unittest.main()
