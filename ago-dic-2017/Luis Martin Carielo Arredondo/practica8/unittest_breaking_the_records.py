import unittest
from breaking_the_records import getRecord

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.n=5; self.s=[2, 3, 5, 1, 24];
		self.n1=1; self.s1=[10];
		self.n2=1; self.s2=[0];
		self.n3=10; self.s3=[42, 35, 13, 0, 55, 10, 4, 52, 55, 30];
		self.n4=13; self.s4=[13, 11, 15, 9, 17, 7, 19, 6, 20, 5, 22, 23, 3];

	#Funciones test:
	def test_getRecord(self):
		self.assertEqual(getRecord(self.s), (3, 1))
		self.assertEqual(getRecord(self.s1), (0, 0))
		self.assertEqual(getRecord(self.s2), (0, 0))
		self.assertEqual(getRecord(self.s3), (1, 3))
		self.assertEqual(getRecord(self.s4), (6, 6))
		
if __name__ == '__main__':
	unittest.main()