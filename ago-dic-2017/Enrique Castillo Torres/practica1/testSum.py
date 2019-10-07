import unittest
from minmax import MinMax

class TestMinMaxSum(unittest.TestCase):

    def testSum(self):
        self.assertEqual(MinMax[1, 2, 3, 4, 5], "10 14")
if __name__ == '__main__':
    unittest.main()
