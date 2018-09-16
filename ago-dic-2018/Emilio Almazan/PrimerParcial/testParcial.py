import unittest
from parcial1 import convertor

class testConvertor(unittest.TestCase):
	def TestConvert(self):
		self.assertEqual(convertor("02:23PM"), "14:23Hrs")
		self.assertEqual(convertor("11:42PM"), "23:43Hrs")
		self.assertEqual(convertor("11:42AM"), "11:42Hrs")
		self.assertEqual(convertor("12:00AM"), "00:00Hrs")
		self.assertEqual(convertor("12:00PM"), "12:00Hrs")
		self.assertEqual(convertor("01:05AM"), "01:05Hrs")
		self.assertEqual(convertor("11:59PM"), "23:59Hrs")
	

if __name__ == '__main__':
	unittest.main()
		
