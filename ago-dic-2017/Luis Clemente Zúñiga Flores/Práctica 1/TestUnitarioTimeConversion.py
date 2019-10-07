import unittest
from timeconversion import timeConversion

#Test unitario para la función timeConversion
class TestUnitario(unittest.TestCase):
   
   def testTimeConversion(self):
	
	   self.assertEqual(timeConversion('07:05:45PM'),'19:05:45')
	   
if __name__ == '__main__':
    unittest.main()
