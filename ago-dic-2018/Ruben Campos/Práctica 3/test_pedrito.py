import unittest
import pedrito

class TestPedrito(unittest.TestCase):
    def test_pedrito(self):

        resultado = pedrito.numtriangular(1)
        self.assertEqual(resultado, 1)

        resultado = pedrito.numtriangular(3)
        self.assertEqual(resultado, 6)

        resultado = pedrito.numtriangular(4)
        self.assertEqual(resultado, 10)

        resultado = pedrito.numtriangular(56)
        self.assertEqual(resultado, 1596)

        resultado = pedrito.numtriangular(400)
        self.assertEqual(resultado, 80200)

if __name__ == '__main__':
    unittest.main()
