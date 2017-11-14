import unittest
from libro import solve

class partial2(unittest.TestCase):
    

    def test_paginas_par(self):
        self.assertEqual(solve(8,1),0)
        self.assertEqual(solve(8,8),0)
        self.assertEqual(solve(8,4),2)
        self.assertEqual(solve(8,4),2)
        self.assertEqual(solve(8,6),1)

    def test_paginas_impar(self):
        self.assertEqual(solve(7,1),0)
        self.assertEqual(solve(7,7),0)
        self.assertEqual(solve(7,4),1)
        self.assertEqual(solve(7,5),1)
        self.assertEqual(solve(7,0),0)
        

    

if __name__ =='__main__':
    unittest.main()
