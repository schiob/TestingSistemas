import unittest
import cpractica3

class TestTriangular (unittest.TestCase):

	def test_triangulo(self):
		res=cpractica3.triangulo(1)
		res2=cpractica3.triangulo(3)
		res3=cpractica3.triangulo(4)
		res4=cpractica3.triangulo(56)
		res5=cpractica3.triangulo(400)

		self.assertEqual(res, 1)
		self.assertEqual(res2, 6)
		self.assertEqual(res3, 10)
		self.assertEqual(res4, 1596)
		self.assertEqual(res5, 80200)


if __name__ =='__main__':
	unittest.main() 
