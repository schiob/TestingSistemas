import unittest
from BirthdayCakeCandles import birthdayCakeCandles

class TestCake(unittest.TestCase):

    def testCake(self):
        self.assertEqual(birthdayCakeCandles(7, [1, 2, 2, 3, 5, 7, 7]), 2)


if __name__ == "__main__":
    unittest.main()
