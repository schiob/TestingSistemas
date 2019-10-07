import unittest
from grading_students import solve

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.n=5; self.grade=[91,50,23,73,88];
		self.n1=1; self.grade1=[3];
		self.n2=1; self.grade2=[0];
		self.n3=1; self.grade3=[83];
		self.n4=13; self.grade4=[13, 71, 65, 99, 87, 47, 39, 56, 100, 5, 22, 33, 93];

	#Funciones test:
	def test_getRecord(self):
		self.assertEqual(solve(self.grade), [91, 50, 23, 75, 90])
		self.assertEqual(solve(self.grade1), [3])
		self.assertEqual(solve(self.grade2), [0])
		self.assertEqual(solve(self.grade3), [85])
		self.assertEqual(solve(self.grade4), [13, 71, 65, 100, 87, 47, 40, 56, 100, 5, 22, 33, 95])
		
if __name__ == '__main__':
	unittest.main()