import unittest
import Practica3Max

class Test3Max(unittest.TestCase):
    def triangular(self):
        res = Practica3Max.calc([1])
        self.assertEqual(res, 1)

    def triangular1(self):
        res = Practica3Max.calc([3])
        self.assertEqual(res, 6)

    def triangular2(self):
        res = Practica3Max.calc([4])
        self.assertEqual(res, 10)

    def triangular3(self):
        res = Practica3Max.calc([56])
        self.assertEqual(res, 1596)

    def triangular4(self):
        res = Practica3Max.calc([400])
        self.assertEqual(res, 80200)

if __name__ == '__main__':
    unittest.main()
