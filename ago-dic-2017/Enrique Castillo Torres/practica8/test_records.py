import unittest
from breaking_the_records import getRecord

class TestBreakingTheRecords(unittest.TestCase):

    def testRecord(self):
        self.assertEqual(getRecord([9, 10, 5, 20, 20, 4, 5, 2, 2, 5, 1]), (2, 4))

    def testRecord2(self):
        self.assertEqual(getRecord([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), (4, 0))

if __name__ == "__main__":
    unittest.main()
