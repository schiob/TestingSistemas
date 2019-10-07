import unittest 
import triangular
#numero triangular Tn= (n(n+1))/2

class TestTriangular(unittest.TestCase):
	def test_numeroTriangular(self):

		T1 = triangular.calcularTriangular(1)
		self.assertEqual(T1, 1)

		T2 = triangular.calcularTriangular(3)
		self.assertEqual(T2, 6)

		T3 = triangular.calcularTriangular(4)
		self.assertEqual(T3, 10)

		T4 = triangular.calcularTriangular(56)
		self.assertEqual(T4, 1596)

		T5 = triangular.calcularTriangular(400)
		self.assertEqual(T5, 80200)

if __name__ == '__main__':
	unittest.main()
		
		
	