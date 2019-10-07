import collections
import unittest 
import LEDs

class TestLEDs (unittest.TestCase):

	def test_LEDs(self):

		Caso1 = salida.contarleds('1')
		self.assertEqual(Caso1, '2')

		Caso2 = salida.contarleds('32')
		self.assertEqual(Caso2, '10')

		Caso3 = salida.contarleds('8888')
		self.assertEqual(Caso3, '28')

		Caso4 = salida.contarleds('115380')
		self.assertEqual(Caso4, '27')

		Caso5 = salida.contarleds('2819311')
		self.assertEqual(Caso5, '29')

		Caso6 = salida.contarleds('23456')
		self.assertEqual(Caso6, '25')

if __name__ == ' __main__ ':
	unittest.main()
