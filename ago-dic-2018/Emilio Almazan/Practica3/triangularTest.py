import unittest
from triangular import Ntriangular

class NumTriangTest(unittest.TestCase):
	def setUp(self):
		pass
	def TriangTest(self):
		x=triangular.Ntriangular(1)
		self.assertEqual(x,1)
		x2=triangular.Ntriangular(3)
		x3=triangular.Ntriangular(4)
		x4=triangular.Ntriangular(56)
		x5=triangular.Ntriangular(400)
		
		self.assertEqual(x2,6)
		self.assertEqual(x3,10)
		self.assertEqual(x4,1596)
		self.assertEqual(x5,80200)
	

if __name__ == '__main__':
	unittest.main()
		
