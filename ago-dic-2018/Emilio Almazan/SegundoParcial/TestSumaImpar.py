import unittest
from sumaImpar import sumarImpares

class testSuma(unittest.TestCase):
	def setup(self):
		pass
	def Test(self):
		x=sumatoria([6,-5])
		self.assertEqual(x,5)

		x2=sumatoria([12,15])
		self.assertEqual(x2,13)

		x3=sumatoria([123,321])
		self.assertEqual(x3, 21756)

		x4=sumatoria([4321,1234])
		self.assertEqual(x4, 4284911)

		x5=sumatoria([-19289,7853])
		self.assertEqual(x5, -77593260)

if __name__ == '__main__':
	unittest.main()