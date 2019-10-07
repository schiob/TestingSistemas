import unittest
import triangular

class TestTriangular(unittest.TestCase):
	def test_numeros(self):
		r1 = triangular.Triangular(1)
		self.assertEqual(r1,1)
		r2 = triangular.Triangular(3)
		self.assertEqual(r2,6)
		r3 = triangular.Triangular(4)
		self.assertEqual(r3,10)
		r4 = triangular.Triangular(56)
		self.assertEqual(r4,1596)
		r5 = triangular.Triangular(400)
		self.assertEqual(r5,80200)
		
if __name__ == '__main__':
	unittest.main()