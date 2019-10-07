import unittest
from candles import birthdayCakeCandles


#Test unitario para la clase birthdayCakeCandles
class TestUnitario(unittest.TestCase):
   
   def testCandles(self):
	   arr = [10,11,12,13,14]	   
	   self.assertEqual(birthdayCakeCandles(5,arr),1)
	 
if __name__ == '__main__':
    unittest.main()



