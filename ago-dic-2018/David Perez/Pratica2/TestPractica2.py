#Test para la Práctica 2
import unittest
import Practica2Numeritos

class Test (unittest.TestCase):
    def test_numeritos(self):
        result=Practica2Numeritos.numeritos(4,[0,45,2,-3])
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 2)
        self.assertEqual(result[3], 2)
    def test_numeritos1(self):
        result=Practica2Numeritos.numeritos(5,[0,45,2,-3,-1])
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 2)
        self.assertEqual(result[3], 3)
if __name__ == '__main__':
    unittest.main()
