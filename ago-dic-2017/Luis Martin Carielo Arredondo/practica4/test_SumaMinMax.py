import unittest
from SumaMinSumaMax import elemento_mayor
from SumaMinSumaMax import elemento_menor
from SumaMinSumaMax import min_max

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.lista=[1,2,3,4,5]
		self.lista2=[2,3,4,5,1]
		self.lista3=[1,3,5,6,9]
		self.lista4=[9,5,4,2,3]
		self.lista5=[8,7,2,6,1]

	#Funciones test:
	def test_time_convertion(self):
		self.assertEqual(min_max(self.lista), (10, 14))
		self.assertEqual(min_max(self.lista2), (10, 14))
		self.assertEqual(min_max(self.lista3), (15, 23))
		self.assertEqual(min_max(self.lista4), (14, 21))
		self.assertEqual(min_max(self.lista5), (16, 23))
		
if __name__ == '__main__':
	unittest.main()