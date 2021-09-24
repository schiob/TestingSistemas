import unittest
from unittest.main import main
from practica2 import suma

class test(unittest.TestCase):
    def positive(self):
        self.assertEqual(suma(5,5), 10)

    def neg_and_pos(self):
        self.assertEqual(suma(-1,10), 9)

    def pos_and_neg(self):
        self.assertEqual(suma(5, -1), 4)

    def negative(self):
        self.assertEqual(suma(-5,-5), -10)

if __name__ == '__main__':
    unittest.main() 