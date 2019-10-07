import unittest
from bon_appetit import bonAppetit

class TestBonAppetit(unittest.TestCase):

    def testBA(self):
        self.assertEqual(bonAppetit(4, 1, 12, [3, 10, 2, 9]), 5)
    def testBA2(self):
        self.assertEqual(bonAppetit(4, 1, 7, [3, 10, 2, 9]), 'Bon Appetit')


if __name__ == '__main__':
    unittest.main()
