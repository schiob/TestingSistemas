import unittest
import cpractica

class TestJuanita (unittest.TestCase):

	def test_numeros(self):
		res1=cpractica.calc([0,3,42,5,6])
		self.assertEqual(res1[0], 3)
		self.assertEqual(res1[1], 2)
		self.assertEqual(res1[2], 0)
		self.assertEqual(res1[3], 4)

		res2=cpractica.calc([10,4,-4,6,-2])
		self.assertEqual(res2[0], 5)
		self.assertEqual(res2[1], 0)
		self.assertEqual(res2[2], 2)
		self.assertEqual(res2[3], 3)

		res3=cpractica.calc([-1,25,90,13,-2])
		self.assertEqual(res3[0], 2)
		self.assertEqual(res3[1], 3)
		self.assertEqual(res3[2], 2)
		self.assertEqual(res3[3], 3)

		res4=cpractica.calc([-17,3,0,14,5])
		self.assertEqual(res4[0], 2)
		self.assertEqual(res4[1], 3)
		self.assertEqual(res4[2], 1)
		self.assertEqual(res4[3], 3)


if __name__ =='__main__':
	unittest.main() 
