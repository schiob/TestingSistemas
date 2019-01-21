import unittest
from contarleds import ContarLeds

class TotalLedsTest(unittest.TestCase):
	"""docstring for ClassName"""
	def setup(self):
		pass
	def LedsTest(self):
		x=ContarLeds(1)
		self.assertEqual(x,2)
		x1=ContarLeds(32)
		self.assertEqual(x1,10)
		x2=ContarLeds(8888)
		self.assertEqual(x2,28)
		x3=ContarLeds(115380)
		self.assertEqual(x3,27)
		x4=ContarLeds(2819311)
		self.assertEqual(x4,29)
		x5=ContarLeds(23456)
		self.assertEqual(x5,25)

if __name__ == '__main__':
	unittest.main()