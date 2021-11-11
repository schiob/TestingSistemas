import unittest
from unittest.main import main
from numeros import numbers

class testNumber(unittest.TestCase):
    def test_1(self):
        input = numbers([51, -12, -3, 0, 2])
        expected = '2 positivos, 2 negativos, 3 pares, 2 impares'
        self.assertEqual(input, expected)

    def test_2(self):
        input = numbers([0, 1, 2, 3, 4])
        expected = '4 positivos, 0 negativos, 3 pares, 2 impares'
        self.assertEqual(input, expected)

    def test_3(self):
        input = numbers([-1, -2, -3])
        expected = '0 positivos, 3 negativos, 1 pares, 2 impares'
        self.assertEqual(input, expected)

    def test_4(self):
        input = numbers([0])
        expected = '0 positivos, 0 negativos, 1 pares, 0 impares'
        self.assertEqual(input, expected)

if __name__ == '__main__':
    unittest.main()