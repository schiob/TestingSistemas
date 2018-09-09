import unittest
from BirthdayCakeCandles import birthdayCandles

class testCake(unittest.TestCase):
	
 	def setUp(self):
 		self.n1=5; self.lista1=[1,2,2,3,4]
 		self.n2=3; self.lista2=[3,3,3]
 		self.n3=1; self.lista3=[1]
 		
 		
 	def test_Candles(self):
 		self.assertEqual(birthdayCandles(self.n1, self.lista1), 0)
 		self.assertEqual(birthdayCandles(self.n2, self.lista2), 1)
 		self.assertEqual(birthdayCandles(self.n3, self.lista3), 1)
               

if __name__ == "__main__":
    unittest.main()
