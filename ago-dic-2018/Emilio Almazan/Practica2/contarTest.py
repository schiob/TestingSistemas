import unittest
from contar2 import contar

class testcontar(unittest.TestCase):
	def setup(self):
		self.mock_nums = [1,2,3,4,-5]
	def contarnum(self):
		resultado=contar2.contar(self.mock_nums)
		self.assertEqual(resultado, (4,1,2,3))
		#self.assertEqual(resultado[1],1)
		#self.assertEqual(resultado[2],2)
		#self.assertEqual(resultado[3],3)

if __name__ == '__main__':
	unittest.main()
