import unittest
import practica2

class TestContar(unittest.TestCase):

	def test_numeros(self):

		resultado = practica2.calcular([0,5,8,13,16,-4,-3])
		self.assertEqual(resultado[0], 4)
		self.assertEqual(resultado[1], 3)
		self.assertEqual(resultado[2], 2)
		self.assertEqual(resultado[3], 5)

		resultado = practica2.calcular([1,75,89,1,6,45])
		self.assertEqual(resultado[0], 1)
		self.assertEqual(resultado[1], 5)
		self.assertEqual(resultado[2], 0)
		self.assertEqual(resultado[3], 6)

		resultado = practica2.calcular([-15,-15,26,54])
		self.assertEqual(resultado[0], 2)
		self.assertEqual(resultado[1], 2)
		self.assertEqual(resultado[2], 2)
		self.assertEqual(resultado[3], 2)

if __name__ == '__main__':
	unittest.main()