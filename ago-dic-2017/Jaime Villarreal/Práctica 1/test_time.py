import unittest
from TimeConversion import timeConversion

class TestTime(unittest.TestCase):

    def testTime(self):
        self.assertEqual(timeConversion('07:05:45PM'), '19:05:45')

if __name__ == '__main__':
    unittest.main()
