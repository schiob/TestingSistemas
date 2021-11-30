import unittest
from practica2 import sum

class TestPractica2(unittest.TestCase):
    def test_two_positive_floats(self):
        self.assertEqual(sum(1,1), 2.0)

    def test_negative_first_number(self):
        self.assertEqual(sum(-1,1), 0.0)

    def test_negative_second_number(self):
        self.assertEqual(sum(1,-1), 0.0)

    def test_two_negative_floats(self):
        self.assertEqual(sum(-1,-1), -2.0)

    def test_two_zeros(self):
        self.assertEqual(sum(0,0), 0.0)

if __name__ == '__main__':
    unittest.main()