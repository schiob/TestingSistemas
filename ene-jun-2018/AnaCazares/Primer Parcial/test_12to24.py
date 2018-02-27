import unittest 
from hora import time_convertion
class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
                self.hora="02:23:00PM"
                self.hora1="11:42:00PM"
                self.hora2="11:42:00AM"
                self.hora3="12:00:00PM"
                self.hora4="12:00:00AM"
                self.hora5="01:05:00AM"
                self.hora6="11:59:00PM"		
		
	    
	#Funciones test:
	def test_time_convertion(self):
		self.assertEqual(time_convertion(self.hora), "14:23:00")
		self.assertEqual(time_convertion(self.hora1), "23:43:00")	
		self.assertEqual(time_convertion(self.hora2), "11:42:00")
		self.assertEqual(time_convertion(self.hora3), "00:00:00")
		self.assertEqual(time_convertion(self.hora4), "12:00:00")
		self.assertEqual(time_convertion(self.hora5), "01:05:00")	
		self.assertEqual(time_convertion(self.hora6), "23:59:00")
		
		
if __name__ == '__main__':
	unittest.main()
