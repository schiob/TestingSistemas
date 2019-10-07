import unittest 
from LetsGoDinner import bonAppetit

class TestUnitario (unittest.TestCase):
	def setUp(self):
		self.n= 4
		self.k= 1
		self.b= 30
		self.ar= [10, 20, 10, 20]

		self.n1= 4
		self.k1= 1
		self.b1= 20
		self.ar1= [10, 20, 10, 20]


	def test_NobonAppetit(self):
		self.assertEqual(bonAppetit (self.n, self.k , self.b, self.ar), 10 ) 

	def test_bonAppetit(self):
		self.assertEqual(bonAppetit (self.n1, self.k1 , self.b1, self.ar1), "Bon Appetit" ) 

if __name__ == '__main__':
	unittest.main()

		