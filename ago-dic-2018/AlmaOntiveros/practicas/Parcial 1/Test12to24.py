import unittest 
from tiempo import Horarios
class Test12to24(unittest.TestCase):
	def test_horas(self):
        self.tiempo="02:23:00PM"
        self.tiempo1="11:42:00PM"
        self.tiempo2="11:42:00AM"
        self.tiempo3="12:00:00PM"

	def test_Horarios(self):
        self.assertEqual(Horarios(self.tiempo), "14:23:00")
		self.assertEqual(Horarios(self.tiempo1), "23:43:00")	
		self.assertEqual(Horarios(self.tiempo2), "11:42:00")

if __name__ == '__main__':
    unittest.main()