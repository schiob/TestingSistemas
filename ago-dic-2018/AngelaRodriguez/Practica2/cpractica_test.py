import unittest
import cpractica

class TestJuanita (unittest.TestCase):

	def test_numeros(self):
		res=cpractica.calc([0,3,42,5,6])
		self.assertEqual(res[0], 3)
		self.assertEqual(res[1], 2)
		self.assertEqual(res[2], 0)
		self.assertEqual(res[3], 4)

if __name__ =='__main__':
	unittest.main() 
