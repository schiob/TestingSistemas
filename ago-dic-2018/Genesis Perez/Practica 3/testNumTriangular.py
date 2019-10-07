import unittest
import numTriangular

class TestNumTriangular(unittest.TestCase):
        def test_numTriangular(self):
            # Caso de prueba 1
            res=numTriangular.numTriang(1)
            self.assertEqual(res, 1)
            # Caso de prueba 2
            res=numTriangular.numTriang(3)
            self.assertEqual(res, 6)
            # Caso de prueba 3
            res=numTriangular.numTriang(4)
            self.assertEqual(res, 10)
            # Caso de prueba 4
            res=numTriangular.numTriang(56)
            self.assertEqual(res, 1596)
            # Caso de prueba 5
            res=numTriangular.numTriang(400)
            self.assertEqual(res, 80200)

if __name__ == '__main__':
    unittest.main()
