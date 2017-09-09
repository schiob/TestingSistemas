import unittest
from suma import suma_nums
from candles import birthdayCakeCandles
from timeconversion import timeConversion

class TestUnitario(unittest.TestCase):
   
   def testCandles(self):
	   arr = [10,11,12,13,14]
	   self.assertEqual(suma_nums(arr),'46 50')
	   self.assertEqual(birthdayCakeCandles(5,arr),1)
	   self.assertEqual(timeConversion('07:05:45PM'),'19:05:45')
	   
if __name__ == '__main__':
    unittest.main()



