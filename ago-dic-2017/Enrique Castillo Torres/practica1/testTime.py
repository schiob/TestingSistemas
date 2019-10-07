import unittest
from TimeConversion import timeConversion

class TestTimeConversion(unittest.TestCase):

    def testHora(self):
        self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")

        self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")

if __name__ == '__main__':
    unittest.main()
