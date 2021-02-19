import unittest

from ejemplo import clasnums

class Testnums(unittest.TestCase):
    def test_nums(self):
        tcs=(
            [2,2,2,2,2,5,0,5,0],#pos,neg,par,imp
            [2,2,2,2,3,5,0,4,1],
            [2,2,2,3,3,5,0,3,2],
            [2,2,3,3,3,5,0,2,3],
            [2,3,3,3,3,5,0,1,4],
            [3,3,3,3,3,5,0,0,5],
            [-2,-2,-2,-2,-2,0,5,5,0],
            
        )
        for t in tcs:
            self.assertEqual(clasnums(t[0:5]),t[5:9])

if __name__ == '__main__':
    unittest.main()