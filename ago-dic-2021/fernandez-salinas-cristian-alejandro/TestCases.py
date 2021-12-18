from logging import error
import unittest
from Practica2 import suma

class TestSuma(unittest.TestCase):
    def test_suma(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(actual,expected)

    def test_fracciones(self):
        actual = suma(1/3,2/3)
        expected = 1
        self.assertEqual(actual,expected)

    def test_puntoDecimal(self):
        actual = suma(0.2,1.4)
        expected = 1.6
        self.assertEqual(actual,expected)

    def test_stringNumeros(self):
        actual = suma('5','8')
        expected = 13
        self.assertEqual(actual,expected)