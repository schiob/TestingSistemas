import unittest
from BirthdayCakeCandles import birthdayCakeCandles

class TestCake(unittest.TestCase):

    def testN(self):
        self.assertEqual(birthdayCakeCandles(5, [2, 2, 2, 2, 2]), 5)

if __name__ == '__main__':
    unittest.main()
