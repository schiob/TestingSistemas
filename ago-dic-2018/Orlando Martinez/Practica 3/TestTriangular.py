import unittest
import NumeroTriangular

class TestTriangular(unittest.TestCase):
      def test_contar1(self):
          res=NumeroTriangular.calcular(1)
          self.assertEqual(res,1)
      def test_contar2(self):
          res=NumeroTriangular.calcular(3)
          self.assertEqual(res,6)
      def test_contar3(self):
          res=NumeroTriangular.calcular(4)
          self.assertEqual(res,10)
      def test_contar4(self):
          res=NumeroTriangular.calcular(56)
          self.assertEqual(res,1596)
      def test_contar5(self):
          res=NumeroTriangular.calcular(400)
          self.assertEqual(res,80200)
if __name__ == '__main__':
    unittest.main()
