import unittest
from drawing_book import solve

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.n0=10; self.p0=1;
		self.n1=10; self.p1=10;
		self.n2=10; self.p2=5;
		self.n3=10; self.p3=4;
		self.n4=10; self.p4=8;
		self.n5=11; self.p5=1;
		self.n6=11; self.p6=11;
		self.n7=11; self.p7=6;
		self.n8=11; self.p8=3;
		self.n9=11; self.p9=10;

	#Funciones test:
	def test_drawing(self):
		self.assertEqual(solve(self.n0, self.p0), 0)
		self.assertEqual(solve(self.n1, self.p1), 0)
		self.assertEqual(solve(self.n2, self.p2), 2)
		self.assertEqual(solve(self.n3, self.p3), 2)
		self.assertEqual(solve(self.n4, self.p4), 1)
		self.assertEqual(solve(self.n5, self.p5), 0)
		self.assertEqual(solve(self.n6, self.p6), 0)
		self.assertEqual(solve(self.n7, self.p7), 2)
		self.assertEqual(solve(self.n8, self.p8), 1)
		self.assertEqual(solve(self.n9, self.p9), 0)

if __name__ == '__main__':
	unittest.main()