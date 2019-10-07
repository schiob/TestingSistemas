import unittest
from VELAS import birthdayCakeCandles
class velas(unittest.TestCase):
    def test_velas(self):
        self.assertEqual( birthdayCakeCandles([4,2,6,9,9]),2 )

if __name__=='__main__':
    unittest.main()
    
