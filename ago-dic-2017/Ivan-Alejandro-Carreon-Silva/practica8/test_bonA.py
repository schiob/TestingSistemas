import unittest
from bon_appetit import bonAppetit

class testBonAppetit(unittest.TestCase):
    def testAppetit(self):
        self.assertEqual(bonAppetit(4, 1, 12, [3, 10, 2, 9]),5)
        self.assertEqual(bonAppetit(4, 1, 7, [3, 10, 2, 9]),'Bon Appetit')


if __name__ == '__main__':
    unittest.main()
