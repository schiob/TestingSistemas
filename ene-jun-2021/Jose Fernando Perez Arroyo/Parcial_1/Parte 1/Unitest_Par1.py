import unittest

from Parcial_1 import *
class DecoratorTest(unittest.TestCase):
    def test_numeros(self):
        test1= primeraparte(1)
        self.assertEqual(test1, 1)
    def test_numeros2(self):
        test1= primeraparte(3)
        self.assertEqual(test1, 6)
    def test_numeros3(self):
        test1= primeraparte(4)
        self.assertEqual(test1, 10)
    def test_numeros4(self):
        test1= primeraparte(56)
        self.assertEqual(test1, 1596)
    def test_numeros5(self):
        test1= primeraparte(400)
        self.assertEqual(test1, 80200)


if __name__ == "__main__":
    unittest.main()
