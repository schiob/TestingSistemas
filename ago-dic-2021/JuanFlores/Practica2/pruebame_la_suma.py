import unittest
from sumas import suma

class TestSumasMethods(unittest.TestCase):

    def test_suma(self):
        a, b = 4, 8
        self.assertEqual(suma(a,b), a+b)

    def test_suma_grandota(self):
        a, b = 125654652245541, 54168465164
        self.assertEqual(suma(a,b), a+b)

if __name__ == '__main__':
    unittest.main()