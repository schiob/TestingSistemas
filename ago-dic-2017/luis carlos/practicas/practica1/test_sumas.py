import unittest
from sumas import min_max
class Sumas(unittest.TestCase):
    def test_sumas(self):
        self.assertEqual( (min_max([2,5,3,4,1])),(10,14) )

if __name__=='__main__':
    unittest.main()
    
