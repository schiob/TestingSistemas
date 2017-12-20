import unittest
from hora import timeconvertion
class Sumas(unittest.TestCase):
    def test_hora(self):
        self.assertEqual( (timeconvertion('04:45:23pm')),('16:45:23') )

if __name__=='__main__':
    unittest.main()
    
