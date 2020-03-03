import unittest
from time_12to24 import time_to24

class testConvertor(unittest.TestCase):
    def testCase(self):
        self.assertEqual(time_to24('02:23 PM'), '14:23 PM')
    
    def testCase2(self):
        self.assertEqual(time_to24('11:42 PM'), '23:42 PM')
        self.assertEqual(time_to24('11:42 AM'), '11:42 AM')
        self.assertEqual(time_to24('12:00 PM'), '12:00 PM')
        self.assertEqual(time_to24('12:00 AM'), '00:00 AM')
        self.assertEqual(time_to24('01:05 AM'), '01:05 AM')
        self.assertEqual(time_to24('11:59 PM'), '23:59 PM')   
        
if __name__=='__main__':
    unittest.main()