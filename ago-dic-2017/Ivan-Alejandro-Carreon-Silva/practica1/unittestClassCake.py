import unittest
from cosa3 import birthdayCakeCandles

class TestCake(unittest.TestCase):

    def test_same_n(self):
        self.assertEqual(birthdayCakeCandles(5,[2,2,2,2,2]),5 )
        #self.assertEqual(birthdayCakeCandles(1,[0],1)

if __name__ == "__main__":
    unittest.main()
