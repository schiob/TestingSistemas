import unittest
from MiniMaxSum import minMaxSum

class TestSum(unittest.TestCase):

    def testSum(self):
        self.assertEqual(minMaxSum([1, 2, 3, 4, 5]), '10 14')

if __name__ == '__main__':
    unittest.main()
