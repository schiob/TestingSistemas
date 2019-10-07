import unittest
from breaking_the_records import getRecord

class TestRecord(unittest.TestCase):

    # Caso donde Fulanita rompe recors altos y bajos.
    def testMix(self):
        self.assertEqual(getRecord([10, 5, 20, 20, 4, 5, 2, 25, 1]), (2,4))

    # Caso donde Fulanita solo rompe sus records altos.
    def testSoloMayor(self):
        self.assertEqual(getRecord([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), (4,0))

    # Caso donde Fulanita solo rompe sus records bajos.
    def testSoloMenor(self):
        self.assertEqual(getRecord([20, 10, 5, 4, 3, 1]), (0,5))



if __name__ == '__main__':
    unittest.main()
