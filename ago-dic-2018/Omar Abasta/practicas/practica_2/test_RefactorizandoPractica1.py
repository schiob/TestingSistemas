#test_RefactorizandoPractica1

import unittest
from RefactorizandoPractica1 import calc


class TestRefactorizandoPractica1(unittest.TestCase):

    def setUp(self):
        self.mock_nums = [1,2,3,4,5,6,-7,8,9,10]

    def test_calc(self):
        result = calc(self.mock_nums)
        self.assertEqual(result, (5, 5, 1, 9))


if __name__ == '__main__':
    unittest.main()
