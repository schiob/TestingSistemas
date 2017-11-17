import unittest
from Hora import time_convertion

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.hora="12:00:00AM"
		self.hora1="01:13:59AM"
		self.hora2="11:59:59PM"
		self.hora3="12:00:00PM"
		self.hora4="04:23:50PM"

	#Funciones test:
	def test_time_convertion(self):
		self.assertEqual(time_convertion(self.hora), "00:00:00")
		self.assertEqual(time_convertion(self.hora1), "1:13:59")
		self.assertEqual(time_convertion(self.hora2), "23:59:59")
		self.assertEqual(time_convertion(self.hora3), "12:00:00")
		self.assertEqual(time_convertion(self.hora4), "16:23:50")
		
if __name__ == '__main__':
	unittest.main()