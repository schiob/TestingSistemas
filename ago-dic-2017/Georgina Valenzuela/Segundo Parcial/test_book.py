import unittest
from book import solve 

class TestUnitario (unittest.TestCase):
	def setUp(self):
		self.n= 10
		self.p= 1

		self.n1=100
		self.p1=100

		self.n2=100
		self.p2=50

		self.n3=100
		self.p3=40

		self.n4=100
		self.p4=80

		self.n5= 15
		self.p5= 1

		self.n6= 101
		self.p6= 101

		self.n7= 101
		self.p7= 50

		self.n8= 101
		self.p8= 40

		self.n9= 101
		self.p9= 80


	def test_PrimeraPag (self):
		self.assertEqual(solve (self.n , self.p), 0)

	def test_PrimeraPagInpar (self):
		self.assertEqual(solve (self.n5 , self.p5), 0)

	def test_UltimaPag (self):
		self.assertEqual(solve (self.n1 , self.p1),0 )

	def test_UltimaPagInpar (self):
		self.assertEqual(solve (self.n6 , self.p6),0 )

	def test_CentralPag (self):
		self.assertEqual(solve (self.n2 , self.p2),25)

	def test_CentralPagInpar (self):
		self.assertEqual(solve (self.n7, self.p7),25)

	def test_PrimeraMitad (self):
		self.assertEqual(solve (self.n3 , self.p3),20)

	def test_PrimeraMitadInpar (self):
		self.assertEqual(solve (self.n8 , self.p8),20)

	def test_SegundaMitad (self):
		self.assertEqual(solve (self.n4 , self.p4),10)

	def test_SegundaMitadInpar (self):
		self.assertEqual(solve (self.n9 , self.p9),10)


if __name__ == '__main__':
	unittest.main()