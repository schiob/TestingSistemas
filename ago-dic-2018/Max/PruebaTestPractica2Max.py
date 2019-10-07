import unittest
import Practica2Max
class TestMax(unittest.TestCase):
	def test_numeros(self):
		res = Practica2Max.calc([0, 4, 3, 5, 8])
		self.assertEqual(res[0],3)
		self.assertEqual(res[1],2)
		self.assertEqual(res[2],0)
		self.assertEqual(res[3],)
if __name__ == '__main__':
	unittest.main()
