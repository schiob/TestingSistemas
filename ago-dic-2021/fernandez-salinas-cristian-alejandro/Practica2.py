import unittest

def suma (n1,n2):
    sum = int(n1) + int(n2)
    print(sum)
    return sum

class TestSuma(unittest.TestCase):
    def test_suma(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(actual,expected)

#suma('a','b')