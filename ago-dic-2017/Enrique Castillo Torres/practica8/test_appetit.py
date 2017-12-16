import unittest
from bon_appetit import bonAppetit

class TestBonAppetit(unittest.TestCase):

    def testDiferencia(self):
        self.assertEqual(bonAppetit(4, 1, 12 ,[3, 10, 2, 9]), 5)

    def testIgual(self):
        self.assertEqual(bonAppetit(4, 1, 7,[3, 10, 2, 9]), 'Bon Appetit')

if __name__ == "__main__":
    unittest.main()
