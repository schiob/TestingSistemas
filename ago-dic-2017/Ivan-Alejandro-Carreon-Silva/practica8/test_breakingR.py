import unittest
from breaking_the_records import getRecord

class testBreakingRecords(unittest.TestCase):
    def testRecords(self):
        self.assertEqual(getRecord([10, 5, 20, 20, 4, 5, 2, 25, 1]), (2, 4))

        self.assertEqual(getRecord([3, 4, 31, 36, 10, 28, 35, 5, 24, 42]),(4, 0))





if __name__ == '__main__':
    unittest.main()
