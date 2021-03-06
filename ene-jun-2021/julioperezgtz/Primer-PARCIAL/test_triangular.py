import unittest 
from numeros_triangulares import *

class Test_numero_trinagular(unittest.TestCase):
    def test_n_triangular(self):
        tcs=(
            [1,1],
            [3,6],
            [4,10],
            [56,1596],
            [400,80200]  
        )
        for t in tcs:
            self.assertEqual(ntriangular(t[0]),t[1])


if __name__ == '__main__' :
    unittest.main()