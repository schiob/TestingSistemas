import unittest 
import NumerosImpares

class TestNumerosImpares(unittest.TestCase):

	def Test_numerosImpares(self):

		suma = NumerosImpares.sumarNumerosImpares('6 -5')
		self.assertEqual(suma, 5)

		suma = NumerosImpares.sumarNumerosImpares('12 15')
		self.assertEqual(suma, 13)

		suma = NumerosImpares.sumarNumerosImpares('12 12')
		self.assertEqual(suma, 0)

		suma = NumerosImpares.sumarNumerosImpares('123 321')
		self.assertEqual(suma, 21756)

		suma = NumerosImpares.sumarNumerosImpares('4321 1234')
		self.assertEqual(suma, 4284911)

		suma = NumerosImpares.sumarNumerosImpares('-19289 7853')
		self.assertEqual(suma, -77593260)

if __name__ == '__main__':
	unittest.main()